---
layout: distill
title: NumPy 배열 활용
description: 인덱싱, 슬라이싱, 축, 브로드캐스팅과 파일 입출력
target: 1학년 2학기
permalink:
featured: true
prerequisite: NumPy 배열 기초
toc: false
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

**목차**

* TOC
{:toc}

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 인덱싱(indexing)과 슬라이싱(slicing)으로 원하는 배열 원소를 선택할 수 있다.
- 원본 데이터를 공유하는 뷰(view)와 별도 데이터를 갖는 복사본(copy)의 차이를 설명할 수 있다.
- <code>reshape()</code>로 배열의 형태를 바꾸고, <code>.T</code>로 2차원 배열의 행과 열을 바꿀 수 있다.
- <code>axis</code>를 지정하여 행별·열별 계산을 수행할 수 있다.
- 여러 축의 shape을 비교하여 브로드캐스팅 가능 여부를 판단하고, <code>None</code>으로 필요한 축을 추가할 수 있다.
- 공백 구분 파일과 CSV (Comma Separated Values) 파일을 읽고 저장할 수 있다.

# 2. 1차원 배열 인덱싱과 슬라이싱

~~~python
import numpy as np
array = np.array([3, 3, 4, 3, 3, 4, 5, 6])
~~~

NumPy 배열의 인덱스는 Python 리스트와 마찬가지로 0부터 시작한다.

~~~python
print(array[0])
print(array[2])
print(array[-1])
~~~

- <code>array[0]</code>: 첫 번째 원소 3
- <code>array[2]</code>: 세 번째 원소 4
- <code>array[-1]</code>: 마지막 원소 6

- <code>start</code>: 시작 인덱스 (포함)
- <code>stop</code>: 종료 인덱스 (포함하지 않음)
- <code>step</code>: 증가분

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

2차원 배열에서는 쉼표 앞이 행 인덱스, 뒤가 열 인덱스이다 (행, 열 순서).

~~~python
print(matrix[0, 0])
print(matrix[1, :])
print(matrix[:, 1])
print(matrix[0:2, 1:3])
~~~

각 결과는 다음과 같다.

- <code>matrix[0, 0]</code>: 첫 행 첫 열의 값 1
- <code>matrix[1, :]</code>: 두 번째 행의 모든 원소 <code>[4 5 6]</code>
- <code>matrix[:, 1]</code>: 두 번째 열의 모든 원소 <code>[2 5 8]</code>
- <code>matrix[0:2, 1:3]</code>: 첫 두 행과 마지막 두 열
~~~text
[[2 3]
 [5 6]]
~~~

## 3.1. 여러 축을 선택할 때의 shape

9장의 시편·시점·센서 배열을 원소마다 다른 값으로 채워 보자.

~~~python
measurements = np.arange(24.0).reshape(2, 3, 4)
print(measurements[1, 2, 3])        # 23.0: 두 번째 시편, 세 번째 시점, 네 번째 센서
print(measurements[0, :, :].shape)  # (3, 4)
print(measurements[:, 1, :].shape)  # (2, 4)
print(measurements[:, :, 2].shape)  # (2, 3)
print(measurements[:, :, 2:3].shape)  # (2, 3, 1)
~~~

정수 인덱스로 한 위치를 선택하면 그 축은 결과에서 사라진다.
반면 <code>:</code>나 <code>2:3</code> 같은 슬라이스는 해당 축을 유지한다.
따라서 <code>2</code>와 <code>2:3</code>은 같은 센서를 선택해도 결과 shape이 다르다.

# 4. 조건을 이용한 선택

배열에 비교 연산을 적용하면 각 원소의 조건 충족 여부를 <code>True</code> 또는 <code>False</code>로 나타낸 불리언(Boolean) 배열을 얻는다.

~~~python
temperatures = np.array([300, 450, 700, 550])

is_high = temperatures >= 500 # 제일 왼쪽 '='가 오른쪽 조건식 결과를 assignment
print(is_high)
print(temperatures[is_high])
~~~

500 K 이상인 값만 선택한 결과는 <code>[700 550]</code>이다. 조건식을 배열에 직접
넣을 수도 있다.

~~~python
print(temperatures[temperatures >= 500])
~~~

# 5. 슬라이싱의 view와 copy

NumPy 배열을 기본 슬라이싱하면 원본 데이터의 일부를 공유하는 **[뷰(view)](https://numpy.org/doc/stable/user/basics.copies.html)**를 얻는다.
따라서 새 변수에 저장했다고 해서 데이터까지 별도로 복사된 것은 아니다.

~~~python
original = np.array([10, 20, 30, 40])
part = original[1:3]

part[0] = 999

print(part)
print(original)
~~~

<code>part</code>의 원소를 바꾸면 <code>original</code>의 해당 원소도 바뀐다.
원본에 영향을 주지 않고 수정하려면 <code>copy()</code>로 **복사본(copy)**을 만든다.

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

## 6.1. 1차원 배열에 새 축 추가하기

1차원 배열에는 행과 열의 구분이 없으며, <code>.T</code>를 사용해도 shape이 바뀌지 않는다.
인덱싱에서 <code>None</code>(또는 <code>np.newaxis</code>)을 넣으면 그 위치에 길이 1인 축이 생긴다.

~~~python
vector = np.array([1.0, 2.0, 3.0])
column = vector[:, None]
row = vector[None, :]
print(vector.shape, vector.T.shape)  # (3,) (3,)
print(column.shape, row.shape)      # (3, 1) (1, 3)
~~~

<code>:</code>는 기존 원소를 모두 선택한다. 그 뒤에 새 축을 넣으면 3행 1열,
앞에 넣으면 1행 3열이 된다. 원소로 <code>None</code> 값을 넣는 것이 아니며,
원래 <code>vector</code>의 값과 shape도 바뀌지 않는다.
8절에서는 이 길이 1인 축을 이용하여 다른 shape의 배열과 연산한다.
2차원 배열의 <code>.T</code>는 행과 열을 바꾸지만, 다차원 배열의 <code>.T</code>는
모든 축의 순서를 뒤집으므로 같은 의미로 일반화하지 않도록 주의하자.

# 7. axis를 이용한 계산

다음 배열은 두 시편에 대해 세 번씩 측정한 값이라고 하자.

~~~python
measurements = np.array([
    [10.0, 12.0, 11.0],
    [20.0, 18.0, 22.0],
])
~~~

shape은 <code>(2, 3)</code>이다.

- <code>mean(axis=0)</code>: 같은 열의 값을 평균 낸다. 시편 축이 사라지고, 측정 시점별 평균 3개가 남는다.
- <code>mean(axis=1)</code>: 같은 행의 값을 평균 낸다. 시점 축이 사라지고, 시편별 평균 2개가 남는다.

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

같은 원리는 여러 축에도 적용된다.
<code>measurements.shape == (2, 3, 4)</code>인 시편·시점·센서 데이터에서
<code>measurements.mean(axis=1)</code>은 시점 축을 따라 평균을 구하여
shape <code>(2, 4)</code>인 시편별·센서별 평균을 남긴다.

# 8. 브로드캐스팅

[브로드캐스팅(broadcasting)](https://numpy.org/doc/stable/user/basics.broadcasting.html)은 shape이 다른 배열끼리 연산할 때, 길이가 1인 축의 값을
상대 배열의 여러 위치에 반복해서 적용하는 규칙이다. 두 배열의 **마지막 축**부터 길이를 비교하여, 길이가 같거나 한쪽이 1이면
브로드캐스팅할 수 있다.

## 8.1. 배열과 스칼라

~~~python
celsius = np.array([0.0, 25.0, 100.0])
kelvin = celsius + 273.15
# 스칼라는 shape이 ()이며, 브로드캐스팅되어 모든 원소에 더해진다.
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
# data의 shape (2, 3)인 배열에, shape (3,)인 offset이 각 행에 반복 적용되어 브로드캐스팅된다.
# data의 마지막 축의 크기(3)와 offset의 크기(3)가 맞아서 브로드캐스팅이 가능하다.
corrected = data + offset

print(corrected)
~~~

shape <code>(3,)</code>인 <code>offset</code>이 각 행에 반복 적용된다.

~~~text
[[11. 22. 33.]
 [14. 25. 36.]]
~~~

연산 전후의 <code>shape</code>을 출력하고, 각 축의 길이가 어떻게 맞춰지는지 확인하자.
다음 절에서는 이 규칙을 여러 축으로 확장한다.

## 8.3. 축이 여러 개인 배열의 일반 규칙

브로드캐스팅은 1차원이나 2차원에만 적용되는 규칙이 아니다. 축이 몇 개이든
**shape을 오른쪽 끝부터 맞추어 모든 축을 비교**하면 된다.

1. 축의 개수가 다르면, 축이 적은 shape의 **왼쪽에 1을 붙인 것처럼** 비교한다.
2. 대응하는 축의 길이가 같거나, 어느 한쪽의 길이가 1이면 그 축은 연산할 수 있다.
3. 길이가 1인 축에서는 같은 값을 상대 축의 여러 위치에 적용한다. 두 축의 길이가 같으면 같은 위치의 원소끼리 계산한다.
4. **모든 축**이 이 조건을 만족해야 한다. 하나라도 맞지 않으면 <code>ValueError</code>가 발생한다.

왼쪽에 1을 붙이는 것은 연산 규칙을 이해하기 위한 표현이며, 원래 배열의 shape을 바꾸지는 않는다.
브로드캐스팅 자체는 입력을 반복 복사한 큰 배열을 만들 필요 없이 계산하지만,
연산 결과 배열은 커질 수 있으므로 결과 shape도 확인해야 한다.

예를 들어 shape이 <code>(2, 3, 4)</code>인 배열과 <code>(3, 1)</code>인 배열은 다음처럼 비교한다.

~~~text
첫 번째 배열:  (2, 3, 4)
두 번째 배열:     (3, 1)
비교할 때:     (1, 3, 1)
결과:          (2, 3, 4)
~~~

마지막 축은 4와 1, 그 앞의 축은 3과 3, 맨 앞의 축은 2와 1이므로 모두 조건을 만족한다.
또한 양쪽 배열이 서로 다른 축에서 확장될 수도 있다.

~~~text
A:     (2, 1, 4, 1)
B:     (   3, 1, 5)
비교:  (1, 3, 1, 5)
결과:  (2, 3, 4, 5)
~~~

반면 <code>(2, 3, 4)</code>와 <code>(3,)</code>은 마지막 축의 4와 3이 맞지 않아 연산할 수 없다.
NumPy가 길이 3인 축을 찾아 자동으로 연결해 주는 것은 아니다.

인덱스 수식을 이용한 해석은
[13장 8절: 브로드캐스팅을 인덱스로 이해하기](/assets/lecture_notes/1_2_data_mse/data_mse_13_행렬벡터연산고급_Ein.md#broadcasting-indices)에서 다룬다.

## 8.4. 측정 데이터의 축에 맞추어 `None` 넣기

두 시편을 세 시점에서 측정하고, 매번 네 센서의 값을 저장했다고 하자.
배열 <code>data</code>의 shape은 <code>(2, 3, 4)</code>이며,
축의 의미는 순서대로 **시편, 시점, 센서**다.

~~~python
data = np.arange(24.0).reshape(2, 3, 4)
sensor_offset = np.array([10.0, 20.0, 30.0, 40.0])
corrected = data + sensor_offset
print(corrected.shape)  # (2, 3, 4)
print(corrected[0, 0])  # [10. 21. 32. 43.]
~~~

<code>sensor_offset</code>의 shape <code>(4,)</code>는 <code>(1, 1, 4)</code>처럼
맞춰지므로, 모든 시편과 시점에 같은 센서별 보정값이 적용된다.
성분으로 쓰면 <code>corrected[i, j, k] = data[i, j, k] + sensor_offset[k]</code>다.

이번에는 시점마다 다른 보정값을 더해 보자.

~~~python
time_offset = np.array([100.0, 200.0, 300.0])
# data + time_offset  # 마지막 축의 길이가 4와 3이므로 오류
corrected_time = data + time_offset[None, :, None]
print(time_offset[None, :, None].shape)  # (1, 3, 1)
print(corrected_time[0, :, 0])           # [100. 204. 308.]
~~~

배열 인덱싱에서 <code>None</code>은 **그 위치에 길이가 1인 새 축을 추가**한다.
<code>np.newaxis</code>와 같으며, 원소에 <code>None</code> 값을 저장한다는 뜻이 아니다.
위의 <code>:</code>는 기존의 시점 축을 유지하고, 양쪽의 <code>None</code>은
시편 축과 센서 축에 대응하는 새 축을 추가한다.
원래 <code>time_offset</code>은 여전히 shape이 <code>(3,)</code>이다.

~~~text
data:                          (2, 3, 4)
time_offset[None, :, None]:     (1, 3, 1)
결과:                          (2, 3, 4)
~~~

즉, <code>corrected_time[i, j, k] = data[i, j, k] + time_offset[j]</code>가 된다.
시편별 값 두 개를 적용하려면 <code>specimen_offset[:, None, None]</code>으로
<code>(2, 1, 1)</code>을 만들면 된다.

**shape이 맞는 것과 데이터의 의미가 맞는 것은 별개다.**
가령 시점 수와 센서 수가 모두 4이면, shape <code>(4,)</code>의 시점별 값을 그대로 더해도
오류는 발생하지 않는다. 하지만 그 값은 마지막 축인 센서 축에 적용된다.
따라서 각 축의 의미를 적고, 보정값이 어느 축에 대응해야 하는지 먼저 정하자.

## 8.5. 평균을 뺄 때 `keepdims=True` 사용하기

각 시편·시점에서 네 센서의 평균을 빼려면, 센서 축인 <code>axis=2</code>에 대해 평균을 구한다.

~~~python
sensor_mean = data.mean(axis=2)
print(sensor_mean.shape)  # (2, 3)
# data - sensor_mean     # (2, 3, 4)와 (2, 3)은 브로드캐스팅 불가

sensor_mean = data.mean(axis=2, keepdims=True)
centered = data - sensor_mean
print(sensor_mean.shape)       # (2, 3, 1)
print(centered.shape)          # (2, 3, 4)
print(centered.mean(axis=2))   # [[0. 0. 0.], [0. 0. 0.]]
~~~

기본적으로 평균을 구한 축은 사라진다. <code>keepdims=True</code>를 사용하면
**평균을 구한 축을 길이 1로 남겨 두므로**, 원래 데이터의 축과 맞추어 다시 연산하기 쉽다.
이 예제에서는 <code>data - data.mean(axis=2)[:, :, None]</code>도 같은 결과를 준다.

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
matrix_csv = np.loadtxt("matrix_01.csv",delimiter=",")
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

np.savetxt("saved_matrix.txt",matrix,fmt="%.2f")
np.savetxt("saved_matrix.csv",matrix,delimiter=",",fmt="%d")
~~~

- <code>fmt="%.2f"</code>: 실수를 소수점 아래 둘째 자리까지 저장
- <code>fmt="%d"</code>: 정수(integer) 형식으로 저장
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
# area_mm2.shape: (3,1)
~~~

<code>force_n</code>의 shape은 <code>(3, 3)</code>이고 <code>area_mm2</code>의
shape은 <code>(3, 1)</code>이다. 같은 행의 힘 세 개를
그 시편의 단면적 하나로 각각 나눈다. 이때 길이가 1인 열 방향으로 브로드캐스팅이 적용된다.

~~~python
stress_mpa = force_n / area_mm2
mean_stress_mpa = stress_mpa.mean(axis=1)

print(stress_mpa)
print(mean_stress_mpa)
~~~

$1\ \mathrm{N/mm^2}=1\ \mathrm{MPa}$이므로 응력 단위는 MPa이다. 각 행의 평균을
구했으므로 시편별 평균응력 세 개가 나온다.

다음은 shape은 맞지만 시편별 면적을 잘못 적용하는 예제다. 앞의 결과와 비교해 보자.
~~~python
force_n = np.array([
    [1000.0, 1020.0, 980.0],
    [1500.0, 1530.0, 1470.0],
    [2000.0, 1980.0, 2020.0],
])

area_mm2 = np.array([10.0, 12.0, 20.0])
## area_mm2.shape: (3,)

stress_mpa = force_n / area_mm2
mean_stress_mpa = stress_mpa.mean(axis=1)

print(stress_mpa)
print(mean_stress_mpa)
~~~

두 번째 예제의 <code>area_mm2</code>는 마지막 축, 즉 측정 순서에 대응한다.
따라서 같은 시편의 힘을 10, 12, 20으로 각각 나누어 물리적 의미가 달라진다.
시편 수와 측정 횟수가 모두 3이어서 오류 없이 실행된다는 점에 주의하자.
시편별 면적을 적용하려면 <code>force_n / area_mm2[:, None]</code>으로 고친다.

# 12. 자주 만나는 오류

## 12.1. IndexError

배열 범위를 벗어난 위치를 선택하면 발생한다. 배열의 shape을 확인하고, 인덱스가 0부터 시작한다는 점에 주의하자.

## 12.2. ValueError: cannot reshape

원소 개수와 새 shape의 원소 개수가 다를 때 발생한다.

~~~python
values = np.arange(12)
print(values.size)
values.reshape(3,4)
values.reshape(5,3)  # ValueError 발생
~~~

12개 원소는 <code>(3, 4)</code>로 바꿀 수 있지만 <code>(5, 3)</code>으로는 바꿀 수 없다.

## 12.3. 브로드캐스팅 오류

두 shape이 브로드캐스팅 규칙에 맞지 않으면 오류가 발생한다. 연산 전에 두 배열의
<code>shape</code>을 출력하여 마지막 축부터 비교한다.

# 13. 정리

- 인덱스는 0부터 시작하며 슬라이싱의 stop 위치는 포함하지 않는다.
- 2차원 배열에서 쉼표 앞은 행, 뒤는 열 인덱스이다.
- 기본 슬라이싱으로 얻은 뷰(view)는 원본 데이터를 공유한다.
- 독립적인 배열이 필요하면 <code>copy()</code>를 사용한다.
- 평균·합계 등의 집계에서 <code>axis</code>는 계산할 축을 지정한다. 기본적으로 그 축이 사라지고, <code>keepdims=True</code>이면 길이 1로 남는다.
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

다음 2행 3열 배열에서 각 행의 평균을 구하려면,
<code>np.mean()</code>의 <code>axis</code> 인자에 어떤 값을 지정해야 하는가?

~~~python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
~~~

<!--
풀이와 해답:
np.mean(A, axis=1)을 사용한다.
A.mean(axis=1)
-->

## 문제 6

CSV 파일 <code>data.csv</code>를 <code>np.loadtxt()</code>로 읽는 표현을 쓰시오.

<!--
풀이와 해답:
np.loadtxt("data.csv", delimiter=",")
-->

## 문제 7

슬라이싱한 배열의 데이터를 별도로 복사할 때 사용하는 NumPy 메서드는 무엇인가?

<!--
풀이와 해답:
copy()이다.
-->

## 문제 8: 여러 축의 브로드캐스팅

다음 shape 쌍마다 덧셈이 가능한지 판단하고, 가능하면 결과 shape을 쓰시오.

1. <code>(5, 2, 3)</code>과 <code>(3,)</code>
2. <code>(5, 2, 3)</code>과 <code>(2,)</code>
3. <code>(5, 1, 3)</code>과 <code>(2, 1)</code>
4. <code>(2, 1, 4, 1)</code>과 <code>(3, 1, 5)</code>

<!--
풀이와 해답:
1. 가능, (5, 2, 3). 두 번째 shape을 (1, 1, 3)처럼 비교한다.
2. 불가능. 마지막 축의 3과 2가 서로 다르고 어느 쪽도 1이 아니다.
3. 가능, (5, 2, 3). 두 번째 shape은 (1, 2, 1)처럼 비교한다.
4. 가능, (2, 3, 4, 5). 두 번째 shape은 (1, 3, 1, 5)처럼 비교한다.
-->

## 문제 9: 원하는 축에 보정값 적용하기

<code>data.shape == (2, 3, 4)</code>이고 각 축은 시편, 시점, 센서를 뜻한다.
시편별 보정값 <code>offset = np.array([10.0, 20.0])</code>을 모든 시점과 센서에
더하는 코드를 쓰시오. 또한 각 시편·센서에 대해 시점 평균을 빼려면
<code>mean</code>의 <code>axis</code>와 <code>keepdims</code>를 어떻게 설정해야 하는가?

<!--
풀이와 해답:
corrected = data + offset[:, None, None]
offset[:, None, None]의 shape은 (2, 1, 1)이다.
centered = data - data.mean(axis=1, keepdims=True)
평균 배열의 shape은 (2, 1, 4), 결과의 shape은 (2, 3, 4)이다.
-->

---

[이전 강의](/assets/lecture_notes/1_2_data_mse/data_mse_09_NumPy기초1.md) · [강의 목록](/_lectures/1_2_data_mse.md) · [다음 강의](/assets/lecture_notes/1_2_data_mse/data_mse_11_벡터연산기초.md)
