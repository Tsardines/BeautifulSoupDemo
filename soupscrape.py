from urllib.request import urlopen as uReq # grabs page itself
from bs4 import BeautifulSoup as soup # parses html text

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+cards'

 # opens connection, grabs the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# does the html parsing
page_soup = soup(page_html, "html.parser") # calling it "soup" is standard
