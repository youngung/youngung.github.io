---
layout: page
title: 수치해석
description: 재료공학도를 위한 수치해석
target: 2학년 1학기
permalink:
prerequisite: 재료공학개론1, 데이터 재료과학
toc:
  sidebar: left
---

- [1. 컴퓨터와 수](#1-컴퓨터와-수)
- [2. 오차의 종류](#2-오차의-종류)
  - [2.1. 반올림 오차 (round-off error).](#21-반올림-오차-round-off-error)
  - [2.2. 절단 오차 (truncation error)](#22-절단-오차-truncation-error)
- [3. 예제](#3-예제)
  - [3.1. 예제: $y=e^x$](#31-예제-yex)
  - [3.2. 예제: $y=\\cos(x)$](#32-예제-ycosx)
  - [3.3. 예제: $y=\\ln(1+x)$](#33-예제-yln1x)
- [4. 오차 측정 방법](#4-오차-측정-방법)
  - [4.1. 절대 오차 (absolute error)](#41-절대-오차-absolute-error)
  - [4.2. 상대 오차 (relative error)](#42-상대-오차-relative-error)
  - [4.3. 상대 오차2](#43-상대-오차2)
  - [4.4. 수열의 오차?](#44-수열의-오차)
- [5. 예제: Maclaurin 급수를 이용한 화학퍼텐셜 근사](#5-예제-maclaurin-급수를-이용한-화학퍼텐셜-근사)
  - [5.1. 계산 예제](#51-계산-예제)
- [6. 연습 문제](#6-연습-문제)
  - [6.1. 기본 개념](#61-기본-개념)
  - [6.2. 절대 오차와 상대 오차](#62-절대-오차와-상대-오차)
  - [6.3. Taylor 급수](#63-taylor-급수)
  - [6.4. Python 실습](#64-python-실습)


# 1. 컴퓨터와 수
- 컴퓨터가 다루는 수에는 항상 오차가 있다. (한정된 메모리)
- 수의 종류
  - 정수 (integer): ..., -2, -1, 0, 1, 2, ...
  - 유리수 (rational): 분수로 나타낼 수 있는 수 (1/2, 2/3, 0.5, ...)
  - 무리수 (irrational): 소수로 끝없이 이어지는 수 (3.141592... , 1.414213..., Euler's number)
  ```python
  import numpy as np
  print('pi:',np.pi)
  # 내 컴퓨터에서는 3.141592653589793 까지만 출력되었다.
  # 여러분들 컴퓨터는 어떤가?
  print('Euler number:',np.exp(1))
  # 마찬가지로 2.718281828459045 까지만 출력되었다.
  ```

# 2. 오차의 종류

##  2.1. 반올림 오차 (round-off error).

 -메모리가 유한하므로, _유한한_ 자리수까지만 저장한다.

 예: `0.3333..`을 소수점 네자리까지만 저장하면 0.3333이 되고, 진짜 값과 '오차'가 생깁니다.

```python
a = 0.1 + 0.2
print(a)   # 0.30000000000000004
```

위 예시에서, 컴퓨터는 2진법으로 수를 저장하다 보니, 정확히 0.3이 계산되지 않고, 오차가 생깁니다.

##  2.2. 절단 오차 (truncation error)

무한한 계산 과정을 중간에 끊어서 근사(approximation)할 때 생기는 오차에요. 예를 들어, Taylor급수로 $$\sin{x}$$를 표현하면,

$$
\sin x= \sum_{n=0}^\infty\frac{(-1)^n}{(2n+1)!}x^{2n+1}
$$

따라서 만약 n=0,..,3까지만 전개해보면 아래와 같다.

$$
\sin x\approx
\frac{1}{1!}x^1
+\frac{-1^1}{3!}x^3
+\frac{(-1)^2}{5!}x^5
+\frac{-1^3}{7!}x^7
$$

우선 Factorial을 구현할 Python 함수를 구해보자.

```python
def factorial(x):
  val=1
  for i in range(1,x+1):
    val=val*i
  return val

## Test factorial function
for i in range(1,4):
  print(f'{i}! = {factorial(i)}')
```

실은 math library에 이미 factorial 함수가 존재한다.

```python
import math
math.factorial(3)
```

그 다음으로 테일러 급수를 함수로 표현해보면...

```python
def sinx_taylor(x,fin):
  val=0.
  for n in range(0,fin+1):
    term=(-1)**n/(factorial(2*n+1))*(x**(2*n+1))
    # print(f'{n}-th term: {term}')
    val+=term
  return val
```

- 테일러 항 차수에 따라 달라지는 오차의 변화를 살펴보자.
* n값의 변화에 따라서,
* 여러 x값에서 Taylor 급수와의 차이값을 그려보자.

  ```python
  import matplotlib.pyplot as plt
  import numpy as np
  xs=np.linspace(-1.5*np.pi,1.5*np.pi)

  plt.plot(xs,np.sin(xs),label='actual')
  for n in range(2,10):
    ys=sinx_taylor(xs,n)
    plt.plot(xs,ys,label=f'Taylor series n={n}')
  plt.legend()
  plt.xlim(-4,4)
  plt.ylim(-2,2)
  ```

# 3. 예제

## 3.1. 예제: $y=e^x$

이 함수의 테일러 시리즈는 다음과 같다:

$$
e^x=\sum_{n=0}^{\infty}\frac{1}{n!}x^n
$$
- $n=4$까지 전개 하면:

  $$
  e^x=1+x+1/2x^2+1/6x^3+1/24x^4 ...
  $$

- 이 둘을 직접 그려보고 얼마나 유사한지 살펴보자

```python
def taylor_ex(x,n):
    s=0.
    for i in range(0,n+1):
      s=s+1./factorial(i)*(x**i)
    return s

xs=np.linspace(0,3)
plt.plot(xs,np.exp(xs),'k-',label=r'$y=e^x$',lw=3,alpha=0.3)
for n in range(1,6):
    plt.plot(xs,taylor_ex(xs,n), #continued
      '--',label=rf'Taylor series up to $n=${n}')

plt.ylim(0,20)
plt.legend()
```

## 3.2. 예제: $y=\cos(x)$

$y=\cos(x)$의 테일러 급수를 사용해서 $$n=1,4,7,10$$까지 경우를 나타내고
실제 $y=\cos(x)$ 함수와의 차이를 비교해보자.

## 3.3. 예제: $y=\ln(1+x)$

- $x$의 범위를 $x\in(-1,1]$로 한정하자.

# 4. 오차 측정 방법

## 4.1. 절대 오차 (absolute error)

$$
E^a=|x^{true}-x^{approx}|
$$

```python
x_true=3
x_approx=3.5
err_abs = abs(x_true - x_approx)
```

## 4.2. 상대 오차 (relative error)

$$
E^r=\frac{|x^{true}-x^{approx}|}{|x^{true}|}
$$

```python
x_true=3
x_approx=3.5
err_rel = abs(x_true - x_approx) / abs(x_true)
```

\*\* 상대 오차를 사용할 수 없는 경우는 언제일까?

## 4.3. 상대 오차2

$$
E^r_{\mathrm{sym}}
=\frac{|x^{true}-x^{approx}|}
{\frac{1}{2}(|x^{true}|+|x^{approx}|)}
$$

## 4.4. 수열의 오차?

만약 수열 $\boldsymbol{x}$가 여러 값으로 이루어진 배열이라면?

각 배열내의 요소의 절대 오차가 아래와 같이 정의되겠다.

$$
E_i=|x^{true}_i-x^{approx}_i|
$$

전체 수열의 오차를 구하면?

$$
\sum_iE_i=\sum_i|x^{true}_i-x^{approx}_i|
$$

혹은 아래와 같이 표현이 더욱 유용할 수 있겠다.

$$
Error=\sqrt{\sum_i(x^{true}_i-x^{approx}_i)^2}
$$
위와 같은 수열의 오차를 표현하자면 아래와 같다.

```python
import numpy as np # numpy 패키지 활용
x_true  =np.array([  1,   2,  4])
x_approx=np.array([1.3,-1.9,4.3] )

summedup=0.
for i in range(len(x_true)):
  summedup += (x_true[i] - x_approx[i])**2
error=np.sqrt(summedup)

## 혹은 Numpy의 broadcasting 기능과 .sum() method 활용해
## 더욱 축약해 아래와 같이 표현할 수 있겠다.
error=np.sqrt(((x_true-x_approx)**2).sum())
```

- 두 벡터 $\boldsymbol a, \boldsymbol b$ 가 서로 얼마나 유사한지 살펴보려면,
  아래와 같이 단순한 차로 살펴볼 수 있을까?

$$
\boldsymbol a -\boldsymbol b=?
$$

위의 결과는 scalar가 아닌 또 다른 벡터의 결과로 이어진다.

앞서 수열에 대한 오차를 표기했듯 아래 표현이 더
적절하겠다.

$$
Error=\sqrt{(a_1-b_1)^2+(a_2-b_2)^2+(a_3-b_3)^2}
$$

혹은 위의 수열에 대한 오차를 표기했듯

$$
Error=\sqrt{\sum_{i=1}^3(a_i-b_i)^2}
$$

라 표기할 수 있겠다. 그리고 이는 더욱 축약하자면

$$
Error=\|\boldsymbol a- \boldsymbol b\|_2
$$

와 같이 표기할 수 있겠다.

만약 상대 오차를 구한다면?

$$
Error=\frac{\|\boldsymbol a-\boldsymbol b\|_2}
{0.5(\|\boldsymbol a\|_2+\|\boldsymbol b\|_2)}
$$

혹은 더욱 명백하게 인덱스 notation을 활용해 표현하자면 아래와 같이 나타낼 수 있다.

$$
Error=\frac{\sqrt{(a_1-b_1)^2+(a_2-b_2)^2+(a_3-b_3)^2}}{0.5\big(\sqrt{a_1^2+a_2^2+a_3^2}+\sqrt{b_1^2+b_2^2+b_3^2}\big)}
$$

위에 제시된 오차의 정의를 파이썬으로 표현해보자.

```python
import numpy as np
def get_abs(v):
  """
  Function that calculates the magnitude of
  given vector `v`

  Arguments
  ---------
  v

  Returns
  -------
  the magnitude of given vector v
  """
  return np.sqrt(v[0]**2+v[1]**2+v[2]**2)

## two vectors
a=np.array([1. ,2. ,3. ])
b=np.array([1.2,1.9,3.1])

## absolute error between the two vectors
err=get_abs(a-b)
print('1 error:',err)
## Relative error between the two vectors
err = get_abs(a-b) / (0.5 * (get_abs(a) + get_abs(b)))
print('2 error:',err)
```



# 5. 예제: Maclaurin 급수를 이용한 화학퍼텐셜 근사

이상용액(ideal solution)에서 성분 $A$의 화학퍼텐셜은 다음과 같이 표현된다.

$$
\mu_A=\mu_A^\circ+RT\ln x_A
$$

여기서 $\mu_A^\circ$는 표준 화학퍼텐셜, $R$은 기체상수, $T$는 절대온도,
$x_A$는 성분 $A$의 몰분율이다. 기준 조성을 $x_0$라고 하고, 조성이
$x_0$에서 $x_A$로 변할 때의 화학퍼텐셜 변화를 구해보자.

$$
\Delta\mu_A
=\mu_A(x_A)-\mu_A(x_0)
=RT\ln\left(\frac{x_A}{x_0}\right)
$$

조성의 상대적인 변화를 $\delta$로 정의하면

$$
\delta=\frac{x_A-x_0}{x_0},
\qquad
x_A=x_0(1+\delta)
$$

이므로 다음과 같이 바꿔 쓸 수 있다.

$$
\Delta\mu_A=RT\ln(1+\delta)
$$

$|\delta|<1$이면 $\ln(1+\delta)$의 Maclaurin 급수는

$$
\ln(1+\delta)
=\delta-\frac{\delta^2}{2}+\frac{\delta^3}{3}
-\frac{\delta^4}{4}+\cdots
$$

이므로 화학퍼텐셜 변화를 다음과 같이 근사할 수 있다.

$$
\Delta\mu_A
\approx RT\left(
\delta-\frac{\delta^2}{2}+\frac{\delta^3}{3}
-\frac{\delta^4}{4}
\right)
$$

## 5.1. 계산 예제

$T=1000\ \mathrm{K}$인 이상용액에서 성분 $A$의 몰분율이
$x_0=0.50$에서 $x_A=0.55$로 증가했다고 하자. 기체상수는
$R=8.314\ \mathrm{J\,mol^{-1}K^{-1}}$을 사용한다.

먼저 조성의 상대적인 변화는

$$
\delta=\frac{0.55-0.50}{0.50}=0.10
$$

이다. 로그 함수를 직접 계산한 기준값은

$$
\Delta\mu_A
=RT\ln(1.1)
\approx 792.409\ \mathrm{J/mol}
$$

이다. Maclaurin 급수의 항을 차례로 추가하면 다음 결과를 얻는다.

| 사용한 급수 | $\Delta\mu_A$의 근삿값 (J/mol) | 절대 오차 (J/mol) |
|---|---:|---:|
| $RT\delta$ | 831.400 | 38.991 |
| $RT(\delta-\delta^2/2)$ | 789.830 | 2.579 |
| $RT(\delta-\delta^2/2+\delta^3/3)$ | 792.601 | 0.192 |
| $RT(\delta-\delta^2/2+\delta^3/3-\delta^4/4)$ | 792.393 | 0.015 |

$\delta=0.10$처럼 기준 조성에서의 변화가 작을 때는 적은 수의 항만 사용해도
화학퍼텐셜 변화를 비교적 정확하게 계산할 수 있다. 또한 항을 추가할수록
절단 오차가 감소하는 것을 확인할 수 있다.

다음 Python 코드를 이용하여 계산 결과를 확인해보자.

```python
import numpy as np
import matplotlib.pyplot as plt

R = 8.314       # J/(mol K)
T = 1000.0      # K
x0 = 0.50
xA = 0.55
delta = (xA-x0)/x0

exact = R*T*np.log1p(delta)

approx = 0.0
for n in range(1, 5):
    approx += (-1)**(n+1)*delta**n/n
    approx_mu = R*T*approx
    abs_error = abs(exact-approx_mu)
    print(n, approx_mu, abs_error)
```

조성 변화의 크기에 따른 근사의 정확도도 비교해보자.

```python
deltas = np.linspace(-0.8, 0.8, 300)
exact = R*T*np.log1p(deltas)

plt.plot(deltas, exact, "k-", linewidth=3, alpha=0.4,
         label="exact")

for N in [1, 2, 3, 4]:
    approx = np.zeros_like(deltas)
    for n in range(1, N+1):
        approx += (-1)**(n+1)*deltas**n/n
    plt.plot(deltas, R*T*approx, label=f"N={N}")

plt.xlabel(r"relative composition change, $\delta$")
plt.ylabel(r"$\Delta\mu_A$ (J/mol)")
plt.legend()
plt.grid()
plt.show()
```

- $\delta$가 0에 가까울수록 적은 항으로도 정확한 근삿값을 얻을 수 있다.
- $|\delta|$가 커지면 같은 정확도를 얻기 위해 더 많은 항이 필요하다.
- 이 급수의 수렴 범위는 $|\delta|<1$이다. 따라서 조성 변화가 이 범위를
  벗어나면 다른 기준 조성 $x_0$를 선택하거나 로그 함수를 직접 계산해야 한다.


# 6. 연습 문제

강의에서 배운 정의와 예제를 확인하는 문제이다. 계산 문제는 풀이 과정을 함께 작성한다.

## 6.1. 기본 개념

1. 다음 빈칸을 채워라.

   - 컴퓨터의 메모리는 유한하므로 수를 저장할 때 (　　　　) 오차가 생길 수 있다.
   - 무한한 계산 과정을 중간에 끊어 근삿값을 구할 때 (　　　　) 오차가 생긴다.
   - 참값과 근삿값의 차이의 크기를 (　　　　) 오차라고 한다.

2. 다음 수를 정수, 정수가 아닌 유리수, 무리수로 분류하라.

   $$
   -2,\quad \frac{1}{2},\quad 0.25,\quad \sqrt{2},\quad \pi
   $$

3. 다음 현상이 반올림 오차와 절단 오차 중 어디에 해당하는지 고르라.

   1. $\pi$를 $3.14$로 저장하였다.
   2. $\sin x$의 Taylor 급수에서 처음 두 항만 사용하였다.
   3. $1/3$을 $0.3333$으로 저장하였다.

## 6.2. 절대 오차와 상대 오차

4. 참값이 $10$, 근삿값이 $9.5$일 때 다음을 구하라.

   1. 절대 오차
   2. 상대 오차
   3. 백분율 상대 오차

5. 다음 표의 빈칸을 채워라.

   | 참값 | 근삿값 | 절대 오차 | 상대 오차 |
   |---:|---:|---:|---:|
   | 5 | 4.5 |  |  |
   | 20 | 21 |  |  |
   | -4 | -3.8 |  |  |

6. 참값이 $0$이고 근삿값이 $0.01$일 때 절대 오차를 구하라.
   이 경우 강의에서 정의한 상대 오차를 계산할 수 없는 이유를 설명하라.

## 6.3. Taylor 급수

7. 강의에서 배운 식을 사용하여 $x=0.5$에서 $\sin x$를 근사하라.

   $$
   \sin x\approx x
   $$

   NumPy의 `np.sin(0.5)`를 기준값으로 사용하여 절대 오차를 구하라.

8. 항을 하나 더 사용하여 같은 계산을 반복하라.

   $$
   \sin x\approx x-\frac{x^3}{3!}
   $$

   7번 결과와 비교하여 어느 근삿값의 절대 오차가 더 작은지 확인하라.

9. 다음 Python 코드를 완성하여 $3!$을 계산하라.

   ~~~python
   val = 1
   for i in range(1, ____):
       val = val * ____

   print(val)
   ~~~

10. 강의의 `sinx_taylor` 함수를 사용하여 다음 코드를 실행하라.

    ~~~python
    x = 0.5

    for n in range(4):
        approx = sinx_taylor(x, n)
        error = abs(np.sin(x) - approx)
        print(n, approx, error)
    ~~~

    `n`이 커질 때 근삿값과 절대 오차가 어떻게 변하는지 한 문장으로 설명하라.

## 6.4. Python 실습

11. 다음 코드를 실행하고 출력 결과를 기록하라.

    ~~~python
    a = 0.1 + 0.2

    print(a)
    print(a == 0.3)
    print(abs(a - 0.3))
    ~~~

    계산 결과가 예상과 다른 이유를 반올림 오차와 관련지어 설명하라.

12. 두 벡터가 다음과 같이 주어졌다.

    ~~~python
    import numpy as np

    a = np.array([1.0, 2.0, 3.0])
    b = np.array([1.1, 1.9, 3.2])
    ~~~

    1. `a - b`를 출력하라.
    2. 각 성분의 절대 오차를 `np.abs(a - b)`로 구하라.
    3. 두 벡터 사이의 오차를 다음 코드로 구하라.

       ~~~python
       error = np.sqrt(((a - b)**2).sum())
       print(error)
       ~~~

    4. 계산된 `error`가 두 벡터가 완전히 같을 때는 어떤 값을 갖는지 답하라.
