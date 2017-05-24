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
  lan = root.cssselect("ul.links")
  lanken = lan[1].cssselect("li")
  nya_lanken = lanken.cssselect("ul li")
  for lankar in nya_lanken:
      lanet = lankar.attrib.get("href")
      lan_url = base_url+lanet
      print lan_url
      return lan_url
      
      
  

base_url = "http://www.skolmaten.se/"

def scrape_link(url):
  html = scraperwiki.scrape(url)
  root = lxml.html.fromstring(html)
  scrape_urls(root)

scrape_link(base_url)
