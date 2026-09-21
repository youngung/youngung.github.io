---
layout: distill
title: 벡터와 좌표계
description: 물리량, 좌표계와 벡터 연산의 기초
target: 학부 고학년
permalink:
featured: true
prerequisite: 기초수학
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

- [벡터와 좌표계]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04_vector_matrix.md %})
- [행렬과 텐서 연산]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %})

# 1. 물리량의 종류

- 물리량은 때로는 스칼라, 벡터로 표현해야 할 때가 있다.

- 더욱 일반적인 물리량 표현법은 '텐서'이다. 텐서(tensor)는 스칼라 벡터를 모두 통합하여 설명한다.

- 텐서의 가장 큰 특징은 '좌표계'에 상관없이 동일한 물리량을 표현한다는 점이다. (좌표계에 무관한 성질)

  - (advanced concept) 텐서가 좌표계에 독립적인 성질을 갖는 방법은, 좌표계에 따라 '변환'하기 때문에 가능하다.

  - 좌표 변환법: 텐서의 랭크에 따라 변환 규칙이 달라진다.

# 2. 스칼라와 벡터

- 자극, 반응, 그리고 물질의 성질 모두 '물리량'으로써 그 세기나 크기를 표현한 '값'(value)으로 표현된다.

- 스칼라(scalar) 물리량은 해당 물리량이 '방향'과 관련된 성질을 갖지 않을 때 활용된다. (예: 질량, 밀도)

- 만약 물리량이 '방향'에 따라 달라진다면 (방향성을 가진다면), 스칼라 물리량만으로 온전히 물리량을 나타낼 수 없다.

- 그럴 경우, 벡터를 활용해 물리량의 세기/크기 뿐만 아니라 그 방향성(directionality)도 표현할 수 있겠다.

- 때로는 벡터 물리량만으로 그 방향성을 완전히 표현하기 힘든 물리량이 있으며, 이럴 때 우리는 '텐서'를 활용한다.

- 응력과 변형률은 대표적인 텐서 물리량이다.

- 텐서 물리량의 '연산'을 위해 이를 종종 매트릭스나 벡터로 나타내어 계산한다.

- 알파벳이나 그리스 알파벳 기호를 활용해 물리량을 표기한다.
  ($m$, $f$, $\alpha$, $\beta$ 등)

- 굵은 글씨체 (bold-face)를 활용해 '방향'성을 가진 물리량을 표기한다.
  ($a, \boldsymbol a, \alpha, {\boldsymbol \alpha}$)

- 윗첨자 혹은 아랫첨자를 활용해 벡터나 텐서, 혹은 매트릭스의 성분을 구분한다.
  ($a_1, \alpha^1, \beta_3, \gamma^1$ 등)

- 랭크
  - 첨자의 개수에 따라 랭크가 구분될 수 있다.
  - 스칼라는 첨자가 없다. 따라서, 랭크 0
  - 벡터는 첨자가 하나 있다. 따라서, 랭크 1
  - $3\times3$ 행렬은 첨자가 두개다. 따라서 랭크 2

# 3. 좌표계 (coordinate system)

좌표계는 공간의 점이나 방향을 수로 표현하기 위한 기준이다. 벡터 자체는 공간에
존재하는 기하학적·물리적 대상이지만, 벡터의 성분은 선택한 좌표계에 따라 정해진다.
따라서 벡터와 그 성분을 구분하는 것이 이후의 텐서 및 좌표변환을 이해하는 출발점이다.

## 3.1. 원점과 기저벡터(basis vector)

직각좌표계는 원점 $O$와 서로 수직인 단위 기저벡터
$\{\boldsymbol e_1,\boldsymbol e_2,\boldsymbol e_3\}$로 정의한다. 기저벡터는 각
좌표축의 양의 방향과 단위 길이를 동시에 정하며,

$$
{\boldsymbol e}_i\cdot{\boldsymbol e}_j=\delta_{ij}
$$

를 만족한다. 즉 같은 기저벡터끼리의 내적은 1이고 서로 다른 기저벡터끼리의 내적은
0이다. 이러한 기저를 **정규직교 기저**(orthonormal basis)라고 한다.

좌표계는 물리법칙에 의해 하나로 정해지는 것이 아니라 문제를 편리하게 기술하도록
선택한다. 예를 들어 압연방향, 폭방향, 판재 두께방향을 각각
$\boldsymbol e_1,\boldsymbol e_2,\boldsymbol e_3$로 선택할 수 있다. 다른 좌표계를
선택해도 물리적 벡터 자체는 변하지 않지만 그 성분은 달라질 수 있다.

## 3.2. 벡터와 벡터의 성분

임의의 3차원 벡터 $\boldsymbol a$는 선택한 기저벡터의 선형결합으로 나타낼 수 있다.

$$
\boldsymbol a
=a_1\boldsymbol e_1+a_2\boldsymbol e_2+a_3\boldsymbol e_3
=\sum_{i=1}^{3}a_i\boldsymbol e_i.
$$

여기서 $\boldsymbol e_i$는 방향을 가진 기저벡터이고, $a_i$는 그 방향으로의 크기를
나타내는 스칼라 성분이다. 정규직교 기저에서는 $\boldsymbol a$를 각 기저벡터에
투영하여

$$
a_i=\boldsymbol a\cdot\boldsymbol e_i
$$

로 성분을 얻는다. 이 성분들을 배열한

$$
[\boldsymbol a]_{\{\boldsymbol e_i\}}
=\begin{bmatrix}a_1\\a_2\\a_3\end{bmatrix}
$$

는 기저 $\{\boldsymbol e_i\}$에서 본 $\boldsymbol a$의 **좌표 열벡터**이다.
$\boldsymbol a$는 물리적 벡터이고, 위 열벡터는 특정 기저에서 그 벡터를 나타낸
수의 배열이라는 차이가 있다.

**열벡터 (column vector)**는 성분을 세로로 배열한 $n\times1$ 행렬이고,
**행벡터 (row vector)**는 성분을 가로로 배열한 $1\times n$ 행렬이다.
한 정규직교 기저에서 3차원 벡터의 성분을 나타내면

$$
[\boldsymbol a]=\begin{bmatrix}a_1\\a_2\\a_3\end{bmatrix}
\quad(3\times1),
\qquad
[\boldsymbol a]^T=\begin{bmatrix}a_1&a_2&a_3\end{bmatrix}
\quad(1\times3).
$$

여기서 위첨자 $T$는 **전치 (transpose)**로, 행과 열을 서로 바꾸는 연산이다.
행벡터·열벡터라는 구분은 성분의 배열 방식이며, 공간에서 벡터가 수평·수직으로
향한다는 뜻은 아니다. 성분 배열에는 대괄호를 유지하여 물리적 벡터와 구분한다.

배열의 방향에 따라 곱의 결과도 달라진다. 같은 정규직교 기저의 실수 성분에 대해

$$
[\boldsymbol a]^T[\boldsymbol b]
=\begin{bmatrix}a_1&a_2&a_3\end{bmatrix}
\begin{bmatrix}b_1\\b_2\\b_3\end{bmatrix}
=\sum_{i=1}^3 a_i b_i
\quad(1\times1)
$$

은 내적을 나타내는 스칼라이고, $[\boldsymbol a][\boldsymbol b]^T$는
$([\boldsymbol a][\boldsymbol b]^T)_{ij}=a_i b_j$인 $3\times3$ 행렬로서 다이아딕 곱을 표현한다.
성분 배열의 행렬곱에서는 **왼쪽 행렬의 열 수와 오른쪽 행렬의 행 수가 같아야 한다.**

<img src="/assets/img/lecture_notes/vector_basis_coordinates.png" alt="동일한 벡터를 두 정규직교 기저에서 서로 다른 성분으로 나타낸 그림" width="800"/>

그림에서 검은색 화살표 $\boldsymbol a$는 하나의 동일한 벡터이다. 파란색 기저에서는
$\boldsymbol a=a_1\boldsymbol e_1+a_2\boldsymbol e_2$로 분해되고, 회전된 붉은색
기저에서는 $\boldsymbol a=a'_1\boldsymbol e'_1+a'_2\boldsymbol e'_2$로 분해된다.
일반적으로 $(a_1,a_2)\ne(a'_1,a'_2)$이지만 두 식이 나타내는 물리적 벡터는 같다.

## 3.3. 행렬도 기저(basis)에 의존한다

2차 텐서 $\boldsymbol A$도 좌표계와 무관한 물리적 대상이며, 그 성분은 선택한
기저를 이용해

$$
A_{ij}=\boldsymbol e_i\cdot(\boldsymbol A\cdot\boldsymbol e_j)
$$

로 정의한다. 이 성분을 행과 열로 배열한 것이 행렬 $[\boldsymbol A]$이다. 따라서
**텐서와 행렬은 같은 말이 아니다.** 텐서는 좌표계와 무관한 대상이고, 행렬은 그
텐서를 특정 기저에서 표현한 성분 배열이다. 이후의 성분 계산은 모두 같은 기저에서 수행한다. 물리적 단일수축에는 $\cdot$,
다이아딕 곱에는 $\otimes$, 이중수축에는 $:$를 사용한다. 성분 배열은
$[\boldsymbol a]$, $[\boldsymbol A]$처럼 대괄호로 표시하고, 배열의 행렬곱은 붙여 쓴다.
스칼라와 벡터·텐서의 곱은 $c\boldsymbol a$, $c\boldsymbol A$처럼 표기한다.

이 강의에서는 주로 직각좌표계를 사용하지만, 원통좌표계나 구면좌표계처럼 위치에 따라
기저벡터의 방향이 달라지는 좌표계도 있다.

# 4. 스칼라 연산

## 4.1. 더하기

- $1 + 3$

- $3 + b$

- $a + c$

## 4.2. 빼기

- $1 - 3$

- $3 - b$

- $a - c$

## 4.3. 곱하기

- $1 \times 3$

- $3 \times b$

- $a \times c$

혹은 문자로만 표현될 때, 곱셈 기호 $\times$를 생략하기도 한다.

- $c\times d=cd$

## 4.4. 나누기

- $1 \div 3$

- $3 / b$

- $\frac{a}{c}$

# 5. 벡터 연산

## 5.1. 벡터의 크기

- 벡터는 스칼라처럼 크기를 가지며 거기에 '방향'도 가진다.

- 한 벡터 $\boldsymbol a$ 의 크기는 아래와 같이 표기된다.
  $|\boldsymbol a|$

- 한 벡터 $\boldsymbol a$가 세 성분 $a_1, a_2, a_3$로 이루어진다면 그 크기는
  아래와 같이 정의된다.

  $$|\boldsymbol a|=\sqrt{a_1^2+a_2^2+a_3^2}$$

- 위를 줄여서 아래와 같이 종종 표기한다.

  $$|\boldsymbol a|=\sqrt{\sum_{i=1}^3 a_i^2}$$

- 혹은

  $$||\boldsymbol a||_{\textcolor{red}{2}}=\sqrt{\sum_{i=1}^3 a_i^{\textcolor{red}{2}}}$$

## 5.2. 더하기, 빼기

- 두 벡터의 더하기 빼기는 각각 $+$와 $-$기호로 표기한다.

$$\boldsymbol a + \boldsymbol b$$

$$\boldsymbol a - \boldsymbol b$$

- 벡터의 덧셈 뺄셈 연산은 결과는 또 다른 벡터이다.

  $$\boldsymbol c = \boldsymbol a + \boldsymbol b$$

  $$\boldsymbol d = \boldsymbol a - \boldsymbol b$$

- 한 벡터가 세 성분으로 이루어져 있다면, 위 더하기 빼기 연산을 각 성분에 대해
  아래와 같이 표기할 수도 있다.

  $$c_1 = a_1 + b_1$$

  $$c_2 = a_2 + b_2$$

  $$c_3 = a_3 + b_3$$

- 혹은 더욱 요약해서

  $$c_i=a_i+b_i \text{, with } i=1,2,3$$

- 덧셈의 교환 법칙이 성립한다.

  $$\boldsymbol a + \boldsymbol b = \boldsymbol b + \boldsymbol a$$

## 5.3. 벡터와 스칼라 곱

- 벡터와 스칼라 사이의 곱은 또 다른 벡터이다.

- 스칼라와의 곱에는 연산 기호가 생략된다.

  $$\boldsymbol c= d \boldsymbol b$$

- 교환 법칙이 성립한다.

  $$d \boldsymbol b = \boldsymbol b d$$

- 양의 스칼라 값이 곱해지면, 벡터의 방향은 그대로 유지되며 그 크기만 달라진다.

- 음의 스칼라 값이 곱해지면, 벡터의 방향이 반전되며 그 크기가 달라진다.

- $d=\pm 1$일하면, $\boldsymbol c$의 크기는 $\boldsymbol b$의 크기과 같다.

## 5.4. 내적

- 두 벡터 $\boldsymbol a$ 와 $\boldsymbol b$ 사이의 내적의 결과는 스칼라이며 이를 $c$라 한다면 아래와 같이 표기된다.

  $$c = \boldsymbol a \cdot \boldsymbol b$$

- 이는 아래와 같이 연산된다.

  $$c = \boldsymbol a \cdot \boldsymbol b = | \boldsymbol a| |\boldsymbol b|\cos\theta$$

- 이때 $\theta$는 두 벡터 $\boldsymbol a$와 $\boldsymbol b$ 사이의 끼인
  각이다.

- 내적은 다음과 같이 연산될 수도 있다.

  $$c = \boldsymbol a \cdot \boldsymbol b = \sum_{i=1}^3 a_ib_i = a_1b_1+a_2b_2+a_3b_3$$

- 따라서 얻어지는 다음 두 관계는 매우 유용하다.

  $$c = \boldsymbol a \cdot \boldsymbol b = | \boldsymbol a| |\boldsymbol b|\cos\theta=\sum_{i=1}^3 a_ib_i$$

## 5.5. 외적

- 두 벡터의 외적의 결과는 또 다른 벡터이다.

  - $\boldsymbol c = \boldsymbol a \times \boldsymbol b$

  - 그리고 그 벡터의 성분은 아래와 같이 정의된다.
    - $c_1 = a_2b_3-a_3b_2$
    - $c_2 = a_3b_1-a_1b_3$
    - $c_3 = a_1b_2-a_2b_1$

## 5.6. 다이아딕 곱하기

- 두 벡터의 다이아딕 곱하기 결과는 2차 텐서이며, 3차원 벡터 둘의 다이아딕 결과은 2차 텐서를 $3\times 3$ 행렬로 표기할 수 있다.

- 두 벡터 $\boldsymbol a$와 $\boldsymbol b$의 다이아딕 연산 결과를 2차 텐서 $\boldsymbol A$라 하면, 이를 행렬로 표기할 때 다음과 같이 정의된다.

$$\boldsymbol A = \boldsymbol a \otimes \boldsymbol b$$

$$A_{ij}= a_i b_j \text{ with } (i,j)=(1,1),(1,2),(1,3),(2,1) ... (3,3)$$

$$\text{혹은}$$

$$A_{ij}= a_i b_j \text{ with } i=1,2,3 \ \ \ j=1,2,3$$

<span id="10-연습-문제"></span>

# 6. 연습 문제

## 문제 1

벡터 $\boldsymbol a=(3,4,0)$의 크기를 구하라.

<!--
풀이와 해답:
벡터의 크기는 sqrt(3^2+4^2)=5이다.
-->

## 문제 2

$\boldsymbol a=(1,0,0)$과 $\boldsymbol b=(0,2,0)$의 내적을 구하고 두 벡터의 관계를 설명하라.

<!--
풀이와 해답:
내적은 0이다. 두 벡터는 서로 수직이다.
-->

## 문제 3

$\boldsymbol a=(1,0,0)$과 $\boldsymbol b=(0,1,0)$의 외적을 구하라.

<!--
풀이와 해답:
a cross b=(0,0,1)이다.
-->


<!--
<details markdown="1">
<summary>분리 이전 절 링크 안내</summary>

이전 자료의 절 링크로 들어온 경우 아래에서 이동한 내용을 찾을 수 있다.

<span id="6-매트릭스-연산"></span>

[6. 매트릭스 연산]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#6-매트릭스-연산)

<span id="61-더하기-빼기"></span>

[6.1. 더하기, 빼기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#61-더하기-빼기)

<span id="62-스칼라-곱하기"></span>

[6.2. 스칼라 곱하기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#62-스칼라-곱하기)

<span id="63-매트릭스-곱하기1-single-contraction"></span>

[6.3. 매트릭스 곱하기1 (single contraction)]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#63-매트릭스-곱하기1-single-contraction)

<span id="64-매트릭스-곱하기2-double-contraction"></span>

[6.4. 매트릭스 곱하기2 (double contraction)]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#64-매트릭스-곱하기2-double-contraction)

<span id="65-매트릭스-전치-transpose"></span>

[6.5. 매트릭스 전치 (transpose)]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#65-매트릭스-전치-transpose)

<span id="66-매트릭스-trace"></span>

[6.6. 매트릭스 trace]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#66-매트릭스-trace)

<span id="67-역행렬-inverse-matrix"></span>

[6.7. 역행렬 (inverse matrix)]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#67-역행렬-inverse-matrix)

<span id="7-determinant"></span>

[7. Determinant]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#7-determinant)

<span id="71-2times2-행렬"></span>

[7.1. $2\times2$ 행렬]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#71-2times2-행렬)

<span id="72-3times3-행렬"></span>

[7.2. $3\times3$ 행렬]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#72-3times3-행렬)

<span id="8-랭크의-증감"></span>

[8. 랭크의 증감]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#8-랭크의-증감)

<span id="9-einstein-표기법"></span>

[9. Einstein 표기법]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#9-einstein-표기법)

<span id="텐서와-행렬-표현을-구분하기"></span>

[텐서와 행렬 표현을 구분하기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#텐서와-행렬-표현을-구분하기)

<span id="문제-4"></span>

[문제 4]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#문제-4)

<span id="추가-연습문제"></span>

[추가 연습문제]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_04b_matrix_tensor_operations.md %}#추가-연습문제)

</details>

-->