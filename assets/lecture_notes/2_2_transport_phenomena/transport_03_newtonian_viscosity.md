---
layout: page
title: 뉴턴 유체와 운동량 전달
description: 점도, 전단응력, Couette 유동 및 압력 구동 유동
target: 2학년 2학기
permalink:
prerequisite: 유체정역학, 미분과 적분, 보존식
toc: false
---

**목차**

* TOC
{:toc}

# 1. 점도와 운동량 전달

이웃한 유체층이 다른 속도로 움직이면 층 사이에서 운동량이 전달된다. 점도는
이러한 상대 운동에 저항하는 정도이다.

$$[\mu]=\mathrm{Pa\,s}$$

$\mu$가 점도(dynamic viscosity)를 의미하며 그 SI단위는 $\mathrm{Pa\, s}$, 즉
파스칼 곱하기 초(second)이다.

# 2. 뉴턴의 점성법칙

유체의 $x$ 방향 속도 $v_x$가 $y$에 따라 변할 때 뉴턴 유체는

$$\boxed{\tau_{yx}=-\mu\frac{dv_x}{dy}}$$

를 따른다. 점도가 일정하고 전단응력이 속도구배에 선형 비례하는 유체를 뉴턴
유체라고 한다.

## 2.1. 부호, 물성 및 적용 조건

$dv_x/dy>0$이면 위쪽 유체층이 더 빠르다. 분자 운동은 위쪽의 큰 $x$ 운동량을
아래쪽으로 전달하므로 $+y$ 방향 운동량 플럭스 $\tau_{yx}$는 음수이다.
반면 위층이 아래층에 가하는 $+x$ 방향 전단력은 양수로 표현할 수 있다.
[제1강의 부호 정의]({% link assets/lecture_notes/2_2_transport_phenomena/transport_01_orientation.md %})와
함께 읽으면 플럭스와 면에 작용하는 힘을 구분할 수 있다.

뉴턴 유체라는 말은 주어진 온도·압력에서 전단응력이 전단률에 선형 비례한다는
뜻이다. **모든 온도에서 점도가 일정하다는 뜻은 아니다.** 용융 고분자나
입자가 많이 포함된 슬러리에서는 점도가 전단률에 따라 변할 수 있으므로
아래의 일정 $\mu$ 해를 그대로 적용할 수 없다.

동점도(kinematic viscosity)는 $\nu=\mu/\rho$이고 단위는 $\mathrm{m^2/s}$이다.
이는 속도 교란이 점성에 의해 퍼지는 시간척도 $H^2/\nu$와 연결된다.

# 3. Couette 유동

거리 $H$인 두 평판 사이에서 아래 판은 정지하고 위 판은 속도 $U$로 움직인다.
정상상태, 일차원, 압력구배가 없는 조건에서

$$\frac{d\tau_{yx}}{dy}=0,\qquad \frac{d^2v_x}{dy^2}=0$$

이다. 점착조건 $v_x(0)=0$, $v_x(H)=U$를 적용하면

$$\boxed{v_x(y)=U\frac{y}{H}},\qquad |\tau|=\mu\frac{U}{H}$$

를 얻는다. 속도분포는 선형이고 평균속도는 $U/2$이다.

## 3.1. 선형 속도분포가 나오는 이유

아래의 해들은 비압축성 뉴턴 유체, 일정 점도, 정상 층류, 입구 영향이 사라진
완전히 발달한 유동을 가정한다. Couette 유동에서는 압력구배와 유동방향 체적력이
없어서 각 층이 받는 전단력이 평형을 이룬다. 따라서 $\tau_{yx}$는 일정하고
$dv_x/dy$도 일정하다. 두 번 적분하면

$$v_x=C_1y+C_2,\qquad C_2=0,\quad C_1=U/H$$

이다. 판의 면적이 $A_p$이면 일정한 속도를 유지하는 데 필요한 힘의 크기는
$F=\mu UA_p/H$이다. 판이 공급하는 동력은 $FU$이며 유체에서 점성에 의해
열로 소산된다. 운동량 수지와 별도로 에너지 수지도 존재한다는 예이다.

# 4. 평행판 사이 압력 구동 유동

정지한 두 평판이 $y=\pm H$에 있고 압력이 $x$ 방향으로 감소하면

$$0=-\frac{dp}{dx}+\mu\frac{d^2v_x}{dy^2}$$

이다. $v_x(\pm H)=0$을 적용하면

$$\boxed{v_x(y)=-\frac{1}{2\mu}\frac{dp}{dx}(H^2-y^2)}$$

이다. 속도분포는 포물선이고 중앙에서 최대이며 $\bar v=2v_{max}/3$이다.

# 5. 원관 유동

반지름 $R$, 길이 $L$인 원관의 완전히 발달한 층류에서

$$v_z(r)=\frac{\Delta p}{4\mu L}(R^2-r^2)$$

이고 체적유량은

$$\boxed{Q=\frac{\pi R^4}{8\mu L}\Delta p}$$

이다. 반지름이 두 배가 되면 같은 압력차에서 유량은 16배가 된다.

## 5.1. 유량은 최대속도에 단면적을 곱한 값이 아니다

원관에서 반지름 $r$인 얇은 고리의 면적은 $dA=2\pi r\,dr$이므로

$$
Q=\int_0^Rv_z(r)2\pi r\,dr
=\frac{\pi\Delta pR^4}{8\mu L},\qquad
\bar v=\frac{Q}{\pi R^2}=\frac{v_{max}}{2}.
$$

여기서 $\Delta p=p_{in}-p_{out}>0$이며, 관이 수평이거나 유동방향 중력 영향을
별도로 제거한 경우이다. 층류 여부를 판단하는 대표 무차원수는

$$\mathrm{Re}=\frac{\rho\bar v(2R)}{\mu}=\frac{\bar v(2R)}{\nu}$$

이다. 매끈한 직선 원관에서 충분히 낮은 Reynolds 수는 층류 해 적용의 근거가
되지만, 전이는 입구 교란과 거칠기에도 영향을 받는다. 반지름을 늘리면 $Q$뿐
아니라 $\bar v$와 Re도 변하므로, $R^4$ 비례관계를 사용할 때 층류 가정이
여전히 성립하는지 다시 확인해야 한다.

# 6. 경사면을 흐르는 액막

두께 $H$인 액체막이 중력에 의해 수직 벽을 따라 아래로 흐른다고 하자. 아래쪽을
$x$의 양의 방향, 벽에서 액체 쪽을 $y$ 방향으로 정한다. 정상상태에서 압력구배를
무시하면 $x$ 방향 운동량 방정식은

$$
\mu\frac{d^2v_x}{dy^2}+\rho g=0
$$

이다. 벽에서는 점착조건 $v_x(0)=0$, 자유표면에서는 전단응력이 없으므로
$dv_x/dy|_{y=H}=0$이다. 두 조건을 적용하면

$$
\boxed{v_x(y)=\frac{\rho g}{\mu}\left(Hy-\frac{y^2}{2}\right)}
$$

를 얻는다. 속도는 벽에서 0이고 자유표면에서 최대이다.

$$
v_{max}=\frac{\rho gH^2}{2\mu},\qquad
\bar v=\frac{\rho gH^2}{3\mu}
$$

이 예제는 압력 대신 중력이 유동의 구동력이 될 수 있음을 보여준다.


## 6.1. 수직 벽에서 경사면으로 확장하기

앞의 식은 제목에 포함된 경사면 중 수직인 경우에 해당한다. 경사각 $\theta$를
**수평면으로부터** 재면 유동방향 중력가속도는 $g\sin\theta$이다. 같은 가정에서

$$
v_x(y)=\frac{\rho g\sin\theta}{\mu}
\left(Hy-\frac{y^2}{2}\right),\qquad
\frac{Q}{b}=\int_0^Hv_x\,dy=\frac{\rho g\sin\theta H^3}{3\mu}.
$$

$b$는 액막의 폭이다. 자유표면의 전단응력을 0으로 둔 것은 위쪽 기체의 전단을
무시한다는 가정이며, 강한 기체 유동이나 표면장력 구배가 있으면 경계조건이 바뀐다.

# 7. 속도분포를 해석하는 방법

- 점착조건 때문에 고체 벽과 접한 유체의 속도는 벽의 속도와 같다.
- 대칭면에서는 속도구배가 0이고 압력 구동 유동의 속도가 최대이다.
- $dv_x/dy$의 부호가 바뀌면 전단응력의 방향도 바뀐다.
- 속도분포를 단면에 대해 적분하면 체적유량을 얻는다.

동일한 관과 압력차에서 점도가 커지면 유량은 작아진다. 반면 Couette 유동에서
벽의 속도를 지정하면 속도분포는 점도와 무관하지만 벽에 필요한 힘은 점도에
비례한다.

# 8. 연습 문제

1. $\mu=0.5\ \mathrm{Pa\,s}$, $U=1\ \mathrm{m/s}$, $H=0.01\ \mathrm m$인 Couette 유동의 전단응력 크기를 구하라.
2. Couette 유동에서 $y=H/4$의 속도를 구하라.
3. 원관의 반지름만 3배가 되면 같은 조건에서 유량은 몇 배가 되는가?
4. $\mu=0.10\ \mathrm{Pa\,s}$, $\rho=1000\ \mathrm{kg/m^3}$일 때 동점도를 구하라.
5. Couette 유동에서 위 판의 속도가 두 배가 되면 전단응력 크기는 어떻게 되는가?
6. 압력 구동 평판 유동에서 벽과 중앙의 속도를 비교하라.

<!--
풀이와 해답:
1. |tau|=mu U/H=50 Pa이다.
2. v_x=U/4이다.
3. Q는 R^4에 비례하므로 81배이다.
4. nu=mu/rho=1.0e-4 m^2/s이다.
5. |tau|=mu*U/H이므로 두 배가 된다.
6. 점착조건으로 벽의 속도는 0이고 대칭면인 중앙에서 최대이다.
-->

## 관련자료와 이어 읽기

- [MIT OCW 3.185: Fluid Dynamics](https://ocw.mit.edu/courses/3-185-transport-phenomena-in-materials-engineering-fall-2003/resources/chap4/): PDF의 Newtonian fluids와 simple Newtonian flows 부분을 읽고, 교재의 응력 부호 정의를 본문과 비교한다.
- [OpenStax: Viscosity and Turbulence](https://openstax.org/books/university-physics-volume-1/pages/14-7-viscosity-and-turbulence): 점도, Poiseuille 유동, Reynolds 수를 복습할 수 있다.

- [제1강: 이동현상 개요]({% link assets/lecture_notes/2_2_transport_phenomena/transport_01_orientation.md %})
- [제4강: 열전달 기초]({% link assets/lecture_notes/2_2_transport_phenomena/transport_04_heat_transfer.md %})

---

[이전 강의](/assets/lecture_notes/2_2_transport_phenomena/transport_02_fluid_statics.md) · [강의 목록](/_lectures/2_2_transport.md) · [다음 강의](/assets/lecture_notes/2_2_transport_phenomena/transport_04_heat_transfer.md)
