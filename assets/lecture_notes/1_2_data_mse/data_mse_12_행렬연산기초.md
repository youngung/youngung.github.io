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

- [1. 행렬간의 내적 (dot product) 이해하기](#1-행렬간의-내적-dot-product-이해하기)
- [2. 두 3x3 행렬 곱? 일반화하여, nxn 행렬사이의 곱은?](#2-두-3x3-행렬-곱-일반화하여-nxn-행렬사이의-곱은)
- [3. 예제](#3-예제)
  - [3.1. Loop 표현](#31-loop-표현)
  - [3.2. 일반적 행렬곱](#32-일반적-행렬곱)
  - [3.3. 예제 3.](#33-예제-3)
  - [3.4. 예제 4.](#34-예제-4)
  - [3.5. 예제 5. 세 행렬의 곱](#35-예제-5-세-행렬의-곱)
- [4. Broadcasting](#4-broadcasting)
- [5. Other various features](#5-other-various-features)

# 1. 행렬간의 내적 (dot product) 이해하기

[두 행렬의 곱](https://ko.wikipedia.org/wiki/행렬_곱셈)을 이해해보자. 행과 열이 각각
$(l,m)$인 행렬

$$\boldsymbol{A}_{l\times m}$$

와 $(m,n)$인

$$\boldsymbol{B}_{m\times n}$$

의 곱은 새로운 행렬 $\boldsymbol{C}$가 된다. $\boldsymbol{C}$ 행렬의 행과 열은
($l,n$)이 되며 다음과 같이 표기되곤 한다.

$$\boldsymbol{C}=\boldsymbol{A}\cdot\boldsymbol{B}$$

이때, 앞선 행렬의 한 행의 요소와, 뒷따르는 행렬의 열 요소들이 각기 순서대로 곱해져서 새로운 행렬 $\boldsymbol{C}$를 이루게 되며, 그 방식이 아래 그림에 표기되어 있다.

<p align="center">
  <img src=https://upload.wikimedia.org/wikipedia/commons/e/eb/Matrix_multiplication_diagram_2.svg />
</p>

예를 아래 두 벡터의 곱의 예를 함께 살펴보자,

$$
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\cdot
\begin{bmatrix}
2 & 0 \\
1 & 3
\end{bmatrix}
= ?
$$

두 2x2 행렬 $\boldsymbol A$와 $\boldsymbol B$를 곱하여 행렬 $\boldsymbol C$가 된다면, 아래와 같이 표현한다.

$$
\boldsymbol C = \boldsymbol A \cdot \boldsymbol B
$$

이 때

$$
\begin{array}{c}
C_{11}=A_{11}B_{11}+A_{12}B_{21} \\
C_{12}=A_{11}B_{12}+A_{12}B_{22} \\
C_{21}=A_{21}B_{11}+A_{22}B_{21} \\
C_{22}=A_{21}B_{12}+A_{22}B_{22} \\
\end{array}
$$

가 된다. 이를 그대로 Python으로 옮기면

```python
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 3]]

C=[[0,0],[0,0]]
C[0][0]=A[0][0]*B[0][0]+A[0][1]*B[1][0]
C[0][1]=A[0][0]*B[0][1]+A[0][1]*B[1][1]
C[1][0]=A[1][0]*B[0][0]+A[1][1]*B[1][0]
C[1][1]=A[1][0]*B[0][1]+A[1][1]*B[1][1]
print('1:',C)
```

위 행렬곱 식에서 $\boldsymbol{C}$ 행렬 요소 위치에 따라 달라지는
$\boldsymbol{A}$와 $\boldsymbol{B}$ 행렬의 위치가 있다.
이를 살펴보면

$$
C_{ij}=A_{i1}B_{1j}+A_{i2}B_{2j}
$$

로 표현됨을 알 수 있다. 이를 반영하여 모든 $(i,j)$ 짝에 적용하면...

```python
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 3]]

C=[[0,0],[0,0]]
i=0;j=0
C[i][j]=A[i][0]*B[0][j]+A[i][1]*B[1][j]
i=0;j=1
C[i][j]=A[i][0]*B[0][j]+A[i][1]*B[1][j]
i=1;j=0
C[i][j]=A[i][0]*B[0][j]+A[i][1]*B[1][j]
i=1;j=1
C[i][1]=A[i][0]*B[0][j]+A[i][1]*B[j][1]
print('2:',C)
```

그런데, 코드를 살펴보면, 아래의 동일한 statements가 4번 반복되는 것을 알 수 있다.

```python
C[i][j]=A[i,0]*B[0,j]+A[i,1]*B[j,1]
```

$(i,j)$가 각각 `for`구문을 통해 0,1을 반복하므로, 아래와 같이 축약할 수 있겠다.

```python
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 3]]

C=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        C[i][j]=A[i][0]*B[0][j]+A[i][1]*B[1][j] ## 네 statements가 동일함에 주목!
print('3:',C)
```

그런데, 반복되던 statement의 우변에서도 0과 1이 반복된다.

```python
C[i][j]=A[i][0]*B[0][j]+A[i][1]*B[j][1]
```

따라서

```python
for k in range(2):
   C[i][j]=C[i][j]+A[i][k]*B[k][j]
```

라 줄일 수 있겠다.
이렇게 모두 줄일 수 있는 만큼 줄여서 축약된 형태로 표현하면 ..

```python
#더 줄이면?
C=[[0,0],[0,0]]
for i in range(2):
	for j in range(2):
		for k in range(2):
			C[i][j]=C[i][j]+A[i][k]*B[k][j]
			#C[i][j]+=A[i,k]*B[k,j]      += 기호 사용
print('4:',C)
```

두 2x2행렬 곱은, 아래 더 상세히 배우게 될 `NumPy`패키지를 활용하면 더욱 축약된 형태로 작성가능하다.

```python
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])
print('6:',A @ B)          # 행렬 곱
print('7:',np.dot(A, B))   # 동일
```

# 2. 두 3x3 행렬 곱? 일반화하여, nxn 행렬사이의 곱은?

행렬 $\boldsymbol A$ 와 $\boldsymbol B$ 의 곱 결과가 또 다른 3x3행렬 $\boldsymbol C$ 이라면

$$
\boldsymbol A\cdot\boldsymbol B = \boldsymbol C
$$

와 같이 표현할 수 있다. 이를 **index**를 활용한 방식으로 아래와 같이 표기 가능하다.

$$
\sum_k^3A_{ik}B_{kj}=C_{ij}, \text{ for } i=1,2,3 \text{ and } \   j=1,2,3
$$


# 3. 예제

## 3.1. Loop 표현

```python
# For loop 3개를 활용해서 표현
C=np.zeros((3,3))
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                C[i,j]=C[i,j]+A[i,k]*B[k,j]
```

## 3.2. 일반적 행렬곱

```python
# 두 nxn 행렬 사이의 곱을 구하는 python 함수를 작성해 보세요.
# 규칙성을 찾고, 그 규칙성을 구현해 보세요.
```

## 3.3. 예제 3.
격자 상수 $(a,b,c)$가 주어진 Tetragonal에서의 격자 위치 $(p_1,p_2,p_3)$가 주어질 때,
격자 위치를 행렬을 활용해 unit cell내에서의 위치로 표현할 수 있다.

우선 아래와 같이 행렬 $A$를 구한다.

$$
A=\begin{bmatrix}
a & 0 & 0 \\
0 & b & 0 \\
0 & 0 & c \\
\end{bmatrix}
$$

다음으로 격자 위치로 이루어진 벡터를 곱한다.

$$
A\cdot p =\begin{bmatrix}
a & 0 & 0 \\
0 & b & 0 \\
0 & 0 & c \\
\end{bmatrix}\cdot
\begin{bmatrix}
p_1\\p_2\\p_3
\end{bmatrix}
$$

그 결과 벡터가 실제 unit cell내의 위치가 된다.


## 3.4. 예제 4.
격자 상수 $(a,b,c)$가 주어진 Tetragonal에서의 두 격자 위치 $p=(p_1,p_2,p_3)$와
$q=(q_1,q_2,q_3)$가 주어질 때, 두 격자 위치 사이의 거리를 구해보자.

우선 아래와 같이 행렬 $A$를 구한다.

$$
A=\begin{bmatrix}
a & 0 & 0 \\
0 & b & 0 \\
0 & 0 & c \\
\end{bmatrix}
$$

다음으로 격자 위치로 이루어진 벡터를 곱한다.

$$
p^\prime=A\cdot p =\begin{bmatrix}
a & 0 & 0 \\
0 & b & 0 \\
0 & 0 & c \\
\end{bmatrix}\cdot
\begin{bmatrix}
p_1\\p_2\\p_3
\end{bmatrix}
$$

$$
q^\prime=A\cdot q =\begin{bmatrix}
a & 0 & 0 \\
0 & b & 0 \\
0 & 0 & c \\
\end{bmatrix}\cdot
\begin{bmatrix}
q_1\\q_2\\q_3
\end{bmatrix}
$$

두 점 $p^\prime$과 $q^\prime$ 사이의 거리는

$$
|p^\prime - q^\prime]
$$
에 해당한다.



## 3.5. 예제 5. 세 행렬의 곱
  세 행렬 사이의 곱이 다음과 같다.

$$
\boldsymbol D=\boldsymbol A \cdot \boldsymbol B \cdot \boldsymbol C
$$

이를 인덱스 notation으로 표현하면

$$
D_{ij}=A_{ik}B_{kl}C_{lj}=\sum_k\sum_l A_{ik}B_{kl}C_{lj} \text{ for } (i,j) = (1,1), (1,2), ..., (3,3)
$$

```python
# 세 nxn 행렬 사이의 곱을 구하는 python 함수를 작성해 보세요.
```


# 4. [Broadcasting](https://numpy.org/devdocs/user/basics.broadcasting.html#basics-broadcasting)

- 브로드캐스팅은 서로 다른 shape의 배열끼리 연산할 때 NumPy가 자동으로 차원을 맞춰주는 기능

- 예시 (1차원+0차원(스칼라))

  ```python
  arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
  print(arr + 10)  # [11 12 13 ... 19] ## stretched ..
  ```

- 예시 (2차원 + 1차원)

  ```python
  mat = np.array([[1, 2, 3],
  			  [4, 5, 6]])
  vec = np.array([10, 20, 30])

  print(mat + vec)
  # [[11 22 33]
  #  [14 25 36]]
  ```

- 주의!

  뒤에서부터 비교하며 차원이 같거나 1이면 확장 가능
  하나라도 불가능하면 에러 발생

# 5. Other various features

```python
arr = np.array([1, 4, 9, 16])

print(np.sqrt(arr))   # 제곱근 → [1. 2. 3. 4.]
print(np.exp(arr))    # e^x
print(np.log(arr))    # 자연로그
print(np.sin(arr))    # 사인 함수
print(np.mean(arr))   # 평균
print(np.sum(arr))    # 합
print(np.min(arr))    # 최소값
print(np.max(arr))    # 최대값
print(np.std(arr))    # 표준편차

arr = np.array([3, 1, 2])

print(np.sort(arr))        # 정렬된 배열
print(np.argsort(arr))     # 정렬 인덱스
print(np.argmax(arr))      # 최대값 인덱스
print(np.argmin(arr))      # 최소값 인덱스

ind=np.argsort(arr)
arr[ind] ## sorting 이 된 배열

# 추가 예제
names=['Michael','Jim','Pam','Dwight','Kevin','Creed']
scores=[5, 30, 20, 40, 10, 25]

inds=np.argsort(scores)
print(names[inds]) ## score에 따라 정렬된 배열
```
