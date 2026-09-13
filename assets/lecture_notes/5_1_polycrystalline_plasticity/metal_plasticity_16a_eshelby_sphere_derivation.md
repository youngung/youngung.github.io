---
layout: distill
title: 구형 inclusion의 Eshelby tensor 유도
description: Kelvin Green 함수와 구면 적분을 이용한 Eshelby tensor의 계산
target: 대학원 입문
permalink:
featured: false
prerequisite: 선형 탄성, 텐서와 좌표변환, Eshelby inclusion 문제
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

- [1. 유도의 목표와 가정](#1-유도의-목표와-가정)
- [2. 전체 계산의 구조](#2-전체-계산의-구조)
- [3. 고유변형률을 등가 체적력으로 바꾸기](#3-고유변형률을-등가-체적력으로-바꾸기)
- [4. Kelvin Green 함수](#4-kelvin-green-함수)
- [5. Hill polarization tensor](#5-hill-polarization-tensor)
- [6. 구면 적분의 계산](#6-구면-적분의-계산)
- [7. Eshelby tensor 계산](#7-eshelby-tensor-계산)
- [8. Lamé 상수에서 Poisson 비로 변환](#8-lamé-상수에서-poisson-비로-변환)
- [9. 결과 검산](#9-결과-검산)
  - [9.1. 텐서 대칭성](#91-텐서-대칭성)
  - [9.2. 독립 성분](#92-독립-성분)
  - [9.3. 체적 고유변형률](#93-체적-고유변형률)
  - [9.4. 편차 고유변형률](#94-편차-고유변형률)
- [10. 이 유도에서 생략한 부분](#10-이-유도에서-생략한-부분)
- [11. 연습 문제](#11-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
- [참고문헌](#참고문헌)

# 1. 유도의 목표와 가정

본 보충자료의 목표는 주 강의의 식 (4), 즉

$$
\boxed{
S_{ijkl}
=\frac{1}{15(1-\nu)}
\left[
(5\nu-1)\delta_{ij}\delta_{kl}
+(4-5\nu)
(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})
\right]}
\tag{1}
$$

을 어떻게 얻는지 설명하는 것이다. 다음을 가정한다.

- 반지름이 $a$인 구형 inclusion
- 무한하고 균질한 등방성 선형탄성 기지
- inclusion과 기지의 탄성계수가 동일함
- inclusion 내부의 균일한 고유변형률 $\boldsymbol\varepsilon^*$
- 미소변형과 완전접합
- 체적력과 원방 하중(far-field load)이 없음

식 (1)은 inclusion **내부점**에 대한 Eshelby tensor다. inclusion 밖의 외부장은 위치에 따라 달라지며
식 (1)만으로 표현되지 않는다.

# 2. 전체 계산의 구조

유도의 핵심 흐름은 다음과 같다.

$$
\boldsymbol\varepsilon^*
\xrightarrow{\ \boldsymbol C\ }
\boldsymbol\sigma^*
\xrightarrow{\ \text{Green 함수}\ }
\boldsymbol\varepsilon^c
$$

고유변형률에 대응하는 eigenstress를

$$
\boldsymbol\sigma^*=\boldsymbol C:\boldsymbol\varepsilon^*
$$

로 정의한다. Green 함수를 적분해 얻는 Hill polarization tensor $\boldsymbol P$가
eigenstress를 구속변형률로 바꾼다.

$$
\boldsymbol\varepsilon^c
=\boldsymbol P:\boldsymbol\sigma^*
=\boldsymbol P:\boldsymbol C:\boldsymbol\varepsilon^*
$$

한편 Eshelby tensor의 정의는

$$
\boldsymbol\varepsilon^c
=\boldsymbol S:\boldsymbol\varepsilon^*
$$

이므로

$$
\boxed{\boldsymbol S=\boldsymbol P:\boldsymbol C}
\tag{2}
$$

이다. 따라서 문제는 구형 영역의 $\boldsymbol P$를 구한 뒤 등방 탄성텐서 $\boldsymbol C$와
축약하는 것으로 바뀐다.

# 3. 고유변형률을 등가 체적력으로 바꾸기

응력과 평형방정식은

$$
\sigma_{ij}
=C_{ijkl}(\varepsilon_{kl}-\varepsilon^*_{kl}),
\qquad
\sigma_{ij,j}=0
$$

이다. $\chi_\Omega(\boldsymbol x)$를 inclusion 영역에서 1이고 그 밖에서 0인
특성함수라 하면 고유변형률장은

$$
\varepsilon^*_{kl}(\boldsymbol x)
=\varepsilon^*_{kl}\chi_\Omega(\boldsymbol x)
$$

로 쓸 수 있다. 이를 평형방정식에 대입하면 Navier 방정식의 오른쪽에

$$
f_i^*(\boldsymbol x)
=-C_{ijkl}\varepsilon^*_{kl}\chi_{\Omega,j}
$$

형태의 등가 체적력이 나타난다. $\chi_{\Omega,j}$는 계면에서만 0이 아니므로, 이는
Eshelby의 절단 사고실험에 등장하는 계면 분포력과 같은 역할을 한다.

이 등가 체적력의 도출 과정, Navier 방정식과의 관계, 특성함수의 분포미분 및 계면력의
의미는 [Eigenstrain의 등가 체적력 유도 보충자료]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16b_eigenstrain_equivalent_body_force.md %})에서
자세히 설명한다.

# 4. Kelvin Green 함수

무한 등방 탄성체에서 단위 집중력이 만드는 변위를 나타내는 Kelvin Green 함수는

$$
G_{ij}(\boldsymbol r)
=\frac{1}{16\pi\mu(1-\nu)r}
\left[
(3-4\nu)\delta_{ij}
+\frac{r_i r_j}{r^2}
\right]
\tag{3}
$$

이다. 여기서 $\boldsymbol r=\boldsymbol x-\boldsymbol y$, $r=\|\boldsymbol r\|$,
$\mu$는 전단탄성계수다. 이 함수는 무한영역 Navier 연산자의 기본해이며, 등가
체적력과 convolution하면 변위장을 얻는다.

Navier 방정식에서 식 (3)을 직접 유도하는 과정과 각 텐서 항의 의미는
[Kelvin Green 함수의 유도와 해석 보충자료]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16c_kelvin_green_function_derivation.md %})에서
자세히 설명한다.

고유변형률이 inclusion 내부에서 일정하므로 부분적분을 수행하면 체적적분을 inclusion
경계 $\partial\Omega$에 대한 표면적분으로 바꿀 수 있다. 변위를 다시 미분하고 대칭부분을
취하면 구속변형률이 얻어진다.

# 5. Hill polarization tensor

Hill polarization tensor는 eigenstress를 inclusion의 구속변형률로 변환한다.

$$
\varepsilon^c_{ij}=P_{ijkl}\sigma^*_{kl}.
$$

내부점 $\boldsymbol x\in\Omega$에서는 다음의 Green 함수 표면적분으로 나타낼 수 있다.

$$
\begin{aligned}
P_{ijkl}(\boldsymbol x)
=\frac{1}{4}\int_{\partial\Omega}
\big[&
(G_{ki,j}+G_{kj,i})n_l\\
&+(G_{li,j}+G_{lj,i})n_k
\big]\,dS_y.
\end{aligned}
\tag{4}
$$

앞쪽 첨자 $i,j$는 구속변형률의 성분을, 뒤쪽 첨자 $k,l$은 eigenstress의 성분을
나타낸다. 계수 $1/4$는 변형률에 대한 $i,j$ 대칭화와 대칭 eigenstress에 대한 $k,l$
대칭화에서 나온다.

Green 함수 convolution에서 식 (4)를 얻는 전체 과정은
[Hill polarization tensor의 표면적분 유도 보충자료]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16d_hill_polarization_surface_integral.md %})에서
자세히 설명한다.

구형 inclusion의 반지름을 $a$라 하고 구의 중심을 원점으로 둔다. 계면 위의 source
point에서는 바깥쪽 단위법선 $\boldsymbol n$과 위치벡터가 나란하므로
$\boldsymbol y=a\boldsymbol n$이다. Polarization tensor를 구의 중심에서 평가하기 위해
field point를 $\boldsymbol x=\boldsymbol0$으로 선택하면

$$
\boldsymbol y=a\boldsymbol n,
\qquad
dS_y=a^2d\Omega,
\qquad
\boldsymbol r=\boldsymbol x-\boldsymbol y=-a\boldsymbol n
$$

이다. 여기서 $d\Omega$는 단위구의 **미소 입체각(solid angle)**이다. 평면에서 두
반직선 사이의 벌어진 정도를 각도로 측정하듯이, 3차원에서는 구의 중심에서 바라본
미소면이 차지하는 방향의 범위를 입체각으로 측정한다. 중심에서 계면의 미소면
$dS_y$를 향해 가는 반직선들을 그리면 매우 작은 원뿔이 만들어지며, 이 원뿔이 단위구
표면에서 잘라 내는 면적이 바로 $d\Omega$다.

반지름 $a$인 구와 단위구에서 같은 방향 범위를 차지하는 미소면은 닮음관계에 있으므로
면적이 반지름의 제곱에 비례한다. 따라서

$$
d\Omega=\frac{dS_y}{a^2},
\qquad
dS_y=a^2d\Omega
$$

가 된다. 즉 $d\Omega$는 길이나 면적의 차원을 갖지 않는 무차원량이며, 단위는
steradian이다. 구면좌표에서 극각을 $\theta$, 방위각을 $\phi$라고 하면

$$
d\Omega=\sin\theta\,d\theta\,d\phi,
\qquad
dS_y=a^2\sin\theta\,d\theta\,d\phi
$$

로 쓸 수 있다. 전체 구면이 차지하는 입체각은

$$
\int_{S^2}d\Omega
=\int_0^{2\pi}\int_0^\pi
\sin\theta\,d\theta\,d\phi
=4\pi
$$

이다. 여기서 inclusion 영역을 나타내는 $\Omega$와 미소 입체각 기호 $d\Omega$는 같은
그리스 문자를 사용하지만 서로 다른 개념임에 유의해야 한다.

구형 inclusion 내부에서는 $\boldsymbol P$가 위치에 무관하므로 중심에서 계산한 값이 모든
내부점에 적용된다.

![구형 inclusion에서 중심의 field point, 계면의 source point, 바깥쪽 법선 및 상대위치벡터의 관계](/assets/img/lecture_notes/micromechanics/hill_polarization_geometry.png)

# 6. 구면 적분의 계산

Kelvin Green 함수를 미분하고 구의 중심에서
\(\boldsymbol r=-a\boldsymbol n\), \(dS_y=a^2d\Omega\)를 대입하면 식 (4)는

$$
\begin{aligned}
P_{ijkl}=\frac14\int_{S^2}\big\{&
(\alpha-\beta)(
\delta_{ki}n_jn_l+\delta_{kj}n_in_l
+\delta_{li}n_jn_k+\delta_{lj}n_in_k)\\
&-4\beta\delta_{ij}n_kn_l
+12\beta n_in_jn_kn_l
\big\}\,d\Omega,
\end{aligned}
$$

$$
\alpha=\frac{\lambda+3\mu}{8\pi\mu(\lambda+2\mu)},
\qquad
\beta=\frac{\lambda+\mu}{8\pi\mu(\lambda+2\mu)}
$$

로 정리된다. 이때 Green 함수 미분의 \(a^{-2}\)와 면적요소의 \(a^2\)가 소거되며,
계산에 필요한 구면 모멘트는 다음 두 식이다.

$$
\int_{S^2}n_i n_j\,d\Omega
=\frac{4\pi}{3}\delta_{ij}
\tag{5}
$$

$$
\int_{S^2}n_i n_j n_k n_l\,d\Omega
=\frac{4\pi}{15}
(\delta_{ij}\delta_{kl}
+\delta_{ik}\delta_{jl}
+\delta_{il}\delta_{jk})
\tag{6}
$$

Kelvin Green 함수의 미분, \(a^{-2}\)의 소거, 회전 불변성을 이용한 식 (5)–(6)의
유도는 [Kelvin Green 함수 미분과 구면 모멘트 적분 보충자료]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16e_kelvin_spherical_moment_derivation.md %})에서
자세히 설명한다.

식 (5)–(6)을 대입해 정리하면 구형 inclusion의 polarization tensor는

$$
\boxed{
P_{ijmn}
=\frac{1}{30\mu(\lambda+2\mu)}
\left[
-2(\lambda+\mu)\delta_{ij}\delta_{mn}
+(3\lambda+8\mu)
(\delta_{im}\delta_{jn}+\delta_{in}\delta_{jm})
\right]}
\tag{7}
$$

이 된다. 식 (7)은 구의 반지름 \(a\)와 무관하며, 구면의 회전대칭성 때문에 두 개의
등방 4계 텐서 조합으로 표현된다.

# 7. Eshelby tensor 계산

등방 탄성텐서는

$$
C_{mnkl}
=\lambda\delta_{mn}\delta_{kl}
+\mu(\delta_{mk}\delta_{nl}+\delta_{ml}\delta_{nk})
\tag{8}
$$

이다. 계산을 간결하게 하기 위해 식 (7)을

$$
P_{ijmn}
=A\delta_{ij}\delta_{mn}
+B(\delta_{im}\delta_{jn}+\delta_{in}\delta_{jm})
$$

로 쓰면

$$
A=-\frac{\lambda+\mu}{15\mu(\lambda+2\mu)},
\qquad
B=\frac{3\lambda+8\mu}{30\mu(\lambda+2\mu)}
$$

이다. 식 (2), 즉 $S_{ijkl}=P_{ijmn}C_{mnkl}$을 계산할 때 필요한 축약은

$$
\delta_{mn}\delta_{mn}=3,
\qquad
(\delta_{im}\delta_{jn}+\delta_{in}\delta_{jm})\delta_{mn}
=2\delta_{ij}
$$

및

$$
\begin{aligned}
(&\delta_{im}\delta_{jn}+\delta_{in}\delta_{jm})
(\delta_{mk}\delta_{nl}+\delta_{ml}\delta_{nk})\\
&=2(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})
\end{aligned}
$$

이다. 따라서

$$
\begin{aligned}
S_{ijkl}
=&\left[A(3\lambda+2\mu)+2\lambda B\right]
\delta_{ij}\delta_{kl}\\
&+2\mu B
(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).
\end{aligned}
\tag{9}
$$

$A$와 $B$를 대입하면

$$
\boxed{
S_{ijkl}
=\frac{3\lambda-2\mu}{15(\lambda+2\mu)}
\delta_{ij}\delta_{kl}
+\frac{3\lambda+8\mu}{15(\lambda+2\mu)}
(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})}
\tag{10}
$$

을 얻는다.

# 8. Lamé 상수에서 Poisson 비로 변환

등방 탄성상수 관계

$$
\lambda=\frac{2\mu\nu}{1-2\nu},
\qquad
\lambda+2\mu=\frac{2\mu(1-\nu)}{1-2\nu}
$$

를 식 (10)에 대입하면

$$
\frac{3\lambda-2\mu}{15(\lambda+2\mu)}
=\frac{5\nu-1}{15(1-\nu)}
$$

및

$$
\frac{3\lambda+8\mu}{15(\lambda+2\mu)}
=\frac{4-5\nu}{15(1-\nu)}
$$

를 얻는다. 따라서 식 (10)은

$$
S_{ijkl}
=\frac{1}{15(1-\nu)}
\left[
(5\nu-1)\delta_{ij}\delta_{kl}
+(4-5\nu)
(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})
\right]
$$

이 되며, 이것이 주 강의의 식 (4)다.

# 9. 결과 검산

## 9.1. 텐서 대칭성

변형률과 고유변형률이 대칭이므로

$$
S_{ijkl}=S_{jikl}=S_{ijlk}
$$

를 만족해야 한다. 식 (1)은 이 minor symmetry를 만족한다. 일반적으로 Eshelby
tensor는 탄성계수 텐서와 달리 major symmetry
$S_{ijkl}=S_{klij}$를 반드시 만족하는 것은 아니지만, 등방성 구형 inclusion의
식 (1)은 특별히 major symmetry도 만족한다.

## 9.2. 독립 성분

식 (1)에서 대표 성분은

$$
S_{1111}=\frac{7-5\nu}{15(1-\nu)},
\qquad
S_{1122}=\frac{5\nu-1}{15(1-\nu)},
\qquad
S_{1212}=\frac{4-5\nu}{15(1-\nu)}
$$

이다. 또한 $S_{1111}=S_{1122}+2S_{1212}$가 성립한다.

## 9.3. 체적 고유변형률

$\varepsilon^*_{kl}=\varepsilon_0\delta_{kl}$을 대입하면

$$
\varepsilon^c_{ij}
=S_{ijkk}\varepsilon_0
=\frac{1+\nu}{3(1-\nu)}
\varepsilon_0\delta_{ij}.
$$

즉 체적모드의 Eshelby 계수는

$$
s_V=\frac{1+\nu}{3(1-\nu)}
=\frac{3K}{3K+4\mu}
$$

이며 주 강의의 수치 예제와 일치한다.

## 9.4. 편차 고유변형률

$\operatorname{tr}(\boldsymbol\varepsilon^*)=0$이면
$\delta_{kl}\varepsilon^*_{kl}=0$이므로 첫 번째 항은 사라진다. 따라서

$$
\boldsymbol\varepsilon^c
=\frac{2(4-5\nu)}{15(1-\nu)}
\boldsymbol\varepsilon^*
$$

이며 편차모드의 계수는

$$
s_D=\frac{2(4-5\nu)}{15(1-\nu)}
$$

이다.

# 10. 이 유도에서 생략한 부분

본 자료는 식 (4)의 구조와 계수 계산에 초점을 맞추기 위해 다음의 긴 계산은 중간결과로
정리하였다.

- Navier 연산자에서 Kelvin Green 함수를 직접 유도하는 과정
- Green 함수 convolution을 식 (4)의 표면적분으로 바꾸는 모든 부분적분 단계
- 식 (3)을 미분하여 식 (7)을 얻는 Kronecker delta 항의 전체 전개
- 일반 타원체의 elliptic integral 계산

이 단계들을 생략해도 핵심 논리는 분명하다. 구의 회전대칭성이 $\boldsymbol P$를 두 개의
등방 텐서로 제한하고, 구면의 2차 및 4차 방향모멘트가 각각 $1/3$과 $1/15$ 계수를
만들며, 마지막으로 $\boldsymbol S=\boldsymbol P:\boldsymbol C$를 계산하면 식 (1)이 나온다.

# 11. 연습 문제

## 문제 1

식 (5)를 $i=j$로 축약하여 계수 $4\pi/3$을 확인하시오.

<!--
풀이와 해답:
등방성에 의해 적분은 A delta_ij 형태다. i=j로 축약하면 왼쪽은
int(n_i n_i)dOmega=int(1)dOmega=4pi이고 오른쪽은 A delta_ii=3A이다.
따라서 A=4pi/3이다.
-->

## 문제 2

식 (7)의 차원을 확인하고 구의 반지름 $a$가 결과에 나타나지 않는 이유를 설명하시오.

<!--
풀이와 해답:
P는 strain을 stress로부터 구하므로 compliance와 같은 1/stress 차원을 갖는다.
Green 함수 미분에서 생기는 a^{-2}와 구면 면적요소의 a^2가 상쇄되므로 고전적인
무한영역 해에는 반지름이 남지 않는다.
-->

## 문제 3

$S_{1212}$를 식 (1)에서 직접 구하시오.

<!--
풀이와 해답:
i=1, j=2, k=1, l=2를 대입하면 delta_12 delta_12=0,
delta_11 delta_22=1, delta_12 delta_21=0이다. 따라서
S_1212=(4-5nu)/[15(1-nu)]이다.
-->

## 문제 4

$\nu=0.30$일 때 $s_V$와 $s_D$를 계산하시오.

<!--
풀이와 해답:
s_V=(1+0.30)/[3(1-0.30)]=0.61905이다.
s_D=2(4-5x0.30)/[15(1-0.30)]=0.47619이다.
-->

# 참고문헌

1. J. D. Eshelby, “The determination of the elastic field of an ellipsoidal
   inclusion, and related problems,” *Proceedings of the Royal Society A*,
   241, 376--396 (1957). [DOI: 10.1098/rspa.1957.0133](https://doi.org/10.1098/rspa.1957.0133)
2. T. Mura, *Micromechanics of Defects in Solids*, 2nd ed., Martinus Nijhoff
   Publishers (1987).

[주 강의로 돌아가기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16_eshelby_inclusion.md %})
