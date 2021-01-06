from selenium import webdriver 
import bs4
import time
driver = webdriver.Chrome()
driver.get("https://www.windermere.com/search#sold_days=30&status=both&ptype_tmp=7&ls_conversion=acres&location_search_field=Seattle%20Metropolitan%20Area%2C%20WA%2C%20USA&drive_time=09%3A00&drive_duration=15&drive_avoid_ferry=1&drive_departure=1&ss_description=Seattle%20Metropolitan%20Area%2C%20WA&ss_email_freq=40&ss_send_zero_result=1&bounds_north=48.67205620746167&bounds_east=-120.41039986710716&bounds_south=46.167611157736445&bounds_west=-123.19481613289285&center_lat=47.6061031&center_lon=-122.3320534&center_lat_pan=47.434730243976766&center_lon_pan=-121.802608&geotype=AdminDivision2&user_lat=47.6061031&user_lon=-122.3320534&pgsize=20&startidx=0&zoom=8&sort_by=10&company_uuid=1234567&commute=0&buffer_miles=0&geospatial=true&ptype=1%2C2%2C3%2C4%2C5%2C7%2C9&searchType=criteria&pstatus=1%2C2%2C11&omit_hidden=true")
time.sleep(30) #loading time

scrolls = 1000
while scrolls > 0:
    driver.execute_script("document.getElementById('picklist-container').scrollTop+=10000;") #scrolling code
    time.sleep(0.1) #loading time
    scrolls -= 1

soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
results = soup.find_all("div", {"class":"pull-left property-address-container"})
res = []
for result in results:
    txt = result.text
    txt = txt.replace("\n", "")
    res.append(txt)
print(res)