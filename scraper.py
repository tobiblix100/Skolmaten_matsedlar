import scraperwiki
import urllib
import lxml.html

def scrape_picsandname(new_root):
  histology = new_root.cssselect("div.thumb-image-box")
  for info in histology:
    imgs = info.cssselect("")

def scrape_content(linkurl):
  links = scrape_links
  for link in links:
    new_html = scraperwiki.scrape(link)
    new_root = lxml.html.fromstring(new_html)
    scrape_picsandname(new_root)

def scrape_urls(root):
  lan = root.cssselect("ul.links li")
  for lans in lan:
    lanken = lans.cssselect("ul li a")
    if lanken:
      nya_lanken = lanken.attrib.get("href")
      lan_url = base_url + nya_lanken
      print lan_url
      return lan_url
      
      
  

base_url = "http://www.skolmaten.se/"

def scrape_link(url):
  html = scraperwiki.scrape(url)
  root = lxml.html.fromstring(html)
  scrape_urls(root)

scrape_link(base_url)
