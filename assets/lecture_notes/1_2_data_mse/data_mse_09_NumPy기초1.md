---
layout: distill
title: NumPy 배열 기초
description: 배열 생성, 자료형, 형태와 원소별 연산
target: 1학년 2학기
permalink:
featured: true
prerequisite: Python 기초 자료구조
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
- [2. NumPy가 필요한 이유](#2-numpy가-필요한-이유)
- [3. NumPy 불러오기](#3-numpy-불러오기)
- [4. 배열 만들기](#4-배열-만들기)
  - [4.1. 리스트로부터 만들기](#41-리스트로부터-만들기)
  - [4.2. 일정한 값으로 채우기](#42-일정한-값으로-채우기)
  - [4.3. 연속된 값 만들기](#43-연속된-값-만들기)
- [5. 배열의 주요 속성](#5-배열의-주요-속성)
- [6. 자료형](#6-자료형)
- [7. 원소별 연산 (element-wise operation)](#7-원소별-연산-element-wise-operation)
- [8. 집계 연산 (reduction)](#8-집계-연산-reduction)
- [9. 배열 형태 바꾸기 (reshape)](#9-배열-형태-바꾸기-reshape)
- [10. 리스트와 배열의 차이](#10-리스트와-배열의-차이)
- [11. 간단한 속도 비교](#11-간단한-속도-비교)
- [12. 재료공학 예제](#12-재료공학-예제)
- [13. 정리](#13-정리)
- [14. 연습 문제](#14-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- Python 리스트와 NumPy 배열의 차이를 설명할 수 있다.
- 1차원 및 2차원 배열을 만들 수 있다.
- <code>shape</code>, <code>ndim</code>, <code>size</code>, <code>dtype</code>을 확인할 수 있다.
- 배열의 원소별 사칙연산을 수행할 수 있다.
- 배열의 합계, 평균, 최솟값과 최댓값을 계산할 수 있다.

# 2. NumPy가 필요한 이유

NumPy(Numerical Python)는 수치 계산에 사용하는 Python 라이브러리이다. NumPy 배열은
같은 종류의 수치 데이터를 효율적으로 저장하고, 여러 원소에 대한 계산을 간단하게 표현한다.

Python 리스트의 각 원소에 2를 곱하려면 반복문과 <code>append()</code>를 사용할 수 있다.

~~~python
values = [1, 2, 3]
doubled = []

for value in values:
    doubled.append(2 * value)

print(doubled)
~~~

NumPy 배열에서는 배열 전체에 2를 곱할 수 있다.

~~~python
import numpy as np

values = np.array([1, 2, 3])
doubled = 2 * values

print(doubled)
~~~

이처럼 배열 전체에 적용되는 연산을 벡터화된 연산(vectorized operation)이라고 한다.

# 3. NumPy 불러오기

NumPy는 일반적으로 <code>np</code>라는 짧은 이름으로 불러온다.

~~~python
import numpy as np
~~~

설치되지 않았다면 터미널에서 다음 명령을 사용할 수 있다.

~~~sh
python -m pip install numpy
~~~

현재 사용 중인 NumPy 버전은 다음과 같이 확인한다.

~~~python
print(np.__version__)
~~~

# 4. 배열 만들기

## 4.1. 리스트로부터 만들기

<code>np.array()</code>는 입력 데이터로 <code>numpy.ndarray</code> 객체를 만든다.

~~~python
vector = np.array([1, 2, 3])
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print(vector)
print(matrix)
~~~

## 4.2. 일정한 값으로 채우기

배열의 형태(shape)는 튜플로 전달한다.

~~~python
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
sevens = np.full((2, 3), 7)

print(zeros)
print(ones)
print(sevens)
~~~

<code>np.zeros((2, 3))</code>의 괄호가 두 겹인 이유는 <code>(2, 3)</code>이라는
shape 튜플을 하나의 인자로 전달하기 때문이다.

## 4.3. 연속된 값 만들기

<code>np.arange()</code>는 시작값 이상, 끝값 미만의 값을 일정한 간격으로 만든다.

~~~python
even_numbers = np.arange(0, 10, 2)
print(even_numbers)
~~~

결과는 <code>[0 2 4 6 8]</code>이다.

<code>np.linspace()</code>는 시작값과 끝값을 포함하여 지정한 개수의 값을 만든다.

~~~python
temperatures = np.linspace(300.0, 500.0, 5)
print(temperatures)
~~~

결과는 <code>[300. 350. 400. 450. 500.]</code>이다.

| 함수 | 지정하는 값 | 끝값 포함 |
|---|---|---|
| <code>np.arange(start, stop, step)</code> | 간격 | 포함하지 않음 |
| <code>np.linspace(start, stop, num)</code> | 원소 개수 | 기본적으로 포함 |

# 5. 배열의 주요 속성

~~~python
array = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print(array.shape)
print(array.ndim)
print(array.size)
print(array.dtype)
~~~

- <code>shape</code>: 각 축의 원소 개수. 위 배열에서는 <code>(2, 3)</code>
- <code>ndim</code>: 배열 축의 개수. 위 배열에서는 2
- <code>size</code>: 전체 원소 개수. 위 배열에서는 6
- <code>dtype</code>: 배열 원소의 자료형

NumPy의 배열 차원(<code>ndim</code>)과 물리학에서 사용하는 텐서의 rank는 같은
개념이 아니므로 구분한다.

# 6. 자료형

NumPy 배열은 일반적으로 한 가지 자료형의 원소를 저장한다.

~~~python
integer_array = np.array([1, 2, 3])
float_array = np.array([1.0, 2.0, 3.0])

print(integer_array.dtype)
print(float_array.dtype)
~~~

정수와 실수를 함께 넣으면 실수를 보존할 수 있는 자료형으로 변환된다.

~~~python
mixed = np.array([1, 2.5, 3])
print(mixed)
print(mixed.dtype)
~~~

<code>dtype</code>을 직접 지정할 수도 있다.

~~~python
measurements = np.array(
    [1, 2, 3],
    dtype=float,
)

print(measurements)
~~~

자료형마다 표현할 수 있는 범위와 정밀도가 다르다. 처음에는 측정값처럼 소수점이 필요한
데이터에는 실수형을 사용한다는 점을 기억하면 된다.

# 7. 원소별 연산 (element-wise operation)

크기가 같은 두 배열에 사칙연산을 적용하면 같은 위치의 원소끼리 계산한다.

~~~python
a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a**2)
~~~

여기서 <code>a * b</code>는 행렬곱이 아니라 원소별 곱이다. 행렬과 벡터의 곱은 뒤의
벡터·행렬 연산 강의에서 다룬다.

스칼라와 배열을 계산하면 모든 원소에 같은 연산을 적용한다.

~~~python
stress_mpa = np.array([100.0, 150.0, 200.0])

print(stress_mpa / 1000.0)
print(stress_mpa + 10.0)
~~~

# 8. 집계 연산 (reduction)

여러 원소를 하나의 값으로 요약하는 계산을 집계 연산(reduction)이라고 한다.

~~~python
values = np.array([3.0, 5.0, 7.0, 9.0])

print(values.sum())
print(values.mean())
print(values.min())
print(values.max())
print(values.std())
~~~

위 결과는 각각 합계, 평균, 최솟값, 최댓값과 모집단 표준편차이다.

함수 형태로도 같은 계산을 할 수 있다.

~~~python
print(np.sum(values))
print(np.mean(values))
~~~

# 9. 배열 형태 바꾸기 (reshape)

<code>reshape()</code>는 원소 개수를 유지하면서 배열의 형태를 바꾼다.

~~~python
values = np.arange(12)
matrix = values.reshape(3, 4)

print(values.shape)
print(matrix.shape)
print(matrix)
~~~

12개의 원소는 $3\times4$ 또는 $2\times6$으로 바꿀 수 있지만 $5\times3$으로는
바꿀 수 없다.

배열을 다시 1차원으로 펼칠 때는 <code>ravel()</code>을 사용할 수 있다.

~~~python
flat = matrix.ravel()

print(flat)
print(flat.shape)
~~~

# 10. 리스트와 배열의 차이

<code>+</code> 연산의 의미가 서로 다르다.

~~~python
list_a = [1, 2, 3]
list_b = [4, 5, 6]

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

print(list_a + list_b)
print(array_a + array_b)
~~~

- 리스트의 <code>+</code>: 두 리스트를 이어 붙인다.
- 배열의 <code>+</code>: 같은 위치의 원소끼리 더한다.

배열은 수치 계산에 편리하지만 이름, 결정구조, 설명처럼 서로 다른 종류의 데이터를 함께
저장할 때는 리스트나 딕셔너리가 더 적합할 수 있다.

# 11. 간단한 속도 비교

속도를 비교하려면 두 코드가 같은 데이터를 대상으로 같은 계산을 수행해야 한다.

~~~python
python_values = list(range(1_000_000))
numpy_values = np.array(python_values)
~~~

Jupyter Notebook에서 다음 두 셀을 각각 실행할 수 있다.

~~~python
%%timeit
sum(python_values)
~~~

~~~python
%%timeit
numpy_values.sum()
~~~

결과는 컴퓨터와 NumPy 버전에 따라 달라진다. 특정 실행시간을 외우는 것이 아니라, 큰
수치 배열에서 NumPy 연산이 일반적인 Python 반복보다 효율적일 수 있음을 확인하는 실습이다.

# 12. 재료공학 예제

세 인장 시편의 힘과 초기 단면적이 다음과 같이 측정되었다고 하자.

~~~python
force_n = np.array([1000.0, 1500.0, 2200.0])
area_mm2 = np.array([10.0, 12.0, 20.0])

stress_mpa = force_n / area_mm2

print(stress_mpa)
print(f"평균 응력: {stress_mpa.mean():.2f} MPa")
~~~

$1\ \mathrm{N/mm^2}=1\ \mathrm{MPa}$이므로 결과의 단위는 MPa이다. 배열을 사용하면
여러 시편의 응력을 한 번에 계산할 수 있다.

# 13. 정리

- NumPy 배열은 같은 종류의 수치 데이터를 효율적으로 다룬다.
- <code>np.array()</code>, <code>np.zeros()</code>, <code>np.arange()</code>,
  <code>np.linspace()</code>로 배열을 만들 수 있다.
- <code>shape</code>, <code>ndim</code>, <code>size</code>, <code>dtype</code>은
  배열의 구조를 설명한다.
- 배열의 사칙연산은 기본적으로 원소별로 수행된다.
- <code>sum()</code>, <code>mean()</code>, <code>min()</code>, <code>max()</code>로
  데이터를 요약할 수 있다.
- <code>reshape()</code>는 원소 수를 유지하면서 배열의 형태를 바꾼다.

# 14. 연습 문제

## 문제 1

NumPy를 <code>np</code>라는 이름으로 불러오는 문장을 쓰시오.

<!--
풀이와 해답:
import numpy as np
-->

## 문제 2

다음 배열의 <code>shape</code>, <code>ndim</code>, <code>size</code>를 구하라.

~~~python
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
~~~

<!--
풀이와 해답:
shape은 (2, 3), ndim은 2, size는 6이다.
-->

## 문제 3

2행 3열의 모든 원소가 0인 배열을 만드는 표현을 쓰시오.

<!--
풀이와 해답:
np.zeros((2, 3))
-->

## 문제 4

<code>np.arange(0, 7, 2)</code>의 결과를 쓰시오.

<!--
풀이와 해답:
[0 2 4 6]이다.
-->

## 문제 5

다음 코드의 결과를 쓰시오.

~~~python
a = np.array([1, 2, 3])
print(2 * a)
~~~

<!--
풀이와 해답:
[2 4 6]이 출력된다.
-->

## 문제 6

배열 <code>a</code>의 평균을 구하는 표현을 하나 쓰시오.

<!--
풀이와 해답:
a.mean() 또는 np.mean(a)를 사용할 수 있다.
-->
