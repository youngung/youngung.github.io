---
layout: distill
title: 벡터 연산 기초
description: NumPy를 이용한 벡터의 합, 크기, 내적과 외적
target: 1학년 2학기
permalink:
featured: true
prerequisite: NumPy 배열 기초, NumPy 배열 활용
toc:
  sidebar: left
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

- [1. 학습 목표](#1-학습-목표)
- [2. 벡터와 NumPy 배열](#2-벡터와-numpy-배열)
- [3. 벡터의 합과 차](#3-벡터의-합과-차)
- [4. 스칼라와 벡터의 곱](#4-스칼라와-벡터의-곱)
- [5. 벡터의 크기](#5-벡터의-크기)
- [6. 단위벡터](#6-단위벡터)
- [7. 내적](#7-내적)
- [8. 두 벡터 사이의 각](#8-두-벡터-사이의-각)
- [9. 외적](#9-외적)
- [10. 재료공학 예제](#10-재료공학-예제)
  - [10.1. 두 힘의 합력](#101-두-힘의-합력)
  - [10.2. 입방정에서 결정방향 사이의 각](#102-입방정에서-결정방향-사이의-각)
  - [10.3. 평행사변형의 넓이](#103-평행사변형의-넓이)
- [11. 자주 하는 실수](#11-자주-하는-실수)
- [12. 정리](#12-정리)
- [13. 연습 문제](#13-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)
  - [문제 7](#문제-7)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 벡터를 1차원 NumPy 배열로 나타낼 수 있다.
- 벡터의 합, 차와 스칼라 곱을 계산할 수 있다.
- 벡터의 크기와 단위벡터를 구할 수 있다.
- 내적을 이용하여 두 벡터의 수직 여부와 끼인 각을 구할 수 있다.
- 외적의 방향과 크기를 설명하고 NumPy로 계산할 수 있다.

# 2. 벡터와 NumPy 배열

벡터(vector)는 크기와 방향을 함께 나타내는 물리량이다. 3차원 벡터
$\boldsymbol a$는 다음과 같이 세 성분으로 나타낼 수 있다.

$$
[\boldsymbol a]=
\begin{bmatrix}
a_x\\a_y\\a_z
\end{bmatrix}
$$

Python에서는 1차원 NumPy 배열로 저장한다.

~~~python
import numpy as np
a = np.array([3.0, 4.0, 5.0])
print(a)
print(a.shape)
print(a.ndim)
~~~

벡터 성분은 앞선 강의에서 배운 인덱싱으로 선택한다.

~~~python
print(a[0])
print(a[1])
print(a[2])
~~~

# 3. 벡터의 합과 차

두 벡터의 합과 차는 같은 위치의 성분끼리 계산한다.

$$
\boldsymbol a+[\boldsymbol b]
=
\begin{bmatrix}
a_x+b_x\\
a_y+b_y\\
a_z+b_z
\end{bmatrix}
$$

~~~python
a = np.array([3.0, 4.0, 5.0])
b = np.array([3.0, -5.0, -2.0])

vector_sum = a + b
vector_difference = a - b

print(vector_sum)
print(vector_difference)
~~~

결과는 각각 $[6,-1,3]$과 $[0,9,7]$이다. 두 배열의 shape이 같아야 성분별로
자연스럽게 더하고 뺄 수 있다.

# 4. 스칼라와 벡터의 곱

벡터에 하나의 수인 스칼라 $c$를 곱하면 모든 성분에 $c$가 곱해진다.

$$
c[\boldsymbol a]
=
\begin{bmatrix}
ca_x\\ca_y\\ca_z
\end{bmatrix}
$$

~~~python
a = np.array([1.0, 2.0, 3.0])
scaled = 0.5 * a

print(scaled)
~~~

이는 앞선 NumPy 강의에서 배운 배열과 스칼라의 브로드캐스팅이다. 양의 값을 곱하면
방향은 같고 크기가 변한다. 음의 값을 곱하면 방향도 반대가 된다.

# 5. 벡터의 크기

벡터 $\boldsymbol a$의 크기(Euclidean norm)는

$$
\|\boldsymbol a\|_2
=
\sqrt{a_x^2+a_y^2+a_z^2}
$$

이다.

줄여서 다음과 같이 표기하기도 한다.

$$
|\boldsymbol a|
$$

벡터 $(3,4,0)$의 크기를 직접 계산하면

$$
\sqrt{3^2+4^2+0^2}=5
$$

이다.

NumPy의 원소별 연산과 집계 연산을 이용할 수 있다.

~~~python
a = np.array([3.0, 4.0, 0.0])

magnitude = np.sqrt((a**2).sum())
print(magnitude)
~~~

NumPy가 제공하는 <code>np.linalg.norm()</code>을 사용하면 더 간단하다.

~~~python
magnitude = np.linalg.norm(a)
print(magnitude)
~~~

# 6. 단위벡터

크기가 1인 벡터를 단위벡터(unit vector)라고 한다. 0이 아닌 벡터를 그 크기로 나누면
같은 방향의 단위벡터를 얻는다.

$$
\widehat{\boldsymbol a}
=
\frac{\boldsymbol a}{\|\boldsymbol a\|_2}
$$

~~~python
def unit_vector(vector):
    magnitude = np.linalg.norm(vector)

    if magnitude == 0:
        raise ValueError("zero vector has no direction")

    return vector / magnitude


a = np.array([3.0, 4.0, 0.0])
a_unit = unit_vector(a)

print(a_unit)
print(np.linalg.norm(a_unit))
~~~

영벡터는 방향이 없으므로 단위벡터로 만들 수 없다.

# 7. 내적

두 벡터의 내적(dot product)은 같은 위치의 성분을 곱한 뒤 모두 더한 값이다.

$$
\boldsymbol a\mathbin{\cdot}\boldsymbol b
=
\sum_{i=1}^{n}a_i b_i
$$

3차원에서는

$$
\boldsymbol a\mathbin{\cdot}\boldsymbol b
=a_1b_1+a_2b_2+a_3b_3
$$

이다.

~~~python
a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])

dot_product = (a * b).sum()
print(dot_product)
~~~

NumPy에서는 다음 두 표현을 사용할 수 있다.

~~~python
print(np.dot(a, b))
print(a @ b)
~~~

결과는 모두 스칼라 32이다. <code>a * b</code>만 계산하면 합을 하지 않으므로
내적이 아니라 원소별 곱 배열이 나온다.

두 벡터가 모두 영벡터가 아니고 내적이 0이면 두 벡터는 서로 수직이다.

~~~python
x_direction = np.array([1.0, 0.0, 0.0])
y_direction = np.array([0.0, 1.0, 0.0])

print(x_direction @ y_direction)
~~~

# 8. 두 벡터 사이의 각

내적은 두 벡터 사이의 각 $\theta$와 다음 관계를 갖는다.

$$
\boldsymbol a\mathbin{\cdot}\boldsymbol b
=
|\boldsymbol a|
|\boldsymbol b|
\cos\theta
$$

따라서

$$
\theta
=
\cos^{-1}
\left(
\frac{\boldsymbol a\mathbin{\cdot}\boldsymbol b}
{|\boldsymbol a||\boldsymbol b|}
\right)
$$

이다.

~~~python
def angle_between(vector_a, vector_b):
    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("zero vector has no direction")

    cosine = (
        vector_a @ vector_b
        / (magnitude_a * magnitude_b)
    )

    cosine = np.clip(cosine, -1.0, 1.0)
    angle_rad = np.arccos(cosine)

    return np.degrees(angle_rad)


a = np.array([1.0, 0.0, 0.0])
b = np.array([0.0, 1.0, 0.0])

print(angle_between(a, b))
~~~

결과는 90도이다. <code>np.arccos()</code>의 결과는 radian이고,
<code>np.degrees()</code>가 degree로 변환한다. 부동소수점 계산 때문에 cosine이
아주 조금 1보다 커지거나 -1보다 작아지는 것을 막기 위해 <code>np.clip()</code>을 사용했다.

# 9. 외적

3차원 벡터의 외적(cross product)은 두 벡터에 모두 수직인 새로운 벡터이다.

$$
\boldsymbol a\times[\boldsymbol b]
=
\begin{bmatrix}
a_yb_z-a_zb_y\\
a_zb_x-a_xb_z\\
a_xb_y-a_yb_x
\end{bmatrix}
$$

~~~python
a = np.array([1.0, 0.0, 0.0])
b = np.array([0.0, 1.0, 0.0])

cross_product = np.cross(a, b)
print(cross_product)
~~~

결과는 $[0,0,1]$이다. 방향은 오른손 법칙을 따른다.

외적은 순서를 바꾸면 부호가 바뀐다.

$$
\boldsymbol b\times\boldsymbol a
=
-\boldsymbol a\times\boldsymbol b
$$

~~~python
print(np.cross(b, a))
~~~

외적의 크기는 두 벡터가 만드는 평행사변형의 넓이이다.

$$
|\boldsymbol a\times\boldsymbol b|
=
|\boldsymbol a|
|\boldsymbol b|
\sin\theta
$$

# 10. 재료공학 예제

## 10.1. 두 힘의 합력

한 점에 두 힘이 작용한다고 하자.

~~~python
force_1 = np.array([100.0, 0.0, 0.0])
force_2 = np.array([0.0, 50.0, 0.0])

resultant = force_1 + force_2
resultant_magnitude = np.linalg.norm(resultant)

print(resultant)
print(resultant_magnitude)
~~~

합력은 $[100,50,0]$ N이고 크기는 약 111.8 N이다.

## 10.2. 입방정에서 결정방향 사이의 각

입방정(cubic crystal)에서는 결정방향 $[uvw]$를 성분이 $(u,v,w)$인 벡터로
다룰 수 있다. $[100]$과 $[110]$ 사이의 각을 계산해 보자.

~~~python
direction_1 = np.array([1.0, 0.0, 0.0])
direction_2 = np.array([1.0, 1.0, 0.0])

angle_deg = angle_between(
    direction_1,
    direction_2,
)

print(angle_deg)
~~~

결과는 45도이다. 비입방정(non-cubic)에서는 격자상수를 고려해야 하므로 같은 방법을 그대로 적용할 수 없다.

## 10.3. 평행사변형의 넓이

두 격자벡터가 만드는 평행사변형의 넓이는 외적의 크기로 구할 수 있다.

~~~python
lattice_a = np.array([2.0, 0.0, 0.0])
lattice_b = np.array([0.0, 3.0, 0.0])

area = np.linalg.norm(
    np.cross(lattice_a, lattice_b)
)

print(area)
~~~

넓이는 6이다. 격자벡터의 단위가 nm라면 넓이 단위는 nm²이다.

# 11. 자주 하는 실수

- 두 벡터의 shape이 서로 다른데 성분별 연산을 시도한다.
- <code>a * b</code>를 내적이라고 생각한다.
- 영벡터를 크기로 나누어 단위벡터를 만들려고 한다.
- radian과 degree를 구분하지 않는다.
- 외적에서 벡터 순서를 바꾸어도 결과가 같다고 생각한다.
- 배열 차원(<code>ndim</code>)과 물리학적 벡터 차원을 혼동한다.

# 12. 정리

- 벡터는 1차원 NumPy 배열로 나타낼 수 있다.
- 벡터의 합과 차는 같은 위치의 성분끼리 계산한다.
- <code>np.linalg.norm()</code>은 벡터의 크기를 계산한다.
- 단위벡터는 벡터를 그 크기로 나누어 구한다.
- 내적 결과는 스칼라이며 두 벡터의 끼인 각과 관계된다.
- 외적 결과는 두 입력 벡터에 모두 수직인 벡터이다.

# 13. 연습 문제

## 문제 1

두 벡터 $\boldsymbol a=(1,2,3)$과 $\boldsymbol b=(2,0,1)$의 합을 구하라.

<!--
풀이와 해답:
a+b=(3,2,4)이다.
-->

## 문제 2

벡터 $(3,4,0)$의 크기를 구하라.

<!--
풀이와 해답:
sqrt(3^2+4^2)=5이다.
-->

## 문제 3

벡터 <code>a</code>의 크기를 NumPy로 계산하는 표현을 쓰시오.

<!--
풀이와 해답:
np.linalg.norm(a)
-->

## 문제 4

$\boldsymbol a=(1,0,0)$과 $\boldsymbol b=(0,2,0)$의 내적을 구하라.

<!--
풀이와 해답:
내적은 0이다. 두 벡터는 서로 수직이다.
-->

## 문제 5

다음 코드에서 <code>a * b</code>와 <code>a @ b</code>의 결과를 각각 구하라.

~~~python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
~~~

<!--
풀이와 해답:
a*b는 [4,10,18]이고 a@b는 32이다.
-->

## 문제 6

$\boldsymbol a=(1,0,0)$과 $\boldsymbol b=(0,1,0)$의 외적을 구하라.

<!--
풀이와 해답:
a cross b=(0,0,1)이다.
-->

## 문제 7

<code>np.arccos()</code>가 반환한 각도의 기본 단위는 무엇인가?

<!--
풀이와 해답:
radian이다.
-->
