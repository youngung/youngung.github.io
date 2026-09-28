---
layout: distill
title: 행렬과 텐서 연산
description: 수축, 전치, 역행렬, 행렬식과 Einstein 표기법
target: 학부 고학년
permalink:
featured: true
prerequisite: 벡터와 좌표계
toc:
  sidebar: left

mermaid:
  enabled: true
  zoomable: true
typograms: true
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---


관련 자료는 다음 순서로 읽을 수 있다.

- [제4강 벡터와 좌표계]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04_vector_matrix.md %})
- [제5강 행렬과 텐서 연산]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %})

# 1. 매트릭스 연산

## 1.1. 더하기, 빼기

- 같은 랭크의 매트릭스 $\boldsymbol A$와 $\boldsymbol B$의 합이나 차는 같은 랭크의 또 다른 매트릭스가 된다.

$$\boldsymbol C = \boldsymbol A + \boldsymbol B$$

$$\boldsymbol D = \boldsymbol A - \boldsymbol B$$

- 랭크 2인 행렬, 즉 $3\times3$ 행렬의 합과 차를 다음과 같이 연산한다.

$$C_{11}=A_{11}+B_{11}$$

$$C_{12}=A_{12}+B_{12}$$

$$C_{13}=A_{13}+B_{13}$$

$$C_{21}=A_{21}+B_{21}$$

$$C_{22}=A_{22}+B_{22}$$

$$C_{23}=A_{23}+B_{23}$$

$$C_{31}=A_{31}+B_{31}$$

$$C_{32}=A_{32}+B_{32}$$

$$C_{33}=A_{33}+B_{33}$$

- 위와 같은 표현을 너무 길다. 아래와 같이 축약해서 표기할 수 있다.

$$C_{ij}=A_{ij}+B_{ij} \text{ with } i=1,2,3, \ \ \ j=1,2,3$$


## 1.2. 스칼라 곱하기

- 매트릭스에 스칼라를 곱하면 같은 랭크의 다른 매트릭스가 된다.

$$\boldsymbol B = c \boldsymbol A $$

- 이는 아래와 같다.

$$B_{ij}=c A_{ij} \text{ with } i=1,2,3, \ \ \ j=1,2,3$$

## 1.3. 매트릭스 곱하기1 (single contraction)

- 랭크 2인 매트릭스에 벡터를 곱하면 벡터가 된다.

$$\boldsymbol b = \boldsymbol A \cdot \boldsymbol v$$

- 위는 아래와 같이 계산된다.

$$b_1 = \sum_{j=1}^3 A_{1j} v_j $$

$$b_2 = \sum_{j=1}^3 A_{2j} v_j $$

$$b_3 = \sum_{j=1}^3 A_{3j} v_j $$

- 따라서 축약하면

$$b_i = \sum_{j=1}^3 A_{ij} v_j \text{ with } i=1,2,3$$

- 아래의 경우를 살펴보자.

$$\boldsymbol c = \boldsymbol v \cdot \boldsymbol B$$

- 위를 앞선 인덱스 표기법을 적용하면 아래와 같다.

$$c_j = \sum_{i=1}^3 v_i B_{ij},\qquad j=1,2,3.$$

이를 성분 배열로 계산할 때는 행벡터 곱 $[\boldsymbol c]^T=[\boldsymbol v]^T[\boldsymbol B]$로 쓴다.
따라서 열벡터로 나타내면 $[\boldsymbol c]=[\boldsymbol B]^T[\boldsymbol v]$이다.

- 교환 법칙이 성립하지 않는다.

$$ \boldsymbol A\cdot \boldsymbol v \ne \boldsymbol v \cdot \boldsymbol A $$

## 1.4. 매트릭스 곱하기2 (double contraction)

- 앞서 곱셈이 한 첨자 기호에만 적용된 경우를 살펴보았다. 즉

$$d_i = \sum_{j=1}^3 A_{ij} b_j \text{ with } i=1,2,3$$

- 랭크2인 두 매트릭스 사이에서는 두 첨자 사이에 위와 같은 곱이 수행될 수 있으며, 그 결과는 스칼라가 된다.

$$c = A_{ij} B_{ij} = \sum_{i=1}^3 \sum_{j=1}^3 A_{ij}B_{ij}$$

- 위와 같은 곱하기를 아래와 같이 ':'기호를 활용해 표기하기도 한다.

$$
c=\boldsymbol A : \boldsymbol B
$$

- 랭크가 3인 매트릭스 $A_{ijk}$와 벡터 $\boldsymbol b$ 사이의 single contraction 곱을 생각해보자.

$$B_{ij} = \sum_{k=1}^3A_{ijk} b_k \text{ with } i=1,2,3,\ \ \ j=1,2,3$$


## 1.5. 매트릭스 곱하기3 (2x2 matrix multiplication)

- 2x2 행렬 $\boldsymbol a$와 $\boldsymbol b$의 곱을 생각하자.
그 결과는 또 다른 2x2 행렬이 되며, 이를 $\boldsymbol c$라 하면

$$
\boldsymbol c = \boldsymbol a \cdot \boldsymbol b
$$

- 각 행렬의 성분을 아래와 같이 표현하면

$$
\boldsymbol a = \begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix},\qquad
\boldsymbol b = \begin{bmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{bmatrix},\qquad
\boldsymbol c = \begin{bmatrix}c_{11}&c_{12}\\c_{21}&c_{22}\end{bmatrix}.
$$

- 2x2 행렬사이의 곱을 성분별로 나타내면 다음과 같다.

$$
\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}
\begin{bmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{bmatrix}
=
\begin{bmatrix}c_{11}&c_{12}\\c_{21}&c_{22}\end{bmatrix}
=
\begin{bmatrix}a_{11}b_{11}+a_{12}b_{21}&a_{11}b_{12}+a_{12}b_{22}\\a_{21}b_{11}+a_{22}b_{21}&a_{21}b_{12}+a_{22}b_{22}\end{bmatrix}
$$

- 따라서 위 결과를 행렬 $\boldsymbol c$를 성분별로 나타내면

$$
c_{11}=a_{11}b_{11}+a_{12}b_{21}
$$

$$
c_{12}=a_{11}b_{12}+a_{12}b_{22}
$$

$$
c_{21}=a_{21}b_{11}+a_{22}b_{21}
$$

$$
c_{22}=a_{21}b_{12}+a_{22}b_{22}
$$


- 위에서 규칙을 찾으면, $\boldsymbol c$ 행렬의 성분 $c_{ij}$는 첫 번째 행렬 $\boldsymbol a$의 $i$번째 행과 두 번째 행렬의 $j$번째 열의 곱의 합으로 계산된다. 즉

$$
c_{ {\color{blue}{i}}{\color{red}{j}}} = a_{ {\color{blue}{i}}1}b_{1{\color{red}{j}}}+a_{ {\color{blue}{i}}2}b_{2{\color{red}{j}}}
$$

위를 summation 기호를 사용해 일반화하면 다음과 같다.

$$
c_{ {\color{blue}{i}}{\color{red}{j}}} = \sum_{k=1}^{2} a_{ {\color{blue}{i}}k} b_{k{\color{red}{j}}}
$$

$k$와 같이 summation index는 반복되는 첨자로 나타내며, 같은 첨자가 두 번 나타나면 그 첨자에 대해 합을 취한다. $k$를 dummy index라고도 부른다.

## 1.6. 매트릭스 곱하기4 (3x3 matrix multiplication)

- 3x3 행렬 $\boldsymbol a$와 $\boldsymbol b$의 곱을 생각하자.
그 결과는 또 다른 3x3 행렬이 되며, 이를 $\boldsymbol c$라 하면

$$
\boldsymbol c = \boldsymbol a \cdot \boldsymbol b
$$

- 각 행렬의 성분을 아래와 같이 표현하면

$$
\boldsymbol a = \begin{bmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{bmatrix},\qquad
\boldsymbol b = \begin{bmatrix}b_{11}&b_{12}&b_{13}\\b_{21}&b_{22}&b_{23}\\b_{31}&b_{32}&b_{33}\end{bmatrix},\qquad
\boldsymbol c = \begin{bmatrix}c_{11}&c_{12}&c_{13}\\c_{21}&c_{22}&c_{23}\\c_{31}&c_{32}&c_{33}\end{bmatrix}.
$$

- 3x3 행렬사이의 곱을 성분별로 나타내면 다음과 같다.

$$
\begin{bmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{bmatrix}
\begin{bmatrix}b_{11}&b_{12}&b_{13}\\b_{21}&b_{22}&b_{23}\\b_{31}&b_{32}&b_{33}\end{bmatrix}
=
\begin{bmatrix}c_{11}&c_{12}&c_{13}\\c_{21}&c_{22}&c_{23}\\c_{31}&c_{32}&c_{33}\end{bmatrix}
=
\begin{bmatrix}a_{11}b_{11}+a_{12}b_{21}+a_{13}b_{31}&a_{11}b_{12}+a_{12}b_{22}+a_{13}b_{32}&a_{11}b_{13}+a_{12}b_{23}+a_{13}b_{33}\\a_{21}b_{11}+a_{22}b_{21}+a_{23}b_{31}&a_{21}b_{12}+a_{22}b_{22}+a_{23}b_{32}&a_{21}b_{13}+a_{22}b_{23}+a_{23}b_{33}\\a_{31}b_{11}+a_{32}b_{21}+a_{33}b_{31}&a_{31}b_{12}+a_{32}b_{22}+a_{33}b_{32}&a_{31}b_{13}+a_{32}b_{23}+a_{33}b_{33}\end{bmatrix}
$$

앞선 2x2 행렬 곱과 마찬가지로, 3x3 행렬 곱도 각 성분 $c_{ij}$는 첫 번째 행렬 $\boldsymbol a$의 $i$번째 행과 두 번째 행렬 $\boldsymbol b$의 $j$번째 열의 곱의 합으로 계산된다. 즉

$$
c_{ {\color{blue}{i}}{\color{red}{j}}} = \sum_{k=1}^{3} a_{ {\color{blue}{i}}k} b_{k{\color{red}{j}}}
$$

## 1.7. 매트릭스 곱하기3 (자리를 바꿔 곱하기)

이 절에서는 두 행렬의 곱에서 자리를 바꿔 곱하는 경우를 다룬다. 일반적으로 행렬 곱은
교환법칙이 성립하지 않으므로,
$$\boldsymbol a \cdot \boldsymbol b \neq \boldsymbol b \cdot \boldsymbol a$$
이다. 다만 특별한 경우, 예를 들어 두 행렬이 모두 대각행렬이거나, 한 행렬이
단위행렬인 경우에는 교환법칙이 성립한다.

2x2 행렬 $\boldsymbol a$와 $\boldsymbol b$의 곱이 $\boldsymbol d$ 행렬이라 하자.
즉,
$$
\boldsymbol d = \boldsymbol b \cdot \boldsymbol a
$$
$$
\begin{bmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{bmatrix}
\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}
=
\begin{bmatrix}b_{11}a_{11}+b_{12}a_{21}&b_{11}a_{12}+b_{12}a_{22}\\b_{21}a_{11}+b_{22}a_{21}&b_{21}a_{12}+b_{22}a_{22}\end{bmatrix}
$$

따라서
$$
\begin{bmatrix}\boldsymbol d\end{bmatrix}
=
\begin{bmatrix}b_{11}a_{11}+b_{12}a_{21}&b_{11}a_{12}+b_{12}a_{22}\\b_{21}a_{11}+b_{22}a_{21}&b_{21}a_{12}+b_{22}a_{22}\end{bmatrix}
$$

그런데 일반적으로 $\boldsymbol a \cdot \boldsymbol b$ 곱의 결과 행렬을$\boldsymbol c$라 하고(즉, $\boldsymbol c = \boldsymbol b \cdot \boldsymbol a$) 그 결과를 구하면

$$
\begin{bmatrix}\boldsymbol c\end{bmatrix}
=
\begin{bmatrix}b_{11}a_{11}+b_{21}a_{12}&b_{12}a_{11}+b_{22}a_{12}\\b_{11}a_{21}+b_{21}a_{22}&b_{12}a_{21}+b_{22}a_{22}\end{bmatrix}

$$

여기서 $\boldsymbol c$ 행렬내의 성분들의 곱은 스칼라 값들간의 곱이므로, 교환법칙이 성립하며 따라서

$$
\begin{bmatrix}\boldsymbol c\end{bmatrix} =
\begin{bmatrix}a_{11}b_{11}+a_{12}b_{21}&a_{11}b_{12}+a_{12}b_{22}\\a_{21}b_{11}+a_{22}b_{21}&a_{21}b_{12}+a_{22}b_{22}\end{bmatrix}
$$

위 절에서 두 행렬의 곱 결과 $\boldsymbol d$와 $\boldsymbol c$를 비교하면,
일반적으로 $\boldsymbol d \neq \boldsymbol c$임을 알 수 있다.
따라서 일반적으로 행렬 곱은 교환법칙이 성립하지 않는다는 것을 알 수 있다.
$$
\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}
\begin{bmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{bmatrix}
\neq
\begin{bmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{bmatrix}
\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}
$$


## 1.8. 매트릭스 전치(transpose)


아래에서는 대괄호를 사용해 대응하는 행렬곱을 설명한다.

행렬 $[\boldsymbol A]$의 전치는 $[\boldsymbol A]^T$로 표기한다. 행과 열을 서로 바꾸므로,
$m\times n$ 행렬의 전치는 $n\times m$ 행렬이며 성분은

$$
([\boldsymbol A]^T)_{ij}=A_{ji}
$$

로 정의한다. 예를 들어

$$
[\boldsymbol A]=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix},
\qquad
[\boldsymbol A]^T=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}.
$$

전치를 두 번 적용하면 원래 행렬이 된다: $([\boldsymbol A]^T)^T=[\boldsymbol A]$.

## 1.9. 매트릭스 곱에서의 전치 적용

텐서 표기로는 $(\boldsymbol A\cdot\boldsymbol B)^T=\boldsymbol B^T\cdot\boldsymbol A^T$이며,

**곱의 전치 법칙**에서는 각 행렬을 전치하는 것과 함께 **곱의 순서를 뒤집어야 한다.**
$[\boldsymbol A]$가 $m\times n$, $[\boldsymbol B]$가 $n\times p$ 행렬이면

$$
\boxed{([\boldsymbol A][\boldsymbol B])^T=[\boldsymbol B]^T[\boldsymbol A]^T}.
$$

좌변은 $p\times m$ 행렬이고, 우변도 $(p\times n)(n\times m)$의 곱이므로 같은 크기다.
성분으로도 확인할 수 있다.

$$
[([{\boldsymbol A}][\boldsymbol B])^T]_{ij}
=([\boldsymbol A][\boldsymbol B])_{ji}
=\sum_{k=1}^{n}A_{jk}B_{ki}\\
$$

$$
=\sum_{k=1}^{n}([\boldsymbol B]^T)_{ik}([\boldsymbol A]^T)_{kj}
=([\boldsymbol B]^T[\boldsymbol A]^T)_{ij}.
$$

일반적으로 $([\boldsymbol A][\boldsymbol B])^T=[\boldsymbol A]^T[\boldsymbol B]^T$는 성립하지 않는다.
행렬 세 개의 곱에도 같은 규칙을 적용한다.

$$
([\boldsymbol A][\boldsymbol B][\boldsymbol C])^T
=[\boldsymbol C]^T[\boldsymbol B]^T[\boldsymbol A]^T.
$$

열벡터도 행렬의 일종이므로, 행렬과 벡터의 곱에 같은 규칙을 적용할 수 있다.

$$
([\boldsymbol A][\boldsymbol a])^T=[\boldsymbol a]^T[\boldsymbol A]^T,
\qquad
([\boldsymbol A][\boldsymbol a])^T([\boldsymbol A][\boldsymbol a])
=[\boldsymbol a]^T[\boldsymbol A]^T[\boldsymbol A][\boldsymbol a].
$$

마지막 식은 변환된 벡터의 길이의 제곱을 나타내는 스칼라이며,
변형 전후 선분의 길이를 비교할 때에도 사용한다.


## 1.10. 매트릭스 trace

- 한 매트릭스 $\boldsymbol A$의 trace는 $tr(\boldsymbol A)$라 표기하고, 다음과 같이 정의된다.

$$
tr(\boldsymbol A) = A_{11}+A_{22}+A_{33}=\sum_{i=1}^3A_{ii}
$$


## 1.11. 역행렬 (inverse matrix)

- 한 매트릭스 $\boldsymbol A$의 역은 $\boldsymbol A^{-1}$라 표기하고, 다음의 성질을 만족한다.

$$
\boldsymbol{A}\cdot\boldsymbol{A}^{-1}=\boldsymbol {I}
$$

- 즉
$$
\sum_{k=1}^3A_{ik}A^{-1}_{kj}=I_{ij} \text{ with } i=1,2,3\ \ \ \ j=1,2,3
$$

# 2. Determinant


## 2.1. $2\times2$ 행렬

$$
[\boldsymbol A]=\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

$$
\det(\boldsymbol A) = |\boldsymbol A| = ad -bc
$$


## 2.2. $3\times3$ 행렬

$$
[\boldsymbol A]=\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
$$

$$
\det(\boldsymbol A)=|\boldsymbol A| = a(ei-fh)-b(di-fg)+c(dh-eg)
$$



# 3. 랭크의 증감

- Contraction: 물리량들 사이에 곱을 통해 랭크가 감소하는 경우

  - $a_i = \sum_{j=1}^3A_{ij}b_j\ \ \text{ with }\ i=1,2,3$

- Outer product: 물리량들 사이에 곱을 통해 랭크가 증가하는 경우

  - $A_{ij}=a_ib_j\ \ \text{ with } i=1,2,3,\ \ \ j=1,2,3$

- 랭크가 유지되는 경우
  - $b_i=ca_i \ \ \text{ with } i=1,2,3$


# 4. Einstein 표기법

- Einstein 합 규약에서는 한 항에 같은 첨자가 두 번 나타나면 그 첨자에 대해 합을 취한 것으로 약속한다.

- 아래 각 결과가 무엇이 될까? 그리고 그 결과는 몇 **랭크**의 물리량이 될까?

$$ a_{ijk} b_{i} $$

$$ a_{ijk} b_{jk} $$

$$ a_{ijk} b_{ik} $$

$$ a_{ijk} b_{ijk} $$

## 텐서와 행렬 표현을 구분하기

벡터와 텐서는 좌표계와 무관한 물리량이고, 열벡터와 행렬은 선택한 좌표계에서 그 성분을
배열한 표현이다. 좌표계를 바꾸면 성분 행렬은 달라지지만 물리량 자체는 달라지지 않는다.

| 연산 | 성분 표현 | 결과 |
|---|---|---|
| 벡터 내적 | $a_ib_i$ | 스칼라 |
| dyadic product | $a_ib_j$ | 2차 텐서 |
| 텐서–벡터 곱 | $A_{ij}b_j$ | 벡터 |
| 텐서 이중수축 | $A_{ij}B_{ij}$ | 스칼라 |

예를 들어 $dW=\boldsymbol\sigma:d\boldsymbol\varepsilon$은 단위부피당 일이라는
스칼라를 만들고, $\boldsymbol t=\boldsymbol\sigma\cdot\boldsymbol n$은 면력벡터(traction vector)를 만든다.
수축되는 첨자의 수와 결과의 랭크를 확인해야 한다.


# 5. 연습 문제


## 문제 1

단위행렬 $\boldsymbol I$와 임의의 벡터 $\boldsymbol a$의 곱 $\boldsymbol I\cdot\boldsymbol a$는 무엇인가?

<!--
풀이와 해답:
원래 벡터 a와 같다.
-->

# 추가 연습문제

[링크]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/Vector_Matrix_Exercises.md %})를 활용하세요
