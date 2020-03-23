## Python Rewind

#### regular & crawling

```
정규식은 import re를 임포트하여 사용할 수 있음

^ : 라인의 처음을 매칭
$ : 라인의 끝을 매칭
. : 임의의 문자를 매칭 (와일드 카드)
\s : 공백 문자를 매칭
\S : 공백이 아닌 문자를 매칭
* : 바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 표기함.
*? : 바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.
+ : 바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 표기함
+? : 바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.
[aeiou]: 명세된 집합 문자에 존재하는 단일 문자와 매칭. “a”, “e”, “i”, “o”, “u” 문자만 매칭되는 예제
[a-z0-9]: - 기호로 문자 범위를 명세할 수 있다. 소문자이거나 숫자인 단일 문자만 매칭되는 예제.
( ) : 괄호가 정규표현식에 추가될 때, 매칭을 무시한다. 하지만 findall()을 사용 할 때 전체 문자열보다 매칭된 문자열의 상세한 부속 문자열을 추출할 수 있게 한다.

findall => 모두를 찾아줌 (re.findall)

역슬래쉬를 활용하여 특수 문자로 이뤙진 패턴을 찾을 수 있음
\$ => 이런석으로 가능

```

```

크롤링을 위한 네트워크 연결

소캣을 임포트하여 사용하기!

import urllib를 이용해서 웹에서 파일을 불러올 수 있음 

BeautifulSoup을 이용하여 웹 스크래핑 가능 

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

    
```