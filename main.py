import requests
from bs4 import BeautifulSoup

url = "https://www.instagram.com/reel/CizKsS8JvKp/"

req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

# print(soup.prettify())
# print(soup.get_text())

# comments = soup.find_all("span")
# print(comments)

print(soup.find_all("span", class_="_aacl _aaco _aacu _aacx _aad7 _aade").get_text())
