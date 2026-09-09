---
layout: distill
title: 고유값과 고유벡터
description: 선형변환의 고유값과 고유벡터를 이해하고 NumPy로 계산하기
target: 1학년 2학기
permalink:
featured: true
prerequisite: 행렬 연산 기초, 함수 기초
toc:
  sidebar: left
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

- [1. 학습 목표](#1-학습-목표)
- [2. 고유값과 고유벡터의 의미](#2-고유값과-고유벡터의-의미)
- [3. 고유값의 기하학적 의미](#3-고유값의-기하학적-의미)
- [4. 특성방정식으로 고유값 구하기](#4-특성방정식으로-고유값-구하기)
- [5. NumPy로 고유값과 고유벡터 구하기](#5-numpy로-고유값과-고유벡터-구하기)
- [6. 재료공학 예제: 변위구배텐서](#6-재료공학-예제-변위구배텐서)
- [7. 고유값을 활용한 반복 변환](#7-고유값을-활용한-반복-변환)
- [8. 자주 만나는 오류](#8-자주-만나는-오류)
- [9. 쉬운 연습 문제](#9-쉬운-연습-문제)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 고유값과 고유벡터의 의미를 설명할 수 있다.
- 고유값 문제를 행렬식과 특성방정식으로 표현할 수 있다.
- `np.linalg.eig()`를 사용하여 고유값과 고유벡터를 계산할 수 있다.
- 고유벡터의 방향과 고유값의 크기 변화를 해석할 수 있다.
- 고유값 계산 결과가 물리적 문제에서 어떤 의미를 갖는지 설명할 수 있다.

# 2. 고유값과 고유벡터의 의미

행렬 $\boldsymbol A$를 벡터 $\boldsymbol v$에 곱하면 일반적으로 벡터의 방향과 크기가 모두 바뀐다. 그러나 특별한 방향의 벡터는 행렬을 곱한 뒤에도 방향이 변하지 않고 크기만 변한다.

$$
\boldsymbol A\boldsymbol v = \lambda \boldsymbol v
$$

이 식을 만족하는 0이 아닌 벡터 $\boldsymbol v$를 **고유벡터(eigenvector)**라고 하고, 그때의 스칼라 $\lambda$를 **고유값(eigenvalue)**이라고 한다.

- 고유벡터: 선형변환 후에도 방향이 유지되는 벡터
- 고유값: 해당 고유벡터가 얼마나 확대 또는 축소되는지를 나타내는 값

고유값의 부호에 따라 다음과 같이 해석할 수 있다.

- $|\lambda|>1$: 크기가 커짐
- $|\lambda|<1$: 크기가 작아짐
- $\lambda<0$: 방향이 반대쪽으로 뒤집힘
- $\lambda=1$: 크기와 방향이 그대로 유지됨

고유벡터는 길이가 1로 정규화되어 있거나 반대 방향으로 표시될 수 있다. 같은 고유벡터라도 상수배한 벡터는 같은 방향을 나타낸다.

# 3. 고유값의 기하학적 의미

다음 행렬을 생각해 보자.

$$
\boldsymbol A=
\begin{bmatrix}
2&0\\
0&1
\end{bmatrix}
$$

이 행렬은 $x$ 방향을 2배로 늘리고 $y$ 방향은 그대로 둔다.

$$
\boldsymbol A
\begin{bmatrix}1\\0\end{bmatrix}
=2\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\boldsymbol A
\begin{bmatrix}0\\1\end{bmatrix}
=1\begin{bmatrix}0\\1\end{bmatrix}
$$

따라서 다음과 같다.

- $\begin{bmatrix}1\\0\end{bmatrix}$ 방향의 고유값은 $2$
- $\begin{bmatrix}0\\1\end{bmatrix}$ 방향의 고유값은 $1$

행렬이 회전을 포함하면 실수 고유벡터가 존재하지 않을 수도 있다. 예를 들어 순수한 90도 회전은 어떤 실수 벡터의 방향도 그대로 유지하지 않으므로 실수 범위의 고유벡터를 갖지 않는다. 이 경우 NumPy는 복소수 고유값을 반환할 수 있다.

# 4. 특성방정식으로 고유값 구하기

고유값 방정식에서 오른쪽 항을 왼쪽으로 옮기면

$$
(\boldsymbol A-\lambda\boldsymbol I)\boldsymbol v=\boldsymbol 0
$$

이 된다. 0이 아닌 고유벡터가 존재하려면 행렬 $\boldsymbol A-\lambda\boldsymbol I$가 역행렬을 가지지 않아야 한다. 따라서

$$
\det(\boldsymbol A-\lambda\boldsymbol I)=0
$$

을 만족해야 한다. 이 식을 **특성방정식(characteristic equation)**이라고 한다.

2×2 행렬

$$
\boldsymbol A=\begin{bmatrix}a&b\\c&d\end{bmatrix}
$$

의 특성방정식은

$$
\lambda^2-(a+d)\lambda+(ad-bc)=0
$$

이다. 여기서 $a+d$는 행렬의 trace이고, $ad-bc$는 determinant이다.

```python
import numpy as np

A = np.array([
    [3.0, 2.0],
    [2.0, 1.0],
])

trace = np.trace(A)
determinant = np.linalg.det(A)
roots = np.roots([1.0, -trace, determinant])

print(roots)
```

# 5. NumPy로 고유값과 고유벡터 구하기

NumPy에서는 `np.linalg.eig()`를 사용한다.

```python
import numpy as np

A = np.array([
    [3.0, 2.0],
    [2.0, 1.0],
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("eigenvalues:")
print(eigenvalues)
print("eigenvectors:")
print(eigenvectors)
```

반환된 `eigenvalues[i]`에 대응하는 고유벡터는 `eigenvectors[:, i]`이다.

```python
for index, value in enumerate(eigenvalues):
    vector = eigenvectors[:, index]
    print(f"lambda = {value}")
    print(f"v = {vector}")
    print("check:", A @ vector, value * vector)
```

수치 계산에서는 아주 작은 반올림 오차가 생길 수 있다. 두 결과가 같은지 확인할 때는 `==`보다 `np.allclose()`를 사용하는 것이 좋다.

```python
for index, value in enumerate(eigenvalues):
    vector = eigenvectors[:, index]
    assert np.allclose(A @ vector, value * vector)
```

고유값만 필요하다면 `np.linalg.eigvals()`를 사용할 수 있다.

```python
eigenvalues_only = np.linalg.eigvals(A)
print(eigenvalues_only)
```

고유값과 고유벡터의 순서는 특별히 보장되지 않는다. 따라서 첫 번째 결과가 항상 가장 큰 고유값이라고 가정하면 안 된다.

# 6. 재료공학 예제: 변위구배텐서

변위구배텐서 또는 선형변환 행렬을 $\boldsymbol F$라고 하자. 변환 전 벡터와 변환 후 벡터의 관계는 다음과 같이 쓸 수 있다.

$$
\boldsymbol v^{\mathrm{new}}=\boldsymbol F\boldsymbol v^{\mathrm{old}}
$$

고유벡터 방향에서는 방향이 바뀌지 않고 고유값만큼 크기가 변한다.

```python
import numpy as np

F = np.array([
    [1.10, 0.05],
    [0.05, 0.95],
])

eigenvalues, eigenvectors = np.linalg.eig(F)

for index, stretch in enumerate(eigenvalues):
    direction = eigenvectors[:, index]
    print(f"direction = {direction}")
    print(f"stretch = {stretch}")
```

회전이 거의 없고 고유값이 변형을 나타내는 변환이라면, $\lambda-1$을 고유벡터 방향의 변형 정도로 해석할 수 있다. 이는 문제의 변환 정의와 변형률의 종류에 따라 달라지므로, 항상 고유값을 곧바로 변형률이라고 부르지는 않아야 한다.

# 7. 고유값을 활용한 반복 변환

행렬을 반복해서 곱하는 문제에서도 고유값이 중요한 역할을 한다.

$$
\boldsymbol x_{n+1}=\boldsymbol A\boldsymbol x_n
$$

예를 들어 두 집단의 인구 변화를 행렬로 표현할 수 있다.

```python
import numpy as np

transition = np.array([
    [0.80, 0.10],
    [0.20, 0.90],
])

population = np.array([8.0, 2.0])

for year in range(5):
    print(year, population)
    population = transition @ population
```

반복 변환에서 크기가 빠르게 커지거나 작아지는 방향은 고유값의 절댓값과 관련이 있다. 충분히 반복한 뒤의 거동을 이해하려면 가장 큰 절댓값을 가진 고유값과 그에 대응하는 고유벡터를 살펴볼 수 있다.

# 8. 자주 만나는 오류

## 8.1. 정방행렬이 아닌 경우

`np.linalg.eig()`는 정방행렬을 대상으로 한다. 행과 열의 개수가 다르면 고유값 문제를 정의할 수 없으므로 오류가 발생한다.

## 8.2. 복소수 결과

회전처럼 실수 고유벡터가 존재하지 않는 변환에서는 복소수 고유값이나 고유벡터가 나올 수 있다. 복소수 결과를 임의로 실수부만 취하지 말고, 문제의 물리적 의미를 먼저 확인해야 한다.

## 8.3. 수치 오차

계산 결과가 이론값과 아주 조금 다를 수 있다. 이런 경우 `np.allclose()`로 허용 오차를 고려하여 비교한다.

# 9. 쉬운 연습 문제

## 문제 1

고유값과 고유벡터를 정의하는 식을 쓰시오.

<!--
풀이와 해답:
A v = lambda v
-->

## 문제 2

다음 행렬을 x 방향 단위벡터에 곱했을 때의 결과를 구하고, x 방향이 고유벡터 방향인지 판단하시오.

$$
A=\begin{bmatrix}2&0\\0&3\end{bmatrix},
\qquad
v=\begin{bmatrix}1\\0\end{bmatrix}
$$

<!--
풀이와 해답:
Av = [2, 0]^T = 2v 이므로 x 방향은 고유벡터 방향이고 고유값은 2이다.
-->

## 문제 3

NumPy에서 행렬의 고유값과 고유벡터를 계산하는 함수를 쓰시오.

<!--
풀이와 해답:
np.linalg.eig()
-->

## 문제 4

다음 코드에서 `eigenvectors[:, index]`가 의미하는 것을 설명하시오.

```python
eigenvalues, eigenvectors = np.linalg.eig(A)
vector = eigenvectors[:, index]
```

<!--
풀이와 해답:
index번째 고유값에 대응하는 고유벡터를 뜻한다.
-->
