---
layout: distill
title: 최소제곱법
description: 측정 데이터에 가장 잘 맞는 직선 구하기
target: 1학년 2학기
permalink:
featured: true
prerequisite: NumPy 배열, 행렬 연산 기초, Matplotlib 기초
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
- [2. 왜 직선 적합이 필요한가?](#2-왜-직선-적합이-필요한가)
- [3. 잔차와 잔차제곱합](#3-잔차와-잔차제곱합)
- [4. 가장 간단한 예: 평균 구하기](#4-가장-간단한-예-평균-구하기)
- [5. 직선의 최소제곱 적합](#5-직선의-최소제곱-적합)
- [6. 작은 데이터로 손 계산하기](#6-작은-데이터로-손-계산하기)
- [7. NumPy로 직선 구하기](#7-numpy로-직선-구하기)
- [8. 적합 결과 확인하기](#8-적합-결과-확인하기)
- [9. 재료공학 예제: 영률 구하기](#9-재료공학-예제-영률-구하기)
- [10. 행렬로 이해하는 최소제곱법](#10-행렬로-이해하는-최소제곱법)
- [11. 적합할 때 주의할 점](#11-적합할-때-주의할-점)
- [12. 핵심 정리](#12-핵심-정리)
- [13. 연습 문제](#13-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)
  - [문제 7](#문제-7)
  - [문제 8](#문제-8)

# 1. 학습 목표

이 자료에서 $[\boldsymbol A]$, $[\boldsymbol x]$는 행렬·벡터의 성분 배열을 뜻하며, 배열의 행렬곱은 $[\boldsymbol A][\boldsymbol x]$처럼 붙여 쓴다. 물리적 벡터·텐서의 단일수축은 $\cdot$로 표시한다.


이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 측정 데이터에 정확히 하나의 직선이 지나지 않는 이유를 설명할 수 있다.
- 측정값, 예측값과 잔차를 구분할 수 있다.
- 최소제곱법이 최소화하는 양을 설명할 수 있다.
- 간단한 데이터의 직선 기울기와 절편을 계산할 수 있다.
- <code>np.polyfit()</code>으로 직선을 적합하고 그래프로 확인할 수 있다.
- 응력–변형률 데이터의 기울기로 영률을 추정할 수 있다.

# 2. 왜 직선 적합이 필요한가?

두 점이 주어지면 두 점을 정확히 지나는 직선을 하나 구할 수 있다. 그러나 실제 실험에는
측정오차, 시편 편차와 주변 환경의 영향이 포함된다. 따라서 여러 측정점이 하나의 직선 위에
정확히 놓이는 경우는 드물다.

예를 들어 탄성구간의 응력과 변형률은 이상적으로

$$
\sigma=E\varepsilon
$$

의 선형관계를 따른다. 실제 측정값은 이 직선 주변에 흩어질 수 있다. 이때 일부 점만
골라 직선을 정하기보다 모든 측정점을 함께 고려하여 데이터를 가장 잘 대표하는 직선을
구하는 것이 합리적이다.

직선 모델을 다음과 같이 쓰자.

$$
\widehat y=ax+b
$$

- $a$: 직선의 기울기
- $b$: $y$축 절편
- $\widehat y$: 모델이 예측한 값

기호 $\widehat y$는 측정값 $y$와 구분하기 위해 사용한다.

# 3. 잔차와 잔차제곱합

$i$번째 데이터 $(x_i,y_i)$에서 모델의 예측값은

$$
\widehat y_i=ax_i+b
$$

이다. 측정값과 예측값의 차이를 **잔차(residual)**라 한다.

$$
\boxed{e_i=y_i-\widehat y_i}
$$

- $e_i>0$: 측정점이 직선보다 위에 있다.
- $e_i<0$: 측정점이 직선보다 아래에 있다.
- $e_i=0$: 직선이 측정점을 정확히 지난다.

잔차를 단순히 더하면 양수와 음수가 서로 상쇄될 수 있다. 이를 피하기 위해 잔차를
제곱하여 더한다.

$$
\boxed{
S(a,b)=\sum_{i=1}^{N}e_i^2
=\sum_{i=1}^{N}\left[y_i-(ax_i+b)\right]^2
}
$$

$S$를 잔차제곱합(sum of squared errors, SSE)이라고 한다. **최소제곱법(least
squares method)**은 $S$가 가장 작아지는 $a$와 $b$를 찾는 방법이다.

잔차를 제곱하면 다음 특징이 있다.

- 모든 항이 0 이상이므로 잔차가 서로 상쇄되지 않는다.
- 큰 잔차는 제곱되므로 더 큰 영향을 준다.
- 미분 가능한 식이 되어 최솟값을 계산하기 쉽다.

# 4. 가장 간단한 예: 평균 구하기

직선보다 단순한 수평선 $\widehat y=b$로 세 측정값 $2$, $4$, $6$을 대표한다고 생각하자.
잔차제곱합은

$$
S(b)=(2-b)^2+(4-b)^2+(6-b)^2
$$

이다. $S$를 최소로 만드는 값은 데이터의 평균인

$$
b=\frac{2+4+6}{3}=4
$$

이다. 즉, 평균도 모든 값과의 차이 제곱합을 가장 작게 만드는 최소제곱 결과로 이해할 수
있다.

~~~python
import numpy as np


measurements = np.array([2.0, 4.0, 6.0])
best_constant = measurements.mean()
residuals = measurements - best_constant
sse = np.sum(residuals**2)

print(f"Best constant: {best_constant:.1f}")
print(f"Residuals: {residuals}")
print(f"SSE: {sse:.1f}")
~~~

# 5. 직선의 최소제곱 적합

직선 $\widehat y=ax+b$의 잔차제곱합은

$$
S(a,b)=\sum_{i=1}^{N}\left[y_i-(ax_i+b)\right]^2
$$

이다. $S$가 최소인 곳에서는 $a$와 $b$ 방향의 기울기가 모두 0이다.

$$
\frac{\partial S}{\partial a}=0,
\qquad
\frac{\partial S}{\partial b}=0
$$

이를 정리하면 다음 두 연립방정식을 얻는다.

$$
a\sum_i x_i^2+b\sum_i x_i=\sum_i x_iy_i
$$

$$
a\sum_i x_i+bN=\sum_i y_i
$$

이를 정규방정식(normal equations)이라 한다. 연립방정식을 풀면 기울기와 절편을 다음과
같이 나타낼 수 있다.

$$
\boxed{
a=
\frac{N\sum_i x_iy_i-(\sum_i x_i)(\sum_i y_i)}
{N\sum_i x_i^2-(\sum_i x_i)^2}
}
$$

$$
\boxed{
b=\frac{\sum_i y_i-a\sum_i x_i}{N}
=\bar y-a\bar x
}
$$

수식을 외우는 것보다 “모든 점의 잔차제곱합이 가장 작은 기울기와 절편을 구한다”는
원리를 이해하는 것이 중요하다. 실제 계산에서는 검증된 NumPy 함수를 사용한다.

# 6. 작은 데이터로 손 계산하기

다음 세 점에 가장 잘 맞는 직선을 구해 보자.

$$
(0,1),\quad(1,3),\quad(2,4)
$$

필요한 합을 표로 정리한다.

| $i$ | $x_i$ | $y_i$ | $x_i^2$ | $x_iy_i$ |
|---:|---:|---:|---:|---:|
| 1 | 0 | 1 | 0 | 0 |
| 2 | 1 | 3 | 1 | 3 |
| 3 | 2 | 4 | 4 | 8 |
| 합 | 3 | 8 | 5 | 11 |

$N=3$이므로 기울기는

$$
a=\frac{3(11)-(3)(8)}{3(5)-3^2}
=\frac{9}{6}=1.5
$$

이고 절편은

$$
b=\frac{8-1.5(3)}{3}
=\frac{7}{6}\approx1.167
$$

이다. 따라서 최소제곱 직선은

$$
\boxed{\widehat y=1.5x+1.167}
$$

이다. 세 점을 모두 정확히 지나지는 않지만 세 점 전체의 잔차제곱합을 가장 작게 만든다.

# 7. NumPy로 직선 구하기

<code>np.polyfit(x, y, 1)</code>은 $x$와 $y$ 데이터에 1차 다항식, 즉 직선을
적합한다. 반환값은 기울기와 절편 순서다.

~~~python
import matplotlib.pyplot as plt

x = np.array([0.0, 1.0, 2.0])
y = np.array([1.0, 3.0, 4.0])

slope, intercept = np.polyfit(x, y, 1)
predicted_y = slope * x + intercept

print(f"Slope: {slope:.3f}")
print(f"Intercept: {intercept:.3f}")
print(f"Predicted values: {predicted_y}")
~~~

결과는 손 계산에서 얻은 $a=1.5$, $b\approx1.167$과 같다.

측정점과 적합 직선을 함께 그려 보자.

~~~python
x_line = np.linspace(x.min(), x.max(), 100)
y_line = slope * x_line + intercept

fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(x, y, color="black", label="Data")
ax.plot(x_line, y_line, color="tab:red", label="Least-squares line")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
plt.show()
~~~

# 8. 적합 결과 확인하기

직선을 구한 다음에는 잔차를 확인해야 한다.

~~~python
residuals = y - predicted_y
sse = np.sum(residuals**2)
rmse = np.sqrt(np.mean(residuals**2))

print(f"Residuals: {residuals}")
print(f"SSE: {sse:.4f}")
print(f"RMSE: {rmse:.4f}")
~~~

평균제곱근오차(root mean squared error, RMSE)는

$$
\mathrm{RMSE}
=\sqrt{\frac{1}{N}\sum_{i=1}^{N}e_i^2}
$$

로 정의한다. RMSE는 $y$와 같은 단위를 가지므로 오차의 대표적인 크기를 해석하기 쉽다.

잔차를 $x$에 대해 그리면 직선 모델이 놓친 경향이 있는지 확인할 수 있다.

~~~python
fig, ax = plt.subplots(figsize=(6, 3))
ax.axhline(0.0, color="black", linewidth=1)
ax.scatter(x, residuals, color="tab:blue")
ax.set_xlabel("x")
ax.set_ylabel("Residual")
ax.set_title("Residual Plot")
ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
~~~

좋은 직선 모델에서는 잔차가 0 주변에 특별한 모양 없이 흩어지는 것이 바람직하다.
잔차가 곡선 모양을 보이면 데이터의 관계가 직선이 아닐 가능성이 있다.

# 9. 재료공학 예제: 영률 구하기

일축인장의 작은 탄성변형 구간에서는 Hooke 법칙이 성립한다.

$$
\sigma=E\varepsilon
$$

응력–변형률 그래프의 기울기 $E$가 영률이다. 다음은 알루미늄의 탄성구간에서 얻었다고
가정한 측정 데이터다.

~~~python
strain = np.array([0.0000, 0.0005, 0.0010, 0.0015, 0.0020])
stress = np.array([2.0, 34.0, 71.0, 103.0, 141.0])  # MPa

youngs_modulus, stress_offset = np.polyfit(strain, stress, 1)

print(f"Young's modulus: {youngs_modulus / 1000:.1f} GPa")
print(f"Stress-axis intercept: {stress_offset:.2f} MPa")
~~~

적합 직선과 측정값을 비교하자.

~~~python
strain_line = np.linspace(0.0, 0.0020, 100)
stress_line = youngs_modulus * strain_line + stress_offset

fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(strain, stress, color="black", label="Measured data")
ax.plot(strain_line, stress_line, color="tab:red", label="Linear fit")
ax.set_xlabel("Strain")
ax.set_ylabel("Stress (MPa)")
ax.set_title("Elastic Modulus from Tensile Data")
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
plt.show()
~~~

이 예제의 영률은 약 69 GPa이다. 절편이 정확히 0이 아닌 것은 하중 영점, 변형률 영점
또는 측정오차의 영향을 나타낼 수 있다.

이론적으로 원점을 지나야 한다는 이유로 무조건 절편을 0으로 고정하기 전에 측정 장비의
영점과 데이터 전처리가 올바른지 확인해야 한다. 또한 소성변형이 시작된 데이터까지
포함하면 탄성 기울기를 정확히 구할 수 없으므로 적합 구간 선택이 중요하다.

# 10. 행렬로 이해하는 최소제곱법

앞선 행렬 연산 강의와 연결하면 직선 모델을 다음과 같이 쓸 수 있다.

$$
\begin{bmatrix}
y_1\\y_2\\\vdots\\y_N
\end{bmatrix}
\approx
\begin{bmatrix}
x_1&1\\x_2&1\\\vdots&\vdots\\x_N&1
\end{bmatrix}
\begin{bmatrix}a\\b\end{bmatrix}
$$

간단히 쓰면

$$
[\boldsymbol y]\approx[\boldsymbol A][\boldsymbol c]
$$

이다. 여기서 $\boldsymbol c=[a,b]^T$다. 데이터가 직선 위에 정확히 놓이지 않으면 모든
식을 동시에 정확히 만족하는 해가 없을 수 있다. <code>np.linalg.lstsq()</code>는
$\|[\boldsymbol y]-[\boldsymbol A][\boldsymbol c]\|_2^2$를 가장 작게 만드는 해를 구한다.

~~~python
design_matrix = np.column_stack((x, np.ones(x.size)))
coefficients, _, _, _ = np.linalg.lstsq(
    design_matrix,
    y,
    rcond=None,
)

print(f"Slope: {coefficients[0]:.3f}")
print(f"Intercept: {coefficients[1]:.3f}")
~~~

이 결과는 <code>np.polyfit()</code> 결과와 같다. 직접 역행렬을 계산하기보다
<code>np.linalg.lstsq()</code>처럼 최소제곱 문제를 풀도록 만들어진 함수를 사용하는 것이
수치적으로 더 적절하다.

# 11. 적합할 때 주의할 점

- $x$와 $y$ 배열의 길이가 같은지 확인한다.
- 축 이름과 물리량의 단위를 표시한다.
- 직선 모델이 적절한 구간만 선택한다.
- 이상치 하나가 제곱 때문에 결과에 큰 영향을 줄 수 있다.
- 적합 직선만 보지 말고 원래 측정점과 잔차도 함께 확인한다.
- 데이터 범위 밖으로 멀리 외삽한 결과는 신뢰하기 어렵다.
- 좋은 적합이 곧 원인과 결과의 관계를 증명하는 것은 아니다.
- 절편을 0으로 고정할지는 물리법칙과 측정 조건을 함께 고려하여 결정한다.

# 12. 핵심 정리

- 잔차는 측정값과 예측값의 차이 $e_i=y_i-\widehat y_i$이다.
- 최소제곱법은 잔차제곱합 $S=\sum_i e_i^2$를 최소화한다.
- 직선 $\widehat y=ax+b$에서 $a$는 기울기이고 $b$는 절편이다.
- <code>np.polyfit(x, y, 1)</code>로 직선을 간단히 적합할 수 있다.
- RMSE는 잔차의 대표적인 크기를 $y$와 같은 단위로 나타낸다.
- 응력–변형률 탄성구간의 기울기로 영률을 추정할 수 있다.
- 행렬 형태의 일반적인 최소제곱 문제는 <code>np.linalg.lstsq()</code>로 풀 수 있다.

# 13. 연습 문제

## 문제 1

측정값이 $y_i=5$이고 모델의 예측값이 $\widehat y_i=4$일 때 잔차를 구하시오.

<!--
풀이와 해답:
e_i = y_i - yhat_i = 5 - 4 = 1이다.
-->

## 문제 2

잔차를 단순히 더하지 않고 제곱하여 더하는 이유를 하나 설명하시오.

<!--
풀이와 해답:
양의 잔차와 음의 잔차가 서로 상쇄되는 것을 막기 위해서다.
-->

## 문제 3

잔차가 $[-1,2,-1]$일 때 잔차제곱합을 구하시오.

<!--
풀이와 해답:
SSE = (-1)^2 + 2^2 + (-1)^2 = 6이다.
-->

## 문제 4

<code>np.polyfit(x, y, 1)</code>의 마지막 숫자 1은 무엇을 의미하는가?

<!--
풀이와 해답:
적합할 다항식의 차수가 1, 즉 직선이라는 뜻이다.
-->

## 문제 5

직선 $\widehat y=3x+2$에서 기울기와 절편을 각각 쓰고, $x=4$일 때 예측값을 구하시오.

<!--
풀이와 해답:
기울기는 3, 절편은 2이다. x = 4일 때 yhat = 3(4) + 2 = 14이다.
-->

## 문제 6

탄성구간의 응력–변형률 직선 기울기가 200000 MPa이다. 이를 GPa로 나타내시오.

<!--
풀이와 해답:
1000 MPa = 1 GPa이므로 200000 MPa = 200 GPa이다.
-->

## 문제 7

잔차 그래프가 뚜렷한 곡선 모양을 보인다면 직선 모델에 관해 무엇을 의심할 수 있는가?

<!--
풀이와 해답:
데이터의 관계가 직선이 아니어서 직선 모델이 적절하지 않을 가능성을 의심할 수 있다.
-->

## 문제 8

영률을 구할 때 소성변형 구간까지 포함하면 안 되는 이유를 설명하시오.

<!--
풀이와 해답:
영률은 탄성구간의 응력과 변형률 사이 기울기이며, 소성구간은 Hooke 법칙의 직선관계를
따르지 않기 때문이다.
-->
