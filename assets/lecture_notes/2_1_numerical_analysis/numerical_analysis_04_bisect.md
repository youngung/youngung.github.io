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

- [1. 학습 목표](#1-학습-목표)
- [2. 해석적 풀이와 수치적 풀이](#2-해석적-풀이와-수치적-풀이)
- [3. $x=\\cos x$를 만족하는 근](#3-xcos-x를-만족하는-근)
- [4. 이분법](#4-이분법)
  - [4.1. 원리와 적용 조건](#41-원리와-적용-조건)
  - [4.2. 알고리듬](#42-알고리듬)
  - [4.3. 오차와 반복 횟수](#43-오차와-반복-횟수)
- [5. 예제: $x^2=2$](#5-예제-x22)
- [6. 연습 문제](#6-연습-문제)

# 1. 학습 목표

- 방정식의 해석적 풀이와 수치적 풀이의 차이를 설명할 수 있다.
- 방정식을 $f(x)=0$ 형태로 바꿀 수 있다.
- 중간값 정리를 이용하여 근이 포함된 구간을 찾을 수 있다.
- 이분법의 반복 과정을 손으로 계산하고 Python으로 구현할 수 있다.
- 구간의 폭으로 근의 위치 오차를 판단할 수 있다.

# 2. 해석적 풀이와 수치적 풀이

해석적 풀이(analytic solution)는 식을 변형하여 해를 정확한 수식으로 나타내는
방법이다. 수치적 풀이(numerical solution)는 계산을 반복하여 해에 가까운 근삿값을
구하는 방법이다.

- 해석적 풀이가 가능한 경우

  - 1차, 2차 방정식: 근의 공식 존재

  - 1차 방정식
   $$ a x + b =0$$

  - 위 일차방정식의 해:

   $$x=-\frac{b}{a}$$

  - 2차 방정식:
    $$a x^{2} + b x + c = 0 $$
  - 위 이차방정식의 해:

    $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

- 해석적 풀이가 불가능하거나 매우 복잡한 경우

  - 일반적인 5차 이상의 다항방정식에는 사칙연산과 거듭제곱근만으로 모든 근을
    표현하는 공식이 없다. 또한 삼각함수나 지수함수가 포함된 방정식은 해석적
    풀이가 어렵거나 불가능한 경우가 많다.

  ```python
  import matplotlib.pyplot as plt
  import numpy as np

  def poly(x, *coefficients):
      """계수가 높은 차수부터 주어진 다항식의 값을 계산한다."""
      y = np.zeros_like(x, dtype=float)
      for coefficient in coefficients:
          y = y*x+coefficient
      return y

  xs = np.linspace(-1.3, 1.0, 300)
  ys = poly(xs, -5, -2, 5, 3, 2, 1)
  plt.plot(xs, ys, label="polynomial")
  plt.axhline(0.0, color="black", linewidth=1)
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.grid()
  plt.legend()
  plt.show()
  ```

# 3. $x=\cos x$를 만족하는 근

- 이 경우 근은 분명 존재한다.

```python
import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return np.cos(x)-x

xs=np.linspace(-1,2,300)
plt.plot(xs,func(xs),label=r'$f(x)=\cos(x)-x$')
plt.axhline(0.0,color='k',linewidth=1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
```

$f(0)=1>0$이고 $f(1)=\cos(1)-1<0$이므로, 연속함수의 중간값 정리에 따라
$0$과 $1$ 사이에 적어도 하나의 근이 있다.

# 4. 이분법

## 4.1. 원리와 적용 조건

함수 $f(x)$가 닫힌 구간 $[a,b]$에서 연속이고

$$
f(a)f(b)<0
$$

이면 중간값 정리에 따라 열린 구간 $(a,b)$ 안에 적어도 하나의 근이 있다.
이분법은 근을 포함하는 구간을 반복해서 절반으로 줄이는 방법이다.

- $f(a)=0$ 또는 $f(b)=0$이면 끝점 자체가 근이다.
- 부호 변화는 근의 존재를 보장하지만 근이 하나뿐이라는 것은 보장하지 않는다.
- $f(x)=x^2$처럼 그래프가 $x$축에 닿고 되돌아가는 경우에는 근이 있어도 양
  끝점에서 부호가 바뀌지 않을 수 있다.
- 함수가 구간에서 연속인지 먼저 확인해야 한다.

<!-- 		   ![bisection_image_wikipedia](https://upload.wikimedia.org/wikipedia/commons/c/c2/Bisection_method.png)
 -->

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c2/Bisection_method.png" alt="drawing" width="400"/>

## 4.2. 알고리듬

1. 연속인 함수 $f(x)$와 시작 구간 $[a,b]$를 정한다.
2. $f(a)=0$ 또는 $f(b)=0$인지 확인한다.
3. $f(a)f(b)<0$인지 확인한다.
4. 구간의 중점 $c$를 계산한다.

   $$
   c=\frac{a+b}{2}
   $$

5. $f(c)=0$이면 $c$가 근이므로 계산을 종료한다.
6. $f(a)f(c)<0$이면 새 구간을 $[a,c]$로 정한다.
7. 그렇지 않으면 새 구간을 $[c,b]$로 정한다.
8. 구간이 충분히 작아질 때까지 4--7단계를 반복한다.

한 번 반복할 때마다 근을 포함하는 구간의 길이는 절반으로 줄어든다.

## 4.3. 오차와 반복 횟수

현재 구간의 중점 $c=(a+b)/2$를 근의 근삿값으로 사용하면 참근 $x^*$와의
위치 오차는 다음 범위를 넘지 않는다.

$$
|x^*-c|\leq\frac{b-a}{2}
$$

따라서 다음 조건을 종료 기준으로 사용할 수 있다.

$$
\frac{b-a}{2}\leq\mathrm{tol}
$$

초기 구간의 길이가 $b_0-a_0$이고 구간을 $n$번 절반으로 줄이면

$$
b_n-a_n=\frac{b_0-a_0}{2^n}
$$

이다. 따라서 필요한 반복 횟수를 다음과 같이 추정할 수 있다.

$$
n\geq
\left\lceil
\log_2\left(\frac{b_0-a_0}{2\,\mathrm{tol}}\right)
\right\rceil
$$

# 5. 예제: $x^2=2$

방정식 $x^2=2$를 풀어보자.

- 근 찾기 함수:

  $$
  f(x)=x^2-2
  $$

- 초기 구간:

$$[a,b]=[1,2]$$

- 부호 확인

    $$f(1)=-1,f(2)=2$$

    함수값의 부호가 다르므로(즉 $f(1)f(2)<0$), 구간 $[1,2]$ 안에 적어도 하나의 근이 존재한다.

- 첫 번째 중점

    $$c=\frac{a+b}{2}=1.5$$

  $$
  f(1.5)=0.25>0
  $$

  $f(1)<0$이고 $f(1.5)>0$이므로 새 구간은 $[1,1.5]$이다.

- 두 번째 중점

    $$c=\frac{a+b}{2}=1.25$$

  $$
  f(1.25)=-0.4375<0
  $$

  $f(1.25)<0$이고 $f(1.5)>0$이므로 새 구간은 $[1.25,1.5]$이다.

같은 과정을 반복하면 근을 포함하는 구간이 계속 줄어든다.

```python
def f(x):
    return x**2 - 2

def bisection(f, a, b, tol=1e-10, max_iter=100):
    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a, 0, []
    if fb == 0:
        return b, 0, []
    if fa*fb > 0:
        raise ValueError("f(a)와 f(b)의 부호가 서로 달라야 합니다.")

    history = []
    iteration = 0

    while (b-a)/2 > tol and iteration < max_iter:
        c = (a+b)/2
        fc = f(c)
        history.append((a, b, c))

        if fc == 0:
            return c, iteration+1, history

        if fa*fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        iteration += 1

    if (b-a)/2 > tol:
        raise RuntimeError("최대 반복 횟수 안에 수렴하지 않았습니다.")

    root = (a+b)/2
    return root, iteration, history

root, iterations, history = bisection(f, 1.0, 2.0)

print("root:", root)
print("f(root):", f(root))
print("iterations:", iterations)
```

초기 구간 $[1,2]$와 허용오차 $10^{-10}$을 사용하면 구간을 33번 줄인 뒤
위치 오차의 상한이 허용오차보다 작아진다.

아래 코드로 하한, 상한과 중점이 변하는 과정을 살펴보자.

```python
a_values = [item[0] for item in history]
b_values = [item[1] for item in history]
c_values = [item[2] for item in history]
k = np.arange(1, len(history)+1)

plt.plot(k, a_values, "ro-", label="lower bound a")
plt.plot(k, b_values, "bo-", label="upper bound b")
plt.plot(k, c_values, "g+-", label="midpoint c")
plt.xlabel("iteration")
plt.ylabel("x")
plt.grid()
plt.legend()
plt.show()
```

$x=\cos x$의 해도 같은 함수로 계산할 수 있다.

```python
def f_cos(x):
    return np.cos(x)-x

root, iterations, history = bisection(f_cos, 0.0, 1.0)

print("root:", root)
print("f(root):", f_cos(root))
print("iterations:", iterations)
```

계산 결과는 약 $x=0.7390851332$이다.

# 6. 연습 문제

강의에서 배운 개념과 예제를 확인하는 기초 문제이다. 계산 문제는 풀이 과정도
함께 작성하라.

1. 다음 빈칸을 채워라.

   - 이분법을 사용하려면 함수가 구간 $[a,b]$에서 (　　　　)이어야 한다.
   - $f(a)$와 $f(b)$의 부호는 서로 (　　　　)야 한다.
   - 한 번 반복하면 구간의 길이는 이전 길이의 (　　　　)가 된다.

   <!--
   풀이 및 정답:
   함수는 연속이어야 하고 양 끝점의 함수값 부호는 서로 달라야 한다.
   한 번 반복하면 구간의 길이는 이전 길이의 1/2이 된다.
   -->

2. 다음 설명이 맞으면 O, 틀리면 X로 표시하라.

   1. 이분법은 근의 근삿값을 구하는 수치적 방법이다. (　　)
   2. f(a)f(b)<0이면 연속인 함수는 a와 b 사이에 적어도 하나의 근을 갖는다. (　　)
   3. 이분법을 한 번 적용하면 구간의 길이가 두 배가 된다. (　　)
   4. f(a)=0이면 a는 근이다. (　　)

   <!--
   풀이 및 정답: 1번 O, 2번 O, 3번 X, 4번 O.
   이분법을 한 번 적용하면 근을 포함하는 구간의 길이는 절반이 된다.
   -->

3. 방정식 $x^2=3$을 $f(x)=0$ 형태로 바꾸고 다음 값을 계산하라.

   $$
   f(1),\qquad f(2)
   $$

   초기 구간 $[1,2]$에 이분법을 적용할 수 있는지도 판단하라.

   <!--
   풀이 및 정답:
   f(x)=x^2-3으로 놓는다. f(1)=-2이고 f(2)=1이므로 두 함수값의 부호가
   다르다. 함수가 연속이므로 [1,2]에 이분법을 적용할 수 있다.
   -->

4. $f(x)=x^2-2$와 초기 구간 $[1,2]$에 이분법을 두 번 적용하라.
   각 반복의 중점과 새 구간을 구하라.

   <!--
   풀이 및 정답:
   첫 번째 중점은 c=(1+2)/2=1.5이다. f(1.5)=0.25이므로 새 구간은
   [1,1.5]이다. 두 번째 중점은 c=(1+1.5)/2=1.25이다.
   f(1.25)=-0.4375이므로 새 구간은 [1.25,1.5]이다.
   -->

5. 근을 포함하는 현재 구간이 $[1.25,1.50]$일 때 다음을 구하라.

   1. 구간의 중점
   2. 구간의 길이
   3. 중점을 근삿값으로 사용할 때 위치 오차의 상한

   <!--
   풀이 및 정답:
   중점은 (1.25+1.50)/2=1.375이고 구간의 길이는 1.50-1.25=0.25이다.
   위치 오차의 상한은 구간 길이의 절반인 0.125이다.
   -->

6. 다음 함수와 구간 중 이분법의 부호 조건을 만족하는 것을 모두 고르라.

   1. $f(x)=x-2$, 구간 $[0,3]$
   2. $f(x)=x^2+1$, 구간 $[-1,1]$
   3. $f(x)=x^2-4$, 구간 $[0,3]$

   <!--
   풀이 및 정답:
   1번은 f(0)=-2, f(3)=1이므로 조건을 만족한다.
   2번은 f(-1)=2, f(1)=2이므로 조건을 만족하지 않는다.
   3번은 f(0)=-4, f(3)=5이므로 조건을 만족한다.
   따라서 정답은 1번과 3번이다.
   -->

7. 강의의 `bisection` 함수를 사용하여 $x^2-3=0$의 양의 근을 구하라.

   ```python
   def f(x):
       return x**2-3

   root, iterations, history = bisection(f, 1.0, 2.0, tol=1e-6)
   print(root)
   print(iterations)
   ```

   계산된 근을 `np.sqrt(3)`과 비교하라.

   <!--
   풀이 및 정답:
   계산 환경에 따라 마지막 자릿수의 표시는 달라질 수 있지만 근은 약
   1.73205이다. np.sqrt(3)도 약 1.7320508076이므로 두 값이 허용오차
   범위에서 일치한다.
   -->

8. $f(x)=x^2+1$에 대해 `bisection(f, -1.0, 1.0)`을 실행하면 어떤 일이
   발생하는지 확인하고 그 이유를 설명하라.

   <!--
   풀이 및 정답:
   f(-1)=2이고 f(1)=2이므로 양 끝점의 함수값 부호가 같다.
   따라서 ValueError가 발생한다. 이 함수는 모든 실수 x에서 양수이므로 실근도 없다.
   -->
