import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.regionofwaterloo.ca/en/health-and-wellness/positive-cases-in-waterloo-region.aspx")
#print(page)
#print(page.status_code)
#print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
[type(item) for item in list(soup.children)]