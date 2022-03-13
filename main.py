from bs4 import BeautifulSoup

with open("website.html", encoding="UTF8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.find_all(name="a")[1])
