---
layout: page
title: 열전도의 유한차분해석
description: 일차원 정상 열전도 방정식을 유한차분법으로 풀기
target: 2학년 2학기
permalink:
prerequisite: 열전도 방정식, 연립방정식, Python과 NumPy
toc:
  sidebar: left
---

- [1. 격자와 절점](#1-격자와-절점)
- [2. 이계 미분의 근사](#2-이계-미분의-근사)
- [3. 정상 열전도 방정식](#3-정상-열전도-방정식)
- [4. 손계산 예제](#4-손계산-예제)
- [5. Python 구현](#5-python-구현)
- [6. 연습 문제](#6-연습-문제)

# 1. 격자와 절점

길이 $L$인 구간을 $N$개의 같은 간격으로 나누면

$$\Delta x=\frac{L}{N},\qquad x_i=i\Delta x$$

이다. 연속적인 온도장 $T(x)$를 절점 온도 $T_i=T(x_i)$로 근사한다.

# 2. 이계 미분의 근사

중앙차분법을 사용하면 내부 절점에서

$$\boxed{\left.\frac{d^2T}{dx^2}\right|_i
\approx\frac{T_{i-1}-2T_i+T_{i+1}}{\Delta x^2}}$$

이다. $\Delta x$가 작을수록 일반적으로 정확도가 좋아지지만 미지수와 계산량이
증가한다.

# 3. 정상 열전도 방정식

열생성이 없는 정상 일차원 문제에서 $d^2T/dx^2=0$이므로

$$T_{i-1}-2T_i+T_{i+1}=0$$

이다. 즉 내부 절점의 온도는 양쪽 이웃 온도의 평균이다.

$$T_i=\frac{T_{i-1}+T_{i+1}}{2}$$

# 4. 손계산 예제

$T_0=100^\circ\mathrm C$, $T_3=40^\circ\mathrm C$이고 내부 절점이 두 개이면

$$\begin{aligned}-2T_1+T_2&=-100,\\T_1-2T_2&=-40\end{aligned}$$

이다. 연립방정식을 풀면 $T_1=80^\circ\mathrm C$, $T_2=60^\circ\mathrm C$이다.

# 5. Python 구현

```python
import numpy as np

left_temperature = 100.0
right_temperature = 40.0
n_internal = 4

A = np.zeros((n_internal, n_internal))
b = np.zeros(n_internal)

for i in range(n_internal):
    A[i, i] = -2.0
    if i > 0:
        A[i, i - 1] = 1.0
    if i < n_internal - 1:
        A[i, i + 1] = 1.0

b[0] = -left_temperature
b[-1] = -right_temperature

temperature_internal = np.linalg.solve(A, b)
temperature = np.concatenate((
    [left_temperature], temperature_internal, [right_temperature]
))
print(temperature)
```

해석해가 선형이므로 계산 결과도 등간격으로 감소한다.

## 계산 결과를 확인하는 방법

- 내부 열생성이 없는 경우 각 내부 온도가 이웃 온도의 평균인지 확인한다.
- 모든 절점 온도가 고온 경계와 저온 경계 사이에 있는지 확인한다.
- 격자 간격을 절반으로 줄여 결과가 크게 변하지 않는지 확인한다.
- 행렬의 첫 행과 마지막 행에 경계조건이 올바르게 반영되었는지 확인한다.

유한차분식은 미분방정식을 대수방정식으로 바꾼다. 내부 절점이 $n$개라면
$n$개의 미지 온도와 $n$개의 방정식이 생긴다.

## 내부 열생성이 있는 차분식

정상상태에서 $k$와 열생성률 $\dot q'''$이 일정하면

$$k\frac{d^2T}{dx^2}+\dot q'''=0$$

이다. 중앙차분식을 대입하면

$$
\boxed{T_{i-1}-2T_i+T_{i+1}
=-\frac{\dot q'''\Delta x^2}{k}}
$$

를 얻는다. 열생성이 없는 문제와 비교하면 행렬의 계수는 같고 오른쪽 벡터에
열생성 항이 추가된다. 예를 들어 $\dot q'''\Delta x^2/k=10\ ^\circ\mathrm C$,
$T_{i-1}=T_{i+1}=50\ ^\circ\mathrm C$이면 $T_i=55\ ^\circ\mathrm C$이다.
내부에서 열이 생성되므로 중앙 온도가 이웃 온도보다 높다.

# 6. 연습 문제

1. 길이 1 m를 5개 구간으로 나눌 때 $\Delta x$를 구하라.
2. $T_{i-1}=90^\circ\mathrm C$, $T_{i+1}=70^\circ\mathrm C$일 때 $T_i$를 구하라.
3. 예제 코드에서 내부 절점 수를 9로 바꾸어 결과를 확인하라.
4. 내부 절점이 3개라면 풀어야 할 연립방정식의 미지수는 몇 개인가?
5. $T_{i-1}=60$, $T_i=50$, $T_{i+1}=40$일 때 $T_{i-1}-2T_i+T_{i+1}$을 구하라.
6. 격자를 더 잘게 나누었을 때 얻는 장점과 비용을 각각 하나씩 쓰시오.

<!--
풀이와 해답:
1. Delta x=0.2 m이다.
2. T_i=(90+70)/2=80 degC이다.
3. 전체 온도는 100, 94, 88, ..., 46, 40 degC로 선형 감소한다.
4. T_1, T_2, T_3의 3개이다.
5. 60-2(50)+40=0이다. 따라서 이 절점은 열생성이 없는 정상 차분식을 만족한다.
6. 연속 해를 더 잘 근사할 수 있지만 미지수와 계산량이 증가한다.
-->
