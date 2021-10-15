# coding : utf-8

"""
    Tableau général des matchs de l’équipe de France de football
    Data source: https://www.chroniquesbleues.fr/Tableau-general-des-matchs-de
"""

import time

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.chroniquesbleues.fr/Tableau-general-des-matchs-de"
DATA = "matchs-equipe-de-france.csv"

def main():
    """
        1. Open browser and go to `URL`
        2. Extract the page source code
        3. Restrict to table balise
        4. Transform into Pandas DataFrame and save table
    """
    print("==== START ====")
    browser = webdriver.Firefox()
    # Got to URL
    print(f"Go to {URL} ...")
    browser.get(URL)
    time.sleep(10)

    # Retreive source code
    source = browser.page_source
    browser.close()

    # Convert into bs4 object
    soup = BeautifulSoup(source, "html.parser")

    # Extract table
    table = soup.find_all("table")[-1]
    # Convert into Pandas DataFrame
    data = pd.read_html(str(table))[0]
    data = data[["#", "Genre", "Date", "Ville", "Adversaire", "score"]]
    print(data.head(10))

    # Save raw data
    data.to_csv(DATA, index=False)  
    print("==== END ====")

if __name__ == "__main__":
    main()
