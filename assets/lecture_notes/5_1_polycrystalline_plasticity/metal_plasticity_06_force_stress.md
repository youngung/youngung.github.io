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
  - [4.1. Cauchy 면력 공식](#41-cauchy-면력-공식)
  - [4.2. 응력 텐서가 필요한 이유](#42-응력-텐서가-필요한-이유)
  - [4.3. 응력 텐서의 대칭성](#43-응력-텐서의-대칭성)
  - [4.4. 계산 예제](#44-계산-예제)
- [5. 응력 분포에서 합력 구하기](#5-응력-분포에서-합력-구하기)
- [6. 면력 방향이 변하는 경우](#6-면력-방향이-변하는-경우)
- [7. 요약](#7-요약)
- [8. 연습 문제](#8-연습-문제)
  - [8.1. 문제 1](#81-문제-1)
  - [8.2. 문제 2](#82-문제-2)
  - [8.3. 문제 3](#83-문제-3)
  - [8.4. 문제 4](#84-문제-4)
  - [8.5. 문제 5](#85-문제-5)
  - [8.6. 문제 6](#86-문제-6)
  - [8.7. 문제 7](#87-문제-7)
  - [8.8. 문제 8](#88-문제-8)
  - [8.9. 문제 9](#89-문제-9)
  - [8.10. 문제 10](#810-문제-10)
  - [8.11. 문제 11](#811-문제-11)
  - [8.12. 문제 12](#812-문제-12)
  - [8.13. 문제 13](#813-문제-13)
  - [8.14. 문제 14](#814-문제-14)
  - [8.15. 문제 15](#815-문제-15)
  - [8.16. 문제 16](#816-문제-16)

# 1. 힘

- 힘이 가해지면 운동 상태의 변화나 변형이 발생한다. 소성 역학에서 우리는 변형 발생에 초점을 둔다.

- 벡터 물리량이며, 크기(magnitude)와 방향을 가진다.

- SI 단위로 표현하면 $1\ \mathrm{N}=1\ \mathrm{kg\,m/s^2}$이다.

힘은 작용 방식에 따라 두 종류로 나눌 수 있다.

- **체적력(body force)**: 물체의 부피 전체에 작용한다. 중력과 전자기력이 예다.
- **표면력(surface force)**: 물체의 경계면이나 접촉면을 통해 전달된다. 인장시험기의
  그립력과 압연 롤의 접촉력이 예다.

한 면 전체에 작용하는 힘은 합력(resultant force)이고, 그 힘이 면에 어떻게 분포하는지는
응력으로 나타낸다.

# 2. 응력

물체 내부의 한 점을 지나는 특정 면에 작용하는 단위면적당 힘을 면력벡터
(traction vector)라 한다. 한 점에서 면의 방향에 따른 면력벡터의 관계 전체는 응력
텐서로 나타낸다. 면 전체에 면력벡터 $\boldsymbol t$가 분포하면 합력은

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
| Pa   | $\mathrm{N/m^2}$     |
| kPa  | $10^3$ Pa |
| MPa  | $10^6$ Pa   |
| GPa  | $10^9$ Pa   |

# 3. 수직 및 전단 응력

- 수직 응력: 면에 수직으로 작용하는 힘에 의한 응력

- 전단 응력: 면과 평행하게 작용하는 힘에 의한 응력
  - 가위
  - 리벳
  - 볼트
  - 전위의 슬립

수직응력과 전단응력은 서로 별개의 면력이 아니라, 한 면에 작용하는 면력벡터를 면의
법선방향과 접선방향으로 나눈 성분이다. 인장응력을 양수, 압축응력을 음수로 두는 부호
관례를 흔히 사용한다. 다음 절에서는 응력 텐서로 임의의 면에 작용하는 면력벡터를 구한
뒤 이 두 성분으로 분해한다.

# 4. 응력 텐서

- 응력은 2차 텐서이며, 선택한 좌표계에서 그 성분을 행렬로 표현할 수 있다.

$$ \boldsymbol\sigma =\begin{bmatrix}
\sigma_{11} & \sigma_{12} & \sigma_{13} \\
\sigma_{21} & \sigma_{22} & \sigma_{23} \\
\sigma_{31} & \sigma_{32} & \sigma_{33}
 \end{bmatrix}$$


- 여기서는 Cauchy 공식 $t_i=\sigma_{ij}n_j$를 사용한다. 따라서 $\sigma_{ij}$의 첫 번째
  첨자 $i$는 면력의 방향, 두 번째 첨자 $j$는 면 법선의 방향을 나타낸다. 예를 들어
  $\sigma_{12}$는 법선이 $\boldsymbol e_2$인 면에 $\boldsymbol e_1$ 방향으로 작용하는
  응력 성분이다.

## 4.1. Cauchy 면력 공식

단위법선벡터가 $\boldsymbol n$인 임의의 면에 작용하는 면력벡터는

$$
\boxed{\boldsymbol t(\boldsymbol n)=\boldsymbol\sigma\cdot\boldsymbol n}
$$

면력의 수직성분과 전단성분은 각각

$$
\sigma_n=\boldsymbol n\cdot\boldsymbol t,
\qquad
\boldsymbol t_n=\sigma_n\boldsymbol n,
\qquad
\boldsymbol t_s=\boldsymbol t-\boldsymbol t_n
$$

로 구한다. 따라서 면력벡터는

$$
\boldsymbol t=\boldsymbol t_n+\boldsymbol t_s
$$

로 분해되며, 전단응력의 크기는 $\tau=\|\boldsymbol t_s\|$이다.

![Cauchy 면력 공식과 면력벡터의 수직 및 전단 성분 분해](/assets/img/lecture_notes/stress/cauchy_traction_decomposition.png)

## 4.2. 응력 텐서가 필요한 이유

한 점의 응력상태를 알려면 서로 수직인 세 면에 작용하는 세 면력벡터를 알아야 한다.
이 아홉 성분을 배열하면 $3\times3$ 응력 행렬이 된다. 응력 텐서를 알면 Cauchy 공식으로
그 점을 지나는 **어떤 방향의 면에서도** 면력벡터를 계산할 수 있다.

반대 방향의 법선을 갖는 면에서는

$$
\boldsymbol t(-\boldsymbol n)
=\boldsymbol\sigma\cdot(-\boldsymbol n)
=-\boldsymbol t(\boldsymbol n)
$$

이다. 이는 같은 내부 절단면의 양쪽 물체에 작용하는 면력이 크기는 같고 방향은 반대라는
작용·반작용 관계와 일치한다.

## 4.3. 응력 텐서의 대칭성

우력응력(couple stress)이 없는 고전적 연속체에서는 각운동량 평형에 의해
$\boldsymbol\sigma=\boldsymbol\sigma^T$가 된다. 따라서 $\sigma_{ij}=\sigma_{ji}$이며,
$3\times3$ 응력 텐서의 독립 성분은 6개다.

## 4.4. 계산 예제

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
\boldsymbol t=\boldsymbol\sigma\cdot\boldsymbol n
=\begin{bmatrix}100\\20\\0\end{bmatrix}\ \mathrm{MPa}
$$

이다. 수직응력은 $\sigma_n=100$ MPa이고 전단응력벡터는
$\boldsymbol t_s=(0,20,0)^T$ MPa이므로 전단응력의 크기는 20 MPa이다.

# 5. 응력 분포에서 합력 구하기

앞의 계산은 한 점에서의 응력상태를 다룬다. 실제 구조물의 면에 작용하는 힘을 구하려면
면의 각 위치에서 면력을 계산한 뒤 면적 전체에 대해 적분해야 한다.

다음 그림은 전체 3차원 큐브와 우리가 선택한 $x=0$ 면을 함께 보여준다. $x=0$ 면은
$yz$ 평면에 해당하므로 면 위의 위치를 $(y,z)$로 나타낸다. 비교를 위해 주황색으로
$z=0$인 $yx$ 면도 표시하였다. 아래의 두 예제에서는 파란색으로 표시된 $x=0$ 면에
작용하는 면력을 계산한다. 첫 번째 예제에서는 모든 면력이 $x$축과 평행하고 크기만
위치에 따라 달라지며, 두 번째 예제에서는 면력의 크기는 일정하고 방향이 달라진다.

![3차원 큐브와 x=0 면 및 yx 면의 관계](/assets/img/lecture_notes/stress/surface_geometry.png)

물체 내부의 응력 텐서가 다음과 같이 $y$의 함수로 주어진다고 하자.

$$
\boldsymbol\sigma(y)=
\begin{bmatrix}
p_0\left(1+\dfrac{y}{H}\right)&0&0\\
0&0&0\\
0&0&0
\end{bmatrix}.
$$

이 응력장은 면의 아래쪽에서 $p_0$이고 위쪽에서 $2p_0$가 되는 선형적인 수직응력
분포를 뜻한다. Cauchy 공식으로 면의 위치 $(y,z)$에서 면력은

$$
\boldsymbol t(y,z)=\boldsymbol\sigma(y)\boldsymbol n
=\begin{bmatrix}
p_0\left(1+\dfrac{y}{H}\right)\\0\\0
\end{bmatrix}.
$$

![직사각형 면의 위치별 면력 분포와 미소 힘](/assets/img/lecture_notes/stress/traction_magnitude_distribution.png)

따라서 면력벡터들은 모두 $x$ 방향을 향하지만, 그 크기는 $y$에 따라 달라진다.
면적요소 $dA=dy\,dz$에 작용하는 미소 힘은

$$
d\boldsymbol F=\boldsymbol t(y,z)\,dA
$$

이고, 면 전체의 합력은

$$
\begin{aligned}
\boldsymbol F
&=\int_A\boldsymbol t\,dA\\
&=\int_0^b\int_0^H
\begin{bmatrix}p_0(1+y/H)\\0\\0\end{bmatrix}\,dy\,dz\\
&=\begin{bmatrix}\dfrac{3}{2}p_0Hb\\0\\0\end{bmatrix}.
\end{aligned}
$$

즉 평균 면력은

$$
\boldsymbol t_{avg}=\frac{\boldsymbol F}{Hb}
=\begin{bmatrix}\dfrac{3}{2}p_0\\0\\0\end{bmatrix}
$$

이다. 이 결과는 평균 응력 $1.5p_0$가 단순히 임의로 정해진 값이 아니라, 실제 면력
분포를 면적에 대해 적분한 결과임을 보여준다. 예를 들어 $p_0=10$ MPa, $H=20$ mm,
$b=30$ mm이면

$$
F_x=\frac{3}{2}(10\ \mathrm{N/mm^2})(20\ \mathrm{mm})(30\ \mathrm{mm})
=9000\ \mathrm{N}.
$$

여기서 $1\ \mathrm{MPa}=1\ \mathrm{N/mm^2}$를 사용하였다. 응력 텐서가 공간에 따라
변하면 각 위치에서 $\boldsymbol t=\boldsymbol\sigma\cdot\boldsymbol n$을 먼저 구하고,
그 결과를 적분해야 한다.

# 6. 면력 방향이 변하는 경우

이번에는 앞의 예시와 같은 $x=0$ 직사각형 면에서 면력의 크기는 일정하지만 방향이
$y$에 따라 서서히 바뀌는 경우를 생각하자. 방향각을

$$
\theta(y)=\frac{\pi}{2}\frac{y}{H}
$$

로 두면, $y=0$에서 $x$ 방향이고 $y=H$에서 $y$ 방향이 된다. 물체 내부의 대칭 응력
텐서는

$$
\boldsymbol\sigma(y)=
\begin{bmatrix}
p_0\cos\theta(y)&p_0\sin\theta(y)&0\\
p_0\sin\theta(y)&0&0\\
0&0&0
\end{bmatrix}
$$

이고, Cauchy 공식에 따라

$$
\boldsymbol t(y,z)=
\begin{bmatrix}
p_0\cos\theta(y)\\
p_0\sin\theta(y)\\0
\end{bmatrix}
$$

이다. 따라서 $\|\boldsymbol t\|=p_0$이지만, 면력의 방향은 면의 높이에 따라
회전한다.

![y 위치에 따라 방향이 변하는 면력벡터 분포](/assets/img/lecture_notes/stress/traction_direction_distribution.png)

면적요소 $dA=dy\,dz$에 작용하는 미소 힘은 $d\boldsymbol F=\boldsymbol t\,dA$이고,
면 전체의 합력은

$$
\begin{aligned}
\boldsymbol F
&=\int_0^b\int_0^H
\begin{bmatrix}p_0\cos(\pi y/2H)\\p_0\sin(\pi y/2H)\\0\end{bmatrix}\,dy\,dz\\
&=\begin{bmatrix}\dfrac{2}{\pi}p_0Hb\\\dfrac{2}{\pi}p_0Hb\\0\end{bmatrix}.
\end{aligned}
$$

따라서 합력은 $x$ 및 $y$ 방향 성분을 모두 가지며, $F_x=F_y$이므로 그 방향은 $x$와
$y$ 사이의 45°이다. $p_0=10$ MPa, $H=20$ mm, $b=30$ mm이면

$$
F_x=F_y=\frac{2}{\pi}(10\ \mathrm{N/mm^2})(20\ \mathrm{mm})(30\ \mathrm{mm})
\simeq3820\ \mathrm{N}.
$$


# 7. 요약

| 개념 | 공식 |
|------|------|
| 힘 | $\mathbf F = m\mathbf a$ |
| 응력 성분 의미 | $\sigma_{ij}$에서 $i$는 면력 방향, $j$는 면 법선 방향이며 $t_i=\sigma_{ij}n_j$ |
| 수직 및 전단응력 | 면력벡터를 면 법선과 나란한 성분과 면에 평행한 성분으로 분해 |
| 응력의 단위 | $1 Pa = 1 N/m²$ |
| 응력 텐서의 대칭성 | $\sigma_{ij}=\sigma_{ji}$, 각운동량 평형에 의한 결과 |
| Cauchy 공식 | $\boldsymbol t(\boldsymbol n)=\boldsymbol\sigma\boldsymbol n$ |

# 8. 연습 문제

## 8.1. 문제 1

단면적이 50 mm²인 면에 수직방향으로 5000 N의 힘이 작용한다. 수직응력을 구하라.

<!--
풀이와 해답:
응력은 5000/50=100 N/mm²=100 MPa이다.
-->

## 8.2. 문제 2

면에 평행하게 작용하는 단위면적당 힘을 무엇이라고 하는가?

<!--
풀이와 해답:
전단응력(shear stress)이라고 한다.
-->

## 8.3. 문제 3

응력 텐서 $\boldsymbol\sigma$와 단위법선벡터 $\boldsymbol n$으로 면력벡터를 나타내라.

<!--
풀이와 해답:
Cauchy 공식에 따라 t(n)=sigma n이다.
-->

## 8.4. 문제 4

각운동량 평형을 만족하는 고전적 연속체에서 응력 텐서가 갖는 대칭성을 쓰시오.

<!--
풀이와 해답:
sigma_ij=sigma_ji이므로 응력 텐서는 대칭이다.
-->

## 8.5. 문제 5

단면적이 $120\ \mathrm{mm^2}$인 봉에 12 kN의 균일한 인장력이 작용한다. 평균
수직응력을 구하시오.

<!--
풀이와 해답:
12 kN=12000 N이다. 평균응력은 12000/120=100 N/mm^2=100 MPa이다.
인장이므로 양의 부호를 사용한다.
-->

## 8.6. 문제 6

단면적이 $40\ \mathrm{mm^2}$인 봉에 8 kN의 균일한 압축력이 작용한다. 인장을 양수로
두었을 때 평균 수직응력을 구하시오.

<!--
풀이와 해답:
8 kN=8000 N이고 응력의 크기는 8000/40=200 MPa이다.
압축이므로 평균 수직응력은 -200 MPa이다.
-->

## 8.7. 문제 7

면적이 $25\ \mathrm{mm^2}$인 면에 평행하게 3000 N의 힘이 균일하게 작용한다.
평균 전단응력을 구하시오.

<!--
풀이와 해답:
평균 전단응력은 3000/25=120 N/mm^2=120 MPa이다.
-->

## 8.8. 문제 8

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

## 8.9. 문제 9

본문 계산 예제의 응력 텐서에서 법선이
$\boldsymbol n=(0,1,0)^T$인 면의 면력벡터를 구하시오.

<!--
풀이와 해답:
t=sigma n은 응력 행렬의 두 번째 열이므로 t=(20,60,0)^T MPa이다.
-->

## 8.10. 문제 10

문제 9의 면력벡터를 수직성분과 전단성분으로 분해하고 전단응력의 크기를 구하시오.

<!--
풀이와 해답:
sigma_n=n dot t=60 MPa이고 t_n=(0,60,0)^T MPa이다.
t_s=t-t_n=(20,0,0)^T MPa이므로 전단응력의 크기는 20 MPa이다.
-->

## 8.11. 문제 11

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

## 8.12. 문제 12

문제 11에서 면의 수직응력과 전단응력의 크기를 구하시오.

<!--
풀이와 해답:
sigma_n=n dot t=(120+40)/2=80 MPa이다.
t_n=80n이고 t_s=t-t_n=(40/sqrt(2),-40/sqrt(2),0)^T MPa이다.
따라서 전단응력의 크기는 sqrt(40^2/2+40^2/2)=40 MPa이다.
-->

## 8.13. 문제 13

한 면의 법선 $\boldsymbol n$에 대한 면력이
$\boldsymbol t(\boldsymbol n)=(30,-10,5)^T$ MPa이다. 반대쪽 면의 법선
$-\boldsymbol n$에 대한 면력을 구하시오.

<!--
풀이와 해답:
t(-n)=-t(n)이므로 (-30,10,-5)^T MPa이다.
-->

## 8.14. 문제 14

대칭 응력 텐서에서 $\sigma_{12}=35$ MPa, $\sigma_{13}=-10$ MPa,
$\sigma_{23}=8$ MPa이다. $\sigma_{21}$, $\sigma_{31}$, $\sigma_{32}$를 구하시오.

<!--
풀이와 해답:
응력 텐서의 대칭성에 따라 sigma_21=35 MPa, sigma_31=-10 MPa,
sigma_32=8 MPa이다.
-->

## 8.15. 문제 15

응력 텐서가 주어졌을 때 법선방향이 다른 면의 면력벡터도 계산할 수 있는 이유를 Cauchy
공식을 사용해 설명하시오.

<!--
풀이와 해답:
응력 텐서는 한 점의 면 방향에 따른 응력정보를 포함하며, 임의의 단위법선 n을
t(n)=sigma n에 대입하면 그 면의 면력벡터를 얻을 수 있기 때문이다.
-->

## 8.16. 문제 16

응력의 단위 MPa를 $\mathrm{N/mm^2}$로 나타내시오.

<!--
풀이와 해답:
1 MPa=10^6 N/m^2이고 1 m^2=10^6 mm^2이므로 1 MPa=1 N/mm^2이다.
-->
