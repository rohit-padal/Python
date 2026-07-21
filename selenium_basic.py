from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://youtube.com")
print("First Tab: ",driver.title)
time.sleep(3)

driver.switch_to.new_window('tab')
driver.get("https://github.com")
print("Second Tab: ",driver.title)
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.close()

input("Enter any key to exit!")
driver.quit()
