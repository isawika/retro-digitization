<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="entry">
    <div class='myEntry'><xsl:apply-templates/></div>
  </xsl:template>
  <xsl:template match="word-entry">
    <p><div class='myWordEntry'><xsl:apply-templates/></div></p>
  </xsl:template>
  <xsl:template match="headword">
    <span class='myHeadword'><xsl:apply-templates/></span>
  </xsl:template>
  <xsl:template match="word-entry/pronounce">
    <span class='myPronounce'><xsl:apply-templates/></span>
  </xsl:template>
  <xsl:template match="flag">
    <span class='myFlag'>[<xsl:apply-templates/>]</span>
  </xsl:template>

  <xsl:template match="sense">
          <span class='mySense'><xsl:apply-templates/></span>
  </xsl:template>
  <xsl:template match="index">
      <div class="bulleted">
        <div class="bullet">    
           <span class="mySenseIndex numberingSymbol"><xsl:apply-templates/></span>
        </div>
      </div>
  </xsl:template>
  <xsl:template match="def">
        <span class='myDefinition'><xsl:apply-templates/></span>
   </xsl:template> 
  <xsl:template match="synonym">
        <div class="indented"><span class='mySynonym'>Synonym</span><xsl:apply-templates/></div>
   </xsl:template>
  <xsl:template match="origin">
        <div class="indented"><span class='myOrigin'>Origin</span><xsl:apply-templates/></div>
   </xsl:template> 
  <xsl:template match="cf">
        <div class="indented"><span class='myCf'>Cf</span><xsl:apply-templates/></div>
   </xsl:template> 
  <xsl:template match="see">
        <div class="indented"><span class='mySeeAlso'>See</span><xsl:apply-templates/></div>
   </xsl:template>
  <xsl:template match="note">
        <div class="indented"><span class='myNote'>Note</span><xsl:apply-templates/></div>
   </xsl:template> 
  <xsl:template match="usage">
        <div class="indented"><span class='myUsage'>Usage</span><xsl:apply-templates/></div>
   </xsl:template> 
  <xsl:template match="usage/pronounce">
        <span class='myUsagePronounce'><xsl:apply-templates/></span>
   </xsl:template> 
  <xsl:template match="usage/example">
        <span class='myExample'><xsl:apply-templates/></span>
   </xsl:template> 
</xsl:stylesheet>