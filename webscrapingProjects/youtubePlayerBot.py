from selenium import webdriver 
import time
driver = webdriver.Chrome()

#allows user to choose what topic they want the youtube video chain to be about
topic = input("What videos would you like to watch: ")

#allowed user to choose when the youtuber browser will close
timer = input("Sleep timer length (minutes): ")
time.sleep(1)

#searches the youtube video based on user's topic
driver.get("https://www.youtube.com/results?search_query="+topic)
time.sleep(2)

#selects the first video found
button = driver.find_element_by_id("video-title")
button.click()
time.sleep(1)

#checks if Autoplay is selected 
#wants Autoplay to be on so that there will be a video chain
"""
toggle = driver.find_element_by_id("toggle")
if toggle.is_selected():
    print("Autoplay is ON.")
else:
    print("Autoplay is now ON.")
"""
#timer is on after youtube playlist/chain is started
x = int(timer)*60
while x > 0:
    try:
        #looks for the 'skip ad' button
        skip = driver.find_element_by_class_name('ytp-ad-skip-button-container')
        skip.click()
    except:
        pass
    time.sleep(1)
    x = x-1

driver.close()