# Set up my Python project with all necessary imports and drivers to utilize Selenium for web scraping.
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv

file = open("scraped_quotes.csv", "w", newline="")
writer = csv.writer(file)

### The data points to grab for each laptop will be name, price, specifications, and number of reviews.
writer.writerow(["ID ", "Name ", "Price ", "Specifications ", "Number of Reviews "])

### Scrape data from the given website, getting laptop information from all 20 pages of data by handling pagination.
### Write code that will store each laptop I scrape inside a Python List.
browser_driver = Service("chromedriver")
scraper = webdriver.Chrome(service=browser_driver)
scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=1")

index = 1
while True:
	computer_thumbnails = scraper.find_element(By.CLASS_NAME, "title")
	for card in computer_thumbnails:
		computer_names = card.find("a", attrs={"class": "title"})["title"]
		computer_prices = card.find(attrs={"class": "pull-right price"}).text
		computer_specifications = card.find(attrs={"class": "description"}).text
		number_of_reviews = card.find("p", attrs={"class": "pull-right"}).text
		
		writer.writerow([index, computer_names, computer_prices, computer_specifications, number_of_reviews])
		index += 1

		try:
			element = scraper.find_elements(By.PARTIAL_LINK_TEXT, "›")
			element.click()
		except NoSuchElementException:
			break

### Clean and format my data so that all of my data is free of any duplicates, null values, and other anomalies, then write the data to a CSV file and include a UNIQUE ID number for each row.
file.close()
# for card in computer_thumbnails:
# index = 0
# for row in reader:
#     row['ID'] = index
#     writer.write(row)
#     index += 1