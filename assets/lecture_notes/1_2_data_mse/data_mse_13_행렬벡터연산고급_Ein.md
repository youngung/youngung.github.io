---
layout: distill
title: 행렬·벡터 연산과 Einstein 표기법
description: 텐서 contraction과 NumPy einsum의 기초
target: 1학년 2학기
permalink:
featured: true
prerequisite: 벡터와 행렬 연산
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

- [1. 목표](#1-목표)
- [2. 아인슈타인 표기법과 np.einsum 함수](#2-아인슈타인-표기법과-npeinsum-함수)
- [3. 벡터 스케일링 (스칼라 곱)](#3-벡터-스케일링-스칼라-곱)
- [4. 벡터의 크기](#4-벡터의-크기)
- [5. 단위 벡터 (unit)](#5-단위-벡터-unit)
- [6. 예제](#6-예제)
  - [6.1. 같은 방향의 단위 벡터 구하기.](#61-같은-방향의-단위-벡터-구하기)
  - [6.2. 예시: 반대방향 벡터](#62-예시-반대방향-벡터)
  - [6.3. 예시: 벡터의 합](#63-예시-벡터의-합)
  - [6.4. 예시: 벡터의 차](#64-예시-벡터의-차)
  - [6.5. 내적 (inner dot)](#65-내적-inner-dot)
  - [6.6. (nxn)행렬과 (n)벡터 곱](#66-nxn행렬과-n벡터-곱)
  - [6.7. 행렬 곱1 (single dot)](#67-행렬-곱1-single-dot)
  - [6.8. 행렬 곱2 (double dot)](#68-행렬-곱2-double-dot)
- [7. np.einsum 활용](#7-npeinsum-활용)
  - [7.1. 입력 인덱스와 출력 인덱스 읽기](#71-입력-인덱스와-출력-인덱스-읽기)
  - [7.2. 3차원 배열 두 개의 이중수축](#72-3차원-배열-두-개의-이중수축)
  - [7.3. 앞에서 배운 연산과 비교하기](#73-앞에서-배운-연산과-비교하기)
  - [7.4. 인덱스를 작성할 때 확인할 사항](#74-인덱스를-작성할-때-확인할-사항)
- [연습 문제](#연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)

# 1. 목표

이 자료에서 $[\boldsymbol A]$, $[\boldsymbol x]$는 행렬·벡터의 성분 배열을 뜻하며, 배열의 행렬곱은 $[\boldsymbol A][\boldsymbol x]$처럼 붙여 쓴다. 물리적 벡터·텐서의 단일수축은 $\cdot$로 표시한다.


- Einstein summation 을 이해하고, 다양한 벡터 및 행렬 연산에 활용할 수 있다.

# 2. [아인슈타인 표기법](https://ko.wikipedia.org/wiki/아인슈타인_표기법)과 [np.einsum](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html) 함수

Reference: [https://rockt.ai/2018/04/30/einsum](https://rockt.ai/2018/04/30/einsum)

아인슈타인 표기법은, 벡터, 행렬, 텐서가 사용된 수학 수식에서, 중복된
(첨자) 기호와 합 기호($\sum$)가 함께 나타나는 연산을 표기할 때,
합기호를 생략하는데 착안하여 복잡한 수식을 좀 더 간략하게 표기하는
방식이다.

아래 수식에서 한 기호가 하나의 값을 표현할 때는 굵지 않은 글씨체로
($a$), 만약 벡터와 같이 하나의 기호가 여러 값으로 이루어져 있을 때는
굵은 글씨체 ($\boldsymbol a$)로 표기하겠다.

# 3. 벡터 스케일링 (스칼라 곱)

- 주어진 벡터 $\boldsymbol a$에 스칼라 $c$를 곱하면 또 다른 벡터
  $\boldsymbol b$이 된다. 이는 아래와 같이 수식으로 표현가능하다.

$$
c\boldsymbol a=\boldsymbol b
$$

- 이를 index 표기법으로 나타내면, 3차원 공간에서 각 벡터는 3성분을 지니므로, 아래 첨자
  $_i$를 활용해 각 첨자를 구분할 수 있다. 즉 벡터 $\boldsymbol a$는 사실
  $(a_1,a_2,a_3)$로 구분되는 세 성분으로 이루어져 있으며, 이는 벡터 $\boldsymbol b$
  도 마찬가지이다. 따라서 앞선 수식을 각 성분에 대해 나타낸다면, 각기 구분되는 세 수식
  $b_1=ca_1$ 그리고 $b_2=ca_2$, 마지막으로 $b_3=ca_3$으로 대신할 수 있다. 그런데,
  아무래도 이건 조금 번거로운 느낌이 든다. 아래와 같이 좀 더 간략하게 표기하는 게 좋겠다.

$$
b_i=ca_i \text{ with } i=1,2,3
$$

- 위를 Python의 List, 그리고 NumPy를 가지고 각기 표현할 수도 있겠다.

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
a=[1,2,3]
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

# 4. 벡터의 크기

- 벡터의 크기는 앞서 이미 다루었다. 한 벡터 $\boldsymbol a$의 크기는
  $|\boldsymbol a|$라 표기하고, 이는 다음과 같이 정의된다.

$$|\boldsymbol a|=\sqrt{\sum_i^3a_i^2}$$

- 고전적인 아인슈타인 표기법은 위와 같이 하나의 물리량에 일반적으로 적용되진 않는다.
  하지만 NumPy의 einsum 함수는 적용된다. 아래와 같이 먼저 벡터내의 요소의 거듭제곱으로
  이루어진 벡터를 구할 수 있다. 벡터 $\boldsymbol a$가 가령 아래와 같다고 하자.

$$
\boldsymbol a= (2,3,4)
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

`np.linalg.norm(a)`

</p></aside>

# 5. 단위 벡터 (unit)

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

# 6. 예제

## 6.1. 같은 방향의 단위 벡터 구하기.

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

## 6.2. 예시: 반대방향 벡터

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

## 6.3. 예시: 벡터의 합

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

## 6.4. 예시: 벡터의 차

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

## 6.5. 내적 (inner dot)

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
## NumPy없이 구현
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
## NumPy없이 구현
a=[1,2,3]
b=[4,5,6]
c=0.
for i in range(len(a)):
   c=c+a[i]*b[i]
print(c)
```

{% endtab %}
{% tab 내적 NumPy %}

```python
import numpy as np
## NumPy로 구현
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
## NumPy로 구현
a=np.array([1,2,3])
b=np.array([4,5,6])
np.einsum('i,i->',a,b)
```

{% endtab %}
{% tab 내적 etc %}

```python
import numpy as np
## NumPy로 구현
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

## 6.6. (nxn)행렬과 (n)벡터 곱

행과 열이 각각 n인 행렬과 (즉 nxn행렬)과 n성분으로 구성된 벡터간의 곱

$$
[\boldsymbol c] = [\boldsymbol A][\boldsymbol v]
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

## 6.7. 행렬 곱1 (single dot)

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

## 6.8. 행렬 곱2 (double dot)

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

# 7. np.einsum 활용

`np.einsum`은 배열의 **어느 축을 곱하고 합산할지, 결과에 어느 축을 남길지**를 인덱스 문자열로 지정한다.
앞의 벡터 내적과 행렬곱뿐 아니라, 세 개 이상의 축을 가진 배열의 수축에도 사용할 수 있다.
이 절에서는 실수 배열을 다룬다.

## 7.1. 입력 인덱스와 출력 인덱스 읽기

```python
C = np.einsum('ikl,lkj->ij', A, B)
```

위 문자열은 다음 순서로 읽는다.

1. 쉼표 앞의 `ikl`은 첫 번째 배열 `A`의 세 축에 붙인 이름이다.
2. 쉼표 뒤의 `lkj`는 두 번째 배열 `B`의 세 축에 붙인 이름이다.
3. `->ij`는 결과에 `i`, `j`를 이 순서로 남긴다는 뜻이다.
4. 입력에는 있지만 출력에는 없는 `k`, `l`은 합산한다.

인덱스 문자는 Python 변수명이 아니라 **배열 축의 이름표**다. 같은 이름으로 연결한 축은 크기가 맞아야 한다.
이 절의 예제는 같은 인덱스의 크기를 정확히 일치시킨다.

고전적인 Einstein 합 규약에서는 반복 인덱스를 합산하지만, `einsum`의 명시적 출력 표기는 이를 더 유연하게 지정한다.
예를 들어 `'i,i->i'`는 `i`를 출력에 남기므로 합산하지 않고 원소별 곱을 계산한다.
반대로 `'i->'`는 한 번만 나타난 `i`도 합산한다.
출력을 생략하면 결과 축의 순서가 인덱스 문자의 알파벳 순서로 정해지므로, 여기서는 **`->`를 명시하는 방식**을 사용한다.
세부 동작은 [NumPy 공식 문서](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html)를 참고한다.

## 7.2. 3차원 배열 두 개의 이중수축

`A.shape = (10, 3, 12)`, `B.shape = (12, 3, 8)`인 두 배열을 생각하자.
축이 세 개인 배열은 일반적인 2차원 행렬과 구분한다. 여기서는 아래에 정의한 수축을 수행한다.

$$
C_{ij}=\sum_{k=1}^{3}\sum_{l=1}^{12}A_{ikl}B_{lkj},
\qquad i=1,\ldots,10,\quad j=1,\ldots,8.
$$

| 인덱스 | `A`의 축과 크기 | `B`의 축과 크기 | 처리 |
| --- | --- | --- | --- |
| `i` | 첫째 축: 10 | 없음 | 결과의 첫째 축으로 유지 |
| `j` | 없음 | 셋째 축: 8 | 결과의 둘째 축으로 유지 |
| `k` | 둘째 축: 3 | 둘째 축: 3 | 합산 |
| `l` | 셋째 축: 12 | 첫째 축: 12 | 합산 |

자유 인덱스는 `i`, `j`이고, 합산 인덱스는 `k`, `l`이다.
따라서 결과는 `C.shape = (10, 8)`인 2차원 배열이다.
각 결과 성분은 $3\times12=36$개의 곱을 더한 값이다.
예를 들어 첫 번째 성분은

$$
C_{11}=\sum_{k=1}^{3}\sum_{l=1}^{12}A_{1kl}B_{lk1}
$$

이다. 수식에서는 인덱스를 1부터 표시했지만, Python에서는 0부터 시작하므로 첫 성분은 `C[0, 0]`이다.

먼저 두 예제가 공통으로 사용할 데이터를 만든다.

```python
import numpy as np

A = np.arange(10 * 3 * 12, dtype=float).reshape(10, 3, 12)
B = np.arange(12 * 3 * 8, dtype=float).reshape(12, 3, 8)
```

{% tabs 행렬곱3차 %}
{% tab 행렬곱3차 반복문 %}

```python
C_loop = np.zeros((A.shape[0], B.shape[2]))
for i in range(A.shape[0]):
    for j in range(B.shape[2]):
        for k in range(A.shape[1]):
            for l in range(A.shape[2]):
                C_loop[i, j] += A[i, k, l] * B[l, k, j]

print(C_loop.shape)  # (10, 8)
```

바깥의 두 반복문은 결과 성분을 선택한다. 안쪽의 두 반복문은 수식의 두 합을 계산한다.

{% endtab %}
{% tab 행렬곱3차 einsum %}

```python
C_einsum = np.einsum('ikl,lkj->ij', A, B)
print(C_einsum.shape)  # (10, 8)
```

`k`, `l`을 출력에서 제외해 두 축을 수축하고, `i`, `j`만 남긴다.

{% endtab %}
{% endtabs %}

두 방법을 모두 실행한 뒤, 결과를 비교한다.

```python
print(np.allclose(C_loop, C_einsum))  # True
print(C_einsum[0, 0])                # 100800.0
```

`np.allclose`는 작은 부동소수점 오차를 허용하여 두 배열이 같은지 검사한다.
인덱스 순서가 맞는지도 확인하려면, 위처럼 원소마다 값이 다른 배열로 비교하는 것이 좋다.
합산되는 항의 개수는 모든 원소가 1인 별도 예제로 확인할 수 있다.

```python
A_ones = np.ones((10, 3, 12))
B_ones = np.ones((12, 3, 8))
C_ones = np.einsum('ikl,lkj->ij', A_ones, B_ones)
print(np.allclose(C_ones, 36))  # True: 각 성분은 1을 36번 더한 값
```

## 7.3. 앞에서 배운 연산과 비교하기

| 연산 | `einsum` 표현 | 같은 연산의 다른 표현 |
| --- | --- | --- |
| 벡터 내적 | `np.einsum('i,i->', a, b)` | `a @ b` |
| 벡터의 원소별 곱 | `np.einsum('i,i->i', a, b)` | `a * b` |
| 다이아딕 곱의 성분 배열 | `np.einsum('i,j->ij', a, b)` | `np.outer(a, b)` |
| 행렬·벡터 곱 | `np.einsum('ij,j->i', M, v)` | `M @ v` |
| 행렬곱 | `np.einsum('ik,kj->ij', M, N)` | `M @ N` |
| 두 행렬의 이중수축 | `np.einsum('ij,ij->', M, Q)` | `np.sum(M * Q)` |
| 행렬 전치 | `np.einsum('ij->ji', M)` | `M.T` |
| 대각 성분 추출 | `np.einsum('ii->i', M)` | `np.diag(M)` |
| 대각합(trace) | `np.einsum('ii->', M)` | `np.trace(M)` |

출력 문자열이 비어 있는 `->`는 결과가 스칼라임을 뜻한다.
또한 같은 배열에 `ii`처럼 인덱스를 반복하면 대각 성분을 선택한다.
이를 출력에 남기면 대각 성분 배열이고, 제거하면 대각합이다.
다이아딕 곱은 벡터 외적(cross product) `np.cross`와 다른 연산이다.

## 7.4. 인덱스를 작성할 때 확인할 사항

- 입력 문자열의 인덱스 수와 각 배열의 축 수가 맞는지 확인한다.
- 합산하려는 축의 이름과 크기가 맞는지 확인한다. 위 예제에서 `B`가 `(12, 4, 8)`이면 `k`의 크기가 맞지 않아 오류가 발생한다.
- 결과에 남길 인덱스와 그 순서를 `->` 뒤에 적는다. 같은 입력에 `->ji`를 사용하면 결과는 `(8, 10)`이고 앞의 결과의 전치다.
- 단순 행렬곱에는 `@`도 명확한 표현이다. 여러 축을 수축할 때에는 `einsum`으로 수식을 직접 대응시킬 수 있다.

---

# 연습 문제

## 문제 1

Einstein 합 규약에서 한 항에 같은 첨자가 두 번 나타나면 무엇을 의미하는가?

<!--
풀이와 해답:
그 첨자에 대해 합을 취한다는 의미이다.
-->

## 문제 2

$A_{ij}b_j$에서 자유첨자를 쓰시오.

<!--
풀이와 해답:
i이다.
-->

## 문제 3

NumPy에서 Einstein 표기법 계산에 사용하는 함수는 무엇인가?

<!--
풀이와 해답:
np.einsum이다.
-->
