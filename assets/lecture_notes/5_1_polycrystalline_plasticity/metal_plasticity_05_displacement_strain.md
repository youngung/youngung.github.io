---
layout: distill
title: 변위와 변형률
description: 변위장과 미소변형률 텐서의 관계
target: 학부 고학년
permalink:
featured: true
prerequisite: 벡터와 행렬
toc:
  sidebar: left

mermaid:
  enabled: true
  zoomable: true
typograms: true
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

- [1. 위치(position)와 위치의 변화(변위; displacement)](#1-위치position와-위치의-변화변위-displacement)
- [2. 변형과 변위장](#2-변형과-변위장)
- [3. 강체 운동 (Rigid Body Motion)](#3-강체-운동-rigid-body-motion)
- [4. 변위장 (displacement field)](#4-변위장-displacement-field)
- [5. 1차원 공간에서의 변형률](#5-1차원-공간에서의-변형률)
- [6. 1차원 예제](#6-1차원-예제)
- [7. 2차원 공간에서의 변위](#7-2차원-공간에서의-변위)
- [8. 변위구배의 대칭부분과 반대칭부분](#8-변위구배의-대칭부분과-반대칭부분)
- [9. 2차원 예제](#9-2차원-예제)
- [10. 요약](#10-요약)
- [11. 연습 문제](#11-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)
  - [문제 7](#문제-7)
  - [문제 8](#문제-8)
  - [문제 9](#문제-9)
  - [문제 10](#문제-10)
  - [문제 12](#문제-12)
  - [문제 13](#문제-13)
  - [문제 14](#문제-14)
  - [문제 15](#문제-15)
  - [문제 16](#문제-16)
  - [문제 17](#문제-17)

# 1. 위치(position)와 위치의 변화(변위; displacement)

- 3차원 공간 상의 위치를 벡터로 표현 가능하다.

$$\boldsymbol x=x_1\boldsymbol e_1+x_2\boldsymbol e_2+x_3\boldsymbol e_3$$

- 변형전 위치: $\boldsymbol X$
- 변형후 위치: $\boldsymbol x$ 라 하자.

- 이럴 경우 변위 $\boldsymbol u$는

$$\boldsymbol u = \boldsymbol x- \boldsymbol X$$

# 2. 변형과 변위장

- 변형은 내부의 상대적인 위치가 바뀌는 현상이다.

- 중요한 차이

| 상황                 | 변형 발생 여부 |
| -------------------- | -------------- |
| 물체 전체가 평행이동   | X              |
| 물체 전체가 회전      | X              |
| 길이가 늘어남        | O              |

# 3. 강체 운동 (Rigid Body Motion)

- 아래의 두 상황에서 변형률이 0이다.

  - 단순 평행 이동 (translation)

  - 회전

# 4. 변위장 (displacement field)

- 변위는 위치마다 다를 수 있다.

$$\boldsymbol u(위치) =\boldsymbol u (\boldsymbol x)=\boldsymbol u (x_1,x_2,x_3)$$

- 혹은 변형 전의 위치를 기준으로

$$\boldsymbol u(위치) =\boldsymbol u (\boldsymbol X)=\boldsymbol u(X_1,X_2,X_3)$$

# 5. 1차원 공간에서의 변형률

- 1차원 공간에서 위치는 스칼라 물릴량이 된다. $x$

- 변위도 scalar가 되며 아래와 같다

  $$u=x-X$$

- 두 점 a와 b의 초기 위치를 $X^a, X^b$, 변형 이후의 위치를 $x^a, x^b$라 할 때, 두 점 사이의 초기 거리는

$$X^b-X^a$$

- 변형 이후의 두 점사이의 거리는

$$x^b-x^a$$

- 변형 전후의 두 점 사이의 거리 변화는?

$$(x^b-x^a) - (X^b-X^a)$$

- 변형 이후의 두점 사이의 거리를 변형 전의 두점 사이의 거리로 나누면

$$
\frac{(x^b-x^a)-(X^b-X^a)}{X^b-X^a}
=\frac{u^b-u^a}{X^b-X^a}
$$

- 두 점 $a$와 $b$ 사이의 거리를 매우 작게 하면, 두 점의 상대변위 변화율로 한 점에서의
  국소 변형률을 정의할 수 있다.

$$
\lim_{a\rightarrow b}\frac{u^b-u^a}{X^b-X^a}
=\frac{du}{dX}
$$

- 위 식은 변형 전 기준좌표 $X$를 사용하는 미소변형률 표현이다. 변형이 매우 작으면
  $X$와 현재좌표 $x$의 차이가 작아 $du/dX\approx du/dx$로 볼 수 있다.

- 엔지니어링 변형률은

$$\varepsilon = \Delta l / l_0$$

- $\varepsilon = \Delta l / l_0$ 와 $\frac{du}{dx}$의 유사성을 생각해보자.

# 6. 1차원 예제

- 변위장이 위치 $x$에 대해 선형적으로 증가하는 경우를 생각해보자.

 $$u(x) = 0.01 x$$

- 변위장의 기울기(변위구배)는

 $$\frac{du}{dx} = 0.01 $$

- 예제

  - 다음 환경에서 변형률은 얼마인가?

  $$u(x)=0$$

  - 다음 환경에서 변형률은 얼마인가?
    $$u(x)=0.02$$

# 7. 2차원 공간에서의 변위

- 변위 장(displacement field)은 위치 장(position field)에 대한 함수이다.

$$\boldsymbol u(\boldsymbol x)$$

- 변위 $\boldsymbol u$도 2차원 벡터, 위치 $\boldsymbol x$도 2차원 벡터이다.

$$\boldsymbol u =
\begin{bmatrix}
u_1\\u_2
\end{bmatrix}$$

$$\boldsymbol x =
\begin{bmatrix}
x_1\\x_2
\end{bmatrix}$$

- 2차원에서의 수직 변형률 성분은

$$\varepsilon_{11}=\partial u_1/\partial x_1$$

$$\varepsilon_{22}=\partial u_2/\partial x_2$$

- 2차원에서의 전단 변형률 성분은

$$\varepsilon_{12}=\frac{1}{2}(\partial u_1/\partial x_2+\partial u_2/\partial x_1)$$

$$\varepsilon_{21}=\frac{1}{2}(\partial u_2/\partial x_1+\partial u_1/\partial x_2)$$

위 두 식의 우변은 사실 같다. 따라서,

$$\varepsilon_{12}=\varepsilon_{21}$$

- 예제

  - 다음 2차원 환경에서 보이는 변위 장에 대한 변형률을 계산해 보시오.

    $$u_1(x_1,x_2)=0.2 x_1$$
    $$u_2(x_1,x_2)=0.3 x_2$$

  - 다음 2차원 환경에서 보이는 변위 장에 대한 변형률을 계산해 보시오.

    $$u_1(x_1,x_2)=0.1 x_1 + 0.05 x_2$$
    $$u_2(x_1,x_2)=0.2 x_1 + 0.05 x_2$$

![두 가지 선형 변위장에 의한 2차원 물체의 변형 전후 형상](/assets/img/lecture_notes/displacement/displacement_field_2d_examples.png)



# 8. 변위구배의 대칭부분과 반대칭부분

변위구배는 물체의 작은 변형과 작은 회전을 함께 포함한다.

$$
\nabla\boldsymbol u
=\boldsymbol\varepsilon+\boldsymbol\omega
$$

$$
\boldsymbol\varepsilon
=\frac{1}{2}\left(\nabla\boldsymbol u+(\nabla\boldsymbol u)^T\right),
\qquad
\boldsymbol\omega
=\frac{1}{2}\left(\nabla\boldsymbol u-(\nabla\boldsymbol u)^T\right)
$$

$\boldsymbol\varepsilon$은 길이와 각도의 변화를, 반대칭 텐서
$\boldsymbol\omega$는 미소 강체회전을 나타낸다. 따라서 강체회전을 변형률에 포함하지
않으려면 대칭부분만 취해야 한다.

공학전단변형률 $\gamma_{12}$와 텐서 전단변형률의 관계는

$$
\gamma_{12}=2\varepsilon_{12}
$$

이다. Voigt 표기에서 전단성분을 사용할 때 이 2의 계수를 빠뜨리지 않도록 주의한다.

# 9. 2차원 예제

- 아래의 상황이라면..

$$u_1(x_1,x_2)=0.5x_1 + 0x_2$$

$$u_2(x_1,x_2)=0x_1-0.5x_2$$

- $\varepsilon_{11}$ 값은?

- $\varepsilon_{12}$ 값은?

- $\varepsilon_{21}$ 값은?

- $\varepsilon_{22}$ 값은?

- 아래의 상황이라면...

$$u_1(x_1,x_2)=0.5x_1x_2$$

$$u_2(x_1,x_2)=0.01x_2$$

- 변형률이 위치에 따라 달리지는 것을 보일 수 있나?

# 10. 요약

| 개념                          | 공식                                                                         |
| ----------------------------- | ---------------------------------------------------------------------------- |
| 변위                          | $u = x - X$                                                                  |
| 1차원 변형률                  | $\varepsilon = du/dx$                                                        |
| $\boldsymbol{e}_1$방향 수직변형률 | $\varepsilon_{11} = \partial u_1/\partial x_1$                               |
| $\boldsymbol{e}_2$방향 수직변형률 | $\varepsilon_{22} = \partial u_2/\partial x_2$                               |
| 전단변형률                    | $\varepsilon_{12} =0.5(\partial u_1/\partial x_2+\partial u_2/\partial x_1)$ |

# 11. 연습 문제

## 문제 1

모든 점이 같은 크기와 방향으로 이동하는 병진운동에서 변형률이 0인 이유를 설명하라.

<!--
풀이와 해답:
점 사이의 상대적인 거리와 각도가 변하지 않고 변위의 공간 미분도 0이기 때문이다.
-->

## 문제 2

1차원 막대의 변위가 $u(x)=0.01x$일 때 미소변형률을 구하라.

<!--
풀이와 해답:
epsilon=du/dx=0.01이다.
-->

## 문제 3

변위가 $u(x)=0.002x^2$일 때 $x=10$에서의 미소변형률을 구하라.

<!--
풀이와 해답:
epsilon=du/dx=0.004x이므로 x=10에서 0.04이다.
-->

## 문제 4

강체회전이 물체의 변형률을 만들지 않는 이유를 한 문장으로 설명하라.

<!--
풀이와 해답:
강체회전은 물체 내부의 길이와 각도를 바꾸지 않기 때문이다.
-->

## 문제 5

한 점의 변형 전 위치가 $\boldsymbol X=(1,2,3)^T$ mm이고 변형 후 위치가
$\boldsymbol x=(2,4,3)^T$ mm이다. 변위벡터를 구하시오.

<!--
풀이와 해답:
u=x-X=(2-1,4-2,3-3)^T=(1,2,0)^T mm이다.
-->

## 문제 6

초기 위치가 $X^a=0$ mm, $X^b=100$ mm인 두 점의 변위가 각각
$u^a=2$ mm, $u^b=3$ mm이다. 두 점 사이의 공칭변형률을 구하시오.

<!--
풀이와 해답:
두 점의 상대변위는 3-2=1 mm이고 초기 거리는 100 mm이다.
따라서 변형률은 1/100=0.01이다. 두 점에 공통인 2 mm 병진성분은 변형률에 기여하지 않는다.
-->

## 문제 7

1차원 변위장이 $u(X)=5$ mm로 위치와 관계없이 일정하다. 미소변형률을 구하고 이 운동을
설명하시오.

<!--
풀이와 해답:
du/dX=0이므로 변형률은 0이다. 모든 점이 같은 양만큼 이동하는 강체 병진이다.
-->

## 문제 8

1차원 변위장이 $u(X)=0.001X^2$일 때 변형률 분포를 구하고 $X=10$에서의 값을
계산하시오.

<!--
풀이와 해답:
epsilon=du/dX=0.002X이다. X=10에서는 epsilon=0.02이다.
위치에 따라 변형률이 달라지는 비균일 변형이다.
-->

## 문제 9

다음 2차원 변위장에서 변위구배와 미소변형률 텐서를 구하시오.

$$
u_1=0.02x_1,
\qquad
u_2=-0.01x_2
$$

<!--
풀이와 해답:
변위구배는 [[0.02,0],[0,-0.01]]이다. 이미 대칭이므로 변형률 텐서도
[[0.02,0],[0,-0.01]]이다. 1방향은 인장되고 2방향은 압축된다.
-->

## 문제 10

다음 단순전단 변위장에서 $\varepsilon_{12}$와 공학전단변형률 $\gamma_{12}$를
구하시오.

$$
u_1=0.04x_2,
\qquad
u_2=0
$$

<!--
풀이와 해답:
partial u1/partial x2=0.04이고 partial u2/partial x1=0이다.
따라서 epsilon_12=(0.04+0)/2=0.02이고 gamma_12=2epsilon_12=0.04이다.
-->

## 문제 12

다음 미소 강체회전 변위장의 변형률 텐서가 0임을 보이시오. 여기서 $\theta$는 작은
회전각이다.

$$
u_1=-\theta x_2,
\qquad
u_2=\theta x_1
$$

<!--
풀이와 해답:
변위구배는 [[0,-theta],[theta,0]]으로 반대칭이다.
대칭부분 (grad u + grad u^T)/2는 영행렬이므로 변형률 텐서는 0이다.
반대칭부분에는 강체회전만 남는다.
-->

## 문제 13

다음 변위장에서 미소변형률 텐서와 미소회전 텐서를 구하시오.

$$
u_1=0.01x_1-0.02x_2+1,
\qquad
u_2=0.02x_1+0.03x_2-2
$$

<!--
풀이와 해답:
변위구배는 [[0.01,-0.02],[0.02,0.03]]이다.
대칭부분인 변형률은 [[0.01,0],[0,0.03]]이고,
반대칭부분인 회전은 [[0,-0.02],[0.02,0]]이다.
상수 1과 -2는 병진이므로 두 텐서에 영향을 주지 않는다.
-->

## 문제 14

3차원 변위장이 다음과 같을 때 체적변형률의 미소변형 근사
$\varepsilon_v=\operatorname{tr}(\boldsymbol\varepsilon)$를 구하시오.

$$
u_1=0.01x_1,
\qquad
u_2=0.02x_2,
\qquad
u_3=-0.005x_3
$$

<!--
풀이와 해답:
수직변형률은 각각 0.01, 0.02, -0.005이다.
따라서 체적변형률은 trace(epsilon)=0.01+0.02-0.005=0.025이다.
-->

## 문제 15

다음 변위장이 미소 비압축성 조건을 만족하도록 상수 $a$를 구하시오.

$$
u_1=0.02x_1,
\qquad
u_2=-0.01x_2,
\qquad
u_3=ax_3
$$

<!--
풀이와 해답:
미소 비압축성 조건은 trace(epsilon)=0이다.
0.02-0.01+a=0이므로 a=-0.01이다.
-->

## 문제 16

다음 비균일 변위장의 변형률 성분을 구하고 $(x_1,x_2)=(2,1)$에서 평가하시오.

$$
u_1=0.5x_1x_2,
\qquad
u_2=0.01x_2
$$

<!--
풀이와 해답:
epsilon_11=partial u1/partial x1=0.5x2,
epsilon_22=partial u2/partial x2=0.01,
epsilon_12=(partial u1/partial x2+partial u2/partial x1)/2=0.25x1이다.
(x1,x2)=(2,1)에서는 epsilon_11=0.5, epsilon_22=0.01,
epsilon_12=0.5이다.
-->

## 문제 17

변위장에 임의의 상수 병진벡터 $\boldsymbol c$를 더해
$\boldsymbol u^{new}(\boldsymbol x)=\boldsymbol u(\boldsymbol x)+\boldsymbol c$로 만들었다.
변형률 텐서가 바뀌는지 설명하시오.

<!--
풀이와 해답:
상수벡터 c의 공간미분은 0이므로 변위구배와 변형률 텐서는 바뀌지 않는다.
변형률은 절대변위가 아니라 위치에 따른 상대변위 변화로 결정된다.
-->
