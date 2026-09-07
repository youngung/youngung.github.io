---
layout: page
title: 벌점법
description: 제약조건이 있는 최적화 문제를 위한 penalty method
target: 2학년 1학기
permalink:
prerequisite: 경사하강법, 함수의 미분, Python 기초
toc:
  sidebar: left
---

- [1. 학습 목표](#1-학습-목표)
- [2. 제약조건이 있는 최적화](#2-제약조건이-있는-최적화)
- [3. 벌점법의 기본 원리](#3-벌점법의-기본-원리)
  - [3.1. 등식 제약조건](#31-등식-제약조건)
  - [3.2. 벌점계수의 역할](#32-벌점계수의-역할)
- [4. 손으로 계산하는 예제](#4-손으로-계산하는-예제)
- [5. 경사하강법으로 풀기](#5-경사하강법으로-풀기)
- [6. 두 변수 예제](#6-두-변수-예제)
- [7. 부등식 제약조건](#7-부등식-제약조건)
- [8. 벌점계수를 증가시키는 방법](#8-벌점계수를-증가시키는-방법)
- [9. 벌점법의 장점과 주의점](#9-벌점법의-장점과-주의점)
- [10. 정리](#10-정리)
- [11. 연습 문제](#11-연습-문제)
  - [문제 1. 목적함수와 제약조건](#문제-1-목적함수와-제약조건)
  - [문제 2. 가능점 판단](#문제-2-가능점-판단)
  - [문제 3. 벌점항 계산](#문제-3-벌점항-계산)
  - [문제 4. 벌점함수 만들기](#문제-4-벌점함수-만들기)
  - [문제 5. 벌점계수 비교](#문제-5-벌점계수-비교)
  - [문제 6. 손으로 최솟점 구하기](#문제-6-손으로-최솟점-구하기)
  - [문제 7. Python 실습](#문제-7-python-실습)
  - [문제 8. 결과 해석](#문제-8-결과-해석)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 목적함수와 제약조건을 구분할 수 있다.
- 벌점법(penalty method)의 기본 생각을 설명할 수 있다.
- 등식 제약조건을 벌점항으로 바꿀 수 있다.
- 벌점계수의 크기가 해와 수치 계산에 미치는 영향을 설명할 수 있다.
- 간단한 벌점함수를 경사하강법으로 최소화할 수 있다.

# 2. 제약조건이 있는 최적화

경사하강법에서는 다음과 같이 목적함수 $f(\boldsymbol{x})$를 가장 작게 만드는
$\boldsymbol{x}$를 찾았다.

$$
\min_{\boldsymbol{x}} f(\boldsymbol{x})
$$

이처럼 모든 $\boldsymbol{x}$를 후보로 허용하는 문제를 **제약조건이 없는
최적화**(unconstrained optimization)라고 한다.

그러나 실제 공학 문제에서는 설계변수가 반드시 만족해야 하는 조건이 자주
등장한다. 예를 들면 다음과 같다.

- 두 합금 원소의 조성 합이 정해진 값과 같아야 한다.
- 재료의 질량은 허용 질량보다 작아야 한다.
- 계산된 응력은 허용응력을 넘지 않아야 한다.

등식 제약조건이 있는 문제는

$$
\begin{aligned}
\min_{\boldsymbol{x}} \quad & f(\boldsymbol{x}) \\
\text{subject to} \quad & h(\boldsymbol{x})=0
\end{aligned}
$$

과 같이 쓴다. 여기서

- $f(\boldsymbol{x})$: 가장 작게 만들고 싶은 **목적함수**(objective function)
- $h(\boldsymbol{x})=0$: 반드시 만족해야 하는 등식 **제약조건**(constraint)

이다. 제약조건을 만족하는 점을 **가능점**(feasible point)이라고 한다.

# 3. 벌점법의 기본 원리

벌점법에서는 제약조건을 어긴 정도만큼 목적함수에 큰 값을 더한다. 그러면
제약조건을 많이 위반한 점은 최소화 과정에서 불리해진다.

> 제약조건을 지키면 벌점(penalty)이 작고, 제약조건을 어기면 벌점이 커진다.

이 방법을 사용하면 제약조건이 있는 문제를 앞에서 배운 경사하강법으로 풀 수
있는 제약조건 없는 문제로 바꿀 수 있다.

## 3.1. 등식 제약조건

등식 제약조건 $h(\boldsymbol{x})=0$에 대해 가장 간단한 이차(2nd order) 벌점항은

$$
\frac{\rho}{2}\left[h(\boldsymbol{x})\right]^{\textcolor{red}{2}}
$$

이다. 원래 목적함수$f(x)$에 이 항을 더한 **벌점함수**(penalty function)를

$$
\boxed{
P(\boldsymbol{x};\rho)
=f(\boldsymbol{x})
+\frac{\rho}{2}\left[h(\boldsymbol{x})\right]^2
}
$$

로 정의한다. $\rho>0$는 **벌점계수**(penalty parameter)이다.

- $h(\boldsymbol{x})=0$이면 벌점항은 $0$이다.
- $h(\boldsymbol{x})\ne0$이면 벌점항은 양수이다.
- 제약조건의 위반량이 두 배가 되면 제곱된 위반량은 네 배가 된다.

따라서 원래 문제 ($\min_{\boldsymbol{x}} f(x) \text{, subject to } h(x)=0$) 대신

$$
\min_{\boldsymbol{x}}P(\boldsymbol{x};\rho)
$$

를 푼다.

만약 여러 개의 등식 제약조건 $h_j(\boldsymbol{x})=0$이 있다면 개별 제약 조건에 의한 벌점항을 모두
더한다.

$$
P(\boldsymbol{x};\rho)
=f(\boldsymbol{x})
+\frac{\rho}{2}\sum_{j=1}^{m}
\left[h_j(\boldsymbol{x})\right]^2
$$

## 3.2. 벌점계수의 역할

벌점계수 $\rho$가 작으면 목적함수를 줄이는 것이 더 중요하고, 제약조건을 어느 정도
위반해도 허용될 수 있다. $\rho$가 커지면 제약조건 위반에 더 큰 벌점을 부과하고 따라서
제약 조건이 더욱 엄밀하게 요구된다.

$$
\rho\uparrow
\quad\Longrightarrow\quad
|h(\boldsymbol{x})|\downarrow
$$

그러나 유한한 $\rho$에서는 일반적으로 제약조건을 정확히 만족하지 않고 조금
위반할 수 있다. 또한 $\rho$를 처음부터 지나치게 크게 정하면 벌점함수의
기울기($\dfrac{dP}{dx}$)가 매우 커져 경사하강법의 학습률을 작게 설정해야 할 수 있다.

# 4. 손으로 계산하는 예제

다음 문제를 생각하자.

$$
\begin{aligned}
\min_x \quad & f(x)=(x-2)^2 \\
\text{subject to} \quad & h(x)=x-1=0
\end{aligned}
$$

목적함수만 생각하면 최솟점은 $x=2$이다. 그러나 제약조건을 만족하는 점은
$x=1$뿐이므로 원래 제약 최적화 문제의 해는 $x^*=1$이다.

이차 벌점함수는

$$
P(x;\rho)=(x-2)^2+\frac{\rho}{2}(x-1)^2
$$

이다. 미분하여 $0$으로 놓으면

$$
\frac{dP}{dx}=2(x-2)+\rho(x-1)=0
$$

이고, 아래와 같이 전개된다.

$$
(2+\rho)x-4-\rho=0
$$

위 조건을 만족시키는 벌점함수의 최솟점은

$$
\boxed{x_\rho=\frac{4+\rho}{2+\rho}}
$$

이다.

| $\rho$ | $x_\rho$ | 제약조건 위반량 $|x_{\rho}-1|$ |
|---:|---:|---:|
| 1 | 1.6667 | 0.6667 |
| 10 | 1.1667 | 0.1667 |
| 100 | 1.0196 | 0.0196 |
| 1000 | 1.0020 | 0.0020 |

$\rho$가 커질수록 $x_\rho$가 제약조건의 해 $x=1$에 가까워지는 것을 확인할
수 있다. 수학적으로는

$$
\lim_{\rho\rightarrow\infty}x_\rho=1
$$

이다.

# 5. 경사하강법으로 풀기

위 벌점함수를 [경사하강법]({% link assets/lecture_notes/2_1_numerical_analysis/numerical_analysis_10_GradientDescent.md %})으로 최소화해 보자. 반복식은

$$
x^{(k+1)}
=x^{(k)}-\alpha\frac{dP}{dx}\left(x^{(k)};\rho\right)
$$

이다. 여기서

$$
\frac{dP}{dx}=2(x-2)+\rho(x-1)
$$

이다.

```python
def penalty_gradient(x, rho):
    return 2.0*(x - 2.0) + rho*(x - 1.0)


def gradient_descent_penalty(x0, rho, alpha, tol=1e-10,
                             max_iter=10000):
    x = float(x0)

    for iteration in range(max_iter):
        grad = penalty_gradient(x, rho)

        if abs(grad) < tol:
            return x, iteration

        x = x - alpha*grad

    raise RuntimeError("최대 반복 횟수 안에 수렴하지 않았습니다.")


for rho in [1.0, 10.0, 100.0]:
    # rho가 커질수록 작은 학습률을 사용한다.
    alpha = 1.0/(rho + 2.0)
    x, n_iter = gradient_descent_penalty(
        x0=0.0,
        rho=rho,
        alpha=alpha,
    )

    print(
        f"rho={rho:5.1f}, x={x:.6f}, "
        f"constraint error={abs(x - 1.0):.6f}"
    )
```

예상되는 결과는 다음과 같다.

```text
rho=  1.0, x=1.666667, constraint error=0.666667
rho= 10.0, x=1.166667, constraint error=0.166667
rho=100.0, x=1.019608, constraint error=0.019608
```

이 예제의 벌점함수는 이차함수이므로 적절한 학습률을 사용하면 쉽게 수렴한다.
일반적인 비선형 문제에서는 $\rho$와 학습률을 함께 조절해야 한다.

# 6. 두 변수 예제

두 설계변수 $x$, $y$의 합이 $4$가 되어야 하는 문제를 생각하자.

$$
\begin{aligned}
\min_{x,y} \quad
& f(x,y)=(x-3)^2+(y-2)^2 \\
\text{subject to} \quad
& h(x,y)=x+y-4=0
\end{aligned}
$$

벌점함수는

$$
P(x,y;\rho)
=(x-3)^2+(y-2)^2
+\frac{\rho}{2}(x+y-4)^2
$$

이다. 기울기는

$$
\nabla P(x,y;\rho)=
\begin{bmatrix}
2(x-3)+\rho(x+y-4)\\
2(y-2)+\rho(x+y-4)
\end{bmatrix}
$$

이다. 따라서 앞에서 배운 경사하강법의 반복식을 그대로 사용할 수 있다.

```python
import numpy as np


def penalty_gradient_2d(point, rho):
    x, y = point
    constraint = x + y - 4.0

    return np.array([
        2.0*(x - 3.0) + rho*constraint,
        2.0*(y - 2.0) + rho*constraint,
    ])


def solve_penalty_2d(x0, rho, alpha, tol=1e-8,
                     max_iter=10000):
    point = np.asarray(x0, dtype=float).copy()

    for iteration in range(max_iter):
        grad = penalty_gradient_2d(point, rho)

        if np.linalg.norm(grad) < tol:
            return point, iteration

        point = point - alpha*grad

    raise RuntimeError("최대 반복 횟수 안에 수렴하지 않았습니다.")


for rho in [1.0, 10.0, 100.0]:
    point, n_iter = solve_penalty_2d(
        x0=[0.0, 0.0],
        rho=rho,
        alpha=0.4/(1.0 + rho),
    )
    violation = point[0] + point[1] - 4.0

    print(
        f"rho={rho:5.1f}, point={point}, "
        f"h(x,y)={violation:.6f}"
    )
```

원래 제약 최적화 문제의 정확한 해는 $(x,y)=(2.5,1.5)$이다. $\rho$를
증가시키면 벌점법으로 구한 점이 이 해에 가까워진다.

# 7. 부등식 제약조건

부등식 제약조건은 보통

$$
g(\boldsymbol{x})\leq0
$$

의 형태로 통일하여 쓴다. 조건을 만족하면 $g(\boldsymbol{x})\leq0$이고,
위반하면 $g(\boldsymbol{x})>0$이다. 따라서 양수인 위반 부분에만 벌점을 주는

$$
\boxed{
P(\boldsymbol{x};\rho)
=f(\boldsymbol{x})
+\frac{\rho}{2}
\left[\max\left(0,g(\boldsymbol{x})\right)\right]^2
}
$$

를 사용할 수 있다.

예를 들어 $x\geq1$이라는 조건은

$$
g(x)=1-x\leq0
$$

으로 바꾼다. 이때 벌점항은

$$
\frac{\rho}{2}[\max(0,1-x)]^2
$$

이다.

- $x=1.5$이면 조건을 만족하므로 벌점은 $0$이다.
- $x=0.8$이면 위반량은 $0.2$이고 벌점은 $\rho(0.2)^2/2$이다.

부등식 제약조건의 경계에서는 함수의 미분을 주의해서 다루어야 한다. 이번
강의에서는 제약조건을 위반한 부분에만 벌점을 준다는 생각까지만 익힌다.

# 8. 벌점계수를 증가시키는 방법

실제 계산에서는 매우 큰 $\rho$ 하나를 처음부터 사용하기보다, 작은 값에서
시작하여 점차 증가시키는 방법을 사용할 수 있다.

1. 비교적 작은 $\rho$를 선택한다.
2. 현재 벌점함수를 최소화한다.
3. 제약조건 위반량 $|h(\boldsymbol{x})|$을 계산한다.
4. 위반량이 허용오차보다 크면 $\rho$를 증가시킨다.
5. 이전 단계의 해를 새로운 초기값으로 사용하여 다시 최소화한다.

이를 간단히 나타내면 다음과 같다.

```python
x = initial_value

for rho in [1.0, 10.0, 100.0, 1000.0]:
    x = minimize_penalty(x, rho)

    if abs(constraint(x)) < constraint_tolerance:
        break
```

위 코드는 전체 흐름을 설명하기 위한 의사 코드이다. `minimize_penalty`에는
경사하강법과 같은 최소화 알고리듬을 사용할 수 있다.

# 9. 벌점법의 장점과 주의점

| 항목 | 내용 |
|---|---|
| 장점 | 제약조건이 있는 문제를 익숙한 제약조건 없는 최소화 문제로 바꿀 수 있다. |
| 장점 | 목적함수와 제약조건의 식만 알면 비교적 쉽게 구현할 수 있다. |
| 주의점 | 유한한 $\rho$에서는 제약조건을 정확히 만족하지 않을 수 있다. |
| 주의점 | $\rho$가 너무 작으면 제약조건 위반이 크다. |
| 주의점 | $\rho$가 너무 크면 함수가 가파르게 변하여 수치 계산이 어려워질 수 있다. |
| 주의점 | 목적함수와 제약조건의 단위나 크기가 크게 다르면 적절한 크기 조정이 필요하다. |

계산 결과를 판단할 때는 목적함수의 값만 확인해서는 안 된다. 반드시
제약조건의 위반량도 함께 확인해야 한다.

$$
\text{목적함수값}: f(\boldsymbol{x}),
\qquad
\text{제약조건 위반량}: |h(\boldsymbol{x})|
$$

# 10. 정리

- 벌점법은 제약조건 위반량을 목적함수에 더하는 방법이다.
- 등식 제약조건 $h(\boldsymbol{x})=0$에는
  $\rho[h(\boldsymbol{x})]^2/2$를 벌점항으로 사용할 수 있다.
- 벌점계수 $\rho$가 커질수록 일반적으로 제약조건 위반량이 감소한다.
- 유한한 $\rho$에서는 제약조건을 조금 위반할 수 있다.
- 지나치게 큰 $\rho$는 최소화 문제를 수치적으로 어렵게 만들 수 있다.
- 계산 결과에서는 목적함수값과 제약조건 위반량을 모두 확인해야 한다.

# 11. 연습 문제

## 문제 1. 목적함수와 제약조건

다음 문제에서 목적함수와 제약조건을 각각 쓰시오.

$$
\begin{aligned}
\min_{x,y}\quad &(x-1)^2+(y-3)^2\\
\text{subject to}\quad &x+y=5
\end{aligned}
$$

<!--
풀이와 해답:
목적함수는 f(x,y)=(x-1)^2+(y-3)^2이다.
제약조건은 h(x,y)=x+y-5=0이다.
-->

## 문제 2. 가능점 판단

제약조건이 $x+y-4=0$일 때 다음 중 가능점을 모두 고르시오.

$$
(1,3),\qquad(2,1),\qquad(0,4)
$$

<!--
풀이와 해답:
(1,3)과 (0,4)는 x+y-4=0을 만족하므로 가능점이다.
(2,1)은 x+y-4=-1이므로 가능점이 아니다.
-->

## 문제 3. 벌점항 계산

$h(x)=x-2$, $\rho=10$일 때 $x=2.5$에서 이차 벌점항
$\rho[h(x)]^2/2$를 계산하시오.

<!--
풀이와 해답:
h(2.5)=2.5-2=0.5이다.
벌점항은 (10/2)*(0.5)^2=1.25이다.
-->

## 문제 4. 벌점함수 만들기

다음 제약 최적화 문제의 이차 벌점함수 $P(x;\rho)$를 쓰시오.

$$
\begin{aligned}
\min_x\quad &(x-3)^2\\
\text{subject to}\quad &x-1=0
\end{aligned}
$$

<!--
풀이와 해답:
목적함수는 f(x)=(x-3)^2이고 제약함수는 h(x)=x-1이다.
따라서 P(x;rho)=(x-3)^2+(rho/2)*(x-1)^2이다.
-->

## 문제 5. 벌점계수 비교

같은 점에서 제약조건의 위반량이 $0.2$일 때 $\rho=10$과 $\rho=100$의
이차 벌점항을 각각 계산하시오.

<!--
풀이와 해답:
rho=10이면 벌점항은 (10/2)*(0.2)^2=0.2이다.
rho=100이면 벌점항은 (100/2)*(0.2)^2=2.0이다.
rho가 10배가 되면 같은 위반량에 대한 벌점도 10배가 된다.
-->

## 문제 6. 손으로 최솟점 구하기

다음 벌점함수에서 $\rho=2$일 때 최솟점 $x$를 구하시오.

$$
P(x;\rho)=(x-2)^2+\frac{\rho}{2}(x-1)^2
$$

<!--
풀이와 해답:
rho=2이면 P'(x)=2(x-2)+2(x-1)=4x-6이다.
P'(x)=0에서 x=1.5이다.
또한 P''(x)=4>0이므로 이 점은 최솟점이다.
-->

## 문제 7. Python 실습

4절의 일변수 예제에서 $\rho=1$, $10$, $100$, $1000$에 대한
$x_\rho=(4+\rho)/(2+\rho)$와 제약조건 위반량 $|x_\rho-1|$을 Python으로
계산하시오.

<!--
풀이와 해답:
예시 코드:
for rho in [1.0, 10.0, 100.0, 1000.0]:
    x = (4.0 + rho)/(2.0 + rho)
    print(rho, x, abs(x - 1.0))

x는 차례로 약 1.666667, 1.166667, 1.019608, 1.001996이다.
제약조건 위반량은 차례로 약 0.666667, 0.166667, 0.019608, 0.001996이다.
-->

## 문제 8. 결과 해석

벌점법으로 구한 두 후보의 결과가 다음과 같다.

| 후보 | $f(\boldsymbol{x})$ | $|h(\boldsymbol{x})|$ |
|---|---:|---:|
| A | 1.0 | 0.2 |
| B | 1.1 | 0.001 |

제약조건 허용오차가 $0.01$일 때 어느 후보를 선택해야 하는지 설명하시오.

<!--
풀이와 해답:
후보 A는 목적함수값이 더 작지만 제약조건 위반량 0.2가 허용오차 0.01보다 크다.
후보 B는 위반량 0.001이 허용오차보다 작으므로 B를 선택해야 한다.
목적함수값뿐 아니라 제약조건 위반량도 함께 확인해야 한다.
-->
