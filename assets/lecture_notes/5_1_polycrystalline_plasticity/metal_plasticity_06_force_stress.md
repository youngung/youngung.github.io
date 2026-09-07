---
layout: distill
title: 힘과 응력
description: 면에 작용하는 힘과 Cauchy 응력 텐서
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

- [1. 힘](#1-힘)
- [2. 응력](#2-응력)
- [3. 수직 및 전단 응력](#3-수직-및-전단-응력)
- [4. 응력 텐서](#4-응력-텐서)
- [5. 요약](#5-요약)
- [6. 연습 문제](#6-연습-문제)

# 1. 힘

- 힘이 가해지면 운동 상태의 변화나 변형이 발생한다. 소성 역학에서 우리는 변형 발생에 초점을 둔다.

- 벡터 물리량이며, 크기(magnitude)와 방향성 가진다.

- SI 단위로 표현하면 $[N]=[kg m/s^2]$

힘은 작용 방식에 따라 두 종류로 나눌 수 있다.

- **체적력(body force)**: 물체의 부피 전체에 작용한다. 중력과 전자기력이 예다.
- **표면력(surface force)**: 물체의 경계면이나 접촉면을 통해 전달된다. 인장시험기의
  그립력과 압연 롤의 접촉력이 예다.

한 면 전체에 작용하는 힘은 합력(resultant force)이고, 그 힘이 면에 어떻게 분포하는지는
응력으로 나타낸다.

# 2. 응력

- 응력은 물체 내부의 한 점을 지나는 면에 작용하는 단위면적당 힘을 나타낸다. 면 전체에
  면력벡터 $\boldsymbol t$가 분포하면 합력은

$$
\boldsymbol F=\int_A\boldsymbol t\,dA
$$

이다. 면력이 균일할 때만 평균 면력은

$$
\boldsymbol t_{avg}=\frac{\boldsymbol F}{A}
$$

로 단순화된다. 면적 $A$는 스칼라이므로 이는 벡터를 스칼라로 나누는 연산이다.

응력 텐서 $\boldsymbol\sigma$ 자체는 단순히 ‘힘 벡터를 면적 벡터로 나눈 값’이 아니다.
같은 점에서도 선택한 면의 법선방향에 따라 면력벡터가 달라지며, 그 관계 전체를 응력
텐서가 나타낸다.

- 단위

| 단위 | 의미     |
| ---- | -------- |
| Pa   | N/m²     |
| kPa  | 1,000 Pa |
| MPa  | 10⁶ Pa   |
| GPa  | 10⁹ Pa   |

# 3. 수직 및 전단 응력

- 수직 응력: 면에 수직으로 작용하는 힘에 의한 응력

- 전단 응력: 면과 평행하게 작용하는 힘에 의한 응력
  - 가위
  - 리벳
  - 볼트
  - 전위의 슬립

인장응력을 양수, 압축응력을 음수로 두는 부호 관례를 흔히 사용한다. 예를 들어 면의
바깥쪽으로 당기는 수직 면력은 양의 수직응력이고, 면을 안쪽으로 누르는 면력은 음의
수직응력이다. 사용하는 교재나 해석 프로그램의 부호 관례를 먼저 확인해야 한다.

임의의 면력벡터 $\boldsymbol t$와 단위법선벡터 $\boldsymbol n$이 주어지면 수직응력과
전단응력벡터는

$$
\sigma_n=\boldsymbol t\cdot\boldsymbol n,
\qquad
\boldsymbol t_n=\sigma_n\boldsymbol n,
\qquad
\boldsymbol t_s=\boldsymbol t-\boldsymbol t_n
$$

이다. 전단응력의 크기는 $\tau=\|\boldsymbol t_s\|$로 구한다. 따라서 면력벡터는

$$
\boldsymbol t=\boldsymbol t_n+\boldsymbol t_s
$$

로 분해된다.

# 4. 응력 텐서

- 응력은 2차 텐서이며, 선택한 좌표계에서 그 성분을 행렬로 표현할 수 있다.

$$ \sigma =\begin{bmatrix}
\sigma_{11} & \sigma_{12} & \sigma_{13} \\
\sigma_{21} & \sigma_{22} & \sigma_{23} \\
\sigma_{31} & \sigma_{32} & \sigma_{33}
 \end{bmatrix}$$


- 여기서는 Cauchy 공식 $t_i=\sigma_{ij}n_j$를 사용한다. 따라서 $\sigma_{ij}$의 첫 번째
  첨자 $i$는 면력의 방향, 두 번째 첨자 $j$는 면 법선의 방향을 나타낸다. 예를 들어
  $\sigma_{12}$는 법선이 $\boldsymbol e_2$인 면에 $\boldsymbol e_1$ 방향으로 작용하는
  응력 성분이다.

## Cauchy 면력 공식

단위법선벡터가 $\boldsymbol n$인 임의의 면에 작용하는 단위면적당 힘을 면력벡터
(traction vector)라 한다.

$$
\boxed{\boldsymbol t(\boldsymbol n)=\boldsymbol\sigma\boldsymbol n}
$$

면력의 수직성분과 전단성분은 각각

$$
\sigma_n=\boldsymbol n\cdot\boldsymbol t,
\qquad
\boldsymbol t_s=\boldsymbol t-\sigma_n\boldsymbol n
$$

로 구한다. 고전적 연속체에서 체적 couple이 없으면 각운동량 평형으로부터
$\boldsymbol\sigma=\boldsymbol\sigma^T$가 되어 독립 응력성분은 6개다.

## 응력 텐서가 필요한 이유

한 점의 응력상태를 알려면 서로 수직인 세 면에 작용하는 세 면력벡터를 알아야 한다.
이 아홉 성분을 배열하면 $3\times3$ 응력 행렬이 된다. 응력 텐서를 알면 Cauchy 공식으로
그 점을 지나는 **어떤 방향의 면에서도** 면력벡터를 계산할 수 있다.

반대 방향의 법선을 갖는 면에서는

$$
\boldsymbol t(-\boldsymbol n)
=\boldsymbol\sigma(-\boldsymbol n)
=-\boldsymbol t(\boldsymbol n)
$$

이다. 이는 같은 내부 절단면의 양쪽 물체에 작용하는 면력이 크기는 같고 방향은 반대라는
작용·반작용 관계와 일치한다.

## 계산 예제

다음 응력상태를 생각하자.

$$
\boldsymbol\sigma=
\begin{bmatrix}
100&20&0\\
20&60&0\\
0&0&40
\end{bmatrix}\ \mathrm{MPa}
$$

법선이 $\boldsymbol n=(1,0,0)^T$인 면의 면력벡터는

$$
\boldsymbol t=\boldsymbol\sigma\boldsymbol n
=\begin{bmatrix}100\\20\\0\end{bmatrix}\ \mathrm{MPa}
$$

이다. 수직응력은 $\sigma_n=100$ MPa이고 전단응력벡터는
$\boldsymbol t_s=(0,20,0)^T$ MPa이므로 전단응력의 크기는 20 MPa이다.


# 5. 요약

| 개념 | 공식 |
|------|------|
| 힘 | $\mathbf F = m\mathbf a$ |
| 응력 성분 의미 | $\sigma_{ij}$에서 $i$는 면력 방향, $j$는 면 법선 방향이며 $t_i=\sigma_{ij}n_j$ |
| 수직 및 전단응력 | 면력벡터를 면 법선과 나란한 성분과 면에 평행한 성분으로 분해 |
| 응력의 단위 | $1 Pa = 1 N/m²$ |
| 전단응력의 대칭성 | $\sigma_{12} = \sigma_{21}$ 모멘트(힘) 평형에 의한 결과|
| Cauchy 공식 | $\boldsymbol t(\boldsymbol n)=\boldsymbol\sigma\boldsymbol n$ |

# 6. 연습 문제

## 문제 1

단면적이 50 mm²인 면에 수직방향으로 5000 N의 힘이 작용한다. 수직응력을 구하라.

<!--
풀이와 해답:
응력은 5000/50=100 N/mm²=100 MPa이다.
-->

## 문제 2

면에 평행하게 작용하는 단위면적당 힘을 무엇이라고 하는가?

<!--
풀이와 해답:
전단응력(shear stress)이라고 한다.
-->

## 문제 3

응력 텐서 $\boldsymbol\sigma$와 단위법선벡터 $\boldsymbol n$으로 면력벡터를 나타내라.

<!--
풀이와 해답:
Cauchy 공식에 따라 t(n)=sigma n이다.
-->

## 문제 4

각운동량 평형을 만족하는 고전적 연속체에서 응력 텐서가 갖는 대칭성을 쓰시오.

<!--
풀이와 해답:
sigma_ij=sigma_ji이므로 응력 텐서는 대칭이다.
-->

## 문제 5

단면적이 $120\ \mathrm{mm^2}$인 봉에 12 kN의 균일한 인장력이 작용한다. 평균
수직응력을 구하시오.

<!--
풀이와 해답:
12 kN=12000 N이다. 평균응력은 12000/120=100 N/mm^2=100 MPa이다.
인장이므로 양의 부호를 사용한다.
-->

## 문제 6

단면적이 $40\ \mathrm{mm^2}$인 봉에 8 kN의 균일한 압축력이 작용한다. 인장을 양수로
두었을 때 평균 수직응력을 구하시오.

<!--
풀이와 해답:
8 kN=8000 N이고 응력의 크기는 8000/40=200 MPa이다.
압축이므로 평균 수직응력은 -200 MPa이다.
-->

## 문제 7

면적이 $25\ \mathrm{mm^2}$인 면에 평행하게 3000 N의 힘이 균일하게 작용한다.
평균 전단응력을 구하시오.

<!--
풀이와 해답:
평균 전단응력은 3000/25=120 N/mm^2=120 MPa이다.
-->

## 문제 8

다음 응력 텐서에서 수직응력 성분과 서로 독립인 전단응력 성분을 쓰시오.

$$
\boldsymbol\sigma=
\begin{bmatrix}
80&15&0\\
15&50&5\\
0&5&30
\end{bmatrix}\ \mathrm{MPa}
$$

<!--
풀이와 해답:
수직응력은 sigma_11=80, sigma_22=50, sigma_33=30 MPa이다.
독립 전단응력은 sigma_12=15, sigma_13=0, sigma_23=5 MPa이다.
-->

## 문제 9

본문 계산 예제의 응력 텐서에서 법선이
$\boldsymbol n=(0,1,0)^T$인 면의 면력벡터를 구하시오.

<!--
풀이와 해답:
t=sigma n은 응력 행렬의 두 번째 열이므로 t=(20,60,0)^T MPa이다.
-->

## 문제 10

문제 9의 면력벡터를 수직성분과 전단성분으로 분해하고 전단응력의 크기를 구하시오.

<!--
풀이와 해답:
sigma_n=n dot t=60 MPa이고 t_n=(0,60,0)^T MPa이다.
t_s=t-t_n=(20,0,0)^T MPa이므로 전단응력의 크기는 20 MPa이다.
-->

## 문제 11

다음 응력상태에서 법선이
$\boldsymbol n=(1/\sqrt{2},1/\sqrt{2},0)^T$인 면의 면력벡터를 구하시오.

$$
\boldsymbol\sigma=
\begin{bmatrix}
120&0&0\\
0&40&0\\
0&0&0
\end{bmatrix}\ \mathrm{MPa}
$$

<!--
풀이와 해답:
t=sigma n=(120/sqrt(2),40/sqrt(2),0)^T MPa이다.
-->

## 문제 12

문제 11에서 면의 수직응력과 전단응력의 크기를 구하시오.

<!--
풀이와 해답:
sigma_n=n dot t=(120+40)/2=80 MPa이다.
t_n=80n이고 t_s=t-t_n=(40/sqrt(2),-40/sqrt(2),0)^T MPa이다.
따라서 전단응력의 크기는 sqrt(40^2/2+40^2/2)=40 MPa이다.
-->

## 문제 13

한 면의 법선 $\boldsymbol n$에 대한 면력이
$\boldsymbol t(\boldsymbol n)=(30,-10,5)^T$ MPa이다. 반대쪽 면의 법선
$-\boldsymbol n$에 대한 면력을 구하시오.

<!--
풀이와 해답:
t(-n)=-t(n)이므로 (-30,10,-5)^T MPa이다.
-->

## 문제 14

대칭 응력 텐서에서 $\sigma_{12}=35$ MPa, $\sigma_{13}=-10$ MPa,
$\sigma_{23}=8$ MPa이다. $\sigma_{21}$, $\sigma_{31}$, $\sigma_{32}$를 구하시오.

<!--
풀이와 해답:
응력 텐서의 대칭성에 따라 sigma_21=35 MPa, sigma_31=-10 MPa,
sigma_32=8 MPa이다.
-->

## 문제 15

응력 텐서가 주어졌을 때 법선방향이 다른 면의 면력벡터도 계산할 수 있는 이유를 Cauchy
공식을 사용해 설명하시오.

<!--
풀이와 해답:
응력 텐서는 한 점의 면 방향에 따른 응력정보를 포함하며, 임의의 단위법선 n을
t(n)=sigma n에 대입하면 그 면의 면력벡터를 얻을 수 있기 때문이다.
-->

## 문제 16

응력의 단위 MPa를 $\mathrm{N/mm^2}$로 나타내시오.

<!--
풀이와 해답:
1 MPa=10^6 N/m^2이고 1 m^2=10^6 mm^2이므로 1 MPa=1 N/mm^2이다.
-->
