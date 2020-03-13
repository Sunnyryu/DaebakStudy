# Liquid Study

```

color_to_rgb => css color를 rgb로 포매팅함
{{ '#7ab55c' | color_to_rgb }} => rgb(122, 181, 92 )
{{ 'hsla(100, 38%, 54%, 0.5)' | color_to_rgb }} => rgba(122, 181, 92, 0.5)

color_to_hsl => css color를  hsl로 포매팅함!
{{ '#7ab55c' | color_to_hsl }} => hsl(100, 38%, 54%)
{{ 'rgba(122, 181, 92, 0.5)' | color_to_hsl }} => hsla(100, 38%, 54%, 0.5)

color_to_hex => css color를 hex6으로 포매팅함 
{{ 'rgb(122, 181, 92)' | color_to_hex }} = > #7ab55c
{{ 'rgba(122, 181, 92, 0.5)' | color_to_hex }} => #7ab55c

color_extract => 색상에서 구성 요소를 추출함 .. 알파, 레드, 블루, 그린, 색조, 채도 및 밝기
{{ '#7ab55c' | color_extract: 'red' }} = > 122

color_brightness => 지정된 색상의 인식된 밝기를 계산 / w3c를 권장 

{{ '#7ab55c' | color_brightness }} => 153.21

color_modify => 0~255 까지 rgb 값으로 변경 / 알파는 0~1 사이여야함 / hue는 0에서 360도 사이여야함 / 채도와 밝기는 0~100퍼센트 사이여야함!

{{ '#7ab55c' | color_modify: 'red', 255 }} = > #ffb55c

{{ '#7ab55c' | color_modify: 'alpha', 0.85 }} => rgba(122, 181, 92, 0.85)

color_lighten => 입력색을 밝게함(0~100 사이)
{{ '#7ab55c' | color_lighten: 30 }} => #d0e5c5

color_darken => 입력색을 어둡게함(0~100 사이)
{{ '#7ab55c' | color_darken: 30 }} => #355325

color_saturate(입력색을 음영처리함 0~100 사이! )
{{ '#7ab55c' | color_saturate: 30 }} => #6ed938

color_desaturate(입력색을 비음영처리함 0~100퍼센트 사이!)
{{ '#7ab55c' | color_desaturate: 30 }} => #869180

color_mix (2가지 색을 섞으며 혼합비율은 0~100%로 함)
{{ '#7ab55c' | color_mix: '#ffc0cb', 50 }} => #bdbb94

{{ 'rgba(122, 181, 92, 0.75)' | color_mix: '#ffc0cb', 50 }} => rgba(189, 187, 148, 0.875)

color_contrast => 두 색상 사이의 대비 비율을 계산함!( 3.5:1이면 3.5를 반환)
{{ '#495859' | color_contrast: '#fffffb' }} => 7.4

color_difference => 두 색상의 차이나 거리를 계산(500이상이 나올꺼임)
{{ '#ff0000' | color_difference: '#abcdef' }} => 528

brightness_difference => 두 색상의 밝기 차이나 거리 (125 이상이 나올까임)
{{ '#fff00f' | brightness_difference: '#0b72ab' }} => 129

Font filters

font_modify (폰트 수정..)

{% assign bold_italic = settings.body_font | font_modify: 'weight', 'bold' | font_modify: 'style', 'italic' %}
(앞은 수정이 필요한 속성 / 두번째는 첫번째가 바뀔 속성을 작성)

style 
normal => 동일한 중량의 일반적인 변형을 반환 (존재할 경우) / italic =>동일한 중량의 기울임 꼴 변형을 반환(존재시) / oblique => 다음과 동일한 동작 / 이탤릭과 같은 동작이라고 생각하기!

weight 
100-> 900 (지정된 무게의 동일한 스타일의 변형을 반환)
normal => 400으로 변환 / bold (700으로 변환 )
+100 -> +900 (같은 스타일의 굵은 글꼴을 증가하여 반환) 400일 경우 +100이면 500의 스타일로 함

-의 경우 (동일한 스타일의 경우 더 밝은 글꼴로 반환함)

lighter => css를 같은 스타일보다 밝게..
bolder => css를 같은 스타일보다 어둡게..

Handling font variants
{% assign bolder_font = settings.body_font | font_modify: 'weight', 'bolder' %}
h2 {
  font-weight: {{ bolder_font.weight }};
} => 
h2 {
    font-weight: ;
}

{% assign bolder_font = settings.body_font | font_modify: 'weight', 'bolder' %}
{% if bolder_font %}
h2 {
  font-weight: {{ bolder_font.weight }};
}
{% endif %}

font_face
<style>
  {{ settings.heading_font | font_face }}
</style>
=> 
<style>
  @font-face {
    font-family: "Neue Haas Unica";
    font-weight: 400;
    font-style: normal;
    src: url("https://fonts.shopifycdn.com/neue_haas_unica/neuehaasunica_n4.8a2375506d3dfc7b1867f78ca489e62638136be6.woff2?hmac=d5feff0f2e6b37fedb3ec099688181827df4a97f98d2336515503215e8d1ff55&host=c2hvcDEubXlzaG9waWZ5Lmlv") format("woff2"),
         url("https://fonts.shopifycdn.com/neue_haas_unica/neuehaasunica_n4.06cdfe33b4db0659278e9b5837a3e8bc0a9d4025.woff?hmac=d5feff0f2e6b37fedb3ec099688181827df4a97f98d2336515503215e8d1ff55&host=c2hvcDEubXlzaG9waWZ5Lmlv") format("woff");
  }
</style>

Additional properties
<style>
  {{ settings.heading_font | font_face: font_display: 'swap' }}
</style>
=> 
<style>
  @font-face {
    font-family: "Neue Haas Unica";
    font-weight: 400;
    font-style: normal;
    font-display: swap;
    src: url("https://fonts.shopifycdn.com/neue_haas_unica/neuehaasunica_n4.8a2375506d3dfc7b1867f78ca489e62638136be6.woff2?hmac=d5feff0f2e6b37fedb3ec099688181827df4a97f98d2336515503215e8d1ff55&host=c2hvcDEubXlzaG9waWZ5Lmlv") format("woff2"),
         url("https://fonts.shopifycdn.com/neue_haas_unica/neuehaasunica_n4.06cdfe33b4db0659278e9b5837a3e8bc0a9d4025.woff?hmac=d5feff0f2e6b37fedb3ec099688181827df4a97f98d2336515503215e8d1ff55&host=c2hvcDEubXlzaG9waWZ5Lmlv") format("woff");
  }
</style>

font_url
{{ settings.heading_font | font_url }}
=> 
https://fonts.shopifycdn.com/neue_haas_unica/neuehaasunica_n4.8a2375506d3dfc7b1867f78ca489e62638136be6.woff2?hmac=d5feff0f2e6b37fedb3ec099688181827df4a97f98d2336515503215e8d1ff55&host=c2hvcDEubXlzaG9waWZ5Lmlv




```