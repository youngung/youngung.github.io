---
layout: distill
title: NumPy 배열 활용
description: 인덱싱, 슬라이싱, 축, 브로드캐스팅과 파일 입출력
target: 1학년 2학기
permalink:
featured: true
prerequisite: NumPy 배열 기초
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
- [2. 1차원 배열 인덱싱과 슬라이싱](#2-1차원-배열-인덱싱과-슬라이싱)
- [3. 2차원 배열 인덱싱](#3-2차원-배열-인덱싱)
- [4. 조건을 이용한 선택](#4-조건을-이용한-선택)
- [5. 슬라이싱의 view와 copy](#5-슬라이싱의-view와-copy)
- [6. reshape과 전치](#6-reshape과-전치)
- [7. axis를 이용한 계산](#7-axis를-이용한-계산)
- [8. 브로드캐스팅](#8-브로드캐스팅)
- [9. 텍스트와 CSV 파일 읽기](#9-텍스트와-csv-파일-읽기)
- [10. 배열 저장하기](#10-배열-저장하기)
- [11. 재료공학 예제](#11-재료공학-예제)
- [12. 자주 만나는 오류](#12-자주-만나는-오류)
- [13. 정리](#13-정리)
- [14. 연습 문제](#14-연습-문제)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 인덱싱과 슬라이싱으로 원하는 배열 원소를 선택할 수 있다.
- 슬라이싱으로 만든 view와 독립적인 copy의 차이를 설명할 수 있다.
- <code>reshape()</code>와 전치행렬을 사용할 수 있다.
- <code>axis</code>를 지정하여 행별·열별 계산을 수행할 수 있다.
- 간단한 브로드캐스팅을 활용할 수 있다.
- 공백 구분 파일과 CSV 파일을 읽고 저장할 수 있다.

# 2. 1차원 배열 인덱싱과 슬라이싱

~~~python
import numpy as np


array = np.array([3, 3, 4, 3, 3, 4, 5, 6])
~~~

Python의 인덱스는 0부터 시작한다.

~~~python
print(array[0])
print(array[2])
print(array[-1])
~~~

- <code>array[0]</code>: 첫 번째 원소 3
- <code>array[2]</code>: 세 번째 원소 4
- <code>array[-1]</code>: 마지막 원소 6

슬라이싱은 <code>array[start:stop:step]</code> 형식을 사용한다. <code>stop</code>
위치의 원소는 포함하지 않는다.

~~~python
print(array[2:6])
print(array[2:6:2])
print(array[::-1])
~~~

결과는 각각 다음과 같다.

~~~text
[4 3 3 4]
[4 3]
[6 5 4 3 3 4 3 3]
~~~

# 3. 2차원 배열 인덱싱

~~~python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
~~~

2차원 배열에서는 쉼표 앞이 행 인덱스, 뒤가 열 인덱스이다.

~~~python
print(matrix[0, 0])
print(matrix[1, :])
print(matrix[:, 1])
print(matrix[0:2, 1:3])
~~~

각 결과는 다음과 같다.

- <code>matrix[0, 0]</code>: 첫 행 첫 열의 값 1
- <code>matrix[1, :]</code>: 두 번째 행 <code>[4 5 6]</code>
- <code>matrix[:, 1]</code>: 두 번째 열 <code>[2 5 8]</code>
- <code>matrix[0:2, 1:3]</code>: 첫 두 행과 마지막 두 열

~~~text
[[2 3]
 [5 6]]
~~~

# 4. 조건을 이용한 선택

배열에 비교 연산을 적용하면 각 원소에 대한 Boolean 배열을 얻는다.

~~~python
temperatures = np.array([300, 450, 700, 550])

is_high = temperatures >= 500
print(is_high)
print(temperatures[is_high])
~~~

500 K 이상인 값만 선택한 결과는 <code>[700 550]</code>이다. 조건식을 배열에 직접
넣을 수도 있다.

~~~python
print(temperatures[temperatures >= 500])
~~~

# 5. 슬라이싱의 view와 copy

NumPy의 기본 슬라이싱은 원본 데이터의 일부를 공유하는 view를 반환하는 경우가 많다.

~~~python
original = np.array([10, 20, 30, 40])
part = original[1:3]

part[0] = 999

print(part)
print(original)
~~~

<code>part</code>를 바꾸면 <code>original</code>도 바뀐다. 원본과 독립된 배열이
필요하면 <code>copy()</code>를 사용한다.

~~~python
original = np.array([10, 20, 30, 40])
part = original[1:3].copy()

part[0] = 999

print(part)
print(original)
~~~

# 6. reshape과 전치

~~~python
values = np.arange(12)
matrix = values.reshape(3, 4)

print(matrix)
print(matrix.shape)
~~~

행과 열을 바꾸려면 전치(transpose)를 사용한다.

~~~python
transposed = matrix.T

print(transposed)
print(transposed.shape)
~~~

<code>matrix</code>의 shape은 <code>(3, 4)</code>이고 <code>matrix.T</code>의
shape은 <code>(4, 3)</code>이다.

# 7. axis를 이용한 계산

다음 배열은 두 시편에 대해 세 번씩 측정한 값이라고 하자.

~~~python
measurements = np.array([
    [10.0, 12.0, 11.0],
    [20.0, 18.0, 22.0],
])
~~~

shape은 <code>(2, 3)</code>이다.

- <code>axis=0</code>을 제거하면 각 열에 대한 결과 3개가 남는다.
- <code>axis=1</code>을 제거하면 각 행에 대한 결과 2개가 남는다.

~~~python
column_mean = measurements.mean(axis=0)
row_mean = measurements.mean(axis=1)

print(column_mean)
print(row_mean)
print(column_mean.shape)
print(row_mean.shape)
~~~

- 열별 평균: <code>[15. 15. 16.5]</code>
- 행별 평균: <code>[11. 20.]</code>

<code>axis</code> 번호를 외우기보다 입력 shape에서 어느 축이 사라지고 어떤 shape이
남는지 확인하면 이해하기 쉽다.

# 8. 브로드캐스팅

브로드캐스팅(broadcasting)은 shape이 다른 배열 사이의 연산을 가능한 형태로 확장하여
계산하는 규칙이다.

## 8.1. 배열과 스칼라

~~~python
celsius = np.array([0.0, 25.0, 100.0])
kelvin = celsius + 273.15

print(kelvin)
~~~

스칼라 273.15가 모든 원소에 더해진다.

## 8.2. 각 열에 서로 다른 값 더하기

~~~python
data = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
])

offset = np.array([10.0, 20.0, 30.0])
corrected = data + offset

print(corrected)
~~~

shape <code>(3,)</code>인 <code>offset</code>이 각 행에 반복 적용된다.

~~~text
[[11. 22. 33.]
 [14. 25. 36.]]
~~~

두 배열의 마지막 축부터 크기를 비교하여, 크기가 같거나 한쪽이 1이면 브로드캐스팅할 수 있다.
처음에는 연산 전후의 <code>shape</code>을 출력하면서 확인하는 것이 좋다.

# 9. 텍스트와 CSV 파일 읽기

링크에서 파일을 내려받아 Notebook과 같은 폴더에 저장한 뒤 실습한다.

- [공백 구분 파일](/assets/dat_files/lectures/1_2_data_mse/matrix_01.txt)
- [CSV 파일](/assets/dat_files/lectures/1_2_data_mse/matrix_01.csv)

공백으로 구분된 파일은 다음과 같이 읽는다.

~~~python
matrix_txt = np.loadtxt("matrix_01.txt")

print(matrix_txt)
print(matrix_txt.shape)
print(matrix_txt.dtype)
~~~

쉼표로 구분된 CSV 파일은 <code>delimiter=","</code>를 지정한다.

~~~python
matrix_csv = np.loadtxt(
    "matrix_01.csv",
    delimiter=",",
)

print(matrix_csv)
~~~

웹 링크의 경로와 Python이 사용하는 로컬 파일 경로는 다를 수 있다.
<code>FileNotFoundError</code>가 발생하면 현재 작업 폴더와 내려받은 파일의 위치를 확인한다.

# 10. 배열 저장하기

~~~python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

np.savetxt(
    "saved_matrix.txt",
    matrix,
    fmt="%.2f",
)

np.savetxt(
    "saved_matrix.csv",
    matrix,
    delimiter=",",
    fmt="%d",
)
~~~

- <code>fmt="%.2f"</code>: 실수를 소수점 아래 둘째 자리까지 저장
- <code>fmt="%d"</code>: 정수 형식으로 저장
- <code>delimiter=","</code>: 원소 사이를 쉼표로 구분

저장한 뒤 다시 읽어 원래 shape과 값이 유지되는지 확인하는 것이 좋다.

# 11. 재료공학 예제

세 시편의 힘을 세 번씩 측정한 데이터가 다음과 같다고 하자.

~~~python
force_n = np.array([
    [1000.0, 1020.0, 980.0],
    [1500.0, 1530.0, 1470.0],
    [2000.0, 1980.0, 2020.0],
])

area_mm2 = np.array([
    [10.0],
    [12.0],
    [20.0],
])
~~~

<code>force_n</code>의 shape은 <code>(3, 3)</code>이고 <code>area_mm2</code>의
shape은 <code>(3, 1)</code>이다. 면적값 하나가 같은 시편의 세 측정값에
브로드캐스팅된다.

~~~python
stress_mpa = force_n / area_mm2
mean_stress_mpa = stress_mpa.mean(axis=1)

print(stress_mpa)
print(mean_stress_mpa)
~~~

$1\ \mathrm{N/mm^2}=1\ \mathrm{MPa}$이므로 응력 단위는 MPa이다. 각 행의 평균을
구했으므로 시편별 평균응력 세 개가 나온다.

# 12. 자주 만나는 오류

## 12.1. IndexError

배열 범위를 벗어난 위치를 선택하면 발생한다. shape과 인덱스가 0부터 시작한다는 점을 확인한다.

## 12.2. ValueError: cannot reshape

원소 개수와 새 shape의 원소 개수가 다를 때 발생한다.

~~~python
values = np.arange(12)
print(values.size)
~~~

12개 원소는 <code>(3, 4)</code>로 바꿀 수 있지만 <code>(5, 3)</code>으로는 바꿀 수 없다.

## 12.3. 브로드캐스팅 오류

두 shape이 브로드캐스팅 규칙에 맞지 않으면 오류가 발생한다. 연산 전에 두 배열의
<code>shape</code>을 출력하여 마지막 축부터 비교한다.

# 13. 정리

- 인덱스는 0부터 시작하며 슬라이싱의 stop 위치는 포함하지 않는다.
- 2차원 배열에서 쉼표 앞은 행, 뒤는 열 인덱스이다.
- 기본 슬라이싱은 원본 데이터를 공유하는 view가 될 수 있다.
- 독립적인 배열이 필요하면 <code>copy()</code>를 사용한다.
- <code>axis=0</code>은 첫 번째 축을, <code>axis=1</code>은 두 번째 축을 제거한다.
- 브로드캐스팅은 shape이 다른 배열 사이의 연산을 가능하게 한다.
- CSV 파일을 읽을 때는 <code>delimiter=","</code>를 지정한다.

# 14. 연습 문제

## 문제 1

다음 코드의 출력값을 쓰시오.

~~~python
a = np.array([10, 20, 30, 40])
print(a[1])
~~~

<!--
풀이와 해답:
20이 출력된다.
-->

## 문제 2

배열 <code>a</code>의 첫 번째부터 세 번째 원소까지 선택하는 표현을 쓰시오.
단, 세 번째 원소까지 포함한다.

<!--
풀이와 해답:
a[0:3] 또는 a[:3]이다.
-->

## 문제 3

2차원 배열 <code>A</code>의 두 번째 열 전체를 선택하는 표현을 쓰시오.

<!--
풀이와 해답:
A[:, 1]
-->

## 문제 4

다음 배열에서 5보다 큰 원소만 선택하는 표현을 쓰시오.

~~~python
a = np.array([2, 5, 7, 9])
~~~

<!--
풀이와 해답:
a[a > 5]
-->

## 문제 5

shape이 <code>(2, 3)</code>인 배열의 행별 평균을 구할 때 사용할 axis를 쓰시오.

<!--
풀이와 해답:
axis=1을 사용한다.
-->

## 문제 6

CSV 파일 <code>data.csv</code>를 <code>np.loadtxt()</code>로 읽는 표현을 쓰시오.

<!--
풀이와 해답:
np.loadtxt("data.csv", delimiter=",")
-->

## 문제 7

슬라이싱한 배열을 원본과 독립적으로 만들 때 사용하는 메서드는 무엇인가?

<!--
풀이와 해답:
copy()이다.
-->
