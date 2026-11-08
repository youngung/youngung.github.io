---
layout: distill
title: 행렬 연산 기초
description: NumPy를 이용한 행렬–벡터곱과 행렬곱
target: 1학년 2학기
permalink:
featured: true
prerequisite: NumPy 배열 활용, 벡터 연산 기초
toc: false
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

**목차**

* TOC
{:toc}

# 1. 학습 목표

이 자료에서 $[\boldsymbol A]$, $[\boldsymbol x]$는 행렬·벡터의 성분을 모은 배열을 뜻한다.
수식에서는 행렬곱을 $[\boldsymbol A][\boldsymbol x]$처럼 붙여 쓰고, Python 코드에서는 <code>A @ x</code>로 쓴다.


이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 행렬을 2차원 NumPy 배열로 나타낼 수 있다.
- 원소별 곱과 행렬곱을 구분할 수 있다.
- 행렬–벡터곱과 행렬곱을 손으로 계산하고 NumPy로 확인할 수 있다.
- 행렬곱이 가능한 shape 조건을 판단할 수 있다.
- 단위행렬, 전치행렬, 행렬식과 역행렬의 의미를 설명할 수 있다.
- <code>np.linalg.solve()</code>로 간단한 연립방정식을 풀 수 있다.

11장에서는 두 벡터의 내적으로 스칼라를 구했다. 이번 장에서는 행렬의 각 행과
벡터의 내적을 모아 새로운 벡터를 만들고, 이를 행렬곱과 선형변환으로 확장한다.
인덱스를 이용한 합산 규칙과 <code>np.einsum</code>은 다음 13장에서 다룬다.

# 2. 행렬과 NumPy 배열

$m$행 $n$열의 행렬은 $m\times n$ 행렬이라고 한다.

$$
[\boldsymbol A]=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
$$

은 2행 3열 행렬이다.

~~~python
import numpy as np
A = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
])

print(A)
print(A.shape)
print(A.ndim)
~~~

<code>A.shape</code>은 <code>(2, 3)</code>이고 <code>A.ndim</code>은 2이다.
이 장의 수식에서는 첨자를 1부터, Python에서는 인덱스를 0부터 센다.
따라서 수식의 $A_{ij}$는 코드의 <code>A[i-1, j-1]</code>에 대응한다.
예를 들어 수식의 $A_{12}$는 코드의 <code>A[0, 1]</code>이다.

~~~python
print(A[0, 0])
print(A[1, 2])
~~~

# 3. 행렬의 합과 원소별 곱

shape이 같은 두 행렬의 합과 차는 같은 위치의 성분끼리 계산한다.

~~~python
A = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
])
B = np.array([
    [5.0, 6.0],
    [7.0, 8.0],
])

print(A + B)
print(A - B)
~~~

별표 연산자 <code>*</code>는 행렬곱이 아니라 원소별 곱을 계산한다.

~~~python
elementwise_product = A * B
print(elementwise_product)
~~~

결과는

$$
\begin{bmatrix}
5&12\\
21&32
\end{bmatrix}
$$

이다.

# 4. 행렬–벡터곱

행렬

$$
[\boldsymbol A]=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix}
$$

와 벡터

$$
[\boldsymbol x]=
\begin{bmatrix}
5\\6
\end{bmatrix}
$$

의 곱은 각 행과 벡터의 내적으로 계산한다.

$$
[\boldsymbol A][\boldsymbol x]
=
\begin{bmatrix}
1\times5+2\times6\\
3\times5+4\times6
\end{bmatrix}
=
\begin{bmatrix}
17\\39
\end{bmatrix}
$$

~~~python
A = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
])
x = np.array([5.0, 6.0])

result = A @ x

print(result)
print(result.shape)
~~~

$$(m,n)$$ 행렬과 shape이 $$(n,)$$인 벡터를 곱하면 shape이 $$(m,)$$인 벡터가 나온다.

## 4.1. 행렬–벡터곱은 열벡터의 선형결합이다

앞에서는 각 행과 벡터의 내적으로 계산했다. 같은 계산을 **각 열에 가중치를 곱해 더하는 과정**으로 읽을 수도 있다.

$$
\begin{bmatrix}1&2\\3&4\end{bmatrix}
\begin{bmatrix}5\\6\end{bmatrix}
=5\begin{bmatrix}1\\3\end{bmatrix}
+6\begin{bmatrix}2\\4\end{bmatrix}
=\begin{bmatrix}17\\39\end{bmatrix}.
$$

벡터의 첫 성분 5는 첫 열의 가중치이고, 두 번째 성분 6은 두 번째 열의 가중치다.
이처럼 벡터에 수를 곱한 뒤 더하는 것을 **[선형결합(linear combination)](https://en.wikipedia.org/wiki/Linear_combination)**이라고 한다.
행렬의 열을 서로 다른 격자벡터로 정하면, 행렬–벡터곱은 격자벡터의 조합으로 실제 위치를 만드는 연산이 된다.

~~~python
A = np.array([[1.0, 2.0], [3.0, 4.0]])
x = np.array([5.0, 6.0])
by_columns = x[0] * A[:, 0] + x[1] * A[:, 1]
print(np.allclose(A @ x, by_columns))  # True
~~~

## 4.2. 행렬을 선형변환으로 읽기

행렬로 나타낸 [선형변환(linear transformation)](https://en.wikipedia.org/wiki/Linear_map)을 이용해
평면의 점을 $$[\boldsymbol y]=[\boldsymbol A][\boldsymbol x]$$로 옮긴다고 생각하자.
첫 번째 단위벡터 $$(1,0)^T$$는 행렬의 첫 열로, 두 번째 단위벡터 $$(0,1)^T$$는 둘째 열로 옮겨진다.
따라서 두 열을 보면 기본 방향이 어디로 가는지 알 수 있다.

예를 들어

$$
[\boldsymbol S]=\begin{bmatrix}2&0\\0&1\end{bmatrix},
\qquad
[\boldsymbol Q]=\begin{bmatrix}0&-1\\1&0\end{bmatrix}
$$

에서 $$[\boldsymbol S]$$는 첫 번째 방향을 2배 늘리고,
$$[\boldsymbol Q]$$는 **고정된 좌표계 안에서 벡터를 반시계방향으로 90° 회전**시킨다.
여기서는 좌표축을 고정한 채 벡터의 크기나 방향을 바꾼다.
벡터는 그대로 두고 좌표축을 바꾸어 성분을 다시 표현하는 경우와 구분하자.

$$
[\boldsymbol x]=\begin{bmatrix}1\\1\end{bmatrix}
\quad\Rightarrow\quad
[\boldsymbol S][\boldsymbol x]=\begin{bmatrix}2\\1\end{bmatrix},
\qquad
[\boldsymbol Q][\boldsymbol x]=\begin{bmatrix}-1\\1\end{bmatrix}.
$$

# 5. 행렬곱

두 행렬

$$
[\boldsymbol A]=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix},
\qquad
[\boldsymbol B]=
\begin{bmatrix}
2&0\\
1&3
\end{bmatrix}
$$

의 곱을 생각하자. 결과의 각 성분은 $$A$$의 한 행과 $$B$$의 한 열의 내적이다.

$$
\begin{aligned}
C_{11}&=1\times2+2\times1=4,\\
C_{12}&=1\times0+2\times3=6,\\
C_{21}&=3\times2+4\times1=10,\\
C_{22}&=3\times0+4\times3=12.
\end{aligned}
$$

따라서

$$
[\boldsymbol C]
=
[\boldsymbol A][\boldsymbol B]
=
\begin{bmatrix}
4&6\\
10&12
\end{bmatrix}
$$

이다.

~~~python
A = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
])
B = np.array([
    [2.0, 0.0],
    [1.0, 3.0],
])

C = A @ B

print(C)
~~~

일반적으로 $$A$$가 $$(l,m)$$ 행렬이고 $$B$$가 $$(m,n)$$ 행렬이면

$$
C_{ij}
=
\sum_{k=1}^{m}A_{ik}B_{kj}
$$

이고 결과 $$C$$는 $$l$$행 $$n$$열, 즉 shape이 $$(l,n)$$인 행렬이다.

$$
C_{ij}
=
\sum_{k=1}^{m}A_{ik}B_{kj}

\text{ with } i=1,2,..., l \ \ j=1,2,...,n
$$


학습을 위해 반복문으로 같은 계산을 구현하면 다음과 같다.

~~~python
rows_a, columns_a = A.shape
rows_b, columns_b = B.shape

C_loop = np.zeros((rows_a, columns_b))

for i in range(rows_a):
    for j in range(columns_b):
        for k in range(columns_a):
            C_loop[i, j] += A[i, k] * B[k, j]

print(C_loop)
print(np.allclose(C, C_loop))
~~~

실제 계산에서는 보통 최적화된 행렬곱 <code>A @ B</code>를 사용한다.
<code>np.allclose()</code>는 작은 부동소수점 오차를 허용하여 두 결과가 같은지 확인한다.

# 6. 행렬곱의 shape

행렬곱에서는 앞 행렬의 **열 개수**와 뒤 행렬의 **행 개수**가 같아야 한다.
shape을 나란히 적었을 때 안쪽의 두 수가 같아야 한다는 뜻이다.

$$
(l,m)(m,n)\rightarrow(l,n)
$$

예를 들어 다음 곱은 가능하다.

~~~python
A = np.ones((2, 3))
B = np.ones((3, 4))

C = A @ B

print(C.shape)
~~~

$$(2,3)(3,4)$$의 안쪽 크기 3이 같고 결과 shape은 $$(2,4)$$이다.

다음 곱은 안쪽 크기가 다르므로 계산할 수 없다.

~~~text
(2, 3) @ (2, 4)
~~~

행렬곱은 일반적으로 순서를 바꿀 수 없다.

$$
[\boldsymbol A][\boldsymbol B]
\ne
[\boldsymbol B][\boldsymbol A]
$$

shape에 따라 한쪽 순서의 곱만 가능한 경우도 있다.

## 6.1. 변환의 순서는 오른쪽부터 읽는다

$$[\boldsymbol Q][\boldsymbol S][\boldsymbol x]$$는 먼저 늘린 뒤 회전시킨다.
반대로 $$[\boldsymbol S][\boldsymbol Q][\boldsymbol x]$$는 회전한 뒤 늘린다.
4.2절의 행렬과 벡터를 사용하면

$$
[\boldsymbol Q][\boldsymbol S][\boldsymbol x]=\begin{bmatrix}-1\\2\end{bmatrix},
\qquad
[\boldsymbol S][\boldsymbol Q][\boldsymbol x]=\begin{bmatrix}-2\\1\end{bmatrix}
$$

이다. **shape이 맞아도 순서를 바꾸면 결과가 달라질 수 있다.**

## 6.2. 1차원 배열과 행·열 배열의 곱

<code>x = np.array([1.0, 2.0])</code>라고 하자.

| 표현 | 결과 shape | 의미 |
|---|---|---|
| <code>x.T</code> | <code>(2,)</code> | 1차원 배열의 형태는 유지된다. |
| <code>x[:, None]</code> | <code>(2, 1)</code> | 열 배열을 만든다. |
| <code>x[None, :]</code> | <code>(1, 2)</code> | 행 배열을 만든다. |
| <code>x @ x</code> | <code>()</code> | 내적, 값은 5다. |
| <code>x[:, None] @ x[None, :]</code> | <code>(2, 2)</code> | 성분곱 $$x_i x_j$$로 이루어진 행렬이다. |
| <code>x[None, :] @ x[:, None]</code> | <code>(1, 1)</code> | 원소 하나가 5인 2차원 배열이다. |

<code>()</code>는 스칼라의 shape이다. 마지막 두 곱은 원소 수와 결과 차원이 다르므로 구별해야 한다.

위의 <code>x[:, None] @ x[None, :]</code>는
11장에서 언급한 <code>np.outer(x, x)</code>와 같다.
행렬곱의 안쪽 크기 조건은 10장의 원소별 연산에 대한 브로드캐스팅 조건과 구분한다.

# 7. 단위행렬과 전치행렬

## 7.1. 단위행렬

단위행렬(identity matrix)은 대각성분이 1이고 나머지가 0인 정사각행렬이다.

~~~python
I = np.eye(3)
x = np.array([2.0, 3.0, 4.0])

print(I)
print(I @ x)
~~~

단위행렬을 곱하면 원래 벡터나 행렬이 유지된다.

$$
[\boldsymbol I][\boldsymbol x]=[\boldsymbol x]
$$

## 7.2. 전치행렬

전치(transpose)는 행과 열을 바꾼다.

~~~python
A = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
])

A_transpose = A.T

print(A.shape)
print(A_transpose.shape)
print(A_transpose)
~~~

$$(2,3)$$ 행렬의 전치는 $$(3,2)$$ 행렬이다.

## 7.3. 곱의 전치는 순서를 뒤집는다

$$
([\boldsymbol A][\boldsymbol B])^T=[\boldsymbol B]^T[\boldsymbol A]^T.
$$

$$[\boldsymbol A]$$가 $$2\times3$$, $$[\boldsymbol B]$$가 $$3\times4$$이면
곱의 전치는 $$4\times2$$다. 오른쪽도 $$(4\times3)(3\times2)$$이므로 같은 shape을 갖는다.
<code>A.T @ B.T</code>로 쓰면 이 예제에서는 곱 자체가 불가능하다.

# 8. 행렬식과 역행렬

## 8.1. 행렬식

[행렬식(determinant)](https://ko.wikipedia.org/wiki/행렬식)은 정사각행렬에 대해 정의되는 스칼라이다. 2×2 행렬에서는

$$
\det
\begin{bmatrix}
a&b\\c&d
\end{bmatrix}
=ad-bc
$$

이다.

~~~python
A = np.array([
    [2.0, 1.0],
    [1.0, 3.0],
])

determinant = np.linalg.det(A)
print(determinant)
~~~

행렬식이 0이면 역행렬이 존재하지 않는다.

## 8.2. 역행렬

역행렬(inverse matrix)은 다음 관계를 만족한다.

$$
[\boldsymbol A]^{-1}[\boldsymbol A]
=
[\boldsymbol I]
$$

~~~python
A_inverse = np.linalg.inv(A)

print(A_inverse)
print(A_inverse @ A)
~~~

부동소수점 계산 결과는 정확한 정수 대신 0에 매우 가깝거나 1에 매우 가까운 값으로
나타날 수 있다. 두 배열이 가까운지 확인할 때는 <code>np.allclose()</code>를 사용한다.

~~~python
print(
    np.allclose(
        A_inverse @ A,
        np.eye(2),
    )
)
~~~

## 8.3. 행렬식의 기하학적 의미와 특이행렬

2차원에서 행렬의 두 열을 변으로 하는 평행사변형의 넓이는 $$|\det[\boldsymbol A]|$$다.
즉, 단위 정사각형을 그 행렬로 변환했을 때의 넓이다.
일반적인 영역의 넓이는 변환 전 넓이의 $$|\det[\boldsymbol A]|$$배가 된다.
음의 행렬식은 넓이가 음수라는 뜻이 아니라 방향의 뒤집힘을 나타낸다.

예를 들어 $$[\boldsymbol A]=\begin{bmatrix}2&1\\0&3\end{bmatrix}$$의 열은
$$(2,0)^T$$와 $$(1,3)^T$$이며, 넓이는 $$|2(3)-1(0)|=6$$이다.

반면

$$
[\boldsymbol D]=\begin{bmatrix}1&2\\2&4\end{bmatrix}
$$

의 두 열은 평행하여 넓이가 0이다. 서로 다른 입력이 같은 출력으로 갈 수 있으므로
출력에서 입력을 유일하게 복원할 수 없다. 이런 행렬을 **특이행렬(singular matrix)**이라 한다.

<code>np.linalg.det(A) == 0</code>이라는 부동소수점 비교만으로 수치적 안정성을 판단하지 말자.
거의 종속인 행·열을 가진 행렬도 계산에 민감할 수 있다.

# 9. 연립방정식 풀기

다음 연립방정식을 생각하자.

$$
\begin{aligned}
2x+y&=5,\\
x+3y&=6.
\end{aligned}
$$

행렬 형태는

$$
[\boldsymbol A][\boldsymbol x]=[\boldsymbol b]
$$

이며

$$
[\boldsymbol A]=
\begin{bmatrix}2&1\\1&3\end{bmatrix},
\quad
[\boldsymbol x]=
\begin{bmatrix}x\\y\end{bmatrix},
\quad
[\boldsymbol b]=
\begin{bmatrix}5\\6\end{bmatrix}
$$

이다.

~~~python
A = np.array([
    [2.0, 1.0],
    [1.0, 3.0],
])
b = np.array([5.0, 6.0])

x = np.linalg.solve(A, b)

print(x)
print(A @ x)
~~~

해는 $$x=1.8$$, $$y=1.4$$이고 <code>A @ x</code>는 원래 우변 $$b$$와 같다.

연립방정식을 풀 때는 역행렬을 직접 계산하여 <code>np.linalg.inv(A) @ b</code>로
구하기보다 <code>np.linalg.solve(A, b)</code>를 사용하는 것이 좋다.

## 9.1. 해를 구한 뒤에는 잔차를 확인한다

계산된 해가 $$[\boldsymbol x]$$이면 **잔차(residual)**를
$$[\boldsymbol r]=[\boldsymbol A][\boldsymbol x]-[\boldsymbol b]$$로 정의한다.

~~~python
A = np.array([[2.0, 1.0], [1.0, 3.0]])
b = np.array([5.0, 6.0])
x = np.linalg.solve(A, b)
residual = A @ x - b
print(x)                          # [1.8, 1.4]
print(residual)
print(np.allclose(A @ x, b))       # True
~~~

잔차가 작다는 것은 방정식을 잘 만족한다는 뜻이다.
다만 계수행렬이 거의 특이하면 작은 입력 오차에도 해가 크게 달라질 수 있으므로,
잔차가 작다는 사실만으로 측정 오차까지 작은 해라고 단정할 수는 없다.

<code>np.linalg.solve()</code>는 여기서 다루는 정사각이고 특이하지 않은 계수행렬에 사용한다.
특이행렬의 연립방정식은 우변에 따라 해가 없거나 무한히 많을 수 있다.
측정식 개수와 미지수 개수가 다른 최소제곱 문제는
[제16강 최소자승법]({% link assets/lecture_notes/1_2_data_mse/data_mse_16_최소자승법.md %})에서 다룬다.

# 10. 재료공학 예제

## 10.1. 격자 좌표를 실제 위치로 변환하기

직교하는 격자벡터의 길이가 $$a=2$$, $$b=3$$, $$c=4$$라고 하자. [분율좌표(fractional coordinates)](https://en.wikipedia.org/wiki/Fractional_coordinates)
$$\boldsymbol p=(0.5,0.5,0.25)$$를 실제 위치로 바꾸는 행렬은

$$
[\boldsymbol L]=
\begin{bmatrix}
2&0&0\\
0&3&0\\
0&0&4
\end{bmatrix}
$$

이다.

~~~python
lattice_matrix = np.diag([2.0, 3.0, 4.0])
fractional_position = np.array([
    0.5,
    0.5,
    0.25,
])

cartesian_position = (
    lattice_matrix @ fractional_position
)

print(cartesian_position)
~~~

결과는 $$(1,1.5,1)$$이다.

## 10.2. 두 격자점 사이의 거리

~~~python
fractional_p = np.array([0.0, 0.0, 0.0])
fractional_q = np.array([0.5, 0.5, 0.25])

cartesian_p = lattice_matrix @ fractional_p
cartesian_q = lattice_matrix @ fractional_q

distance = np.linalg.norm(
    cartesian_q - cartesian_p
)

print(distance)
~~~

두 점 사이의 거리는 $$\sqrt{1^2+1.5^2+1^2}\approx2.062$$이다.

## 10.3. 기울어진 격자와 여러 점의 위치

평면 내 격자벡터를 $$\boldsymbol a=(2,0)\,\mathrm{nm}$$,
$$\boldsymbol b=(1,3)\,\mathrm{nm}$$로 정하자. 이 벡터들을 **열**에 배치하면

$$
[\boldsymbol L]=\begin{bmatrix}2&1\\0&3\end{bmatrix},
\qquad
[\boldsymbol r]=[\boldsymbol L]\begin{bmatrix}p\\q\end{bmatrix}
=p\begin{bmatrix}2\\0\end{bmatrix}+q\begin{bmatrix}1\\3\end{bmatrix}
$$

이다. $$p=q=0.5$$이면 실제 위치는 $$(1.5,1.5)\,\mathrm{nm}$$다.
분율좌표의 성분 $$p,q$$는 무차원이며, 격자벡터에 곱해 실제 위치를 만든다.
기울어진 격자에서는 분율좌표의 성분을 제곱해 더한 뒤 제곱근을 구해도 실제 거리가 되지 않는다.
먼저 격자행렬로 실제 직교좌표 성분을 구한 뒤 벡터의 크기를 계산해야 한다.

여러 점을 **행마다 하나씩** 저장했다면 <code>L @ P</code> 대신 <code>P @ L.T</code>를 쓴다.
한 점에 대한 식을 전치하면 $$([\boldsymbol L][\boldsymbol p])^T=[\boldsymbol p]^T[\boldsymbol L]^T$$이기 때문이다.

~~~python
L = np.array([[2.0, 1.0], [0.0, 3.0]])
P = np.array([[0.0, 0.0], [0.5, 0.5], [1.0, 0.0]])
positions = P @ L.T
print(positions)  # [[0.0, 0.0], [1.5, 1.5], [2.0, 0.0]]
print(np.allclose(positions[1], L @ P[1]))  # True
~~~

여기서 구하는 것은 지정한 두 점의 직접 거리다. 주기적 경계조건에서 가장 가까운 원자 이미지를 찾는 문제는 별도의 처리가 필요하다.

# 11. 자주 하는 실수

- <code>A * B</code>를 행렬곱이라고 생각한다.
- 행렬곱 전에 두 행렬의 shape을 확인하지 않는다.
- 수학의 첨자와 Python 인덱스의 시작 번호를 혼동한다.
- $$AB=BA$$라고 생각한다.
- 정사각행렬이 아닌 행렬의 행렬식이나 역행렬을 구하려 한다.
- 행렬식이 0인 행렬의 역행렬을 구하려 한다.
- 연립방정식 계산에서 역행렬을 불필요하게 직접 구한다.

# 12. 정리

- 행렬은 2차원 NumPy 배열로 나타낼 수 있다.
- <code>*</code>는 원소별 곱이고 <code>@</code>는 행렬곱이다.
- 행렬–벡터곱은 각 행과 벡터의 내적으로 계산한다.
- $$(l,m)$$ 행렬과 $$(m,n)$$ 행렬의 곱은 $$(l,n)$$ 행렬이다.
- <code>np.eye()</code>는 단위행렬을 만든다.
- <code>A.T</code>는 전치행렬이다.
- <code>np.linalg.det()</code>와 <code>np.linalg.inv()</code>로 행렬식과 역행렬을 계산한다.
- 연립방정식은 <code>np.linalg.solve()</code>로 푼다.

{% comment %}TODO: 파일 추가 후 복구
[기울어진 격자와 원자 이동 실습]({% link assets/lecture_notes/1_2_data_mse/data_mse_supp_vector_matrix_lab.md %})에서 위치 변환, 변위, 투영, 넓이와 역변환을 함께 연습할 수 있다.
{% endcomment %}

# 13. 연습 문제

## 문제 1

다음 행렬의 shape을 쓰시오.

$$
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
$$

<!--
풀이와 해답:
2행 3열이므로 shape은 (2,3)이다.
-->

## 문제 2

NumPy에서 원소별 곱과 행렬곱에 사용하는 연산자를 각각 쓰시오.

<!--
풀이와 해답:
원소별 곱은 *이고 행렬곱은 @이다.
-->

## 문제 3

다음 행렬–벡터곱을 계산하라.

$$
\begin{bmatrix}
1&0\\
0&2
\end{bmatrix}
\begin{bmatrix}
3\\4
\end{bmatrix}
$$

<!--
풀이와 해답:
결과는 (3,8)^T이다.
-->

## 문제 4

shape이 $$(2,3)$$인 행렬과 $$(3,4)$$인 행렬을 곱할 수 있는가? 결과 shape도 쓰시오.

<!--
풀이와 해답:
안쪽 크기 3이 같으므로 곱할 수 있고 결과 shape은 (2,4)이다.
-->

## 문제 5

단위행렬 $$\boldsymbol I$$와 벡터 $$\boldsymbol x$$의 곱은 무엇인가?

<!--
풀이와 해답:
I x=x이므로 원래 벡터 x이다.
-->

## 문제 6

다음 2×2 행렬

$$\begin{bmatrix}2&1\\1&3\end{bmatrix}$$

의 행렬식을 구하라.

<!--
풀이와 해답:
2 곱하기 3에서 1 곱하기 1을 빼면 5이다.
-->

## 문제 7

행렬 $$A$$와 벡터 $$b$$로 이루어진 연립방정식 $$Ax=b$$를 푸는 NumPy 함수를 쓰시오.

<!--
풀이와 해답:
np.linalg.solve(A, b)를 사용한다.
-->

## 문제 8: 열벡터의 선형결합

$$
[\boldsymbol A]=\begin{bmatrix}2&-1\\1&3\end{bmatrix},
\qquad [\boldsymbol x]=\begin{bmatrix}3\\2\end{bmatrix}
$$

에 대해 행별 내적과 열벡터의 선형결합 두 방법으로 곱을 계산하고 비교하라.

<!--
풀이와 해답:
행별로는 (2(3)-1(2), 1(3)+3(2))^T=(4,9)^T이다.
열별로는 3(2,1)^T+2(-1,3)^T=(4,9)^T이다.
-->

## 문제 9: 곱의 순서

4.2절의 $$[\boldsymbol S]$$, $$[\boldsymbol Q]$$에 대해
$$[\boldsymbol Q][\boldsymbol S]$$와 $$[\boldsymbol S][\boldsymbol Q]$$를 손으로 구하라.
$$[\boldsymbol x]=(2,1)^T$$에 작용한 결과도 비교하라.

<!--
풀이와 해답:
QS=[[0,-1],[2,0]], SQ=[[0,-2],[1,0]]이다.
QSx=(-1,4)^T, SQx=(-2,2)^T이므로 다르다.
-->

## 문제 10: 전치와 shape

<code>A.shape == (2, 3)</code>, <code>B.shape == (3, 4)</code>일 때
<code>A @ B</code>, <code>(A @ B).T</code>, <code>B.T @ A.T</code>의 shape을 쓰시오.
<code>A.T @ B.T</code>가 불가능한 이유를 설명하라.

<!--
풀이와 해답:
각각 (2,4), (4,2), (4,2)이다.
A.T @ B.T는 (3,2) @ (4,3)으로 안쪽 크기 2와 4가 맞지 않는다.
-->

## 문제 11: 1차원 배열과 행·열 배열

<code>x = np.array([2.0, 3.0])</code>에 대해
<code>x.T</code>, <code>x @ x</code>,
<code>x[:, None] @ x[None, :]</code>의 값과 shape을 각각 구하라.

<!--
풀이와 해답:
x.T는 [2,3], shape (2,)이다.
x @ x는 13, shape ()이다.
열 배열과 행 배열의 곱은 [[4,6],[6,9]], shape (2,2)이다.
-->

## 문제 12: 행렬식과 격자 넓이

평면 격자벡터가 $$(2,0)\,\mathrm{nm}$$와 $$(1,3)\,\mathrm{nm}$$다.
이들을 열에 놓은 행렬을 쓰고 행렬식과 단위 격자 평행사변형의 넓이를 구하라.
두 열을 바꾸면 행렬식과 넓이는 어떻게 바뀌는가?

<!--
풀이와 해답:
L=[[2,1],[0,3]], det(L)=6 nm^2이고 넓이는 6 nm^2이다.
열을 교환하면 det=-6 nm^2이지만 넓이는 절댓값인 6 nm^2이다.
-->

## 문제 13: 해가 없거나 무한히 많은 경우

$$
[\boldsymbol D]=\begin{bmatrix}1&2\\2&4\end{bmatrix}
$$

에 대해 우변이 $$(3,6)^T$$일 때와 $$(3,7)^T$$일 때를 비교하라.
각 경우에 해가 하나인지, 없는지, 무한히 많은지 설명하라.

<!--
풀이와 해답:
두 번째 좌변은 첫 번째 좌변의 2배다.
우변이 (3,6)이면 같은 방정식이 반복되며 x+2y=3을 만족하는 해가 무한히 많다.
우변이 (3,7)이면 x+2y=3과 2x+4y=7이 모순되므로 해가 없다.
두 경우 모두 유일한 해를 구하는 np.linalg.solve의 전제에 맞지 않는다.
-->

## 문제 14: 혼합물의 질량수지

두 원료의 특정 원소 질량분율이 각각 0.2와 0.6이다.
총질량 10 g, 해당 원소 질량 4 g인 혼합물을 만들기 위한 원료 질량 $$m_1,m_2$$를 구하라.
행렬식을 세우고 <code>np.linalg.solve()</code>로 계산한 뒤 잔차를 확인하라.

<!--
풀이와 해답:
m_1+m_2=10, 0.2m_1+0.6m_2=4이다.
A=np.array([[1.,1.],[0.2,0.6]]), b=np.array([10.,4.])이다.
np.linalg.solve(A,b)의 결과는 [5,5] g이다.
A @ masses-b는 부동소수점 오차 범위에서 영벡터다.
-->

## 문제 15: 기울어진 격자의 두 점

10.3절의 격자행렬에서 분율좌표 $$P=(0,0)$$와 $$Q=(0.5,0.5)$$의 실제 위치와 직접 거리를 구하라.
여러 점을 행으로 저장한 배열에 <code>P @ L.T</code>를 적용하는 이유도 설명하라.

<!--
풀이와 해답:
실제 위치는 (0,0) nm와 (1.5,1.5) nm이며 거리는 sqrt(4.5)=약 2.12132 nm이다.
한 점의 열벡터 식 r=L p를 전치하면 r^T=p^T L^T이므로,
각 행에 한 점을 저장한 경우 오른쪽에 L.T를 곱해야 한다.
분율좌표 거리 sqrt(0.5)는 무차원이므로 실제 거리로 사용할 수 없다.
-->

[이전 강의]({% link assets/lecture_notes/1_2_data_mse/data_mse_11_벡터연산기초.md %}) | [강의 목록]({% link _lectures/1_2_data_mse.md %}) | [다음 강의]({% link assets/lecture_notes/1_2_data_mse/data_mse_13_행렬벡터연산고급_Ein.md %})
