from selenium import webdriver

chrome_drover_path = "/Users/veechente/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_drover_path)

# TODO: Pull price from Amazon
# driver.get("https://www.amazon.com/Ascent-Native-Fuel-Protein-Powder/dp/B01MZD6VN0/ref=sr_1_1_sspa?crid=12O66AMJ783U6&keywords=whey+protein&qid=1668051482&sprefix=whey+%2Caps%2C639&sr=8-1-spons&psc=1&smid=A3782EXB865CBV")
# price = driver.find_element(By.ID, "sns-base-price")
# print(price.text)

driver.get("https://www.python.org")
search_bar = driver.find_element(by.NAME, "q")
print(search_bar)


driver.quit()       # Closes entire browser
