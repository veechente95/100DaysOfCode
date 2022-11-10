from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_drover_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(executable_path=chrome_drover_path)

# TODO: Pull price from Amazon by ID
# driver.get("https://www.amazon.com/Ascent-Native-Fuel-Protein-Powder/dp/B01MZD6VN0/ref=sr_1_1_sspa?crid=12O66AMJ783U6&keywords=whey+protein&qid=1668051482&sprefix=whey+%2Caps%2C639&sr=8-1-spons&psc=1&smid=A3782EXB865CBV")
# price = driver.find_element(By.ID, "sns-base-price")
# print(price.text)

#TODO: Pull by NAME, CLASS_NAME, and CSS_SELECTOR
driver.get("https://www.python.org")
search_bar = driver.find_element(By.NAME, "q")
logo = driver.find_element(By.CLASS_NAME, "python-logo")
documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# Get a hold of a link (Ex Submit Website Bug
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

print(search_bar.tag_name)                      # input
print(search_bar.get_attribute("placeholder"))  # Search
print(logo.size)                                # {'height': 82, 'width': 290}
print(documentation_link.text)                  # docs.python.org
print(bug_link.text)                            # Submit Website Bug


driver.quit()       # Closes entire browser
