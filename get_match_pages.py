#coding: utf8 
from selenium import webdriver

browser = webdriver.Firefox()
#for i in range( 1006000, 1006095 ):
#for i in range( 959880, 959890 ):
#for i in [ 1035323, 1058726, 969779, 985755 ]: 
for i in [ 866178 ]: 
  browser.get( 'https://www.whoscored.com/Matches/%d/Live' % i )
  with open( 'original_pages/page_%d' % i, 'w' ) as text_file:
    text_file.write( browser.page_source.encode( 'utf-8' ) )
browser.close()
