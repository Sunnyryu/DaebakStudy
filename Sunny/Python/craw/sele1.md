## Selenium Rewind

```

Locating one element

driver.find_element_by_id("cheese")

cheese = driver.find_element_by_id("cheese")
cheddar = cheese.find_elements_by_id("cheddar")

cheddar = driver.find_element_by_css_selector("#cheese #cheddar")

mucho_cheese = driver.find_elements_by_css_selector("#cheese li")

class name: 클래스 이름에 검색 값이 포함된 요소를 찾습니다(복합 클래스 이름은 허용되지 않음).
css selector: CSS선택기와 일치하는 요소를 찾습니다.
id: ID특성이 검색 값과 일치하는 요소를 찾습니다.
name: NAME특성이 검색 값과 일치하는 요소를 찾습니다.
link text: 표시 가능한 텍스트가 검색 값과 일치하는 앵커 요소를 찾습니다.
partial link text : 표시 가능한 텍스트가 검색 값과 일치하는 앵커 요소를 찾습니다.
tag name: 태그 이름이 검색 값과 일치하는 요소를 찾습니다.
xpath : XPath식과 일치하는 요소를 찾습니다.

name = "Charles"
driver.find_element_by_name("name").send_keys(name)

source = driver.find_element_by_id("source")
target = driver.find_element_by_id("target")
ActionChains(driver).drag_and_drop(source, target).perform()
(일부 웹 응용 프로그램에서는 JavaScript라이브러리를 사용하여 끌어서 놓기 기능을 추가합니다. 다음은 한 요소를 다른 요소로 끌어 오는 기본적인 예입니다.)

driver.find_element_by_css_selector("input[type='submit']").click()
```

```

브라우저 탐색

다음으로 이동할 위치
driver.get("https://selenium.dev")

driver.current_url(현재 URL 가져오기)
driver.back() (뒤로가기)
driver.forward() (앞으로가기)
driver.refresh() (새로고침)
driver.title => 현재 제목 읽기
driver.current_window_handle (윈도우 핸들러 가져오기)
```

```python
#창 또는 탭 전환

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the driver
with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://seleniumhq.github.io")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    driver.find_element_by_link_text("new window").click()

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("Selenium documentation"))
```

```

새 창(또는)새 탭 및 스위치 만들기

# Opens a new tab and switches to new tab
driver.switch_to.new_window('tab')

# Opens a new window and switches to new window
driver.switch_to.new_window('window')

창 또는 탭 닫기

#Close the tab or window
driver.close()

#Switch back to the old tab or window
driver.switch_to.window(original_window)

세션 종료 시 브라우저 종료
driver.quit()

해당 WebDriver세션과 관련된 모든 창과 탭을 닫습니다.
브라우저 프로세스 닫기
백그라운드 드라이버 프로세스 닫기
SeleniumGrid에게 브라우저가 더 이상 사용되지 않으므로 다른 세션에서 사용할 수 있음을 알립니다(SeleniumGrid를 사용 중인 경우).

# unittest teardown
# https://docs.python.org/3/library/unittest.html?highlight=teardown#unittest.TestCase.tearDown
def tearDown(self):
    self.driver.quit()

테스트 컨텍스트에서 WebDriver를 실행하지 않는 경우 다음을 고려할 수 있습니다.try / finally예외가 여전히 WebDriver세션을 정리할 수 있도록 대부분의 언어에서 제공됩니다.

try:
    #WebDriver code here...
finally:
    driver.quit()

Python의 WebDriver는 이제 python컨텍스트 관리자를 지원합니다.with키워드는 실행이 끝날 때 자동으로 드라이버를 종료할 수 있습니다.

with webdriver.Firefox() as driver:
  # WebDriver code here...

# WebDriver will automatically quit after indentation
```


```

프레임 및 Iframes

<div id="modal">
  <iframe id="buttonframe" name="myframe"  src="https://seleniumhq.github.io">
   <button>Click here</button>
 </iframe>
</div>

# This Wont work
driver.find_element_by_tag_name('button').click()

웹 라이선스 사용
WebElement를 사용하여 전환하는 것이 가장 유연한 옵션입니다. 원하는 선택기를 사용하여 프레임을 찾고 전환할 수 있습니다.

# Store iframe web element
iframe = driver.find_element_by_css_selector("#modal > iframe")

# switch to selected iframe
driver.switch_to.frame(iframe)

# Now click on button
driver.find_element_by_tag_name('button').click()

이름 또는 ID사용
프레임 또는 iframe에 ID또는 이름 속성이 있는 경우, 대신 이 속성을 사용할 수 있습니다. 페이지에서 이름이나 ID가 고유하지 않으면 처음 발견된 이름으로 전환됩니다.

# Switch frame by id
driver.switch_to.frame('buttonframe')

# Now, Click on the button
driver.find_element_by_tag_name('button').click()

색인 사용
또한 JavaScript에서 Window.frame을 사용하여 쿼리 할 수 있는 프레임의 인덱스를 사용할 수도 있습니다.

# Switch to the second frame
driver.switch_to.frame(1)
  
프레임 남기기
iframe또는 frameset을 남기려면, 다음과 같이 기본 내용으로 다시 전환합니다.

# switch back to default content
driver.switch_to.default_content()
```


```

창 관리
화면 해상도는 웹 애플리케이션의 렌더링 방식에 영향을 줄 수 있으므로 WebDriver에서는 브라우저 창을 이동하고 크기를 조정하는 메커니즘을 제공합니다.

창 크기 가져오기
브라우저 창의 크기를 픽셀로 가져옵니다.

# Access each dimension individually
width = driver.get_window_size().get("width")
height = driver.get_window_size().get("height")

# Or store the dimensions and query them later
size = driver.get_window_size()
width1 = size.get("width")
height1 = size.get("height")

창 크기 설정
창을 복원하고 창 크기를 설정합니다.
driver.set_window_size(1024, 768)

창 위치 가져오기
브라우저 창의 왼쪽 상단 좌표를 가져옵니다.

# Access each dimension individually
x = driver.get_window_position().get('x')
y = driver.get_window_position().get('y')

# Or store the dimensions and query them later
position = driver.get_window_position()
x1 = position.get('x')
y1 = position.get('y')

창 위치 설정
# Move the window to the top left of the primary monitor
driver.set_window_position(0, 0)

최대 창
창을 확대합니다. 대부분의 운영 체제에서 창은 운영 체제의 메뉴와 도구 모음을 차단하지 않고 화면을 채웁니다.

driver.maximize_window()

최소화 창
driver.minimize_window() 

전체 창
driver.fullscreen_window() => f11과 비슷한 기능
```
