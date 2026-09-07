---
layout: distill
title: 벡터와 행렬 연습문제
description: 벡터와 행렬의 기본 연산 연습
target: 학부 고학년
permalink:
featured: true
prerequisite: 벡터와 행렬
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

# 1. 다음 두 벡터가 있다. 두 벡터간의 연산 결과를 답하시오.

$$
\boldsymbol a=\begin{bmatrix}2\\2\\-1\end{bmatrix}
$$

$$
\boldsymbol b=\begin{bmatrix}2\\-3\\1\end{bmatrix}
$$

## 1.1. $\boldsymbol a + \boldsymbol b$

<!-- 풀이와 해답: (4,-1,0)^T -->

## 1.2. $\boldsymbol a - \boldsymbol b$

<!-- 풀이와 해답: (0,5,-2)^T -->

## 1.3. $\boldsymbol a \cdot \boldsymbol b$

<!-- 풀이와 해답: -3 -->

## 1.4. $\boldsymbol b - \boldsymbol a$

<!-- 풀이와 해답: (0,-5,2)^T -->

## 1.5. $\boldsymbol a \otimes \boldsymbol b$

<!-- 풀이와 해답: [[4,-6,2],[4,-6,2],[-2,3,-1]] -->

## 1.6. $\boldsymbol b \otimes \boldsymbol a$

<!-- 풀이와 해답: [[4,4,-2],[-6,-6,3],[2,2,-1]] -->

## 1.7. $\boldsymbol b \times \boldsymbol a$

<!-- 풀이와 해답: (1,4,10)^T -->

## 1.8. $\boldsymbol a \times \boldsymbol b$

<!-- 풀이와 해답: (-1,-4,-10)^T -->


## 1.9. $|\boldsymbol a| |\boldsymbol b|$

<!-- 풀이와 해답: 3 sqrt(14) -->

## 1.10. $|\boldsymbol a\cdot \boldsymbol b|$

<!-- 풀이와 해답: 3 -->

# 2. 다음 두 행렬이 있다. 두 행렬간의 연산 결과를 답하시오.



$$
\boldsymbol A=\begin{bmatrix}
 1& 1& -1 \\
 3& 4& -4 \\
 3& 1&  2 \\
\end{bmatrix}
$$

$$
\boldsymbol B=\begin{bmatrix}
  1 &  1& -1 \\
 -1 & -2& -4 \\
 -2 &  2&  2\\
\end{bmatrix}
$$

## 2.1. $\boldsymbol A+ \boldsymbol B$

<!-- 풀이와 해답: [[2,2,-2],[2,2,-8],[1,3,4]] -->

## 2.2. $\boldsymbol A- \boldsymbol B$

<!-- 풀이와 해답: [[0,0,0],[4,6,0],[5,-1,0]] -->

## 2.3. $\boldsymbol B- \boldsymbol A$

<!-- 풀이와 해답: [[0,0,0],[-4,-6,0],[-5,1,0]] -->

## 2.4. $\boldsymbol A \cdot \boldsymbol B$

<!-- 풀이와 해답: [[2,-3,-7],[7,-13,-27],[-2,5,-3]] -->

## 2.5. $\boldsymbol B \cdot \boldsymbol A$

<!-- 풀이와 해답: [[1,4,-7],[-19,-13,1],[10,8,-2]] -->

## 2.6. $\boldsymbol A : \boldsymbol B$

<!-- 풀이와 해답: 같은 위치의 성분을 곱해 모두 더하면 8이다. -->

## 2.7. $\boldsymbol B : \boldsymbol A$

<!-- 풀이와 해답: double contraction은 이 경우 교환 가능하므로 8이다. -->

# 3. 소성역학에 적용하기

## 3.1. 면력벡터

응력 텐서와 단위법선벡터가 다음과 같을 때
$\boldsymbol t=\boldsymbol\sigma\boldsymbol n$을 구하시오.

$$
\boldsymbol\sigma=
\begin{bmatrix}
100&20&0\\
20&50&0\\
0&0&30
\end{bmatrix}\ \mathrm{MPa},
\qquad
\boldsymbol n=
\begin{bmatrix}1\\0\\0\end{bmatrix}
$$

<!-- 풀이와 해답: t=(100,20,0)^T MPa이다. -->

## 3.2. 응력의 trace

문제 3.1의 응력 텐서에 대해 $\operatorname{tr}(\boldsymbol\sigma)$와 평균응력
$\sigma_m=\operatorname{tr}(\boldsymbol\sigma)/3$을 구하시오.

<!-- 풀이와 해답: trace는 180 MPa이고 평균응력은 60 MPa이다. -->

## 3.3. 단위부피당 일 증분

$$
\boldsymbol\sigma=
\begin{bmatrix}100&0\\0&50\end{bmatrix}\ \mathrm{MPa},
\qquad
d\boldsymbol\varepsilon=
\begin{bmatrix}0.001&0\\0&-0.0002\end{bmatrix}
$$

일 때 $dW=\boldsymbol\sigma:d\boldsymbol\varepsilon$을 구하시오.

<!-- 풀이와 해답: dW=100(0.001)+50(-0.0002)=0.09 MPa=0.09 MJ/m^3이다. -->

# 4. 벡터의 크기, 방향과 투영

- 이 절에서는 앞에서 주어진

  $$
  \boldsymbol a=
  \begin{bmatrix}2\\2\\-1\end{bmatrix},

  \qquad
  \boldsymbol b=
  \begin{bmatrix}2\\-3\\1\end{bmatrix}
  $$

  를 계속 사용한다.

## 4.1. 벡터의 크기

- $|\boldsymbol a |$ 와 $| \boldsymbol b|$ 를 각각 구하시오.

<!--
풀이와 해답:
|a|=sqrt(2^2+2^2+(-1)^2)=3이고,
|b|=sqrt(2^2+(-3)^2+1^2)=sqrt(14)이다.
-->

## 4.2. 단위벡터

$\boldsymbol a$와 같은 방향의 단위벡터 $\widehat{\boldsymbol a}$를 구하시오.

<!--
풀이와 해답:
a를 |a|=3으로 나누면 ahat=(2/3,2/3,-1/3)^T이다.
-->

## 4.3. 두 벡터 사이의 각

$\boldsymbol a$와 $\boldsymbol b$ 사이의 각 $\theta$에 대해 $\cos\theta$를 구하시오.
두 벡터가 이루는 각은 예각인가, 둔각인가?

<!--
풀이와 해답:
cos(theta)=(a dot b)/(|a||b|)=-3/(3 sqrt(14))=-1/sqrt(14)이다.
cos(theta)가 음수이므로 두 벡터가 이루는 각은 둔각이다.
-->

## 4.4. 수직 여부 확인

다음 벡터 $\boldsymbol c$가 $\boldsymbol a$와 수직인지 내적으로 확인하시오.

$$
\boldsymbol c=\begin{bmatrix}1\\0\\2\end{bmatrix}
$$

<!--
풀이와 해답:
a dot c=2(1)+2(0)+(-1)(2)=0이므로 서로 수직이다.
-->

## 4.5. 벡터 투영

$\boldsymbol a$를 $\boldsymbol b$ 방향으로 투영한 벡터
$\operatorname{proj}_{\boldsymbol b}\boldsymbol a$를 구하시오.

$$
\operatorname{proj}_{\boldsymbol b}\boldsymbol a
=\frac{\boldsymbol a\cdot\boldsymbol b}
{\boldsymbol b\cdot\boldsymbol b}\boldsymbol b
$$

<!--
풀이와 해답:
a dot b=-3이고 b dot b=14이므로 (-3/14)b이다.
따라서 투영벡터는 (-3/7,9/14,-3/14)^T이다.
-->

## 4.6. 외적의 기하학적 의미

$\boldsymbol a$와 $\boldsymbol b$가 만드는 평행사변형의 넓이를 구하시오.

<!--
풀이와 해답:
평행사변형의 넓이는 |a cross b|이다.
a cross b=(-1,-4,-10)^T이므로 넓이는 sqrt(1+16+100)=sqrt(117)=3sqrt(13)이다.
-->

# 5. 행렬의 기본 성질

이 절에서는 앞에서 주어진 행렬 $\boldsymbol A$와 $\boldsymbol B$를 계속 사용한다.

## 5.1. 전치행렬

$\boldsymbol A^T$를 구하시오.

<!--
풀이와 해답:
A^T=[[1,3,3],[1,4,1],[-1,-4,2]]이다.
-->

## 5.2. Trace

$\operatorname{tr}(\boldsymbol A)$와 $\operatorname{tr}(\boldsymbol B)$를 구하시오.

<!--
풀이와 해답:
대각성분을 더하면 tr(A)=1+4+2=7이고 tr(B)=1-2+2=1이다.
-->

## 5.3. Determinant

$\det\boldsymbol A$와 $\det\boldsymbol B$를 구하시오. 두 행렬의 역행렬이 존재하는지도
판단하시오.

<!--
풀이와 해답:
det(A)=3이고 det(B)=20이다. 두 determinant가 모두 0이 아니므로 두 행렬 모두
역행렬이 존재한다.
-->

## 5.4. 행렬곱의 교환법칙

앞에서 구한 $\boldsymbol A\boldsymbol B$와 $\boldsymbol B\boldsymbol A$를 비교하여
행렬곱에 교환법칙이 성립하는지 설명하시오.

<!--
풀이와 해답:
A B와 B A의 성분이 서로 다르므로 일반적인 행렬곱에는 교환법칙이 성립하지 않는다.
-->

## 5.5. 단위행렬

$3\times3$ 단위행렬을 $\boldsymbol I$라 할 때
$\boldsymbol A\boldsymbol I$와 $\boldsymbol I\boldsymbol A$를 구하시오.

<!--
풀이와 해답:
단위행렬의 성질에 의해 A I=I A=A이다.
-->

## 5.6. 대칭부분과 반대칭부분

행렬 $\boldsymbol A$를 다음과 같이 대칭부분 $\boldsymbol A^{sym}$과 반대칭부분
$\boldsymbol A^{skw}$로 분해하시오.

$$
\boldsymbol A^{sym}=\frac{1}{2}(\boldsymbol A+\boldsymbol A^T),
\qquad
\boldsymbol A^{skw}=\frac{1}{2}(\boldsymbol A-\boldsymbol A^T)
$$

<!--
풀이와 해답:
A_sym=[[1,2,1],[2,4,-1.5],[1,-1.5,2]]이고,
A_skw=[[0,-1,-2],[1,0,-2.5],[2,2.5,0]]이다.
두 행렬을 더하면 원래 A가 된다.
-->

# 6. 응력과 변형률 텐서에 적용하기

## 6.1. 수직응력과 전단응력 구분

다음 응력 텐서에서 수직응력 성분과 서로 독립적인 전단응력 성분을 각각 쓰시오.

$$
\boldsymbol\sigma=
\begin{bmatrix}
120&30&0\\
30&80&10\\
0&10&50
\end{bmatrix}\ \mathrm{MPa}
$$

<!--
풀이와 해답:
수직응력은 sigma_11=120, sigma_22=80, sigma_33=50 MPa이다.
독립 전단응력은 sigma_12=30, sigma_13=0, sigma_23=10 MPa이다.
-->

## 6.2. 임의 면의 면력벡터

문제 6.1의 응력 텐서와
$\boldsymbol n=(0,1,0)^T$에 대해
$\boldsymbol t=\boldsymbol\sigma\boldsymbol n$을 구하시오.

<!--
풀이와 해답:
행렬에 n을 곱하면 두 번째 열이 선택되므로 t=(30,80,10)^T MPa이다.
-->

## 6.3. 면력의 수직성분과 전단성분

문제 6.2에서 구한 면력벡터를 면의 수직성분
$\boldsymbol t_n$과 전단성분 $\boldsymbol t_s$로 나누시오.

<!--
풀이와 해답:
sigma_n=n dot t=80 MPa이므로 t_n=sigma_n n=(0,80,0)^T MPa이다.
t_s=t-t_n=(30,0,10)^T MPa이다.
-->

## 6.4. 평균응력과 편차응력

다음 응력상태의 평균응력과 편차응력 텐서를 구하시오.

$$
\boldsymbol\sigma=
\begin{bmatrix}
90&0&0\\
0&60&0\\
0&0&30
\end{bmatrix}\ \mathrm{MPa}
$$

<!--
풀이와 해답:
평균응력은 (90+60+30)/3=60 MPa이다.
편차응력은 s=sigma-60I=diag(30,0,-30) MPa이다.
편차응력의 trace는 0이다.
-->

## 6.5. von Mises 등가응력

문제 6.4의 주응력을 이용하여 von Mises 등가응력을 구하시오.

$$
\sigma^{VM}=\sqrt{\frac{1}{2}
\left[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2
+(\sigma_3-\sigma_1)^2\right]}
$$

<!--
풀이와 해답:
sigma_VM=sqrt{[(90-60)^2+(60-30)^2+(30-90)^2]/2}
=sqrt(2700)=30sqrt(3), 즉 약 51.96 MPa이다.
-->

## 6.6. 정수압 응력의 von Mises 응력

$\boldsymbol\sigma=100\boldsymbol I$ MPa일 때 편차응력과 von Mises 등가응력을
구하시오.

<!--
풀이와 해답:
평균응력이 100 MPa이므로 편차응력은 100I-100I=0이다.
따라서 von Mises 등가응력도 0 MPa이다.
-->

## 6.7. 탄성 일에 대한 이중수축

응력과 탄성변형률이 다음과 같을 때
$W=\frac{1}{2}\boldsymbol\sigma:\boldsymbol\varepsilon^{el}$을 구하시오.

$$
\boldsymbol\sigma=
\begin{bmatrix}200&0\\0&100\end{bmatrix}\ \mathrm{MPa},
\qquad
\boldsymbol\varepsilon^{el}=
\begin{bmatrix}0.001&0\\0&0.0005\end{bmatrix}
$$

<!--
풀이와 해답:
sigma:epsilon=200(0.001)+100(0.0005)=0.25 MPa이다.
따라서 W=0.5(0.25)=0.125 MPa=0.125 MJ/m^3이다.
-->
