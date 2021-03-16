import requests
from bs4 import BeautifulSoup


URL = 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xnumnuts=2105'

# hlavni ridici funkce
def main() -> None:
    pass



# funkce scrapovani
def scraper():
    response = requests.get(URL)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    tabulka = soup.find("div", {'class': "t2_470"})
    radky = tabulka.find_all('tr')
    nevim = radky.find('td')
    return radky





# funkce zapisovani do souboru csv


print(scraper())

if __name__ == '__main__':
    main()

