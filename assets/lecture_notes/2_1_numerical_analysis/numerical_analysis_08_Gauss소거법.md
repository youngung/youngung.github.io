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

- [1. 가우스 소거법](#1-가우스-소거법)
- [2. 가우스 소거법 worked example](#2-가우스-소거법-worked-example)
  - [2.1. 1단계](#21-1단계)
  - [2.2. 1단계 파이썬](#22-1단계-파이썬)
  - [2.3. 행 위치 교환 (row swap - optional)](#23-행-위치-교환-row-swap---optional)
  - [2.4. 지금까지 한 내용을 Python 코드로 옮기면](#24-지금까지-한-내용을-python-코드로-옮기면)
  - [2.5. 전진 소거 (forward elimination)](#25-전진-소거-forward-elimination)
  - [2.6. Python으로 정리하면 아래와 같다.](#26-python으로-정리하면-아래와-같다)
  - [2.7. 다시 행교환 (swap)](#27-다시-행교환-swap)
  - [2.8. 다시 전진소거 (forward elimination)](#28-다시-전진소거-forward-elimination)
  - [2.9. 앞선 결과 Python 정리하면](#29-앞선-결과-python-정리하면)
  - [2.10. Swap/Forward 축약](#210-swapforward-축약)
  - [2.11. Diagonalization](#211-diagonalization)
- [3. 전체 코드](#3-전체-코드)
- [4. take home](#4-take-home)
- [5. 덧붙이는 말](#5-덧붙이는-말)



# 1. 가우스 소거법
-  확장행렬(augmented matrix) 만들기
-  두행 (가로줄)의 교환
-  한 행에 0이 아닌 상수를 곱함 (scaling)
-  한행에 다른 행의 배수를 더함 (row addition)
-  앞선 2-4단계를 반복하며 삼각형 모양의 행렬을 만듦
-  Diagnolization
-  삼각형 행렬이 다 만들어지면 아래에서부터 거꾸로 대입 (back-substitution)


#  2. 가우스 소거법 worked example

## 2.1. 1단계

- 예를 들어 아래 행렬식을 푼다면

$$
\begin{bmatrix}
2& 3 & 1 \\
1& -1 & 1\\
3& 11 & 5
\end{bmatrix}
\begin{bmatrix}
    x\\
    y\\
    z\\
13. \end{bmatrix}
=
\begin{bmatrix}
9\\
1\\
35\\
\end{bmatrix}
$$

- 우선 좌변의 3x3행렬과 우변의 3x1'벡터'를 결합한 3x4 확장 행렬을 만듭니다.

$$
\left[
\begin{array}{ccc|c}
  2& 3 & 1 & 9\\
  1& -1 & 1 & 1\\
  3& 11 & 5 & 35
\end{array}
\right]
\begin{array}{c}
  \text{1st row}\\
  \text{2nd row}\\
  \text{3rd row}
\end{array}
\begin{array}{c}
  \text{irow=0}\\
  \text{irow=1}\\
  \text{irow=2}
\end{array}
$$

- 그리고 이를 행렬 $\boldsymbol A$라 부릅시다. 따라서 아래와 같습니다.

$$
\begin{bmatrix}
A_{11} & A_{12} & A_{13} & A_{14} \\
A_{21} & A_{22} & A_{23} & A_{24} \\
A_{31} & A_{32} & A_{33} & A_{34} \\
\end{bmatrix}

=

\left[
\begin{array}{ccc|c}
2& 3 & 1 & 9\\
1& -1 & 1 & 1\\
3& 11 & 5 & 35
\end{array}
\right]
$$

## 2.2. 1단계 파이썬

- 1단계까지 작업 내용을 파이썬으로 구현한다면 아래와 같습니다.

```python
def show(A,fmt='%+7.2f'):
  """
  Function to more neatly print out the matrix.
  """
  print('--')
  for i, As in enumerate(A):
    cr=''
    for j, a in enumerate(As):
      cr=f'{cr} {fmt}'%a
    print(cr)

import numpy as np
A=np.zeros((3,4)) # 3 x 4 (three rows, four columns) (3행, 4열)
A[0,:]=2, 3, 1, 9 #irow=0
A[1,:]=1,-1, 1, 1 #irow=1
A[2,:]=3,11, 5,35 #irow=2
show(A) ## 말끔하게 행렬을 소수 2째자리 까지만 출력해서 봅시다.
```

- 위에서 함수 ```show```는 행렬을 말끔하게 출력하기 위해서 간략히 작성해 봤습니다.


## 2.3. 행 위치 교환 (row swap - optional)

 - 행의 위치를 교환합니다 반드시 필요한 단계는 아니지만, truncation 오차를 줄여줍니다.
 - 첫번째 열(즉 ```A[:,0]```)의 절대값이 높은 순서대로 아래에서부터 위로 채웁니다.
 - 1열 즉

$$
\begin{bmatrix}
    \textcolor{blue}{2} &\textcolor{blue}{...}\\
    \textcolor{red}{1}&\textcolor{red}{...} \\
    \textcolor{green}{3}&\textcolor{green}{...}
\end{bmatrix}
$$

을 따라서, 3번째 행(3rd row)의 1열(1st col.) 값, 즉 $A_{13}$의 절대 값

$$|A_{13}|=\textcolor{green}{3}$$

이며 가장 큰 수입니다. 그 다음이

$$|A_{11}|=\textcolor{blue}{2}, A_{12}=\textcolor{red}{1}$$

순서입니다.

$$
\left[
\begin{array}{ccc|c}
  \textcolor{red}{1}& \textcolor{red}{-1} & \textcolor{red}{1} & \textcolor{red}{1}\\
  \textcolor{blue}{2}& \textcolor{blue}{3} & \textcolor{blue}{1} & \textcolor{blue}{9}\\
  \textcolor{green}{3}& \textcolor{green}{11} & \textcolor{green}{5} & \textcolor{green}{35}
\end{array}
\right]
\begin{array}{c}
\text{2nd row}\rightarrow\text{3rd row}\\
\text{1st row}\rightarrow\text{2nd row}\\
\text{3rd row}\rightarrow\text{1st row}
\end{array}
$$

행렬 옆에 표기된 방법대로 row를 바꾸면

$$
\left[
\begin{array}{ccc|c}
  \textcolor{green}{3}& \textcolor{green}{11} & \textcolor{green}{5} & \textcolor{green}{35} \\
  \textcolor{blue}{2}& \textcolor{blue}{3} & \textcolor{blue}{1} & \textcolor{blue}{9}\\
  \textcolor{red}{1}& \textcolor{red}{-1} & \textcolor{red}{1} & \textcolor{red}{1}
\end{array}
\right]
$$

## 2.4. 지금까지 한 내용을 Python 코드로 옮기면

```python
#------------------------------------------------
import numpy as np
# initial empty A.
A=np.zeros((3,4))
# filling up the matrix.
A[0,:]=2, 3, 1, 9 #1st row, irow=0
A[1,:]=1,-1, 1, 1 #2nd row, irow=1
A[2,:]=3,11, 5,35 #3rd row, irow=2
show(A)

B=A.copy() ## copy to a temp matrix, and named it `B`
A[::]=0.   ## zeroed.
A[0,:] = B[2,:] # 3rd row [3,11,5,35] -> 1st row
A[1,:] = B[0,:] # 1st row [2, 3, 1,9] -> 2nd row
A[2,:] = B[1,:] # 2nd row [1,-1, 1,1] -> 3rd row
show(A)
```

그런데, $A$ 행렬의 순서를 바꾸는 걸 Python에게 시키고 싶다면
[np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html)를 다음과 같이 활용할 수 있겠다.

```python
print(A[:,0]) #1열 - 혹은 A[0:3,0]
# 위 결과는 [2,1,3] 순서가 된다. 그런데 우리는 절대 값의 순서가 필요.
# 따라서 np.abs 을 활용해 절대값을
print(np.abs(A[:,0]))
# 1열을 따라 낮은 값에서 순서대로 인덱스를 저장.
ind = np.argsort(np.abs(A[:,0]))
#
show(A[ind,:])       #낮은->높은 값 순서대로 바뀜.
show(A[ind[::-1],:]) #높은->낮은 값 순서대로... ind[::-1]
```

## 2.5. 전진 소거 (forward elimination)

- 앞서 재 정렬된 행렬은 아래와 같다.

$$
\boldsymbol A=
\left[
\begin{array}{ccc|c}
\textcolor{green}{3}& \textcolor{green}{11} & \textcolor{green}{5} & \textcolor{green}{35} \\
\textcolor{blue}{2}& \textcolor{blue}{3} & \textcolor{blue}{1} & \textcolor{blue}{9}\\
\textcolor{red}{1}& \textcolor{red}{-1} & \textcolor{red}{1} & \textcolor{red}{1}
\end{array}
\right]
$$

- 첫번째 행의 첫번째 렬 값, ```A[0,0]```, 즉 $\textcolor{green}{3}$을 분자로
그리고 $\textcolor{blue}{\text{row2}}$, 첫번째 렬(col1) 값, 즉 $A_{21}$,
```A[1,0]```$=\textcolor{blue}{2}$을 분모로 하는 factor
$\frac{\textcolor{green}{3}}{\textcolor{blue}{2}}$을 두번째 행, ```A[1,:]```에
곱해서 첫번째 행에서 뺀 후, 두번째 행을 대체합니다.


## 2.6. Python으로 정리하면 아래와 같다.

```python
# irow=1
A[1,:]=A[0,:]-(A[0,0]/A[1,0])*A[1,:]
```

- 위 작업을 3번째 행에도 동일하게 수행하면

```python
# irow=2
A[2,:]=A[0,:]-(A[0,0]/A[2,0])*A[2,:]
```

* 그런데 이를 한번에 loop안에 적용할 수 있다. 즉:

```python
#------------------------------------------------
import numpy as np
# initial empty A.
A=np.zeros((3,4))
# filling up the matrix.
A[0,:]=2, 3, 1, 9 #1st row, irow=0
A[1,:]=1,-1, 1, 1 #2nd row, irow=1
A[2,:]=3,11, 5,35 #3rd row, irow=2
show(A)

B=A.copy() ## copy to a temp matrix, and named it `B`
A[::]=0.   ## zeroed.
A[0,:] = B[2,:] # 3rd row [3,11,5,35] -> 1st row
A[1,:] = B[0,:] # 1st row [2, 3, 1,9] -> 2nd row
A[2,:] = B[1,:] # 2nd row [1,-1, 1,1] -> 3rd row
show(A)

for irow in range(1,3):
    A[irow,:]=A[0,:]-(A[0,0]/A[irow,0])*A[irow,:]
show(A)
```

## 2.7. 다시 행교환 (swap)

- 이제 행렬은 아래와 같은 형태가 된다.

$$
\boldsymbol A=
\left[
\begin{array}{ccc|c}
\textcolor{green}{3}& \textcolor{green}{11} & \textcolor{green}{5} & \textcolor{green}{35} \\
\textcolor{blue}{0}& \textcolor{blue}{6.5} & \textcolor{blue}{3.5} & \textcolor{blue}{21.5}\\
\textcolor{red}{0}& \textcolor{red}{14} & \textcolor{red}{2} & \textcolor{red}{32}
\end{array}
\right]
$$

이제 우리의 기준은 $A_{22}$ 즉 ```A[1,1]```입니다. 그런데
$|\textcolor{blue}{6.5}|<|\textcolor{red}{14}|$
이므로 행 교환이 필요하다.

$$
\boldsymbol A=
\left[
\begin{array}{ccc|c}
\textcolor{green}{3}& \textcolor{green}{11} & \textcolor{green}{5} & \textcolor{green}{35} \\
\textcolor{red}{0}& \textcolor{red}{14} & \textcolor{red}{2} & \textcolor{red}{32}         \\
\textcolor{blue}{0}& \textcolor{blue}{6.5} & \textcolor{blue}{3.5} & \textcolor{blue}{21.5}
\end{array}
\right]
$$

```python
# swap
ind = np.argsort(np.abs(A[1:,1]))
A[1:,]=A[1:,][ind[::-1],:]
show(A)
```

## 2.8. 다시 전진소거 (forward elimination)
* 전진 소거의 기준이, 앞서 살펴보았듯 $A_{22}$부터다. 즉,

$$
\textcolor{blue}{A_{3,:}}\leftarrow\textcolor{red}{A_{2,:}}-A_{22}/A_{32}\times \textcolor{blue}{A_{3,:}}
$$

```python
icol=1 # A{:,2}
irow=2 # A{3,:}
A[irow,:]=A[icol,:]-(A[icol,icol]/A[irow,icol])*A[irow,:]
show(A)
```

## 2.9. 앞선 결과 Python 정리하면

- 즉 앞서 이어온 결과와 다 모아 행바꾸기, 전진 소거를 표현하자면 아래와 같다.

```python
#------------------------------------------------
import numpy as np
# initial empty A.
A=np.zeros((3,4))
# filling up the matrix.
A[0,:]=2, 3, 1, 9 #1st row, irow=0
A[1,:]=1,-1, 1, 1 #2nd row, irow=1
A[2,:]=3,11, 5,35 #3rd row, irow=2
show(A)

# swap
icol=0
ind = np.argsort(np.abs(A[icol:,icol]))
A=A[ind[::-1],:]
show(A)
# forward
for irow in range(icol+1,A.shape[0]):
 A[irow,:]=A[icol,:]-(A[icol,icol]/A[irow,icol])*A[irow,:]
show(A)

# swap
icol=1
ind = np.argsort(np.abs(A[icol:,icol]))
A[icol:,]=A[icol:,][ind[::-1],:]
show(A)
# forward
for irow in range(icol+1,A.shape[0]):
 A[irow,:]=A[icol,:]-(A[icol,icol]/A[irow,icol])*A[irow,:]
show(A)
```

## 2.10. Swap/Forward 축약

- 여기서, row swap과 forward elimination이 icol=0,1로 바뀌며 동일한 코드가 반복되는 걸 알 수 있다.

- Swap/Forward 축약 표기
- 앞 단계의 결과를 행렬의 크기와 swap/forward의 대상 행과 열을 고려하여
더욱 축약하자면 아래와 같이 표현된다.

```python
A=np.zeros((3,4))
# filling up the matrix.
A[0,:]=2,3,1,9
A[1,:]=1,-1,1,1
A[2,:]=3,11,5,35

for icol in range(0,A.shape[0]-1):
    ## swap
    a=np.abs(A[icol:,icol]) ## Based on [absolute values] of a portion of column
    ind=np.argsort(a)
    ind=ind[::-1] # reverse order
    A[icol:,:]=A[icol:,:][ind,:]
    show(A)
    ## forward
    for irow in range(icol+1,A.shape[0]):
        A[irow,:]=A[irow,:]-A[irow,icol]/A[icol,icol]*A[icol,:]
    show(A)
    print('****************')
```

- 그 결과는 아래와 같다

$$
\left[
\begin{array}{ccc|c}
+3.00&  +11.00&   +5.00&  +35.00 \\
+0.00&   -4.67&   -0.67&  -10.67 \\
+0.00&   +0.00&   -1.71&   -4.43
\end{array}
\right]
$$

## 2.11. Diagonalization
- 앞선 단계의 결과를 더욱 진행하여 대각선 값들을 제외하고 `0`을 만들 수 있다.
아래 코드를 참고하자.

```python
# now one could 'diagonalize'
for icol in range(A.shape[0]-1,0,-1):
    for irow in range(0,icol):
        f=A[irow,icol]/A[icol,icol]
        A[irow,:]=A[irow,:]-f*A[icol,:]
```

그 결과는 아래와 같다.

$$
\left[
\begin{array}{ccc|c}
+3.00&  -0.00&   +0.00&   +1.00 \\
+0.00&  -4.67&   +0.00&   -8.94 \\
+0.00&  +0.00&   -1.71&   -4.43
\end{array}
\right]
$$

정리하자면, 현재 연립 방정식은 아래와 같은 형태가 된 것이다.

$$
\left[
\begin{array}{c}
+3.00x=+1.00 \\
-4.67y=-8.94 \\
-1.71z=-4.43
\end{array}
\right]
$$

각 식을 풀기 위해서는 행렬의 대각선 값들을 각 행에 각가 나눠주면 되겠다.
즉 아래와 같은 수행을 하고 나면

```python
for icol in range(A.shape[0]):
  A[icol,:]=A[icol,:]/A[icol,icol]
```

$$
  \left[
  \begin{array}{ccc|c}
  +1.00&  -0.00&   +0.00&  +0.33 \\
  -0.00&  +1.00&   -0.00&  +1.92 \\
  -0.00&  -0.00&   +1.00&  +2.58
  \end{array}
  \right]
$$

가 되어 $(x,y,z)=(0.33,1.92,2.58)$ 해를 찾게 되었다.

# 3. 전체 코드
- 모든 단계에 이르는 전체 코드를 살펴보자.

```python
def show(A,fmt='%+7.2f'):
  """
  Function to more neatly print out the matrix.
  """
  print('--')
  for i, As in enumerate(A):
    cr=''
    for j, a in enumerate(As):
      cr=f'{cr} {fmt}'%a
    print(cr)

import numpy as np
# initial empty A.
A=np.zeros((3,4))
# filling up the matrix.
A[0,:]=2,3,1,9
A[1,:]=1,-1,1,1
A[2,:]=3,11,5,35
#show(A)

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

show(A)

# now one could 'diagonalize'
for icol in range(A.shape[0]-1,0,-1):
  for irow in range(0,icol):
    f=A[irow,icol]/A[icol,icol]
    A[irow,:]=A[irow,:]-f*A[icol,:]
show(A)
for icol in range(A.shape[0]):
  A[icol,:]=A[icol,:]/A[icol,icol]
show(A)
```

# 4. take home
- 위에서 만든 Gauss 소거법 코드를 활용해 아래를 풀어보자.

$$
\left[
\begin{array}{cccc|c}
+2  & +3 & +1  & +9  & -1 \\
-1  & -1 & -1 &  +1 & +10 \\
+3  & +3 & -5  & +35 &  +0 \\
+3  & +4 & +10 &  +3 &  -3
\end{array}
\right]
$$

# 5. 덧붙이는 말

- 중간에 row의 순서를 바꾸는 과정이 없는 알고리듬으로 구현한 웹 프로그램을
[여기](https://onlinemschool.com/math/assistance/equation/gaus/)에서
찾을 수 있다.

- Numpy의 선형대수(Linear Algebra) 패키지 ([np.linalg](https://numpy.org/doc/2.2/reference/routines.linalg.html)) 활용

```python
import numpy
A=np.zeros((3,4))
# filling up the matrix.
A[0,:]=2,3,1,9
A[1,:]=1,-1,1,1
A[2,:]=3,11,5,35
n=A.shape[0]

## determinant 를 구한다.
print('det:',np.linalg.det(A[:,:n]))
# Inverse matrix 구한 다음 곱하기.
root=np.linalg.inv(A[:,:n])@A[:,n]
print(root)

# 혹은 solve를 활용해서
print(np.linalg.solve(A[:,:n], A[:,n]))
```