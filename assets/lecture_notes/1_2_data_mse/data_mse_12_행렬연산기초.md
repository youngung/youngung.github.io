---
layout: distill
title: 행렬 연산 기초
description: NumPy를 이용한 행렬–벡터곱과 행렬곱
target: 1학년 2학기
permalink:
featured: true
prerequisite: NumPy 배열 활용, 벡터 연산 기초
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
- [2. 행렬과 NumPy 배열](#2-행렬과-numpy-배열)
- [3. 행렬의 합과 원소별 곱](#3-행렬의-합과-원소별-곱)
- [4. 행렬–벡터곱](#4-행렬벡터곱)
- [\\boldsymbol A\\boldsymbol x](#boldsymbol-aboldsymbol-x)
- [\\end{bmatrix}](#endbmatrix)
- [5. 행렬곱](#5-행렬곱)
- [\\boldsymbol C](#boldsymbol-c)
- [\\boldsymbol A\\cdot\\boldsymbol B](#boldsymbol-acdotboldsymbol-b)
- [C\_{ij}](#c_ij)
- [C\_{ij}](#c_ij-1)
- [6. 행렬곱의 shape](#6-행렬곱의-shape)
- [7. 단위행렬과 전치행렬](#7-단위행렬과-전치행렬)
  - [7.1. 단위행렬](#71-단위행렬)
  - [7.2. 전치행렬](#72-전치행렬)
- [8. 행렬식과 역행렬](#8-행렬식과-역행렬)
  - [8.1. 행렬식](#81-행렬식)
  - [8.2. 역행렬](#82-역행렬)
- [\\boldsymbol A^{-1}\\boldsymbol A](#boldsymbol-a-1boldsymbol-a)
- [9. 연립방정식 풀기](#9-연립방정식-풀기)
- [10. 재료공학 예제](#10-재료공학-예제)
  - [10.1. 격자 좌표를 실제 위치로 변환하기](#101-격자-좌표를-실제-위치로-변환하기)
  - [10.2. 두 격자점 사이의 거리](#102-두-격자점-사이의-거리)
- [11. 자주 하는 실수](#11-자주-하는-실수)
- [12. 정리](#12-정리)
- [13. 쉬운 연습 문제](#13-쉬운-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)
  - [문제 7](#문제-7)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 행렬을 2차원 NumPy 배열로 나타낼 수 있다.
- 원소별 곱과 행렬곱을 구분할 수 있다.
- 행렬–벡터곱과 행렬곱을 손으로 계산하고 NumPy로 확인할 수 있다.
- 행렬곱이 가능한 shape 조건을 판단할 수 있다.
- 단위행렬, 전치행렬, 행렬식과 역행렬의 의미를 설명할 수 있다.
- <code>np.linalg.solve()</code>로 간단한 연립방정식을 풀 수 있다.

# 2. 행렬과 NumPy 배열

$m$행 $n$열의 행렬은 $m\times n$ 행렬이라고 한다.

$$
\boldsymbol A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
$$

은 2행 3열 행렬이다.

~~~python
import numpy as np
A = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
])

print(A)
print(A.shape)
print(A.ndim)
~~~

<code>A.shape</code>은 <code>(2, 3)</code>이고 <code>A.ndim</code>은 2이다.
행렬 성분 $A_{ij}$는 Python에서 <code>A[i, j]</code>로 선택한다. 다만 수학에서 첨자는
1부터, Python의 인덱스는 0부터 시작한다.

~~~python
print(A[0, 0])
print(A[1, 2])
~~~

# 3. 행렬의 합과 원소별 곱

shape이 같은 두 행렬의 합과 차는 같은 위치의 성분끼리 계산한다.

~~~python
A = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
])
B = np.array([
    [5.0, 6.0],
    [7.0, 8.0],
])

print(A + B)
print(A - B)
~~~

별표 연산자 <code>*</code>는 행렬곱이 아니라 원소별 곱을 계산한다.

~~~python
elementwise_product = A * B
print(elementwise_product)
~~~

결과는

$$
\begin{bmatrix}
5&12\\
21&32
\end{bmatrix}
$$

이다.

# 4. 행렬–벡터곱

행렬

$$
\boldsymbol A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

와 벡터

$$
\boldsymbol x=
\begin{bmatrix}
5\\6
\end{bmatrix}
$$

의 곱은 각 행과 벡터의 내적으로 계산한다.

$$
\boldsymbol A\boldsymbol x
=
\begin{bmatrix}
1\times5+2\times6\\
3\times5+4\times6
\end{bmatrix}
=
\begin{bmatrix}
17\\39
\end{bmatrix}
$$

~~~python
A = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
])
x = np.array([5.0, 6.0])

result = A @ x

print(result)
print(result.shape)
~~~

$(m,n)$ 행렬과 shape이 $(n,)$인 벡터를 곱하면 shape이 $(m,)$인 벡터가 나온다.

# 5. 행렬곱

두 행렬

$$
\boldsymbol A=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix},
\qquad
\boldsymbol B=
\begin{bmatrix}
2&0\\
1&3
\end{bmatrix}
$$

의 곱을 생각하자. 결과의 각 성분은 $A$의 한 행과 $B$의 한 열의 내적이다.

$$
\begin{aligned}
C_{11}&=1\times2+2\times1=4,\\
C_{12}&=1\times0+2\times3=6,\\
C_{21}&=3\times2+4\times1=10,\\
C_{22}&=3\times0+4\times3=12.
\end{aligned}
$$

따라서

$$
\boldsymbol C
=
\boldsymbol A\cdot\boldsymbol B
=
\begin{bmatrix}
4&6\\
10&12
\end{bmatrix}
$$

이다.

~~~python
A = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
])
B = np.array([
    [2.0, 0.0],
    [1.0, 3.0],
])

C = A @ B

print(C)
~~~

일반적으로 $A$가 $(l,m)$ 행렬이고 $B$가 $(m,n)$ 행렬이면

$$
C_{ij}
=
\sum_{k=1}^{m}A_{ik}B_{kj}
$$

이고 결과 $C$의 크기는 $(l,n)$이다.

$$
C_{ij}
=
\sum_{k=1}^{m}A_{ik}B_{kj}

\text{ with } i=1,2,..., l \ \ j=1,2,...,n
$$


학습을 위해 반복문으로 같은 계산을 구현하면 다음과 같다.

~~~python
rows_a, columns_a = A.shape
rows_b, columns_b = B.shape

C_loop = np.zeros((rows_a, columns_b))

for i in range(rows_a):
    for j in range(columns_b):
        for k in range(columns_a):
            C_loop[i, j] += A[i, k] * B[k, j]

print(C_loop)
print(np.allclose(C, C_loop))
~~~

실제 계산에서는 반복문보다 <code>A @ B</code>를 사용한다. 연산 속도가 더 빠르다.

# 6. 행렬곱의 shape

행렬곱에서는 안쪽 크기가 같아야 한다.

$$
(l,m)(m,n)\rightarrow(l,n)
$$

예를 들어 다음 곱은 가능하다.

~~~python
A = np.ones((2, 3))
B = np.ones((3, 4))

C = A @ B

print(C.shape)
~~~

$(2,3)(3,4)$의 안쪽 크기 3이 같고 결과 shape은 $(2,4)$이다.

다음 곱은 안쪽 크기가 다르므로 계산할 수 없다.

~~~text
(2, 3) @ (2, 4)
~~~

행렬곱은 일반적으로 순서를 바꿀 수 없다.

$$
\boldsymbol A\cdot \boldsymbol B
\ne
\boldsymbol B\cdot \boldsymbol A
$$

shape에 따라 한쪽 순서의 곱만 가능한 경우도 있다.

# 7. 단위행렬과 전치행렬

## 7.1. 단위행렬

단위행렬(identity matrix)은 대각성분이 1이고 나머지가 0인 정사각행렬이다.

~~~python
I = np.eye(3)
x = np.array([2.0, 3.0, 4.0])

print(I)
print(I @ x)
~~~

단위행렬을 곱하면 원래 벡터나 행렬이 유지된다.

$$
\boldsymbol I\cdot \boldsymbol x=\boldsymbol x
$$

## 7.2. 전치행렬

전치(transpose)는 행과 열을 바꾼다.

~~~python
A = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
])

A_transpose = A.T

print(A.shape)
print(A_transpose.shape)
print(A_transpose)
~~~

$(2,3)$ 행렬의 전치는 $(3,2)$ 행렬이다.

# 8. 행렬식과 역행렬

## 8.1. 행렬식

행렬식(determinant)은 정사각행렬에 대해 정의되는 스칼라이다. 2×2 행렬에서는

$$
\det
\begin{bmatrix}
a&b\\c&d
\end{bmatrix}
=ad-bc
$$

이다.

~~~python
A = np.array([
    [2.0, 1.0],
    [1.0, 3.0],
])

determinant = np.linalg.det(A)
print(determinant)
~~~

행렬식이 0이면 역행렬이 존재하지 않는다.

## 8.2. 역행렬

역행렬은 다음 관계를 만족한다.

$$
\boldsymbol A^{-1}\boldsymbol A
=
\boldsymbol I
$$

~~~python
A_inverse = np.linalg.inv(A)

print(A_inverse)
print(A_inverse @ A)
~~~

부동소수점 계산 결과는 정확한 정수 대신 0에 매우 가깝거나 1에 매우 가까운 값으로
나타날 수 있다. 두 배열이 가까운지 확인할 때는 <code>np.allclose()</code>를 사용한다.

~~~python
print(
    np.allclose(
        A_inverse @ A,
        np.eye(2),
    )
)
~~~

# 9. 연립방정식 풀기

다음 연립방정식을 생각하자.

$$
\begin{aligned}
2x+y&=5,\\
x+3y&=6.
\end{aligned}
$$

행렬 형태는

$$
\boldsymbol A\cdot \boldsymbol x=\boldsymbol b
$$

이며

$$
\boldsymbol A=
\begin{bmatrix}2&1\\1&3\end{bmatrix},
\quad
\boldsymbol x=
\begin{bmatrix}x\\y\end{bmatrix},
\quad
\boldsymbol b=
\begin{bmatrix}5\\6\end{bmatrix}
$$

이다.

~~~python
A = np.array([
    [2.0, 1.0],
    [1.0, 3.0],
])
b = np.array([5.0, 6.0])

x = np.linalg.solve(A, b)

print(x)
print(A @ x)
~~~

해는 $x=1.8$, $y=1.4$이고 <code>A @ x</code>는 원래 우변 $b$와 같다.

연립방정식을 풀 때는 역행렬을 직접 계산하여 <code>np.linalg.inv(A) @ b</code>로
구하기보다 <code>np.linalg.solve(A, b)</code>를 사용하는 것이 좋다.

# 10. 재료공학 예제

## 10.1. 격자 좌표를 실제 위치로 변환하기

직교하는 격자축의 길이가 $a=2$, $b=3$, $c=4$라고 하자. 격자 좌표
$\boldsymbol p=(0.5,0.5,0.25)$를 실제 위치로 바꾸는 행렬은

$$
\boldsymbol L=
\begin{bmatrix}
2&0&0\\
0&3&0\\
0&0&4
\end{bmatrix}
$$

이다.

~~~python
lattice_matrix = np.diag([2.0, 3.0, 4.0])
fractional_position = np.array([
    0.5,
    0.5,
    0.25,
])

cartesian_position = (
    lattice_matrix @ fractional_position
)

print(cartesian_position)
~~~

결과는 $(1,1.5,1)$이다.

## 10.2. 두 격자점 사이의 거리

~~~python
fractional_p = np.array([0.0, 0.0, 0.0])
fractional_q = np.array([0.5, 0.5, 0.25])

cartesian_p = lattice_matrix @ fractional_p
cartesian_q = lattice_matrix @ fractional_q

distance = np.linalg.norm(
    cartesian_q - cartesian_p
)

print(distance)
~~~

두 점 사이의 거리는 $\sqrt{1^2+1.5^2+1^2}\approx2.062$이다.

# 11. 자주 하는 실수

- <code>A * B</code>를 행렬곱이라고 생각한다.
- 행렬곱 전에 두 행렬의 shape을 확인하지 않는다.
- 수학의 첨자와 Python 인덱스의 시작 번호를 혼동한다.
- $AB=BA$라고 생각한다.
- 정사각행렬이 아닌 행렬의 행렬식이나 역행렬을 구하려 한다.
- 행렬식이 0인 행렬의 역행렬을 구하려 한다.
- 연립방정식 계산에서 역행렬을 불필요하게 직접 구한다.

# 12. 정리

- 행렬은 2차원 NumPy 배열로 나타낼 수 있다.
- <code>*</code>는 원소별 곱이고 <code>@</code>는 행렬곱이다.
- 행렬–벡터곱은 각 행과 벡터의 내적으로 계산한다.
- $(l,m)$ 행렬과 $(m,n)$ 행렬의 곱은 $(l,n)$ 행렬이다.
- <code>np.eye()</code>는 단위행렬을 만든다.
- <code>A.T</code>는 전치행렬이다.
- <code>np.linalg.det()</code>와 <code>np.linalg.inv()</code>로 행렬식과 역행렬을 계산한다.
- 연립방정식은 <code>np.linalg.solve()</code>로 푼다.

# 13. 연습 문제

## 문제 1

다음 행렬의 shape을 쓰시오.

$$
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
$$

<!--
풀이와 해답:
2행 3열이므로 shape은 (2,3)이다.
-->

## 문제 2

NumPy에서 원소별 곱과 행렬곱에 사용하는 연산자를 각각 쓰시오.

<!--
풀이와 해답:
원소별 곱은 *이고 행렬곱은 @이다.
-->

## 문제 3

다음 행렬–벡터곱을 계산하라.

$$
\begin{bmatrix}
1&0\\
0&2
\end{bmatrix}
\begin{bmatrix}
3\\4
\end{bmatrix}
$$

<!--
풀이와 해답:
결과는 (3,8)^T이다.
-->

## 문제 4

shape이 $(2,3)$인 행렬과 $(3,4)$인 행렬을 곱할 수 있는가? 결과 shape도 쓰시오.

<!--
풀이와 해답:
안쪽 크기 3이 같으므로 곱할 수 있고 결과 shape은 (2,4)이다.
-->

## 문제 5

단위행렬 $\boldsymbol I$와 벡터 $\boldsymbol x$의 곱은 무엇인가?

<!--
풀이와 해답:
I x=x이므로 원래 벡터 x이다.
-->

## 문제 6

2×2 행렬
$\begin{bmatrix}2&1\\1&3\end{bmatrix}$의 행렬식을 구하라.

<!--
풀이와 해답:
2 곱하기 3에서 1 곱하기 1을 빼면 5이다.
-->

## 문제 7

행렬 $A$와 벡터 $b$로 이루어진 연립방정식 $Ax=b$를 푸는 NumPy 함수를 쓰시오.

<!--
풀이와 해답:
np.linalg.solve(A, b)를 사용한다.
-->
