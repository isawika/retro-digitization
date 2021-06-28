#!/usr/bin/env python3
#
# conklin2xml.py - reformat an OCD'ed page of the Conklin Hanunoo-English dictionary 
#                  into XML suitable for uploading to Lexonomy
#

from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom.minidom import parseString
import sys
import re

posTags = {
    'noun': 'noun',
    'verb': 'verb',
    'adjective': 'adj',
    'adverb': 'adv',
    'pronoun': 'pron',
    'interjection': 'intj',
    'determiner': 'det',
    'adpositon': 'adp'  # preposition and postposition
}

def usage():
    print(f'\nusage: {sys.argv[0]} <conklin-OCR-text>\n')
    sys.exit(0)

def romanize(entry):
    """Remove the special symbols (glottal stop, diacritical marks) in the text"""
    mytrans = entry.maketrans('ÁÉÍÓÚáéíóúÀÈÌÒÙàèìòù', 'AEIOUaeiouAEIOUaeiou', 'ʔ')
    entry = entry.translate(mytrans)
    entry = entry.replace('ŋ', 'ng')
    return entry

def cleanup(text):
    """Remove any extraneous punctuation marks in the text"""
    if text.endswith('.') and \
        not text.endswith('..') and \
        not text.endswith('q.v.'):
        text = text[:-1]
    elif text.endswith('."'):
        text = f'{text[:-2]}"'
    if text.startswith('—'):
        text = text[1:]
    return text.strip()

def pageToXml(pagefile):
    """Parse the dictionary entries from an OCR'ed text page into XML"""
    xmlPage = Element('dictionary')
    xmlPageContainer = SubElement(xmlPage, 'entry')  # need to fake it
    xmlPageNumber = SubElement(xmlPageContainer, 'page')

    with open(pagefile) as fin:
        state = 'WHITESPACE'
        entry = ''
        definition = ''
        senseIndex = '1'
        pronounciations = []
        notes = []
        flags = []

        for line in fin:
            line = line.strip()
            if 'VOCABULARY' in line:
                pagenum = line.split()[1]
                xmlPageNumber.text = pagenum
            elif 'UNIVERSITY OF CALIFORNIA PUBLICATIONS' in line:
                pagenum = line.split()[0]
                xmlPageNumber.text = pagenum
            elif line.isdigit():
                continue  # disregard Page number since we extract it from filename
            elif line == '':
                if state != 'WHITESPACE':
                    xmlEntry = SubElement(xmlPageContainer, 'word-entry')
                    xmlHeadword = SubElement(xmlEntry, 'headword')
                    xmlHeadword.text = entry
                    xmlHeadword.set('xml:lang', 'hnn')
                    xmlPronounce = SubElement(xmlEntry, 'pronounce')
                    xmlPronounce.text = ', '.join(pronounciations)
                    xmlPronounce.set('xml:lang', 'hnn')
                    xmlSense = SubElement(xmlEntry, 'sense')
                    xmlSenseIndex = SubElement(xmlSense, 'index')
                    xmlSenseIndex.text = senseIndex
                    if flags:
                        xmlFlags = SubElement(xmlSense, 'flag')
                        xmlFlags.text = ', '.join(flags)

                    hyperlinks = []
                    cf = None
                    synonym = None
                    origin = None
                    seeThisTerm = None
                    senseIndex = '1'
                    for pattern in ('Cf.', 'cf.', '(=', '(<', '. See also ', '. See '):
                        idx = definition.find(pattern)
                        if idx != -1:
                            hyperlinks.append([idx, pattern])
                    hyperlinks.sort()
                    while hyperlinks:
                        idx, pattern = hyperlinks.pop()
                        text = cleanup(definition[idx + len(pattern):])
                        if text.endswith(', q.v.)'):
                            text = cleanup(text[:-7])
                        if pattern == 'Cf.' or pattern == 'cf.':
                            cf = text
                        elif pattern == '(=':
                            synonym = text
                        elif pattern == '(<':
                            origin = text
                        elif pattern == '. See also ' or pattern == '. See ':
                            seeThisTerm = text
                        else:
                            raise Exception(f'No rule to handle the pattern /{pattern}/')
                        definition = cleanup(definition[:idx])

                    xmlDef = SubElement(xmlSense, 'def')
                    xmlDef.text = cleanup(definition)
                    if seeThisTerm:
                        xmlSee = SubElement(xmlSense, 'see')
                        xmlSee.text = seeThisTerm
                    if synonym:
                        xmlSynonym = SubElement(xmlSense, 'synonym')
                        xmlSynonym.text = synonym
                    if origin:
                        xmlOrigin = SubElement(xmlSense, 'origin')
                        xmlOrigin.text = origin
                    if cf:
                        xmlCf = SubElement(xmlSense, 'cf')
                        xmlCf.text = cf
                    for note in notes:
                        xmlUsage = SubElement(xmlSense, 'usage')
                        tokens = note.split()
                        specialChars = '[ʔÁÉÍÓÚáéíóúÀÈÌÒÙàèìòù]'
                        if re.search(specialChars, tokens[0]):
                            #xmlUsageHeadword = SubElement(xmlUsage, 'headword')
                            #xmlUsageHeadword.text = romanize(tokens[0])
                            xmlUsagePronounce = SubElement(xmlUsage, 'pronounce')
                            xmlUsagePronounce.text = tokens[0]
                            xmlUsageExample = SubElement(xmlUsage, 'example')
                            xmlUsageExample.text = ' '.join(tokens[1:])
                        else:
                            xmlUsageExample = SubElement(xmlUsage, 'example')
                            xmlUsageExample.text = note
                    
                    state = 'WHITESPACE'
                    entry = ''
                    definition = ''
                    pronounciations = []    
                    notes = []
                    flags = []
                continue
            elif state == 'DEF':
                definition += f" {line}"  # cleanup after all text has been concatenated
            elif state == 'NOTE':
                notes.append(cleanup(line))
            else:
                if line.startswith('+'):
                    line = line[1:]
                    flags.append('+')
                tokens = line.split()

                # Romanize the entry term. Up to 3 sequential Hanunoo words can comprise it.
                specialChars = '[ʔÁÉÍÓÚáéíóúÀÈÌÒÙàèìòù]'
                if len(tokens) > 3 and \
                    not tokens[0].endswith(',') and \
                    re.search(specialChars, tokens[1]) and \
                    re.search(specialChars, tokens[2]):
                        entry = ' '.join(tokens[0:3])
                        pronounciations = [entry]
                        tokens = tokens[3:]
                elif len(tokens) > 2 and \
                    not tokens[0].endswith(',') and \
                    re.search(specialChars, tokens[1]):
                        entry = ' '.join(tokens[0:2])
                        pronounciations = [entry]
                        tokens = tokens[2:]
                else:
                    entry = tokens[0]
                    # Hack: assume only single-word entries can have 2+ pronounciations
                    while tokens[0].endswith(','):
                        pronounciations.append(tokens.pop(0)[:-1])
                    pronounciations.append(tokens.pop(0))

                entry = romanize(entry)
                if entry.endswith(','):
                    entry = entry[:-1]

                # Parse the sense index: eg. (1), (2)
                if tokens[0].startswith('(') and tokens[0].endswith(')') and tokens[0][1:-1].isdigit():
                    senseIndex = tokens.pop(0)[1:-1]
                
                # Parse other flags such as: Z, S
                if re.match('^[\[\(](.+)[\]\)]$', tokens[0]):  # flags enclosed in [] or ()
                    flags.append(tokens.pop(0)[1:-1])
                elif re.match('^[\[\(]', tokens[0]):
                    flags.append(tokens.pop(0)[1:].replace(',', ''))
                    while tokens and not re.match('(.+)[\]\)]$', tokens[0]):
                        flags.append(tokens.pop(0).replace(',', ''))
                    if tokens:
                        flags.append(tokens.pop(0)[:-1])

                definition = ' '.join(tokens)
                if definition.endswith('.'):  # next line is not a defn anymore
                    state = 'NOTE'
                else:
                    state = 'DEF'
    
    return xmlPage

def formatXml(elem, prettify=False):
    """Return a pretty-printed XML string for the Element"""
    rough_string = tostring(elem, 'utf-8')
    reparsed = parseString(rough_string)
    if prettify:
        return reparsed.toprettyxml(indent="  ")
    return reparsed.toxml()

def main(prettify=False):
    for fname in sys.argv[1:]:
        xml = pageToXml(pagefile=fname)
        xmlString = formatXml(xml, prettify)
        print(xmlString)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    main(True)