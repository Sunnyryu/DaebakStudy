# Liquid Study

```
Liquid는 shopify에서 루비 온 레일즈를 가공하여 만든 언어라고 생각하자

Objects ( {{ }})
{{ }}를 사용하여 변수 이름을 설정한다! 

Tags(로직을 만들거나 템플릿의 흐름을 제어 할 때 쓰임!!)
ex) 
# user가 sunny라면.....
    {% if user %}
        Hello {{ user.name }}!
    {% endif %}
=> Hello. Sunny!

Filters => 리퀴드 오브젝트의 출력을 바꿀 때 쓰임~? | => 라는 아이도 사용됨
ex) 
{{ "/a/b/url" | append: ".html" }}
=> /a/b/url.html

ex2) 
{{ "sunny!" | capitalize | prepend: "Hello " }}
=> Hello Sunny!

Operators => Liquid는 많은 로직과 비교 연산자가 있음!

== , != , >, <, >=, <=, or, and

contains => 문자열 내부에 하위 문자열이 있는지 확인 (배열에서도 확인 할 수 있음!)

작업순서(둘 이상의 및 / 또는 연산자가있는 태그에서 연산자는 오른쪽에서 왼쪽으로 순서대로 확인함)

Truthy and falsy

Truthy => nii과 false를 제외하곤 모두 Truthy임 

false => nii과 false 뿐




```