---
layout: page
title: 수치해석
description: 재료공학도를 위한 수치해석
target: 2학년 1학기
permalink:
prerequisite: Newton–Raphson 방법 1, Taylor 급수
toc:
  sidebar: left
---

- [1. 학습 목표](#1-학습-목표)
- [2. Newton–Raphson 방법 복습](#2-newtonraphson-방법-복습)
- [3. Taylor 전개를 이용한 유도](#3-taylor-전개를-이용한-유도)
- [4. 수렴이 빠른 이유](#4-수렴이-빠른-이유)
- [5. 예제: $x^2+x=10$](#5-예제-x2x10)
  - [5.1. 반복식](#51-반복식)
  - [5.2. 초기값의 영향](#52-초기값의-영향)
  - [5.3. Python 구현](#53-python-구현)
- [6. 실패할 수 있는 경우](#6-실패할-수-있는-경우)
  - [6.1. 도함수가 0인 경우](#61-도함수가-0인-경우)
  - [6.2. 근 사이에서 반복하는 경우](#62-근-사이에서-반복하는-경우)
  - [6.3. 정의역을 벗어나는 경우](#63-정의역을-벗어나는-경우)
- [7. 이계도함수를 이용하는 방법](#7-이계도함수를-이용하는-방법)
  - [7.1. 2차 Taylor 모델](#71-2차-taylor-모델)
  - [7.2. Halley 방법](#72-halley-방법)
- [8. Newton 방법과 Halley 방법 비교](#8-newton-방법과-halley-방법-비교)
- [9. 정리](#9-정리)
- [10. 연습 문제](#10-연습-문제)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- Taylor 전개에서 Newton–Raphson 반복식을 유도할 수 있다.
- Newton–Raphson 방법이 근 근처에서 빠르게 수렴하는 이유를 설명할 수 있다.
- 초기값을 바꾸어 서로 다른 근을 구할 수 있다.
- Newton–Raphson 방법이 실패할 수 있는 경우를 설명할 수 있다.
- 2차 Taylor 모델과 Halley 방법을 표준 Newton 방법과 구분할 수 있다.

# 2. Newton–Raphson 방법 복습

방정식

$$
f(x)=0
$$

의 근을 구하기 위한 Newton–Raphson 반복식은 다음과 같다.

$$
\boxed{
x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}
}
$$

현재 근삿값 $x_k$에서 접선을 그리고, 그 접선이 $x$축과 만나는 점을 다음
근삿값 $x_{k+1}$로 사용한다. 좋은 초기값에서 시작하면 이분법보다 훨씬 적은
반복으로 정확한 근삿값을 얻을 수 있다.

다만 다음 조건을 자동으로 만족하는 것은 아니다.

- 반복값이 항상 근에 가까워진다는 보장은 없다.
- 반복 중 $f^{\prime}(x_k)=0$이면 다음 값을 계산할 수 없다.
- 여러 근이 있으면 초기값에 따라 서로 다른 근으로 수렴할 수 있다.
- 반복값이 로그나 제곱근 함수의 정의역을 벗어날 수 있다.

# 3. Taylor 전개를 이용한 유도

함수 $f(x)$를 현재 근삿값 $x_k$ 주변에서 Taylor 전개하면

$$
f(x_k+h)
=f(x_k)+f'(x_k)h
+\frac{1}{2}f''(x_k)h^2
+\frac{1}{6}f'''(x_k)h^3+\cdots
$$

이다. 여기서

$$
h=x-x_k
$$

는 현재점에서 새로운 점까지의 변화량이다.

Newton–Raphson 방법은 1차항까지만 사용하여 함수를 접선으로 근사한다.

$$
f(x_k+h)\approx f(x_k)+f'(x_k)h
$$

새로운 점이 근이라고 가정하여 왼쪽을 0으로 놓으면

$$
0\approx f(x_k)+f'(x_k)h
$$

이고,

$$
h\approx-\frac{f(x_k)}{f'(x_k)}
$$

을 얻는다. 따라서 $x_{k+1}=x_k+h$를 사용하면

$$
x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}
$$

이 된다. 접선을 이용한 기하학적 설명과 Taylor 1차 근사는 같은 반복식을 준다.

# 4. 수렴이 빠른 이유

참근을 $x^{\ast}$라고 하고 $f(x^{\ast})=0$,
$f^{\prime}(x^{\ast})\ne0$인 **단순근**이라고 하자.
근에 충분히 가까운 곳에서 Newton–Raphson 방법을 적용하면 대략

$$
|x^*-x_{k+1}|\approx
C|x^*-x_k|^2
$$

의 관계가 나타난다. 여기서 $C$는 함수와 근에 따라 결정되는 상수이다.
즉, 현재 오차가 작을 때 다음 오차는 현재 오차의 제곱에 비례한다. 이를
**이차수렴(quadratic convergence)**이라고 한다.[^quadratic-convergence]

예를 들어 현재 오차가 약 $10^{-2}$라면 다음 오차는 대략 $10^{-4}$ 크기,
그다음 오차는 대략 $10^{-8}$ 크기로 줄어들 수 있다. 이 성질은 초기값이
근에 충분히 가깝고 도함수가 0이 아닌 경우에 기대할 수 있다.

# 5. 예제: $x^2+x=10$

방정식을 $f(x)=0$ 형태로 바꾸면

$$
f(x)=x^2+x-10=0
$$

이고 도함수는

$$
f'(x)=2x+1
$$

이다. 이 방정식의 정확한 두 근은

$$
x=\frac{-1\pm\sqrt{41}}{2}
$$

이다.

## 5.1. 반복식

Newton–Raphson 반복식은 다음과 같다.

$$
x_{k+1}
=x_k-\frac{x_k^2+x_k-10}{2x_k+1}
$$

초기값 $x_0=1$에서 계산하면 다음과 같다.

| $k$ | $x_k$ | $|f(x_k)|$ |
|---:|---:|---:|
| 0 | 1.000000000 | 8.000000000 |
| 1 | 3.666666667 | 7.111111111 |
| 2 | 2.813333333 | 0.728177778 |
| 3 | 2.703447351 | 0.012074929 |
| 4 | 2.701562673 | $3.5520\times10^{-6}$ |
| 5 | 2.701562119 | $3.09\times10^{-13}$ |

양의 근

$$
x^*=\frac{-1+\sqrt{41}}{2}\approx2.701562119
$$

에 빠르게 가까워지는 것을 확인할 수 있다.

## 5.2. 초기값의 영향

같은 함수에서 $x_0=-5$로 시작하면 음의 근으로 수렴한다.

$$
x^*=\frac{-1-\sqrt{41}}{2}\approx-3.701562119
$$

$x_0=1$은 양의 근에, $x_0=-5$는 음의 근에 비교적 가까운 초기값이다.
초기값은 반복 과정과 최종적으로 도달하는 근을 결정할 수 있다. 두 초기값의
계산 결과는 다음 절의 코드로 직접 확인한다.

## 5.3. Python 구현

앞 강의에서 작성한 **newton_raphson** 함수를 다시 정의하여 사용한다.

~~~python
import numpy as np
import matplotlib.pyplot as plt

def newton_raphson(f, df, x0, tol=1e-10, max_iter=50):
    x = float(x0)
    history = [x]

    for iteration in range(max_iter+1):
        fx = f(x)

        if abs(fx) <= tol:
            return x, iteration, history

        if iteration == max_iter:
            break

        dfx = df(x)
        if abs(dfx) < 1e-14:
            raise ZeroDivisionError("도함수가 0에 너무 가까워 계산할 수 없습니다.")

        x = x-fx/dfx
        history.append(x)

    raise RuntimeError("최대 반복 횟수 안에 수렴하지 않았습니다.")

def f(x):
    return x**2+x-10

def df(x):
    return 2*x+1

root, iterations, history = newton_raphson(f, df, x0=1.0)

print("root:", root)
print("f(root):", f(root))
print("iterations:", iterations)

for x0 in [1.0, -5.0]:
    root, iterations, history = newton_raphson(f, df, x0)
    print("x0 =", x0, "root =", root, "iterations =", iterations)
~~~

반복에 따른 잔차를 그려보자.

~~~python
root, iterations, history = newton_raphson(f, df, x0=1.0)
history = np.array(history)
residuals = np.abs(f(history))

plt.semilogy(range(len(history)), residuals, "o-")
plt.xlabel("iteration")
plt.ylabel(r"$|f(x_n)|$")
plt.grid()
plt.show()
~~~

# 6. 실패할 수 있는 경우

## 6.1. 도함수가 0인 경우

$f(x)=x^3-1$에서 $x_0=0$을 선택하면

$$
f'(x)=3x^2,
\qquad
f'(0)=0
$$

이므로 첫 번째 반복을 계산할 수 없다.

## 6.2. 근 사이에서 반복하는 경우

함수와 초기값에 따라 반복값이 두 점 사이를 계속 오갈 수도 있다. 예를 들어

$$
f(x)=x^3-2x+2
$$

에 $x_0=0$을 사용하면

$$
x_1=1,
\qquad
x_2=0,
\qquad
x_3=1,\ldots
$$

이 되어 수렴하지 않는다.

## 6.3. 정의역을 벗어나는 경우

$f(x)=\ln x-1$은 $x>0$에서만 정의된다. 반복값이 0 이하가 되면 함수값과
도함수를 계산할 수 없다.

Newton–Raphson 방법을 사용할 때는 그래프를 그려 근의 위치를 예상하고, 반복 횟수의
상한을 두며, 도함수와 함수의 정의역을 확인해야 한다.

# 7. 이계도함수를 이용하는 방법

## 7.1. 2차 Taylor 모델

Taylor 전개의 2차항까지 유지하면

$$
f(x_n+h)
\approx f(x_n)+f'(x_n)h+\frac{1}{2}f''(x_n)h^2
$$

이다. 오른쪽을 0으로 놓고 $h$에 관한 이차방정식을 풀면

$$
h=
\frac{-f'(x_n)\pm
\sqrt{[f'(x_n)]^2-2f(x_n)f''(x_n)}}
{f''(x_n)}
$$

을 얻는다. 이를 이용한 갱신은

$$
x_{n+1}=x_n+h
$$

이다.

이 방법은 표준 Newton–Raphson 방법과 구분해야 한다. 다음과 같은 추가 문제가 있다.

- 두 해 중 어느 $h$를 선택할지 정해야 한다.
- 판별식이 음수이면 실수 범위에서 $h$를 계산할 수 없다.
- $f^{\prime\prime}(x_n)=0$이면 위 식을 직접 사용할 수 없다.
- 제곱근을 포함하므로 반올림에 의한 소거 오차가 생길 수 있다.

따라서 이번 강의에서는 개념적인 2차 근사로 이해하고, 기본 근 찾기에는 표준
Newton–Raphson 방법을 사용한다.

## 7.2. Halley 방법

이계도함수를 이용하는 대표적인 근 찾기 방법으로 Halley 방법이 있다.

$$
\boxed{
x_{n+1}
=x_n-
\frac{2f(x_n)f'(x_n)}
{2[f'(x_n)]^2-f(x_n)f''(x_n)}
}
$$

Halley 방법은 조건이 좋으면 근 근처에서 삼차수렴을 보일 수 있지만, 이계도함수를
계산해야 하고 분모가 0에 가까워질 수 있다는 단점이 있다. 따라서 Newton 방법보다
항상 효율적인 것은 아니다.

# 8. Newton 방법과 Halley 방법 비교

$f(x)=x^3-2$의 양의 근을 $x_0=1$에서 구해보자.

$$
f'(x)=3x^2,
\qquad
f''(x)=6x
$$

~~~python
def f(x):
    return x**3-2

def df(x):
    return 3*x**2

def ddf(x):
    return 6*x

def halley(f, df, ddf, x0, tol=1e-10, max_iter=50):
    x = float(x0)
    history = [x]

    for iteration in range(max_iter+1):
        fx = f(x)

        if abs(fx) <= tol:
            return x, iteration, history

        if iteration == max_iter:
            break

        dfx = df(x)
        ddfx = ddf(x)
        denominator = 2*dfx**2-fx*ddfx

        if abs(denominator) < 1e-14:
            raise ZeroDivisionError("분모가 0에 너무 가까워 계산할 수 없습니다.")

        x = x-2*fx*dfx/denominator
        history.append(x)

    raise RuntimeError("최대 반복 횟수 안에 수렴하지 않았습니다.")

root_newton, n_newton, hist_newton = newton_raphson(f, df, 1.0)
root_halley, n_halley, hist_halley = halley(f, df, ddf, 1.0)

print("Newton:", root_newton, n_newton)
print("Halley:", root_halley, n_halley)
~~~

허용 잔차를 $10^{-10}$으로 설정하면 일반적인 배정밀도 환경에서 Newton 방법은
5회, Halley 방법은 3회 갱신하여 $\sqrt[3]{2}\approx1.25992105$에 도달한다.
한 반복 횟수만 비교하기보다 각 반복에 필요한 도함수 계산 비용도 함께 고려해야 한다.

# 9. 정리

- Newton–Raphson 방법은 Taylor 전개의 1차항까지 사용한 근사에서 유도할 수 있다.
- 단순근 근처에서는 오차가 제곱에 비례하여 줄어드는 이차수렴을 기대할 수 있다.
- 초기값에 따라 다른 근에 수렴하거나 수렴에 실패할 수 있다.
- 2차 Taylor 모델을 직접 푸는 방법은 표준 Newton–Raphson 방법과 다르다.
- Halley 방법은 이계도함수를 사용하며 조건이 좋으면 삼차수렴할 수 있다.

# 10. 연습 문제

강의의 식을 직접 적용하는 기초 문제이다.

1. 다음 빈칸을 채워라.

   $$
   f(x_n+h)
   \approx f(x_n)+(　　　　　　　　)h
   $$

   이 식에서 $f(x_n+h)=0$으로 놓으면

   $$
   h\approx-\frac{(　　　　　　　　)}{(　　　　　　　　)}
   $$

   을 얻는다.

   <!--
   풀이 및 정답:
   첫 번째 빈칸은 f'(x_n)이다. h=-f(x_n)/f'(x_n)이므로 다음 두 빈칸은
   각각 f(x_n), f'(x_n)이다.
   -->

2. $f(x)=x^2+x-10$의 도함수를 구하고, $x_0=1$에서 $x_1$을 계산하라.

   <!--
   풀이 및 정답:
   f'(x)=2x+1이다.
   x_1=1-(1^2+1-10)/(2×1+1)=1-(-8)/3=11/3≈3.6667이다.
   -->

3. 같은 함수에서 $x_1=11/3$일 때 $x_2$를 계산하라.

   <!--
   풀이 및 정답:
   f(11/3)=64/9이고 f'(11/3)=25/3이다.
   x_2=11/3-(64/9)/(25/3)=11/3-64/75=211/75≈2.8133이다.
   -->

4. $f(x)=x^3-1$과 초기값 $x_0=0$에서 Newton–Raphson 반복식을 바로
   적용할 수 없는 이유를 설명하라.

   <!--
   풀이 및 정답:
   f'(x)=3x^2이고 f'(0)=0이다. 반복식에서 f'(x_0)로 나누어야 하므로
   분모가 0이 되어 계산할 수 없다.
   -->

5. $f(x)=x^3-2x+2$와 $x_0=0$에 대해 $x_1$과 $x_2$를 계산하라.

   <!--
   풀이 및 정답:
   f'(x)=3x^2-2이다.
   x_1=0-f(0)/f'(0)=0-2/(-2)=1이다.
   x_2=1-f(1)/f'(1)=1-1/1=0이다.
   따라서 0과 1 사이를 반복하여 수렴하지 않는다.
   -->

6. 다음 설명이 Newton 방법에 해당하면 N, Halley 방법에 해당하면 H를 적어라.

   1. 일계도함수만 필요하다. (　　)
   2. 이계도함수도 필요하다. (　　)
   3. 조건이 좋으면 근 근처에서 이차수렴한다. (　　)
   4. 조건이 좋으면 근 근처에서 삼차수렴할 수 있다. (　　)

   <!--
   풀이 및 정답: 1번 N, 2번 H, 3번 N, 4번 H이다.
   -->

7. 강의의 **newton_raphson** 함수를 사용하여 $x^2+x-10=0$을 계산하라.

   1. $x_0=1$에서 시작한다.
   2. $x_0=-5$에서 시작한다.
   3. 두 초기값에서 얻은 근을 비교한다.

   <!--
   풀이 및 정답:
   x_0=1에서는 약 2.701562119, x_0=-5에서는 약 -3.701562119에 수렴한다.
   초기값에 따라 서로 다른 근으로 수렴한다.
   -->

8. 다음 중 Newton–Raphson 방법을 사용할 때 확인할 사항을 모두 고르라.

   1. 도함수가 0에 가까운가?
   2. 반복값이 함수의 정의역 안에 있는가?
   3. 최대 반복 횟수를 설정했는가?
   4. 함수값과 도함수를 올바르게 작성했는가?

   <!--
   풀이 및 정답:
   네 항목 모두 확인해야 한다.
   -->

[^quadratic-convergence]: 참근을 $x^{\ast}$, 현재 오차를
    $e_k=x_k-x^{\ast}$라고 하자. $f(x^{\ast})=0$이고
    $f^{\prime}(x^{\ast})\ne0$인 단순근 주변에서 Taylor 정리를 적용하면,
    $x_k$과 $x^{\ast}$ 사이의 어떤 점 $\xi_k$에 대하여 다음 관계를 얻는다.

    $$
    e_{k+1}
    =\frac{f^{\prime\prime}(\xi_k)}{2f^{\prime}(x_k)}e_k^2
    $$

    근 주변에서 $f^{\prime\prime}$이 유계이고 $f^{\prime}$이 0에서 떨어져
    있으면 $|e_{k+1}|\leq C|e_k|^2$이므로 이차수렴한다. 특히
    $f(x)=x^2-2$에서는 다음 식이 정확히 성립한다.

    $$
    e_{k+1}=\frac{e_k^2}{2x_k}
    $$

    이 결과는 초기값이 단순근에 충분히 가까울 때 적용된다. 중근에서는 일반적으로
    이차수렴하지 않는다.
