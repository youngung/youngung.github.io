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
- [7. 1차원 예제](#7-1차원-예제)
- [8. 2차원 공간에서의 변위](#8-2차원-공간에서의-변위)
- [9. 2차원 예제](#9-2차원-예제)
- [10. 요약](#10-요약)

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

$$\frac{(x^b-x^a) - (X^b-X^a)} {x^b-x^a}=\frac{u^b-u^a}{x^b-x^a}$$

- a와 b점이 가까워 지면??

$$\lim_{a \rightarrow b} \frac{u^b-u^a}{x^b-x^a}=\frac{du}{dx}$$

- 엔지니어링 변형률은

$$\varepsilon = \Delta l / l_0$$

- $\varepsilon = \Delta l / l_0$ 와 $\frac{du}{dx}$의 유사성을 생각해보자.

# 6. 1차원 예제

- $$u(x) = 0.01 x$$

- $$\frac{du}{dx} = 0.01 $$

- 다음 환경에서 변형률은 얼마인가?
  $$u(x)=0$$

- 다음 환경에서 변형률은 얼마인가?
  $$u(x)=0.02$$

# 7. 2차원 공간에서의 변위

- 변위 장
  (displacement field)은 위치 장(position field)에 대한 함수.

$$\boldsymbol u(\boldsymbol x)$$

- 변위 $\boldsymbol u$도 2차원 벡터, 위치 $\boldsymbol x$도 2차원 벡터이다.

$$\boldsymbol u =
\begin{bmatrix}
u_1&u_2
\end{bmatrix}$$

$$\boldsymbol x =
\begin{bmatrix}
x_1&x_2
\end{bmatrix}$$

- 2차원에서의 수직 변형률 성분은

$$\varepsilon_{11}=\partial u_1/\partial x_1$$

$$\varepsilon_{22}=\partial u_2/\partial x_2$$

- 2차원에서의 전단 변형률 성분은

$$\varepsilon_{12}=\frac{1}{2}(\partial u_1/\partial x_2+\partial u_2/\partial x_1)$$

$$\varepsilon_{21}=\frac{1}{2}(\partial u_2/\partial x_1+\partial u_1/\partial x_2)$$

위 두 식의 우변은 사실 같다. 따라서,

$$\varepsilon_{12}=\varepsilon_{21}$$

# 8. 2차원 예제

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

# 9. 요약

| 개념                          | 공식                                                                         |
| ----------------------------- | ---------------------------------------------------------------------------- |
| 변위                          | $u = x - X$                                                                  |
| 1차원 변형률                  | $\varepsilon = du/dx$                                                        |
| $\boldsymbol{e}_1$방향 수직변형률 | $\varepsilon_{11} = \partial u_1/\partial x_1$                               |
| $\boldsymbol{e}_2$방향 수직변형률 | $\varepsilon_{22} = \partial u_2/\partial x_2$                               |
| 전단변형률                    | $\varepsilon_{12} =0.5(\partial u_1/\partial x_2+\partial u_2/\partial x_1)$ |

# 10. 연습 문제

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
