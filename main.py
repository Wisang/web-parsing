from bs4 import BeautifulSoup

import requests

response = requests.get("https://www.ycombinator.com/people/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

print(soup.find(name="a").get("href"))
