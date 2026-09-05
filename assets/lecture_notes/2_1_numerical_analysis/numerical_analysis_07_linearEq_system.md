---
layout: page
title: 수치해석
description: 재료공학도를 위한 수치해석
target: 2학년 1학기
permalink:
prerequisite: 재료공학개론1, 데이터 재료과학
toc:
  0.1. sidebar: left
---


- [1. Week5 (연립 방정식)](#1-week5-연립-방정식)
  - [1.1. 2원 연립 방정식](#11-2원-연립-방정식)
  - [1.2. 대입법 풀이 (손으로 풀이)](#12-대입법-풀이-손으로-풀이)
  - [1.3. 가감법 풀이 (덧셈이나 뺄셈을 활용해 손으로 풀이)](#13-가감법-풀이-덧셈이나-뺄셈을-활용해-손으로-풀이)
  - [1.4. 기하학적 의미](#14-기하학적-의미)
- [2. 3원 연립 방정식](#2-3원-연립-방정식)
- [3. 행렬을 활용한 풀이](#3-행렬을-활용한-풀이)
  - [3.1. 2원 연립 방정식을 행렬식으로 표현](#31-2원-연립-방정식을-행렬식으로-표현)
  - [3.2. 3원 연립 방정식을 행렬식으로 표현](#32-3원-연립-방정식을-행렬식으로-표현)
- [4. 예시](#4-예시)
  - [4.1. 아래 연립 방정식을 행렬의 형태로 바꿔보세요.](#41-아래-연립-방정식을-행렬의-형태로-바꿔보세요)
  - [4.2. 아래 연립 방정식을 행렬의 형태로 바꿔보세요.](#42-아래-연립-방정식을-행렬의-형태로-바꿔보세요)
  - [4.3. 해가 없는 경우?](#43-해가-없는-경우)
  - [4.4. 판별식](#44-판별식)
- [5. 행렬로 표현된 연립방정식의 풀이](#5-행렬로-표현된-연립방정식의-풀이)


# 1. Week5 (연립 방정식)

## 1.1. 2원 연립 방정식

$$
\begin{matrix}
2x+y=5  \ \ \text{eq. (1)}\\
x-y=-1   \ \ \text{eq. (2)}
\end{matrix}
$$

  미지수가 $x,y$ 두 개 (2원), 식도 2개!

## 1.2. 대입법 풀이 (손으로 풀이)

- 식 (2)를 바꿔서
  $$y=x+1$$
  이라 정리되고, 이를 다시 식 (1)에 대입하면,

- 식 (1)이

$$2x+(x+1)=5$$

로 바뀌고

$$3x=4\rightarrow x=4/3$$

따라서

$$y=4/3+1=7/3$$

- 주어진 연립방정식을 만족하는 $$(x,y)$$ 짝을 완성

$$
x=4/3, y=7/3
$$

## 1.3. 가감법 풀이 (덧셈이나 뺄셈을 활용해 손으로 풀이)

- 식 (1)+식(2) 혹은 식 (1) - 식(2) 등을 활용

- 식 (1)과 식(2)를 더하면

$$
3x=4
$$

따라서 $x$와 $y$를 이어 구할 수 있다.

## 1.4. 기하학적 의미

2원 1차 연립 방정식에서 각 방정식은 각기 다른 '직선'을 의미

$$
2x+y=5 \rightarrow y=-2x+5
$$

$$
x-y=-1 \rightarrow y=x+1
$$

두 직선의 교점 $(x,y)=(3/4,7/3)$

```python
import matplotlib.pyplot as plt
import numpy as np

## the two lines
def y1(x): return 5-2*x
def y2(x): return x+1

xs=np.linspace(-2,4) ## -10~10 범위 내의 선 그리기
plt.plot(xs,y1(xs),'r-',label='Line 1')
plt.plot(xs,y2(xs),'b-',label='Line 2')

xy=(4/3,7/3) # actual solution
plt.plot(*xy,marker='+',mfc='None',mec='k',ms=10)

# deco
plt.legend()
```

# 2. 3원 연립 방정식

$$
\begin{matrix}
2x+y+z=5  \ \ \text{eq. (1)}\\
x-y-z=-1   \ \ \text{eq. (2)}\\
x+5y+2z=0 \ \ \text{eq. (3)}
\end{matrix}
$$

- 미지수가 $x,y,z$ 세 개 (3원), 식도 3개!

- 기하학적 의미? 서로 다른 세 면이 만나는 점.

```python
import matplotlib.pyplot as plt
import numpy as np
%matplotlib widget

def z1(x,y):
  return 5-2*x-y
def z2(x,y):
  return x-y+1
def z3(x,y):
  return (-x-5*y)/2.

nres=10
x=np.linspace(-10,10,nres)
y=np.linspace(-10,10,nres)
xx,yy=np.meshgrid(x,y)
zz1=z1(xx,yy)
zz2=z2(xx,yy)
zz3=z3(xx,yy)

fig=plt.figure()
ax1=fig.add_subplot(projection='3d')
kws=dict(alpha=0.5)
ax1.plot_surface(xx,yy,zz1,color='r',**kws)
ax1.plot_surface(xx,yy,zz2,color='g',**kws)
ax1.plot_surface(xx,yy,zz3,color='b',**kws)

## actual point
xyz=1.3333333,-2, 4.3333333
ax1.scatter(*xyz,color='k',marker='o')
  ```

# 3. 행렬을 활용한 풀이

## 3.1. 2원 연립 방정식을 행렬식으로 표현

- 우선 풀이를 위해서는 연립 방정식을 행렬의 형태로 바꿔야 한다.

$$
\begin{matrix}
2x+y=5  \ \ \text{eq. (1)}\\
x-y=-1   \ \ \text{eq. (2)}
\end{matrix}
$$

을 다음의 행렬 형태로 바꾸자.

$$
\begin{bmatrix}
2& 1\\
1&-1\\
\end{bmatrix}
\begin{bmatrix}
x\\
y
4. \end{bmatrix}
=
\begin{bmatrix}
5\\
-1
\end{bmatrix}
$$


## 3.2. 3원 연립 방정식을 행렬식으로 표현

- 우선 풀이를 위해서는 연립 방정식을 행렬의 형태로 바꿔야 한다.

$$
\begin{matrix}
2x+y+z=5  \ \ \text{eq. (1)}\\
x-y-z=-1   \ \ \text{eq. (2)}\\
x+z=3 \ \ \text{eq. (3)}
\end{matrix}
$$

을 다음의 행렬 형태로 바꾸자.

$$
\begin{bmatrix}
2& 1 & 1\\
1&-1 & -1\\
1& 0 & 1
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
z
5. \end{bmatrix}
=
\begin{bmatrix}
5\\
-1\\
3
\end{bmatrix}
$$

위처럼 연립 방정식을 행렬의 형태로 바꿔서 풀이할 수 있다. 따라서 연립 방정식을
행렬 형태로 바꾸는 연습이 필요.

# 4. 예시

## 4.1. 아래 연립 방정식을 행렬의 형태로 바꿔보세요.

- 아래 연립 방정식을 행렬의 형태로 바꿔보세요.

    $$
    \begin{matrix}
    x-5=y  \\
    y-3x+3=0 \\
    \end{matrix}
    $$

- 답

    $$
    \begin{bmatrix}
    1&-1\\
    -3&1\\
    \end{bmatrix}
    \begin{bmatrix}
    x\\
    y\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    5\\
    -3\\
    \end{bmatrix}
    $$

## 4.2. 아래 연립 방정식을 행렬의 형태로 바꿔보세요.

- 아래 연립 방정식을 행렬의 형태로 바꿔보세요.

    $$
    \begin{matrix}
    x=y  \\
    y=3+x
    \end{matrix}
    $$

- 답

    $$
    \begin{bmatrix}
    1&-1\\
    1&-1\\
    \end{bmatrix}
    \begin{bmatrix}
    x\\
    y \\
    \end{bmatrix}
    =
    \begin{bmatrix}
    0\\
    -3 \\
    \end{bmatrix}
    $$

- 하나의 형태로만 답이 나오는 건 아니다. 예를 들어 위의 경우

    $$
    \begin{bmatrix}
    1&-1\\
    -1&1\\
    \end{bmatrix}
    \begin{bmatrix}
    x\\
    y \\
    \end{bmatrix}
    =
    \begin{bmatrix}
    0\\
    3
    \end{bmatrix}
    $$

으로 표기될 수 있습니다. 하지만 형태가 다르더라도 정답은 동일하게 도출됩니다.

- 그리고 위의 경우에는 해가 없습니다!! 왜 그럴까요?

## 4.3. 해가 없는 경우?

$$
\begin{matrix}
2x+y=5  \ \ \text{eq. (1)}\\
2x+y=-1   \ \ \text{eq. (2)}
\end{matrix}
$$

- 위 연립방정식을 만족하는 해는 없습니다. 왜 그럴까요?
- 행렬을 보고 해가 없는 경우를 '판별'할 수 있을까요?

## 4.4. 판별식

- 판별(determination)하기 위해 우리는 '판별값' 혹은 '판별식'이라고 불리는 [determinant](https://ko.wikipedia.org/wiki/행렬식)를
구해서 알 수 있다.

- 예를 들어, 2x2행렬의 경우

$$
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
$$

의 판별값을 아래와 같이 표기한다.

$$
\begin{vmatrix}
a & b\\
c & d
\end{vmatrix}
=ad-bc
$$

- 3x3행렬의 경우

$$
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
$$

의 판별값을 아래와 같이 표기한다.

$$
\begin{vmatrix}
a & b & c \\
d&e&f\\
g&h&i
\end{vmatrix}
=aei+bfg+cdh-ceg-bdi-afh
$$

# 5. 행렬로 표현된 연립방정식의 풀이

- 행렬로 표현된 연립방정식은 여러 '규칙성'을 가진 알고리듬을 통해 그 해를 구할 수 있습니다.

    - 행렬로 표현된 수식을 풀이하는 방법은 크게 2가지로 나뉠 수 있음.
    * 직접해법 (direct method)
      - [가우스 소거법 (Gauss elimination)](https://ko.wikipedia.org/wiki/가우스_소거법)
      - [LU 분해법 (Low and Upper triangle decomposition)](https://ko.wikipedia.org/wiki/LU_분해)
      - 수치 안정성이 높음
    * 반복해법 (iterative method)
      - Jacobi method
      - Gauss-Seidel method
      - 반복해법은 발산하는 경우가 더러 있음. 항상 해를 찾을 수 있지 않음. 따라서 수치안정성이 낮음
