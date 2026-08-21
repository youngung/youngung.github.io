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
- [2. 벡터의 성분](#2-벡터의-성분)
- [3. 벡터의 합](#3-벡터의-합)
  - [3.1. 예시: 벡터의 차](#31-예시-벡터의-차)
- [4. 벡터 스케일링 (스칼라 곱)](#4-벡터-스케일링-스칼라-곱)
- [5. 벡터의 크기 (magnitude)](#5-벡터의-크기-magnitude)
- [6. 단위 벡터 (unit vector)](#6-단위-벡터-unit-vector)
- [7. 벡터 내적과 끼인 각 구하기](#7-벡터-내적과-끼인-각-구하기)
- [8. 예시](#8-예시)
  - [8.1. Cubic구조내의 두 결정방위 $(u\_1,v\_1,w\_1)$과 $(u\_2,v\_2,w\_2)$ 간의 각도?](#81-cubic구조내의-두-결정방위-u_1v_1w_1과-u_2v_2w_2-간의-각도)
  - [8.2. Cubic구조내의 두 결정면 $(h\_1,k\_1,l\_1)$과 $(h\_2,k\_2,l\_2)$의 각 법선방향](#82-cubic구조내의-두-결정면-h_1k_1l_1과-h_2k_2l_2의-각-법선방향)
  - [8.3. Cubic 내 두 면 $(h\_1k\_1l\_1)$과 $(h\_2k\_2l\_2)$ 면 법선 사이의 끼인 각 구하기](#83-cubic-내-두-면-h_1k_1l_1과-h_2k_2l_2-면-법선-사이의-끼인-각-구하기)
  - [8.4. Tetragonal내의 두 결정방향(crystal direction) $\[u\_1,v\_1,w\_1\]$과 $\[u\_2,v\_2,w\_2\]$ 간의 각도 구하기](#84-tetragonal내의-두-결정방향crystal-direction-u_1v_1w_1과-u_2v_2w_2-간의-각도-구하기)
  - [8.5. 예시 5:](#85-예시-5)
  - [8.6. 예시 6 (take-home)](#86-예시-6-take-home)
- [9. 외적 (cross product)](#9-외적-cross-product)
  - [9.1. unitcell 부피계산.](#91-unitcell-부피계산)
  - [9.2. (take-home)](#92-take-home)
  - [9.3. (take-home)](#93-take-home)


# 1. 목표
- 반복문, 함수, Numpy를 활용해 기초 벡터 연산 및 행렬 연산 수행 및 이해

# 2. 벡터의 성분
한 벡터 $\boldsymbol a$는 아래와 같이 세 성분으로 이루어져 있다.

$\boldsymbol a = (a_x,a_y,a_z)$


# 3. 벡터의 합

벡터 $\boldsymbol a$ 와  $\boldsymbol b$의 합은 새로운 벡터 $\boldsymbol c$가
된다.

$$
\boldsymbol c =  \boldsymbol a + \boldsymbol b
$$

이는 아래와 같이 각 성분들간의 합을 수행하고,

$$
c_x = a_x+b_x,
\ \ \
c_y = a_y+b_y,
\ \ \
c_z = a_z+b_z
$$

이 결과 값이 성분으로 이루어진 벡터가 그 결과가 된다.

$$
\boldsymbol c = (c_x,c_y,c_z)=(a_x+b_x,a_y+b_y,a_z+b_z)
$$

이는 아래와 같이 List 자료를 활용해 구현할 수 있다.

```python
a=[3,4,5]
b=[3,-5,-2]
c=[0,0,0]
for i in range(len(a)):
	c[i]=a[i]+b[i]
```

## 3.1. 예시: 벡터의 차
아래와 같이 두 벡터의 차도 새로운 벡터가 된다.
$$
\boldsymbol c =  \boldsymbol a - \boldsymbol b
$$

$$
c_x = a_x-b_x,
\ \ \
c_y = a_y-b_y,
\ \ \
c_z = a_z-b_z
$$

$$
\boldsymbol c = (c_x,c_y,c_z)=(a_x-b_x,a_y-b_y,a_z-b_z)
$$

위를 구현하면 아래와 같이 된다.

```python
a=[3,4,5]
b=[3,-5,-2]
c=[0,0,0]
for i in range(len(a)):
	c[i]=a[i]-b[i]
```

# 4. 벡터 스케일링 (스칼라 곱)

주어진 벡터 $\boldsymbol a$에 스칼라 $c$를 곱하면 또 다른 벡터 $\boldsymbol b$이 된다.

3차원 공간에서 각 벡터는 3성분을 이를 각각 $(a_x,a_y,a_z)$ 라 하자.

스케일링이 된 벡터 $\boldsymbol b$는 아래와 같이 계산된다.

$$
(b_x,b_y,b_z)=(ca_x,ca_y,ca_z)
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


# 5. 벡터의 크기 (magnitude)

벡터는 방향과 크기를 모두 가지고 있다. 한 벡터 $\boldsymbol a$의 크기를
$|\boldsymbol a|$라 표기하자. 이는 다음과 같이 정의된다.

$$|\boldsymbol a|=\sqrt{a_x^2+a_y^2+a_z^2}$$

이를 List를 활용해 구현한다면:
```python
a=[2,3,4]
mag=a[0]**2+a[1]**2+a[2]**2
mag=mag**0.5
```

혹은 numpy를 활용해서 아래와 같이 구현할 수 있다.
```python
import numpy as np
a=np.array([2,3,4])
mag=(a**2).sum()
mag=mag**0.5

# 혹은 더 줄여서
mag=((a**2).sum())**0.5
```

# 6. 단위 벡터 (unit vector)

벡터 $\boldsymbol a$의 크기가 1 이라면 (즉 $|\boldsymbol a=1|$),
벡터 $\boldsymbol a$ 를 단위 벡터(unit vector)라 부른다. 즉 단위 벡터란, 크기가 1인
벡터를 뜻한다. 주어진 한 벡터 $\boldsymbol a$의 단위 벡터를 $\bar{\boldsymbol a}$라
할 때, $\boldsymbol a$와 $\bar{\boldsymbol a}$의 관계를 다음과 같이 표현할 수 있다:

$$
(\bar a_x,\bar a_y,\bar a_z)
=\bigg(
  \frac{a_x}{\sqrt{a_x^2+a_y^2+a_z^2}},
  \frac{a_y}{\sqrt{a_x^2+a_y^2+a_z^2}},
  \frac{a_z}{\sqrt{a_x^2+a_y^2+a_z^2}}
  \bigg)
$$

이와 같은 연산을 Python을 활용해 아래와 같이 구현할 수 있겠다.
```python
def get_mag(v):
   import math
   return math.sqrt(v[0]**2+v[1]**2+v[2]**2)
```

혹은 아래와 같이 math 페키지 없이 구현할 수 있겠다.
```python
def get_mag(v):
   return (v[0]**2+v[1]**2+v[2]**2)**0.5
```

# 7. 벡터 내적과 끼인 각 구하기

두 3D 벡터가 주어졌을 때 사이 끼인 각을 구하려면, 앞서 활용된 서로다른 두 벡터의 정의를 함께
활용할 수 있다. 즉

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

위를 `math`모듈과 그 모듈내의 `sqrt`, `acos`을 활용하여 아래와 같은 간단한 코드를 작성할
수 있다. <aside><p>sqrt는 square root, 즉 제곱근에서 따왔고 acos 함수는 arccosine,
즉 코사인 함수의 역함수, $\cos^{-1}$ 에서 따왔다. </p></aside>

```python
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
## 정확히 90도가 아니라 90.00001872397223 로 표현된다면??? 무엇 때문일까?
```

# 8. 예시
## 8.1. Cubic구조내의 두 결정방위 $(u_1,v_1,w_1)$과 $(u_2,v_2,w_2)$ 간의 각도?

```python
## cubic 결정구조내의 밀러 인덱스 [uvw]로 주어진 결정방위에 해당하는 unit vector 구하기
miller1=np.array([u1,v1,w1])
unit_vector1=miller / get_mag(miller1)

miller2=np.array([u2,v2,w2])
unit_vector2=miller / get_mag(miller2)

angle=get_ang(unit_vector1,unit_vector2)

angle*180/np.pi ## np.pi: 원주율

np.deg2rad(angle) ## np 패키지내의 메소드 활용 가능
```

## 8.2. Cubic구조내의 두 결정면 $(h_1,k_1,l_1)$과 $(h_2,k_2,l_2)$의 각 법선방향

사이의 각도?

## 8.3. Cubic 내 두 면 $(h_1k_1l_1)$과 $(h_2k_2l_2)$ 면 법선 사이의 끼인 각 구하기

## 8.4. Tetragonal내의 두 결정방향(crystal direction) $[u_1,v_1,w_1]$과 $[u_2,v_2,w_2]$ 간의 각도 구하기
- Cubic의 경우, $a=b=c$이며 세 사이 각이 $\alpha=\beta=\gamma=90\degree$이다.
- Tetragonal의 경우, $a=b\ne c$이며 $\alpha=\beta=\gamma=90\degree$을 만족한다.
- Tetragonal structure는 c축 방향으로 늘어난 형태이다. cubic과 다르게 miller 인덱스를
  마냥 벡터로 활용할 수 없다. Tetragonality의 정도에 따라 주어진 밀러 인덱스를 적절히 벡터로
  바꿔야 한다. 예를 들어, c축의 길이가 a축에 비해 2배 길다면 [001] 밀러 인덱스는 사실 [0,0,2]
  벡터가 된다.
- 이와 같은 상황을 '보정'해주기 위해서는 $c/a$ 비율 (c over a ratio)를 활용해야 한다.
- 따라서, $c/a$ ratio가 알려진 Tetragonal의 Miller index [$u_1v_1w_1$]로 표현된 결정방위의
  실제 길이는:
  $$
  \sqrt{ (u_1\times 1)^2+(v_1\times 1)^2+(w_1\times \frac{c}{a})^2 }
  $$

- Tetragonal 내의 결정 방향 $[uvw]$를 벡터 $[x,y,z]$로 바꾸는 함수는?
  ```python
  def miller2vect_tetragonal(miller,ca_ratio):
    u,v,w=miller
    ## 오직 z성분값을 구할때만 c over a 비율이 곱해진 것에 유의하시오.
    x=u
    y=v
    z=w*ca_ratio
    return x,y,z
  ```

- 위 결과인 벡터 $(x,y,z)$를 unit 벡터 $(\bar x,\bar y,\bar z)$로 바꾸면?
  $$
  \bar x= \frac{x}{\sqrt{x^2+y^2+{\color{red}z}^2}} = \frac{x}{\sqrt{u^2+v^2+({\color{red} w\frac{c}{a}})^2}}  \newline
  \bar y= \frac{y}{\sqrt{x^2+y^2+{\color{red}z}^2}} = \frac{y}{\sqrt{u^2+v^2+({\color{red} w\frac{c}{a}})^2}}  \newline
  \bar z= \frac{z}{\sqrt{x^2+y^2+{\color{red}z}^2}} = \frac{z}{\sqrt{u^2+v^2+({\color{red} w\frac{c}{a}})^2}}  \newline
  $$

- 위를 Python으로 구현해보자.
```python
def m2unitv_tetragonal(miller,ca_ratio):
  v=miller2vect_tetragonal(miller,ca_ratio)
  v=np.array(v)
  mag=get_mag(v)
  return v/mag ## element-wise operation
```

- 다음으로 두 결정 방위 간의 각도는?
```python
m1=[3,1,1]
m2=[1,0,1]

um1=m2unitv_tetragonal(m1)
um2=m2unitv_tetragonal(m2)

get_ang(um1,um2) #
```

## 8.5. 예시 5:
- Tetragonal 내의 결정면 $(hkl)$의 수직 방향은?
  결정 방향(crystal direction)과 다르게 결정면의 수직방향은 (norm of crystal plane)
  다른 방식으로 영향을 받는다.

  결정 방향의 경우 아래와 같이 벡터로 바뀌었다면
   $(x,y,z)=(u,v,w{\color{red}\frac{c}{a}})$
  결정 면의 수직방향은 아래와 같이 바뀐다.
   $(x,y,z)=(h,k,l{\color{green}\frac{a}{c}})$
- 두 결정면 $(h_1,k_1,l_1)$과 $(h_2,k_2,l_2)$의 수직선 사이의 각도 구하는 Python script 작성해보기

## 8.6. 예시 6 (take-home)
 cubic내에서는 $[101]$ 결정방향과 $(101)$면의 법선방향이 일치한다. 하지만
 Tetragonal의 경우 $[101]$ 결정방향과 $(101)$면의 법선 방향이 일치하지 않는다.
 $\beta$Tin은 상온에서 Body-centered tetragonal 구조를 가진다. 격자상수 $a,b,c$가
 각각 5.81, 5.81, 3.18 $\AA$ 라면, $[101]$ 결정 방향과 $(101)$ 결정면의 법선 방향
 사이의 끼인 각도는 얼마인가? 이미 작성된 Python script를 활용하고, 보완하거나 추가하여
 각도를 계산해보자.

# 9. 외적 (cross product)

- 설명
  두 벡터 $\boldsymbol a, \boldsymbol b$의 외적이 다음과 같이 표현된다.

  $$
  \boldsymbol c = \boldsymbol a \times \boldsymbol b
  $$

  $$
  c_i=\sum_j^3 \sum_k^3 \epsilon_{ijk}a_jb_k \newline

  c_x= a_yb_z - a_zb_y \newline
  c_y= a_zb_x - a_xb_z \newline
  c_z= a_xb_y - a_yb_x
  $$

  어떻게 파이썬으로 구현할 수 있나?

  ```python
  import numpy as np

  a = np.array([1, 2, 3])
  b = np.array([4, 5, 6])

  c = np.zeros(3)

  c[0]=a[1]*b[2]-a[2]*b[1]
  c[1]=a[2]*b[0]-a[0]*b[2]
  c[2]=a[0]*b[1]-a[1]*b[0]
  ```

## 9.1. unitcell 부피계산.


## 9.2. (take-home)

전위선 (dislocation line)의 방향 $\boldsymbol{l}$이고 버거스 벡터의
방향 $\boldsymbol{b}$이라면 슬립면의 법선 벡터 $\boldsymbol{n}$은 다음의
관계를 가진다.

$$
\boldsymbol{n}=\boldsymbol{l}\times \boldsymbol{b}
$$

위를 통해 임의의 전위 선 방향 $\boldsymbol{l}=[uvw]$와 버거스 벡터
$\boldsymbol{b}=[hkl]$ 가 주어진 cubic 결정 구조에서 슬립면 벡터 $\boldsymbol{n}$
을 계산하는 함수를 작성해보시오.

## 9.3. (take-home)

앞선 예시에서 주어진 결정법선 $n$을 miller index로 구해보시오.