---
layout: distill
title: Matplotlib 기초 1
description: NumPy 배열을 선 그래프와 산점도로 표현하기
target: 1학년 2학기
permalink:
featured: true
prerequisite: NumPy 배열 기초, NumPy 배열 활용
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
- [2. Matplotlib 시작하기](#2-matplotlib-시작하기)
- [3. 선 그래프](#3-선-그래프)
- [4. Figure와 Axes](#4-figure와-axes)
- [5. 그래프 꾸미기](#5-그래프-꾸미기)
- [6. 산점도 (scatter plot)](#6-산점도-scatter-plot)
- [7. 여러 데이터 비교하기](#7-여러-데이터-비교하기)
- [8. 재료공학 예제: 응력–변형률 곡선](#8-재료공학-예제-응력변형률-곡선)
- [9. 일차 함수 그려보기](#9-일차-함수-그려보기)
  - [삼각함수](#삼각함수)
- [9. 그림 저장하기](#9-그림-저장하기)
- [10. 자주 하는 실수](#10-자주-하는-실수)
- [11. 정리](#11-정리)
- [12. 연습 문제](#12-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- NumPy 배열을 선 그래프와 산점도로 나타낼 수 있다.
- Figure와 Axes의 역할을 구분할 수 있다.
- 제목, 축 이름, 범례와 격자를 추가할 수 있다.
- 한 그래프에서 여러 데이터를 비교할 수 있다.
- 응력–변형률 데이터를 그래프로 나타낼 수 있다.
- 완성한 그림을 파일로 저장할 수 있다.

# 2. Matplotlib 시작하기

[Matplotlib](https://matplotlib.org/)은 Python에서 데이터를 시각화할 때 널리 사용하는
라이브러리다. 보통 NumPy는 데이터를 계산하고, Matplotlib은 계산 결과를 그림으로
표현하는 데 사용한다.

~~~python
import numpy as np
import matplotlib.pyplot as plt
~~~

관례적으로 <code>numpy</code>는 <code>np</code>, <code>matplotlib.pyplot</code>은
<code>plt</code>라는 이름으로 불러온다.

# 3. 선 그래프

선 그래프(line plot)는 $x$와 $y$의 관계 또는 값의 연속적인 변화를 표현하기에
적합하다. <code>np.linspace()</code>로 $x$ 좌표를 만들고, 앞선 NumPy 강의에서 배운
원소별 연산으로 $y$ 좌표를 계산해 보자.

~~~python
x = np.linspace(-3.0, 3.0, 101)
y = x**2 # element-wise operation

plt.plot(x, y)
plt.show()
~~~

<code>x</code>와 <code>y</code>에는 같은 개수의 값이 들어 있다. 같은 인덱스의 두 값
$(x_i,y_i)$가 하나의 좌표가 되고, 선 그래프는 이 점들을 연결한다.

# 4. Figure와 Axes

- **Figure**는 그림 전체를 담는 캔버스다.
- **Axes**는 실제 그래프가 그려지는 좌표 영역이다.

<code>plt.subplots()</code>는 Figure와 Axes를 함께 만든다.

~~~python
x = np.linspace(0.0, 10.0, 101)
y = 2.0 * x + 3.0

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
~~~

이후에는 어느 그래프를 수정하는지 명확한 객체 지향(object-oriented) 방식을 사용한다.
즉, <code>plt.plot()</code>보다 <code>ax.plot()</code>을 주로 사용한다.

# 5. 그래프 꾸미기

그래프에는 데이터의 의미와 단위를 표시해야 한다.

~~~python
x = np.linspace(0.0, 10.0, 101)
y = 2.0 * x + 3.0

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, color="tab:blue", linewidth=2, label=r"$y=2x+3$")
ax.set_title("Linear Function")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim(0.0, 10.0)
ax.set_ylim(0.0, 25.0)
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
plt.show()
~~~

| 명령 | 역할 |
|---|---|
| <code>ax.set_title()</code> | 그래프 제목 |
| <code>ax.set_xlabel()</code> | $x$축 이름과 단위 |
| <code>ax.set_ylabel()</code> | $y$축 이름과 단위 |
| <code>ax.set_xlim()</code> | $x$축 표시 범위 |
| <code>ax.set_ylim()</code> | $y$축 표시 범위 |
| <code>ax.grid()</code> | 격자 표시 |
| <code>ax.legend()</code> | 범례 표시 |

# 6. 산점도 (scatter plot)

산점도(scatter plot)는 측정값처럼 서로 떨어진 데이터의 관계를 나타내기에 적합하다.

~~~python
temperature = np.array([300, 400, 500, 600, 700])
strength = np.array([315, 302, 284, 258, 225])

fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(temperature, strength, color="tab:red", s=60)
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Yield strength (MPa)")
ax.set_title("Temperature and Yield Strength")
ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
~~~

여기에서 <code>s</code>는 점의 크기다. 측정된 점 사이의 값이 알려져 있지 않다면 선으로
연결하기보다 산점도로 먼저 표현하는 것이 자연스럽다.

# 7. 여러 데이터 비교하기

하나의 Axes에 <code>ax.plot()</code>을 여러 번 호출하면 여러 데이터를 함께 비교할 수
있다. 각 데이터에 <code>label</code>을 지정하고 범례를 표시하자.

~~~python
strain = np.linspace(0.0, 0.01, 101)
stress_al = 70_000 * strain
stress_fe = 210_000 * strain

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(strain, stress_al, label="Al: E = 70 GPa")
ax.plot(strain, stress_fe, label="Fe: E = 210 GPa")
ax.set_xlabel("Strain")
ax.set_ylabel("Stress (MPa)")
ax.set_title("Elastic Stress–Strain Curves")
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
plt.show()
~~~

응력의 단위를 MPa로 사용했으므로 영률도 $70\,000$ MPa와 $210\,000$ MPa로
계산하였다. 그래프에 물리량을 표시할 때는 단위를 반드시 확인해야 한다.

# 8. 재료공학 예제: 응력–변형률 곡선

초기 길이가 $L_0$, 초기 단면적이 $A_0$인 인장시험편에서 공칭 변형률과 공칭 응력은

$$
e=\frac{\Delta L}{L_0},
\qquad
\sigma=\frac{F}{A_0}
$$

이다. 초기 길이 $50$ mm, 폭 $6$ mm, 두께 $2$ mm인 시험편의 측정값을 그래프로
나타내자. $1\ \mathrm{N/mm^2}=1\ \mathrm{MPa}$이다.

~~~python
displacement = np.array([0.00, 0.05, 0.10, 0.15, 0.20, 0.30])  # mm
force = np.array([0, 2400, 4750, 6900, 8200, 8700])             # N

initial_length = 50.0  # mm
width = 6.0            # mm
thickness = 2.0        # mm
initial_area = width * thickness

engineering_strain = displacement / initial_length
engineering_stress = force / initial_area

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(engineering_strain, engineering_stress, marker="o")
ax.set_xlabel("Engineering strain")
ax.set_ylabel("Engineering stress (MPa)")
ax.set_title("Tensile Test")
ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
~~~

<code>marker="o"</code>는 실제 측정 지점을 원으로 표시한다.


# 9. 일차 함수 그려보기

## 삼각함수
$$
y=\sin(x), \text{in}\ -\pi\le x  \le \pi
$$

$$
y=\tan(x), \text{in}\ 0 \le x \le \frac{\pi}{2}
$$

~~~python
x=np.linspace(-np.pi,np.pi)
sinx=np.sin(x)
tanx=np.tan(x)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, sinx,label='sin')
ax.plot(x, tanx,label='tan')
ax.set_xlabel("x (rad)")
ax.set_ylabel("sinx, tanx")
~~~

# 9. 그림 저장하기

<code>fig.savefig()</code>로 그림을 저장할 수 있다. 저장 명령은 일반적으로
<code>plt.show()</code>보다 앞에 둔다.

~~~python
x = np.linspace(0.0, 2.0 * np.pi, 201)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y)
ax.set_xlabel("x (rad)")
ax.set_ylabel("sin(x)")
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig("sine_curve.png", dpi=150)
plt.close(fig)
~~~

# 10. 자주 하는 실수

- $x$와 $y$ 데이터의 길이가 다르면 그래프를 그릴 수 없다.
- 축 이름만 쓰고 단위를 빠뜨리지 않도록 한다.
- <code>label</code>과 함께 <code>ax.legend()</code>도 호출해야 범례가 나타난다.
- 측정값의 점과 모델의 선이 무엇을 의미하는지 구분해서 표시한다.

# 11. 정리

- <code>ax.plot(x, y)</code>는 선 그래프를, <code>ax.scatter(x, y)</code>는 산점도를 그린다.
- Figure는 그림 전체이고 Axes는 실제 좌표 영역이다.
- 제목, 축 이름, 단위, 범례를 표시해야 그래프의 의미가 분명해진다.
- NumPy의 배열 연산 결과를 Matplotlib으로 바로 시각화할 수 있다.

# 12. 연습 문제

## 문제 1

다음 코드의 빈칸을 채워 $y=3x$를 선 그래프로 나타내시오.

~~~python
x = np.linspace(0.0, 5.0, 51)
y = 3.0 * x
fig, ax = plt.subplots()
# 여기에 코드를 작성한다.
plt.show()
~~~

<!--
풀이와 해답:
ax.plot(x, y)
-->

## 문제 2

선 그래프와 산점도는 각각 어떤 종류의 데이터를 표현하기에 적합한지 설명하시오.

<!--
풀이와 해답:
선 그래프는 연속적인 변화나 함수의 경향에, 산점도는 서로 떨어진 측정값에 적합하다.
-->

## 문제 3

그래프에 $x$축 이름 <code>Time (s)</code>와 $y$축 이름
<code>Temperature (K)</code>를 추가하는 코드를 쓰시오.

<!--
풀이와 해답:
ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (K)")
-->

## 문제 4

초기 길이가 $40$ mm이고 변위가 $0.2$ mm일 때 공칭 변형률을 계산하시오.

<!--
풀이와 해답:
e = 0.2 / 40 = 0.005이다.
-->
