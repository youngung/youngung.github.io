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

# 1. 목표
  - 방정식을 해석적(analytic)으로 그리고 수치적(numerical)으로 푸는 방법 비교
  - Bisection method 이해하고, 활용할 수 있다.

# 2. 해석적 풀이와 수치적 풀이

- (방정식을 왜 수치적으로 풀어야 하나), 해석적 풀이 vs. 수치적 풀이, 2차 방정식 손계산

- 해석적 풀이가 가능한 경우

  - 1차, 2차 방정식: 근의 공식 존재

  - 1차 방정식
   $$ a x + b =0$$

  - 위 1차 방정식의 근의 방정식:

   $$x=-\frac{b}{a}$$

  - 2차 방정식:
    $$a x^{2} + b x + c = 0 $$
  - 위 2차 방정식의 근의 방정식:

    $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

- 해석적 풀이가 불가능하거나 매우 복잡한 경우

  - [5차이상의 다항식의 경우, 근의 공식 없음](https://ko.wikipedia.org/wiki/오차_방정식)
    (사칙연산이나, 거듭 제곱근 등, 손으로 계산 못한다.)
    하지만 실근은 존재한다.

  ```python
  import matplotlib.pyplot as plt
  import numpy as np

  def poly(x,*args):
  	"""
  	polynomial function
  	"""
  	n=len(args)-1
  	y=0.
  	print('n,i,arg')
  	for i, arg in enumerate(args):
  		print(n,i,arg)
  		y+=arg*(x**n)
  		n-=1
  	return y

  xs=np.linspace(-1.3,1,100)
  ys=poly(xs,-5,-2,5,3,2,1)
  plt.plot(xs,ys,'-')
  ```

# 3. $x=\cos(x)$ 만족하는 $x$값 구하기.

- 이 경우 근은 분명 존재한다.

```python
import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return np.cos(x)-x

xs=np.linspace(-10,10)
plt.plot(xs,func(xs),label=r'$y=\cos(x)$')
plt.axhline(c='k')
plt.legend()
```

# 4. 이분법(bisection method)
- 원리:
* $f(x)=0$가 연속일 때, 두 점 $a,b$에서
  함수값의 부호가 다르면, 그 사이에 반드시 해가 있다. (중간값 정리)
* 즉, [a, b] 구간에서 근이 있음을 알면 구간을 절반으로 줄여가며 해를 찾는 방법

<!-- 		   ![bisection_image_wikipedia](https://upload.wikimedia.org/wikipedia/commons/c/c2/Bisection_method.png)
 -->

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c2/Bisection_method.png" alt="drawing" width="400"/>

- 알고리듬:

* 시작 구간 $[a,b]$ 선택:

$$f(a)×f(b)<0$$

위가 반드시 만족되어야 함 (근이 반드시 존재)

- 위와 같은 조건 만족하는 $$a,b$$ 값의 중간 값 $$c$$ 구하기.

$$c=\frac{a+b}{2}$$

- f(c)의 부호 확인

+ case 1.

$$f(a)\times f(c)<0$$

근이 $$[a,c]$$ 안에 존재

+ case 2.

$$f(c)\times f(b)<0$$

근이 $[c,b]$ 안에 존재

- 새로운 구간을 $[a,c]$ 또는 $[c,b]$로 좁힘

- 원하는 허용 구간 내 오차가 나올 때 까지 반복.

$$E^a \leq Tol. $$

# 5. 예제

방정식 $x^2=2$를 풀어보자.

- 구간선택:

$$[a,b]=[1,2]$$

- 조건 탐색

    $$f(1)=-1,f(2)=2$$

    부호가 다르므로, 선택된 구간 $[1,2]$ 안에 해 존재.

- 중점 설정

    $$c=\frac{a+b}{2}=1.5$$

- 조건 탐색

    $$f(1.5)=0.25>0$$

- 구간 조정

    따라서 근은 $[1,1.5]$ 범위 내 존재

- 다시 중점 설정

    $$c=\frac{a+b}{2}=1.25$$

    - 조건 탐색

    $$f(1.25)=-0.4375<0$$

    - 구간 조정

    따라서 근은 $[1.25,1.5]$사이에 존재

- 중점 빛 범위의 구간 설정을 반복하여 수정하며 오차 좁힘.

```python
def f(x): ## f(x)=x^2-2 함수
    return x**2 - 2
a=1
b=2
tol=1e-10
error=tol*2
if f(a) * f(b) > 0:
    print("root not in [a, b]")
k=0
while error>tol: #(b - a) / 2 > tol:
    c = (a + b) / 2 # center
    if f(a) * f(c) < 0: # opposite sign
        b = c # update b
    else:
        a = c # or update a
    error=(b-a)/2.
    k=k+1
print('total iteration:',k)
```

- 내 컴퓨터에서는 33번 반복해야 $10^{-10}$ 허용오차 범위내의 근을 구할 수 있었다.

- 아래 예시를 통해 upper limit (파란색), lower limit (빨간색)이 반복 횟수에 따라 변하는 과정을 살펴보자.

```python
def f(x): ## f(x)=x^2-2 함수
    return x**2 - 2
a=1
b=2
tol=1e-2
error=tol*2
if f(a) * f(b) > 0:
    print("root not in [a, b]")
k=0
while error>tol: #(b - a) / 2 > tol:
    plt.plot(k,a,'ro')
    plt.plot(k,b,'bo')
    c = (a + b) / 2 # center
    plt.plot(k,c,'g+')
    if f(a) * f(c) < 0: # opposite sign
        b = c # update b
    else:
        a = c # or update a
    error=(b-a)/2.
    k=k+1

print('total iteration:',k,'root:',c)
print('a,b:',a,b)
plt.plot(np.nan,'ro',label='a')
plt.plot(np.nan,'bo',label='b')
plt.plot(np.nan,'g+',label='center')
plt.xlabel('iteration')
plt.ylabel('Range')
plt.legend()
```