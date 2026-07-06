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


- [제1강 orientation]({% link _lectures/1_2_data_mse/01_data_mse.md %})

- [제2강 기초 조작 및 실습]({% link _lectures/1_2_data_mse/02_data_mse.md %})

- [제3강 기초 자료 구조]({% link _lectures/1_2_data_mse/03_data_mse.md %})

- [제4강 조건문과 반복문]({% link _lectures/1_2_data_mse/04_data_mse.md %})

- [제5강 함수]({% link _lectures/1_2_data_mse/05_data_mse.md %})

- [제6강 IO]({% link _lectures/1_2_data_mse/06_data_mse.md %})




# 7. Week5
- NumPy 02 - 배열 연산(산술, 내적, 외적), 브로드캐스팅, 그 외 기타 함수
- 목표
  - 다양한 벡터/행렬 연산을 NumPy 라이브러리 활용해 수행할 수 있다.
  - 브로드캐스팅을 이해한다.
  - Determinant, Eigenvalue 등을 계산할 수 있다.

## 7.1. 수업 05-1 (List활용한 기초 행렬 연산)

### 7.1.1. 기본 예제 (벡터의 크기, 내적)

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
   import math
   return math.sqrt(v[0]**2+v[1]**2+v[2]**2)
```

주어진 벡터를 3차원에서 벗어나 n차원 공간으로 일반화 한다면 ([Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm))정의를 활용해 다음과 같이 표현할 수 있다.

$$
|\boldsymbol a|=\sqrt{\sum_i^na_i^2}
$$

이를 다시 다음과 같은 파이썬 코드 예시로 작성할 수 있겠다.

```python
def frob(vector):
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

두 3D 벡터가 주어졌을 때 사이 끼인 각을 구하려면, 앞서 활용된 서로다른 두 벡터의 정의를 함께 활용할 수 있다. 즉

$$
\boldsymbol a \cdot \boldsymbol b=a_1b_1+a_2b_2+a_3b_3=\sum_i^3a_ib_i=|\boldsymbol a||\boldsymbol b|\cos\theta
$$

위 식을 정리하여 활용하면 아래와 같다.

$$
\frac{a_1b_1+a_2b_2+a_3b_3}{|\boldsymbol a||\boldsymbol b|}=\cos\theta
$$

따라서

$$
\theta=\cos^{-1}\bigg(\frac{a_1b_1+a_2b_2+a_3b_3}{|\boldsymbol a||\boldsymbol b|}\bigg)
$$

위를 `math`모듈과 그 모듈내의 `sqrt`, `acos`을 활용하여 아래와 같은 간단한 코드를 작성할 수 있다.
<aside><p>sqrt는 square root, 즉 제곱근에서 따왔고 acos 함수는 arccosine, 즉 코사인 함수의 역함수, $\cos^{-1}$ 에서 따왔다. </p></aside>

```python
def get_mag(v):
   import math
   return math.sqrt(v[0]**2+v[1]**2+v[2]**2)

def get_ang(a,b):
   import math
   dotprod=0.
   for i in range(len(a)):
      dotprod+=a[i]*b[i]
   costh=dotprod/(get_mag(a)*get_mag(b))
   print(f'costh:{costh}')
   th=math.acos(costh)
   return th

a=[1,0,0]
b=[0,1,0]
angle=get_ang(a,b)
print('ang in radian:', angle)
## angle to degree?
print('ang in degree:', angle*180/3.141592)
```

### 7.1.2. 행렬간의 dot product 이해하기

[두 행렬의 곱](https://ko.wikipedia.org/wiki/행렬_곱셈)을 이해해보자. 행과 열이 각각 (l,m)인 행렬

$$\boldsymbol{A}_{l\times m}$$

와 (m,n)인

$$\boldsymbol{B}_{m\times n}$$

의 곱은 새로운 행렬이 된다. 새로운 행렬을 $$\boldsymbol{C}$$라 하면, 그 행렬의 행과 열은 (l,n)이 되며 다음과 같이 표기되곤 한다.

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

두 2x2 행렬 $$\boldsymbol A$$와 $$\boldsymbol B$$를 곱하여 행렬 $$\boldsymbol C$$가 된다면, 아래와 같이 표현한다.

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

### 7.1.3. 두 3x3 행렬 곱? 일반화하여, nxn 행렬사이의 곱은?

행렬 $$\boldsymbol A$$ 와 $$\boldsymbol B$$ 의 곱 결과가 또 다른 3x3행렬 $$\boldsymbol C$$ 이라면

$$
\boldsymbol A\cdot\boldsymbol B = \boldsymbol C
$$

와 같이 표현할 수 있다. 이를 **index**를 활용한 방식으로 아래와 같이 표기 가능하다.

$$
\sum_k^3A_{ik}B_{kj}=C_{ij}, \text{ for } i=1,2,3 \text{ and } \   j=1,2,3
$$

- 05-1-3-1. 예제

```python
# for loop 3개를 활용해서 표현할 수 있겠는가?
```

- 05-1-3-2. 예제

```python
# 두 nxn 행렬 사이의 곱을 구하는 python 함수를 작성해 보세요.
```

- 05-1-3-3. 예제
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

### 7.1.4. 외적

- 설명

  두 벡터 $$\boldsymbol a, \boldsymbol b$$의 외적이 다음과 같이 표현된다.

  $$
  \boldsymbol c = \boldsymbol a \times \boldsymbol b
  $$

  $$
  c_i=\epsilon_{ijk}a_jb_k
  $$

  어떻게 파이썬으로 구현할 수 있나?

  ```python
  import numpy as np

  a = np.array([1, 2, 3])
  b = np.array([4, 5, 6])

  c = np.cross(a, b)
  print(c)  # [-3  6 -3]
  ```

- 예시 ~~tetrahedral site & octaheral site 크기 구하기~~

### 7.1.5. [Broadcasting](https://numpy.org/devdocs/user/basics.broadcasting.html#basics-broadcasting)

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

### 7.1.6. Other various features

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

## 7.2. 수업 05-2 [아인슈타인 표기법](https://ko.wikipedia.org/wiki/아인슈타인_표기법)과 [np.einsum](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html) 함수

Reference: [https://rockt.ai/2018/04/30/einsum](https://rockt.ai/2018/04/30/einsum)

아인슈타인 표기법은, 벡터, 행렬, 텐서가 사용된 수학 수식에서, 중복된 기호와 합기호 $\sum$가 함께 나타나는 연산을 표기할 때, 합기호를 생략하는데 착안하여 복잡한 수식을 좀 더 간략하게 표기하는 방식이다.
아래 수식에서 한 기호가 하나의 값을 표현할 때는 굵지 않은 글씨체로 ($a$), 만약 벡터와 같이 하나의 기호가 여러 값으로 이루어져 있을 때는 굵은 글씨체 ($\boldsymbol a$)로 표기하겠다.

### 7.2.1. 벡터 스케일링 (스칼라 곱)

주어진 벡터 $\boldsymbol a$에 스칼라 $c$를 곱하면 또 다른 벡터 $\boldsymbol b$이 된다. 이는 아래와 같이 수식으로 표현가능하다.

$$
c\boldsymbol a=\boldsymbol b
$$

이를 index 표기법으로 나타내면, 3차원 공간에서 각 벡터는 3성분을 지니므로, 아래 첨자 $_i$를 활용해 각 첨자를 구분할 수 있다. 즉 벡터 $\boldsymbol a$는 사실 $(a_1,a_2,a_3)$로 구분되는 세 성분으로 이루어져 있으며, 이는 벡터 $\boldsymbol b$도 마찬가지이다. 따라서 앞선 수식을 각 성분에 대해 나타낸다면, 각기 구분되는 세 수식 $b_1=ca_1$ 그리고 $b_2=ca_2$, 마지막으로 $b_3=ca_3$으로 대신할 수 있다. 그런데, 아무래도 이건 조금 번거로운 느낌이 든다. 아래와 같이 좀 더 간략하게 표기하는 게 좋겠다.

$$
b_i=ca_i \text{ with } i=1,2,3
$$

위를 Python의 List, 그리고 NumPy를 가지고 각기 표현할 수도 있겠다.

{% tabs vector %}
{% tab vector List %}

```python
## List로 구현
c=0.3
a=[1,2,3]
b=[] # empty list
for i in range(3): ## iteration
   b.append(c*a[i])
```

{% endtab %}
{% tab vector range와 len 활용 %}

```python
## Range와 len의 조합을 활용해, 임의의 크기를 가진 list에 적용 가능
c=0.3
a=[1,2,3,4,5]
b=[] # empty list
for i in range(len(a)): ## iteration
   b.append(c*a[i])
```

{% endtab %}
{% tab vector NumPy %}

```python
## NumPy로 구현
c=0.3
a=np.array([1,2,3])
b=c*a ## broadcasting (?!)
```

{% endtab %}
{% endtabs %}


### 7.2.2. 벡터의 크기

벡터의 크기는 앞서 이미 다루었다. 한 벡터 $\boldsymbol a$의 크기는 $|\boldsymbol a|$라 표기하고, 이는 다음과 같이 정의된다.

$$|\boldsymbol a|=\sqrt{\sum_i^3a_i^2}$$

고전적인 아인슈타인 표기법은 위와 같이 하나의 물리량에 일반적으로 적용되진 않는다. 하지만 NumPy의 einsum 함수는 적용된다. 아래와 같이 먼저 벡터내의 요소의 거듭제곱으로 이루어진 벡터를 구할 수 있다. 벡터 $\boldsymbol a$가 가령 아래와 같다고 하자.
$$\boldsymbol a= (2,3,4)
$$

```python
import numpy as np
a=np.array([2,3,4])
```
만약 2+3+4를 구하는게 목적이라면, 즉 $\sum_i a_i$가 목적이라면, 아래와 같이 수행할 수 있다.

```python
np.einsum('i->',a)
```

그런데 우리는 $\sum_ia_i^2$을 먼저 구해야 하겠다. 따라서 아래와 같이 약간 변화를 줄 수 있다.
```python
np.einsum('i->',a**2)
```

다음으로 이렇게 얻어진 값의 제곱근을 구해야 하므로 아래가 최종적으로 적절한 형식이 되겠다.

```python
np.sqrt(np.einsum('i->',a**2))
```

<aside><p>
실은 NumPy의 선형대수(Linear Algebra) 함수 모듬을 활용하여 더욱 간략히 수행할 수 있다.

```np.linalg.norm(a)```
</p></aside>


### 7.2.3. 단위 벡터 (unit)

벡터 $\boldsymbol a$의 크기가 1 이라면 (즉 $|\boldsymbol a=1|$), 벡터 $\boldsymbol a$ 를 단위 벡터(unit vector)라 부른다. 즉 단위 벡터란, 크기가 1인 벡터를 뜻한다.
주어진 한 벡터 $\boldsymbol a$의 단위 벡터를 $\bar{\boldsymbol a}$라 할 때, $\boldsymbol a$와 $\bar{\boldsymbol a}$의 관계를 다음과 같이 표현할 수 있다:

$$
\bar{\boldsymbol a}=\frac{\boldsymbol a}{|\boldsymbol a|}
$$

앞서 스칼라곱에서 보았듯, 마찬가지로 개별 성분값들을 활용한 index표기법을 활용해 아래와 같이 표현할 수 있다.

$$
\bar{a}_i=\frac{a_i}{\sqrt{a_1^2+a_2^2+a_3^2}}
$$

위 수식도 사실은 $i$가 1, 혹은 2, 혹은 3인 세 경우에 각기 해당하는 수식을 의미한다. 즉 위는 아래 표기법과 같이

$$
\bar{a}_i=\frac{a_i}{\sqrt{a_1^2+a_2^2+a_3^2}}, \text{ with } i=1,2,3
$$

의 $i=1,2,3$ 부분이 생략된 것이라 볼 수 있다. 정리하자면 아래 탭에 세가지 각기 다른 방식으로 표현된 수식들은 사실 모두 동일한 수식을 표현하고 있는 것이다.

{% tabs 수식 %}
{% tab 수식 굵은 글씨체 사용 %}

$$
\bar{\boldsymbol a}=\frac{\boldsymbol a}{|\boldsymbol a|}
$$

{% endtab %}
{% tab 수식 with사용 %}

$$
\bar{a}_i=\frac{a_i}{\sqrt{a_1^2+a_2^2+a_3^2}}, \text{ with } i=1,2,3
$$

{% endtab %}
{% tab 수식 with생략 %}

$$
\bar{a}_i=\frac{a_i}{\sqrt{a_1^2+a_2^2+a_3^2}}
$$

{% endtab %}
{% tab 수식 생략없이 %}

$$
\bar{a}_1=\frac{a_1}{\sqrt{a_1^2+a_2^2+a_3^2}},
\ \ \
\bar{a}_2=\frac{a_2}{\sqrt{a_1^2+a_2^2+a_3^2}},
\ \ \
\bar{a}_3=\frac{a_3}{\sqrt{a_1^2+a_2^2+a_3^2}}
$$

{% endtab %}
{% endtabs 수식 %}
index를 활용하되 아무런 생략없이 표기된 경우(`생략없이`)와 비교했을 때, `WITH생략`의 경우 얼마나 많이 수식에 활용된 표현이 축약될 수 있는지 비교해보자. 그리고 생략 되어 표기된 경우만 주어지더라도, 생략되지 않은 경우를 의미하는 바를 잘 파악할 수 있어야 하겠다. 굵은 글씨체로 표기된 경우가 가장 많이 생략된 표기법이나, index가 사용되지 않아 수식의 명확성이 높지 않을 수 있다. 마지막에 완전히 생략된 표기법은 Einstein 표기법을 이해하기 위한 기초가 된다.

### 7.2.4. 예제들

#### 7.2.4.1. 예시: 같은 방향 단위 벡터 구하기.

주어진 벡터 $\boldsymbol a$와 방향은 같으나 크기가 1인 단위 벡터를 구하는 Python 예제를 살펴보자.

{% tabs 단위벡터구하기 %}
{% tab 단위벡터구하기 수식 %}

$$
\bar{a}_i=\frac{a_i}{\sqrt{a_1^2+a_2^2+a_3^2}}
$$

{% endtab %}
{% tab 단위벡터구하기 List활용 %}

```python
a=[3,4,5]
magnitude=0. ## 벡터 크기
for i in range(len(a)):
	magnitude+=a[i]**2
magnitude=magnitude**0.5 ## sqrt(a)
for i in range(len(a)):
	a[i]=a[i]/mag
print(bar_a)
```

{% endtab %}
{% tab 단위벡터구하기 NumPy활용1 %}

```python
import numpy as np
old_a=np.array([3,4,5])
new_a=old_a**2
mag=np.sqrt(new_a.sum())
bar_a=old_a/mag
print(bar_a)
```

{% endtab %}
{% tab 단위벡터구하기 NumPy활용2 %}

```python
import nump as np
old_a=np.array([3,4,5])
bar_a=old_a/np.sqrt((old_a**2).sum())
print(bar_a)
```

{% endtab %}
{% endtabs %}

#### 7.2.4.2. 예시: 반대방향 벡터

한 벡터 $\boldsymbol a$와 크기가 같으나, 방향이 반대인 벡터를 $\boldsymbol b$라 한다면, 아래와 같은 결과를 얻는다.
{% tabs 반대방향벡터 %}
{% tab 반대방향벡터 굵은기호수식 %}

$$
\boldsymbol a = - \boldsymbol b
$$

{% endtab %}
{% tab 반대방향벡터 index표기법 %}

$$
a_1 = -b_1,
\ \ \
a_2 = -b_2,
\ \ \
a_3 = -b_3
$$

{% endtab %}
{% tab 반대방향벡터 index표기법과with %}

$$
a_i = -b_i, \text{ with } i=1,2,3
$$

{% endtab %}
{% tab 반대방향벡터 index표기법과with생략 %}

$$
a_i = -b_i
$$

{% endtab %}
{% tab 반대방향벡터 List %}

```python
a=[3,4,5]
b=[0,0,0]
for i in range(len(a)):
	b[i]=-a[i]
```

{% endtab %}
{% tab 반대방향벡터 NumPy %}

```python
a=np.array([3,4,5])
b=-a
```

{% endtab %}
{% endtabs %}

#### 7.2.4.3. 예시: 벡터의 합

{% tabs 벡터합 %}
{% tab 벡터합 굵은기호수식 %}

$$
\boldsymbol c =  \boldsymbol a + \boldsymbol b
$$

{% endtab %}
{% tab 벡터합 index표기법 %}

$$
c_1 = a_1+b_1,
\ \ \
c_2 = a_2+b_2,
\ \ \
c_3 = a_3+b_3
$$

{% endtab %}
{% tab 벡터합 index표기법과with %}

$$
c_i = a_i+b_i, \text{ with } i=1,2,3
$$

{% endtab %}
{% tab 벡터합 index표기법과with생략 %}

$$
c_i =a_i + b_i
$$

{% endtab %}
{% tab 벡터합 List %}

```python
a=[3,4,5]
b=[3,-5,-2]
c=[0,0,0]
for i in range(len(a)):
	c[i]=a[i]+b[i]
```

{% endtab %}
{% tab 벡터합 NumPy %}

```python
a=np.array([3,4,5])
b=np.array([3,-5,-2])
c=a+b
```

{% endtab %}
{% endtabs %}

#### 7.2.4.4. 예시: 벡터의 차

{% tabs 벡터차 %}
{% tab 벡터차 굵은기호수식 %}

$$
\boldsymbol c =  \boldsymbol a - \boldsymbol b
$$

{% endtab %}
{% tab 벡터차 index표기법 %}

$$
c_1 = a_1-b_1,
\ \ \
c_2 = a_2-b_2,
\ \ \
c_3 = a_3-b_3
$$

{% endtab %}
{% tab 벡터차 index표기법과with %}

$$
c_i = a_i-b_i, \text{ with } i=1,2,3
$$

{% endtab %}
{% tab 벡터차 index표기법과with생략 %}

$$
c_i =a_i - b_i
$$

{% endtab %}
{% tab 벡터차 List %}

```python
a=[3,4,5]
b=[3,-5,-2]
c=[0,0,0]
for i in range(len(a)):
	c[i]=a[i]-b[i]
```

{% endtab %}
{% tab 벡터차 NumPy %}

```python
a=np.array([3,4,5])
b=np.array([3,-5,-2])
c=a-b
```

{% endtab %}
{% endtabs %}

#### 7.2.4.5. 내적 (inner dot)

두 벡터간의 '내적'이라 일컫는 연산의 결과는 스칼라가 된다.

$$
\boldsymbol a \cdot \boldsymbol b = \sum_i^3 a_ib_i=c
$$

위를 [Einstein summation convention](https://ko.wikipedia.org/wiki/아인슈타인_표기법)으로 표기하면

$$
\boldsymbol a \cdot \boldsymbol b = a_ib_i=c
$$

Einstein 표기법에 따르면, 앞서 $\text{ with } i=1,2,3 $가 생략되었듯, summation 기호 $$\sum_i^3$$가 생략되어 표기된다. 정리하자면, 두 벡터간의 내적에서 '곱'이 나타난 경우, 곱셈의 대상이 되는 두 물리량의 인덱스가 동일하게 표기된다 (위 에서는 $i$). 중복된 인덱스 $i$가 나타나면 summation기호가 같이 표현되므로, 중복된 인덱스가 나타날 때, 필연적으로 summation이 수행됨을 예상할 수 있다. 이러한 생각이 summation기호를 생략하는데 이르게 된다.
{% tabs 내적 %}
{% tab 내적 List1 %}

```python
## Numpy없이 구현
a=[1,2,3]
b=[4,5,6]
c=0.
for i in range(3):
   c=c+a[i]*b[i]
print(c)
```

{% endtab %}
{% tab 내적 List2 %}

```python
## Numpy없이 구현
a=[1,2,3,5,2,1]
b=[4,5,6,3,4,1]
c=0.
for i in range(len(a)):
   c=c+a[i]*b[i]
print(c)
```

{% endtab %}
{% tab 내적 Numpy %}

```python
import numpy as np
## Numpy로 구현
a=np.array([1,2,3])
b=np.array([4,5,6])
c=a*b  ## element-wise operation되는 것을 유념하라.
		## 즉 c=np.array([a[0]*b[0],a[1]*b[1],a[2]*b[2]])
c=c.sum()
print(c)

#혹은 마지막 두 줄을 줄여서 아래와 같은 한줄의 명령어로 바꿀 수 있겠다.
c=(a*b).sum()
print(c)
```

{% endtab %}
{% tab 내적 np.einsum %}

```python
import numpy as np
## Numpy로 구현
a=np.array([1,2,3])
b=np.array([4,5,6])
np.einsum('i,i->',a,b)
```

{% endtab %}
{% tab 내적 etc %}

```python
import numpy as np
## Numpy로 구현
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.einsum('i,i->',a,b))
print(a@b)
print(np.dot(a,b))
print(np.inner(a,b))
print(np.sum(a*b))
```

{% endtab %}
{% endtabs %}

#### 7.2.4.6. (nxn)행렬과 (n)벡터 곱

행과 열이 각각 n인 행렬과 (즉 nxn행렬)과 n성분으로 구성된 벡터간의 곱

$$
\boldsymbol c = \boldsymbol A \cdot \boldsymbol v
$$

이 index를 활용해 다음과 같이 표기된다.

$$
c_i = \sum_j^nA_{ij}v_j \ \text{ for } i=1,2,...,n
$$

위 결과를 정리하자면 아래와 같다.

{% tabs 행렬벡터곱 %}
{% tab 행렬벡터곱 einstein %}

$$
c_i=A_{ij}v_j
$$

{% endtab %}

{% tab 행렬벡터곱 List활용코드 %}

```python
A=[[2,1],[3,1]]
v=[3,1]
n=2 # 2x2 행렬과 (2)차원 벡터라 가정하자면
c=[0,0,0]
for i in range(n): # 각 c[i]성분의 초기값을 0으로.
   c[i]=0.
   for j in range(n): # 생략된 summation 기호에 해당하는 loop
      c[i]=c[i]+A[i][j]*v[j]
print(c)
```

{% endtab %}
{% tab 행렬벡터곱 NumPy1 %}

```python
A=np.array([[2,1],[3,1]])
v=np.array([3,1])
n=2 # 2x2 행렬과 (2)차원 벡터라 가정하자면
c=np.array([0,0,0])
for i in range(n): # 각 c[i]성분의 초기값을 0으로.
   c[i]=0.
   for j in range(n): # 생략된 summation 기호에 해당하는 loop
      c[i]=c[i]+A[i,j]*v[j]
print(c)
```

{% endtab %}
{% tab 행렬벡터곱 NumPy2 %}

```python
A=np.array([[2,1],[3,1]])
v=np.array([3,1])
c=A@v
print(c)
```

{% endtab %}
{% tab 행렬벡터곱 np.einsum %}

```python
A=np.array([[2,1],[3,1]])
v=np.array([3,1])
c=np.einsum('ij,j->i',A,v)
print(c)
```

{% endtab %}
{% endtabs %}

#### 7.2.4.7. 행렬 곱1 (single dot)

두 행렬 $\boldsymbol A$와 $\boldsymbol B$의 곱이 아래와 같이 정의된다고 하자.

$$
C_{ij} = \sum_k^3 A_{ik}B_{kj} \text{ for } (i,j) \text{ of } (1,1), (1,2), ... , (n,n-1), (n,n)
$$

아래 결과로 정리된다.

{% tabs 행렬곱1 %}
{% tab 행렬곱1 LIST %}

```python
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[3,2,1],[6,5,4],[9,8,7]]
C=[]
for i in range(3): # C행렬의 각 행을 초기화
C.append([])
for j in range(3): # C형렬 각 행에서의 j렬의 초기값에 0 대입
	C[i].append(0)
	for k in range(3): # sum_k^3에 해당하는 summation!
	C[i][j]+=A[i][k]*B[k][j]
```

{% endtab %}
{% tab 행렬곱1 NUMPY1 %}

```python
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
C=np.zeros((3,3)) ## 처음부터 0으로만 가득찬 3x3행렬 초기화
for i in range(3):
	for j in range(3):
		for k in range(3):
			## Nested-list와 달리 ',' 콤마 기호로
			## 각 축의 index를 구분한다.
			C[i,j]+=A[i,k]*B[k,j]
print(C)
```

{% endtab %}
{% tab 행렬곱1 NUMPY2 %}

```python
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
# 혹은 dot 활용하여
C=np.dot(A,B)
print(C)
```

{% endtab %}
{% tab 행렬곱1 NUMPY3 %}

```python
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
# 혹은 더 줄여서 (python 3.5이상)
C=A@B # dtype 이 float로 바뀜
print(C)
```

{% endtab %}
{% tab 행렬곱1 NUMPY4 %}

```python
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
np.einsum('ik,kj->ij',A,B)
```

{% endtab %}
{% endtabs %}

#### 7.2.4.8. 행렬 곱2 (double dot)

$$
c=\boldsymbol A : \boldsymbol B
$$

$$
\rightarrow c=\sum_i\sum_jA_{ij}B_{ij}=\sum_j\sum_iA_{ij}B_{ij}=\sum_j\sum_iB_{ij}A_{ij}=\sum_i\sum_jB_{ij}A_{ij}
$$

파이썬 코드로 바꾸면...

```python
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[3,2,1],[6,5,4],[9,8,7]]
## 1
c=0.
for i in range(3): # i is outer
  for j in range(3): # j is inner
	  c+=A[i][j]*B[i][j]
print(c)
## 2, 안/바깥 for-loop 바뀜.
c=0.
for j in range(3): # j is outer
  for i in range(3): # i is inner
    c+=A[i][j]*B[i][j]
print(c)
## 3. 안/바깥 for-loop 바뀜, 그리고 A와 B의 순서 바뀜
c=0.
for j in range(3): # j is outer
  for i in range(3): # i is inner
    c+=B[i][j]*A[i][j] # A[i][j] x B[i][j] 혹은 B[i][j] x A[i][j]
print(c)
## 4. A와 B의 순서 바뀜
c=0.
for i in range(3): # i is outer
  for j in range(3): # j is inner
    c+=B[i][j]*A[i][j] # A[i][j] x B[i][j] 혹은 B[i][j] x A[i][j]
print(c)
```

`NumPy`를 활용해서 표현해보자. 아래 두 경우중에 더욱 마음에 드는 스타일이 있는가? 교수자는 개인적으로 후자의 스타일이 더 간략하면서도 직관적이라 마음에 든다.

```python
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
##
c=0.
for i in range(3): # i is outer
  for j in range(3): # j is inner
    c+=A[i,j]*B[i,j]
```


```python
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
c=np.einsum('ij,ij->',A,B)
```
.

#### 7.2.4.9. 6.2.1.12 np.einsum 활용
- 10 x 3 x 12 행렬 $\boldsymbol A$와 12 x 3 x 8 행렬 $\boldsymbol B$의 곱의 결과가 10 x 8 행렬 $\boldsymbol C$고 아래와 같이 수행된다고 하자.
$$ C_{ij}=\sum_{k=1}^3\sum_{l=1}^{12}A_{ikl}B_{lkj}$$

{% tabs 행렬곱3차 %}
{% tab 행렬곱3차 질문 %}
Python으로 코드를 작성한 후, 예시로 제시된 정답과 비교해보자.
{% endtab %}
{% tab 행렬곱3차 정답예시1 %}
```python
C=np.zeros((10,8))
for i in range(10):
  for j in range(8):
    for k in range(3):
      for l in range(12):
        C[i,j]=C[i,j]+A[i,k,l]*B[l,k,j]
```
{% endtab %}
{% tab 행렬곱3차 정답예시2 %}
```python
C=np.einsum('ikl,lkj->ij',A,B)
```
{% endtab %}
{% endtabs %}

행렬의 축이 늘어나면 늘어날 수록, 정답 예시1과 같은 형태의 코드 스타일은 선호되지 않을 것이다. 여러 인공지능 기술에서 매우 차원이 높은 다수의 행렬들간의 복잡한 연산이 요구된다. 그럴 경우, Einstein summation 기법을 익히고 간략히 표현할 수 있을수록 유리할 것이다.


<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

---

# 8. Week6
- NumPy 03, Eigenvalue, ANN

## 8.1. 수업 06-1 (Eigenvalue)

### 8.1.1. 개념

- 고유값(eigen value): 행렬(특히 선형변환)을 적용했을 때, 크기만 변하고 방향은 변하지 않는 벡터의 크기 변화 비율.

- 고유벡터(eigen vector): 그 “변하지 않는 방향”을 가지는 벡터.

- 수식:

  $$
  \boldsymbol A\cdot \boldsymbol v = \lambda \boldsymbol v
  $$

  를 만족시키는 스칼라 $$\lambda$$ 값을 고유값이라 한다.
  위 관계를 만족시키는 고유값 세개가 각각 $$\lambda_1,\lambda_2,\lambda_3$$라면
  $$\lambda_1\boldsymbol{v},\lambda_2\boldsymbol{v},\lambda_3\boldsymbol{v}$$
  를 고유 벡터라 한다.

### 8.1.2. 선형 변환(linear transformation; linear map)

#### 8.1.2.1. 선형변환 조건

- 행렬과 벡터의 곱을, 벡터 맵핑으로 해석할 수 있다.

<p align="center">
  <img src=https://upload.wikimedia.org/wikipedia/commons/4/43/Streckung_eines_Vektors.gif />
</p>


- 아래와 같은 두 조건을 만족시키는 행렬 $$\boldsymbol A$$를 선형변환 행렬이라 한다.

  $$
  \boldsymbol A\cdot (\boldsymbol a+\boldsymbol b)
  = \boldsymbol A\cdot \boldsymbol a+ \boldsymbol A\cdot \boldsymbol b
  $$

  $$
  \boldsymbol A\cdot (\lambda\boldsymbol a)=\lambda A\cdot\boldsymbol a
  $$

<p align="center">
  <img src=https://upload.wikimedia.org/wikipedia/commons/2/25/Streckung_der_Summe_zweier_Vektoren.gif />
</p>

<p align="center">
  <img src=https://upload.wikimedia.org/wikipedia/commons/e/e6/Streckung_homogenitaet_Version_3.gif />
</p>

\*\* [Wikipedia 발췌 이미지](https://en.wikipedia.org/wiki/Linear_map)

#### 8.1.2.2. 선형변환 특성

- 선형변환의 특성을 잘 반영하는 방향을 찾을 수 있다.
- 아래의 행렬은 선형변환을 하며, 그 특성을 대표하는 두 방향을 빨간색으로 나타내었다.

### 8.1.3. 고유값의 기하하적 의미

고유값의 기하학적 의미를 파악해보자. 다음과 같은 행렬의 경우를 살펴보자. 다음의 여러 행렬들에 의한 벡터(점)의 변환을 살펴보자. 그리고 빨간 선과 (표기되어 있다면) 파란 선 위의 점들이 다른 점들과 어떠한 차이가 있는지 눈여겨 살펴보자.

![eigen1](/assets/dat_files/lectures/1_2_data_mse/eigen_1.gif)

![eigen2](/assets/dat_files/lectures/1_2_data_mse/eigen_2.gif)

![eigen2](/assets/dat_files/lectures/1_2_data_mse/eigen_3.gif)

위 세 경우와 달리, 아래 경우는 조금 특별하다. 특성값이 복소수
$$\lambda_1=0.71+0.71i,$$
그리고
$$\lambda_2=0.71-0.71i$$
임을 눈여겨 보자.

![eigen3](/assets/dat_files/lectures/1_2_data_mse/eigen_4.gif)

### 8.1.4. 고유값 (Eigenvalue), 고유벡터 (Eigenvector) 구하기.

- 2차원 예시01

  $$
  \begin{bmatrix}
  A_{11}&A_{12}\\
  A_{21}&A_{22}
  \end{bmatrix}
  \begin{bmatrix}
  v_1\\
  v_2
  8. \end{bmatrix}
  =
  \lambda
  \begin{bmatrix}
  v_1\\
  v_2
  \end{bmatrix}
  $$

  $$
  A_{11}v_1+A_{12}v_2=\lambda v_1\ \ \ \ (1)
  $$

  $$
  A_{21}v_1+A_{22}v_2=\lambda v_2\ \ \ \ (2)
  $$

  (1)식을 고치면,

  $$
  (A_{11}-\lambda)v_1=-A_{12}v_2
  $$

  따라서

  $$
  v_1=\frac{-A_{12}}{A_{11}-\lambda}v_2
  $$

  (2)에 대입하면

  $$
  \frac{-A_{21}A_{12}}{A_{11}-\lambda}v_2+A_{22}v_2=\lambda v_2\ \ \ \ (3)
  $$

  (3)의 $$v_2=0$$인 해는 trivial. 이걸 제외하면,

  $$
  \frac{-A_{21}A_{12}}{A_{11}-\lambda}+A_{22}=\lambda
  $$

  정리하면

  $$
  -A_{21}A_{12}+A_{22}(A_{11}-\lambda)=\lambda(A_{11}-\lambda)
  $$

  위는 $\lambda$에 대한 2차 방정식이며

  $$
  \lambda^2-(A_{11}-A_{22})\lambda-A_{21}A_{12}+A_{22}A_{11}=0
  $$

- 2차원 예시02

  $$
  \boldsymbol A\cdot \boldsymbol v = \lambda \boldsymbol v
  \ \ \
  \rightarrow
  \ \ \
  (\boldsymbol A-\lambda\boldsymbol I)\cdot v=0
  $$

  $$
  \boldsymbol A =
  \begin{bmatrix}
  A_{11}& A_{12}\\
  A_{21}& A_{22}
  \end{bmatrix}
  $$

  그리고

  $$
  \boldsymbol I =
  \begin{bmatrix}
  1& 0\\
  0& 1
  \end{bmatrix}
  $$

  고유값 $\lambda$는 아래와 같이 구해진다.

  $$
  \det(\boldsymbol A-\lambda\boldsymbol I)=0
  $$

  ```python
  import numpy as np
  def eig2x2(A):
    a=A[0,0]
    b=A[0,1]
    c=A[1,0]
    d=A[1,1]
    tr = a + d
    det = a*d - b*c
    disc = tr*tr - 4*det
    lam1 = (tr + np.sqrt(disc)) / 2
    lam2 = (tr - np.sqrt(disc)) / 2
    return lam1, lam2

  A = np.array([[3,2],[2,1]], dtype=float)
  lam1, lam2 = eig2x2(A)
  print("manual:", lam1, lam2)
  print("numpy :", np.linalg.eigvals(A))
  ```

- 예시
  주어진 [파일](/assets/dat_files/lectures/1_2_data_mse/matrix_03.txt)의 매트릭스의 값들을 활용해서 각 파일에서 고유값들을 구해서
  출력하시오.

  ```python
  import numpy as np
  def eig2x2(A):
    a=A[0,0]
    b=A[0,1]
    c=A[1,0]
    d=A[1,1]
    tr = a + d
    det = a*d - b*c
    disc = tr*tr - 4*det
    lam1 = (tr + np.sqrt(disc)) / 2
    lam2 = (tr - np.sqrt(disc)) / 2
    return lam1, lam2
  d=np.loadtxt('../data/matrix_03.txt',skiprows=1)
  for i, mat2x2 in enumerate(d):
    mat=mat2x2.reshape(2,2)
    print(eig2x2(mat)) ## nan 은 어던 경우인가?
  ```

- `np.ling.eigen`활용 소개

- 변형률

역학에서 변위구배텐서(displacement gradient tensor) $\boldsymbol u$라는 물리량을 활용해, 변형 전 후의 위치변화를 다음과 같이 위치를 나타내는 벡터 변환으로 나타낸다.

$$
\boldsymbol v^{new}=\boldsymbol u \cdot \boldsymbol v^{old}
$$

이때, 변위구배텐서의 eigen value를 활용해 변형의 `량`을 가늠해볼 수 있다. 2차원 변위구배텐서의 특성값을 각각 $\lambda_1, \lambda_2$라 한다면, 경우에 따라 (회전이 거의 없다면) $\lambda_1-1$과 $\lambda_2-1$은 꽤 괜찮은 변형의 정도를 나타내는 지표가 될 수 있다. 여기서 1을 빼는 이유는 무엇일까?

- 예시 Human vs. Zombie [ref](https://www.youtube.com/watch?v=i8FukKfMKCI)

신분제가 공고하던 조선 시대에서도 [양반](https://en.wikipedia.org/wiki/Yangban)과 [노비](https://en.wikipedia.org/wiki/Nobi) 계층간의 변화가 일어나곤 했다 ([참고](https://product.kyobobook.co.kr/detail/S000001197638)). 매우 불안정했던 가상의 조선시대에 매년 역적으로 몰린 양반의 20%가 노비가 되고, 노비 중 10%가 큰 부를 쌓아 양반으로 신분상승을 했다고 가정하자.

```mermaid
stateDiagram-v2

Yangban(YB) --> Nobi(NB) : 20%
Nobi(NB) --> Yangban(YB): 10%
```
해가 거듭 될 수록 달라지는 양반(YB)과 노비(NB)의 상관 관계를 수식으로 표현하자면 아래와 같다.
$$
YB_{(n+1)} = 0.80 YB_{(n)} + 0.10 NB_{(n)}
$$
$$
NB_{(n+1)} = 0.20 YB_{(n)} + 0.90 NB_{(n)}
$$
여기서 첨자 $_{n}$과 $_{n+1}$은 각각 직전 해, 그리고 다음해에 해당하는 노비와 양반을 가리킨다. 위 연립 방정식을 아래와 같이 행렬식으로 나타낼 수 있겠다.
$$
\begin{bmatrix}
YB_{(n+1)} \\
NB_{(n+1)}
9. \end{bmatrix}
=
\begin{bmatrix}
  0.90& 0.01 \\
  0.02& 0.95
 \end{bmatrix}

\begin{bmatrix}
YB_{(n)} \\
NB_{(n)}
\end{bmatrix}
$$

예들 들어, 양반과 노비의 인구수가 첫해($n=0$)에 8명 vs 2명 이었다고 가정하자. 그 다음해에는
$$
\begin{bmatrix}
YB_{(1)} \\
NB_{(1)}
10. \end{bmatrix}
=
\begin{bmatrix}
  0.8& 0.1 \\
  0.2& 0.90
 \end{bmatrix}

\begin{bmatrix}
8 \\
2
11. \end{bmatrix}
=
\begin{bmatrix}
6.60 \\
3.40
\end{bmatrix}
$$
그리고 그 다음에는
$$
\begin{bmatrix}
YB_{(2)} \\
NB_{(2)}
12. \end{bmatrix}
=
\begin{bmatrix}
  0.8& 0.1 \\
  0.2& 0.90
 \end{bmatrix}

\begin{bmatrix}
6.60 \\
3.40
13. \end{bmatrix}
=
\begin{bmatrix}
5.62 \\
4.38
\end{bmatrix}
$$

이렇게 차례로 시간이 더욱 지나고 나면 3.34, 6.66으로 수렴된다. 하지만 초기 세팅이 8대2가 아니라 8대 4였다면 4대 8로 바뀌게 된다. 위 경우를 포함해 양반대 노비의 비율이 각기 다를경우에도 시간이 충분히 지나면, 규칙성 있게 바뀌게 된다.
![NBYB](/assets/dat_files/lectures/1_2_data_mse/nobiyangban.gif)

다음 몇몇 선형변환 매트리스와 그에 해당하는 Eigenvector와 Eigenvalue가 보여주는 변화를 살펴보자
![egenflow1](/assets/dat_files/lectures/1_2_data_mse/eigen_flow1.gif)
![egenflow2](/assets/dat_files/lectures/1_2_data_mse/eigen_flow2.gif)
![egenflow3](/assets/dat_files/lectures/1_2_data_mse/eigen_flow3.gif)
![egenflow3](/assets/dat_files/lectures/1_2_data_mse/eigen_flow4.gif)


- 구글(Google)의 Page ranking system: [ref](https://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html)
<!--

```typograms
                                                        ----0.3--+
                                                        |        |
                                                        V        |
+-----------------+                    +---------------------+   |
| www.daum.net    | ------ 0.2 ---   | www.naver.com       |---+
|                 | <----- 0.3 -----   |                     |
+-----------------+                    +---------------------+
     ^     |        \                     ^           |
     |     |         \                    |           |
    0.2    0.3        \                   0.15        0.3
     |     |           \                  |           |
     |     v            0.2               |           v
+-----------------+       \           +-------------------+
|                 |        \          |                   |
| www.youtube.com |         +------ |    google.com     |
|                 |<-------0.7--------|                   |
|                 |--------0.05-----|                   |
+-----------------+                   +-------------------+
```

$$
\begin{bmatrix}
daum \\
naver \\
youtube \\
google  \\
\end{bmatrix}
=
\begin{bmatrix}
0 & 0.3  & 0.2 & 0 \\
0.2 & 0.3 & 0 & 0.15\\
0.3 & 0 & 0 & 0.7 \\
0.2 & 0.3 & 0 & 0.05
\end{bmatrix}
\begin{bmatrix}
daum \\
naver \\
youtube \\
google  \\
\end{bmatrix}
$$

-->

------------------------------
## 8.2. 수업 06-2 (ANN, Activation)

- 인공 신경망 (Artificial Neural Network)

  - [인공 신경망](https://ko.wikipedia.org/wiki/신경망)
    ([neutral network](<https://en.wikipedia.org/wiki/Neural_network_(machine_learning)>))에 쓰이는
    일반적인 [인공뉴런](https://ko.wikipedia.org/wiki/인공_뉴런)
    ([artificial neuron](https://en.wikipedia.org/wiki/Artificial_neuron))은 다음 형태를 가지는 경우가 많다.
  - 신경망

- Basic structure of Artificial Neural Network

  - 행렬곱과 더하기 조합. 아래 수식은 실제로 Artifical Neutral Network(ANN)에서 널리 활용되는 형태의 연산이다.

    $$
    \boldsymbol y=\boldsymbol W\cdot \boldsymbol x + \boldsymbol b
    $$

    $$
    y_i=\bigg(\sum_j^mW_{ij}x_j\bigg)+b_i=W_{ij}x_j+b_i \text{ with } i=1,2, ..., n
    $$

    ```python
    W=np.array([[1,2,3,4],[5,6,7,8]]) ## 2x4 행렬 (with n and m beging 2 and 4, respectively)
    x=np.array([5.5,0.1,0.3,1.0])     ## 4 (nested 가 아님. 1차원 임에 유의)
    b=np.array([-0.5,+0.5])

    n=2
    m=4
    y=np.zeros(n) # 주의 정수 n은 2이다.

    for i in range(n): ## i=1,2,...,n
    for j in range(m):
      y[i]+=W[i,j]*x[j]+b[i]
    print(y)
    ## 위 표현은 틀렸다.
    ## 올바른 표현의 예는 아래와 같다. 무엇이 고쳐졌는가?
    n=2
    m=4
    y=np.zeros(n)
    for i in range(n): ## i=1,2,...,n
    y[i]+=b[i]
    for j in range(m):
      y[i]+=W[i,j]*x[j]
    ## summation_j^m가 어디까지의 term에 적용되는지 정확히 알아야 함.
    print(y)
    ```

  - 예시

  `W[n,m]`행렬과 `x[m]`벡터, 그리고 `b[n]`벡터로 구성된
  배열을 활용해 위 수식

  $$\boldsymbol v=\boldsymbol W\cdot \boldsymbol x + \boldsymbol b$$

  을 계산하여 리턴하는 함수를 만드시오.

  ```python
  def neuron(w,x,b):
  	  """
  	  Arguments
  	  ---------
  	  W: ndarray
  	   [m x n] matrix (weight)
  	  b: ndarray
  	   [n] vector (bias)

  	  Returns
  	  -------
  	  W.x + b
  	  """
  	  n,m=w.shape() # tuple
  	  y=np.zeros(n)
  	  for i in range(n):
  		y[i]+=b[i]
  		for j in range(m):
  		  y[i]+=w[i,j]*x[j]
  	  return y
  ```

- Activation

  - [인공 신경망](https://ko.wikipedia.org/wiki/신경망)
    ([neutral network](<https://en.wikipedia.org/wiki/Neural_network_(machine_learning)>))에 쓰이는
    일반적인 [인공뉴런](https://ko.wikipedia.org/wiki/인공_뉴런)
    ([artificial neuron](https://en.wikipedia.org/wiki/Artificial_neuron))은 다음 형태를 가지는 경우가 많다.

    $$
    y_k=\phi\bigg(\sum_{j}^mw_{kj}x_j+b_k\bigg)
    $$

    이 때 $$\phi$$는 activation function이라 불리며 다양한 형태가 사용되고 있다.
    우리는 이를 element-wise로 적용되는 함수라 보자.

  - Activation function

    - Binary step

    $$
    \phi(x_i)=0 \text{ if } x_i<0
    \newline
    \phi(x_i)=1 \text{ if } x_i\geq0
    $$

    ```python
    def act_func_binary(x):
      """
      Binary function as the activation function for neuron
      """
      flg=x>=0
      y=np.zeros(x.shape)
      y[flg]=1.
      return y
    ```

    - 예시 (Logistic function)

    $$
    \phi(x_i)=\frac{1}{1+e^{-x_i}}
    $$

    - 예시: Rectified linear unit (ReLU)

    $$
    \phi(x_i)=\frac{x+|x|}{2}
    $$

# 9. Week7
- 중간고사

## 9.1. 수업 07-1

- 목표
  - 복습, 출제 방향 설명

## 9.2. 수업 07-2

# 10. Week8
- Matplotlib 01

- 목표
  - axes, figure 를 만들 수 있다.
  - 선(line), 점(dot)으로 이루어진 그래프를 그릴 수 있다.
  - x축, y축의 label, tick, limits을 만들 수 있다.
  - linear scale, logscale을 만들고 이해할 수 있다.
  - 3차원 그래프를 그릴 수 있다.
  - 파일로부터 데이터를 불러오고, 이를 graph로 바꿀 수 있다.

## 10.1. 수업 08-1

[Matplotlib](https://matplotlib.org): Python 환경에서 데이터를 시각화하는데 가장 널리 쓰이는 라이브러리 중에 하나이다. MATLAB과 유사한 환경을 제공해주는 pyplot 모듈을 활용한 인터페이스가 널리쓰인다. 아래 예시들을 함께 살펴보자.
```python
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)          # 선 그래프
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
```

- scatter plot

```python
x = [5, 7, 8, 7, 6, 9, 5, 4, 5, 6]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
plt.scatter(x, y, color='red')
plt.title("Scatter Plot")
```

각 데이터 세트 (선, 점 등)에 라벨을 부여하고, 이를 레전드(```legend```) 함수를 활용해 그래프를 꾸밀 수 있다.

```python
plt.plot([1,2,3],[1,4,9], label=r'$y = x^2$')
plt.plot([1,2,3],[1,2,3], label=r'$y = x$')
plt.legend() ## legend
```

```plt.subplot```을 활용해서 행렬 행태의 그래프 모임을 그릴 수 있다.

```python
plt.subplot(1, 2, 1)  # 1행 2열 중 첫 번째
plt.plot([1,2,3],[1,4,9])
plt.title("Left")

plt.subplot(1, 2, 2)  # 두 번째
plt.plot([1,2,3],[1,2,3])
plt.title("Right")
```

```plt```환경을 조금 더 상세히 살펴보면, 두개의 오브젝트 ```figure```와 ```axis```를 이해할 수 있다. ```figure```는 그림을 그리는 캔버스, ```axis```는 그래프가 시각화되는 좌표계라 볼 수 있다.

- Figure: 그래프 전체 "캔버스"
- Axes: 실제 데이터가 그려지는 "좌표 영역"

따라서 한 Figure 안에 여러 개의 axes가 삽입될 수 있다. 아래 예제를 살펴보자.

```python
import matplotlib.pyplot as plt

# Figure(도화지), Axes(좌표 영역) 생성
fig, ax = plt.subplots()

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# ax 객체를 활용해 데이터 플롯
ax.plot(x, y, label="y = x^2", color="blue")

# 그래프 꾸미기
ax.set_title("Figure & Axes Example")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
ax.grid(True)

plt.show()
```

NumPy의 ```linspace```, ```logspace```등과 결합하면 여러 1D 그래프를 손쉽게 그릴 수 있다. 예를 들어 $y=x^2$을 $x\in[-10,10]$을 그리자면

```python
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10) # [-10,10] 범위내의 50 포인트
y=x**2 ## NumPy의 element-wise operation을 기억하자.
plt.plot(x,y)
```
결과를 살펴보자.

위 예제를 응용하여 아래 실습을 수행해보자. 범위 내의 아래 삼각함수를 그려보자.

예1.

$$
y=\cos(\theta), \text{ with } \theta\in[-\pi,\pi]
$$

예2.

$$
y=\sin(\theta), \text{ with } \theta\in[-\pi,\pi]
$$

예3.
$$
y=\tan(\theta), \text{ with } \theta\in\big[-\frac{\pi}{2},\frac{\pi}{2}\big]
$$

- 반지름의 길이가 10인 원을 그려보자.

$$
x^2+y^2=10^2
$$

- 길이 변화에 따라서 나타나는 공칭 변형률과 진형병률 그래프 관계를 그리고 이를 비교해보자.

$$
\varepsilon=\ln(\epsilon+1)
$$

- Stress vs. strain curve 그리기
다음 [압축파일](/assets/dat_files/lectures/1_2_data_mse/tensile_test_results.zip)을 풀어서, 파일 하나를
살펴보자 - 예를 들어 `00_DD_WZ_01.csv`
위 데이터 파일을 활용해
1.  폭: 6.04 mm, 두께 2.99 mm 인걸 확인하고,
2.  힘과 변위 칼럼을 활용해서 응력과 변형률을 구하자.
3.  그 다음 응력과 변형률 곡선을 Figure로 그려보자.


- 임의의 3차원 벡터 생성과 stereographic projection.

cubic crystal structure내의 결정 방위 [h,k,l]에 해당하는 단위 벡터를 그려보자. Cubic crystal의 경우 Miller index $[uvw]$가 한 결정 방향이라면 그 방향에 해당하는 벡터 $\boldsymbol b$는 아래와 같이 구할 수 있다.
$$
\boldsymbol b = (b_1,b_2,b_3)=\bigg(\frac{h}{\sqrt{h^2+k^2+l^2}},\frac{h}{\sqrt{h^2+k^2+l^2}},\frac{h}{\sqrt{h^2+k^2+l^2}}\bigg)
$$
이를 계산하는 함수를 작성해보면
```python
def get_direct(uvw=np.array([1,1,0])):
  """
  Argument
  --------
  uvw: as in <ndarray> or <list>

  Return
  ------
  """
  ##
  if type(uvw).__name__=='list':
    uvw=np.array(uvw)

  deno=(uvw**2).sum() # demoniator: 분모, numerator: 분자
  deno=np.sqrt(deno)
  return uvw/deno

## 테스트 해보자.
get_direct([1,1,0])
get_direct([1,1,1])
```

꼭 List 타입으로 주는 방식이 싫다면 아래와 같은 형태도 괜찮은 대안이 될 수 있겠다.
```python
def get_direct(v1,v2,v3):
  """
  Argument
  --------
  v1,v2,v3

  Return
  ------
  """
  ##
  uvw=np.array([v1,v2,v3])
  deno=(uvw**2).sum() # demoniator: 분모, numerator: 분자
  deno=np.sqrt(deno)
  return uvw/deno
```

위 함수를 활용해 결정학적으로 같이 $[100],[010],[001],[\bar{1}00],[0\bar{1}0],[00\bar{1}]$을 3차원 그래프로 표현해보자. 3차원 점들을 표현하기 위해서는 3차원 axis가 필요하다. 이를 위해서 fig의 add_subplot 매소드에 'projection=3d' 파라미터를 입력하여 3차원 axis를 만들자. 그 다음, 앞서 생성한 점들을 'scatter'함수를 활용해 아래와 같이 표현해보자.
```python
%matplotlib widget
fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')
vs=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
for i, v in enumerate(vs):
    uvw=get_direct2(*v)
    ax1.scatter(*uvw,marker='o',color='k')
```

3차원 공간인지 사실 한눈에 살펴보기 어렵다. 따라서, 원점(0,0,0)에서부터 각 지점까지 화살표로 이어보는게 더 좋겠다. 화살표를 그리기 위해서 [```quiver```](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html)매소드를 활용하였다.
```python
%matplotlib widget
import matplotlib.pyplot as plt
fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')
vs=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
orig=[0,0,0]
for i, v in enumerate(vs):
    uvw=get_direct2(*v)
    ax1.scatter(*uvw,marker='o',color='k')
    ax1.quiver(*orig,*uvw,arrow_length_ratio=0.2,color='r')
```

3차원 방향을 좀 더 명확히 살펴보기 위해, 반지름 1인 구(sphere)를 같이 그려보면 좋겠다. 이를 위해서는 [구면 좌표계(spherical coordinate system)](https://ko.wikipedia.org/wiki/구면좌표계)를 활용하면 더욱 쉽게 구를 그릴 수 있다. $(r,\theta,\phi)$의 좌표계에서 $r=1$로 고정하면, 반지름이 1인 구의 면에 해당한다. 아래 범위 내의 경우를 활용하면 되겠다.
- $\theta=[0,\pi]$
- $\phi=[0,2\pi]$

주어진 구 좌표계는 다음과 같이 직교 좌표계 $(x,y,z)$로 아래와 같이 변환된다.

- $x=r\times \sin\theta\cos\phi$
- $y=r\times \sin\theta\sin\phi$
- $z=r\cos\theta$

[```np.mgrid```](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html)기능을 활용하면 쉽게 그리드를 만들 수 있다. np.linspace와 유사하나, 다차원으로 확장가능하며, grid를 만들기에 적합하다.

```python
import numpy as np
theta,phi=np.mgrid[0:np.pi:10j,0:2*np.pi:10j]
```
위에 만들어진 theta와 phi를 직교좌표계로 바꾸면
```python
import numpy as np
theta,phi=np.mgrid[0:np.pi:10j,0:2*np.pi:10j]
r=1 # radius가 1이다.
## 직교 좌표계로 아래와 같이 변환할 수 있다.
x=r*np.sin(theta)*np.cos(phi)
y=r*np.sin(theta)*np.sin(phi)
z=r*np.cos(theta)
```

이제 grid된 x,y,z좌표와 matplotlib의 plot_wireframe을 활용해서 3D 구면을 그려보자.

```python
import numpy as np
theta,phi=np.mgrid[0:np.pi:10j,0:2*np.pi:10j]
r=1 # radius가 1이다.
## 직교 좌표계로 아래와 같이 변환할 수 있다.
x=r*np.sin(theta)*np.cos(phi)
y=r*np.sin(theta)*np.sin(phi)
z=r*np.cos(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x,y,z,alpha=0.2,lw=0.9) ## alpha: 투명도, lw: linewidth
```

나아가, 그 위에 앞서 구한 결정방향들을 올려보자.

```python
import numpy as np
theta,phi=np.mgrid[0:np.pi:20j,0:2*np.pi:20j]
r=1 # radius가 1이다.
## 직교 좌표계로 아래와 같이 변환할 수 있다.
x=r*np.sin(theta)*np.cos(phi)
y=r*np.sin(theta)*np.sin(phi)
z=r*np.cos(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x,y,z,alpha=0.2,lw=0.9)

##
vs=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
orig=[0,0,0]
for i, v in enumerate(vs):
    uvw=get_direct2(*v)
    ax.scatter(*uvw,marker='o',color='k')
    ax.quiver(*orig,*v,arrow_length_ratio=0.2,color='r')
```

그런데 사실, 3차원으로 그린 그래프 툴이 개발되기 전에도 많은 재료공학자들이 3차원 정보를 표현해야만 했다. 그들은 3차원 정보를 2차원면에 표현하기 위해 stereographic projection법을 활용하였다.

```python
%matplotlib widget
#%matplotlib inline
fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')
vs=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
orig=[0,0,0]
for i, v in enumerate(vs):
    uvw=get_direct2(*v)
    ## quiver 메소드를 활용하였다.
    ax1.quiver(*orig,*v,arrow_length_ratio=0.2,color='r')

d=1.2
ax1.set_xlim(-d,d)
ax1.set_ylim(-d,d)
ax1.set_zlim(-d,d)
```

## 10.2. Crystal symmetry

## 10.3. 수업 08-2 (~~np.meshgrid~~, np.mgrid, grid, contouring)

# 11. Week9
- Force vs. Disp curve 분석, 최소 자승법
- 목표
  - force vs. displacement 파일로 불러올 수 있다.
  - 응력 변형률로 데이터를 분석하고 이를 진응력 진변형률로 바꿀 수 있다.
  - 최소 자승법을 이해하고 활용할 수 있다.

## 11.1. 수업 09-1 (Force vs. displ 데이터 -> 응력 선도)

- 실습을 위해 필요한 다음 [calibration1](/assets/dat_files/lectures/1_2_data_mse/calibration1.txt),
  [calibration2](/assets/dat_files/lectures/1_2_data_mse/calibration2.txt)
  파일을 다운로드 받자.
- 첫번째 calibration file은 변위 측정 장치에서 측정된 voltage 변화를 mm 단위의 변위로 '변환'해준다.
- 두번째 calibration file은 로드셀 (load)장치에서 측정된 voltage 변화를 kN 단위의 힘으로 '변환'해준다.

  ```python
  import matplotlib.pyplot as plt
  c1=np.loadtxt('calibration1.txt')
  c2=np.loadtxt('calibration2.txt')

  fig=plt.figure()
  ax1=fig.add_subplot(121)
  ax2=fig.add_subplot(122)

  y=c1[:,0] # extension in [mm]
  x=c1[:,1] # voltage
  ## 뒤죽박죽 시행된 calibration sheet의 데이터를 X(voltage)기준으로 정렬하자.
  ind=np.argsort(x)
  y=y[ind]
  x=x[ind]
  # 정렬된 calibration sheet 데이터를 그리자.
  ax1.plot(x,y,'-o',mfc='None',label='Calibration')

  ## let's find out what y=ax+b fits this equation well.
  a1=0.1
  b1=0.1 ## a1 과  b1 을 바꿔가며 calibration 해보자.
  xs=np.linspace(-4,2)
  ys=xs*a1+b1
  ax1.plot(xs,ys,label='fit')
  ax1.legend()

  y=c2[:,0] # force in kN
  x=c2[:,1] # voltage
  # .... 이어 계속해서 프로그래밍 해보자.
  ```

  이렇게 얻어진 데이터를 가지고 폭과 두께, 그리고 gauge length를 안다면
  응력 vs. 변형률 데이터로 변환 가능하다.

- 다음으로, 위에서 구한 힘과 변위를 활용해 응력 vs. 변형률 데이터로 바꿔보자.

  - 폭이 12.695 mm, 두께가 1.193 mm, 게이즈가 20 mm라 가정하자.
  - 공칭 응력

  $$
  \sigma^{engi}=\frac{force}{Area}
  $$

  - 공칭 변형률

  $$
  \epsilon^{engi}=\frac{\Delta l}{l_0}
  $$

  - 진 변형

  $$
  \varepsilon=\ln(1+\epsilon)
  $$

  - 진 응력

  $$
  \sigma^{true}=\sigma^{engi}(1+\epsilon)
  $$

  ```python
  ## algorithm
  # 1. 파일로부터 Numpy를 활용해 데이터를 불러온다.
  # 2. 주어진 시편의 폭과 두께로부터 초기단면적을 구한다.
  # 3. 초기 단면적과 힘을 활용해 공칭 응력을 구한다.
  # 4. 초기 게이지 길이와 변위를 활용해 공칭 변형률을 구한다.
  # 5. 진 변형률을 구한다.
  # 7. 진 응력을 구한다.
  # 8. 진응력 vs. 진 변형률 곡선을 구한다.
  # 9. 최대 하중 이후의 데이터를 trimming 해본다.
  ```

- Hollomon Equation으로 바꿔본다.

$$
\sigma=k\varepsilon^n
$$

적절한 k값과 n값을 앞서 calibration sheet의 $ a$ 그리고 $ b $에 해당하는 값을 찾기 위해서는
$\log$ 함수의 활용이 유용하다.

$$
\log\sigma=\log k + n\log \varepsilon
$$

밑(base)이 자연수(2.713...)인 로그 함수를 활용한다면

$$
ln\sigma=\ln{k}+n\ln\varepsilon
$$

이를 활용해 적절한 $k$ 값 및 $n$ 값을 구해보자.

```python
# np.log 함수를 활용해 밑이 자연수인 로그 함수를 활용하자.
# np.log(sigma), np.log(epsilon)
# plt.plot 활용해 직선 그려보기
# a값 그리고 b값 찾기.
# log (a) 그리고 log (b)로부터 a, b값을 역산(거꾸로 계산) 해보자.
```

- 복잡한 형태의 데이터 파일의 경우를 생각해보자.
  이미 calibration된 이후 얻어진 [힘/변위 데이터](/assets/dat_files/lectures/1_2_data_mse/force_vs_displ.txt)를
  살펴보고, 분석해보자.

  ```python
  np.loadtxt('filename') # 이 명령어가 적용되지 않는 여러 이유가 있다. 그 이유를 파일을 직접 살펴보고 고민해보자.
  #with open(fn,'r') as fo:
  #    cnt=fo.read()
  #    blocks=cnt.split('Data Acquisition')
  #    blocks=blocks[1:]

  #for ib,block in enumerate(blocks):
  #    lines=block.split('\n')
  #    lines=lines[3:-2] ##??
  #    bl=''
  #    dmaster=np.zeros((len(lines),4),dtype='float')
  #    for i, line in enumerate(lines):
  #        dmaster[i,:]=np.array(line.split('\t'),dtype='float')

  #    plt.plot(dmaster[:,1],dmaster[:,2])
  ```

## 11.2. 수업 09-2 (노이즈가 있는 데이터로부터 최소자승법을 활용한 선형회귀)

- 목표

  - 최소 자승법을 이해한다.
  - 09-1의 데이터의 활용헤서 '최소자승법'을 활용해본다.

- 개념

  - 주어진$$n$$ 쌍의의 데이터가 아래와 같이 표현될 수 있다.

  $$
  (x_i,y_i) \text{ with } i=1,2,...,n
  $$

  이때 위 $$n$$쌍의 데이터를 우리가 구하는 직선의 방정식이 매우 잘 대표해야 하겠다.

  $$
  y=ax+b
  $$

  그러한 직선의 방정식을 구하기 위해서는 데이터와 계산된 값 사이의 차이를 최소화시켜야겠다.

  - 예시.

    - 실제로는 2.5x + 5가 데이터인데, 가상의 노이즈를 부과해보자.

      ```python
      import numpy as np
      import matplotlib.pyplot as plt

      # example data with noise
      xs = np.linspace(0, 10, 20)
      # 실제로는 2.5x + 5가 데이터인데, 가상의 노이즈를 부과해보자.
      a=2.5
      b=5
      y_true = a * xs + b
      ## 정규 분포를 따르는 인위적 노이즈를 부과해보자.
      noise = np.random.normal(0, 3, size=xs.shape) ## 정규분포 mean:0, std: 3
      ys = y_true + noise
      ```

    - 그 다음, 정확한 $a, b$ 값을 모른다 가정하고, 각 추측된 값
      $\tilde a,\tilde b$ 값을 사용해보자. 그리고 추측된 값과, 노이즈가 있는 값
      들 사이에 차이를 아래와 같이 정의하여 살펴보자.

      $$
      \epsilon_i=y_i-(\tilde a x_i+\tilde b)
      $$

    - 각 쌍

      $$
      (x_i,y_i)
      $$

      에 따라 음의 차이 혹은 양의 차이가 있을 수 있으므로, 자승(square)값을 구하고
      그 자승 값의 총 합을 살펴보자. 즉

      $$
      \sum_i^n(\epsilon_i)^2
      $$

      값을 찾아 보자.

    - 여기까지의 과정은 아래와 같이 Python으로 구현될 수 있다.

      ```python
      plt.plot(xs,ys,'rx',label='Data with noise')
      #plt.plot(xs,y_true,'k-',label='True data')

      tilde_a=2.2
      tilde_b=5
      plt.plot(xs,tilde_a*xs+tilde_b,'m--',label='Guessed fit')
      epsilon=np.zeros(xs.shape)
      for i, x in enumerate(xs):
      	y=x*tilde_a+tilde_b
      	epsilon[i]=y-ys[i]
      	plt.plot([x,x],[ys[i],y],'-b')
      print(f'residual: {(epsilon**2).sum()}')
      leg=plt.legend()
      ```

    - 이제 자승값의 합을 최소화 시키는 $\tilde a, \tilde b$ 값을 어떻게
      구할 수 있을지 고민해보자.

    - 가장 적절한 $\tilde a, \tilde b$ 값을 구하기 위해 우선

      $$
      S=\sum_i^n(\epsilon_i)^2
      $$

      라 하고, 이를 풀어서 표현하면

      $$
      S=\sum_i^n(\epsilon_i)^2=\sum_i^n(y_i-(\tilde ax_i+\tilde b))^2
      $$

      가 된다. 위 표현은 위 코드 박스에서

      ```python
      (epsilon**2).sum()
      ```

      에 해당한다.

      제곱 항을 전개하면

      $$
      S=\sum_i^n(y_i-(\tilde ax_i+\tilde b))^2
      =\sum_i^n\bigg(y_i^2+(\tilde ax_i-2y_i(\tilde ax_i+\tilde b)+\tilde b)^2\bigg)
      $$

      가 된다. 이때

      $$
      \frac{\partial S}{\partial \tilde a}=0
      $$

      그리고

      $$
      \frac{\partial S}{\partial \tilde b}=0
      $$

      를 만족하는 $\tilde a, \tilde b$ 값이 최소자승법에 의해 구해진다.
      따라서 각 미분 값을 구해보면

      $$
      \frac{\partial S}{\partial \tilde a}
      =\sum_i^n\frac{\partial \bigg((y_i-(\tilde ax_i+\tilde b))^2\bigg) }{\partial \tilde a}
      =\sum_i^n{\bigg(2(y_i-(\tilde ax_i+\tilde b))(-x_i)\bigg)}
      $$

      위 미분값이 0이 되는 조건을 더욱 정리해보면

      $$
      \frac{\partial S}{\partial \tilde a}
      =-2\sum_i^n{\bigg((x_iy_i-\tilde ax_ix_i-\tilde bx_i)\bigg)}=0
      $$

      따라서

      $$
      \frac{\partial S}{\partial \tilde a}
      =-2\sum_i^n{\bigg((x_iy_i-\tilde ax_i^2-\tilde bx_i)\bigg)}=0
      \newline
      \rightarrow \bigg(\sum_i^nx_iy_i\bigg)-\tilde a\bigg(\sum_i^nx_i^2\bigg)-\tilde b\bigg(\sum_i^nx_i\bigg)=0
      $$

      마찬가지로

      $$
      \frac{\partial S}{\partial\tilde b}=\sum_i^n\bigg(2(y_i-\tilde a x_i-\tilde b)\bigg)
      $$

      가 되며, 최적 조건은

      $$
      \bigg(\sum_i^ny_i\bigg)-\tilde a\bigg(\sum_i^nx_i\bigg)-n\tilde b=0
      $$

      으로 표현된다. 두 최적 조건을 나타내는 식을 '연립 방정식'으로 표현할 수 있으며, 이는

      $$
      \begin{bmatrix}
      \sum_i^nx_i^2 & \sum_i^nx_i\\
      \sum_i^nx_i & n
      \end{bmatrix}
      \begin{bmatrix}
      \tilde a\\
      \tilde b
      \end{bmatrix}
      =
      \begin{bmatrix}
      \sum_i^nx_iy_i\\
      \sum_i^ny_i
      \end{bmatrix}
      $$

      따라서, 위 연립 방정식을 풀이하면 $$S$$를 최소화하는
      $\tilde a, \tilde b$ 쌍을 구할 수 있다.

      ```python
      import numpy as np
      import matplotlib.pyplot as plt

      # example data with noise
      xs = np.linspace(0, 10, 10)
      a=2.5
      b=5
      y_true = a * xs + b
      ## artificial noise added.
      noise = np.random.normal(0, 3, size=xs.shape) ## 정규분포 mean:0, std: 3
      ys = y_true + noise

      plt.plot(xs,ys,'ro',label='Data with noise')
      #plt.plot(xs,y_true,'k-',label='True data')

      tilde_a=2
      tilde_b=5

      epsilon=np.zeros(xs.shape)
      for i, x in enumerate(xs):
      	y=x*tilde_a+tilde_b
      	epsilon[i]=y-ys[i]
      	plt.plot([x,x],[ys[i],y],'-')
      plt.plot(xs,tilde_a*xs+tilde_b,'m--',label='manual fit')
      print(f'residual: {(epsilon**2).sum()}')
      plt.legend()

      ## least square
      # the 2x2 matrix
      matrix=np.zeros((2,2))
      matrix[0,0]=(xs**2).sum()
      matrix[0,1]=xs.sum()
      matrix[1,0]=xs.sum()
      matrix[1,1]=len(xs)
      # the 2d vector on the right-hand-side.
      c=np.zeros(2)
      c[0]=(xs*ys).sum()
      c[1]=ys.sum()
      # obtain inverse matrix and multiply it with c
      a_lsq,b_lsq=np.linalg.inv(matrix)@c ## m^{-1} . c
      ```

# 12. Week10 (Matplotlib + Hall-petch equations, Creep data)

## 12.1. 수업 10-1 (Creep data)

- SN curve 데이터 파일 [SN_curve.txt](/assets/dat_files/lectures/1_2_data_mse/SN_curve.txt)을 다운받아서
  아래 예측 모형에 걸맞는 값들을 구해보자.

  $$
  N=B/\sigma^m
  $$

  위에서 각 기호는 아래와 같이 설명된다.

  $$
  N: \text{ number of cycles at failure }
  \newline
  \sigma: \text{Stress amplitude}
  $$

  $$
  B, m : \text{material parameters}
  $$

- Creep 데이터 파일 [creep.txt](/assets/dat_files/lectures/1_2_data_mse/creep.txt)을 다운받아서
  아래 예측 모형에 걸맞는 값들을 구해보자.

  $$
  \dot\varepsilon=K\sigma^n
  $$

  $$
  \dot\varepsilon : \text{ creep rate}
  $$

  $$
  \sigma : \text{ 응력}
  $$

  $$
  K, n : \text{material parameters}
  $$

- [SciPy](https://scipy.org)의 curve_fit 함수 활용하기

  ```python
  import numpy as np
  import matplotlib.pyplot as plt
  from scipy.optimize import curve_fit

  def power(edot,K,n):
  	return (edot/K)**(1/n)

  dat=np.loadtxt('creep.txt',skiprows=1).T
  x_data,y_data=dat

  popt, pcov=curve_fit(power,x_data,y_data,p0=[1,1])
  args=popt
  power(x_data,*args)
  plt.plot(x_data,y_data,'x')
  plt.plot(x_data,power(x_data,*args))
  plt.xscale('log')
  plt.yscale('log')
  ```

- 실습: 데이터를 활용해
  $$
  \dot\varepsilon<10^{-2}
  $$
  영역과
  $$
  \dot\varepsilon\geq 10^{-2}
  $$
  에 따로 `curve_fit`을 적용시켜서
  $$
  K
  $$
  와
  $$
  n
  $$
  값을 구해보자.

## 12.2. 수업 10-2 (Contouring)

- 등고선 (contour) plot
- 예시

  ```python
  %matplotlib widget
  import numpy as np
  import matplotlib.pyplot as plt
  ## number of grid lines
  xn=20 #along horizontal
  yn=20 #along vertical

  ## x,y range
  xlim=np.array([-2,2])
  ylim=np.array([-6,6])
  ## actual grids
  xs=np.linspace(*xlim,xn) ## 4
  ys=np.linspace(*ylim,yn) ## 11
  yy,xx=np.meshgrid(ys,xs) ##  11 x 4
  #xx,yy=np.meshgrid(xs,ys) ##  11 x 4

  ## canvas (two 2D axes, one 3D axis)
  fig=plt.figure(figsize=(13,3))
  ax1=fig.add_subplot(131)
  ax2=fig.add_subplot(132)
  ax3=fig.add_subplot(133,projection='3d')

  ## grid points
  ax1.scatter(xx,yy,c='k')
  mappable=ax2.contourf(xx,yy,z,cmap='jet')
  plt.colorbar(mappable,ax=ax2)
  if True:
  	#z=np.sqrt(xx**2+yy**2)
  	z=np.cos(xx)*yy+10
  	#z=np.log(np.abs(xx))*np.abs(yy)

  	## 3D surface
  	ax3.plot_surface(xx,yy,z,cmap='jet',alpha=0.5)
  	## colored 2D contour
  	ax3.contour(xx,yy,z,offset=0,cmap='jet')

  	for i in range(xn): ## x
  		for j in range(yn): ## y
  			ax1.text(xx[i,j],yy[i,j],f"z{i,j}={z[i,j]:.1f}",size=7,va='bottom',ha='center')

  fig.tight_layout()
  for i, ax in enumerate([ax1,ax2,ax3]):
  	ax.set_xlabel('X'); ax.set_ylabel('Y')
  	ax.set_xlim(xlim*1.3)
  	ax.set_ylim(ylim*1.3)
  ax3.set_zlabel('Z')
  ax3.set_zlim(0,)
  ```

- 예시: Schmid law

  $$
  \tau=\sigma\cos\phi\cos\lambda
  $$

  이 때

  $$
  \cos\phi\cos\lambda
  $$

  를 Schmid factor라 부른다.

  ```python
  %matplotlib inline
  import numpy as np
  import matplotlib.pyplot as plt
  nphi=200
  nlam=100
  phi=np.linspace(0,2*np.pi,nphi) ## x
  lamb=np.linspace(0,2*np.pi,nlam) ## y

  P,L=np.meshgrid(phi,lamb)
  print(L.shape)
  print(P.shape)

  fig=plt.figure(figsize=(8,2))
  ax1=fig.add_subplot(121)
  ax2=fig.add_subplot(122)
  sf=np.cos(L)*np.cos(P) # schmid factor calculation
  map=ax1.contourf(np.rad2deg(P),np.rad2deg(L),sf) ## radian -> degree로 바꿔서
  plt.colorbar(map,ax=ax1)
  ax1.set_xlabel(r'$\phi ^\circ{}$')
  ax1.set_ylabel(r'$\lambda ^\circ{}$')
  ```

- 예시, FCC 단결정의 슬립계 면방향 지수

  $$(h,k,l)$$

  그리고 슬립 방향

  $$[u,v,w]$$

  이 주어지고, 일축 인장 방향이 벡터

  $$
  (x_1,x_2,x_3)
  $$

  로 주어졌을 때,

  $$
  \phi,\lambda
  $$

  를 계산하고, 이를 활용해 인장 응력 방향에 따라서 달라지는 Schmid factor 값을 살펴보시오.

- 인장 응력 방향을 polar coordinate로 표현해서 살펴봅시다.

# 13. Week11
- 무게비 원자비

## 13.1. 수업 11-1 (무게비 원자비 변환)

- 무게비 (weight fraction)

  $$
  w_a=\frac{W_a}{W_a+W_b}\times 100 (wt.\%)
  $$

  $$
  W_a, W_b
  $$

  는 각각

  $$
  a
  $$

  원소와

  $$
  b
  $$

  원소의 질량 (혹은 무게).
  마찬가지로, 부피비는 다음과 같이 표현이 가능하겠다.

  $$
  f_a=\frac{V_a}{V_a+V_b}\times 100 (vol.\%)
  $$

  $$
  V_a, V_b
  $$

  는 각각

  $a$ 원소와 $b$ 원소의 부피

- 무게비 <-> 변환?

  - 원소 $a$의 무게는 밀도 $\rho_a$
    와 부피 $V_a$의 관계로 설명가능하다.

    $$
    \rho_a=\frac{W_a}{V_a}
    $$

    $$
    w_a=\frac{W_a}{W_a+W_b}\times 100 =\frac{\rho_aV_a}{\rho_aV_a+\rho_bV_b}\times 100
    $$

    $$
    \rightarrow w_a=\frac{1}{1+\frac{\rho_bV_b}{\rho_aV_a}}\times 100
    $$

    $$
    \rightarrow 1+\frac{\rho_bV_b}{\rho_aV_a}=\frac{100}{w_a}
    \rightarrow \frac{\rho_bV_b}{\rho_aV_a}=\frac{100}{w_a} -1
    $$

    $$
    \therefore
    \frac{V_b}{V_a}=(\frac{100}{w_a} -1)\frac{\rho_a}{\rho_b}
    $$

    마지막 관계식을 활용하여 부피비를 다시 표현하면

    $$
    f_a=\frac{V_a}{V_a+V_b}\times 100=\frac{1}{1+V_b/V_a}\times 100=\frac{1}{1+(\frac{100}{w_a} -1)\frac{\rho_a}{\rho_b}}\times 100
    $$

    따라서 각 원소의 밀도

    $$
    \rho_a,\rho_b
    $$

    그리고 무게비

    $$
    w_a [\%]
    $$

    를 알면 백분율 부피비를 구할 수 있다.

    $$
    a
    $$

    원소와

    $$
    b
    $$

    원소의 자리르 바꾸면

    $$
    f_b=\frac{1}{1+(\frac{100}{w_b} -1)\frac{\rho_b}{\rho_a}}\times 100
    $$

    ```python
    def convert_a(wa,rhoa,rhob): ## get f_a
    	return 1/(1+(100/w_a-1)*(rhoa/rhob))*100
    def convert_b(wb,rhoa,rhob): ## get f_a
    	return 1/(1+(100/w_b-1)*(rhob/rhoa))*100
    ```

- 유용한 패키지 [periodic table](https://pypi.org/project/periodictable/),
  [Github page](https://github.com/python-periodictable/periodictable)
  [Documentation](https://periodictable.readthedocs.io/en/latest/)

  ```bash
  c:\users\user> pip install periodictable
  ```

- 예제
  한 철강 제품의 무게비가 다음과 같았다.

  $$
  Fe:C = 0.99: 0.01
  $$

  철의 부피비,

  $$
  v_{Fe}
  $$

  는 얼마인가?

  ```python

  ```

## 13.2. 수업 11-2

# 14. Week12
- Matplotlib imaging, color-coding, EBSD 데이터 분석

- 목표
  - SEM 데이터를 소개하고, Ferrite와 Martensite로 분류

## 14.1. 수업 12-1

- 색표현을 설명

  - Gray scale (0~255)
  - RGB R(0~255), G(0~255), B(0~255)
  - RGBA R(0~2550), G(0~255), B(0~255), alpha(0~1)
  - [참고](<https://www.w3schools.com/colors/colors_rgb.asp?color=rgb(102,%20255,%20255)>)

- [imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html) 함수

  ```python
  import matplotlib.pyplot as plt
  import numpy as np

  # 5x5 랜덤 배열
  data = np.random.rand(5, 5)

  plt.imshow(data, cmap='viridis', interpolation='nearest')
  plt.colorbar()  # 값과 색의 대응 막대 추가
  plt.show()
  ```

- Color map (`cmap`) 옵션

  ```python
  import matplotlib.pyplot as plt
  import numpy as np

  # 100x100 배열: 0~255 값 (가상의 화상)
  grain_map = np.random.randint(0, 255, (100, 100))

  fig=plt.figure(figsize=(8,2))
  # 1x3 axes 생성
  ax1=fig.add_subplot(131)
  ax2=fig.add_subplot(132)
  ax3=fig.add_subplot(133)
  #--
  # random하게 만들어진 0~255 사이의 값 확인
  ax1.hist(grain_map.flatten())# histogram
  ##
  cmaps=['jet','gray']
  for i, ax in enumerate([ax2,ax3]):
  	ax.imshow(grain_map, cmap=cmaps[i])
  	ax.set_title(f'color map: {cmaps[i]}')
  ```

- 실제 미세조직 사진 활용 실습

  - 아래 사진을 [여기](/assets/dat_files/lectures/1_2_data_mse/dualphase_sem.png) 눌러서 다운 받자

  ![imag](/assets/dat_files/lectures/1_2_data_mse/dualphase_sem.png)

  ```python
  from PIL import Image
  import numpy as np
  import matplotlib.pyplot as plt

  fn='../data/dualphase_sem.png' ## file name을 경로를 포함하여 정확하게 기입해야 한다.
  img_rgba = Image.open(fn) ## PIL, RGBA
  img_gray=img_rgba.convert('L') ## convert image into gray scale
  img_gray=np.asarray(img_gray)
  plt.imshow(img_gray,cmap='gray')
  ```

  위 사진은 ferrite와 martensite가 같이 존재하는 dual-phase 철강 제품의
  주사 전자 현미경 사진이다. 이 사진에서 밝은 부분은 ferrite, 어두운 부분은 martensite
  상이다. 이를 구분하여 두 상의 '분율'을 구해보자.

  ```python
  from PIL import Image
  import numpy as np
  import matplotlib.pyplot as plt
  img=Image.open('../data/dualphase_sem.png')
  img=np.asarray(img)
  print(img.shape)

  ## Canvas와 사용할 축을 2x2 grid의 형태로 만들자.
  fig=plt.figure(figsize=(7,4))
  ax1=fig.add_subplot(221)
  ax2=fig.add_subplot(222)
  ax3=fig.add_subplot(223)
  ax4=fig.add_subplot(224)

  ## 첫번째 axis에는 각 화상(pixel)에서 0~255사이의
  # 값들이 어떻게 분포하는지 histogram으로 그리자.
  ax1.hist(img.flatten())
  # 그리고 그 옆에 불러온 SEM 이미지를 그려보자.
  ax2.imshow(img,cmap='gray')

  ## 아래는 ferrite상과 martensite 상을 구분하는 간단한 예시를 살펴보자.

  #newimg=img.copy()
  #flg=img>img.mean()
  #newimg[flg]=255
  #newimg[~flg]=0
  #h=ax3.hist(newimg.flatten())
  #ax4.imshow(newimg,cmap='gray')
  #for i, ax in enumerate([ax1,ax3]):
  #    ax.set_ylim(0,300000)

  #white,black=h[0][0],h[0][-1]
  #ferrite=white/(white+black)
  #martensite=black/(white+black)
  #print(ferrite,martensite)
  ```

- 아래 세 이미지는 한 dual-phase 시편 내의 각기 다른 3 위치에서 촬영한 SEM image이다.
  위에서 다뤘던 내용을 익혀 적용하고, 이를 바탕으로 이 시편에서의 ferrite와 martensite
  분율을 고르시오.

  ![imag](/assets/dat_files/lectures/1_2_data_mse/centercenter.png)
  ![imag](/assets/dat_files/lectures/1_2_data_mse/edgecenter.png)
  ![imag](/assets/dat_files/lectures/1_2_data_mse/edgeedge.png)

  - 위 SEM 사진을 다음 링크를 활용해 다운 받자:

  [imag1](/assets/dat_files/lectures/1_2_data_mse/centercenter.png)
  [imag2](/assets/dat_files/lectures/1_2_data_mse/edgecenter.png)
  [imag3](/assets/dat_files/lectures/1_2_data_mse/edgeedge.png)

## 14.2. 수업 12-2

- 수업 12-1 내용을 Argparse를 활용해 CLI 프로그램으로 작성해보자.
- EBSD data 분석

# 15. Week13
- 내삽과 외삽, 선형회귀

## 15.1. 수업 13-1

## 15.2. 수업 13-2

# 16. Week14

## 16.1. 수업 14-1

- 실습 예시
  - 금속 합금 조성 (Cu %) vs 전기 전도도

```python
import numpy as np
import matplotlib.pyplot as plt

# 예제: 금속 합금 조성(Cu %) vs 전기 전도도
x = np.array([0, 5, 10, 15, 20])
y = np.array([58, 55, 50, 45, 42])  # 전도도 W/mK

plt.scatter(x, y, color='b', label='Data')
plt.xlabel("Cu content [%]")
plt.ylabel("Electrical Conductivity [W/mK]")
plt.title("Conductivity vs Cu content")
plt.grid(True)
plt.legend()
plt.show()
```

## 16.2. 수업 14-2

# 17. Week15 (기말고사)

## 17.1. 수업 15-1

## 17.2. 수업 15-2
