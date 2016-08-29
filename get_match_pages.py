#coding: utf8 
from selenium import webdriver

browser = webdriver.PhantomJS()
my_ranges = []
#my_ranges.append( ( 985000, 986000 ) ) # Liga 2015-2016
#my_ranges.append( ( 1005000, 1006400 ) ) # Serie A 2015-2016
#my_ranges.append( ( 958400, 959000 ) ) # Premier League 2015-2016
#my_ranges.append( ( 406000, 1007000 ) ) # All
my_ranges.append( ( 406000, 407000 ) ) # All
for my_range in my_ranges:
  for Id in range( my_range[ 0 ], my_range[ 1 ] ): 
    print 'Checking %d' % Id
    browser.get( 'https://www.whoscored.com/Matches/%d/Live' % Id )
    with open( 'original_pages/page_%d' % Id, 'w' ) as text_file:
      text_file.write( browser.page_source.encode( 'utf-8' ) )
browser.close()
