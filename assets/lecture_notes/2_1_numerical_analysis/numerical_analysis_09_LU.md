---
layout: page
title: 수치해석
description: 재료공학도를 위한 수치해석
target: 2학년 1학기
permalink:
prerequisite: 선형 연립방정식, 가우스 소거법, Python 기초
toc:
  sidebar: left
---

- [1. 학습 목표](#1-학습-목표)
- [2. LU 분해](#2-lu-분해)
  - [2.1. 삼각행렬](#21-삼각행렬)
  - [2.2. 연립방정식 풀이](#22-연립방정식-풀이)
  - [2.3. LU 분해가 유용한 경우](#23-lu-분해가-유용한-경우)
- [3. 가우스 소거법과 LU 분해](#3-가우스-소거법과-lu-분해)
- [4. 손으로 계산하는 예제](#4-손으로-계산하는-예제)
  - [4.1. $\\boldsymbol A=\\boldsymbol L \\cdot \\boldsymbol U$ 구하기](#41-boldsymbol-aboldsymbol-l-cdot-boldsymbol-u-구하기)
  - [4.2. 전진 대입](#42-전진-대입)
- [\\end{bmatrix}](#endbmatrix)
  - [4.3. 후진 대입](#43-후진-대입)
- [\\end{bmatrix}](#endbmatrix-1)
- [5. Python 구현](#5-python-구현)
  - [5.1. LU 분해 확인](#51-lu-분해-확인)
  - [5.2. 연립방정식 풀이](#52-연립방정식-풀이)
- [6. 피벗팅이 필요한 경우](#6-피벗팅이-필요한-경우)
- [7. 보충: Jacobi 반복법](#7-보충-jacobi-반복법)
  - [7.1. 반복식](#71-반복식)
- [x\_i^{(k+1)}](#x_ik1)
  - [7.2. 간단한 예제](#72-간단한-예제)
- [\\boldsymbol x^{(1)}](#boldsymbol-x1)
- [\\boldsymbol x^{(2)}](#boldsymbol-x2)
  - [7.3. Python 구현](#73-python-구현)
- [8. 직접해법과 반복해법 비교](#8-직접해법과-반복해법-비교)
- [9. 정리](#9-정리)
- [10. 연습 문제](#10-연습-문제)
- [\\end{bmatrix}](#endbmatrix-2)
- [\\end{bmatrix}](#endbmatrix-3)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 행렬을 하삼각행렬과 상삼각행렬의 곱으로 나타낼 수 있다.
- 가우스 소거법의 소거 계수와 $L$ 행렬의 관계를 설명할 수 있다.
- $L\boldsymbol y=\boldsymbol b$를 전진 대입으로 풀 수 있다.
- $U\boldsymbol x=\boldsymbol y$를 후진 대입으로 풀 수 있다.
- LU 분해를 Python으로 구현하고 결과를 검증할 수 있다.
- 직접해법인 LU 분해와 반복해법인 Jacobi 방법의 차이를 설명할 수 있다.

# 2. LU 분해

LU 분해(LU decomposition)는 정사각행렬 $\boldsymbol A$를 다음 두 삼각행렬의
곱으로 나타내는 방법이다.

$$
\boxed{
\boldsymbol A=\boldsymbol L \cdot \boldsymbol U
}
$$

- $\boldsymbol L$: 하삼각행렬(lower triangular matrix)
- $\boldsymbol U$: 상삼각행렬(upper triangular matrix)

이 강의에서는 $L$의 대각 원소를 모두 1로 두는 Doolittle 형태를 사용한다.

## 2.1. 삼각행렬

4×4 행렬의 일반적인 형태는 다음과 같다.

$$
\boldsymbol L=
\begin{bmatrix}
1&0&0&0\\
l_{21}&1&0&0\\
l_{31}&l_{32}&1&0\\
l_{41}&l_{42}&l_{43}&1
\end{bmatrix},
\qquad
\boldsymbol U=
\begin{bmatrix}
u_{11}&u_{12}&u_{13}&u_{14}\\
0&u_{22}&u_{23}&u_{24}\\
0&0&u_{33}&u_{34}\\
0&0&0&u_{44}
\end{bmatrix}.
$$

$L$은 대각선 위의 원소가 0이고, $U$는 대각선 아래의 원소가 0이다.

## 2.2. 연립방정식 풀이

연립방정식

$$
\boldsymbol A \cdot \boldsymbol x=\boldsymbol b
$$

에서 $\boldsymbol A=\boldsymbol L \cdot \boldsymbol U$를 대입하면

$$
\boldsymbol L \cdot \boldsymbol U \cdot \boldsymbol x=\boldsymbol b
$$

이다. 새로운 벡터 $\boldsymbol y$를

$$
\boldsymbol y=\boldsymbol U \cdot \boldsymbol x
$$

라고 두면 두 개의 삼각 연립방정식으로 나눌 수 있다.

$$
\boldsymbol L \cdot \boldsymbol y=\boldsymbol b
$$

$$
\boldsymbol U \cdot \boldsymbol x=\boldsymbol y
$$

따라서 다음 순서로 해를 구한다.

1. $\boldsymbol L \cdot \boldsymbol y=\boldsymbol b$를 **전진 대입(forward substitution)**으로 푼다.
2. $\boldsymbol U \cdot \boldsymbol x=\boldsymbol y$를 **후진 대입(back substitution)**으로 푼다.

행렬의 역행렬을 직접 계산할 필요가 없다.

## 2.3. LU 분해가 유용한 경우

같은 계수행렬 $\boldsymbol A$에 대해 우변 벡터만 다른 여러 연립방정식을 생각해보자.

$$
\boldsymbol A \cdot \boldsymbol x^{(1)}=\boldsymbol b^{(1)},
\qquad
\boldsymbol A \cdot \boldsymbol x^{(2)}=\boldsymbol b^{(2)},
\qquad\ldots
$$

$\boldsymbol A=\boldsymbol L \cdot \boldsymbol U$는 한 번만 계산하고, 새로운 $\boldsymbol b$가 주어질 때마다 전진 대입과 후진 대입만
수행하면 된다. 행렬 분해에는 약 $O(n^3)$, 각 삼각 연립방정식 풀이에는
$O(n^2)$의 연산이 필요하므로 우변이 여러 개일 때 특히 유용하다.

# 3. 가우스 소거법과 LU 분해

가우스 소거법에서 피벗 아래의 원소를 없앨 때

$$
R_i\leftarrow R_i-m_{ik}R_k,
\qquad
m_{ik}=\frac{a_{ik}}{a_{kk}}
$$

를 사용했다. 전진 소거를 마치고 얻은 상삼각행렬이 $\boldsymbol U$가 되고, 각 단계에서 사용한
소거 계수 $m_{ik}$를 $\boldsymbol L$의 대각선 아래에 저장한다.

$$
L_{ik}=m_{ik},
\qquad i>k
$$

즉, 가우스 소거 과정에는 이미 LU 분해에 필요한 정보가 포함되어 있다.

# 4. 손으로 계산하는 예제

다음 연립방정식을 LU 분해로 풀어보자.

$$
\begin{aligned}
x+y+z&=6,\\
2x+3y+z&=11,\\
-x+2y+3z&=12.
\end{aligned}
$$

계수행렬과 우변 벡터는

$$
\boldsymbol A=
\begin{bmatrix}
1&1&1\\
2&3&1\\
-1&2&3
\end{bmatrix},
\qquad
\boldsymbol b=
\begin{bmatrix}
6\\11\\12
\end{bmatrix}
$$

이다.

## 4.1. $\boldsymbol A=\boldsymbol L \cdot \boldsymbol U$ 구하기

첫 번째 피벗 아래를 소거할 때 사용하는 계수는

$$
m_{21}=\frac{a_{21}}{a_{11}}=\frac{2}{1}=\textcolor{red}{2},
\qquad
m_{31}=\frac{a_{31}}{a_{11}}=\frac{-1}{1}=\textcolor{blue}{-1}
$$

이다. 이어서 두번째 세번째 행을 업데이트한다.

$$
R_2\leftarrow R_2-\textcolor{red}{2}R_1
$$

$$
R_3\leftarrow R_3-(\textcolor{blue}{-1})R_1
$$

그러면 $\boldsymbol U$는
$$
\begin{bmatrix}
1&1&1\\
0&1&-1\\
0&0&7
\end{bmatrix}
$$

소거한 뒤 두 번째 피벗 아래에서 사용하는 계수는

$$
m_{32}=\textcolor{green}{3}
$$

이다. 따라서

$$
\boldsymbol L=
\begin{bmatrix}
1&0&0\\
\textcolor{red}{2}&1&0\\
\textcolor{blue}{-1}&\textcolor{green}{3}&1
\end{bmatrix},
\qquad
\boldsymbol U=
\begin{bmatrix}
1&1&1\\
0&1&-1\\
0&0&7
\end{bmatrix}.
$$

직접 곱하면

$$
\boldsymbol L \cdot \boldsymbol U=
\begin{bmatrix}
1&1&1\\
2&3&1\\
-1&2&3
\end{bmatrix}
=\boldsymbol A
$$

임을 확인할 수 있다.

## 4.2. 전진 대입

먼저 $\boldsymbol L \cdot \boldsymbol y=\boldsymbol b$를 푼다.

$$
\begin{bmatrix}
1&0&0\\
2&1&0\\
-1&3&1
\end{bmatrix}
\begin{bmatrix}
y_1\\y_2\\y_3
\end{bmatrix}
=
\begin{bmatrix}
6\\11\\12
\end{bmatrix}
$$

첫 번째 행부터 차례대로 계산하면

$$
y_1=6
$$

$$
2y_1+y_2=11
\quad\Longrightarrow\quad
y_2=-1
$$

$$
-y_1+3y_2+y_3=12
\quad\Longrightarrow\quad
y_3=21
$$

이다. 따라서

$$
\boldsymbol y=
\begin{bmatrix}
\textcolor{magenta}{6}\\\textcolor{magenta}{-1}\\\textcolor{magenta}{21}
\end{bmatrix}.
$$

## 4.3. 후진 대입

이제 $\boldsymbol U \cdot \boldsymbol x=\textcolor{magenta}{\boldsymbol y}$를 푼다.

$$
\begin{bmatrix}
1&1&1\\
0&1&-1\\
0&0&7
\end{bmatrix}
\begin{bmatrix}
x_1\\x_2\\x_3
\end{bmatrix}
=
\begin{bmatrix}
\textcolor{magenta}{6}\\\textcolor{magenta}{-1}\\\textcolor{magenta}{21}
\end{bmatrix}.
$$

마지막 행부터 계산하면

$$
7x_3=21
\quad\Longrightarrow\quad x_3=3
$$

$$
x_2-x_3=-1
\quad\Longrightarrow\quad x_2=2
$$

$$
x_1+x_2+x_3=6
\quad\Longrightarrow\quad x_1=1
$$

이다. 따라서

$$
\boxed{(x_1,x_2,x_3)=(1,2,3)}
$$

이다.

# 5. Python 구현

다음 함수는 피벗팅이 필요하지 않은 행렬을 Doolittle 방법으로 LU 분해한다.

~~~python
import numpy as np

def lu_decomposition(A, tol=1e-12):
    A = np.asarray(A, dtype=float)

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A는 정사각행렬이어야 합니다.")

    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros_like(A)

    for i in range(n):
        # U의 i번째 행
        for j in range(i, n):
            known = L[i, :i]@U[:i, j]
            U[i, j] = A[i, j]-known

        if abs(U[i, i]) < tol:
            raise np.linalg.LinAlgError(
                "0에 가까운 피벗입니다. 피벗팅이 필요한 행렬일 수 있습니다."
            )

        # L의 i번째 열
        for j in range(i+1, n):
            known = L[j, :i]@U[:i, i]
            L[j, i] = (A[j, i]-known)/U[i, i]

    return L, U
~~~

## 5.1. LU 분해 확인

~~~python
A = np.array([
    [ 1.0, 1.0, 1.0],
    [ 2.0, 3.0, 1.0],
    [-1.0, 2.0, 3.0],
])

L, U = lu_decomposition(A)

print("L =")
print(L)
print("U =")
print(U)
print("L @ U =")
print(L@U)
print("A와 LU가 같은가?", np.allclose(A, L@U))
~~~

## 5.2. 연립방정식 풀이

전진 대입과 후진 대입을 함수로 작성한다.

~~~python
def forward_substitution(L, b):
    b = np.asarray(b, dtype=float)
    n = len(b)
    y = np.zeros(n)

    for i in range(n):
        known = L[i, :i]@y[:i]
        y[i] = (b[i]-known)/L[i, i]

    return y

def back_substitution(U, y):
    y = np.asarray(y, dtype=float)
    n = len(y)
    x = np.zeros(n)

    for i in range(n-1, -1, -1):
        known = U[i, i+1:]@x[i+1:]
        x[i] = (y[i]-known)/U[i, i]

    return x
~~~

앞의 예제를 계산해보자.

~~~python
b = np.array([6.0, 11.0, 12.0])

y = forward_substitution(L, b)
x = back_substitution(U, y)

print("y:", y)
print("solution:", x)
print("NumPy:", np.linalg.solve(A, b))
print("residual norm:", np.linalg.norm(A@x-b))
~~~

# 6. 피벗팅이 필요한 경우

다음 행렬은 첫 번째 피벗이 0이므로 위의 단순한 LU 구현을 바로 적용할 수 없다.

$$
A=
\begin{bmatrix}
0&1\\
1&1
\end{bmatrix}.
$$

실제 계산에서는 행 교환을 포함한 부분 피벗팅을 사용하며 일반적으로 다음 형태로
분해한다.

$$
\boxed{
PA=LU
}
$$

여기서 $P$는 행 교환을 나타내는 순열행렬(permutation matrix)이다. 피벗팅은 0인
피벗을 피할 뿐 아니라 작은 피벗으로 인한 반올림 오차의 증폭도 줄여준다.

이 강의의 직접 구현은 $A=LU$의 원리를 이해하기 위한 것이다. 실제 문제에서는
피벗팅이 구현된 **scipy.linalg.lu_factor**, **scipy.linalg.lu_solve** 또는
**np.linalg.solve**와 같은 검증된 함수를 사용하는 것이 좋다.

# 7. 보충: Jacobi 반복법

LU 분해는 직접해법이지만 Jacobi 방법은 초기값에서 시작하여 해를 반복적으로
개선하는 반복해법이다.

## 7.1. 반복식

연립방정식의 $i$번째 행은

$$
a_{ii}x_i+\sum_{j\ne i}a_{ij}x_j=b_i
$$

이므로 $a_{ii}\ne0$이면

$$
\boxed{
x_i^{(k+1)}
=
\frac{1}{a_{ii}}
\left(
b_i-\sum_{j\ne i}a_{ij}x_j^{(k)}
\right)
}
$$

이다. Jacobi 방법은 오른쪽의 모든 값을 이전 반복 $k$의 값으로 계산한다.

## 7.2. 간단한 예제

$$
\begin{aligned}
4x_1+x_2&=7,\\
x_1+3x_2&=8
\end{aligned}
$$

을 반복식으로 바꾸면

$$
x_1^{(k+1)}=\frac{7-x_2^{(k)}}{4},
\qquad
x_2^{(k+1)}=\frac{8-x_1^{(k)}}{3}
$$

이다. 초기값을 $\boldsymbol x^{(0)}=(0,0)$으로 정하면

$$
\boldsymbol x^{(1)}
=
\left(
\frac{7}{4},
\frac{8}{3}
\right)
\approx(1.750,2.667)
$$

이고,

$$
\boldsymbol x^{(2)}
=
\left(
\frac{7-2.667}{4},
\frac{8-1.750}{3}
\right)
\approx(1.083,2.083)
$$

이다. 반복하면 정확한 해

$$
\boldsymbol x=
\left(
\frac{13}{11},
\frac{25}{11}
\right)
\approx(1.182,2.273)
$$

에 가까워진다.

## 7.3. Python 구현

~~~python
def jacobi(A, b, x0=None, tol=1e-8, max_iter=100):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    n = len(b)

    diagonal = np.diag(A)

    if np.any(np.abs(diagonal) < 1e-14):
        raise ZeroDivisionError("대각 원소가 0이면 반복식을 계산할 수 없습니다.")

    x = np.zeros(n) if x0 is None else np.asarray(x0, dtype=float).copy()
    remainder = A-np.diag(diagonal)

    for iteration in range(1, max_iter+1):
        x_new = (b-remainder@x)/diagonal

        if np.linalg.norm(x_new-x) <= tol:
            return x_new, iteration

        x = x_new

    raise RuntimeError("최대 반복 횟수 안에 수렴하지 않았습니다.")
~~~

~~~python
A_jacobi = np.array([
    [4.0, 1.0],
    [1.0, 3.0],
])
b_jacobi = np.array([7.0, 8.0])

x_jacobi, iterations = jacobi(A_jacobi, b_jacobi)

print("Jacobi:", x_jacobi)
print("iterations:", iterations)
print("residual norm:", np.linalg.norm(A_jacobi@x_jacobi-b_jacobi))
~~~

Jacobi 방법은 모든 행렬에서 수렴하는 것은 아니다. 행렬이 엄격한 대각우세인 경우,
즉 각 행에서

$$
|a_{ii}|>\sum_{j\ne i}|a_{ij}|
$$

이면 수렴이 보장된다. 이는 충분조건이며 Jacobi 방법이 수렴하는 유일한 조건은 아니다.

# 8. 직접해법과 반복해법 비교

| 항목 | LU 분해 | Jacobi 방법 |
|---|---|---|
| 분류 | 직접해법 | 반복해법 |
| 초기값 | 필요하지 않음 | 필요함 |
| 주요 계산 | 행렬 분해와 삼각 대입 | 반복적인 행렬·벡터 계산 |
| 수렴 판단 | 별도의 반복 수렴 조건 없음 | 종료 조건과 최대 반복 횟수 필요 |
| 같은 $A$, 여러 $b$ | 분해를 재사용할 수 있음 | 각 $b$마다 반복 계산 |
| 주의 사항 | 실제 계산에서는 피벗팅 필요 | 행렬에 따라 발산할 수 있음 |

# 9. 정리

- LU 분해는 $A=LU$로 계수행렬을 두 삼각행렬로 분리한다.
- 가우스 소거의 소거 계수는 $L$의 대각선 아래에 저장된다.
- $Ly=b$는 전진 대입, $Ux=y$는 후진 대입으로 푼다.
- 같은 $A$에 여러 우변 $b$가 주어지면 LU 분해를 재사용할 수 있다.
- 피벗팅이 필요하면 분해는 일반적으로 $PA=LU$ 형태가 된다.
- Jacobi 방법은 초기값에서 시작하는 반복해법이며 행렬에 따라 발산할 수 있다.

# 10. 연습 문제

강의에서 다룬 LU 분해와 삼각 대입을 확인하는 기초 문제이다.

1. 다음 빈칸을 채워라.

   - LU 분해는 $A=(　　　　)(　　　　)$로 나타낸다.
   - $L$은 (　　　　　　)행렬이고 $U$는 (　　　　　　)행렬이다.
   - $Ly=b$는 (　　　　　　) 대입으로 푼다.
   - $Ux=y$는 (　　　　　　) 대입으로 푼다.

   <!--
   풀이 및 정답:
   A=LU이다. L은 하삼각행렬, U는 상삼각행렬이다.
   Ly=b는 전진 대입, Ux=y는 후진 대입으로 푼다.
   -->

2. 다음 행렬 중 하삼각행렬과 상삼각행렬을 각각 고르라.

   $$
   A_1=
   \begin{bmatrix}
   1&0\\2&1
   \end{bmatrix},
   \qquad
   A_2=
   \begin{bmatrix}
   3&4\\0&2
   \end{bmatrix}.
   $$

   <!--
   풀이 및 정답:
   A_1은 대각선 위가 0이므로 하삼각행렬이고, A_2는 대각선 아래가 0이므로
   상삼각행렬이다.
   -->

3. 다음 두 행렬을 곱하여 $A=LU$를 구하라.

   $$
   L=
   \begin{bmatrix}
   1&0\\2&1
   \end{bmatrix},
   \qquad
   U=
   \begin{bmatrix}
   3&1\\0&4
   \end{bmatrix}.
   $$

   <!--
   풀이 및 정답:
   첫 번째 행은 [3,1]이고 두 번째 행은 [6,6]이다.
   따라서 A=[[3,1],[6,6]]이다.
   -->

4. 행렬

   $$
   A=
   \begin{bmatrix}
   2&1\\6&5
   \end{bmatrix}
   $$

   의 첫 번째 열에서 사용할 소거 계수 $m_{21}$을 구하고 $L$과 $U$를 구하라.

   <!--
   풀이 및 정답:
   m_21=6/2=3이다. R_2를 R_2-3R_1로 바꾸면 [0,2]가 된다.
   따라서 L=[[1,0],[3,1]], U=[[2,1],[0,2]]이고 LU=A이다.
   -->

5. 다음 하삼각 연립방정식을 전진 대입으로 풀어라.

   $$
   \begin{bmatrix}
   1&0\\
   2&1
   \end{bmatrix}
   \begin{bmatrix}
   y_1\\y_2
   \end{bmatrix}
   =
   \begin{bmatrix}
   5\\13
   \end{bmatrix}.
   $$

   <!--
   풀이 및 정답:
   첫 번째 행에서 y_1=5이다. 두 번째 행에서 2y_1+y_2=13이므로
   y_2=13-10=3이다.
   -->

6. 다음 상삼각 연립방정식을 후진 대입으로 풀어라.

   $$
   \begin{bmatrix}
   2&1\\
   0&3
   \end{bmatrix}
   \begin{bmatrix}
   x_1\\x_2
   \end{bmatrix}
   =
   \begin{bmatrix}
   7\\6
   \end{bmatrix}.
   $$

   <!--
   풀이 및 정답:
   두 번째 행에서 x_2=2이다. 첫 번째 행에서 2x_1+2=7이므로 x_1=2.5이다.
   -->

7. 다음 코드의 빈칸을 채워 LU 분해 결과를 확인하라.

   ~~~python
   L, U = lu_decomposition(A)
   reconstructed = ____ @ ____
   print(np.allclose(A, reconstructed))
   ~~~

   <!--
   풀이 및 정답:
   빈칸은 L과 U이다. reconstructed=L@U로 계산하며 결과는 True이다.
   -->

8. 같은 계수행렬 $A$에 서로 다른 우변 $b$가 여러 개 주어질 때 LU 분해가
   유용한 이유를 한 문장으로 설명하라.

   <!--
   풀이 및 정답:
   A=LU를 한 번만 계산한 뒤 각 우변마다 전진 대입과 후진 대입만 수행하면
   되므로 계산을 줄일 수 있다.
   -->

9. 다음 행렬에 단순한 $A=LU$ 분해를 바로 적용하기 어려운 이유를 설명하라.

   $$
   A=
   \begin{bmatrix}
   0&1\\
   1&1
   \end{bmatrix}.
   $$

   <!--
   풀이 및 정답:
   첫 번째 피벗이 0이므로 소거 계수를 계산할 때 0으로 나누게 된다.
   두 행을 교환하는 피벗팅이 필요하며, 이때 일반적으로 PA=LU 형태로 표현한다.
   -->

10. Jacobi 예제에서 초기값 $x_1^{(0)}=0$, $x_2^{(0)}=0$일 때 첫 번째
    반복값을 구하라.

    $$
    x_1^{(k+1)}=\frac{7-x_2^{(k)}}{4},
    \qquad
    x_2^{(k+1)}=\frac{8-x_1^{(k)}}{3}.
    $$

    <!--
    풀이 및 정답:
    x_1^(1)=7/4=1.75이고 x_2^(1)=8/3≈2.667이다.
    -->
