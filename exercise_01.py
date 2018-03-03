from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ureq

target_url = "https://www.youtube.com/watch?v=XQgXKtPSzUI"

uClient = ureq(target_url)
html = uClient.read()
uClient.close()

page_soup = bs(html, "html.parser")

print(page_soup.body)