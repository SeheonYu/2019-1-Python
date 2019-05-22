from selenium import webdriver
 
path = "Selenium\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://google.com/")

search_box = driver.find_element_by_name("q")
search_box.send_keys("셀레니움")
search_box.submit()