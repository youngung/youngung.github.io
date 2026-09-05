---
layout: page
title: 수치해석
description: 재료공학도를 위한 수치해석
target: 2학년 1학기
permalink:
prerequisite: 재료공학개론1, 데이터 재료과학
toc:
  sidebar: left
---

- [1. 학습 목표](#1-학습-목표)
- [2. 선형 연립방정식](#2-선형-연립방정식)
  - [2.1. 2원 연립방정식](#21-2원-연립방정식)
  - [2.2. 손으로 풀이하기](#22-손으로-풀이하기)
  - [2.3. 기하학적 의미](#23-기하학적-의미)
- [3. 3원 연립방정식](#3-3원-연립방정식)
- [4. 행렬 형태로 표현하기](#4-행렬-형태로-표현하기)
  - [4.1. 2원 연립방정식](#41-2원-연립방정식)
- [\\end{bmatrix}}\_{\\boldsymbol x}](#endbmatrix_boldsymbol-x)
  - [4.2. 3원 연립방정식](#42-3원-연립방정식)
- [\\end{bmatrix}](#endbmatrix)
- [5. 해의 개수](#5-해의-개수)
  - [5.1. 유일한 해](#51-유일한-해)
  - [5.2. 해가 없는 경우](#52-해가-없는-경우)
  - [5.3. 해가 무한히 많은 경우](#53-해가-무한히-많은-경우)
- [6. 행렬식](#6-행렬식)
  - [6.1. 2×2 행렬식](#61-22-행렬식)
  - [6.2. 3×3 행렬식](#62-33-행렬식)
- [7. NumPy로 풀이하기](#7-numpy로-풀이하기)
- [8. 연립방정식의 수치해법](#8-연립방정식의-수치해법)
- [9. 정리](#9-정리)
- [10. 연습 문제](#10-연습-문제)
- [\\end{bmatrix}](#endbmatrix-1)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 선형 연립방정식을 행렬 형태 $\boldsymbol A\boldsymbol x=\boldsymbol b$로 나타낼 수 있다.
- 계수행렬, 미지수 벡터와 우변 벡터를 구분할 수 있다.
- 2원 연립방정식의 해를 대수적·기하학적으로 설명할 수 있다.
- 행렬식을 계산하고 유일한 해의 존재 여부를 판단할 수 있다.
- 해가 하나인 경우, 없는 경우와 무한히 많은 경우를 구분할 수 있다.
- NumPy로 연립방정식을 풀고 잔차를 확인할 수 있다.

# 2. 선형 연립방정식

각 미지수가 모두 1차로만 나타나는 여러 방정식을 함께 만족시키는 값을 찾는 문제를
선형 연립방정식(system of linear equations)이라고 한다. 예를 들어 다음 식에는
미지수 $x,y$가 곱해진 $xy$, 제곱된 $x^2$, 또는 $\sin x$ 같은 항이 없다.

$$
\begin{aligned}
2x+y&=5,\\
x-y&=-1.
\end{aligned}
$$

## 2.1. 2원 연립방정식

미지수가 $x,y$ 두 개이고 서로 독립적인 식이 두 개 있는 경우를 생각해보자.

$$
\begin{aligned}
2x+y&=5 &&\text{식 (1)},\\
x-y&=-1 &&\text{식 (2)}.
\end{aligned}
$$

## 2.2. 손으로 풀이하기

식 (2)를 $y$에 대해 정리하면

$$
y=x+1
$$

이다. 이를 식 (1)에 대입하면

$$
2x+(x+1)=5
$$

이므로

$$
3x=4,
\qquad
x=\frac{4}{3}
$$

이다. 다시 $y=x+1$에 대입하면

$$
y=\frac{4}{3}+1=\frac{7}{3}
$$

이다. 따라서 해는

$$
\boxed{
(x,y)=\left(\frac{4}{3},\frac{7}{3}\right)
}
$$

이다. 두 식을 직접 더해 $3x=4$를 얻는 가감법으로도 같은 해를 구할 수 있다.

## 2.3. 기하학적 의미

2원 선형방정식 하나는 $xy$ 평면에서 하나의 직선을 나타낸다.

$$
2x+y=5
\quad\Longrightarrow\quad
y=-2x+5
$$

$$
x-y=-1
\quad\Longrightarrow\quad
y=x+1
$$

두 직선의 교점은 연립방정식의 해

$$
\left(\frac{4}{3},\frac{7}{3}\right)
$$

이다.

~~~python
import numpy as np
import matplotlib.pyplot as plt

def y1(x):
    return 5-2*x

def y2(x):
    return x+1

x = np.linspace(-2, 4, 200)
solution = (4/3, 7/3)

plt.plot(x, y1(x), "r-", label=r"$2x+y=5$")
plt.plot(x, y2(x), "b-", label=r"$x-y=-1$")
plt.plot(*solution, "ko", label="solution")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
~~~

# 3. 3원 연립방정식

미지수가 세 개인 선형 연립방정식의 예는 다음과 같다.

$$
\begin{aligned}
2x+y+z&=5,\\
x-y-z&=-1,\\
x+5y+2z&=0.
\end{aligned}
$$

각 식은 3차원 공간에서 하나의 평면을 나타낸다. 세 평면이 한 점에서 만나면 그
교점이 연립방정식의 유일한 해이다. 위 식의 해는

$$
(x,y,z)=\left(\frac{4}{3},-2,\frac{13}{3}\right)
$$

이다.

~~~python
def z1(x, y):
    return 5-2*x-y

def z2(x, y):
    return x-y+1

def z3(x, y):
    return (-x-5*y)/2

grid = np.linspace(-4, 4, 20)
xx, yy = np.meshgrid(grid, grid)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection="3d")

ax.plot_surface(xx, yy, z1(xx, yy), color="red", alpha=0.35)
ax.plot_surface(xx, yy, z2(xx, yy), color="green", alpha=0.35)
ax.plot_surface(xx, yy, z3(xx, yy), color="blue", alpha=0.35)
ax.scatter(4/3, -2, 13/3, color="black", s=50, label="solution")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()
plt.show()
~~~

# 4. 행렬 형태로 표현하기

$n$개의 미지수를 갖는 $n$개의 선형방정식은 다음과 같이 간단히 나타낼 수 있다.

$$
\boxed{
\boldsymbol A \cdot \boldsymbol x=\boldsymbol b
}
$$

- $\boldsymbol A$: 계수행렬(coefficient matrix)
- $\boldsymbol x$: 미지수 벡터
- $\boldsymbol b$: 우변 벡터

$\boldsymbol A$가 $n\times n$ 행렬이면 $\boldsymbol x$와 $\boldsymbol b$는
각각 $n$개의 성분을 갖는 벡터이다.

## 4.1. 2원 연립방정식

$$
\begin{aligned}
2x+y&=5,\\
x-y&=-1
\end{aligned}
$$

을 행렬 형태로 나타내면

$$
\underbrace{
\begin{bmatrix}
2&1\\
1&-1
\end{bmatrix}}_{\boldsymbol A}
\underbrace{
\begin{bmatrix}
x\\y
\end{bmatrix}}_{\boldsymbol x}
=
\underbrace{
\begin{bmatrix}
5\\-1
\end{bmatrix}}_{\boldsymbol b}
$$

이다. 행렬의 첫 번째 행과 벡터를 곱하면 첫 번째 방정식 $2x+y=5$가 된다.

## 4.2. 3원 연립방정식

$$
\begin{aligned}
2x+y+z&=5,\\
x-y-z&=-1,\\
x+z&=3
\end{aligned}
$$

은 다음과 같이 표현된다.

$$
\begin{bmatrix}
2&1&1\\
1&-1&-1\\
1&0&1
\end{bmatrix}
\begin{bmatrix}
x\\y\\z
\end{bmatrix}
=
\begin{bmatrix}
5\\-1\\3
\end{bmatrix}
$$

어떤 미지수가 식에 나타나지 않으면 해당 계수에 0을 쓴다. 예를 들어 세 번째
방정식에는 $y$가 없으므로 $A_{32}=0$이다.

# 5. 해의 개수

2원 선형 연립방정식은 두 직선의 관계에 따라 세 가지 경우로 나뉜다.

## 5.1. 유일한 해

두 직선이 한 점에서 만나면 해가 하나이다.

$$
\begin{aligned}
2x+y&=5,\\
x-y&=-1.
\end{aligned}
$$

## 5.2. 해가 없는 경우

다음 두 직선은 기울기가 같고 절편이 다르므로 평행하다.

$$
\begin{aligned}
2x+y&=5,\\
2x+y&=-1.
\end{aligned}
$$

동일한 $2x+y$가 동시에 5와 $-1$이 될 수 없으므로 해가 없다.

또 다른 예를 살펴보자.

$$
\begin{aligned}
x-y&=0,\\
-x+y&=3.
\end{aligned}
$$

첫 번째 식에 $-1$을 곱하면 $-x+y=0$이므로 두 번째 식과 모순된다. 따라서 해가 없다.

## 5.3. 해가 무한히 많은 경우

두 식이 같은 직선을 나타내면 그 직선 위의 모든 점이 해이다.

$$
\begin{aligned}
x-y&=0,\\
-2x+2y&=0.
\end{aligned}
$$

두 번째 식은 첫 번째 식에 $-2$를 곱한 것이므로 독립적인 새로운 조건을 주지 않는다.

# 6. 행렬식

행렬식(determinant)은 정사각행렬에 대응하는 하나의 수이며
$\det(\boldsymbol A)$ 또는 $|\boldsymbol A|$로 표기한다.

정사각 연립방정식 $\boldsymbol A\boldsymbol x=\boldsymbol b$에서

$$
\det(\boldsymbol A)\ne0
$$

이면 유일한 해가 존재한다. 반면

$$
\det(\boldsymbol A)=0
$$

이면 유일한 해가 없다. 이때는 **해가 없거나 해가 무한히 많을 수 있으므로**
행렬식만으로 두 경우를 구분할 수 없다. 방정식 사이의 관계 또는 확대행렬의
행 연산을 추가로 살펴봐야 한다.

## 6.1. 2×2 행렬식

$$
\boldsymbol A=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
$$

이면

$$
\det(\boldsymbol A)=ad-bc
$$

이다. 앞의 예제에서는

$$
\det
\begin{bmatrix}
2&1\\
1&-1
\end{bmatrix}
=2(-1)-1(1)=-3\ne0
$$

이므로 유일한 해가 존재한다.

## 6.2. 3×3 행렬식

$$
\boldsymbol A=
\begin{bmatrix}
a&b&c\\
d&e&f\\
g&h&i
\end{bmatrix}
$$

이면 첫 번째 행을 따라 전개하여

$$
\det(\boldsymbol A)
=a(ei-fh)-b(di-fg)+c(dh-eg)
$$

을 얻는다.

# 7. NumPy로 풀이하기

NumPy에서는 역행렬을 직접 계산하여 곱하기보다 **np.linalg.solve**를 사용하는
것이 더 효율적이고 일반적으로 더 정확하다.

~~~python
import numpy as np

A = np.array([
    [2.0,  1.0],
    [1.0, -1.0],
])
b = np.array([5.0, -1.0])

x = np.linalg.solve(A, b)

print("solution:", x)
print("A @ x:", A @ x)
print("b:", b)
~~~

계산 결과는 다음과 같다.

~~~text
solution: [1.33333333 2.33333333]
A @ x: [ 5. -1.]
b: [ 5. -1.]
~~~

계산된 해가 방정식을 얼마나 잘 만족하는지는 잔차 벡터로 확인할 수 있다.

$$
\boldsymbol r=\boldsymbol A\boldsymbol x-\boldsymbol b
$$

~~~python
residual = A@x-b
print("residual:", residual)
print("residual norm:", np.linalg.norm(residual))
~~~

정확한 산술에서는 잔차가 영벡터이다. 부동소수점 계산에서는 매우 작은 값이 남을 수 있다.

# 8. 연립방정식의 수치해법

행렬로 표현된 연립방정식은 여러 알고리듬으로 풀 수 있다.

- 직접해법(direct method)
  - 가우스 소거법
  - LU 분해
  - 유한한 단계의 연산으로 해를 구한다.
  - 실제 계산에서는 수치 안정성을 위해 피벗팅이 필요할 수 있다.
- 반복해법(iterative method)
  - Jacobi 방법
  - Gauss–Seidel 방법
  - 초기값에서 시작하여 해를 반복적으로 개선한다.
  - 행렬의 성질과 알고리듬에 따라 수렴하거나 발산할 수 있다.

다음 강의에서는 가우스 소거법으로 $\boldsymbol A\boldsymbol x=\boldsymbol b$를
직접 푸는 과정을 살펴본다.

# 9. 정리

- 선형 연립방정식은 $\boldsymbol A\boldsymbol x=\boldsymbol b$로 표현할 수 있다.
- 2원 연립방정식의 해는 두 직선의 교점이다.
- $\det(\boldsymbol A)\ne0$이면 정사각 연립방정식은 유일한 해를 갖는다.
- $\det(\boldsymbol A)=0$이면 해가 없거나 무한히 많을 수 있다.
- NumPy의 **np.linalg.solve**로 해를 계산하고 잔차로 결과를 확인할 수 있다.
- 가우스 소거법과 LU 분해는 대표적인 직접해법이다.

# 10. 연습 문제

강의에서 다룬 개념과 계산을 확인하는 기초 문제이다.

1. 다음 중 선형방정식을 모두 고르라.

   1. $2x+3y=4$
   2. $x^2+y=1$
   3. $xy=2$
   4. $x-y+z=0$

   <!--
   풀이 및 정답:
   1번과 4번이다. 2번에는 x의 제곱이 있고, 3번에는 두 미지수의 곱이 있으므로
   선형방정식이 아니다.
   -->

2. 다음 연립방정식을 $\boldsymbol A\boldsymbol x=\boldsymbol b$ 형태로 나타내라.

   $$
   \begin{aligned}
   3x+2y&=7,\\
   x-y&=1.
   \end{aligned}
   $$

   <!--
   풀이 및 정답:
   A=[[3,2],[1,-1]], x=[x,y]^T, b=[7,1]^T이다.
   즉 [[3,2],[1,-1]][x,y]^T=[7,1]^T이다.
   -->

3. 다음 행렬 곱을 두 개의 방정식으로 바꾸어라.

   $$
   \begin{bmatrix}
   1&2\\
   3&-1
   \end{bmatrix}
   \begin{bmatrix}
   x\\y
   \end{bmatrix}
   =
   \begin{bmatrix}
   5\\4
   \end{bmatrix}.
   $$

   <!--
   풀이 및 정답:
   첫 번째 행에서 x+2y=5, 두 번째 행에서 3x-y=4를 얻는다.
   -->

4. 다음 연립방정식을 대입법 또는 가감법으로 풀어라.

   $$
   \begin{aligned}
   x+y&=5,\\
   x-y&=1.
   \end{aligned}
   $$

   <!--
   풀이 및 정답:
   두 식을 더하면 2x=6이므로 x=3이다. 첫 번째 식에 대입하면 y=2이다.
   따라서 해는 (3,2)이다.
   -->

5. 다음 행렬의 행렬식을 계산하고 유일한 해의 존재 여부를 판단하라.

   $$
   \boldsymbol A=
   \begin{bmatrix}
   2&1\\
   1&3
   \end{bmatrix}.
   $$

   <!--
   풀이 및 정답:
   det(A)=2×3-1×1=5이다. det(A)가 0이 아니므로 Ax=b는 임의의 b에 대해
   유일한 해를 갖는다.
   -->

6. 다음 연립방정식의 해가 하나인지, 없는지, 무한히 많은지 판단하라.

   1. $x+y=2$, $x-y=0$
   2. $x-y=0$, $-x+y=3$
   3. $x-y=0$, $-2x+2y=0$

   <!--
   풀이 및 정답:
   1번은 두 직선이 한 점에서 만나므로 해가 하나이며 (x,y)=(1,1)이다.
   2번은 서로 모순되는 평행한 직선이므로 해가 없다.
   3번은 두 식이 같은 직선을 나타내므로 해가 무한히 많다.
   -->

7. 3원 연립방정식

   $$
   \begin{aligned}
   x+y+z&=6,\\
   2x-y+z&=3,\\
   x+2y-z&=2
   \end{aligned}
   $$

   의 계수행렬 $\boldsymbol A$, 미지수 벡터 $\boldsymbol x$와 우변 벡터
   $\boldsymbol b$를 각각 적어라.

   <!--
   풀이 및 정답:
   A=[[1,1,1],[2,-1,1],[1,2,-1]], x=[x,y,z]^T, b=[6,3,2]^T이다.
   -->

8. 다음 코드의 빈칸을 채워 연립방정식을 풀어라.

   ~~~python
   A = np.array([[2.0, 1.0],
                 [1.0, 3.0]])
   b = np.array([5.0, 7.0])

   x = np.linalg.________(A, b)
   print(x)
   ~~~

   <!--
   풀이 및 정답:
   빈칸은 solve이다. 해는 x=[1.6, 1.8]이다.
   첫 번째 식은 2×1.6+1.8=5이고 두 번째 식은 1.6+3×1.8=7이다.
   -->

9. 계산된 해가 $\boldsymbol x=(1,2)$이고

   $$
   \boldsymbol A=
   \begin{bmatrix}
   2&1\\
   1&-1
   \end{bmatrix},
   \qquad
   \boldsymbol b=
   \begin{bmatrix}
   4\\-1
   \end{bmatrix}
   $$

   일 때 잔차 $\boldsymbol r=\boldsymbol A\boldsymbol x-\boldsymbol b$를 구하라.

   <!--
   풀이 및 정답:
   Ax=[2×1+1×2, 1×1-1×2]^T=[4,-1]^T=b이므로 r=[0,0]^T이다.
   -->

10. 다음 방법을 직접해법과 반복해법으로 분류하라.

    - 가우스 소거법
    - LU 분해
    - Jacobi 방법
    - Gauss–Seidel 방법

    <!--
    풀이 및 정답:
    가우스 소거법과 LU 분해는 직접해법이다.
    Jacobi 방법과 Gauss–Seidel 방법은 반복해법이다.
    -->
