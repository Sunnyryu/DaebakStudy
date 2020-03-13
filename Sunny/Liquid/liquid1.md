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

Types => Liquid 오브젝트는 5가지 타입 중에 하나임!
String / Number / Boolean / Nil / Array

String => {% assign my_string = "Hello Sunny!" %}

Number => {% assign my_number = 25 %} (floats & integers)
Boolean(true & false)

Nil => special empty value => no results

Array => hold lists of variables of any type.

Whitespace control => {{- -}}, {%- -%}, 태그가 쓰임 
일반적으로 쓸일이 없지만 공백이 있게 나온다면 하이폰을 추가한다면 공백이 제거됨!

Tags
Comment => 수정되지 않은 코드를 리퀴드 템플릿에 그대로 둘 수 있음
ex) Anything you put between {% comment %} and {% endcomment %} tags
is turned into a comment => Anything you put between tags is turned into a comment.

Control flow => 흐름 제어 태그는 리퀴드에서 프로그래믹 로직을 사용할 수 있다.

if 
{% if a == "a" %}
    hi
{% endif %} => hi

unless => if의 특정 조건이 충족되지 않을 경우에만 코드블록 실행!
{% unless product.title == "Awesome Shoes" %}
  These shoes are not awesome.
{% endunless %}
= 
{% if product.title != "Awesome Shoes" %}
  These shoes are not awesome.
{% endif %}

elsif / else => if와는 다른 조건을 쓸 때 혹은 나머지 일때에 쓰임!!

case/when => 여러가지 조건을 만들때 사용하며 어떤 조건일 때는 a, 어떤 조건일 때는 b라 할 수있음 
{% assign handle = "cake" %}
{% case handle %}
  {% when "cake" %}
     This is a cake
  {% when "cookie" %}
     This is a cookie
  {% else %}
     This is not a cake nor a cookie
{% endcase %}

iteration( 코드블록을 반복적으로 수행하는 태그!)

for (코드 블록을 반복적으로 실행)


{% for product in collection.products %}
  {{ product.title }}
{% endfor %}
=> hat shirt pants

else (반복 문에서 값이 없을 경우에 else를 사용)
{% for product in collection.products %}
  {{ product.title }}
{% else %}
  The collection is empty.
{% endfor %}

break(무한루프를 예방하기 위해도 사용하지만.. 해당 값일 경우.. 반복문 종료)
{% for i in (1..5) %}
  {% if i == 4 %}
    {% break %}
  {% else %}
    {{ i }}
  {% endif %}
{% endfor %}

continue(반복문에서 해당 값은 제외하고 진행함!)
{% for i in (1..5) %}
  {% if i == 4 %}
    {% continue %}
  {% else %}
    {{ i }}
  {% endif %}
{% endfor %}

for에서의 limit/offset/range/reversed

limit => 해당 값까지만 나오게한다거나 그럴 때 사용

<!-- if array = [1,2,3,4,5,6] -->
{% for item in array limit:2 %}
  {{ item }}
{% endfor %}

=> 1 2

offset => 해당 인덱스에서부터 루프를 돌림!

<!-- if array = [1,2,3,4,5,6] -->
{% for item in array offset:2 %}
  {{ item }}
{% endfor %}
=> 3 4 5 6 

range => 반복문의 범위를 지정하기 위해 정의함!
{% for i in (3..5) %}
  {{ i }}
{% endfor %}

{% assign num = 4 %}
{% for i in (1..num) %}
  {{ i }}
{% endfor %}
3 4 5 
1 2 3 4 

reversed => 루프를 반대로 돌림!
<!-- if array = [1,2,3,4,5,6] -->
{% for item in array reversed %}
  {{ item }}
{% endfor %}
=> 6 5 4 3 2 1

cycle => 그룹을 한 개씩 출력하는 방식을 사용 .. 매번 cycle을 호출하면 다음 문자열 인수를 출력함!

{% cycle "one", "two", "three" %}
{% cycle "one", "two", "three" %}
{% cycle "one", "two", "three" %}
{% cycle "one", "two", "three" %}
one
two
three
one

cycle은 그룹의 이름을 정하여 사용할 수 있음
{% cycle "first": "one", "two", "three" %}
{% cycle "second": "one", "two", "three" %}
{% cycle "second": "one", "two", "three" %}
{% cycle "first": "one", "two", "three" %}
one
one
two
two

tablerow => 테이블을 만들기 위해 사용함.. <table>과 </table>이 있어야함!!
<table>
{% tablerow product in collection.products %}
  {{ product.title }}
{% endtablerow %}
</table>
<table>
  <tr class="row1">
    <td class="col1">
      Cool Shirt
    </td>
    <td class="col2">
      Alien Poster
    </td>
    <td class="col3">
      Batman Poster
    </td>
    <td class="col4">
      Bullseye Shirt
    </td>
    <td class="col5">
      Another Classic Vinyl
    </td>
    <td class="col6">
      Awesome Jeans
    </td>
  </tr>
</table>

{% tablerow product in collection.products cols:2 %}
  {{ product.title }}
{% endtablerow %}
<table>
  <tr class="row1">
    <td class="col1">
      Cool Shirt
    </td>
    <td class="col2">
      Alien Poster
    </td>
  </tr>
  <tr class="row2">
    <td class="col1">
      Batman Poster
    </td>
    <td class="col2">
      Bullseye Shirt
    </td>
  </tr>
  <tr class="row3">
    <td class="col1">
      Another Classic Vinyl
    </td>
    <td class="col2">
      Awesome Jeans
    </td>
  </tr>
</table>

limit, offset=> 끝나는 점이나 시작하는 인덱스를 조건으로 추가가능

{% tablerow product in collection.products cols:2 offset:3 %}
  {{ product.title }}
{% endtablerow %}

range => 루프에서 반복하는 범위를 지정가능 
<!--variable number example-->

{% assign num = 4 %}
<table>
{% tablerow i in (1..num) %}
  {{ i }}
{% endtablerow %}
</table>

<!--literal number example-->

<table>
{% tablerow i in (3..5) %}
  {{ i }}
{% endtablerow %}
</table>
```