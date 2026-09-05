---
layout: page
title: 다변수 Newton–Raphson 방법
description: 재료공학도를 위한 수치해석
target: 2학년 1학기
permalink:
prerequisite: Newton–Raphson 방법, 선형 연립방정식, LU 분해
toc:
  sidebar: left
---

- [1. 학습 목표](#1-학습-목표)
- [2. 비선형 연립방정식](#2-비선형-연립방정식)
- [\\boldsymbol F(\\boldsymbol x)](#boldsymbol-fboldsymbol-x)
- [\\end{bmatrix}](#endbmatrix)
- [3. Jacobian 행렬](#3-jacobian-행렬)
- [\\boldsymbol J(x,y)](#boldsymbol-jxy)
- [\\boldsymbol J(x,y)](#boldsymbol-jxy-1)
- [4. 다변수 Newton–Raphson 방법](#4-다변수-newtonraphson-방법)
  - [4.1. 선형화](#41-선형화)
- [\\Delta\\boldsymbol x^{(k)}](#deltaboldsymbol-xk)
- [\\boldsymbol x^{(k+1)}](#boldsymbol-xk1)
  - [4.2. 알고리듬](#42-알고리듬)
- [5. 손으로 계산하는 첫 번째 반복](#5-손으로-계산하는-첫-번째-반복)
- [\\boldsymbol x^{(0)}](#boldsymbol-x0)
- [\\boldsymbol F(1.5,0.5)](#boldsymbol-f1505)
- [\\end{bmatrix}](#endbmatrix-1)
- [\\boldsymbol J(1.5,0.5)](#boldsymbol-j1505)
- [\\end{bmatrix}](#endbmatrix-2)
- [\\boldsymbol x^{(1)}](#boldsymbol-x1)
- [\\end{bmatrix}](#endbmatrix-3)
- [6. Python 구현](#6-python-구현)
  - [6.1. 두 근 구하기](#61-두-근-구하기)
  - [6.2. 수렴 기록 확인](#62-수렴-기록-확인)
- [7. 세 변수로 확장](#7-세-변수로-확장)
- [\\boldsymbol F(x,y,z)](#boldsymbol-fxyz)
- [\\boldsymbol J(x,y,z)](#boldsymbol-jxyz)
- [8. 수렴과 주의 사항](#8-수렴과-주의-사항)
- [9. 경사하강법과의 차이](#9-경사하강법과의-차이)
- [10. 정리](#10-정리)
- [11. 연습 문제](#11-연습-문제)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 비선형 연립방정식을 벡터 함수 $\boldsymbol F(\boldsymbol x)=\boldsymbol0$으로 나타낼 수 있다.
- Jacobian 행렬을 편미분으로 구성할 수 있다.
- 다변수 Newton–Raphson 방법의 선형 시스템을 유도할 수 있다.
- 역행렬을 직접 계산하지 않고 갱신량을 구할 수 있다.
- Python으로 다변수 비선형 연립방정식을 풀 수 있다.
- 경사하강법과 다변수 Newton–Raphson 방법의 목적을 구분할 수 있다.

# 2. 비선형 연립방정식

두 변수 $x,y$에 관한 두 방정식을 생각해보자.

$$
\begin{aligned}
x^2+y^2&=5,\\
x-y&=1.
\end{aligned}
$$

모든 항을 왼쪽으로 옮기면

$$
f_1(x,y)=x^2+y^2-5=0
$$

$$
f_2(x,y)=x-y-1=0
$$

이다. 이를 하나의 벡터 함수로 나타내면

$$
\boldsymbol F(\boldsymbol x)
=
\begin{bmatrix}
f_1(x,y)\\
f_2(x,y)
\end{bmatrix}
=
\begin{bmatrix}
x^2+y^2-5\\
x-y-1
\end{bmatrix},
\qquad
\boldsymbol x=
\begin{bmatrix}
x\\y
\end{bmatrix}.
$$

우리가 찾는 해는

$$
\boldsymbol F(\boldsymbol x)=\boldsymbol0
$$

을 만족한다. 각 방정식은 평면에서 하나의 곡선을 나타내며, 두 곡선의 교점이
연립방정식의 해이다. 이 예제에는 $(2,1)$과 $(-1,-2)$라는 두 해가 있다.

# 3. Jacobian 행렬

Jacobian 행렬은 벡터 함수의 모든 일계 편미분을 모은 행렬이다.

$$
J_{ij}=\frac{\partial f_i}{\partial x_j}
$$

두 변수의 경우

$$
\boldsymbol J(x,y)
=
\begin{bmatrix}
\dfrac{\partial f_1}{\partial x}&
\dfrac{\partial f_1}{\partial y}\\[6pt]
\dfrac{\partial f_2}{\partial x}&
\dfrac{\partial f_2}{\partial y}
\end{bmatrix}.
$$

앞의 예제에서는

$$
\boldsymbol J(x,y)
=
\begin{bmatrix}
2x&2y\\
1&-1
\end{bmatrix}.
$$

Jacobian의 $i$번째 행은 함수 $f_i$의 기울기 벡터를 전치한 것이다.

# 4. 다변수 Newton–Raphson 방법

## 4.1. 선형화

현재 근삿값을 $\boldsymbol x^{(k)}$, 작은 변화량을
$\Delta\boldsymbol x^{(k)}$라고 하자. 벡터 함수의 1차 Taylor 근사는

$$
\boldsymbol F
\left(
\boldsymbol x^{(k)}+\Delta\boldsymbol x^{(k)}
\right)
\approx
\boldsymbol F\left(\boldsymbol x^{(k)}\right)
+
\boldsymbol J\left(\boldsymbol x^{(k)}\right)
\Delta\boldsymbol x^{(k)}
$$

이다. 새로운 점에서 함수값이 영벡터가 되도록 왼쪽을 0으로 놓으면

$$
\boxed{
\boldsymbol J\left(\boldsymbol x^{(k)}\right)
\Delta\boldsymbol x^{(k)}
=
-\boldsymbol F\left(\boldsymbol x^{(k)}\right)
}
$$

을 얻는다. 이 선형 연립방정식을 풀어 변화량을 구한 다음

$$
\boxed{
\boldsymbol x^{(k+1)}
=
\boldsymbol x^{(k)}+\Delta\boldsymbol x^{(k)}
}
$$

로 갱신한다.

$J^{-1}$을 명시적으로 계산하여 곱하기보다 가우스 소거법, LU 분해 또는
**np.linalg.solve**로 선형 시스템을 직접 푸는 것이 좋다.

## 4.2. 알고리듬

1. 초기값 $\boldsymbol x^{(0)}$와 허용오차를 정한다.
2. $\boldsymbol F(\boldsymbol x^{(k)})$와 $\boldsymbol J(\boldsymbol x^{(k)})$를 계산한다.
3. $\|\boldsymbol F(\boldsymbol x^{(k)})\|_2$가 충분히 작으면 종료한다.
4. $J\Delta\boldsymbol x=-F$를 풀어 변화량을 구한다.
5. $\boldsymbol x^{(k+1)}=\boldsymbol x^{(k)}+\Delta\boldsymbol x$로 갱신한다.
6. 최대 반복 횟수 안에서 2--5단계를 반복한다.

# 5. 손으로 계산하는 첫 번째 반복

초기값을

$$
\boldsymbol x^{(0)}
=
\begin{bmatrix}
1.5\\0.5
\end{bmatrix}
$$

로 정하자. 함수 벡터와 Jacobian은

$$
\boldsymbol F(1.5,0.5)
=
\begin{bmatrix}
1.5^2+0.5^2-5\\
1.5-0.5-1
\end{bmatrix}
=
\begin{bmatrix}
-2.5\\0
\end{bmatrix}
$$

$$
\boldsymbol J(1.5,0.5)
=
\begin{bmatrix}
3&1\\
1&-1
\end{bmatrix}
$$

이다. 따라서 변화량은

$$
\begin{bmatrix}
3&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
\Delta x\\
\Delta y
\end{bmatrix}
=
\begin{bmatrix}
2.5\\0
\end{bmatrix}
$$

을 만족한다. 두 번째 식에서 $\Delta x=\Delta y$이고, 첫 번째 식에 대입하면

$$
4\Delta x=2.5
$$

이므로

$$
\Delta x=\Delta y=0.625
$$

이다. 다음 근삿값은

$$
\boldsymbol x^{(1)}
=
\begin{bmatrix}
1.5\\0.5
\end{bmatrix}
+
\begin{bmatrix}
0.625\\0.625
\end{bmatrix}
=
\begin{bmatrix}
2.125\\1.125
\end{bmatrix}.
$$

# 6. Python 구현

~~~python
import numpy as np

def multivariate_newton(func, jacobian, x0, tol=1e-10, max_iter=50):
    x = np.asarray(x0, dtype=float).copy()
    history = [x.copy()]
    residual_history = [np.linalg.norm(func(x))]

    for iteration in range(max_iter+1):
        F = np.asarray(func(x), dtype=float)

        if np.linalg.norm(F) <= tol:
            return x, iteration, np.array(history), np.array(residual_history)

        if iteration == max_iter:
            break

        J = np.asarray(jacobian(x), dtype=float)

        try:
            dx = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError as error:
            raise np.linalg.LinAlgError(
                "Jacobian이 특이하여 변화량을 계산할 수 없습니다."
            ) from error

        x = x+dx
        history.append(x.copy())
        residual_history.append(np.linalg.norm(func(x)))

    raise RuntimeError("최대 반복 횟수 안에 수렴하지 않았습니다.")
~~~

예제의 함수와 Jacobian을 정의한다.

~~~python
def func(x):
    x1, x2 = x
    return np.array([
        x1**2+x2**2-5,
        x1-x2-1,
    ])

def jacobian(x):
    x1, x2 = x
    return np.array([
        [2*x1, 2*x2],
        [1.0,   -1.0],
    ])
~~~

## 6.1. 두 근 구하기

초기값을 바꾸어 두 근을 구해보자.

~~~python
for x0 in ([1.5, 0.5], [-0.5, -1.5]):
    root, iterations, history, residuals = multivariate_newton(
        func, jacobian, x0
    )
    print("initial:", x0)
    print("root:", root)
    print("iterations:", iterations)
    print("residual norm:", np.linalg.norm(func(root)))
~~~

첫 번째 초기값에서는 $(2,1)$, 두 번째 초기값에서는 $(-1,-2)$에 수렴한다.

## 6.2. 수렴 기록 확인

~~~python
import matplotlib.pyplot as plt

root, iterations, history, residuals = multivariate_newton(
    func, jacobian, [1.5, 0.5]
)

plt.semilogy(range(len(residuals)), residuals, "o-")
plt.xlabel("iteration")
plt.ylabel(r"$\|\boldsymbol F(\boldsymbol x^{(k)})\|_2$")
plt.grid()
plt.show()
~~~

# 7. 세 변수로 확장

변수가 세 개이면 함수 벡터와 Jacobian도 세 개의 행과 열을 갖는다. 예를 들어

$$
\boldsymbol F(x,y,z)
=
\begin{bmatrix}
x^2+y+z-3\\
x+y^2+z-3\\
x+y+z^2-3
\end{bmatrix}
$$

이면

$$
\boldsymbol J(x,y,z)
=
\begin{bmatrix}
2x&1&1\\
1&2y&1\\
1&1&2z
\end{bmatrix}.
$$

$(1,1,1)$은 $F(1,1,1)=0$을 만족하는 해이다. 앞서 작성한 함수는 벡터의
차원에 관계없이 같은 방법으로 사용할 수 있다.

~~~python
def func3(x):
    x1, x2, x3 = x
    return np.array([
        x1**2+x2+x3-3,
        x1+x2**2+x3-3,
        x1+x2+x3**2-3,
    ])

def jacobian3(x):
    x1, x2, x3 = x
    return np.array([
        [2*x1, 1.0, 1.0],
        [1.0, 2*x2, 1.0],
        [1.0, 1.0, 2*x3],
    ])

root, iterations, history, residuals = multivariate_newton(
    func3, jacobian3, [0.8, 1.2, 0.9]
)
print(root)
~~~

# 8. 수렴과 주의 사항

단일변수 Newton–Raphson 방법과 마찬가지로 단순근에 충분히 가까운 초기값에서는
빠른 수렴을 기대할 수 있다. 다변수 문제의 단순근에서는 해에서의 Jacobian이
가역행렬이어야 한다.

- 초기값에 따라 서로 다른 근으로 수렴할 수 있다.
- Jacobian이 특이하거나 거의 특이하면 변화량을 구하기 어렵다.
- 초기값이 해에서 멀면 발산하거나 예상하지 않은 근으로 이동할 수 있다.
- 함수와 Jacobian의 행·열 순서를 서로 일치시켜야 한다.
- 잔차와 변화량을 확인하고 최대 반복 횟수를 설정해야 한다.
- 실제 문제에서는 변화량에 감쇠계수 $0<\lambda\leq1$을 곱하는 감쇠 Newton
  방법을 사용하여 안정성을 높이기도 한다.

# 9. 경사하강법과의 차이

| 항목 | 경사하강법 | 다변수 Newton–Raphson 방법 |
|---|---|---|
| 목적 | 스칼라 함수 $f(\boldsymbol x)$의 최솟값 | 벡터 함수 $F(\boldsymbol x)=0$의 근 |
| 사용하는 미분 | 기울기 $\nabla f$ | Jacobian $J$ |
| 갱신량 | $-\alpha\nabla f$ | $J\Delta x=-F$의 해 |
| 선형 시스템 | 기본형에서는 필요하지 않음 | 매 반복마다 풀이 |
| 초기값 영향 | 수렴점과 속도에 영향 | 수렴하는 근과 성공 여부에 영향 |

# 10. 정리

- 비선형 연립방정식은 $F(x)=0$인 벡터 근 찾기 문제이다.
- Jacobian의 각 원소는 $J_{ij}=\partial f_i/\partial x_j$이다.
- 매 반복에서 $J\Delta x=-F$를 풀고 $x$에 $\Delta x$를 더한다.
- 역행렬을 직접 구하지 않고 선형 연립방정식을 푼다.
- 초기값과 Jacobian의 가역성이 수렴에 중요한 영향을 준다.

# 11. 연습 문제

1. 다음 벡터 함수의 Jacobian을 구하라.

   $$
   F(x,y)=
   \begin{bmatrix}
   x^2+y\\
   x-y^2
   \end{bmatrix}.
   $$

   <!--
   풀이 및 정답:
   J=[[2x,1],[1,-2y]]이다.
   -->

2. 예제의 $F(x,y)=[x^2+y^2-5,\ x-y-1]^T$에서 $F(2,1)$을 계산하라.

   <!--
   풀이 및 정답:
   F(2,1)=[4+1-5, 2-1-1]^T=[0,0]^T이므로 (2,1)은 해이다.
   -->

3. 같은 예제에서 $J(2,1)$을 구하라.

   <!--
   풀이 및 정답:
   J(2,1)=[[4,2],[1,-1]]이다.
   -->

4. 초기값 $(1.5,0.5)$에서 풀어야 하는 선형 시스템의 우변 $-F$를 구하라.

   <!--
   풀이 및 정답:
   F(1.5,0.5)=[-2.5,0]^T이므로 -F=[2.5,0]^T이다.
   -->

5. 변화량이 $\Delta x=(0.2,-0.1)^T$이고 현재점이 $x=(1,2)^T$이면 다음
   근삿값을 구하라.

   <!--
   풀이 및 정답:
   x_new=x+Delta x=(1.2,1.9)^T이다.
   -->

6. 다음 코드의 빈칸을 채워 변화량을 구하라.

   ~~~python
   dx = np.linalg.solve(____, ____)
   ~~~

   <!--
   풀이 및 정답:
   dx=np.linalg.solve(J,-F)이다.
   -->

7. Jacobian이 특이행렬이면 Newton 갱신이 어려운 이유를 한 문장으로 설명하라.

   <!--
   풀이 및 정답:
   J Delta x=-F가 유일한 변화량을 갖지 않을 수 있어 np.linalg.solve로
   Delta x를 결정할 수 없기 때문이다.
   -->

8. 경사하강법과 다변수 Newton–Raphson 방법의 목적을 각각 적어라.

   <!--
   풀이 및 정답:
   경사하강법은 스칼라 함수의 최솟값을 찾고, 다변수 Newton 방법은 벡터 함수가
   영벡터가 되는 근을 찾는다.
   -->
