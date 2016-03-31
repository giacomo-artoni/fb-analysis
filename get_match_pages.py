#coding: utf8 
from selenium import webdriver

browser = webdriver.Firefox()
for i in range( 1006000, 1006095 ):
  browser.get( 'https://www.whoscored.com/Matches/%d/Live' % i )
  with open( 'original_pages/page_%d' % i, 'w' ) as text_file:
    text_file.write( browser.page_source.encode( 'utf-8' ) )
