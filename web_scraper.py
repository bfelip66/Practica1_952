import requests
from bs4 import BeautifulSoup

web = 'https://www.who.int/data/gho/data/indicators/indicator-details/GHO/ambient-air-pollution-attributable-deaths'

page = requests.get(web)
http_code = page.status_code

soup = BeautifulSoup(page.content, 'html.parser')
fixed_html = soup.prettify()

def download_content():
    my_data_file = open('web.html', 'w')
    my_data_file.write(fixed_html)
    my_data_file.close()
    print("Webpage downloaded to web.html")

"""
head_tag = soup.head
print("head tag: ".format(child))

title_tag = head_tag.contents[0]

for child in title_tag.children:
    print("children: ".format(child))
"""