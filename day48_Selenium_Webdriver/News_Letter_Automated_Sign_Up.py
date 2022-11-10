from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/veechente/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# TODO: Type on webpage
first_name = driver.find_element(By.NAME, "fname")
first_name.send_keys("Vicente")
last_name = driver.find_element(By.NAME, "lname")
last_name.send_keys("Ceja")
email = driver.find_element(By.NAME, "email")
email.send_keys("veechente.py@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
