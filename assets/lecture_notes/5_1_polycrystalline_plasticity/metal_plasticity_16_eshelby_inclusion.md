---
layout: distill
title: Eshelby inclusion 문제
description: 고유변형률을 갖는 타원체 inclusion의 탄성장과 Eshelby tensor
target: 학부 고학년 및 대학원 입문
permalink:
featured: true
prerequisite: 응력과 변형률, 선형 탄성, 텐서와 좌표변환
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

- [1. 왜 Eshelby 문제를 배우는가?](#1-왜-eshelby-문제를-배우는가)
- [2. Inclusion, inhomogeneity, eigenstrain](#2-inclusion-inhomogeneity-eigenstrain)
- [3. Eshelby의 사고실험](#3-eshelby의-사고실험)
- [4. 지배방정식](#4-지배방정식)
- [5. Eshelby의 핵심 결과](#5-eshelby의-핵심-결과)
- [6. 등방성 기지 속 구형 inclusion](#6-등방성-기지-속-구형-inclusion)
- [7. 체적 고유변형률 계산 예제](#7-체적-고유변형률-계산-예제)
- [8. Inclusion과 inhomogeneity의 연결](#8-inclusion과-inhomogeneity의-연결)
- [9. 적용과 한계](#9-적용과-한계)
  - [주요 적용](#주요-적용)
  - [고전 해의 주요 가정](#고전-해의-주요-가정)
- [10. 요약](#10-요약)
- [11. 연습 문제](#11-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
- [참고문헌](#참고문헌)

# 1. 왜 Eshelby 문제를 배우는가?

석출물, 상변태 영역, 열팽창 불일치, 전위 주변의 소성변형과 같이 재료 내부의 한
영역이 주변과 다른 **자유 변형**을 하려고 하면, 주변 재료의 구속 때문에 내부응력이
발생한다. Eshelby inclusion 문제는 이와 같은 불일치 변형이 만드는 탄성장과
잔류응력을 구하는 미세역학(micromechanics)의 기본 문제다.

특히 타원체 영역에 균일한 고유변형률이 주어지면 inclusion 내부의 변형률이 균일하다는
결과가 중요하다.

# 2. Inclusion, inhomogeneity, eigenstrain

세 용어를 먼저 구분해야 한다.

- **고유변형률(eigenstrain)** $\boldsymbol\varepsilon^*$: 주변의 구속이 없다면 해당
  영역이 응력 없이 가지려는 변형률이다. 열변형률, 상변태 변형률, 소성변형률 등이
  예다. (변형률 텐서의 주 변형률과 다른 개념이다. 혼동하지 말아야 한다.)
- **Inclusion**: 기지(matrix)와 탄성계수는 같지만, 지정된 고유변형률을 갖는 영역이다.
- **Inhomogeneity**: 기지와 탄성계수가 다른 영역이다. 실제 석출물이나 강화입자는 보통
  고유변형률과 탄성계수 차이를 모두 가질 수 있다.

전체 미소변형률을

$$
\boldsymbol\varepsilon
=\boldsymbol\varepsilon^e+\boldsymbol\varepsilon^*
$$

로 분해하면 응력을 **탄성변형률**에 대한 함수로 표현할 수 있다.

$$
\boxed{
\boldsymbol\sigma
=\boldsymbol C:(\boldsymbol\varepsilon-\boldsymbol\varepsilon^*)}
\tag{1}
$$

여기서 $\boldsymbol C$는 4차 탄성계수 텐서다. 고유변형률 자체는 응력이 아니며, 공간적으로
양립하지 않거나 주변 재료에 의해 구속될 때 응력을 만든다.

# 3. Eshelby의 사고실험

Eshelby 문제는 다음의 가상적인 절단--변형--용접 과정으로 이해할 수 있다.

1. 무한히 큰 탄성체 매질(medium)에서 inclusion 영역($\Omega$)을 잘라낸다.
2. 잘라낸 영역에 고유변형률 $\boldsymbol\varepsilon^*$를 **응력 없이** 발생시킨다.
3. 변형된 영역이, inclusion을 잘라내고 남은 공동(cavity)에 맞도록 가상의 표면력(fictitious traction)을 가한다.
4. 영역을 기지에 다시 용접한 뒤 가상의 표면력을 제거한다 - 그에 따라 내부 응력이 발생하고 최종 변형률이 $\boldsymbol\varepsilon^{*}$와 달라진다.
5. inclusion과 기지가 함께 **힘평형**을 이루면서 구속변형률과 잔류응력이 생긴다.

![Eshelby inclusion 문제의 절단, 자유변형, 재결합 및 평형화 과정](/assets/img/lecture_notes/micromechanics/eshelby_inclusion_process.png)

그림의 원은 이해를 위한 2차원 표현이다. 고전적인 해는 3차원 무한 탄성체 속
타원체(ellipsoid)를 대상으로 한다.

# 4. 지배방정식

체적력(body force)이 없고 정적 평형상태라면

$$
\nabla\cdot\boldsymbol\sigma=\boldsymbol 0
$$

즉

$$
\sum_j^3\sigma_{ij}n_j=0\  \text{ with\ } i=1,2,3
$$

이다. 변위 $\boldsymbol u$로부터 전체 변형률은

$$
\boldsymbol\varepsilon
=\frac{1}{2}\left(\nabla\boldsymbol u+
(\nabla\boldsymbol u)^T\right)
$$

이고, 구성식은 식 (1)과 같다. 완전접합(perfect bonding)을 가정하면 계면에서 변위와
면력이 연속이어야 한다.

$$
\left[\!\left[\boldsymbol u\right]\!\right]=\boldsymbol 0,
\qquad
\left[\!\left[\boldsymbol\sigma\cdot\boldsymbol n\right]\!\right]=\boldsymbol 0
$$

무한 원방에서는 inclusion이 만드는 섭동장이 사라지는 조건을 사용한다.

$$
\boldsymbol u(\boldsymbol x)\rightarrow\boldsymbol 0,
\qquad \|\boldsymbol x\|\rightarrow\infty
$$

# 5. Eshelby의 핵심 결과

균질한 무한 선형탄성체 속 **타원체 inclusion**에 균일한 고유변형률
$\boldsymbol\varepsilon^*$가 주어지면, inclusion 내부의 전체 변형률
$\boldsymbol\varepsilon^c$는 균일하며

$$
\boxed{
\varepsilon^c_{ij}=S_{ijkl}\varepsilon^*_{kl}}
\qquad\text{또는}\qquad
\boxed{
\boldsymbol\varepsilon^c=\boldsymbol S:\boldsymbol\varepsilon^*}
\tag{2}
$$

로 쓸 수 있다. $\boldsymbol S$가 **Eshelby tensor**다. 위 첨자 $c$는 주변에 의해
구속된(constrained) 전체 변형률을 뜻한다.

- $\boldsymbol S$는 무차원(dimensionless) 4차 텐서다.
- **등방성 기지**에서는 inclusion의 형상, 방향 및 기지의 Poisson 비에 의해 정해진다. 즉 $\boldsymbol S=f(\text{inclusion shape, orientation, Poisson's ratio})$
- inclusion의 크기 자체에는 의존하지 않는다. 이는 내부 길이척도가 없는 고전
  선형탄성 및 무한영역 가정의 결과다.
- inclusion 내부응력은

$$
\boxed{
\boldsymbol\sigma^I
=\boldsymbol C:(\boldsymbol\varepsilon^c-\boldsymbol\varepsilon^*)
=\boldsymbol C:(\boldsymbol S:\boldsymbol\varepsilon^*-\boldsymbol\varepsilon^*)
=\boldsymbol C:(\boldsymbol S-\boldsymbol I^s):
\boldsymbol\varepsilon^*}
\tag{3}
$$

이다. 여기서 $\boldsymbol I^s$는 대칭 2계 텐서 공간의 4계 항등텐서로

$$
I^s_{ijkl}=\frac{1}{2}
(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})
$$

이다.

# 6. 등방성 기지 속 구형 inclusion

Poisson 비가 $\nu$인 등방성 기지 속 구형 inclusion의 Eshelby tensor는

$$
\boxed{
S_{ijkl}
=\frac{1}{15(1-\nu)}
\left[
(5\nu-1)\delta_{ij}\delta_{kl}
+(4-5\nu)
(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})
\right]}
\tag{4}
$$

[식 (4)의 상세 유도: 구형 inclusion의 Eshelby tensor]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16a_eshelby_sphere_derivation.md %})

이다. 체적 투영텐서와 편차 투영텐서(전체에서 체적을 제외한 부분)를 각각

$$
\boldsymbol I^V=\frac{1}{3}\boldsymbol I\otimes\boldsymbol I,
\qquad
\boldsymbol I^D=\boldsymbol I^s-\boldsymbol I^V
$$

로 정의하면 식 (4)는

$$
\boldsymbol S=s_V\boldsymbol I^V+s_D\boldsymbol I^D
$$

로 쓸 수 있으며

$$
s_V=\frac{1+\nu}{3(1-\nu)}
=\frac{3K}{3K+4G},
\qquad
s_D=\frac{2(4-5\nu)}{15(1-\nu)}
$$

이다. 따라서 구형 inclusion에서는 고유변형률의 체적성분과 편차성분이 서로 섞이지
않고 각각 $s_V$, $s_D$만큼 구속된다.

# 7. 체적 고유변형률 계산 예제

등방성 기지의 물성이

$$
E=70\ \mathrm{GPa},
\qquad \nu=0.30
$$

이고, 구형 inclusion이 균일한 체적 팽창 고유변형률

$$
\boldsymbol\varepsilon^*=\varepsilon_0\boldsymbol I,
\qquad \varepsilon_0=0.001
$$

을 가지려 한다고 하자. 체적 고유변형률에는 $\boldsymbol I^V$ 성분만 있으므로

$$
\boldsymbol\varepsilon^c
=s_V\boldsymbol\varepsilon^*
=\frac{1+\nu}{3(1-\nu)}\varepsilon_0\boldsymbol I.
$$

Poisson's ratio, $\nu=0.30$을 대입하면

$$
s_V=\frac{1.30}{3(0.70)}\simeq0.6190
$$

이므로

$$
\boxed{
\boldsymbol\varepsilon^c
=0.000619\boldsymbol I}
$$

이다. 자유롭게 팽창할 때의 $0.001\boldsymbol I$보다 작으므로 기지가 inclusion을
구속한다는 것을 알 수 있다. inclusion 내부의 탄성변형률은

$$
\boldsymbol\varepsilon^e
=\boldsymbol\varepsilon^c-\boldsymbol\varepsilon^*
=-0.000381\boldsymbol I
$$

이다. 체적탄성계수는

$$
K=\frac{E}{3(1-2\nu)}=58.33\ \mathrm{GPa}
$$

이므로 inclusion 내부응력은

$$
\begin{aligned}
\boldsymbol\sigma^I
&=3K(-0.000381)\boldsymbol I\\
&\simeq-66.7\ \mathrm{MPa}\,\boldsymbol I.
\end{aligned}
$$

즉, 팽창하려는 inclusion 내부에는 균일한 정수압축응력이 발생한다. 전체 계가 외력을
받지 않더라도 inclusion 주변 기지에는 이 압축응력과 평형을 이루는 비균일 탄성장이
존재한다.

# 8. Inclusion과 inhomogeneity의 연결

실제 입자의 탄성계수 $\boldsymbol C^I$가 기지의 $\boldsymbol C^M$과 다르면 이것은 inclusion이
아니라 inhomogeneity 문제다. Eshelby의 **등가 inclusion 방법** (Equivalent inclusion method; effective medium approach)에서는 실제
inhomogeneity를 다음 두 효과가 동일하도록 가상의 inclusion으로 바꾼다.

$$
\boldsymbol C^I:(\boldsymbol\varepsilon^I-
\boldsymbol\varepsilon^T)
=\boldsymbol C^M:(\boldsymbol\varepsilon^I-
\boldsymbol\varepsilon^{**})
$$

여기서 $\boldsymbol\varepsilon^T$는 실제 변태 또는 열 고유변형률이고,
$\boldsymbol\varepsilon^{**}$는 탄성계수 차이까지 대신하도록 정한 등가
고유변형률이다. 이 변환을 이용하면 앞선 Eshelby tensor의 해를 불균일한 성질을 가진 inhomogeneity 문제에도 적용할 수 있다 (ELSC, VPSC).

# 9. 적용과 한계

## 주요 적용

- 상변태에 의한 transformation strain과 잔류응력
- 열팽창계수가 다른 입자와 기지의 열응력
- 복합재료의 strain concentration tensor와 유효탄성계수
- 소성영역을 등가 고유변형률로 나타내는 미세역학 모델
- 매트릭스의 성질을 여러 서로 다른 성질의 입자의 평균으로 가정하여 유효 매트릭스 성질을 추정하는 경우 (Homogenization)

## 고전 해의 주요 가정

- 무한 또는 inclusion에 비해 충분히 큰 기지
- **선형**탄성 및 미소변형(infinitesimal strain, $\boldsymbol \varepsilon = \frac{1}{2}(\nabla \boldsymbol u + (\nabla \boldsymbol u)^\mathrm{T})$)
- 완전접합된 계면
- 균질한 기지 재료
- 균일한 고유변형률 (uniform eigenstrain)
- **타원체 inclusion**일 때 균일한 내부장

유한 경계, 계면 박리 또는 계면탄성, 비선형 재료, 큰 변형, 고유변형률 구배가 중요하면
고전적인 Eshelby tensor만으로는 충분하지 않으며 유한요소해석이나 확장된 미세역학
모델이 필요하다.

# 10. 요약

| 개념 | 핵심 내용 |
|---|---|
| Eigenstrain | 구속이 없을 때 응력 없이 발생하려는 변형률 |
| Inclusion | 기지와 탄성계수는 같고 고유변형률을 갖는 영역 |
| Inhomogeneity | 기지와 탄성계수가 다른 영역 |
| Eshelby 결과 | 타원체 inclusion의 균일 고유변형률은 균일한 내부 변형률을 생성 |
| 내부 변형률 | $\boldsymbol\varepsilon^c=\boldsymbol S:\boldsymbol\varepsilon^*$ |
| 내부응력 | $\boldsymbol\sigma^I=\boldsymbol C:(\boldsymbol S-\boldsymbol I^s):\boldsymbol\varepsilon^*$ |
| 구형 inclusion | $\boldsymbol S=s_V\boldsymbol I^V+s_D\boldsymbol I^D$ |
| 크기효과 | 고전 무한영역 해의 $\boldsymbol S$는 inclusion 크기에 무관 |

# 11. 연습 문제

## 문제 1

고유변형률과 탄성변형률의 차이를 설명하시오.

<!--
풀이와 해답:
고유변형률은 주변 구속이 없을 때 응력 없이 발생하려는 변형률이다. 탄성변형률은
전체변형률에서 고유변형률을 뺀 값이며, 응력은 탄성변형률에 의해 결정된다.
-->

## 문제 2

Inclusion과 inhomogeneity의 차이를 탄성계수 관점에서 설명하시오.

<!--
풀이와 해답:
Inclusion은 기지와 같은 탄성계수를 갖지만 지정된 고유변형률을 갖는 영역이다.
Inhomogeneity는 기지와 다른 탄성계수를 갖는 영역이다.
-->

## 문제 3

타원체 형상이 Eshelby 문제에서 특별한 이유를 쓰시오.

<!--
풀이와 해답:
무한 균질 선형탄성체 속 타원체 inclusion에 균일한 고유변형률이 주어지면 inclusion
내부의 전체 변형률과 응력이 균일하기 때문이다.
-->

## 문제 4

$\nu=0.25$인 등방성 기지 속 구형 inclusion에
$\boldsymbol\varepsilon^*=0.002\boldsymbol I$의 체적 고유변형률이 주어졌다.
$s_V$와 inclusion 내부의 구속변형률 $\boldsymbol\varepsilon^c$를 구하시오.

<!--
풀이와 해답:
s_V=(1+nu)/[3(1-nu)]=1.25/[3(0.75)]=5/9이다.
따라서 epsilon^c=(5/9)(0.002)I=0.001111I이다.
-->

## 문제 5

문제 4에서 inclusion 내부의 탄성변형률 부호를 구하고 그 물리적 의미를 설명하시오.

<!--
풀이와 해답:
epsilon^e=epsilon^c-epsilon^*=(0.001111-0.002)I=-0.000889I이다.
음의 구면 탄성변형률은 자유 팽창하려는 inclusion이 주변 기지에 의해 구속되어
내부에 정수압축응력이 발생함을 의미한다.
-->

# 참고문헌

1. J. D. Eshelby, “The determination of the elastic field of an ellipsoidal
   inclusion, and related problems,” *Proceedings of the Royal Society A*,
   241, 376--396 (1957). [DOI: 10.1098/rspa.1957.0133](https://doi.org/10.1098/rspa.1957.0133)
2. T. Mura, *Micromechanics of Defects in Solids*, 2nd ed., Martinus Nijhoff
   Publishers (1987).
