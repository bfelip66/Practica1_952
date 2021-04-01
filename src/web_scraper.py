import requests
import io
from bs4 import BeautifulSoup
from selenium import webdriver

#region Global variables
web = 'https://analisi.transparenciacatalunya.cat/Salut/Registre-de-casos-de-COVID-19-realitzats-a-Catalun/jj6z-iyrp/data'
web_paginacio = 'https://analisi.transparenciacatalunya.cat/api/id/jj6z-iyrp.json?$query=select%20*%2C%20%3Aid%20offset%20200%20limit%20100'
fitxer_web = "../scraping/web.html"
fitxer_dades = '../scraping/dades_paginacio.json'
driver_location = "C:/Users/vicen/Downloads/chromedriver.exe"
#endregion

"""
Starts webdriver
"""
driver = webdriver.Chrome(driver_location)
driver.get(web)

#region Private functions
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
    try:
        with io.open(filename, mode, encoding="utf-8") as f:
            f.write(content)
        f.close()
    except:
        print("Error with file: {}".format(filename))
#endregion

#region Webdriver functions
"""
Extract data using web driver
"""
def get_first_rows(nrows):
    """
    Returns first n rows
    """
    if nrows > 0:
        for r in range(1, nrows + 1):
            el_list = []
            for i in range(1, 12):
                element = driver.find_element_by_xpath("//div[@class='socrata-table frozen-columns']/table/tbody/tr["+ str(r) +"]/td["+ str(i) +"]/div").text
                el_list.append(element)
            print(el_list)
    else:
        print("El valor ha de ser mínim 1")

def get_column(n, column):
    """
    Return first n registers of selected column
    """
    if column > 0 and column < 12:
        if n > 0:
            for i in range(1, n + 1):
                table = driver.find_element_by_xpath("//div[@class='socrata-table frozen-columns']/table/tbody/tr["+ str(i) +"]/td["+ str(column) +"]/div").text
                print(table)
        else:
            print("El valor ha de ser mínim 1")
    else:
        print("El valor ha d'estar entre 1 i 11")
#endregion

#region Download content
def download_web():
    """
    Save web content to file web.html
    """
    fixed_html = get_web_content(web)
    write_to_file(fixed_html, fitxer_web, 'w')
    print("Webpage downloaded to web.html")

# download_web()

def download_data(npages):
    """
    Save n pages of content to file dades_paginacio.json
    """
    if npages > 0:
        url_web = web_paginacio
        offset = 20200
        max_offset = offset + (npages * 100) - 100

        try:
            fixed_html = get_web_content(url_web)
            print("Data downloaded to dades_paginacio.json, offset: {}".format(offset))
            if offset < max_offset:
                fixed_html = fixed_html.replace(']', ',')

            write_to_file(fixed_html, fitxer_dades, 'w')

            while offset < max_offset:
                #Descarreguem els següents 100 resultats
                url_web = url_web.replace(str(offset), str(offset + 100))
                offset += 100
                fixed_html = get_web_content(url_web)
                print("Data downloaded to dades_paginacio.json, offset: {}".format(offset))
                fixed_html = fixed_html.replace('[', '')

                if offset < max_offset:
                    fixed_html = fixed_html.replace(']', ',')
                    write_to_file(fixed_html, fitxer_dades, 'a')
                else:
                    write_to_file(fixed_html, fitxer_dades, 'a')
                    break

        except Exception as e:
            print(e)

    else:
        print("El valor ha de ser mínim 1")

# download_data(3)
#endregion