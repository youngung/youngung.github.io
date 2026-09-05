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
  - [3.1. 에제: $$y=e^x$$](#31-에제-yex)
  - [3.2. 에제: $y=\\cos(x)$](#32-에제-ycosx)
  - [3.3. 예제: $y=\\ln(1+x)$](#33-예제-yln1x)
  - [3.4. 예제: Maclaurin series expansion for chemical potential (?)](#34-예제-maclaurin-series-expansion-for-chemical-potential-)
- [4. 오차 측정 방법](#4-오차-측정-방법)
  - [4.1. 절대 오차 (absolute error)](#41-절대-오차-absolute-error)
  - [4.2. 상대 오차 (relative error)](#42-상대-오차-relative-error)
  - [4.3. 상대 오차2](#43-상대-오차2)
  - [4.4. 수열의 오차?](#44-수열의-오차)


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

## 3.1. 에제: $$y=e^x$$

이 함수의 테일러 시리즈는 다음과 같다:

$$
e^x=\sum_{n=0}^{\infty}\frac{1}{n!}x^n
$$
- $$n=4$$까지 전개 하면:

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

## 3.2. 에제: $y=\cos(x)$

$y=\cos(x)$의 테일러 급수를 사용해서 $$n=1,4,7,10$$까지 경우를 나타내고
실제 $y=\cos(x)$ 함수와의 차이를 비교해보자.

## 3.3. 예제: $y=\ln(1+x)$

- $x$의 범위를 $x\in(-1,1]$로 한정하자.

## 3.4. 예제: Maclaurin series expansion for chemical potential (?)

# 4. 오차 측정 방법

##  4.1. 절대 오차 (absolute error)

$$
E^a=|x^{true}-x^{approx}|
$$

```python
x_true=3
x_approx=3.5
err_rel= abs(x_true-x_approx)
```

## 4.2. 상대 오차 (relative error)

$$
E^r=\frac{|x^{true}-x^{approx}|}{|x^{true}|}
$$

```python
x_true=3
x_approx=3.5
err_rel= abs(x_true-x_approx)/abs(x_true)
```

\*\* 상대 오차를 사용할 수 없는 경우는 언제일까?

## 4.3. 상대 오차2

$$
E^r=\frac{x^{true}-x^{approx}}{\frac{1}{2}(x^{true}+x^{approx})}
$$

## 4.4. 수열의 오차?

만약 수열 $\boldsymbol{x}$가 여러 값으로 이루어진 배열이라면?

각 배열내의 요소의 절대 오차가 아래와 같이 정의되겠다.

$$
E_i=|x^{true}_i-x^{approx}_i|
$$

전체 수열의 오차를 구하면?

$$
\sum_iE_i=|x^{true}_i-x^{approx}_i|
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
summedup+=(x_true[i]-x_approx[i])**2
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
Error=\sqrt{\sum_i^3(a_i-b_i)^2}
$$

라 표기할 수 있겠다. 그리고 이는 더욱 축약하자면

$$
Error=|\boldsymbol a- \boldsymbol b|
$$

와 같이 표기할 수 있겠다.

만약 상대 오차를 구한다면?

$$
Error=\frac{|\boldsymbol a- \boldsymbol b|}{0.5(|\boldsymbol a|+|\boldsymbol b|)}
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
err=get_abs(a-b) #분자까지만,
err=err/0.5*(get_abs(a)+get_abs(b)) # 분모로 나누면..
print('2 error:',err)
```