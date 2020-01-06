import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://www.amazon.com/s?k=graphic+card&ref=nb_sb_noss_2")
soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find('div', class_='s-result-list')
resultList = content.find_all('div', class_='s-result-item')

with open('output.csv', mode='w', newline='') as outputFile:
    amazon_prices = csv.writer(outputFile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    amazon_prices.writerow(['Name', 'Price', 'Currency', 'Stars', 'Number of Ratings'])

    for result in resultList:
        title = result.find('h2').text.strip()
        stars = result.find('div', class_='a-row a-size-small').find_all('span')[0].text.strip()[:3]
        numberRatings = result.find('div', class_='a-row a-size-small').find_all('span')[3].text.strip()
        prices = result.find('span', class_='a-price').find('span', class_='a-offscreen').text.strip()
        currency = prices[:1]
        price = prices[1:]
        amazon_prices.writerow([title, price, currency, stars, numberRatings])
