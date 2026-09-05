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

- [1. Newton-Raphson](#1-newton-raphson)
- [2. 예제](#2-예제)
- [3. 초기값의 영향](#3-초기값의-영향)
- [4. 예제](#4-예제)
  - [4.1. 방정식 $x^2=3$를 풀어보자.](#41-방정식-x23를-풀어보자)
  - [4.2. 방정식 $x^{4}=2$를 풀어보자.](#42-방정식-x42를-풀어보자)
  - [4.3. 방정식 $\\ln{x}=1$를 풀어보자.](#43-방정식-lnx1를-풀어보자)
  - [4.4. 예제](#44-예제)

# 1. Newton-Raphson

- [Bisection method](<https://ko.wikipedia.org/wiki/이분법_(수학)>)

  원리가 쉽고 그리고 근을 찾긴 하지만, 때로는 너무 많은 반복 계산을
  필요로 한다. 더욱 빠르고 효율적인 방법이 없을까?

- 아래 그림의 알고리듬을 반복.

  ![imag](/assets/dat_files/lectures/2_1_numerical_analysis/nr.gif)

# 2. 예제

 - 방정식 $x^2=2$를 풀어보자.

 - 해석적 해:

$$x=\pm\sqrt{2}$$

 - 수치적 해?

 - 알고리듬 (점화식)이 다음과 같다.

$$
x_{n+1}=x_n-\frac{x_n^2-2}{2x_n}
$$

오차가 항상 있으므로, 허용가능한 오차(tolerance)를 설정해야 하겠다. 절대 오차를
아래와 같이 정의하고, 허용가능한 오차를 $10^{-10}$으로 설정하자.

$$
E^a = |x_{n+1}^2-2|\leq 10^{-10}
$$

이 알고리듬은 처음 추측값($x_0$)이 필요하다.
이를 $x_0=+1$로 설정하고 알고리듬을 적용해보자.

- At $(n=0)$

$$x_0=+1$$

- At $(n=1)$

$$x_1=x_0-\frac{x_0^2-2}{2x_0}=1-\frac{1^2-2}{2}=1+0.5=1.5$$

$$E^a=|1.5^2-2|=0.25 \ge10^{-10} \therefore \text{not accurate enough}$$

- At $(n=2)$

$$x_2=x_1-\frac{x_1^2-2}{2x_1}=1.5-\frac{1.5^2-2}{3}=1.4166666...$$

$$E^a=|1.4166...^2-2|=0.006944...\times 10^{-6}\ge10^{-10} \therefore \text{not accurate enough}$$

- At $(n=3)$

$$x_3=x_2-\frac{x_2^2-2}{2x_2}=1.41421568 ... $$

$$E^a=6.007..\times10^{-6}\ge10^{-10} \therefore \text{not accurate enough}$$

- At $(n=4)$

$$x_4=x_3-\frac{x_3^2-2}{2x_3}=1.41421356237... $$

$$E^a=4.51\times10^{-12}\red{\lt}10^{-10} \therefore \text{accurate enough!}$$

```python
fig=plt.figure()
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)

x=1 ## initial guess
ax1.plot(0,x,'o',label='initial guess')
tol=1e-10
err=tol*2
k=0
while(err>tol and k< 10): ## k counts the number of iteration.
    x=x-(x**2-2)/(2*x)
    err=abs(x**2-2)
    print(k+1,x,err)
    print(err<=tol)
    k=k+1
    ## see the trend.
    ax1.plot(k,x,'+',label=r'$x_%i$'%k)
    ax2.plot(k,err,'o')

#ax2.set_yscale('log')
ax1.legend()
```

# 3. 초기값의 영향
- 위 예시에서 초기값을 $x_0=-1$ 로 세팅하고 시작해보자.
- $y=x^2-2$ 그래프를 실제로 그리고, 반복할 때 마다 어떻게 값이 변하고 있는지 살펴보자.

# 4. 예제

## 4.1. 방정식 $x^2=3$를 풀어보자.

- 주어진 알고리듬은 아래와 같다.

$x_{n+1}=x_{n} - \frac{x_n^{2}-3}{2x_{n}}$

## 4.2. 방정식 $x^{4}=2$를 풀어보자.

- 주어진 알고리듬은 아래와 같다.

$$
x_{n+1}=x_n-\frac{x_n^4-2}{4x_n^3}
$$

## 4.3. 방정식 $\ln{x}=1$를 풀어보자.

- 주어진 알고리듬은 아래와 같다.

$$
x_{n+1}=x_n-\frac{\ln(x_n)-1}{1/x_n}
$$

## 4.4. 예제

방정식 $\cos{x}=0.3$를 풀어보자.

- 주어진 알고리듬은 아래와 같다.

$$
x_{n+1}=x_n-\frac{\cos(x_n)-0.3}{-\sin(x_n)}
$$

- 물음: 위 예제에서 보이는 특정 규칙을 찾아보자.

- 물음: 초기값을 바꿔보고 그 영향을 살펴보자.
