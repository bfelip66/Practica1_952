import pandas as pd

try:
    df = pd.read_json(r'../scraping/dades_paginacio.json')
    try:
        df.to_csv(r'../scraping/dades_paginacio.csv', index = None)
        print("csv created")
    except Exception as e:
        print(e)
except Exception as e:
    print(e)