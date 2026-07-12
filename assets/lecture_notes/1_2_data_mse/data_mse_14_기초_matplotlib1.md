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
- [2. 소개](#2-소개)
- [3. scatter plot](#3-scatter-plot)
- [4. Figure \& axes objects](#4-figure--axes-objects)
- [5. 1차원 그래프 그리기](#5-1차원-그래프-그리기)
  - [5.1. 1차원 그래프](#51-1차원-그래프)
    - [5.1.1. $y=\\cos\\theta$](#511-ycostheta)
    - [5.1.2. $y=\\sin\\theta$](#512-ysintheta)
    - [5.1.3. $y=\\tan\\theta$](#513-ytantheta)
    - [5.1.4. 반지름의 길이가 10인 원](#514-반지름의-길이가-10인-원)
  - [5.2. 공칭 변형률과 진변형률](#52-공칭-변형률과-진변형률)
  - [5.3. Stress vs. strain curve 그리기](#53-stress-vs-strain-curve-그리기)


# 1. 목표
 - axes, figure 를 만들 수 있다.
 - 선(line), 점(dot)으로 이루어진 그래프를 그릴 수 있다.
 - x축, y축의 label, tick, limits을 만들 수 있다.
 - linear scale, logscale을 만들고 이해할 수 있다.
 - 3차원 그래프를 그릴 수 있다.
 - 파일로부터 데이터를 불러오고, 이를 graph로 바꿀 수 있다.

# 2. 소개

[Matplotlib](https://matplotlib.org): Python 환경에서 데이터를 시각화하는데 가장
널리 쓰이는 라이브러리 중 하나이다. MATLAB과 유사한 환경을 제공해주는 pyplot 모듈을 활용한
인터페이스가 널리쓰인다. 아래 예시들을 함께 살펴보자.
```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4] # list 혹은 numpy array 모두 활용 가능
y = [0, 1, 4, 9, 16]

plt.plot(x, y)          # 선 그래프
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
```

# 3. scatter plot

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

```plt```환경을 조금 더 상세히 살펴보면, ```figure```와 ```axis``` 객체가 사용되는
것을 알 수 있다. ```figure```는 그림을 그리는 캔버스, ```axis```는 그래프가 시각화되는
좌표계라 볼 수 있다.

# 4. Figure & axes objects
- Figure: 그래프 전체 "캔버스"
- Axes: 실제 데이터가 그려지는 "좌표 영역"

따라서 한 Figure 안에 여러 개의 axes가 삽입될 수 있다. 아래 예제를 살펴보자.

```python
import matplotlib.pyplot as plt

# Figure(도화지), Axes(좌표 영역) 생성
fig, ax = plt.subplots()

x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [9, 8, 7, 6, 5]

# ax 객체를 활용해 데이터 플롯
ax.plot(x, y1, label="y = x^2", color="blue")
ax.plot(x, y2, label="y =-x+9", color="red")

# 그래프 꾸미기
ax.set_title("Figure & Axes Example")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
ax.grid(True)

plt.show()
```

혹은 각각을 다른 axis에 그리기
```python
import matplotlib.pyplot as plt

# Figure(도화지), Axes(좌표 영역) 생성
fig=plt.figure(figsize=(9,3))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)

x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [9, 8, 7, 6, 5]

# ax 객체를 활용해 데이터 플롯
ax1.plot(x, y1, label="y = x^2", color="blue")
ax2.plot(x, y2, label="y =-x+9", color="red")

# 그래프 꾸미기
ax1.set_title("Axis 1")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")
ax1.legend()
ax1.grid(True)

ax2.set_title("Axis 2")
ax2.set_xlabel("X-axis")
ax2.set_ylabel("Y-axis")
ax2.legend()
ax2.grid(True)

plt.show()
```

# 5. 1차원 그래프 그리기

- NumPy의 ```linspace```, ```logspace```등과 결합하면 여러 1D 그래프를 손쉽게 그릴
수 있다. 예를 들어 $y=x^2$을 $x\in[-10,10]$을 그리자면

```python
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10) # [-10,10] 범위내의 50 포인트
y=x**2 ## NumPy의 element-wise operation을 기억하자.
plt.plot(x,y)
```
결과를 살펴보자.

## 5.1. 1차원 그래프
위 예제를 응용하여 아래 실습을 수행해보자. 범위 내의 아래 삼각함수를 그려보자.

### 5.1.1. $y=\cos\theta$

$$
y=\cos(\theta), \text{ with } \theta\in[-\pi,\pi]
$$

### 5.1.2. $y=\sin\theta$

$$
y=\sin(\theta), \text{ with } \theta\in[-\pi,\pi]
$$

### 5.1.3. $y=\tan\theta$
$$
y=\tan(\theta), \text{ with } \theta\in\big[-\frac{\pi}{2},\frac{\pi}{2}\big]
$$

### 5.1.4. 반지름의 길이가 10인 원

$$
x^2+y^2=10^2
$$

## 5.2. 공칭 변형률과 진변형률

- 길이 변화에 따라서 나타나는 공칭 변형률(engineering strain)과 진변형률
  (true strain)그래프 관계를 그리고 이를 비교해보자.

$$
\varepsilon=\ln(\epsilon+1)
$$

## 5.3. Stress vs. strain curve 그리기
다음 [압축파일](/assets/dat_files/lectures/1_2_data_mse/tensile_test_results.zip)을 풀어서, 파일 하나를
살펴보자 - 예를 들어 `00_DD_WZ_01.csv`
위 데이터 파일을 활용해
1.  폭: 6.04 mm, 두께 2.99 mm 인걸 확인하고,
2.  힘과 변위 칼럼을 활용해서 응력과 변형률을 구하자.
3.  그 다음 응력과 변형률 곡선을 Figure로 그려보자.
