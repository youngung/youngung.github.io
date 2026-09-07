---
layout: distill
title: Matplotlib 기초 2
description: 여러 그래프와 로그축, 오차막대 및 3차원 그래프
target: 1학년 2학기
permalink:
featured: true
prerequisite: Matplotlib 기초 1, 벡터 연산 기초
toc:
  sidebar: left
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

- [1. 학습 목표](#1-학습-목표)
- [2. 여러 그래프 배치하기](#2-여러-그래프-배치하기)
- [3. 선과 점의 모양 바꾸기](#3-선과-점의-모양-바꾸기)
- [4. 로그축](#4-로그축)
- [5. 오차막대](#5-오차막대)
- [6. 2차원 색상 그래프](#6-2차원-색상-그래프)
- [7. 3차원 그래프](#7-3차원-그래프)
  - [7.1. meshgrid로 2차원 함수 계산하기](#71-meshgrid로-2차원-함수-계산하기)
  - [7.2. 3차원 mesh 그리기](#72-3차원-mesh-그리기)
  - [7.3. 등고선으로 표현하기](#73-등고선으로-표현하기)
- [8. 재료공학 예제: 결정방향](#8-재료공학-예제-결정방향)
- [9. 자주 하는 실수](#9-자주-하는-실수)
- [10. 정리](#10-정리)
- [11. 쉬운 연습 문제](#11-쉬운-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)

# 1. 학습 목표

- 하나의 Figure에 여러 Axes를 배치할 수 있다.
- 선의 종류, 색과 표식을 구분하여 데이터를 비교할 수 있다.
- 값의 범위가 매우 넓을 때 로그축을 사용할 수 있다.
- 평균값과 측정 불확실성을 오차막대로 나타낼 수 있다.
- 2차원 색상 그래프와 간단한 3차원 그래프를 그릴 수 있다.
- 결정방향을 단위벡터로 바꾸어 3차원 공간에 표현할 수 있다.

# 2. 여러 그래프 배치하기

서로 단위나 크기가 다른 데이터를 한 Axes에 겹치면 읽기 어려울 수 있다.
<code>plt.subplots()</code>에 행과 열의 개수를 지정해 여러 Axes를 배치하자.

~~~python
import numpy as np
import matplotlib.pyplot as plt

temperature = np.array([300, 400, 500, 600, 700])
strength = np.array([315, 302, 284, 258, 225])
elongation = np.array([12, 14, 17, 21, 26])

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(temperature, strength, marker="o")
axes[0].set_xlabel("Temperature (K)")
axes[0].set_ylabel("Yield strength (MPa)")
axes[0].grid(True, alpha=0.3)

axes[1].plot(temperature, elongation, marker="s", color="tab:orange")
axes[1].set_xlabel("Temperature (K)")
axes[1].set_ylabel("Elongation (%)")
axes[1].grid(True, alpha=0.3)

fig.suptitle("Mechanical Properties")
fig.tight_layout()
plt.show()
~~~

# 3. 선과 점의 모양 바꾸기

색만으로 데이터를 구분하지 말고 선의 종류와 표식도 함께 다르게 지정하자.

~~~python
strain = np.linspace(0.0, 0.01, 101)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(strain, 70_000 * strain, linestyle="-", label="Al")
ax.plot(strain, 210_000 * strain, linestyle="--", label="Fe")
ax.set_xlabel("Strain")
ax.set_ylabel("Stress (MPa)")
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
~~~

대표적인 선 종류는 실선 <code>"-"</code>, 파선 <code>"--"</code>, 점선
<code>":"</code>이고, 표식에는 원 <code>"o"</code>, 사각형 <code>"s"</code>,
삼각형 <code>"^"</code> 등이 있다.

# 4. 로그축

확산계수처럼 여러 자릿수에 걸쳐 변하는 값에는 로그축(logarithmic scale)이 유용하다.

~~~python
temperature = np.array([700, 800, 900, 1000, 1100])
diffusivity = np.array([2.0e-17, 3.0e-15, 1.2e-13, 2.1e-12, 1.8e-11])

fig, ax = plt.subplots(figsize=(6, 4))
ax.semilogy(temperature, diffusivity, marker="o")
ax.set_xlabel("Temperature (K)")
ax.set_ylabel(r"Diffusivity ($m^2/s$)")
ax.grid(True, which="both", alpha=0.3)
fig.tight_layout()
plt.show()
~~~

<code>ax.semilogy()</code>는 $y$축만 로그축으로 만든다. 로그축에는 0이나 음수를
표시할 수 없다.

# 5. 오차막대

같은 조건에서 여러 번 측정했다면 평균값과 데이터의 퍼짐을 함께 표현한다.

~~~python
temperature = np.array([300, 400, 500, 600])
mean_strength = np.array([320, 305, 282, 255])
std_strength = np.array([8, 7, 10, 9])

fig, ax = plt.subplots(figsize=(6, 4))
ax.errorbar(
    temperature,
    mean_strength,
    yerr=std_strength,
    marker="o",
    capsize=4,
)
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Yield strength (MPa)")
ax.set_title("Mean and Standard Deviation")
ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
~~~

그림 설명에는 오차막대가 표준편차인지 표준오차인지 밝혀야 한다.

# 6. 2차원 색상 그래프

두 위치 좌표에 따라 물리량이 변할 때 색으로 크기를 나타낼 수 있다. 다음은 시편 표면의
간단한 온도 분포다.

~~~python
x = np.linspace(-2.0, 2.0, 101)
y = np.linspace(-2.0, 2.0, 101)
X, Y = np.meshgrid(x, y)
temperature = 300.0 + 500.0 * np.exp(-(X**2 + Y**2))

fig, ax = plt.subplots(figsize=(6, 5))
image = ax.contourf(X, Y, temperature, levels=20, cmap="inferno")
colorbar = fig.colorbar(image, ax=ax)
ax.set_xlabel("x (mm)")
ax.set_ylabel("y (mm)")
ax.set_title("Surface Temperature")
ax.set_aspect("equal")
colorbar.set_label("Temperature (K)")
fig.tight_layout()
plt.show()
~~~

<code>np.meshgrid()</code>는 1차원 좌표 배열로 2차원 격자를 만든다. 색상 막대에는
색이 나타내는 물리량과 단위를 표시한다.

# 7. 3차원 그래프

## 7.1. <code>meshgrid</code>로 2차원 함수 계산하기

다음과 같이 두 변수를 갖는 함수를 생각하자.

$$
f(x,y)=x^2+y^2
$$

이 함수를 그리려면 여러 $x$와 $y$의 조합에서 함수값을 계산해야 한다. 먼저
<code>np.linspace()</code>로 각각의 1차원 좌표를 만든다.

~~~python
x = np.linspace(-2.0, 2.0, 5)
y = np.linspace(-2.0, 2.0, 5)

print(x)
print(y)
~~~

<code>np.meshgrid(x, y)</code>는 모든 $(x,y)$ 조합을 계산할 수 있도록 두 개의
2차원 좌표 배열 <code>X</code>와 <code>Y</code>를 만든다.

~~~python
X, Y = np.meshgrid(x, y)

print(X)
print(Y)
print(X.shape, Y.shape)
~~~

<code>X</code>의 각 행에는 $x$ 좌표가 반복되고, <code>Y</code>의 각 열에는 $y$ 좌표가
반복된다. 따라서 같은 위치의 <code>X[i, j]</code>와 <code>Y[i, j]</code>가 격자점
하나의 좌표를 나타낸다. NumPy의 원소별 연산을 적용하면 모든 격자점의 함수값을 한 번에
구할 수 있다.

~~~python
Z = X**2 + Y**2

print(Z)
print(Z.shape)
~~~

예를 들어 <code>X[0, 0] = -2</code>, <code>Y[0, 0] = -2</code>이므로
<code>Z[0, 0] = 8</code>이다.

## 7.2. 3차원 mesh 그리기

계산한 $Z=f(X,Y)$를 <code>plot_wireframe()</code>에 전달하면 격자선으로 이루어진
3차원 mesh를 그릴 수 있다. 부드러운 그림을 위해 좌표의 개수를 늘려 보자.

~~~python
x = np.linspace(-2.0, 2.0, 51)
y = np.linspace(-2.0, 2.0, 51)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection="3d")
ax.plot_wireframe(X, Y, Z, color="tab:blue", linewidth=0.6)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
ax.set_title(r"$z=x^2+y^2$")
fig.tight_layout()
plt.show()
~~~

<code>plot_wireframe()</code>에는 shape이 같은 2차원 배열 <code>X</code>, <code>Y</code>,
<code>Z</code>가 필요하다. 격자선 대신 색칠된 표면을 그리고 싶다면 다음과 같이
<code>plot_surface()</code>를 사용한다.

~~~python
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection="3d")
surface = ax.plot_surface(X, Y, Z, cmap="viridis")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
fig.colorbar(surface, ax=ax, shrink=0.7, label="f(x, y)")
fig.tight_layout()
plt.show()
~~~

## 7.3. 등고선으로 표현하기

등고선(contour)은 함수값이 같은 점들을 연결한 선이다. 3차원 표면을 위에서 내려다본
것처럼 2차원 평면에 함수의 변화를 표현할 수 있다. 앞에서 계산한
$Z=X^2+Y^2$를 <code>ax.contour()</code>에 전달해 보자.

~~~python
x = np.linspace(-2.0, 2.0, 101)
y = np.linspace(-2.0, 2.0, 101)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig, ax = plt.subplots(figsize=(6, 5))
contours = ax.contour(X, Y, Z, levels=8, cmap="viridis")
ax.clabel(contours, inline=True, fontsize=9)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"Contours of $f(x,y)=x^2+y^2$")
ax.set_aspect("equal")
ax.grid(True, alpha=0.2)

fig.tight_layout()
plt.show()
~~~

<code>levels=8</code>은 등고선의 높이를 8단계로 나누도록 요청한다.
<code>ax.clabel()</code>은 각 등고선 위에 해당 함수값을 표시한다. 이 함수에서는
원점에서 거리가 같은 점의 함수값이 같으므로 등고선이 원 모양으로 나타난다.

등고선 사이도 색으로 채우고 싶다면 <code>contour()</code> 대신
<code>contourf()</code>를 사용한다.

~~~python
fig, ax = plt.subplots(figsize=(6, 5))
filled = ax.contourf(X, Y, Z, levels=20, cmap="viridis")
contours = ax.contour(X, Y, Z, levels=8, colors="black", linewidths=0.6)
ax.clabel(contours, inline=True, fontsize=8)
fig.colorbar(filled, ax=ax, label="f(x, y)")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"Filled contours of $f(x,y)=x^2+y^2$")
ax.set_aspect("equal")

fig.tight_layout()
plt.show()
~~~

# 8. 재료공학 예제: 결정방향

입방정(cubic crystal)의 결정방향 $[uvw]$는 벡터 $(u,v,w)$와 나란하다. 방향을
표현하기 위해 다음과 같이 단위벡터로 바꾼다.

$$
\widehat{\boldsymbol d}
=\frac{1}{\sqrt{u^2+v^2+w^2}}
\begin{bmatrix}u\\v\\w\end{bmatrix}
$$

~~~python
def unit_direction(uvw):
    direction = np.asarray(uvw, dtype=float)
    magnitude = np.linalg.norm(direction)
    if magnitude == 0:
        raise ValueError("[000] has no direction")
    return direction / magnitude


print(unit_direction([1, 1, 0]))
~~~

$[100]$, $[010]$, $[001]$, $[110]$ 방향을 화살표로 나타내자.

~~~python
directions = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
])
labels = ["[100]", "[010]", "[001]", "[110]"]

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")

for direction, label in zip(directions, labels):
    vector = unit_direction(direction)
    ax.quiver(0, 0, 0, *vector, arrow_length_ratio=0.12)
    ax.text(*(1.08 * vector), label)

ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.2)
ax.set_zlim(0, 1.2)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Directions in a Cubic Crystal")
ax.set_box_aspect((1, 1, 1))
fig.tight_layout()
plt.show()
~~~

결정면의 극점도(pole figure)와 입체투영(stereographic projection)은 별도의 결정학
강의에서 다룬다.

# 9. 자주 하는 실수

- <code>plt.subplots(1, 2)</code>가 반환한 <code>axes</code>는 Axes 배열이다.
- 로그축에는 0과 음수를 넣을 수 없다.
- 색상 그래프에는 물리량과 단위를 표시한 colorbar를 추가한다.
- <code>plot_surface()</code>의 <code>X</code>, <code>Y</code>, <code>Z</code> shape은 같아야 한다.
- 영벡터 $[000]$은 방향을 나타내지 않는다.

# 10. 정리

- 여러 Axes를 이용하면 서로 다른 데이터를 읽기 쉽게 비교할 수 있다.
- 넓은 범위의 양수 데이터에는 로그축이 유용하다.
- 오차막대는 대표값과 데이터의 불확실성을 함께 보여 준다.
- <code>contourf()</code>는 2차원 분포를 색으로 나타낸다.
- <code>contour()</code>는 함수값이 같은 위치를 등고선으로 나타낸다.
- <code>plot_wireframe()</code>, <code>plot_surface()</code>, <code>quiver()</code>로
  3차원 값과 방향을 표현할 수 있다.

# 11. 쉬운 연습 문제

## 문제 1

한 Figure에 1행 2열의 Axes를 만드는 코드를 쓰시오.

<!--
풀이와 해답:
fig, axes = plt.subplots(1, 2)
-->

## 문제 2

확산계수 $10^{-18}$부터 $10^{-10}$까지를 표시할 때 선형축과 로그축 중 어느 것이 더
적절한가?

<!--
풀이와 해답:
값이 여러 자릿수에 걸쳐 변하므로 로그축이 더 적절하다.
-->

## 문제 3

평균 경도 <code>hardness</code>와 표준편차 <code>hardness_std</code>를 오차막대로
그리는 한 줄의 코드를 쓰시오.

<!--
풀이와 해답:
ax.errorbar(temperature, hardness, yerr=hardness_std, marker="o", capsize=4)
-->

## 문제 4

결정방향 $[001]$의 단위벡터를 구하시오.

<!--
풀이와 해답:
(0, 0, 1)이며 이미 크기가 1이다.
-->

## 문제 5

3차원 Axes를 만드는 다음 코드의 빈칸을 채우시오.

~~~python
fig = plt.figure()
ax = fig.add_subplot(111, __________)
~~~

<!--
풀이와 해답:
projection="3d"
-->
