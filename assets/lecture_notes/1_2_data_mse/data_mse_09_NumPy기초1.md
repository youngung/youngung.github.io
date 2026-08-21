---
layout: distill
title: 데이터 재료과학 (제 7강)
description: IO
target: 1학년 2학기
permalink:
featured: true
prerequisite: 재료공학개론1
toc:
#sidebar: left
#- name: Orientation
#- name: Week1
#- name: Week2
#- name: Week3
#- name: Week4
#- name: Week5
#- name: Week6

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
- [2. 기초 개념](#2-기초-개념)
- [3. 차원과 축: NumPy 배열을 바라보는 두가지 관점](#3-차원과-축-numpy-배열을-바라보는-두가지-관점)


# 1. 목표
Numerical Python package. Python을 활용한 수학적 연산은 파이썬 본연의 built-in
자료 객체 (List, Set, 등)를 활용하면 연산 속도가 느리다. 따라서 수학적 연산을 빠르게
수행하고자 만든 패키지이며 매우 널리 쓰인다. 본 강의에서는 NumPy의 기초 활용 방법을 배운다.

# 2. 기초 개념
- [NumPy](https://numpy.org)는 파이썬 환경에서, 고성능 수치 계산을 위한
  library이다. 사실 빠른 연산을 위해 최적화된 [C](https://www.c-language.org)나
  [FORTRAN](https://fortran-lang.org) library를 활용한다.
- 공식 사이트에서 더욱 상세히 배울 수 있다: [링크](https://numpy.org/devdocs/user/quickstart.html).

앞서 List를 활용하여, math package를 함께 사용하면, 스칼라, 벡터, 행렬 등을 대상으로
다양한 수학적 연산을 수행할 수 있다. 하지만 Python의 built-in 기능으로는 빠른 수학적
연산처리가 어렵다. 이를 보완하고자 연산속도가 빠르면서도 다양한 수학적 기능을 도와주는
[NumPy](https://numpy.org)패키지가 개발되었다. NumPy설치를 위해서는 ```pip```를
활용할 수 있다. 인터넷이 연결된 컴퓨터의 CLI환경에서 다음과 같이 명령어를 입력하면 설치가
가능하다. 인터넷으로 연결된 시스템의 터미널에서 아래와 같이 입력하면 설치된다.

```dos
c:/users/user/myrepo> pip install numpy
```

이후 파이썬 환경에서 NumPy패키지를 import해 사용하면 되겠다. 많은 경우, 아래와 같이
```np```라는 이름으로 불러오는 경우가 많다.

```python
import numpy as np
```
다른 많은 Python 패키지들과 마찬가지로, open source 프로젝트로 개발되었으며, 현재로 활발히
업데이트가 되고 있다. 따라서 새로운 기능이 추가되거나, 종전의 기능이 없어지는 경우가 있으므로,
어떠한 버전을 활용하고 있는지 확인이 필요할 때가 있다. 그리고 한 시스템내에서 다양한 위치에
서로다른 패키지가 설치될 때가 있으므로, 사용되는 NumPy패키지의 위치를 확인할 필요가 있다.
아래의 두 경우를 살펴보자.

```python
import numpy as np
print(np.__version__)
print(np.__file__)
```

List로 생성된 값의 모임을 간단히 NumPy배열 형식 ```numpy.ndarray```로 간편히 바꿀 수 있다. 아래 예시들을 살펴보자.
```python
# 1차원 배열
arr1 = np.array([1, 2, 3]) # np.array 클래스 생성.
print(arr1)

# 2차원 배열
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# 0으로 채운 배열
zeros_arr = np.zeros((2, 3)) # zeros method 활용하여 2x3배열
print(zeros_arr)

# 1로 채운 배열
ones_arr = np.ones((3, 3)) # 3x3배열
print(ones_arr)

# 특정 값으로 채운 배열
full_arr = np.full((2, 2), 7)
print(full_arr)

# 연속된 수
range_arr = np.arange(0, 10, 2)  # 0부터 10 전까지 2씩 증가
print(range_arr)

# 랜덤 배열
rand_arr = np.random.rand(2, 3)  # 0~1 사이 난수로 이루어진 행렬
print(rand_arr)
```

```numpy.ndarray```형식은 NumPy의 array클래스의 instance로써, 다양한
속성(attributes)과 매서드(method) 갖고 있다. 아래의 attributes와 매서드가 자주
쓰인다. 그 쓰임을 익힐 필요가 있다.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)   # (2, 3) → 2행 3열
print(arr.ndim)    # 차원 수 → 2
print(arr.size)    # 전체 원소 개수 → 6
print(arr.dtype)   # 데이터 타입 → int64 (환경에 따라 다름)
print(arr.ravel()) ## memory-efficient
print(arr.flatten()) ## independent copy
print(arr.ravel().sum())
print(arr.flatten().sum())
```

NumPy의 배열간의 연산은 벡터화되어 속도가 빠르다. 많은 경우, `for`, `range` 등의
일반적인 반복문 필요없어, 간단한 형태로 표기되어, list를 활용한 것보다 간략한 수식을 코드로
구현하기 쉬우며 연산속도도 빠르다.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a * b)   # [ 4 10 18]  (요소별 곱)
print(a / b)   # [0.25 0.4 0.5]
print(a ** 2)  # [1 4 9]    (제곱)


## 각각의 경우 List를 활용했을 때 훨씬 많은 코딩 필요함.
c=[] # +
for i in range(a):
  c.append(a[i]+b[i])

c=[] # -
for i in range(a):
  c.append(a[i]-b[i])

c=[] # *
for i in range(a):
  c.append(a[i]*b[i])

c=[] # /
for i in range(a):
  c.append(a[i]/b[i])

c=[] # **
for i in range(a):
  c.append(a[i]**2)

##?
print((a**2).sum())
```

List를 활용한 방식과 NumPy의 속도 비교를 위해 아래 예제를 활용해보자. 우선 0에서부터
100까지 정수가 담겨있는 ```List```와 ```numpy.ndarray``` 형식의 자료를 만들자.

```python
mylist=list(range(101))
mylist ## The list type object
myarray=np.array(mylist)
myarray ## The numpy type object
```
아래와 같이 각각의 연산을 JuPyter의 매직 키워드 ```%%timeit```를 활용해 7번 반복
연산해 평균 연산 속도를 측정해보자.
```python
%%timeit
s=0.
for i in range(100):
    s=s+mylist[i]
```
그리고 ```sum``` 매소드를 활용한 결과를 비교해보자.

```python
%%timeit
s=myarray.sum()
```

나의 경우에는 전자는
$$1.85 \mu s = 1.85 \times 10^{-6} s$$
그리고 후자는
$$539 ns = 538\times 10^{-9} s = 0.538 10^{-6} s$$
결과가 나왔다. 후자는 전자에 비해 약 1/3 정도의 시간만 필요하였다.

# 3. 차원과 축: NumPy 배열을 바라보는 두가지 관점
NumPy배열의 '차원'(dimension, 혹은 rank)는 배열이 몇 겹으로 중첩되어 있는지를 의미한다.
쉽게 말해, 데이터가 몇 단계의 리스트로 레이어로 감싸져 있는지에 따라 차원이 달라진다.
아래를 살펴보자.

```python
import numpy as np

a = np.array(5)                  # 스칼라 (0차원)
b = np.array([1, 2, 3])          # 벡터 (1차원)
c = np.array([[1, 2, 3],
              [4, 5, 6]])        # 행렬 (2차원)
d = np.array([[[1], [2], [3]],
              [[4], [5], [6]]])  # 행렬 (3차원) ... 혹은 ML/AI 관련 문헌에서
                                 # '텐서(tensor)'라 불림 - 수학/물리/역학 등의
                                 # 문헌에서 정의되는 '텐서'와 다름에 유의할 것.
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
```

차원과 다르게 '축'(axis)의 관점에서 배열을 바라보는 관점도 있다. 이때 '축'은 배열의
index방향을 의미한다. 즉, 다차원 배열에서 데이터를 접근하거나 연산할 때 어느 방향을 기준으로
하느냐에 따라 축이 달라진다. 다음 배열은 차원의 관점에서는 2차원임을 알 수 있다.
```python
c = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
```
이 경우 축이 2개인 것으로 이해할 수 있다. 첫번째 축 ```0```은 행을 따라 내려가는 방향
(세로, column-wise)이 되며, 축 ```1```은 열을 따라 가로로 가는 방향
(가로, row-wise)로 이해된다. 아래 각 열, 그리고 행 '축'을 따라 덧셈을 하는 경우를 살펴보자.

```python
c = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(c.sum(axis=0))  # 열별 합 → [12 15 18]
print(c.sum(axis=1))  # 행별 합 → [ 6 15 24]
## axis의 순서는 마지막, 마지막-1, 마지막-2, ...
## 이 경우, '행'과 '열'로 불리는 두 축만 있으며, 축의 순서는 '열' 그리고 '행' 순으로 이어진다.
```

3D 배열에서 축 번호는 '바깥'(혹은 마지막)부터 '안쪽' 순으로 0, 1, 2, ... 순으로 이어진다.

```python
d = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
```
```d.shape```은 ```(2,2,2)```이고, ```d.ndim```은 3이다. 즉 3차원이고, 총 세 축으로 이루어진다. 각 축을 따라 2개씩 element가 있는 구조로 이해할 수 있다. 이때
- ```axis=0``` 은 가장 바깥 차원 (가장 마지막)
- ```axis=1``` 은 중간 차원 (row)
- ```axis=2``` 는 가장 안쪽 차원 (column)
로 이해된다.

아래 경우를 더 살펴보자.
```python
a = np.arange(15)
```
위 결과로 1D 배열에 0에서부터 14까지 15개의 element 숫자가 자료가 ```a```에 저장된다.
이를 (3x5) 형태의 2D 배열로 형태를 바꿀 수 있다. ```reshape``` method를 활용한다.
```python
b=a.reshape(3,5)
```
이때 두 축이 활용된 것으로 볼 수 있고, 첫번째 축 ```axis=0```은 3 요소를, 두번째 축
```axis=1```은 5 요소를 가진 것으로 이해할 수 있다. 그 결과를 ```b```로 저장했고 그
결과를 출력해보자
```python
print(b)
```
다음과 같이 출력이 될것이다.
```
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
```
첫번째 축(```axis=0```)의 첫 요소는 [0,1,2,3,4], 그 다음은 [5,6,7,8,9], 마지막 세번째는 [10,11,12,13,14]가 된다. 이를 인덱싱 해보면
```python
print(b[0,:])
print(b[1,:])
print(b[2,:])
```

이번에는 두번째 축 (```axis==1```)을 따라 살펴보자.
첫 요소는 [0,5,10], 그 다음은 [1,6,11], [2,7,12], [3,8,13], 마지막 5번째 요소는 [4,9,14]가 될 것이다.
```python
print(b[:,0])
print(b[:,1])
print(b[:,2])
```