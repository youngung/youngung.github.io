---
layout: page
title: 수치해석
description: 재료공학도를 위한 수치해석
target: 2학년 1학기
permalink:
prerequisite: 재료공학개론1, 데이터 재료과학
toc:
  0.1. sidebar: left
---

- [1. 뉴턴 랩슨 법 활용하는 방법](#1-뉴턴-랩슨-법-활용하는-방법)
- [2. 테일러 급수로 부터 Newton-Raphson 방법을 도출할 수 있다.](#2-테일러-급수로-부터-newton-raphson-방법을-도출할-수-있다)
  - [2.1. 1st order Newton-Raphson 식](#21-1st-order-newton-raphson-식)
  - [2.2. 2nd order Newton-Raphson 식](#22-2nd-order-newton-raphson-식)
- [3. 예제](#3-예제)
  - [3.1. 방정식 $$x^2+x=10$$을 풀어보자.](#31-방정식-x2x10을-풀어보자)
  - [3.2. 앞선 예제에서 초기값을 바꿔보고 그 영향을 살펴보자.](#32-앞선-예제에서-초기값을-바꿔보고-그-영향을-살펴보자)
  - [3.3. **고급 예제**: 앞선 예제를 아래와 같이 2nd order Taylor expansion을 활용해 작성해보자.](#33-고급-예제-앞선-예제를-아래와-같이-2nd-order-taylor-expansion을-활용해-작성해보자)
- [**고급 예제**: 임의의 2차 함수의 해를 찾는 script를 작성해보자.](#고급-예제-임의의-2차-함수의-해를-찾는-script를-작성해보자)
- [**고급 예제**: CLI 환경에서 $a,b,c$ 를 줬을 때, $ax^2+bx+c=0$의 해를 찾는 모듈을 만들어보자.](#고급-예제-cli-환경에서-abc-를-줬을-때-ax2bxc0의-해를-찾는-모듈을-만들어보자)


# 1. 뉴턴 랩슨 법 활용하는 방법

- 아래 형태의 함수의 답, 즉 $f=0$을 만족하는 $x$값을 구하고 싶을 때 사용할 수 있다.

$$f(x)=0$$

- 따라서, 문제의 방정식을 위와 같은 형태로 바꿔 표현할 수 있다면, Newton-Raphson 방법을 활용해 해를 구할 수 있다.

- 예: $x^2=2$ 의 해를 구하기 위해서는

$$f(x)=x^2-2=0$$

위의 해를 구하면 되겠다.

- Bisection method는 항상 해를 구할 수 있지만, Newton Raphson은 가끔 해를 못구할 때도 (해를 구하는데 실패할 수) 있다.

- 하지만 Bisection method에 비해 훨씬 빠르게 해를 찾을 수 있다.

- '접선'을 활용해 해를 빠르게 찾아간다.

- 미지수가 둘 이상은 경우에도 활용가능하다 (Advanced). 따라서, 벡터 함수에도 적용가능하다.

- $f(x,y)=0$ 혹은 $\boldsymbol f(\boldsymbol v)=0$ 에도 활용 가능.

# 2. 테일러 급수로 부터 Newton-Raphson 방법을 도출할 수 있다.

- [테일러 급수(Taylor series)](https://ko.wikipedia.org/wiki/테일러_급수)로부터
 [Newton Raphson](https://ko.wikipedia.org/wiki/뉴턴_방법) 방법 도출

- 함수 $f(x)$ 의 테일러 급수에 의하면

$f(x)=\sum_{n=0}$

$$
f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n
=f(a)+f^\prime(a)(x-a)+\frac{1}{2}f^{\prime\prime}(a)(x-a)^2+\frac{1}{6}f^{\prime\prime\prime}(a)(x-a)^3 + ...
$$

- Example of $f(x)=x^2$ 의 경우?

$$
f(x)=x^2
$$

$$
f^\prime(x)=2x
$$

$$
f^{\prime\prime}(x)=2
$$

$$
f^{\prime\prime\prime}(x)=0.
$$

- 따라서, 이어서 나오는 고차 항의 도함수는 0이 되며 기여하는 바가 없게 된다.
다시 테일러 급수의 정의를 따라,

- $a=0$ 일 때의 경우(Maclaurin series)를 살펴보면

$$
f(x)=f(0)+f^\prime(0)x+\frac{1}{2}f^{\prime\prime}(0)x^2
\newline
=0+0\times x+1/2\times 2\times x^2=x^2
$$

- $a=1$일 때의 경우에는?

$$
f(x)=f(1)+f^\prime(1)(x-1)+\frac{1}{2}f^{\prime\prime}(1)(x-1)^2
\newline
=1+2(x-1)+(x-1)^2
\newline
=1+2x-2+x^2-2x+1=x^2
$$

- Newton-Raphson 식 도출 (1st order)

$$
f(x)=0
$$

을 풀이하는 문제가 있다 가정하자. 이때 이를 위 의 $$a$$값을 $$x_n$$라 놓고 풀면

$$
f(x)=f(x_n)+f^\prime(x_n)(x-x_n)+\frac{1}{2}f^{\prime\prime}(x_n)(x-x_n)^2+ ...
$$

## 2.1. 1st order Newton-Raphson 식
여기서 $n=1$까지 항만 고려한다면..

$$
f(x)\approx f(x_n)+f^\prime(x_n)(x-x_n)
$$

우리가 풀이하고자 하는 조건에 의하면 $f(x)=0$ 이므로

$$
0\approx f(x_n)+f^\prime(x_n)(x-x_n)
$$

따라서 $x$에 대해 풀이하면

$$
-\frac{f(x_n)}{f^\prime(x_n)}\approx x-x_n
$$

아래가 도출된다.

$$
\rightarrow x\approx x_n-\frac{f(x_n)}{f^\prime(x_n)}
$$

이 때 근사된 $$x$$을 다음번 추측값 $$x_{n+1}$$이라 하면 Newton-Raphson에 활용되는 반복식이 얻어진다.


## 2.2. 2nd order Newton-Raphson 식

- Taylor 공식에서 2차 오더까지 사용하면 어떠한 Newton-Raphson식이 도출되나?
- 도출

$$
f(x)\approx f(x_n)+f^\prime(x_n)(x-x_n)+\frac{1}{2}f^{\prime\prime}(x_n)(x-x_n)^2
$$

급수의 중심을 바꾸기 위해 $h$값을 아래와 같이 도입하자

$$
h=x-x_n
$$

그러면 2차항까지의 테일러 급수가 아래와 같이 표현된다.

$$
f(x_n+h)\approx f(x_n)+f^\prime(x_n)h+\frac{1}{2}f^{\prime\prime}(x_n)h^2
$$

그 다음 좌항이 0이 되면

$$
0\approx f(x_n)+f^\prime(x_n)h+\frac{1}{2}f^{\prime\prime}(x_n)h^2
$$

$h$에 대한 2차 방정식이므로, 근의 공식을 사용하면

$$
h=\frac{-f^\prime(x_n)\pm\sqrt{[f^\prime(x_n)]^2-2f(x_n)f^{\prime\prime}(x_n)}}{f^{\prime\prime}(x_n)}
$$

위 계산으로 구해진 $h$를 활용해서

$$
x_{n+1}=x_{n}+h
$$

- 주의: 근의 공식에 따른 두 $h$값 중에 무엇을 선택해야 하나? 대부분의 경우 두 값을 비교하여 더욱 작은 $h$값을 활용한다.

# 3. 예제

## 3.1. 방정식 $$x^2+x=10$$을 풀어보자.

- 우선 $$f(x)=0$$ 형태로 바꿔 표현하면,

$$
f(x)=x^2+x-10=0
$$

혹은

$$
f(x)=-x^2-x+10=0
$$

이 된다. 사실 어느 쪽을 고르나 동일한 알고리듬이 적용 가능하다. 전자의 경우를 선택하고
파이썬으로 함수 $f(x)$를 표현해보자.

```python
def func(x):
    return x**2+x-10
```

풀이에 의하면 함수의 도함수 $f^\prime(x)$도 필요하다. 따라서,

$$
f^\prime(x)=\frac{\partial f(x)}{\partial x}=2x+1
$$

파이썬으로 표현하자면

```python
def fprime(x):
    return 2*x+1
```

이를 활용해 아래 알고리듬에 대입하면

$$
x_{n+1}\leftarrow x_n-\frac{f(x_n)}{f^\prime(x_n)}
$$

```python
x=1 # initial guess
x=x-func(x)/fprime(x)
```

여기에 tolerance를 추가한다면

```python
x=1 # initial guess
tol=1e-10
err=abs(func(x))
while err>tol:
    x=x-func(x)/fprime(x)
    err=abs(func(x))
```

## 3.2. 앞선 예제에서 초기값을 바꿔보고 그 영향을 살펴보자.

## 3.3. **고급 예제**: 앞선 예제를 아래와 같이 2nd order Taylor expansion을 활용해 작성해보자.

$$
h=\frac{-f^\prime(x_n)\pm\sqrt{[f^\prime(x_n)]^2-2f(x_n)f^{\prime\prime}(x_n)}}{f^{\prime\prime}(x_n)}
$$

위 계산으로 구해진 $h$를 활용해서

$$
x_{n+1}=x_{n}+h
$$

- 아래는 Halley's method으로 알려진 방법이다.

$$
x_{n+1}=x_n-\frac{2f(x_n)f^\prime(x_n)}{2[f^\prime(x_n)]^2-f(x_n)f^{\prime\prime}(x_n)}
$$

이를 활용해

$$
f(x)=\cos(x)e^{3x}-3=0
$$

을 만족하는 $x$값을 구하시오.

- 1st and 2nd order Newton-Raphson과 Halley's method 비교 예제

```python
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.cos(x)*np.exp(3*x)-3
def fp(x):
    return np.cos(x)*np.exp(3*x)*3-np.sin(x)*np.exp(3*x)
def fpp(x):
    return -np.sin(x)*np.exp(3*x)*3+np.cos(x)*np.exp(3*x)*9
def h(x): # 2nd order NR
    F=f(x)
    p=fp(x)
    pp=fpp(x)

    det=p**2-2*F*pp
    det=np.sqrt(det)
    h1=-p+det
    h1=h1/pp

    h2=-p-det
    h2=h2/pp
    if abs(h1)<abs(h2): return h1
    else: return h2

def Halley(x): ## Halley's term
    F=f(x)
    p=fp(x)
    pp=fpp(x)
    return 2*F*p/(2*p**2-F*pp)

xs=np.linspace(-2.5,1)
ys=f(xs)

fig=plt.figure(figsize=(7,3))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
ax1.plot(xs,ys)

xinit=-0.1
tol=1e-10
## Newton Raphson
x=xinit
err=tol*2
i=0
while err>tol:
ax1.plot(x,f(x),'ko',mfc='None')
ax2.plot(i,f(x),'ko')
x+=-f(x)/fp(x)
err=abs(f(x))
i+=1

## 2nd order
x=xinit
err=tol*2
i=0
while err>tol:
ax1.plot(x,f(x),'r+')
ax2.plot(i,f(x),'r+')
x+=+h(x) # here it is + sign.
err=abs(f(x))
i+=1

## Halley's method
## 2nd order
x=xinit
err=tol*2
i=0
while err>tol:
print(i,x)
ax1.plot(x,f(x),'bx')
ax2.plot(i,f(x),'bx')
x-=Halley(x) # note the minus sign here!
err=abs(f(x))
i+=1
```





# **고급 예제**: 임의의 2차 함수의 해를 찾는 script를 작성해보자.
- 해석적 해와 수치적해를 비교해보자.
- 수치적 해를 구하는 방법은 위에서 배운 Newton-Raphson 방법을 활용하면 된다.

# **고급 예제**: CLI 환경에서 $a,b,c$ 를 줬을 때, $ax^2+bx+c=0$의 해를 찾는 모듈을 만들어보자.

- CLI 환경에서 입력값을 주는 방법은 다양하다. 그 중에서 argpase를 활용하는 방법을 추천한다.
