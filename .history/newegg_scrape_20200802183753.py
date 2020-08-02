from urllib.request import urlopen as uReq # grabs page itself
from bs4 import BeautifulSoup as soup # parses html text

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+cards'

# opens connection, grabs the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# does the html parsing
page_soup = soup(page_html, "html.parser") # calling it "soup" is standard

# grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})    

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip() # strip removes excess whitespace

    print("brand:" + brand)
    print("product_name:" + product_name)
    print("shipping:" + shipping)


