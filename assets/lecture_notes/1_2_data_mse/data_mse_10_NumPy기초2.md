---
layout: distill
title: 데이터 재료과학
description: 데이터 분석/해석 및 시각화(그래프) 등 기초 컴퓨터 활용 능력
target: 1학년 2학기
permalink:
featured: true
prerequisite: 재료공학개론1
toc:
#sidebar: left
- name: Orientation
- name: Week1
- name: Week2
- name: Week3
- name: Week4
- name: Week5
- name: Week6

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

- [1. 목표](#1-목표)
- [2. 인덱싱(indexing)과 슬라이싱(slicing)](#2-인덱싱indexing과-슬라이싱slicing)
- [3. 예제](#3-예제)
  - [3.1. 예제: 데이터 파일](#31-예제-데이터-파일)
  - [3.2. 예제: csv file](#32-예제-csv-file)
  - [3.3. 예제: 저장하기](#33-예제-저장하기)
- [4. List활용한 기초 벡터/행렬 연산](#4-list활용한-기초-벡터행렬-연산)
  - [4.1. 기본 예제 (벡터의 크기, 내적)](#41-기본-예제-벡터의-크기-내적)


# 1. 목표
- Indexing & Slicing 이해
- 다양한 벡터/행렬 연산을 NumPy 라이브러리 활용해 수행할 수 있다.
- 브로드캐스팅을 이해한다.
- Determinant, Eigenvalue 등을 계산할 수 있다.

# 2. 인덱싱(indexing)과 슬라이싱(slicing)

- List 타입의 자료에서도 indexing과 slicing이 사용된다. [시작,끝,스텝]형태의 인덱싱이 NumPy 배열에도 동일하게 적용된다.

```python
mylist=List((3,3,4,3,3,4,5,6))
#mylist[시작:끝:스텝] 형태로 index가 적용되는 것 처럼 ..
```

```python
myarray=np.array((3,3,4,3,3,4,5,6))
myarray[2:6:2] #3번째부터 6번째까지, 2칸씩 띄어 넘으며 ..
#mylist[시작:끝:스텝] 형태로 index가 적용되는 것 처럼 ..
```

위 결과는 아래와 같을 것이다.

```python
array([ 5, 10])
```

- NumPy 배열에 경우에는 이러한 indexing이 각 '축'에 깔끔히 적용될 수 있다.
 아래 2차원 배열 (혹은 2축으로 구성된 배열)을 살펴보자.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

위의 경우, 첫번째 축(axis=0)은 2개의 요소 그 다음 축(axis=1)은 3개의 요소로 이루어진 것을 알 수 있다. 즉

```python
# nested 배열의 각 축을 '행'(가로)과 '열'(세로)이라 하면
# arr = [  1  2  3 ] # 첫번째 가로
#.         4  5  6   # 두번째 가로

print(arr[0, 0])  # 1행 1열 → 1
print(arr[1, :])  # 2행 전체 → [4 5 6]
print(arr[:, 1])  # 모든 행의 2열 → [2 5]
```

각 축마다 begin, end, step이 적용되므로, 복잡한 slicing을 할 수 있다. 아래를 보자.
```python
## 각 '축'에서 List indexing 적용가능. 예를 들어
print(arr[1::,1::])
print(arr[::2,::2])

#
print(arr[::-1,::])  #행만 거꾸로
print(arr[::,::-1])  #열만 거꾸로
print(arr[::-1,::-1]) #행과 열을 모두 거꾸로
```

아래 경우를 하나씩 입력 후 차근차근 살펴보며 실습해보자.
```python
a=np.arange(100)
a=a.reshape(10,10)
a[:,::2]  # 각 10자리에서 짝수로만 이루어진 2차원 배열
a[0::2,::] # 10자리수가 짝수로 이루어진 2차원 배열
a[1::2,::] # 10자리수가 홀수로 이루어진 2차원 배열
a[::,1::2] # 1의 자리수가 홀수로 이루어진 2차원 배열
a[::,0::3] # 1의 자리수가 0, 3, 6, 9로 끝나는 수로 이루어진 2차원 배열
a[0::3,::] # 10의 자리수가 0, 3, 6, 9로 끝나는 수로 이루어진 2차원 배열
```

다음 3차원의 경우도 살펴보자.

```python
a=np.arange(1000)
a=a.reshape(10,10,10) #
a[::5,::,::] #?
```

# 3. 예제

## 3.1. 예제: 데이터 파일
  Use data in here [matrix_01.txt](/assets/dat_files/lectures/1_2_data_mse/matrix_01.txt)

  ```python
  import numpy as np

  # 공백 구분 텍스트 불러오기
  matrix = np.loadtxt("matrix.txt")

  print("불러온 행렬:")
  print(matrix)

  print("shape:", matrix.shape)   # (3, 3)
  print("dtype:", matrix.dtype)   # ?
  ```

## 3.2. 예제: csv file
  Use data in here [matrix_01.csv](/assets/dat_files/lectures/1_2_data_mse/matrix_01.csv)

  ```python
  import numpy as np

  # 공백 구분 텍스트 불러오기
  matrix = np.loadtxt("matrix.txt")

  print("불러온 행렬:")
  print(matrix)

  print("shape:", matrix.shape)   # (3, 3)
  print("dtype:", matrix.dtype)   # ?
  ```

## 3.3. 예제: 저장하기
<aside><p>%d 와 %f로 정수는 각각 정수와 실수 형식 저장에 쓰인다.</p></aside>

```python
# 행렬 저장하기 (공백 구분)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt("save_matrix.txt", matrix, fmt="%.2f")

# CSV로 저장
np.savetxt("save_matrix.csv", matrix, delimiter=",", fmt="%d")
```


# 4. List활용한 기초 벡터/행렬 연산

## 4.1. 기본 예제 (벡터의 크기, 내적)

3차원 벡터는, 가령 아래와 같이 세 성분으로 이루어져 있으며,

$$
\boldsymbol a=(a_1,a_2,a_3)
$$

그 크기는 다음과 같이 정의된다.

$$
|\boldsymbol a|=\sqrt{a_1^2+a_2^2+a_3^2}=\sqrt{\sum_i^3a_i^2}.
$$

주어진 벡터 `v`의 크기를 구하는 함수 `get_mag`를 아래의 예와같이 작성될 수 있겠다.

```python
def get_mag(v):
    """
    벡터의 크기 구하기
    """
    import math
    return math.sqrt(v[0]**2+v[1]**2+v[2]**2)

    ## 혹은 아래와 같이 math 모듈의 sqrt 함수 없이 계산 가능하다.
    ## return (v[0]**2+v[1]**2+v[2]**2)**0.5
```

주어진 벡터를 3차원에서 벗어나 n차원 공간으로 일반화 한다면
([Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm))
정의를 활용해 다음과 같이 표현할 수 있다.

$$
|\boldsymbol a|=\sqrt{\sum_i^na_i^2}
$$

위를 다음과 같은 파이썬 코드로 작성할 수 있다.

```python
def frob(vector):
    """
    Generalized vector's norm - Frobenius norm
    """
    import math
    s=0. # sum
    for i, e in enumerate(vector):
       s=s+e**2
    return math.sqrt(s)
```

두 벡터 $\boldsymbol a$와 $\boldsymbol b$의 내적은 다음과 같이 정의된다.

$$
\boldsymbol a \cdot \boldsymbol b=a_1b_1+a_2b_2+a_3b_3=\sum_i^3a_ib_i
$$

혹은 아래와 같이 두 벡터 사이의 끼인 각 $\theta$를 활용해 표현할 수 있다.

$$
\boldsymbol a \cdot \boldsymbol b=|\boldsymbol a||\boldsymbol b|\cos\theta
$$

두 벡터 사이의 내적을 `list`, `len`, `range`, `enumerate` 등을 활용하여 아래와 같이 표현 가능하다.

```python
a=[1,2,3]
b=[4,5,6]
dotprod=0.
for i in range(3):
   dotprod=dotprod+a[i]*b[i]
   ## 위를 `dotprod+=a[i]*b[i]`로 줄여서 표현 가능
```

NumPy의 배열을 활용한다면 위를 더욱 축약 시킬 수 있다.

```python
a=np.array([1,2,3])
b=np.array([4,5,6])
dotprod=0.
for i in range(len(a)):
   dotprod+=a[i]*b[i]
print(dotprod)
```

혹은 위를 더 축약 시켜

```python
a=np.array([1,2,3])
b=np.array([4,5,6])
dotprod=0.
print((a[i]*b[i]).sum())
```

혹은 @을 활용하여 다음과 같이 더욱 축약하여 작성할 수 있다.

```python
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a@b)
```
