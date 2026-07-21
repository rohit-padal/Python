from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url="https://github.com/rohit-padal"

driver.get(url)
repo_name=driver.find_element(By.CLASS_NAME, "repo").text

url = url + f"/{repo_name}"

driver.get(url)

file_names = driver.find_elements(By.CSS_SELECTOR, "a.Link--primary")[1].text    

url = url + f"/blob/main/{file_names}"



driver.get(url)
# raw = driver.find_element(By.CSS_SELECTOR, "a[data-testid='raw-button']")
# raw_link=raw.get_attribute("href")
# driver.get(raw_link)


if "password" in driver.page_source:
    print("Found")
else:
    print("Not Found")

input("Click any key to exit!")
driver.quit()