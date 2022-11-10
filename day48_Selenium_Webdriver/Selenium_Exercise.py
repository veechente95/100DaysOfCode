from selenium import webdriver
from selenium.webdriver.common.by import By

#TODO: Extract upcoming events from python.org website and put them in a nested dict
chrome_drover_path = "/Users/veechente/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_drover_path)
driver.get("https://www.python.org")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# for time in event_times:
#     print(time.text)

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.quit()