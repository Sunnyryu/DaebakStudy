from selenium import webdriver

#path = "/home/sunny/DaebakStudy/Sunny/Python/craw/chrome/chromedriver"
path = "./chrome/chromedriver"
driver = webdriver.Chrome(path)
driver.get("http://google.com/")
search_box = driver.find_element_by_name("q")
search_box.send_keys("sunny")
search_box.submit()
