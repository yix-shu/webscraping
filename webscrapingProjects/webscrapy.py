import requests
import bs4
from selenium import webdriver
import time
import matplotlib.pyplot as plt

thread = input("Search up a reddit thread topic: ")
driver=webdriver.Chrome()
driver.get("https://www.reddit.com/r/" + thread + "/new/")

SCROLL_PAUSE_TIME = 0.01

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

x = 1000
while (x>0):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    x -= 1
'''
url = 'https://www.reddit.com/r/depression/new/'
headers = {'User-Agent': 'Mozilla/5.0'}

page = requests.get(url, headers = headers)
'''
soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
#print(soup)
results = soup.find_all("a", {"data-click-id" : "timestamp"})
#results = soup.find_all("div")
print(results)
for result in results:
    print(result.text)


plt.plot(results, results)