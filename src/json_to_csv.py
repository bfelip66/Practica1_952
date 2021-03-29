import pandas as pd

try:
    df = pd.read_json(r'../scraping/dades_paginacio.json')
except:
    print("Error opening file")

try:
    df.to_csv(r'../scraping/dades_paginacio.csv', index = None)
    print("csv created")
except:
    print("Error creating csv")