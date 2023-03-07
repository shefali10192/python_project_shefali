from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\112552\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("https://www.selenium.dev/")
print(driver.title)