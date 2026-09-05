---
layout: page
title: 수치해석
description: 재료공학도를 위한 수치해석
target: 2학년 1학기
permalink:
prerequisite: 선형 연립방정식, 행렬과 벡터, Python 기초
toc:
  sidebar: left
---

- [1. 학습 목표](#1-학습-목표)
- [2. 가우스 소거법](#2-가우스-소거법)
  - [2.1. 확대행렬](#21-확대행렬)
- [\[\\boldsymbol A\\mid\\boldsymbol b\]](#boldsymbol-amidboldsymbol-b)
  - [2.2. 기본 행 연산](#22-기본-행-연산)
  - [2.3. 전체 알고리듬](#23-전체-알고리듬)
- [3. 손으로 계산하는 예제](#3-손으로-계산하는-예제)
  - [3.1. 확대행렬 만들기](#31-확대행렬-만들기)
  - [3.2. 첫 번째 열 소거](#32-첫-번째-열-소거)
  - [3.3. 두 번째 열 소거](#33-두-번째-열-소거)
  - [3.4. 후진 대입 (back substitution)](#34-후진-대입-back-substitution)
- [4. 부분 피벗팅](#4-부분-피벗팅)
- [5. Python 구현](#5-python-구현)
  - [5.1. 계산 예제](#51-계산-예제)
- [(x,y,z)](#xyz)
  - [5.2. 잔차 확인](#52-잔차-확인)
- [6. Gauss–Jordan 소거법과의 차이](#6-gaussjordan-소거법과의-차이)
- [7. 계산량과 주의 사항](#7-계산량과-주의-사항)
- [8. 정리](#8-정리)
- [9. 연습 문제](#9-연습-문제)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 연립방정식을 확대행렬(augmented matrix)로 나타낼 수 있다.
- 기본 행 연산을 이용하여 확대행렬을 상삼각(upper triangular) 형태로 바꿀 수 있다.
- 소거 계수를 계산하고 전진 소거(forward elimination)를 수행할 수 있다.
- 후진 대입(back substitution)으로 미지수를 구할 수 있다.
- 부분 피벗팅(partial pivoting)이 필요한 이유를 설명할 수 있다.
- 가우스 소거법(Gaussian elimination)을 Python으로 구현하고 잔차로 결과를 확인할 수 있다.

# 2. 가우스 소거법

가우스 소거법(Gaussian elimination)은 선형 연립방정식

$$
\boldsymbol A \cdot \boldsymbol x=\boldsymbol b
$$

를 기본 행 연산으로 변형하여 푸는 직접해법이다. 계산 과정은 크게 두 단계로
나뉜다.

1. **전진 소거(forward elimination):** 계수행렬을 상삼각행렬로 만든다.
2. **후진 대입(back substitution):** 마지막 식부터 거꾸로 미지수를 구한다.

## 2.1. 확대행렬

다음 연립방정식을 생각하자.

$$
\begin{aligned}
a_{11}x_1+a_{12}x_2+a_{13}x_3&=b_1,\\
a_{21}x_1+a_{22}x_2+a_{23}x_3&=b_2,\\
a_{31}x_1+a_{32}x_2+a_{33}x_3&=b_3.
\end{aligned}
$$

계수행렬과 우변 벡터를 결합한 행렬을 **확대행렬(augmented matrix)**이라고 한다.

$$
[\boldsymbol A\mid\boldsymbol b]
=
\left[
\begin{array}{ccc|c}
a_{11}&a_{12}&a_{13}&b_1\\
a_{21}&a_{22}&a_{23}&b_2\\
a_{31}&a_{32}&a_{33}&b_3
\end{array}
\right]
$$

**세로선은 계수행렬과 우변 벡터를 구분하기 위한 표시이며 행렬의 원소가 아니다.

## 2.2. 기본 행 연산

연립방정식의 해를 바꾸지 않는 기본 행 연산은 세 가지이다.

1. 두 행(row)을 서로 교환한다.

   $$
   R_i\leftrightarrow R_j
   $$

2. 한 행에 0이 아닌 상수를 곱한다.

   $$
   R_i\leftarrow cR_i,
   \qquad c\ne0
   $$

3. 한 행에 다른 행의 배수를 더한다.

   $$
   R_i\leftarrow R_i+cR_j
   $$

전진 소거에서는 주로 세 번째 연산을 다음 형태로 사용한다.

$$
R_i\leftarrow R_i-m_{ik}R_k,
\qquad
m_{ik}=\frac{a_{ik}}{a_{kk}}
$$

여기서 $a_{kk}$는 현재 계산의 기준이 되는 **피벗(pivot)**이고,
$m_{ik}$는 **소거 계수(multiplier)**이다.

## 2.3. 전체 알고리듬

$n\times n$ 연립방정식에 대한 과정은 다음과 같다.

1. 확대행렬 $[\boldsymbol A\mid\boldsymbol b]$를 만든다.
2. 첫 번째 열(column)부터 피벗을 선택한다.
3. 필요하면 현재 행과 아래 행을 교환한다.
4. 피벗 아래의 원소를 0으로 만든다.
5. 다음 열로 이동하여 같은 작업을 반복한다.
6. 상삼각 연립방정식이 만들어지면 후진 대입한다.

전진 소거가 끝난 계수행렬은 다음 형태이다.

$$
\boldsymbol U=
\begin{bmatrix}
u_{11}&u_{12}&u_{13}\\
0&u_{22}&u_{23}\\
0&0&u_{33}
\end{bmatrix}
$$

# 3. 손으로 계산하는 예제

다음 연립방정식을 풀어보자.

$$
\begin{aligned}
x+y+z&=6,\\
2x+3y+z&=11,\\
-x+2y+3z&=12.
\end{aligned}
$$

이 연립방정식의 해는 아래에 이어 계산하여 확인한다.

## 3.1. 확대행렬 만들기

$$
\left[
\begin{array}{ccc|c}
1&1&1&6\\
2&3&1&11\\
-1&2&3&12
\end{array}
\right]
$$

## 3.2. 첫 번째 열 소거

첫 번째 피벗은 $a_{11}=1$이다. 두 번째 행에서 첫 번째 원소를 없애기 위한 소거
계수는

$$
m_{21}=\frac{a_{21}}{a_{11}}=\frac{2}{1}=\textcolor{red}{2}
$$

이다. 따라서

$$
R_2\leftarrow R_2-\textcolor{red}{2}R_1
$$

을 수행한다. 세 번째 행의 소거 계수는

$$
m_{31}=\frac{a_{31}}{a_{11}}=\frac{-1}{1}=\textcolor{blue}{-1}
$$

이므로

$$
R_3\leftarrow R_3-\textcolor{blue}{(-1)}R_1=R_3+R_1
$$

을 수행한다. 결과는

$$
\left[
\begin{array}{ccc|c}
1&1&1&6\\
0&1&-1&-1\\
0&3&4&18
\end{array}
\right]
$$

이다.

## 3.3. 두 번째 열 소거

두 번째 피벗은 $a_{22}=1$이고 소거 계수는

$$
m_{32}=\frac{a_{32}}{a_{22}}=\frac{3}{1}=\textcolor{green}{3}
$$

이다. 따라서

$$
R_3\leftarrow R_3-\textcolor{green}{3}R_2
$$

를 수행하면

$$
\left[
\begin{array}{ccc|c}
1&1&1&6\\
0&1&-1&-1\\
0&0&7&21
\end{array}
\right]
$$

이 된다.

## 3.4. 후진 대입 (back substitution)

마지막 행부터 미지수를 구한다.

$$
7z=21
\quad\Longrightarrow\quad
z=3
$$

두 번째 행에 $z=3$을 대입하면

$$
y-z=-1
\quad\Longrightarrow\quad
y=2
$$

첫 번째 행에 $y=2$, $z=3$을 대입하면

$$
x+y+z=6
\quad\Longrightarrow\quad
x=1
$$

이다. 따라서 최종 해는

$$
\boxed{(x,y,z)=(1,2,3)}
$$

이다.

일반적인 상삼각 연립방정식의 후진 대입은 다음 식으로 나타낼 수 있다.

$$
x_i=
\frac{
b_i-\displaystyle\sum_{j=i+1}^{n}u_{ij}x_j
}{u_{ii}},
\qquad
i=n,n-1,\ldots,1
$$

# 4. 부분 피벗팅

피벗이 0이면 해당 피벗으로 나눌 수 없다. 다음 연립방정식을 살펴보자.

$$
\begin{aligned}
0x+2y&=4,\\
x+y&=3.
\end{aligned}
$$

첫 번째 피벗은 0이지만 두 행을 교환하면 계산할 수 있다.

$$
\left[
\begin{array}{cc|c}
0&2&4\\
1&1&3
\end{array}
\right]
\quad\xrightarrow{R_1\leftrightarrow R_2}\quad
\left[
\begin{array}{cc|c}
1&1&3\\
0&2&4
\end{array}
\right]
$$

또한 피벗의 절댓값이 매우 작으면 나눗셈 과정에서 반올림 오차가 크게 증폭될 수
있다. **부분 피벗팅(partial pivoting)**은 현재 열에서 피벗 후보와 그 아래 원소 중
절댓값이 가장 큰 원소를 찾아 현재 피벗 행과 교환한다.

열 $k$에서 피벗 행은 다음과 같이 선택한다.

$$
p=k+\mathop{\mathrm{argmax}}_{i=k,\ldots,n-1}|a_{ik}|
$$

부분 피벗팅은 모든 행을 단순히 크기순으로 정렬하는 작업이 아니다. 소거가 한 단계
끝날 때마다 아직 처리하지 않은 부분행렬에서 새 피벗을 선택한다.

# 5. Python 구현

다음 구현은 입력 배열을 복사한 뒤 부분 피벗팅, 전진 소거와 후진 대입을 수행한다.

~~~python
import numpy as np

def gaussian_elimination(A, b, tol=1e-12):
    A = np.asarray(A, dtype=float).copy()
    b = np.asarray(b, dtype=float).copy()

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A는 정사각행렬이어야 합니다.")
    if b.ndim != 1 or len(b) != A.shape[0]:
        raise ValueError("b의 길이는 A의 행 개수와 같아야 합니다.")

    n = len(b)

    # 전진 소거
    for k in range(n-1):
        pivot_row = k+np.argmax(np.abs(A[k:, k]))

        if abs(A[pivot_row, k]) < tol:
            raise np.linalg.LinAlgError("유일한 해가 없습니다.")

        if pivot_row != k:
            # partial pivoting
            A[[k, pivot_row], :] = A[[pivot_row, k], :]
            b[[k, pivot_row]] = b[[pivot_row, k]]

        for i in range(k+1, n):
            multiplier = A[i, k]/A[k, k]
            A[i, k:] = A[i, k:]-multiplier*A[k, k:]
            b[i] = b[i]-multiplier*b[k]

    if abs(A[-1, -1]) < tol:
        raise np.linalg.LinAlgError("유일한 해가 없습니다.")

    # 후진 대입
    x = np.zeros(n)

    for i in range(n-1, -1, -1):
        known_terms = A[i, i+1:]@x[i+1:]
        x[i] = (b[i]-known_terms)/A[i, i]

    return x
~~~

## 5.1. 계산 예제

원래 강의에서 사용한 연립방정식을 풀어보자.

$$
\begin{aligned}
2x+3y+z&=9,\\
x-y+z&=1,\\
3x+11y+5z&=35.
\end{aligned}
$$

~~~python
A = np.array([
    [2.0,  3.0, 1.0],
    [1.0, -1.0, 1.0],
    [3.0, 11.0, 5.0],
])
b = np.array([9.0, 1.0, 35.0])

x = gaussian_elimination(A, b)

print("solution:", x)
print("NumPy:", np.linalg.solve(A, b))
~~~

계산 결과는

$$
(x,y,z)
=
\left(
\frac{1}{3},
\frac{23}{12},
\frac{31}{12}
\right)
\approx
(0.3333,1.9167,2.5833)
$$

이다.

## 5.2. 잔차 확인

계산한 해가 원래 연립방정식을 얼마나 잘 만족하는지 잔차 벡터로 확인한다.

$$
\boldsymbol r=\boldsymbol A \cdot \boldsymbol x-\boldsymbol b
$$

~~~python
residual = A@x-b

print("residual:", residual)
print("residual norm:", np.linalg.norm(residual))
~~~

부동소수점 연산 때문에 잔차가 정확히 0이 아니라 매우 작은 값으로 나타날 수 있다.

# 6. Gauss–Jordan 소거법과의 차이

가우스 소거법은 전진 소거로 상삼각행렬을 만든 뒤 후진 대입한다.

$$
\left[
\begin{array}{ccc|c}
u_{11}&u_{12}&u_{13}&c_1\\
0&u_{22}&u_{23}&c_2\\
0&0&u_{33}&c_3
\end{array}
\right]
$$

Gauss–Jordan 소거법은 피벗 위의 원소까지 모두 0으로 만들고 피벗을 1로 만들어
다음과 같은 기약 행 사다리꼴을 구한다.

$$
\left[
\begin{array}{ccc|c}
1&0&0&x_1\\
0&1&0&x_2\\
0&0&1&x_3
\end{array}
\right]
$$

둘은 관련된 방법이지만 동일한 알고리듬은 아니다. 연립방정식 하나를 푸는 표준
가우스 소거법에서는 모든 비대각 원소를 0으로 만들 필요가 없다.

# 7. 계산량과 주의 사항

- 피벗이 0이면 행 교환이 필요하다.
- 매우 작은 피벗은 반올림 오차를 증폭시킬 수 있으므로 부분 피벗팅을 사용한다.
- 행렬이 특이행렬이면 유일한 해가 없다.
- 입력 배열을 직접 수정하지 않으려면 복사본을 만들어 계산한다.
- 실제 프로그램에서는 검증된 **np.linalg.solve**를 사용하는 것이 좋다.
- 학습 목적으로 가우스 소거법을 직접 구현하면 선형대수 알고리듬의 구조를
  이해하는 데 도움이 된다.

# 8. 정리

- 가우스 소거법은 전진 소거와 후진 대입으로 구성된다.
- 확대행렬의 기본 행 연산은 연립방정식의 해를 바꾸지 않는다.
- 소거 계수는 $m_{ik}=a_{ik}/a_{kk}$로 계산한다.
- 부분 피벗팅은 현재 열에서 절댓값이 가장 큰 피벗을 선택한다.
- 계산 결과는 잔차 $\boldsymbol A \cdot \boldsymbol x-\boldsymbol b$로 확인한다.
- Gauss–Jordan 소거법은 피벗 위까지 소거한다는 점에서 가우스 소거법과 다르다.

# 9. 연습 문제

강의에서 다룬 행 연산과 계산 과정을 확인하는 기초 문제이다.


1. 다음 빈칸을 채워라.

   - 계수행렬과 우변 벡터를 결합한 행렬을 (　　　　　　)이라고 한다.
   - 가우스 소거법은 (　　　　　　)와 후진 대입의 두 단계로 이루어진다.
   - 현재 계산에서 기준으로 사용하는 대각 원소를 (　　　　　　)이라고 한다.

   <!--
   풀이 및 정답:
   확대행렬, 전진 소거, 피벗이다.
   -->

2. 다음 연립방정식의 확대행렬을 작성하라.

   $$
   \begin{aligned}
   2x+y&=5,\\
   x-y&=-1.
   \end{aligned}
   $$

   <!--
   풀이 및 정답:
   확대행렬은 [[2,1|5],[1,-1|-1]]이다.
   -->

3. 다음 중 기본 행 연산으로 사용할 수 있는 것을 모두 고르라.

   1. 두 행을 교환한다.
   2. 한 행에 0을 곱한다.
   3. 한 행에 0이 아닌 상수를 곱한다.
   4. 한 행에 다른 행의 배수를 더한다.

   <!--
   풀이 및 정답:
   1번, 3번, 4번이다. 한 행에 0을 곱하면 원래 방정식의 정보를 잃으므로
   사용할 수 없다.
   -->

4. 첫 번째 피벗이 2이고 그 아래에서 없애려는 원소가 6일 때 소거 계수
   $m_{21}$을 구하라.

   <!--
   풀이 및 정답:
   m_21=6/2=3이다. 따라서 R_2를 R_2-3R_1로 바꾸면 첫 번째 열의 6이 0이 된다.
   -->

5. 다음 확대행렬에 $R_2\leftarrow R_2-2R_1$을 수행하라.

   $$
   \left[
   \begin{array}{cc|c}
   1&1&3\\
   2&3&8
   \end{array}
   \right]
   $$

   <!--
   풀이 및 정답:
   두 번째 행은 [2,3,8]-2[1,1,3]=[0,1,2]가 된다.
   결과는 [[1,1|3],[0,1|2]]이다.
   -->

6. 다음 상삼각 연립방정식을 후진 대입으로 풀어라.

   $$
   \begin{aligned}
   x+2y&=5,\\
   3y&=6.
   \end{aligned}
   $$

   <!--
   풀이 및 정답:
   두 번째 식에서 y=2이다. 첫 번째 식에 대입하면 x+4=5이므로 x=1이다.
   -->

7. 다음 확대행렬에서 첫 번째 단계의 부분 피벗팅을 수행하면 어느 두 행을
   교환해야 하는가?

   $$
   \left[
   \begin{array}{cc|c}
   0.1&1&2\\
   2&3&4
   \end{array}
   \right]
   $$

   <!--
   풀이 및 정답:
   첫 번째 열에서 절댓값이 가장 큰 원소는 두 번째 행의 2이다.
   따라서 R_1과 R_2를 교환한다.
   -->

8. 다음 코드의 빈칸을 채워 해를 계산하라.

   ~~~python
   A = np.array([[1.0, 1.0],
                 [2.0, 3.0]])
   b = np.array([3.0, 8.0])

   x = gaussian_elimination(____, ____)
   print(x)
   ~~~

   <!--
   풀이 및 정답:
   빈칸은 A와 b이다. 연립방정식은 x+y=3, 2x+3y=8이고 해는 x=1, y=2이다.
   -->

9. 계산된 해 $\boldsymbol x=(1,2)$와 다음 행렬 및 벡터에 대해 잔차를 구하라.

   $$
   \boldsymbol A=
   \begin{bmatrix}
   1&1\\
   2&3
   \end{bmatrix},
   \qquad
   \boldsymbol b=
   \begin{bmatrix}
   3\\8
   \end{bmatrix}.
   $$

   <!--
   풀이 및 정답:
   Ax=[3,8]^T=b이므로 잔차 r=Ax-b=[0,0]^T이다.
   -->

10. 가우스 소거법과 Gauss–Jordan 소거법의 차이를 한 문장으로 설명하라.

    <!--
    풀이 및 정답:
    가우스 소거법은 피벗 아래를 소거한 뒤 후진 대입하고, Gauss–Jordan
    소거법은 피벗의 위와 아래를 모두 소거하여 기약 행 사다리꼴을 만든다.
    -->
