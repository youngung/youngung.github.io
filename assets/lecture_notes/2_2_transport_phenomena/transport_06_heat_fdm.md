---
layout: page
title: 열전도의 유한차분해석
description: 일차원 정상 열전도 방정식을 유한차분법으로 풀기
target: 2학년 2학기
permalink:
prerequisite: 열전도 방정식, 연립방정식, Python과 NumPy
toc: false
---

**목차**

* TOC
{:toc}

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

## 2.1. Taylor 전개로 중앙차분식 유도하기

충분히 매끄러운 온도함수를 $x_i$ 주위에서 전개하면

$$
T_{i\pm1}=T_i\pm\Delta xT_i'
+\frac{\Delta x^2}{2}T_i''
\pm\frac{\Delta x^3}{6}T_i'''
+\frac{\Delta x^4}{24}T_i^{(4)}+\cdots.
$$

두 식을 더하면 홀수차 항이 소거되어

$$
\frac{T_{i-1}-2T_i+T_{i+1}}{\Delta x^2}
=T_i''+\frac{\Delta x^2}{12}T_i^{(4)}+O(\Delta x^4)
$$

이다. 따라서 이계 미분의 중앙차분 근사는 일반적으로 **2차 정확도**를 갖는다.
이는 온도 자체의 크기가 아니라 격자 간격에 대한 절단오차의 감소율을 말한다.
선형 또는 이차함수에서는 $T^{(4)}=0$이므로 이 차분식이 해당 함수의 이계
미분을 정확하게 계산한다. 선형 정상해만으로는 일반적인 격자 수렴률을
검증하기 어렵다는 점에 주의한다.

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

b[0] -= left_temperature
b[-1] -= right_temperature

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

## 열생성 문제를 행렬식에 넣고 에너지 수지 확인하기

$N$개 구간에는 경계를 포함하여 $N+1$개 절점, 내부에는 $N-1$개 미지수가
있다. 다음 예제는 양 끝 온도를 고정하고 내부 열생성을 포함한다. 경계값은
오른쪽 벡터에서 **빼서** 반영한다. `-=`를 쓰면 내부 절점이 하나뿐이라 양쪽
경계가 같은 방정식에 들어가는 경우도 처리할 수 있다.

```python
import numpy as np

length = 0.02          # m
k = 10.0               # W/(m K)
source = 1.0e6         # W/m^3
T_left, T_right = 300.0, 300.0  # K
n_intervals = 10
x = np.linspace(0.0, length, n_intervals + 1)
dx = length / n_intervals
n = n_intervals - 1

matrix = -2.0 * np.eye(n)
matrix += np.eye(n, k=1) + np.eye(n, k=-1)
rhs = np.full(n, -source * dx**2 / k)
rhs[0] -= T_left
rhs[-1] -= T_right
T = np.r_[T_left, np.linalg.solve(matrix, rhs), T_right]
T_exact = (T_left + (T_right - T_left) * x / length
           + source * x * (length - x) / (2.0 * k))

# 이차 정확도의 편측차분으로 바깥쪽 열유속을 구한다.
q_left = k * (-3*T[0] + 4*T[1] - T[2]) / (2*dx)
q_right = -k * (3*T[-1] - 4*T[-2] + T[-3]) / (2*dx)
print("max temperature error [K]:", np.max(np.abs(T - T_exact)))
print("outward flux sum [W/m^2]:", q_left + q_right)
print("generation per area [W/m^2]:", source * length)
```

중심온도는 305 K, 양면의 바깥쪽 열유속 합은
$2.0\times10^4\ \mathrm{W/m^2}$이다. 해가 이차함수이므로 절점 온도는 반올림 오차
범위에서 해석해와 일치한다. 이는 경계조건과 열생성항의 구현을 확인하는 예이다.
일반적인 수렴률은 예를 들어 매끄러운 비균일 열원을 갖는 문제에서 격자 간격을
절반으로 줄이고 해석해에 대한 오차가 약 1/4이 되는지 조사하여 확인한다.

## 물성이 위치에 따라 변하는 경우

$k$가 변할 때는 $kT''$로 바꾸지 말고 면을 통과하는 열유속을 보존하는 형태로

$$
\frac{k_{i+1/2}(T_{i+1}-T_i)-k_{i-1/2}(T_i-T_{i-1})}{\Delta x^2}
+\dot q_i'''=0
$$

이산화한다. 같은 길이의 두 반구간에 서로 다른 열전도도가 있으면 면의 유효값에
직렬 열저항에 대응하는 조화평균을 사용한다. 재료 계면에서 열유속을 연속으로
유지하는 것이 핵심이다.

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

## 관련자료와 이어 읽기

- [MIT OCW 3.185: Heat Conduction](https://ocw.mit.edu/courses/3-185-transport-phenomena-in-materials-engineering-fall-2003/resources/chap3/): PDF의 Finite Differences 부분에서 미분방정식을 절점 방정식으로 바꾸는 방법을 비교한다.

- [제5강: 열전도 방정식](/assets/lecture_notes/2_2_transport_phenomena/transport_05_heat_equation.md)
- [제10강: 비정상 확산](/assets/lecture_notes/2_2_transport_phenomena/transport_10_transient_diffusion.md)

---

[이전 강의](/assets/lecture_notes/2_2_transport_phenomena/transport_05_heat_equation.md) · [강의 목록](/_lectures/2_2_transport.md) · [다음 강의](/assets/lecture_notes/2_2_transport_phenomena/transport_07_transient_heat.md)
