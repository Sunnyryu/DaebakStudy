## Electron 

#### image service


```
디스플레이 정보 
id(디스플레이의 식별자)
rotation(디스플레이가 회전했다면 해당 각도 설정)
scaleFactor (디스플레이의 디바이스에 대한 픽셀 비율)
touchSupport (디스플레이가 터치 조작이 가능하다면 available이 되옵니다)
bounds (디스플레이의 위치 정보!)
size( 디스플레이의 크기!)
workArea (디스플레이의 활용 가능 영역의 정보)
workAreaSize (디스플레이의 활용 가능 영역의 크기!)
getPrimaryDisplay(주 디스플레이의 정보를 반환합니다.)
getDisplayNearestPoint(매개변수로 전달한 x좌표, y좌표에서 가장 가까운 디스플레이의 정보를 반환)
getDisplayMatching(매개변수로 전달한 사각형 영역을 포함한 디스플레이 정보를 반환함!)
frame(false로 지정하면 윈도우의 타이틀 바를 표시하지 않음!)
transparent(true로 지정하면 윈도우의 배경이 투명해짐!)
alwaysOnTop(true로 지정하면 항상 모든 화면 가장 위에 표시됨!)
x,y, width,height(윈도우의 위치 정보(왼쪽의 좌표, 위의 좌표, 너비, 높이 지정!))

display.name에는 "Screen 1"과 같은 문자열이 저장되어 있음! 여기에는 설정한 이름은 캡쳐 이미지를 추출할 때사용!
SEND_BOUNDS 이벤트는 자르기 조각이 완료된느 시점에 렌더러 프로세스에서 송신되는 이벤트! (디스플레이 정보와 자른 영역의 정보 메서드를 호출한 쪽으로 전달하게 하고 있음!)

리액트를 활용해서 자르기 작업 전용 컴포넌트를 작성함! / Trimmer 컴포넌트에는 마우스 드래그 주에 2종류의 마우스 좌표 값을 추출하게 구현!
(clientPosition => BrowserWindow의 HTML 내부에서의 상대 좌표! 이 값을 새용해서 사각형을 그림!
screenPosition : 데스크톱 전체에서의 절대 좌표입니다. 이 값을 SEND_BOUNDS 이벤트를 통해 메인 프로세스에 전송하고 자를 대상의 위치 정보로 사용함!)

desktopCapturer.getSources 
screen : 사용자의 디스플레이 전체의 정보가 콜백에 전달됩니다.
windows : 사용자가 실행하고 있는 어플리케이션 원도우의 정보가 콜백에 전달됩니다.

id : source의 유일 식별자 / name : 소스의 이름 / 멀티 디스플레이의 경우 스크린 1, 2 ... 번호 형식으로 나옴 .. 싱글 디스플레이의 경우 엔타이어 스크린 이라는 문자열이 나옴! 
thumbnail : 디스플레이 또는 어플리케이션 윈도우의 썸네일 이미지임!




```