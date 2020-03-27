from selenium import webdriver

#path = "/home/sunny/DaebakStudy/Sunny/Python/craw/chrome/chromedriver"
path = "./chrome/chromedriver"
a= input()
driver = webdriver.Chrome(path)
driver.get("http://google.com/")
search_box = driver.find_element_by_name("q")
search_box.send_keys(a)
search_box.submit()
