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
- [1. 비선형 연립 방정식](#1-비선형-연립-방정식)
  - [1.1. 비선형 연립 방정식의 해](#11-비선형-연립-방정식의-해)
  - [1.2. Multivariate Newton-Raphson method](#12-multivariate-newton-raphson-method)
    - [1.2.1. Single variate Newton-Raphson method](#121-single-variate-newton-raphson-method)
    - [1.2.2. Multivariate Newton-Raphson method](#122-multivariate-newton-raphson-method)
    - [1.2.3. Multivariate Newton-Raphson method algorithm](#123-multivariate-newton-raphson-method-algorithm)
    - [1.2.4. Gauss elimination method를 활용한 Multivariate Newton-Raphson method](#124-gauss-elimination-method를-활용한-multivariate-newton-raphson-method)
    - [1.2.5. Gauss elimination method를 활용한 Multivariate Newton-Raphson method 예시](#125-gauss-elimination-method를-활용한-multivariate-newton-raphson-method-예시)
  - [1.3. Multivariate NR method를 함수화시키자.](#13-multivariate-nr-method를-함수화시키자)
- [2. Multivariate NR method를 활용한 예시](#2-multivariate-nr-method를-활용한-예시)
- [3. 예시: 비선형 다항식](#3-예시-비선형-다항식)
- [4. 예시: 3원 연립방정식](#4-예시-3원-연립방정식)


# 1. 비선형 연립 방정식

## 1.1. 비선형 연립 방정식의 해
- 세상 모든 문제들이 선형적(linear)이다면 가우스 소거법이나 LU 분해법을 활용해 풀이가
 가능하면 참 좋겠지만, 그렇지 않다... 실은 대부분 흥미로운 일들은 비선형적이다.

- 예를 들어 다음 연립 방정식을 보자.

  $$
  x^2+y^2=7
  \newline
  e^x+y=8
  $$

  이 두 식을 만족하는 $(x,y)$좌표가 존재하는 것은 아래 Python 프로그램을 통해
  쉽게 확인할 수 있다.

```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
## 1st line
ths=np.linspace(-np.pi,np.pi)
r=np.sqrt(7)
x=np.cos(ths)*r
y=np.sin(ths)*r
plt.plot(x,y,label='Line1')
## 2nd line
x=np.linspace(-3,3)
y=8-np.exp(x)
plt.plot(x,y,label='Line2')
plt.legend()
  ```

## 1.2. Multivariate Newton-Raphson method

### 1.2.1. Single variate Newton-Raphson method
- Single variate Newton-Raphson method는 이미 다루었다.

- 아래 알고리듬을 따르면 되었다.

$$
x^{(n+1)}=x^{(n)}-\frac{f(x^{(n)})}{f^\prime(x^{(n)})}
$$

### 1.2.2. Multivariate Newton-Raphson method

- Multivariate Newton-Raphson method의 알고리듬도 유사한 형태이다.

- 우선 앞서 다루었던 연립방정식을 아래와 같이 표현하자.

  $$
  f_1(x_1,x_2)=x_1^2+x_2^2-7
  \newline
  f_2(x_1,x_2)=e^{x_1}+x_2-8
  $$

```python
def func(x1,x2):
    f=np.zeros(2) #
    f[0]=x1**2+x2**2-7
    f[1]=np.exp(x1)+x2-8
    return f
```

- 그런 다음 Jacobian matrix를 구하자. 이는 아래와 같이 정의된다.

$$
J_{ij}=\frac{\partial f_i}{\partial x_j}
$$

따라서,

$$
J_{11}=\frac{\partial f_1}{\partial x_1}=2x_1
\newline
J_{12}=\frac{\partial f_1}{\partial x_2}=2x_2
\newline
J_{21}=\frac{\partial f_2}{\partial x_1}=e^{x_1}
\newline
J_{22}=\frac{\partial f_2}{\partial x_2}=1
$$

```python
def jacob(x1,x2):
    j=np.zeros(2,2) # 2x2 jacob
    j[0,0]=2*x1
    j[0,1]=2*x2
    j[1,0]=np.exp(x1)
    j[1,1]=1
    return j
```

### 1.2.3. Multivariate Newton-Raphson method algorithm

- 그런 다음 아래 알고리듬을 따르면 된다.

$$
x^{n+1}_1=x^{n}_1-J_{11}^{-1}f_1(x^n_1,x^n_2)-J_{12}^{-1}f_2(x^n_1,x^n_2)
$$
$$
x^{n+1}_2=x^{n}_2-J_{21}^{-1}f_1(x^n_1,x^n_2)-J_{22}^{-1}f_2(x^n_1,x^n_2)
$$

- 위 식을 행렬식을 활용해 표현하자면 아래와 같다.

    $$
    \begin{bmatrix}
    x_1^{n+1}\\
    x_2^{n+1}\\
    \end{bmatrix}
    $$

    $$
    =
    \begin{bmatrix}
    x_1^{n}\\
    x_2^{n}\\
    2.1. \end{bmatrix}
    -
    \begin{bmatrix}
    J_{11}(x_1^n,x_2^n) & J_{12}(x_1^n,x_2^n) \\
    J_{21}(x_1^n,x_2^n) & J_{22}(x_1^n,x_2^n) \\
    \end{bmatrix}^{-1}
    \cdot
    \begin{bmatrix}
    f_1(x_1^n,x_2^n)\\
    f_2(x_1^n,x_2^n)\\
    \end{bmatrix}
    $$

- 아래와 같이 좀 더 간략히 아래와 같이 표기해보자.

    $$
    \begin{bmatrix}
    \boldsymbol x^{n+1}\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    \boldsymbol x^{n}\\
    \end{bmatrix}
    -
    \begin{bmatrix}
    \boldsymbol J\\
    \end{bmatrix}^{-1}
    \cdot
    \begin{bmatrix}
    \boldsymbol f\\
    \end{bmatrix}
    $$

- 행렬과 벡터를 재배치 해보면...

    $$
    \begin{bmatrix}
    \boldsymbol J\\
    \end{bmatrix}
    \cdot
    \begin{pmatrix}
    \begin{bmatrix}
    \boldsymbol x^{n+1}\\
    \end{bmatrix}
    -
    \begin{bmatrix}
    \boldsymbol x^{n}\\
    \end{bmatrix}
    \end{pmatrix}
    =
    \begin{bmatrix}
    \boldsymbol f\\
    \end{bmatrix}
    $$

- 벡터의 변화량 $\Delta \boldsymbol x$를 활용하면

    $$
    \begin{bmatrix}
    \boldsymbol J \\
    \end{bmatrix}
    \cdot
    \begin{bmatrix}
    \Delta \boldsymbol x \\
    \end{bmatrix}
    =
    -\begin{bmatrix}
    \boldsymbol f \\
    \end{bmatrix}
    $$

- 로 표현 가능하다. 따라서, 앞서 배운 Gauss 소거법 등을 통해, 역행렬을 계산하지 않고,
$[\Delta \boldsymbol x]$를 구할 수 있다.

### 1.2.4. Gauss elimination method를 활용한 Multivariate Newton-Raphson method

- 그렇게 하기 위해서 아래 정의된 `guass`함수를 활용하자.

```python
def gauss(A):
    """
    Gauss elimination

    Arguments
    --------
    A: augmented matrix in  [n,n+1] dimension

    Returns
    -------
    Root in [n]-dimensional vector.
    """
    # swap and forward
    for icol in range(0,A.shape[0]-1):
        ## swap
        a=np.abs(A[icol:,icol])
        ind=np.argsort(a)
        ind=ind[::-1] # reverse order
        A[icol:,:]=A[icol:,:][ind,:]

        ## forward
        for irow in range(icol+1,A.shape[0]):
            A[irow,:]=A[irow,:]-A[irow,icol]/A[icol,icol]*A[icol,:]
    # now one could 'diagonalize'
    for icol in range(A.shape[0]-1,0,-1):
        for irow in range(0,icol):
            f=A[irow,icol]/A[icol,icol]
            A[irow,:]=A[irow,:]-f*A[icol,:]
    for icol in range(A.shape[0]):
        A[icol,:]=A[icol,:]/A[icol,icol]
    return A[:,-1]
```

### 1.2.5. Gauss elimination method를 활용한 Multivariate Newton-Raphson method 예시

- 위 `gauss`함수를 활용해 풀이한 예시이다.

```python
## Canvas

## 1st line
ths=np.linspace(-np.pi,np.pi)
r=np.sqrt(7)
x=np.cos(ths)*r
y=np.sin(ths)*r

## 2nd line
x=np.linspace(-3,3)
y=8-np.exp(x)

## Function and Jacobian required for NR procedure
def func(x1,x2):
    f=np.zeros(2) #
    f[0]=x1**2+x2**2-7
    f[1]=np.exp(x1)+x2-8
    return f
def jacob(x1,x2):
    j=np.zeros((2,2)) # 2x2 jacob
    j[0,0]=2*x1
    j[0,1]=2*x2
    j[1,0]=np.exp(x1)
    j[1,1]=1
    return j

## NEWTON-RAPHSON begins here.
# hist arrays for recording changes.
## Initial guess
x=np.zeros(2) ## initial guess
x[::]=-1.0 ## initial guess

# Tolerance setting
tol=1e-9
err=tol*2
#
n=0
while err>tol and n<50:
    # jacobian and functions
    J=jacob(*x)
    F=func(*x)

    # Create augmented matrix A
    A=np.zeros((J.shape[0],J.shape[0]+1))
    A[:2,:2]=J[:,:]
    A[:,-1]=-F[::]

    # Obtain Delta x via guass elimination method
    dx=gauss(A)

    # Update x
    x=x+dx
    n+=1

    # estimate the error
    err=np.sqrt((F**2).sum())

print('solution:',x)
```

## 1.3. Multivariate NR method를 함수화시키자.

```python
def mvNR(func,func_jac,xinit):
    """
    Arguments
    ---------
    func: objective function
    func_jac: jacobian
    xinit: initial guess on x vectors.

    Returns
    -------
    x     : solution vector
    hist  : trajectory of x vector
    fhist : trajectory of f vector
    """
    x=xinit[::]
    # hist arrays for recording changes.
    hist=[]
    fhist=[]
    # Tolerance setting
    tol=1e-9
    err=tol*2
    n=0
    maxiter=50
    while err>tol and n<maxiter:
        # jacobian and functions
        J=jacob(*x)
        F=func(*x)

        # history
        hist.append(x)
        fhist.append(F)

        # Create augmented matrix A
        A=np.zeros((J.shape[0],J.shape[0]+1))
        A[:2,:2]=J[:,:]
        A[:,-1]=-F[::]

        # Obtain Delta x via guass elimination method
        dx=gauss(A)

        # updates x, count (n), and error
        x=x+dx
        n+=1
        err=np.sqrt((F**2).sum())

    hist=np.array(hist)
    fhist=np.array(fhist)
    return x,hist,fhist
  ```

# 2. Multivariate NR method를 활용한 예시
- `mvNR`함수를 앞선 `guass`함수와 함께 사용한다면 아래와 같이 매우 짧은 몇 줄의
  코드로 앞선 예제를 작성할 수 있다. 따라서 한번 작성해 놓은 함수를 다시 사용할 수 있게 되었다.
  학생들이 이 경험을 통해 모듈화의 이점을 몸소 체험해 보길 바란다.

```python
def f1(x,y):  return x*y-10
def f2(x,y):  return x**2-y-3
def func(x,y): return np.array([f1(x,y),f2(x,y)])
def jacob(x,y):
    j=np.zeros((2,2))
    j[0,0]=y
    j[0,1]=x
    j[1,0]=2*x
    j[1,1]=-1
    return j

## NEWTON-RAPHSON begins here.
## Initial guess
x=np.zeros(2) ## initial guess
x[::]=4.0 ## initial guess
x,hist,fhist=mvNR(func,jacob,xinit=np.ones(2))
```

# 3. 예시: 비선형 다항식
- 다음 비선형 다항식을 풀어보자.
    $$
    \begin{bmatrix}
    x_1^2+x_2^2-7\\
    e^{x_1}+x_2-8
    8. \end{bmatrix}
    =
    \begin{bmatrix}
    0\\
    0\\
    \end{bmatrix}
    $$

# 4. 예시: 3원 연립방정식
- 다음 3원 연립방정식을 풀어보자.
    $$
    \begin{bmatrix}
    x_1^2+x_2^2+x_3^2\\
    e^{x_1}+x_2+x_3\\
    x_1+x_2+x_3 \\
    \end{bmatrix}
    =
    \begin{bmatrix}
    3\\
    8\\
    1\\
    \end{bmatrix}
    $$