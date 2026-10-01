---
layout: distill
title: 유한변형의 운동학
description: Lagrangian·Eulerian 기술법, 변형구배, 유한변형률과 극분해
target: 학부 고학년
permalink:
featured: true
prerequisite: 변위와 미소변형률
toc: false

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


이 자료는 연속체의 좌표 기술법, 변형구배, 유한변형률과 극분해를 다룬다.
VPSC에 적용하는 속도구배와 결정립의 운동은
[VPSC의 운동학]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_15_kinematics.md %})에서 다룬다.

관련 자료는 다음 순서로 읽을 수 있다.

- [변위와 미소변형률]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05_displacement_strain.md %})
- [변위와 미소변형률 연습문제]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %})
- [유한변형의 운동학]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %})
- [물질미분과 ALE 기술법]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %})

**목차**

* 목차
{:toc}

<span id="10-lagrangian과-eulerian-기술법"></span>

# 1. Lagrangian과 Eulerian 기술법

[변위와 미소변형률 자료]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05_displacement_strain.md %})에서는 변형 전 위치($\boldsymbol X$)를 기준으로 변위를 표현했다. 이제 같은
운동을 현재 위치($\boldsymbol x$)를 기준으로 표현하면 무엇이 달라지는지
살펴보자.

<span id="101-같은-물질점과-같은-공간-위치"></span>

## 1.1. 같은 물질점과 같은 공간 위치

**Lagrangian 기술법 (Lagrangian description, 물질 기술법)**은 같은 물질점을 따라간다.
기준 배치(reference configuration)의 좌표 $\boldsymbol X$를 물질점의 이름표로 삼으면,
시간 $t$에서의 현재 위치는 운동함수 $\boldsymbol\Phi$로 표현된다.

$$
\boldsymbol x=\boldsymbol\Phi(\boldsymbol X,t),
\qquad
\boldsymbol u_L(\boldsymbol X,t)=\boldsymbol\Phi(\boldsymbol X,t)-\boldsymbol X.
$$

예를 들어 막대에 표시한 점이 인장 중 어디로 이동하는지 추적하는 관점이다.
기준 배치는 보통 초기 형상으로 택하지만 반드시 무응력 상태일 필요는 없다.

**Eulerian 기술법 (Eulerian description, 공간 기술법)**은 현재 공간의 위치
$\boldsymbol x$에서 물리량을 관찰한다. 고정된 관찰 지점을 서로 다른 물질점들이
지나갈 수 있다. 운동함수가 역변환 가능하면
$\boldsymbol X=\boldsymbol\Phi^{-1}(\boldsymbol x,t)$이므로,

$$
\boldsymbol u_E(\boldsymbol x,t)=\boldsymbol x-\boldsymbol\Phi^{-1}(\boldsymbol x,t),
\qquad
\boldsymbol u_E(\boldsymbol\Phi(\boldsymbol X,t),t)=\boldsymbol u_L(\boldsymbol X,t).
$$

두 기술법은 같은 운동을 서로 다른 독립변수로 표현한다. 변위값은 같은 물질점에서
같지만, $\nabla_X\boldsymbol u_L$과 $\nabla_x\boldsymbol u_E$는 일반적으로 다르다.
[변위와 미소변형률 자료의 5–9절]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05_displacement_strain.md %})은 기준 좌표 구배를 사용했다. 변위구배가 작을 때에는 현재 좌표 구배와
거의 같지만, 유한변형에서는 두 구배를 구분해야 한다.

두 기술법의 차이를 요약하면 다음과 같다.

| 비교 항목 | Lagrangian 기술법 (물질 기술법) | Eulerian 기술법 (공간 기술법) |
| --------- | ------------------------------ | ---------------------------- |
| 관찰 기준 | 같은 물질점을 따라감 | 고정된 공간 위치에서 관찰함 |
| 독립변수 | 기준 좌표 $\boldsymbol X$와 시간 $t$ | 현재 좌표 $\boldsymbol x$와 시간 $t$ |
| 좌표의 의미 | 물질점의 이름표 | 물리량을 관찰하는 공간 위치 |
| 변위 표현 | $\boldsymbol u_L(\boldsymbol X,t)=\boldsymbol\Phi(\boldsymbol X,t)-\boldsymbol X$ | $\boldsymbol u_E(\boldsymbol x,t)=\boldsymbol x-\boldsymbol\Phi^{-1}(\boldsymbol x,t)$ |
| 공간미분 | 기준 좌표에 대한 구배 $\nabla_X$ | 현재 좌표에 대한 구배 $\nabla_x$ |
| 관찰 예 | 막대에 표시한 점의 이동을 추적 | 고정된 위치를 지나는 물질의 속도를 측정 |

<span id="102-앞의-1차원-인장을-두-기술법으로-표현하기"></span>

## 1.2. 앞의 1차원 인장을 두 기술법으로 표현하기

[기본 자료 6절]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05_displacement_strain.md %}#6-1차원-예제)의 $u(X)=0.01X$를 다시 생각하자. 이 예제를 일반화하기 위해
**신장비 (stretch ratio)**를 먼저 정의한다.

$$
\Lambda=\frac{l}{l_0}>0.
$$

여기서 $l_0$는 초기 길이, $l$은 변형 후 길이이며, $\Lambda$는 무차원이다.
$\Lambda=1$이면 길이 변화가 없고, $\Lambda>1$이면 인장, $0<\Lambda<1$이면 압축이다.
[기본 자료 6절]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05_displacement_strain.md %}#6-1차원-예제)의 예제는 $\Lambda=1.01$에 해당한다.
이 기호를 사용하면 작은 변형과 큰 변형에서 두 기술법을 같은 식으로 비교할 수 있다.

평행이동 없이 원점을 고정한 균일 변형 $x=\Lambda X$에서

$$
u_L(X)=(\Lambda-1)X,
\qquad X=\frac{x}{\Lambda},
\qquad u_E(x)=\left(1-\frac1\Lambda\right)x.
$$

따라서 같은 운동의 변위구배도 미분에 사용하는 좌표에 따라 달라진다.

$$
\frac{du_L}{dX}=\Lambda-1,
\qquad \frac{du_E}{dx}=1-\frac1\Lambda.
$$

[기본 자료 6절]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05_displacement_strain.md %}#6-1차원-예제)처럼 $\Lambda=1.01$이면 두 값은 $0.01$과 약 $0.009901$로 가깝다.
반면 $\Lambda=1.5$이면 $0.5$와 약 $0.3333$으로 차이가 커진다.
두 기술법이 다른 변형을 뜻하는 것이 아니라, **미분에 사용하는 좌표가 다르기 때문**이다.

이 구분을 바탕으로 다음 절에서는 기준 배치의 선분이 현재 배치로 어떻게 변환되는지 다룬다.
물질점을 따라 관찰하는 시간 변화율은 [물질미분 자료]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %}),
계산 격자의 운동까지 구분하는 ALE 기술법은 [ALE 기술법]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %}#부록-b-ale-기술법)에서 설명한다.

<span id="11-유한변형률-finite-strain"></span>

# 2. 유한변형률 (finite strain)

<span id="111-변형구배-deformation-gradient"></span>

## 2.1. 변형구배 (deformation gradient)

변위구배가 작지 않거나 회전각이 크면 미소변형 근사를 사용할 수 없다.
기준 좌표에 대한 현재 위치의 구배인 **변형구배**를 정의하자.

$$
\boxed{\boldsymbol F=\frac{\partial\boldsymbol x}{\partial\boldsymbol X}
=\boldsymbol I+\nabla_X\boldsymbol u_L},
\qquad F_{ij}=\frac{\partial x_i}{\partial X_j}.
$$

$\boldsymbol I$는 단위텐서다. $F_{ij}$에서 $i$는 현재 위치의 성분이고,
$j$는 미분하는 기준좌표 방향을 나타낸다. 변위구배의 성분은

$$
(\nabla_X\boldsymbol u_L)_{ij}=\frac{\partial u_{L,i}}{\partial X_j}
$$

로 정의한다. 우변의 $\partial u_{L,i}$에서 첨자 $_L$은 Lagrangian 기술법 $_i$는 변위 성분을 뜻한다.

이웃한 물질점 사이의 미소 선분은

$$
d\boldsymbol x=\boldsymbol F\cdot d\boldsymbol X
$$

로 변환된다. 이 관계는 유한변형에서도 성립한다.
$\boldsymbol F$에는 변형과 회전이 함께 들어 있으므로,
$\boldsymbol F$ 자체를 변형률이라고 부르지는 않는다.
체적비를 나타내는 스칼라를 $J=\det\boldsymbol F$로 정의한다.
매끄럽고 방향을 보존하는 국소 변형에서는 $J>0$이고,

$$
dv=J\,dV,
\qquad \frac{dv-dV}{dV}=J-1
$$

이다. $dV$와 $dv$는 기준 배치와 현재 배치의 체적요소(volume element)다.
$J=dv/dV$는 **체적비**이고, $J-1=(dv-dV)/dV$은 **기준 체적에 대한 상대 체적 변화량**이다.
$J>1$이면 체적이 증가하고, $0<J<1$이면 감소한다.
비압축성 변형의 정확한 조건은 $J=1$이다.

현재 좌표 $\boldsymbol x$에 대한 Eulerian 변위구배와의 관계도 확인하자.
운동함수 $\boldsymbol\Phi$가 매끄럽고 역변환 가능하다고 가정하면,
현재 위치에 있는 물질점의 기준 위치는

$$
\boldsymbol X=\boldsymbol\Phi^{-1}(\boldsymbol x,t)
=\boldsymbol x-\boldsymbol u_E(\boldsymbol x,t)
$$

이다. 시간을 고정하고 현재좌표로 미분하면

$$
\boxed{\boldsymbol F^{-1}
=\frac{\partial\boldsymbol X}{\partial\boldsymbol x}
=\boldsymbol I-\nabla_x\boldsymbol u_E}
$$

를 얻는다.

<span id="112-길이-변화로부터-정의하는-유한변형률"></span>

## 2.2. 길이 변화로부터 정의하는 유한변형률

### 2.2.1. Green–Lagrange 변형률의 정의

기준 배치의 미소 선분을 $d\boldsymbol X$, 변형 후 선분을 $d\boldsymbol x$라 하자.
각 선분의 길이를 $\ell_0=\|d\boldsymbol X\|$, $\ell=\|d\boldsymbol x\|$라 하면,
벡터와 자기 자신의 내적은 길이의 제곱이므로

$$
\ell_0^2=d\boldsymbol X\cdot d\boldsymbol X,
\qquad
\ell^2=d\boldsymbol x\cdot d\boldsymbol x.
$$

**길이 자체 대신 제곱 길이를 사용하면 제곱근 없이 내적과 텐서로 길이 변화를 표현할 수 있다.**
여기서 $\ell^2-\ell_0^2$는 제곱 길이의 차이이며,
길이 차이 $\ell-\ell_0$나 그 제곱 $(\ell-\ell_0)^2$와는 다르다.

앞 절의 $d\boldsymbol x=\boldsymbol F\cdot d\boldsymbol X$를 이용하여 이 차이를 계산하자.
같은 정규직교 기저에서 선분의 성분을 열벡터 $[d\boldsymbol X]$, $[d\boldsymbol x]$로
배열한다. 대괄호는 성분 배열이고, 내적은
$\boldsymbol a\cdot\boldsymbol b=[\boldsymbol a]^T[\boldsymbol b]$로 계산한다.
곱의 전치 규칙 $([\boldsymbol A][\boldsymbol B])^T=[\boldsymbol B]^T[\boldsymbol A]^T$를 적용하면

$$
\begin{aligned}
\ell^2
&=[d\boldsymbol x]^T[d\boldsymbol x]\\
&=([\boldsymbol F][d\boldsymbol X])^T([\boldsymbol F][d\boldsymbol X])\\
&=[d\boldsymbol X]^T[\boldsymbol F]^T[\boldsymbol F][d\boldsymbol X].
\end{aligned}
$$

기준 선분의 제곱 길이는
$\ell_0^2=[d\boldsymbol X]^T[\boldsymbol I][d\boldsymbol X]$이므로

$$
\ell^2-\ell_0^2
=[d\boldsymbol X]^T
\left([\boldsymbol F]^T[\boldsymbol F]-[\boldsymbol I]\right)
[d\boldsymbol X].
$$

이 식에서 기준 선분의 제곱 길이 변화를 나타내는 텐서를
**Green–Lagrange 변형률 (Green–Lagrange strain)**로 정의한다.

$$
\boxed{\boldsymbol E=\frac12(\boldsymbol F^T\cdot\boldsymbol F-\boldsymbol I)}.
$$

따라서 제곱 길이 차이는 다음과 같이 쓸 수 있다.

$$
\boxed{\ell^2-\ell_0^2
=2[d\boldsymbol X]^T[\boldsymbol E][d\boldsymbol X]
=2d\boldsymbol X\cdot(\boldsymbol E\cdot d\boldsymbol X)}.
$$

이는 벡터가 행렬의 양쪽에 나타나는 **이차형식 (quadratic form)**이다.
3차원에서 배열 크기는 $(1\times3)(3\times3)(3\times1)$이므로 결과는 스칼라이며,
$\boldsymbol E$는 무차원이고 결과의 단위는 길이의 제곱이다.
성분으로 쓰면 $\ell^2-\ell_0^2=2dX_iE_{ij}dX_j$이며, 반복 첨자에 대해 합한다.

기준 선분의 길이와 방향을 분리해 보자. 길이가 $\ell_0>0$인 선분의 단위방향을
$\boldsymbol N$이라 정의하면

$$
\boldsymbol N=\frac{d\boldsymbol X}{\ell_0},
\qquad \|\boldsymbol N\|=1,
\qquad d\boldsymbol X=\ell_0\boldsymbol N.
$$

이를 앞에서 구한 제곱 길이 차이에 대입하면

$$
\begin{aligned}
\ell^2-\ell_0^2
&=2d\boldsymbol X\cdot(\boldsymbol E\cdot d\boldsymbol X)\\
&=2(\ell_0\boldsymbol N)\cdot
\left[\boldsymbol E\cdot(\ell_0\boldsymbol N)\right]\\
&=2(\ell_0\boldsymbol N)\cdot
\left[\ell_0(\boldsymbol E\cdot\boldsymbol N)\right]\\
&=2\ell_0^2\,\boldsymbol N\cdot(\boldsymbol E\cdot\boldsymbol N).
\end{aligned}
$$

세 번째 줄에서는 텐서의 선형성에 의해
$\boldsymbol E\cdot(\ell_0\boldsymbol N)=\ell_0(\boldsymbol E\cdot\boldsymbol N)$을 사용했다.
네 번째 줄에서는 내적의 양쪽 벡터에 곱해진 스칼라 $\ell_0$를 각각 밖으로 꺼냈다.
따라서 두 계수가 곱해져 $\ell_0^2$이 된다.

이제 양변을 $2\ell_0^2$으로 나누면

$$
\begin{aligned}
\boldsymbol N\cdot(\boldsymbol E\cdot\boldsymbol N)
&=\frac{\ell^2-\ell_0^2}{2\ell_0^2}\\
&=\frac12\left(\frac{\ell^2}{\ell_0^2}-1\right)\\
&=\frac12\left[\left(\frac{\ell}{\ell_0}\right)^2-1\right].
\end{aligned}
$$

왼쪽 식은 먼저 $\boldsymbol E\cdot\boldsymbol N$이라는 벡터를 구한 뒤,
이를 $\boldsymbol N$과 내적한 **스칼라**다. 성분 배열로는
$[\boldsymbol N]^T[\boldsymbol E][\boldsymbol N]$, 첨자 표기로는 $N_iE_{ij}N_j$이다.
특히 $\boldsymbol N=(1,0,0)^T$이면 이 값은 $E_{11}$이지만,
임의의 방향에서는 여러 변형률 성분이 함께 기여한다.
해당 방향 선분의 신장비 $\Lambda=\ell/\ell_0$를 사용하면

$$
\boxed{\boldsymbol N\cdot(\boldsymbol E\cdot\boldsymbol N)
=\frac12(\Lambda^2-1)}.
$$

즉 $\boldsymbol E$는 **기준 방향별 선분의 신장 또는 수축**을 나타낸다.
앞의 $1/2$ 계수는 작은 신장 $\ell/\ell_0=1+\eta$에서
$[(1+\eta)^2-1]/2=\eta+\eta^2/2\approx\eta$가 되어
기존 미소변형률과 일차항이 일치하도록 한다. 다음 절에서 이를 텐서식으로 확인한다.

### 2.2.2. Green–Lagrange 변형률과 미소변형률의 관계

위의 길이 관계에는 변위구배가 작다는 가정이 없다. 여기서 **미소 선분**은 서로 매우
가까운 두 물질점을 잇는 선분을 뜻하며, 그 선분의 **신장비까지 작다는 뜻은 아니다**.
Green–Lagrange 변형률은 이러한 선분의 제곱 길이 변화를 기준 배치에서 표현한다.

변위구배 $\boldsymbol H=\nabla_X\boldsymbol u_L$와
$\boldsymbol F=\boldsymbol I+\boldsymbol H$를 대입하여 전개하면

$$
\begin{aligned}
\boldsymbol E
&=\frac12\left[(\boldsymbol I+\boldsymbol H)^T
\cdot(\boldsymbol I+\boldsymbol H)-\boldsymbol I\right]\\
&=\frac12\left(\boldsymbol H+\boldsymbol H^T
+\boldsymbol H^T\cdot\boldsymbol H\right).
\end{aligned}
$$

[기본 자료]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05_displacement_strain.md %})에서
정의한 미소변형률은 변위구배의 대칭부분이므로

$$
\boldsymbol\varepsilon=\frac12(\boldsymbol H+\boldsymbol H^T),
\qquad
\boxed{\boldsymbol E=\boldsymbol\varepsilon
+\frac12\boldsymbol H^T\cdot\boldsymbol H}.
$$

마지막 식은 정확한 항등식이다. 성분으로 쓰면

$$
E_{ij}=\underbrace{\frac12\left(
\frac{\partial u_{L,i}}{\partial X_j}
+\frac{\partial u_{L,j}}{\partial X_i}\right)}_{\varepsilon_{ij}}
+\frac12\sum_{k=1}^3
\frac{\partial u_{L,k}}{\partial X_i}
\frac{\partial u_{L,k}}{\partial X_j}.
$$

따라서 **미소변형률은 Green–Lagrange 변형률에서 변위구배의 이차항을 생략한 근사**다.
$\|\boldsymbol H\|\ll1$이면 일차항에 비해 이차항이 작아서
$\boldsymbol E\approx\boldsymbol\varepsilon$로 계산할 수 있다.
예를 들어 변위구배의 크기가 $10^{-2}$ 수준이면 이차항은 $10^{-4}$ 수준이다.
다만 특정 성분의 일차항이 0이면, 그 성분에서는 이차항이 첫 번째로 나타나는 기여일 수 있다.

근사의 기준은 **변위 자체의 크기가 아니라 변위구배의 크기**다.
모든 점이 같은 상수벡터 $\boldsymbol c$만큼 이동하는 병진운동에서는

$$
\boldsymbol u_L=\boldsymbol c,
\qquad \boldsymbol H=\boldsymbol0,
\qquad \boldsymbol E=\boldsymbol\varepsilon=\boldsymbol0.
$$

따라서 병진 거리가 커도 변형률은 0이다. 반면 실제 늘어남이 작더라도 회전이 크면
$\boldsymbol H$가 작지 않을 수 있다. 이 경우 이차항을 생략하면 잘못된 변형률이
나올 수 있으며, 2.3절에서 강체회전으로 확인한다.

### 2.2.3. 현재 배치를 기준으로 표현하는 Euler–Almansi 변형률

2.2.1절에서는 제곱 길이 차이 $\ell^2-\ell_0^2$를 **기준 선분** $d\boldsymbol X$로
표현하여 Green–Lagrange 변형률 $\boldsymbol E$를 정의했다.
같은 차이를 **현재 선분** $d\boldsymbol x$로 표현하면
Euler–Almansi 변형률 $\boldsymbol e$를 얻는다.
여기서도 $\ell_0=\|d\boldsymbol X\|$, $\ell=\|d\boldsymbol x\|$이다.

**현재 선분으로 기준 선분의 길이 표현하기**

$\boldsymbol F$가 가역이면 $d\boldsymbol x=\boldsymbol F\cdot d\boldsymbol X$로부터

$$
d\boldsymbol X=\boldsymbol F^{-1}\cdot d\boldsymbol x
$$

를 얻는다. 같은 정규직교 기저에서 성분을 배열하고 곱의 전치 규칙을 적용하면

$$
\begin{aligned}
\ell_0^2
&=[d\boldsymbol X]^T[d\boldsymbol X]\\
&=([\boldsymbol F]^{-1}[d\boldsymbol x])^T
([\boldsymbol F]^{-1}[d\boldsymbol x])\\
&=[d\boldsymbol x]^T[\boldsymbol F]^{-T}
[\boldsymbol F]^{-1}[d\boldsymbol x].
\end{aligned}
$$

여기서 $\boldsymbol F^{-T}=(\boldsymbol F^{-1})^T$다.
현재 선분에 대해서는 $\ell^2=[d\boldsymbol x]^T[\boldsymbol I][d\boldsymbol x]$이므로

$$
\ell^2-\ell_0^2
=[d\boldsymbol x]^T
\left([\boldsymbol I]-[\boldsymbol F]^{-T}[\boldsymbol F]^{-1}\right)
[d\boldsymbol x].
$$

따라서 **Euler–Almansi 변형률 (Euler–Almansi strain)**을

$$
\boxed{\boldsymbol e=\frac12
(\boldsymbol I-\boldsymbol F^{-T}\cdot\boldsymbol F^{-1})}
$$

로 정의하면

$$
\boxed{\ell^2-\ell_0^2
=2[d\boldsymbol x]^T[\boldsymbol e][d\boldsymbol x]
=2d\boldsymbol x\cdot(\boldsymbol e\cdot d\boldsymbol x)}
$$

가 된다. $\boldsymbol E$와 마찬가지로 $\boldsymbol e$도 대칭인 무차원 텐서다.

**현재 방향의 신장과 변형률 값의 의미**

현재 선분의 단위방향을 $\boldsymbol n$이라 하여
$d\boldsymbol x=\ell\boldsymbol n$을 대입하고, 해당 선분의 신장비를
$\Lambda=\ell/\ell_0$라 하면

$$
\boldsymbol n\cdot(\boldsymbol e\cdot\boldsymbol n)
=\frac{\ell^2-\ell_0^2}{2\ell^2}
=\frac12(1-\Lambda^{-2}).
$$

2.2.1절의 $\boldsymbol N\cdot(\boldsymbol E\cdot\boldsymbol N)
=(\ell^2-\ell_0^2)/(2\ell_0^2)$와 비교하면,
**같은 제곱 길이 차이를 각각 기준 길이와 현재 길이의 제곱으로 나누고 있다**.
여기서 $\boldsymbol N$과 $\boldsymbol n$은 같은 물질 선분의 변형 전후 방향이며,
일반적으로 서로 다르다.
예를 들어 1차원에서 $\Lambda=1.5$이면 $E=0.625$, $e\approx0.2778$이다.
두 값이 다른 것은 서로 다른 운동을 뜻해서가 아니라 변형률의 정의가 다르기 때문이다.

**Green–Lagrange 변형률과의 정확한 관계**

$\boldsymbol E=(\boldsymbol F^T\boldsymbol F-\boldsymbol I)/2$의 왼쪽에
$\boldsymbol F^{-T}$, 오른쪽에 $\boldsymbol F^{-1}$을 곱하면

$$
\begin{aligned}
\boldsymbol F^{-T}\boldsymbol E\boldsymbol F^{-1}
&=\frac12\boldsymbol F^{-T}
(\boldsymbol F^T\boldsymbol F-\boldsymbol I)\boldsymbol F^{-1}\\
&=\frac12\left[
(\boldsymbol F^{-T}\boldsymbol F^T)(\boldsymbol F\boldsymbol F^{-1})
-\boldsymbol F^{-T}\boldsymbol F^{-1}\right]\\
&=\frac12(\boldsymbol I-\boldsymbol F^{-T}\boldsymbol F^{-1})
=\boldsymbol e.
\end{aligned}
$$

따라서

$$
\boxed{\boldsymbol e=\boldsymbol F^{-T}\boldsymbol E\boldsymbol F^{-1}},
\qquad
\boxed{\boldsymbol E=\boldsymbol F^T\boldsymbol e\boldsymbol F}.
$$

이 관계를 통해 두 텐서는 같은 길이 변화를 서로 다른 배치의 선분으로 표현한다.

**현재 좌표의 변위구배로 전개하기**

2.1절에서 구한 $\boldsymbol F^{-1}=\boldsymbol I-\nabla_x\boldsymbol u_E$를 이용하자.
현재 좌표에 대한 변위구배를 $\boldsymbol h=\nabla_x\boldsymbol u_E$라 쓰면

$$
\begin{aligned}
\boldsymbol e
&=\frac12\left[\boldsymbol I
-(\boldsymbol I-\boldsymbol h)^T(\boldsymbol I-\boldsymbol h)\right]\\
&=\frac12\left[\boldsymbol I
-(\boldsymbol I-\boldsymbol h^T)(\boldsymbol I-\boldsymbol h)\right]\\
&=\frac12\left[\boldsymbol I
-(\boldsymbol I-\boldsymbol h-\boldsymbol h^T+\boldsymbol h^T\boldsymbol h)\right]\\
&=\frac12(\boldsymbol h+\boldsymbol h^T-\boldsymbol h^T\boldsymbol h).
\end{aligned}
$$

기준 좌표 구배 $\boldsymbol H=\nabla_X\boldsymbol u_L$로 쓴
$\boldsymbol E=(\boldsymbol H+\boldsymbol H^T+\boldsymbol H^T\boldsymbol H)/2$와 달리
이차항 앞에 음수가 붙는다. 다만 $\boldsymbol h$와 $\boldsymbol H$도 서로 다르므로,
같은 구배를 넣고 부호만 바꾸어 두 변형률을 계산하면 안 된다.

실제로 $\boldsymbol h=\boldsymbol I-\boldsymbol F^{-1}
=\boldsymbol H(\boldsymbol I+\boldsymbol H)^{-1}$이므로,
$\|\boldsymbol H\|\ll1$이면 $\boldsymbol h\approx\boldsymbol H$이고
이차항을 생략하여

$$
\boldsymbol e\approx\frac12(\boldsymbol h+\boldsymbol h^T)
\approx\frac12(\boldsymbol H+\boldsymbol H^T)
=\boldsymbol\varepsilon\approx\boldsymbol E
$$

를 얻는다. 즉 작은 변위구배의 범위에서는 두 유한변형률이 모두 기존 미소변형률로 근사된다.

### 2.2.4. 실험과의 연결: DIC로 측정한 변위장에서 변형률 구하기

**DIC (Digital Image Correlation, 디지털 영상 상관법)**는 변형 전후의 시편 표면 영상을
비교하여 스페클(speckle) 무늬의 이동을 추적하고, 표면의 변위장을 구하는 방법이다.
기준 영상의 물질점 위치를 $\boldsymbol X$, 변형 후 대응 위치를 $\boldsymbol x$로 보면,
이 측정은 앞서 배운 $\boldsymbol u_L(\boldsymbol X)=\boldsymbol x-\boldsymbol X$와 연결된다.

평평한 시편의 면내 운동을 측정하는 2D DIC에서는, 보정된 물리 좌표에 대한
두 변위 성분 $u_{L,1},u_{L,2}$로부터 면내 변형구배를 계산할 수 있다.

$$
[\boldsymbol F]=
\begin{bmatrix}
1+\dfrac{\partial u_{L,1}}{\partial X_1}&\dfrac{\partial u_{L,1}}{\partial X_2}\\
\dfrac{\partial u_{L,2}}{\partial X_1}&1+\dfrac{\partial u_{L,2}}{\partial X_2}
\end{bmatrix},
\qquad
\boldsymbol E=\frac12(\boldsymbol F^T\boldsymbol F-\boldsymbol I).
$$

즉 **영상의 대응점 탐색 → 변위장 → 변위구배 → 변형률**이라는 계산 흐름이다.
예를 들어 균일 인장에서 $u_{L,1}=0.2X_1$, $u_{L,2}=0$을 얻었다면
$\varepsilon_{11}=0.2$인 반면 $E_{11}=0.2+0.2^2/2=0.22$다.
따라서 DIC 결과의 “strain”을 읽을 때에는 소프트웨어가 출력한 값이
미소변형률, Green–Lagrange 변형률, 로그변형률 중 무엇인지 확인해야 한다.

실제 변형률 계산에는 이산 변위 자료의 국소 근사와 미분이 필요하므로,
변위의 측정 잡음과 평활화 범위가 결과에 영향을 준다.
또한 일반적인 단일 카메라 2D DIC는 면외 이동·회전에 민감하다.
스테레오 DIC는 표면의 3차원 위치와 변위를 측정할 수 있지만,
그것만으로 시편 내부의 전체 3차원 변형구배까지 얻는 것은 아니다.

<span id="113-1차원-인장과-강체회전의-비교"></span>

## 2.3. 1차원 인장과 강체회전의 비교

균일 인장 $x=\Lambda X$에서 **신장비 (stretch ratio)**는 $\Lambda=l/l_0>0$이다.
아래 척도들은 작은 인장에서는 비슷하지만 큰 인장에서는 달라진다.

| 변형률 척도 | 정의 | $\Lambda=1.5$ |
| ----------- | ---- | ------------ |
| 공칭·공학변형률 | $\Lambda-1$ | $0.5$ |
| Green–Lagrange 변형률 | $(\Lambda^2-1)/2$ | $0.625$ |
| Euler–Almansi 변형률 | $(1-\Lambda^{-2})/2$ | $0.2778$ |
| 로그변형률 (logarithmic strain) | $\ln\Lambda$ | $0.4055$ |

공칭변형률 $du_L/dX=\Lambda-1$은 이 1차원 문제에서는 큰 인장에도 정확하다.
다만 이를 일반적인 유한변형률 텐서와 동일시할 수는 없다.

1차원에서 $u_L=(\Lambda-1)X$이므로 미소변형률 식에 대입한 값은
$\varepsilon=du_L/dX=\Lambda-1$이다. 따라서 2.2.2절의 관계는

$$
\boxed{E=\frac12(\Lambda^2-1)
=\varepsilon+\frac12\varepsilon^2}
$$

로 단순해진다. 길이가 1% 증가하면 $\varepsilon=0.01$, $E=0.01005$로 가깝지만,
50% 증가하면 $\varepsilon=0.5$, $E=0.625$로 차이가 커진다.
여기서 $E=0.625$를 길이가 62.5% 증가했다는 뜻으로 해석하면 안 된다.
초기 길이 $l_0$와 현재 길이 $l$에 대해 두 척도의 정의는

$$
\varepsilon=\frac{l-l_0}{l_0},
\qquad E=\frac{l^2-l_0^2}{2l_0^2}
$$

로 다르다. $E$로부터 실제 신장비를 구하려면 $\Lambda=\sqrt{1+2E}$를 사용한다.


이제 강체운동 $\boldsymbol x=\boldsymbol Q\cdot \boldsymbol X+\boldsymbol c$를 생각하자.
$\boldsymbol Q^T\cdot \boldsymbol Q=\boldsymbol I$, $\det\boldsymbol Q=1$인 회전텐서에 대해

$$
\boldsymbol F=\boldsymbol Q,
\qquad \boldsymbol E=\boldsymbol e=\boldsymbol 0.
$$

반면 평면에서 $\theta$만큼 회전할 때 미소변형률 공식을 기준 좌표 구배에 적용하면

$$
\frac12[(\boldsymbol Q-\boldsymbol I)+(\boldsymbol Q-\boldsymbol I)^T]
=(\cos\theta-1)\boldsymbol I
$$

가 된다. $90^\circ$ 회전에서는 $-\boldsymbol I$라는 잘못된 변형률이 나온다.
작은 $\theta$에서는 $\cos\theta-1\approx-\theta^2/2$가 이차항이므로
미소변형 근사에서 무시할 수 있다.

이 예에서 이차항의 역할을 직접 확인할 수 있다. 2차원 회전에서는
$\boldsymbol H=\boldsymbol Q-\boldsymbol I$이므로

$$
\begin{aligned}
\frac12\boldsymbol H^T\cdot\boldsymbol H
&=\frac12(\boldsymbol Q^T-\boldsymbol I)
\cdot(\boldsymbol Q-\boldsymbol I)\\
&=\frac12(2\boldsymbol I-\boldsymbol Q-\boldsymbol Q^T)\\
&=(1-\cos\theta)\boldsymbol I.
\end{aligned}
$$

따라서 미소변형률 식에서 나온 항을 이차항이 정확히 상쇄한다.

$$
\boldsymbol E
=\underbrace{(\cos\theta-1)\boldsymbol I}_{\boldsymbol\varepsilon}
+\underbrace{(1-\cos\theta)\boldsymbol I}_{\boldsymbol H^T\cdot\boldsymbol H/2}
=\boldsymbol0.
$$

즉 이차항은 큰 신장에서의 수치 보정뿐 아니라, **유한한 강체회전을 변형으로
잘못 계산하지 않도록 하는 데에도 필요하다**. 다음 절의 극분해는
$\boldsymbol F$에 함께 들어 있는 회전과 신장을 분리하는 방법이다.

<span id="12-극분해-polar-decomposition"></span>

# 3. 극분해 (polar decomposition)

<span id="121-회전과-신장의-분리"></span>

## 3.1. 회전과 신장의 분리

$\det\boldsymbol F>0$인 변형구배는 다음과 같이 유일하게 분해된다.

$$
\boxed{\boldsymbol F=\boldsymbol R\cdot \boldsymbol U=\boldsymbol V\cdot \boldsymbol R}.
$$

$\boldsymbol R$은 $\boldsymbol R^T\cdot \boldsymbol R=\boldsymbol I$, $\det\boldsymbol R=1$을 만족하는
회전텐서(rotation tensor)다. $\boldsymbol U$와 $\boldsymbol V$는 대칭 양의 정부호인
우신장텐서(right stretch tensor)와 좌신장텐서(left stretch tensor)다.
이들의 고유값은 양의 주신장비(principal stretches)다.

텐서의 연속 작용은 오른쪽부터 적용하므로 $\boldsymbol R\cdot \boldsymbol U$는 기준 배치 방향에서 신장한 뒤
회전하는 표현이고, $\boldsymbol V\cdot \boldsymbol R$는 회전한 뒤 현재 배치 방향에서 신장하는 표현이다.
이는 같은 국소 변형을 나타내는 두 수학적 표현이며 실제 변형의 시간 순서를 뜻하지 않는다.

[기본 자료 8절]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05_displacement_strain.md %}#8-변위구배의-대칭부분과-반대칭부분)의 $\nabla_X\boldsymbol u=\boldsymbol\varepsilon+\boldsymbol\omega$는
작은 변형·회전의 **가법적 분해**이고, 극분해는 유한변형의 **곱셈적 분해**다.
극분해의 회전·신장은 탄성·소성 성분을 분리하는 $\boldsymbol F=\boldsymbol F_e\cdot \boldsymbol F_p$와는
다른 구분이다.

<span id="122-신장-후-회전하는-예제"></span>

## 3.2. 신장 후 회전하는 예제

같은 정규직교 기저의 성분 배열로 계산한다. 평면에서 $X_1$방향으로 2배 신장한 뒤 $90^\circ$ 회전하면

$$
[\boldsymbol U]=\begin{bmatrix}2&0\\0&1\end{bmatrix},
\qquad [\boldsymbol R]=\begin{bmatrix}0&-1\\1&0\end{bmatrix},
\qquad [\boldsymbol F]=[\boldsymbol R][\boldsymbol U]=\begin{bmatrix}0&-1\\2&0\end{bmatrix}.
$$

이때

$$
[\boldsymbol V]=[\boldsymbol R][\boldsymbol U][\boldsymbol R]^T=\begin{bmatrix}1&0\\0&2\end{bmatrix},
\qquad [\boldsymbol E]=\frac12([\boldsymbol U]^2-[\boldsymbol I])=\begin{bmatrix}1.5&0\\0&0\end{bmatrix}.
$$

기준 배치의 $X_1$방향 신장이 회전 후 현재 배치의 $x_2$방향 신장으로 표현된다.
$\boldsymbol E$는 기준 배치에서의 신장을 나타내며 강체회전 때문에 값이 바뀌지 않는다.

# 4. 요약

| 개념                          | 공식                                                                         |
| ----------------------------- | ---------------------------------------------------------------------------- |
| 두 기술법의 미소변형률 근사 | $\varepsilon = du_L/dX\approx du_E/dx$ |
| 변형구배 | $\boldsymbol F=\partial\boldsymbol x/\partial\boldsymbol X=\boldsymbol I+\nabla_X\boldsymbol u_L$ |
| 체적비 | $J=\det\boldsymbol F$ |
| Green–Lagrange 변형률 | $\boldsymbol E=(\boldsymbol F^T\cdot \boldsymbol F-\boldsymbol I)/2$ |
| Euler–Almansi 변형률 | $\boldsymbol e=(\boldsymbol I-\boldsymbol F^{-T}\cdot \boldsymbol F^{-1})/2$ |
| 극분해 | $\boldsymbol F=\boldsymbol R\cdot \boldsymbol U=\boldsymbol V\cdot \boldsymbol R$ |

# 5. 연습문제

## 문제 1. 같은 운동을 두 좌표로 표현하기

좌표와 변위의 단위가 mm일 때, 1차원 운동이 $x=1.5X+2$로 주어진다.
$u_L(X)$, 역변환 $X(x)$, $u_E(x)$를 구하시오.
$X=4\,\mathrm{mm}$인 물질점에서 두 표현의 변위값이 같음을 확인하고,
$du_L/dX$와 $du_E/dx$가 다른 이유를 설명하시오.

<!--
풀이와 해답:
$u_L=0.5X+2$, $X=(x-2)/1.5$, $u_E=x-(x-2)/1.5=x/3+4/3$이다.
$X=4$인 점은 $x=8$로 이동하므로 두 식 모두 변위 $4$ mm를 준다.
$du_L/dX=1/2$, $du_E/dx=1/3$이다. 같은 운동이지만 미분 좌표가 다르다.
$F=1.5$이고 $1-du_E/dx=2/3=F^{-1}$도 성립한다.
-->

## 문제 2. 변형구배와 선분의 변화

2차원 운동이 다음과 같다.

$$
x_1=1.2X_1+0.3X_2,\qquad x_2=0.8X_2.
$$

$\boldsymbol F$와 $J$를 구하시오. 기준 선분
$d\boldsymbol X=\ell_0(0,1)^T$의 변형 후 벡터와 신장비를 구하고,
면적 변화율 $J-1$을 계산하시오. 여기서 $\ell_0>0$은 미소 선분의 초기 길이다.

<!--
풀이와 해답:
$$
[\boldsymbol F]=\begin{bmatrix}1.2&0.3\\0&0.8\end{bmatrix},
\qquad J=1.2\times0.8=0.96.
$$
$d\boldsymbol x=\ell_0(0.3,0.8)^T$이므로 신장비는
$\sqrt{0.3^2+0.8^2}=\sqrt{0.73}\approx0.8544$다.
$J-1=-0.04$이므로 면적은 4% 감소한다.
-->

## 문제 3. 정확한 비압축성 조건

3차원 변형구배가 $\boldsymbol F=\operatorname{diag}(1.2,1.2,a)$이며 $a>0$이다.
체적이 보존되도록 $a$를 정하시오. 이때
$\boldsymbol\varepsilon=(\boldsymbol F+\boldsymbol F^T)/2-\boldsymbol I$의
대각합을 계산하고, 유한변형에서 $\operatorname{tr}\boldsymbol\varepsilon=0$을
정확한 비압축성 조건으로 사용할 수 있는지 설명하시오.

<!--
풀이와 해답:
$J=1.44a=1$이므로 $a=25/36\approx0.694444$이다.
$\operatorname{tr}\boldsymbol\varepsilon=0.2+0.2+(25/36-1)=17/180\approx0.094444$로 0이 아니다.
정확한 조건은 $\det\boldsymbol F=1$이다.
$J\approx1+\operatorname{tr}\boldsymbol\varepsilon$는 변위구배가 작을 때의 일차 근사다.
-->

## 문제 4. 1차원 변형률 척도의 비교

길이 $100\,\mathrm{mm}$인 막대가 균일하게 늘어나 $120\,\mathrm{mm}$가 되었다.
신장비 $\Lambda$, 공칭변형률, Green–Lagrange 변형률 $E$,
Euler–Almansi 변형률 $e$, 로그변형률을 구하시오.
$E=\varepsilon+\varepsilon^2/2$를 확인하고, $E$를 길이 증가율로 읽으면 안 되는 이유를 설명하시오.

<!--
풀이와 해답:
$\Lambda=1.2$, $\varepsilon=0.2$, $E=(1.44-1)/2=0.22$,
$e=(1-1/1.44)/2=11/72\approx0.152778$, $\ln\Lambda\approx0.182322$이다.
$0.2+0.2^2/2=0.22$다. 길이는 20% 증가했으며,
$E$는 제곱 길이의 차이를 $2l_0^2$로 나눈 값이다.
-->

## 문제 5. 큰 병진과 큰 회전

2차원에서 다음 두 운동의 $\boldsymbol H$, $\boldsymbol\varepsilon$, $\boldsymbol E$를 구하시오.

$$
\text{(가)}\quad \boldsymbol x=\boldsymbol X+\boldsymbol c,
\qquad
\text{(나)}\quad \boldsymbol x=\boldsymbol Q\boldsymbol X,
\qquad
[\boldsymbol Q]=\begin{bmatrix}0&-1\\1&0\end{bmatrix}.
$$

$\boldsymbol c$는 위치에 무관한 상수벡터다.
(나)에서 $\boldsymbol H^T\boldsymbol H/2$를 계산하여 이차항의 역할을 확인하시오.
두 운동의 결과로부터 미소변형 근사의 적용 기준을 설명하시오.

<!--
풀이와 해답:
(가)는 $\boldsymbol H=\boldsymbol0$이고 두 변형률 모두 0이다.
(나)는 $\boldsymbol H=\boldsymbol Q-\boldsymbol I$,
$\boldsymbol\varepsilon=-\boldsymbol I$, $\boldsymbol E=\boldsymbol0$이다.
$\boldsymbol H^T\boldsymbol H/2=\boldsymbol I$가 미소변형률 식의 값을 상쇄한다.
큰 병진은 변위구배를 만들지 않지만 큰 회전은 큰 변위구배를 만든다.
미소변형 근사의 기준은 변위의 크기가 아니라 $\|\boldsymbol H\|\ll1$이다.
-->

## 문제 6. 유한 단순전단

2차원 운동이 $x_1=X_1+\gamma X_2$, $x_2=X_2$로 주어진다.
$\boldsymbol F$, $J$, $\boldsymbol\varepsilon$, $\boldsymbol E$를 구하시오.
$\gamma=0.5$일 때 $E_{22}$를 계산하고, 처음에 $X_2$방향이었던 선분의
신장비와 연결하여 이 성분이 0이 아닌 이유를 설명하시오.

<!--
풀이와 해답:
$$
[\boldsymbol F]=\begin{bmatrix}1&\gamma\\0&1\end{bmatrix},\qquad J=1,
$$
$$
[\boldsymbol\varepsilon]=\begin{bmatrix}0&\gamma/2\\\gamma/2&0\end{bmatrix},
\qquad
[\boldsymbol E]=\begin{bmatrix}0&\gamma/2\\\gamma/2&\gamma^2/2\end{bmatrix}.
$$
$E_{22}=0.125$다. 초기 선분 $\ell_0(0,1)^T$는 $\ell_0(\gamma,1)^T$가 되므로
신장비가 $\sqrt{1+\gamma^2}$다. 따라서 $E_{22}=[(1+\gamma^2)-1]/2$이다.
면적 보존은 모든 방향의 길이 보존을 뜻하지 않는다.
-->
