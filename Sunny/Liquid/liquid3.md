# Liquid Study

```

map
=> 다른 객체에서 명명된 속성의 값을 추출하여 값을 배열을 출력..

{% assign all_categories = site.pages | map: "category" %}

{% for item in all_categories %}
- {{ item }}
{% endfor %}

- business
- celebrities
- lifestyle
- sports
- technology

minus => 숫자에서 다른 숫자를 뺌 
{{ 4 | minus: 2 }} =>2 

{{ 183.357 | minus: 12}} => 171.357

modulo => 분할 작업의 나머지 부분을 반환 !
{{ 3 | modulo: 2 }} => 1 / {{ 24 | modulo: 7 }} => 3 / 
{{ 183.357 | modulo: 12 }} => 3.357

newline_to_br = > \n을 <br />으로 바꿔줌!
plus => 숫자와 다른 숫자를 더함 
{{ 4 | plus: 2 }} => 6 / {{ 183.357 | plus: 12 }} => 195.357

prepend (프리펜드) 
{{ "apples, oranges, and bananas" | prepend: "Some fruit: " }} => Some fruit: apples, oranges, and bananas 
 {% assign url = "example.com" %}
{{ "/index.html" | prepend: url }} => example.com/index.html

remove => 해당 단어가 들어있는 문자열은 모두 제거
{{ "I strained to see the train through the rain" | remove: "rain" }} => I sted to see the t through the 

remove_first => 처음 나오는 것만 제거!
{{ "I strained to see the train through the rain" | remove_first: "rain" }} => I sted to see the train through the rain

replace => 해당 단어가 들어있는 문자열은 모두 대체
{{ "Take my protein pills and put my helmet on" | replace: "my", "your" }} => Take your protein pills and put your helmet on

replace_first => 해당 단어가 처음으로 나오는 것만 대체

{{ "Take my protein pills and put my helmet on" | replace_first: "my", "your" }} => Take your protein pills and put my helmet on

reverse => 배열이나 문자열을 반대로 출력해줌 
{% assign my_array = "apples, oranges, peaches, plums" | split: ", " %} {{ my_array | reverse | join: ", " }}  => plums, peaches, oranges, apples

{{ "Ground control to Major Tom." | split: "" | reverse | join: "" }}
=> .moT rojaM ot lortnoc dnuorG

round => 반올림
{{ 1.2 | round }} => 1 / {{ 183.357 | round: 2 }} => 183.36

rstrip => 우측 공백 제거 
{{ "          So much room for activities!          " | rstrip }}
          So much room for activities!

size => 문자열이나 배열의 개수 등을 리턴해줌!!
{{ "Ground control to Major Tom." | size }} => 28
{% assign my_array = "apples, oranges, peaches, plums" | split: ", " %}

{{ my_array.size }} => 4

{% if site.pages.size > 10 %}
  This is a big website!
{% endif %} => 태그에서 사용할 때에는 점을 사용하여 코딩함!!

slice => 인덱스으로 자름 (0 => 첫번째 문자열만 출력 1, 5면 => 두번쨰~6번째 문자열을 출력)

{{ "Liquid" | slice: 2, 5 }} => quid
{{ "Liquid" | slice: -3, 2 }} => ui (-3에서 2번째까지 출력!)

sort => 대문자 에서 소문자 순으로 .. 빠른 순으로 출력해줌!
{% assign my_array = "zebra, octopus, giraffe, Sally Snake" | split: ", " %}

{{ my_array | sort | join: ", " }} => Sally Snake, giraffe, octopus, zebra

{% assign products_by_price = collection.products | sort: "price" %}
{% for product in products_by_price %}
  <h4>{{ product.title }}</h4>
{% endfor %} => 배열에서는 점을 이용하여 사용가능함!

sort_natural => 알파뱃 순서대로 출력해줌 => 대소문자 구별 안함!
{% assign my_array = "zebra, octopus, giraffe, Sally Snake" | split: ", " %}

{{ my_array | sort_natural | join: ", " }}
=> giraffe, octopus, Sally Snake, zebra

{% assign products_by_company = collection.products | sort_natural: "company" %}
{% for product in products_by_company %}
  <h4>{{ product.title }}</h4>
{% endfor %}
=> 점 문자를 사용하여 태그 안에서 사용가능!

split => 해당하는 것을 기준으로 분리하여 출력!
{% assign beatles = "John, Paul, George, Ringo" | split: ", " %} 

{% for member in beatles %}
  {{ member }}
{% endfor %} =>   
  John

  Paul

  George

  Ringo

strip => 양쪽 공백을 제거하여 출력 
{{ "          So much room for activities!          " | strip }} => So much room for activities!

strip_html => html 태그를 문자열에서 제거해줌
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }} => Have you read Ulysses?

strip_newlines => \n으로 나눠져 있는 것을 제거하여 합쳐서 나옴!
{% capture string_with_newlines %}
Hello
there
{% endcapture %}

{{ string_with_newlines | strip_newlines }} => Hellothere

times => 곱셈이라고 이해하기!?
{{ 3 | times: 2 }} => 6 / {{ 183.357 | times: 12 }} => 2200.284

truncate => 인수로 전달된 문자 수까지 문자열을 줄임!!
{{ "Ground control to Major Tom." | truncate: 20 }} => Ground control to...

{{ "Ground control to Major Tom." | truncate: 25, ", and so on" }} => Ground control, and so on
{{ "Ground control to Major Tom." | truncate: 20, "" }} => Ground control to Ma

truncatewords 
{{ "Ground control to Major Tom." | truncatewords: 3 }} => 인수로 전달된 단어수로 문자열을 줄임(지정한 단어 수가 문자열의 단어 수보다 작으면 줄임표가 문자열에 추가됨!!)

{{ "Ground control to Major Tom." | truncatewords: 3, "--" }} => Ground control to--

uniq => 배열에서 중복을 제거함 ! 

{% assign my_array = "ants, bugs, bees, bugs, ants" | split: ", " %}

{{ my_array | uniq | join: ", " }} => ants, bugs, bees

upcase => 모든 문자열을 대문자로 변환 / 이미 되어있는 아이는 상관없음!

{{ "Parker Moore" | upcase }} => PARKER MOORE

url_decode => url 이나 encode로 된 인코딩 문자열을 디코딩함!
{{ "%27Stop%21%27+said+Fred" | url_decode }} => 'Stop!' said Fred

url_encode => 문자열의 공백이나 기호를 인코딩함 

{{ "john@liquid.com" | url_encode }} => john%40liquid.com
{{ "Tetsuro Takara" | url_encode }} => Tetsuro+Takara

where => 기본적으로 지정된 속성 값 또는 신뢰할 수 있는 값을 가진 개체만 포함하여 배열 생성 .. 


All products:
{% for product in products %}
- {{ product.title }}
{% endfor %}

{% assign kitchen_products = products | where: "type", "kitchen" %}

Kitchen products:
{% for product in kitchen_products %}
- {{ product.title }}
{% endfor %}
=> 
All products:
- Vacuum
- Spatula
- Television
- Garlic press

Kitchen products:
- Spatula
- Garlic press
(type은 생략 가능!)

All products:
{% for product in products %}
- {{ product.title }}
{% endfor %}

{% assign available_products = products | where: "available" %}

Available products:
{% for product in available_products %}
- {{ product.title }}
{% endfor %}

All products:
- Coffee mug
- Limited edition sneakers
- Boring sneakers

Available products:
- Coffee mug
- Boring sneakers


{% assign new_shirt = products | where: "type", "shirt" | first %}

Featured product: {{ new_shirt.title }}
Featured product: Hawaiian print sweater vest

```