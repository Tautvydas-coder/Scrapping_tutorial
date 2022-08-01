from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.service import Service

CHROME_DRIVER_PATH = "C:/Users/takvietk/Downloads/Programos/chromedriver_win32_103/chromedriver"
ser = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=ser)
driver.get('https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW')

# Scraping Movie Names
movies_names = driver.find_elements(By.XPATH,
                                    '//td[@class="a-text-left mojo-field-type-title"]/a[@class="a-link-normal"]')  # targets all the elements on the web that has same Xpath
movie_name_list = []  # an empty list for storing movie names
for movie in range(len(movies_names)):  # a loop that runs until the length of movies_name list
    movie_name_list.append(
        movies_names[movie].text)  # extracting text from the movie name and appending it on the movies name list
# print(movie_name_list)

# Scraping Movies Lifetime Grossings
lifetime_gross = driver.find_elements(By.XPATH, '//td[@class="a-text-right mojo-field-type-money"]')
lifetime_gross_list = []
for gross in range(len(lifetime_gross)):
    lifetime_gross_list.append(lifetime_gross[gross].text)
# print(lifetime_gross_list)


# Scraping Movies Release Date
release_year = driver.find_elements(By.XPATH,
                                    '//td[@class="a-text-left mojo-field-type-year"]/a[@class="a-link-normal"]')
release_year_list = []
for year in range(len(release_year)):
    release_year_list.append(release_year[year].text)
# print(release_year_list)

data = list(zip(movie_name_list, release_year_list, lifetime_gross_list))
# dataset name
df = pd.DataFrame(data, columns=['Movie Name', 'Release Date', 'Lifetime Earnings'])
# columns names
df.to_csv('top_200_movies_with_lifetime_gross.csv', index=False)
