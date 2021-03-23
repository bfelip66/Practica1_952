import requests
import io
from bs4 import BeautifulSoup

web = 'https://analisi.transparenciacatalunya.cat/Salut/Registre-de-casos-de-COVID-19-realitzats-a-Catalun/jj6z-iyrp/data'
web_paginacio = 'https://analisi.transparenciacatalunya.cat/api/id/jj6z-iyrp.json?$query=select%20*%2C%20%3Aid%20offset%20200%20limit%20100'

def get_web_content(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.prettify()


# Dades web
fixed_html = get_web_content(web)

with io.open('web.html', "w", encoding="utf-8") as f:
    f.write(fixed_html)
f.close()
print("Webpage downloaded to web.html")


# Dades paginació
offset = 20200

for i in range(10):
    fixed_html2 = get_web_content(web_paginacio)
    with io.open('dades_paginacio.html', "a", encoding="utf-8") as f2:
        f2.write(fixed_html2)
    f.close()
    print("Webpage downloaded to dades_paginacio.html, iteration: {}".format(i))

    web_paginacio.replace(str(offset), str(offset+100))
    offset += 100



"""
head_tag = soup.head
print("head tag: ".format(child))

title_tag = head_tag.contents[0]

for child in title_tag.children:
    print("children: ".format(child))
"""