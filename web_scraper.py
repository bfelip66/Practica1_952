import requests
import io
from bs4 import BeautifulSoup

MAX_OFFSET = 20300
web = 'https://analisi.transparenciacatalunya.cat/Salut/Registre-de-casos-de-COVID-19-realitzats-a-Catalun/jj6z-iyrp/data'
web_paginacio = 'https://analisi.transparenciacatalunya.cat/api/id/jj6z-iyrp.json?$query=select%20*%2C%20%3Aid%20offset%20200%20limit%20100'


def get_web_content(url):
    """
    Return web content from url
    """
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.prettify()

def write_to_file(content, filename, mode):
    """
    Write content to file
    """
    with io.open(filename, mode, encoding="utf-8") as f:
        f.write(content)
    f.close()

# Dades web
def download_web():
    """
    Save web content to file web.html
    """
    try:
        fixed_html = get_web_content(web)
        write_to_file(fixed_html, 'web.html', 'w')
        print("Webpage downloaded to web.html")

    except:
        print("Ivalid url: {}".format(web))


# Dades paginació
def download_data():
    """
    Save paging content to file dades_paginacio.html
    """

    offset = 20200
    next_page = True
    try:
        fixed_html = get_web_content(web_paginacio)
        print("Data downloaded to dades_paginacio.json, offset: {}".format(offset))
        fixed_html = fixed_html.replace(']', ',')
        write_to_file(fixed_html, 'dades_paginacio.json', 'a')

        # while len(fixed_html2[:-3]) > 0:
        while next_page:
            #Descarreguem els següents 100 resultats
            web_paginacio.replace(str(offset), str(offset + 100))
            offset += 100
            fixed_html = get_web_content(web_paginacio)
            print("Data downloaded to dades_paginacio.json, offset: {}".format(offset))
            fixed_html = fixed_html.replace('[', '')

            if offset < MAX_OFFSET:
                fixed_html = fixed_html.replace(']', ',')
            else:
                next_page = False

            write_to_file(fixed_html, 'dades_paginacio.json', 'a')

    except:
        print("Ivalid url: {}".format(web_paginacio))


def navigate_tags():
    """
    Navigate for tags structure
    """
    page = requests.get(web)
    soup = BeautifulSoup(page.content, 'html.parser')
    web_cont = soup.prettify()

    head_tag = soup.head
    print("head tag: ".format(head_tag))

    # title_tag = head_tag.contents[0]

    a_tag = soup.find_all('a')
    # No se que fer ni com navegar per a_tag
    print("a_tag: {}".format(a_tag))

navigate_tags()