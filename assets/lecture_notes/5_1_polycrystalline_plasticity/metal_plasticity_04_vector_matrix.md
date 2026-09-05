---
layout: distill
title: 벡터와 행렬
description: 소성역학에 필요한 벡터, 행렬 및 텐서 연산
target: 학부 고학년
permalink:
featured: true
prerequisite: 기초수학, 응력과 변형률
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

- [1. 물리량의 종류](#1-물리량의-종류)
- [2. 스칼라와 벡터](#2-스칼라와-벡터)
- [3. 좌표계 (coordinate system)](#3-좌표계-coordinate-system)
- [4. 스칼라 연산](#4-스칼라-연산)
  - [4.1. 더하기](#41-더하기)
  - [4.2. 빼기](#42-빼기)
  - [4.3. 곱하기](#43-곱하기)
  - [4.4. 나누기](#44-나누기)
- [5. 벡터 연산](#5-벡터-연산)
  - [5.1. 벡터의 크기](#51-벡터의-크기)
  - [5.2. 더하기, 빼기](#52-더하기-빼기)
  - [5.3. 벡터와 스칼라 곱](#53-벡터와-스칼라-곱)
  - [5.4. 내적](#54-내적)
  - [5.5. 외적](#55-외적)
  - [5.6. 다이아딕 곱하기](#56-다이아딕-곱하기)
- [6. 매트릭스 연산](#6-매트릭스-연산)
  - [6.1. 더하기, 빼기](#61-더하기-빼기)
  - [6.2. 스칼라 곱하기](#62-스칼라-곱하기)
  - [6.3. 매트릭스 곱하기1 (single contraction)](#63-매트릭스-곱하기1-single-contraction)
  - [6.4. 매트릭스 곱하기2 (double contraction)](#64-매트릭스-곱하기2-double-contraction)
  - [6.5. 매트릭스 전치 (transpose)](#65-매트릭스-전치-transpose)
  - [6.6. 매트릭스 trace](#66-매트릭스-trace)
  - [6.7. 역행렬 (inverse matrix)](#67-역행렬-inverse-matrix)
- [7. Determinant](#7-determinant)
  - [7.1. $2\\times2$ 행렬](#71-2times2-행렬)
  - [7.2. $3\\times3$ 행렬](#72-3times3-행렬)
- [8. 랭크의 증감](#8-랭크의-증감)
- [9. Einstein 표기법](#9-einstein-표기법)

# 1. 물리량의 종류

- 물리량은 때로는 스칼라, 벡터로 표현해야 할 때가 있다.

- 더욱 일반적인 물리량 표현법은 '텐서'이다. 텐서는 스칼라 벡터를 모두 통합하여 설명한다.

- 텐서의 가장 큰 특징은 '좌표계'에 상관없이 동일한 물리량을 표현한다는 점이다 (좌표계에 무관한 성질)

- (advanced concept) 텐서가 좌표계에 독립적인 성질을 갖는 방법은, 좌표계에 따라 '변환'하기 때문에 가능하다.

# 2. 스칼라와 벡터

- 자극, 반응, 그리고 물질의 성질 모두 '물리량'으로써 그 세기나 크기를 표현한 '값'(value)으로 표현된다.

- 스칼라(scalar) 물리량은 해당 물리량이 '방향'과 관련된 성질을 갖지 않을 때 활용된다. (예: 질량, 밀도)

- 만약 물리량이 '방향'에 따라 달라진다면 (방향성을 가진다면), 스칼라 물리량만으로 온전히 물리량을 나타낼 수 없다.

- 그럴 경우, 벡터를 활용해 물리량의 세기/크기 뿐만 아니라 그 방향성(directionality)도 표현할 수 있겠다.

- 때로는 벡터 물리량만으로 그 방향성을 완전히 표현하기 힘든 물리량이 있으며, 이럴 때 우리는 '텐서'를 활용한다.

- 응력과 변형률은 대표적인 텐서 물리량이다.

- 텐서 물리량의 '연산'을 위해 이를 종종 매트릭스나 벡터로 나타내어 계산한다.

- 알파벳이나 그리스 알파벳 기호를 활용해 물리량을 표기한다.
  ($m$, $f$, $\alpha$, $\beta$ 등)

- 굵은 글씨체 (bold-face)를 활용해 '방향'성을 가진 물리량을 표기한다.
  ($a, \boldsymbol a, \alpha, {\boldsymbol \alpha}$)

- 윗첨자 혹은 아랫첨자를 활용해 벡터나 텐서, 혹은 매트릭스의 성분을 구분한다.
  ($a_1, \alpha^1, \beta_3, \gamma^1$ 등)

- 랭크
  - 첨자의 개수에 따라 랭크가 구분될 수 있다.
  - 스칼라는 첨자가 없다. 따라서, 랭크 0
  - 벡터는 첨자가 하나 있다. 따라서, 랭크 1
  - $3\times3$ 행렬은 첨자가 두개다. 따라서 랭크 2

# 3. 좌표계 (coordinate system)

- 좌표계는 서로 구분되는 여러 좌표축(axis)으로 이루어진다.

- '방향성'을 가진 물리량을 표현하기 위해서는 좌표계가 필요하다.

- 좌표계는 순전히 '편의'에 의해 선택되며 우리는 '직각좌표계'를 중심으로 활용하겠다.
  그외 다양한 좌표계도 있음을 잊지 말자.

- 우리가 사용하는 직각 좌표계의 좌표 축은 세 unit vector로, 서로 수직이다.

# 4. 스칼라 연산

## 4.1. 더하기

- $1 + 3$

- $3 + b$

- $a + c$

## 4.2. 빼기

- $1 - 3$

- $3 - b$

- $a - c$

## 4.3. 곱하기

- $1 \times 3$

- $3 \times b$

- $a \times c$

혹은 문자로만 표현될 때, 곱셈 기호 $\times$를 생략하기도 한다.

- $c\times d=cd$

## 4.4. 나누기

- $1 \div 3$

- $3 / b$

- $\frac{a}{c}$

# 5. 벡터 연산

## 5.1. 벡터의 크기

- 벡터는 스칼라처럼 크기를 가지며 거기에 '방향'도 가진다.

- 한 벡터 $\boldsymbol a$ 의 크기는 아래와 같이 표기된다.
  $|\boldsymbol a|$

- 한 벡터 $\boldsymbol a$가 세 성분 $a_1, a_2, a_3$로 이루어진다면 그 크기는
  아래와 같이 정의된다.

  $$|\boldsymbol a|=\sqrt{a_1^2+a_2^2+a_3^2}$$

- 위를 줄여서 아래와 같이 종종 표기한다.

  $$|\boldsymbol a|=\sqrt{\sum_{i=1}^3 a_i^2}$$

## 5.2. 더하기, 빼기

- 두 벡터의 더하기 빼기는 각각 $+$와 $-$기호로 표기한다.

$$\boldsymbol a + \boldsymbol b$$

$$\boldsymbol a - \boldsymbol b$$

- 벡터의 덧셈 뺄셈 연산은 결과는 또 다른 벡터이다.

  $$\boldsymbol c = \boldsymbol a + \boldsymbol b$$

  $$\boldsymbol d = \boldsymbol a - \boldsymbol b$$

- 한 벡터가 세 성분으로 이루어져 있다면, 위 더하기 빼기 연산을 각 성분에 대해
  아래와 같이 표기할 수도 있다.

  $$c_1 = a_1 + b_1$$

  $$c_2 = a_2 + b_2$$

  $$c_3 = a_3 + b_3$$

- 혹은 더욱 요약해서

  $$c_i=a_i+b_i \text{, with } i=1,2,3$$

- 덧셈의 교환 법칙이 성립한다.

  $$\boldsymbol a + \boldsymbol b = \boldsymbol b + \boldsymbol a$$

## 5.3. 벡터와 스칼라 곱

- 벡터와 스칼라 사이의 곱은 또 다른 벡터이다.

- 스칼라와의 곱에는 연산 기호가 생략된다.

  $$\boldsymbol c= d \boldsymbol b$$

- 교환 법칙이 성립한다.

  $$d \boldsymbol b = \boldsymbol b d$$

- 양의 스칼라 값이 곱해지면, 벡터의 방향은 그대로 유지되며 그 크기만 달라진다.

- 음의 스칼라 값이 곱해지면, 벡터의 방향이 반전되며 그 크기가 달라진다.

- $d=\pm 1$일하면, $\boldsymbol c$의 크기는 $\boldsymbol b$의 크기과 같다.

## 5.4. 내적

- 두 벡터 $\boldsymbol a$ 와 $\boldsymbol b$ 사이의 내적의 결과는 스칼라이며 이를 $c$라 한다면 아래와 같이 표기된다.

  $$c = \boldsymbol a \cdot \boldsymbol b$$

- 이는 아래와 같이 연산된다.

  $$c = \boldsymbol a \cdot \boldsymbol b = | \boldsymbol a| |\boldsymbol b|\cos\theta$$

- 이때 $\theta$는 두 벡터 $\boldsymbol a$와 $\boldsymbol b$ 사이의 끼인
  각이다.

- 내적은 다음과 같이 연산될 수도 있다.

  $$c = \boldsymbol a \cdot \boldsymbol b = \sum_{i=1}^3 a_ib_i = a_1b_1+a_2b_2+a_3b_3$$

- 따라서 얻어지는 다음 두 관계는 매우 유용하다.

  $$c = \boldsymbol a \cdot \boldsymbol b = | \boldsymbol a| |\boldsymbol b|\cos\theta=\sum_{i=1}^3 a_ib_i$$

## 5.5. 외적

- 두 벡터의 외적의 결과는 또 다른 벡터이다.

  - $\boldsymbol c = \boldsymbol a \times \boldsymbol b$

  - 그리고 그 벡터의 성분은 아래와 같이 정의된다.
    - $c_1 = a_2b_3-a_3b_2$
    - $c_2 = a_3b_1-a_1b_3$
    - $c_3 = a_1b_2-a_2b_1$

## 5.6. 다이아딕 곱하기

- 두 벡터의 다이아딕 곱하기 결과는 2차 텐서이며, 3차원 벡터 둘의 다이아딕 결과은 2차 텐서를 $3\times 3$ 행렬로 표기할 수 있다.

- 두 벡터 $\boldsymbol a$와 $\boldsymbol b$의 다이아딕 연산 결과를 2차 텐서 $\boldsymbol A$라 하면, 이를 행렬로 표기할 때 다음과 같이 정의된다.

$$\boldsymbol A = \boldsymbol a \otimes \boldsymbol b$$

$$A_{ij}= a_i b_j \text{ with } (i,j)=(1,1),(1,2),(1,3),(2,1) ... (3,3)$$

$$\text{혹은}$$

$$A_{ij}= a_i b_j \text{ with } i=1,2,3 \ \ \ j=1,2,3$$

# 6. 매트릭스 연산

## 6.1. 더하기, 빼기

- 같은 랭크의 매트릭스 $\boldsymbol A$와 $\boldsymbol B$의 합이나 차는 같은 랭크의 또 다른 매트릭스가 된다.

$$\boldsymbol C = \boldsymbol A + \boldsymbol B$$

$$\boldsymbol D = \boldsymbol A - \boldsymbol B$$

- 랭크 2인 행렬, 즉 $3\times3$ 행렬의 합과 차를 다음과 같이 연산한다.

$$C_{11}=A_{11}+B_{11}$$

$$C_{12}=A_{12}+B_{12}$$

$$C_{13}=A_{13}+B_{13}$$

$$C_{21}=A_{21}+B_{21}$$

$$C_{22}=A_{22}+B_{22}$$

$$C_{23}=A_{23}+B_{23}$$

$$C_{31}=A_{31}+B_{31}$$

$$C_{32}=A_{32}+B_{32}$$

$$C_{33}=A_{33}+B_{33}$$

- 위와 같은 표현을 너무 길다. 아래와 같이 축약해서 표기할 수 있다.

$$C_{ij}=A_{ij}+B_{ij} \text{ with } i=1,2,3, \ \ \ j=1,2,3$$

## 6.2. 스칼라 곱하기

- 매트릭스에 스칼라를 곱하면 같은 랭크의 다른 매트릭스가 된다.

$$\boldsymbol B = c \boldsymbol A $$

- 이는 아래와 같다.

$$B_{ij}=c A_{ij} \text{ with } i=1,2,3, \ \ \ j=1,2,3$$

## 6.3. 매트릭스 곱하기1 (single contraction)

- 랭크 2인 매트릭스에 벡터를 곱하면 벡터가 된다.

$$\boldsymbol b = \boldsymbol A \cdot \boldsymbol v$$

- 위는 아래와 같이 계산된다.

$$b_1 = \sum_{j=1}^3 A_{1j} v_j $$

$$b_2 = \sum_{j=1}^3 A_{2j} v_j $$

$$b_3 = \sum_{j=1}^3 A_{3j} v_j $$

- 따라서 축약하면

$$b_i = \sum_{j=1}^3 A_{ij} v_j \text{ with } i=1,2,3$$

- 아래의 경우를 살펴보자.

$$\boldsymbol c = \boldsymbol v \cdot \boldsymbol B$$

- 위를 앞선 인덱스 표기법을 적용하면 아래와 같다.

$$c_i = v_i B_{ij} $$

- 교환 법칙이 성립하지 않는다.

$$ \boldsymbol A\cdot \boldsymbol v \ne \boldsymbol v \cdot \boldsymbol A $$

## 6.4. 매트릭스 곱하기2 (double contraction)

- 앞서 곱셈이 한 첨자 기호에만 적용된 경우를 살펴보았다. 즉

$$d_i = \sum_{j=1}^3 A_{ij} b_j \text{ with } i=1,2,3$$

- 랭크2인 두 매트릭스 사이에서는 두 첨자 사이에 위와 같은 곱이 수행될 수 있으며, 그 결과는 스칼라가 된다.

$$c = A_{ij} B_{ij} = \sum_{i=1}^3 \sum_{j=1}^3 A_{ij}B_{ij}$$

- 위와 같은 곱하기를 아래와 같이 ':'기호를 활용해 표기하기도 한다.

$$
c=\boldsymbol A : \boldsymbol B
$$

- 랭크가 3인 매트릭스 $A_{ijk}$와 벡터 $\boldsymbol v$ 사이의 single contraction 곱을 생각해보자.

$$B_{ij} = \sum_{k=1}^3A_{ijk} b_k \text{ with } i=1,2,3,\ \ \ j=1,2,3$$

## 6.5. 매트릭스 전치 (transpose)

- 한 매트릭스 $\boldsymbol A$의 전치는 $\boldsymbol A^T$라 표기하고, 다음과 같이 정의된다.

$$
A^T_{ij}=A_{ji}, \text{ with } i=1,2,3 \ \ \ j=1,2,3
$$

## 6.6. 매트릭스 trace

- 한 매트릭스 $\boldsymbol A$의 trace는 $tr(\boldsymbol A)$라 표기하고, 다음과 같이 정의된다.

$$
tr(\boldsymbol A) = A_{11}+A_{22}+A_{33}=\sum_{i=1}^3A_{ii}
$$

## 6.7. 역행렬 (inverse matrix)

- 한 매트릭스 $\boldsymbol A$의 역은 $\boldsymbol A^{-1}$라 표기하고, 다음의 성질을 만족한다.

$$
\boldsymbol{A}\cdot\boldsymbol{A}^{-1}=\boldsymbol {I}
$$

- 즉
$$
\sum_{k=1}^3A_{ik}A^{-1}_{kj}=I_{ij} \text{ with } i=1,2,3\ \ \ \ j=1,2,3
$$

# 7. Determinant

## 7.1. $2\times2$ 행렬

$$
\boldsymbol A=\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

$$
\det(\boldsymbol A) = |\boldsymbol A| = ad -bc
$$

## 7.2. $3\times3$ 행렬

$$
\boldsymbol A=\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
$$

$$
\det(\boldsymbol A)=|\boldsymbol A| = a(ei-fh)-b(di-fg)+c(dh-eg)
$$


# 8. 랭크의 증감

- Contraction: 물리량들 사이에 곱을 통해 랭크가 감소하는 경우

  - $a_i = \sum_{j=1}^3A_{ij}b_j\ \ \text{ with }\ i=1,2,3$

- Outer product: 물리량들 사이에 곱을 통해 랭크가 증가하는 경우

  - $A_{ij}=a_ib_j\ \ \text{ with } i=1,2,3,\ \ \ j=1,2,3$

- 랭크가 유지되는 경우
  - $b_i=ca_i \ \ \text{ with } i=1,2,3$

# 9. Einstein 표기법

- Einstein 합 규약에서는 한 항에 같은 첨자가 두 번 나타나면 그 첨자에 대해 합을 취한 것으로 약속한다.

- 아래 각 결과가 무엇이 될까? 그리고 그 결과는 몇 **랭크**의 물리량이 될까?

$$ a_{ijk} b_{i} $$

$$ a_{ijk} b_{jk} $$

$$ a_{ijk} b_{ik} $$

$$ a_{ijk} b_{ijk} $$

# 10. 연습 문제

## 문제 1

벡터 $\boldsymbol a=(3,4,0)$의 크기를 구하라.

<!--
풀이와 해답:
벡터의 크기는 sqrt(3^2+4^2)=5이다.
-->

## 문제 2

$\boldsymbol a=(1,0,0)$과 $\boldsymbol b=(0,2,0)$의 내적을 구하고 두 벡터의 관계를 설명하라.

<!--
풀이와 해답:
내적은 0이다. 두 벡터는 서로 수직이다.
-->

## 문제 3

$\boldsymbol a=(1,0,0)$과 $\boldsymbol b=(0,1,0)$의 외적을 구하라.

<!--
풀이와 해답:
a cross b=(0,0,1)이다.
-->

## 문제 4

단위행렬 $\boldsymbol I$와 임의의 벡터 $\boldsymbol a$의 곱 $\boldsymbol I\boldsymbol a$는 무엇인가?

<!--
풀이와 해답:
원래 벡터 a와 같다.
-->
