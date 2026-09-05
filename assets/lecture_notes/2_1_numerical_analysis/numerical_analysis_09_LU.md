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

- [1. LU decomposition](#1-lu-decomposition)
  - [1.1. 4x4행렬의 예](#11-4x4행렬의-예)
- [2. Jacobi 법](#2-jacobi-법)
  - [2.1. 예시](#21-예시)
  - [2.2. 예시: 3x3](#22-예시-3x3)


# 1. LU decomposition

- LU decomposition
- Gauss 소거법과 더불어 설명되는 연립 방정식 풀이법

$$
\boldsymbol A\cdot \boldsymbol x = \boldsymbol b
$$

를 만족시키는 벡터 $\boldsymbol x$의 $x_1,x_2,...,x_n$을 구하는 방법 중에
하나로써, 행렬 $\boldsymbol A$를 아래와 같이 나뉘어 활용한다.

$$
\boldsymbol A=\boldsymbol L \cdot \boldsymbol U
$$

$\boldsymbol L$: **L**ower triangular matrix (대각선을 따라서 1)

$\boldsymbol U$: **U**ower triangular matrix

## 1.1. 4x4행렬의 예

- 일반적 형태

    $$
    \boldsymbol A
    =
    \begin{bmatrix}
    A_{11} & A_{12} & A_{13} & A_{14}\\
    A_{21} & A_{22} & A_{23} & A_{24}\\
    A_{31} & A_{32} & A_{33} & A_{34} \\
    A_{41} & A_{42} & A_{43} & A_{44}\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    1 & 0 & 0 & 0\\
    L_{21} & 1 & 0 &0 \\
    L_{31} & L_{32} & 1 &0 \\
    L_{41} & L_{42} & L_{43} &1 \\
    \end{bmatrix}
    \cdot
    \begin{bmatrix}
    U_{11} & U_{12} & U_{13} & U_{14}\\
    0 & U_{22} & U_{23} & U_{24} \\
    0 & 0 & U_{33} & U_{34} \\
    0 & 0 & 0 & U_{44} \\
    \end{bmatrix}
    $$

- 예시

    $$
    \boldsymbol A
    =
    \begin{bmatrix}
    2& 1& 0 & 3 \\
    4& 4& 1& 7 \\
    2 &-1& 2 &4 \\
    6 & 7 & 5& 15 \\
    \end{bmatrix}
    =
    \begin{bmatrix}
    1 & 0 & 0 & 0\\
    L_{21} & 1 & 0&0 \\
    L_{31} & L_{32} & 1 &0 \\
    L_{41} & L_{42} & L_{43} & 1 \\
    \end{bmatrix}
    \cdot
    \begin{bmatrix}
    U_{11} & U_{12} & U_{13} & U_{14}\\
    0 & U_{22} & U_{23} & U_{24}\\
    0 & 0 & U_{33} & U_{34} \\
    0 & 0 & 0 & U_{44} \\
    \end{bmatrix}
    $$

  <!-- + 유용한 점
    * Swapping은 고려하지 않는 경우를 설명
    - 열 1: icol=0, irow=icol+1:ncol
    0 & 0 & U_{33} & U_{34} \\
    $$
    \boldsymbol A\cdot \boldsymbol x = \boldsymbol b
    $$
    을
    $$
    \rightarrow
    \boldsymbol L \cdot (\boldsymbol U\cdot \boldsymbol x) = \boldsymbol b
    $$
    로 계산하면,
    $$
    \boldsymbol U\cdot \boldsymbol x = b
    $$
    는  -->

# 2. Jacobi 법

  - Newton-Raphson 처럼 반복하여 행렬 풀이

  - 개념

    $$
    \boldsymbol A \cdot \boldsymbol x = \boldsymbol b
    $$

    $\boldsymbol A$가 $n\times n$행렬이라 하면, 각 행 $i$마다 아래 식이

    $$
    \sum_{j=1}^nA_{ij}x_j=b_i
    $$

    만족해야 함. 위 식을 바꿔 표현하여 각 행 $i$에 대해 아래와 같이 전개 가능함.

    $$
    A_{ii}x_i+\sum_{j\ne i}^nA_{ij}x_j=b_i
    $$

    만약 $A_{ii}\ne 0$이면, 고정되어 있는 한 행 $i$에 대한 위 식을 바꿔 $x_i$에 대해 표현하면

    $$
    x_i=\frac{1}{A_{ii}}\bigg(b_i-\sum_{j\ne i}^nA_{ij}x_j\bigg)
    $$

  - 반복 알고리듬
    앞선 식에서 우변과 좌변의 $\boldsymbol x$벡터를 각각 직전$(k)$, 그리고 직후 $(k+1)$ 값으로
    표현하면

    $$
    x_i^{(k+1)}=\frac{1}{A_{ii}}\bigg(b_i-\sum_{j\ne i}^nA_{ij}x_j^{(k)}\bigg)
    $$

    로 표현되며, 위 반복문을 활용해 $\boldsymbol x$를 평가함.

  - 예시: 2x2

    $$
    \bigg(
    \begin{matrix}
    4x_1+x_2=7  \ \ \text{eq. (1)}\\
    x_1+3x_2=8   \ \ \text{eq. (2)}
    \end{matrix}
    $$

    이라면 각 $i=1,2$ 마다 아래 두 식이 성립된다.

    $$
    x_1^{(k+1)}=\frac{1}{A_{11}}(b_1-\sum_{j\ne 1}A_{1j}x_j^{(k)})=\frac{1}{4}(7-\sum_{j\ne1}A_{1j}x_j^{(k)}) \ \ \ \ Eq. (1)
    \newline
    x_2^{(k+1)}=\frac{1}{A_{22}}(b_2-\sum_{j\ne 2}A_{2j}x_j^{(k)})=\frac{1}{3}(8-\sum_{j\ne2}A_{2j}x_{j}^{(k)}) \ \ \ \ Eq. (2)
    $$

## 2.1. 예시
  - 초기값 $\boldsymbol x^{(0)}=(0,0)$으로 시작해보자.

    - Iteration 1
    * 식1

      $$
      x_1^{(1)}=\frac{1}{4}(7-\sum_{j\ne 1}A_{1j}x_j^{(0)})=\frac{1}{4}\times 7=1.75
      $$

    * 식2

      $$
      x_2^{(k+1)}=\frac{1}{3}(8-\sum_{j\ne 2}A_{2j}x_j^{(k)})=\frac{1}{3}\times8\approx2.667
      $$
    - Iteration 2
    * 식1

      $$
      x_1^{(2)}=\frac{1}{4}(7-\sum_{j\ne 1}A_{1j}x_j^{(1)})=\frac{1}{4}(7-2.667)=1.083
      $$

    * 식2

      $$
      x_2^{(2)}=\frac{1}{3}(8-\sum_{j\ne 2}A_{2j}x_j^{(2)})=\frac{1}{3}(8-1.75)=2.083
      $$
    - ... 반복

  - 종료 조건: 오차의 수렴

    - 오차 조건 1.

    $$
    |\boldsymbol{A}\cdot\boldsymbol{x}^{(k+1)}-\boldsymbol{b}|<Tol.
    $$
    - 오차 조건 2.

    $$
    |\boldsymbol{x}^{(k+1)}-\boldsymbol{x}^{(k)}| < Tol.
    $$

## 2.2. 예시: 3x3

```python
import matplotlib.pyplot as plt
import numpy as np

A=np.zeros((3,3))
b=np.zeros(3)
# filling up the matrix.
A[0,:]=12,3,1
A[1,:]=9,-11,5
A[2,:]=1,-10,-20

b[:]=3,4,5

ndim=b.shape[0]
x=np.zeros(ndim)
tol=1e-4
err=tol*2
k=0
hist=[]
while err> tol and k<100: # max iter. set to 100
    newx=np.zeros(ndim)
    for icol in range(ndim):
        summation=0.
        for jrow in range(ndim):
            if icol==jrow:
                pass
            else:
                summation+=A[icol,jrow]*x[jrow]
        newx[icol]=(b[icol]-summation)/A[icol,icol]
        #x[icol]=1/A[icol,icol]*(b[icol]-)
    err=np.sqrt(((newx-x)**2).sum())
    Ea=np.sqrt(((A@newx-b)**2).sum())
    x[::]=newx[::]
    hist.append([err,Ea])
    k+=1
hist=np.array(hist)

plt.plot(hist[:,0],'-x',label=r'$|\boldsymbol{A}\cdot\boldsymbol{x}^{(k+1)}-\boldsymbol{b}|$')
plt.plot(hist[:,1],'-o',label=r'$|\boldsymbol{x}^{(k+1)}-\boldsymbol{x}^{(k)}|$')
plt.legend()
```