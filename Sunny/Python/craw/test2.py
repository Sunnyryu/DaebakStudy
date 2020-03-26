from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr = "id"
pwd = "password"

path = "WebDriver의 경로"
driver = webdriver.Chrome(path)
driver.get("http://www.facebook.org")
assert "Facebook" in driver.title
# driver.title이 Facebook 이 아니면 예외처리를 함
sunny = driver.find_element_by_id("email")
#위에서 분석한 아이디 입력란의 id를 찾아서 커서를 둠
sunny.send_keys(usr)
#usr에 입력한 페이스북 아이디 값을 현재 커서가 위치한 곳에 넣음
sunny = driver.find_element_by_id("pass")
#위에서 분석한 패스워드 입력란의 id를 찾아서 커서를 둠
sunny.send_keys(pwd)
#pwd에 입력한 페이스북 패스워드 값을 현재 커서가 위치한 곳에 넣음
sunny.send_keys(Keys.RETURN)
#Enter키를 누르게 함
