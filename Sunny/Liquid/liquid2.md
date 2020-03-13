# Liquid Study

```

Filter

abs => 절대값으로 숫자를 리턴시킴

{{ -17 | abs }} => 17
{{ 4 | abs }} => 4

{{ "-19.86" | abs }} => 19.86

append => 
{% assign filename = "/index.html" %}
{{ "website.com" | append: filename }}
=> website.com/index.html

at_least => 최소 값으로 지정함 (제한을)
{{ 4 | at_least: 5 }} => 5
{{ 4 | at_least: 3 }} => 4

at_most => 최대 값으로 지정함 (제한을)
{{ 4 | at_most: 5 }} => 4
{{ 4 | at_most: 3 }} => 3

capitalize => 첫글 자를 대문자로 바꿔줌!
{{ "title" | capitalize }} => Title
{{ "my great title" | capitalize }} => My great title

ceil => 일반적으로 정수로 올림함!
{{ 1.2 | ceil }}=>2
{{ 183.357 | ceil }} => 184

compact => 배열에서 nii 값을 제거함!


{% assign site_categories = site.pages | map: "category" %}

{% for category in site_categories %}
- {{ category }}
{% endfor %}
- business
- celebrities
-
- lifestyle
- sports
-
- technology

{% assign site_categories = site.pages | map: "category" | compact %}

{% for category in site_categories %}
- {{ category }}
{% endfor %}
- business
- celebrities
- lifestyle
- sports
- technology

concat
다양한 배열을 결합시킴(결과에서 나오게끔 확인!)

{% assign fruits = "apples, oranges, peaches" | split: ", " %}
{% assign vegetables = "carrots, turnips, potatoes" | split: ", " %}

{% assign everything = fruits | concat: vegetables %}

{% for item in everything %}
- {{ item }}
{% endfor %}
- apples
- oranges
- peaches
- carrots
- turnips
- potatoes

{% assign furniture = "chairs, tables, shelves" | split: ", " %}

{% assign everything = fruits | concat: vegetables | concat: furniture %}

{% for item in everything %}
- {{ item }}
{% endfor %}
- apples
- oranges
- peaches
- carrots
- turnips
- potatoes
- chairs
- tables
- shelves

date

date에서 지정한 조건으로 보여주게함!

{{ article.published_at | date: "%a, %b %d, %y" }} => Fri, Mar 13, 20
This page was last updated at {{ "now" | date: "%Y-%m-%d %H:%M" }}.
=> This page was last updated at 2020-03-13 17:16.

default => 변수가 존재하지 않을 때(nil, false, empty 일 때)
=> 사용가능 (만약 값이 있다면 사용할 수 없음!)

divided_by => Divides a number by another number.
{{ 16 | divided_by: 4 }} => 4 
{{ 5 | divided_by: 3 }} => 1.xxx지만 int 값만 처리하기에 1로 나옴!
만약 float로 보고 싶다면 
{{ 20 | divided_by: 7.0 }} => 2.857xxx
혹은 times를 1.0으로 설정한다듯이 float 타입으로 바꿔서 계산함
{% assign my_integer = 7 %}
{% assign my_float = my_integer | times: 1.0 %}
{{ 20 | divided_by: my_float }}
=> 2.85714

downcase => 각 문자를 소문자로 바꿈
{{ "Parker Moore" | downcase }} => parker moore

escape => 문자를 이스케이프 시퀀스로 바꾸어 문자열을 설정합니다(예를 들어 URL에서 사용할 수 있음), 바꿀 수 없는 것은 그대로 나옴!

{{ "Have you read 'James & the Giant Peach'?" | escape }}
=> Have you read &#39;James &amp; the Giant Peach&#39;?

escape_one => 기존의 이스케이프 된 엔티티를 변경하지 않고 문자열을 설정 (탈출 조건이 없으면 . 바뀌지 않음!)
{{ "1 < 2 & 3" | escape_once }} => 1 &lt; 2 &amp; 3
{{ "1 &lt; 2 &amp; 3" | escape_once }} => 1 &lt; 2 &amp; 3

first => 배열의 첫번째 값을 반환함!
{{ "Ground control to Major Tom." | split: " " | first }} => Ground

{% assign my_array = "zebra, octopus, giraffe, tiger" | split: ", " %}

{{ my_array.first }}
=> zebra 


{% if my_array.first == "zebra" %}
  Here comes a zebra!
{% endif %} => 내부 태그에서 쓰일 때는 점 표기법을 사용함!!

floor => 입력값을 가장 가까운 정수로 내림!=> 리퀴드는 필터가 적용되기 전에 바꾸려고함!
{{ 1.2 | floor }} => 1 / {{ "3.5" | floor }} => 3

join 
{% assign beatles = "John, Paul, George, Ringo" | split: ", " %}
{{ beatles | join: " and " }}
John and Paul and George and Ringo!

last => 배열의 끝 아이템을 호출함!
{{ "Ground control to Major Tom." | split: " " | last }} => Tom.
{% assign my_array = "zebra, octopus, giraffe, tiger" | split: ", " %} => tiger

{% if my_array.last == "tiger" %}
  There goes a tiger!
{% endif %}

lstrip => 왼쪽 공백 제거 
{{ "          So much room for activities!          " | lstrip }} =>So much room for activities!


```