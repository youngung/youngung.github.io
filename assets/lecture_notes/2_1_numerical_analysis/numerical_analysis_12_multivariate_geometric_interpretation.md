---
layout: page
title: 다변수 Newton–Raphson 방법의 기하학적 해석
description: 영점 곡선과 선형화를 이용한 다변수 Newton–Raphson 방법의 이해
target: 2학년 1학기
permalink:
prerequisite: 다변수 Newton–Raphson 방법
toc:
  sidebar: left
---

- [1. 학습 목표](#1-학습-목표)
- [2. 연립 비선형방정식의 기하학적 의미](#2-연립-비선형방정식의-기하학적-의미)
- [3. Jacobian 행렬의 기하학적 의미](#3-jacobian-행렬의-기하학적-의미)
- [4. Newton 보정량의 기하학적 의미](#4-newton-보정량의-기하학적-의미)
- [5. Python 시각화](#5-python-시각화)
- [6. 주의할 점](#6-주의할-점)
- [7. 연습문제](#7-연습문제)

# 1. 학습 목표

- 두 비선형방정식의 해를 두 영점 곡선의 교점으로 해석할 수 있다.
- Jacobian 행렬의 각 행을 영점 곡선의 법선벡터와 연결할 수 있다.
- Newton 보정량을 선형화된 두 방정식의 교점으로 이동시키는 양으로 설명할 수 있다.

# 2. 연립 비선형방정식의 기하학적 의미

다음 연립방정식을 생각하자.

$$
\begin{aligned}
f_1(x,y) &= x^2+y^2-5=0,\\
f_2(x,y) &= x-y-1=0.
\end{aligned}
$$

$f_1=0$은 원점 중심, 반지름 $\sqrt{5}$인 원이고, $f_2=0$은 직선 $y=x-1$이다.
따라서 연립방정식의 해는 두 곡선의 교점 $(2,1)$과 $(-1,-2)$이다.

# 3. Jacobian 행렬의 기하학적 의미

각 함수의 gradient는 해당 함수의 등고선에 수직이다.

$$
\nabla f_i(\mathbf x)=
\begin{bmatrix}
\partial f_i/\partial x\\
\partial f_i/\partial y
\end{bmatrix},
\qquad
\mathbf J(\mathbf x)=
\begin{bmatrix}
\nabla f_1(\mathbf x)^T\\
\nabla f_2(\mathbf x)^T
\end{bmatrix}.
$$

예제에서는

$$
\mathbf J(x,y)=
\begin{bmatrix}
2x & 2y\\
1 & -1
\end{bmatrix}.
$$

첫 번째 행은 원의 등고선에 수직인 방향을, 두 번째 행은 직선에 수직인 방향을 나타낸다.

# 4. Newton 보정량의 기하학적 의미

현재 추정값 $\mathbf x^{(k)}$에서 각 함수를 1차 Taylor 전개하면

$$
f_i(\mathbf x^{(k)}+\Delta\mathbf x)
\approx f_i(\mathbf x^{(k)})
+\nabla f_i(\mathbf x^{(k)})^T\Delta\mathbf x
$$

이다. 선형화된 두 식을 동시에 0으로 두면

$$
\mathbf J(\mathbf x^{(k)})\Delta\mathbf x
=-\mathbf F(\mathbf x^{(k)})
$$

을 얻는다. 즉, $\mathbf x^{(k+1)}=\mathbf x^{(k)}+\Delta\mathbf x$는
현재 점에서 선형화한 두 영점 곡선의 교점이다.

## 4.1. 첫 번째 반복을 직접 계산하기

$\mathbf x^{(0)}=(1.5,0.5)^T$이면

$$
\mathbf F(\mathbf x^{(0)})=
\begin{bmatrix}-2.5\\0\end{bmatrix},
\qquad
\mathbf J(\mathbf x^{(0)})=
\begin{bmatrix}3&1\\1&-1\end{bmatrix}.
$$

$\mathbf J\Delta\mathbf x=-\mathbf F$를 풀면
$\Delta x=\Delta y=0.625$이다. 그러므로

$$
\mathbf x^{(1)}
=
\begin{bmatrix}1.5\\0.5\end{bmatrix}
+
\begin{bmatrix}0.625\\0.625\end{bmatrix}
=
\begin{bmatrix}2.125\\1.125\end{bmatrix}
$$

이며, 정확한 해 $(2,1)$에 더 가까워졌다.

# 5. Python 시각화

## 5.1. 영점 곡선과 반복 경로

~~~python
import numpy as np
import matplotlib.pyplot as plt

def F(point):
    x, y = point
    return np.array([x**2 + y**2 - 5.0, x - y - 1.0])

def J(point):
    x, y = point
    return np.array([[2.0*x, 2.0*y], [1.0, -1.0]])

point = np.array([1.5, 0.5])
history = [point.copy()]

for _ in range(6):
    delta = np.linalg.solve(J(point), -F(point))
    point = point + delta
    history.append(point.copy())

history = np.asarray(history)
x = np.linspace(-3.0, 3.0, 401)
y = np.linspace(-3.0, 3.0, 401)
X, Y = np.meshgrid(x, y)
Z1 = X**2 + Y**2 - 5.0
Z2 = X - Y - 1.0

fig, ax = plt.subplots(figsize=(7, 7))
ax.contour(X, Y, Z1, levels=[0], colors="tab:blue", linewidths=2)
ax.contour(X, Y, Z2, levels=[0], colors="tab:orange", linewidths=2)
ax.plot(history[:, 0], history[:, 1], "ko--", label="Newton iterations")

for k, (xk, yk) in enumerate(history):
    ax.annotate(str(k), (xk, yk), xytext=(5, 5),
                textcoords="offset points")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)
ax.legend()
plt.show()
~~~

## 5.2. 3차원 곡면과 $z=0$ 평면

두 식을 $z=f_1(x,y)$와 $z=f_2(x,y)$인 곡면으로 그리면,
각 곡면과 $z=0$ 평면의 교선이 영점 곡선이다.

~~~python
fig = plt.figure(figsize=(11, 5))

for index, (Z, title, color) in enumerate([
    (Z1, "z = f1(x, y)", "tab:blue"),
    (Z2, "z = f2(x, y)", "tab:orange"),
], start=1):
    ax = fig.add_subplot(1, 2, index, projection="3d")
    ax.plot_surface(X, Y, Z, color=color, alpha=0.65,
                    rstride=8, cstride=8)
    ax.plot_surface(X, Y, np.zeros_like(X), color="gray", alpha=0.25)
    ax.contour(X, Y, Z, levels=[0], zdir="z", offset=0,
               colors="black", linewidths=2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(title)

plt.tight_layout()
plt.show()
~~~

# 6. 주의할 점

- 두 gradient가 거의 평행하면 Jacobian 행렬이 특이하거나 매우 불안정해질 수 있다.
- 초깃값에 따라 서로 다른 해로 수렴하거나 수렴하지 않을 수 있다.
- 실제 계산에서는 역행렬을 직접 구하지 않고 <code>np.linalg.solve(J, -F)</code>로 보정량을 계산한다.
- $\|\mathbf F(\mathbf x^{(k)})\|_2$와 $\|\Delta\mathbf x\|_2$를 함께 확인하면 수렴 여부를 더 안전하게 판단할 수 있다.

# 7. 연습문제

## 연습문제 1

$f_1(x,y)=x^2+y^2-5=0$이 나타내는 도형의 중심과 반지름을 구하라.

<!--
풀이와 해답:
중심은 (0,0)이고 반지름은 sqrt(5)이다.
-->

## 연습문제 2

$f_2(x,y)=x-y-1=0$을 $y=ax+b$의 형태로 나타내라.

<!--
풀이와 해답:
y=x-1이므로 a=1, b=-1이다.
-->

## 연습문제 3

점 $(2,1)$을 $f_1$과 $f_2$에 대입하여 연립방정식의 해인지 확인하라.

<!--
풀이와 해답:
f1(2,1)=4+1-5=0이고 f2(2,1)=2-1-1=0이므로 해이다.
-->

## 연습문제 4

$f_1(x,y)=x^2+y^2-5$의 gradient $\nabla f_1(x,y)$를 구하라.

<!--
풀이와 해답:
각 변수로 편미분하면 nabla f1=(2x, 2y)^T이다.
-->

## 연습문제 5

$\mathbf x^{(0)}=(1.5,0.5)^T$에서 $f_2=0$인지 확인하라.

<!--
풀이와 해답:
f2(1.5,0.5)=1.5-0.5-1=0이므로 f2의 영점 직선 위에 있다.
-->

## 연습문제 6

첫 Newton 보정량이 $(0.625,0.625)^T$일 때 $\mathbf x^{(1)}$을 구하라.

<!--
풀이와 해답:
(1.5,0.5)^T+(0.625,0.625)^T=(2.125,1.125)^T이다.
-->

## 연습문제 7

Jacobian 행렬의 두 행이 거의 같은 방향을 가리킬 때 계산이 어려워지는 이유를 한 문장으로 설명하라.

<!--
풀이와 해답:
두 행이 거의 선형종속이 되어 Jacobian이 특이행렬에 가까워지고 보정량이 오차에 매우 민감해지기 때문이다.
-->
