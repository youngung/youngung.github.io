---
layout: distill
title: 유한변형의 운동학
description: Lagrangian·Eulerian 기술법, 변형구배, 유한변형률과 극분해
target: 학부 고학년
permalink:
featured: true
prerequisite: 변위와 미소변형률
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


이 자료는 연속체의 좌표 기술법, 변형구배, 유한변형률과 극분해를 다룬다.
VPSC에 적용하는 속도구배와 결정립의 운동은
[VPSC의 운동학]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_15_kinematics.md %})에서 다룬다.

관련 자료는 다음 순서로 읽을 수 있다.

- [변위와 미소변형률]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05_displacement_strain.md %})
- [변위와 미소변형률 연습문제]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %})
- [유한변형의 운동학]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %})
- [물질미분과 ALE 기술법]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %})

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

변형 전후 선분 길이의 제곱 차이[^squared-length]는

$$
d\boldsymbol x\cdot d\boldsymbol x-d\boldsymbol X\cdot d\boldsymbol X
=d\boldsymbol X\cdot\left((\boldsymbol F^T\cdot\boldsymbol F-\boldsymbol I)\cdot d\boldsymbol X\right)
=2d\boldsymbol X\cdot(\boldsymbol E\cdot d\boldsymbol X)
$$

이다.[^line-element-quadratic-form] 따라서 **Green–Lagrange 변형률 (Green–Lagrange strain)**, $\boldsymbol E$는

$$
\boxed{\boldsymbol E=\frac12(\boldsymbol F^T\cdot \boldsymbol F-\boldsymbol I)}.
$$

$\boldsymbol H=\nabla_X\boldsymbol u_L$을 대입하면

$$
\boldsymbol E=\frac12(\boldsymbol H+\boldsymbol H^T+\boldsymbol H^T\cdot \boldsymbol H).
$$

미소변형률은 이 식에서 이차항 $\boldsymbol H^T\cdot \boldsymbol H$를 무시한 근사다.
즉 $\|\boldsymbol H\|\ll1$일 때 $\boldsymbol E\approx\boldsymbol\varepsilon$이다.
병진변위(translational displacement)의 크기(즉 $\|\boldsymbol u_L\|$)보다 **변위구배**($\boldsymbol H=\nabla_X\boldsymbol u_L$)**의 크기**가 근사의 기준이라는 점에 주목하자.

같은 길이 변화를 현재 선분 $d\boldsymbol x$로 표현하면
**Euler–Almansi 변형률 (Euler–Almansi strain)**, $\boldsymbol e$를 얻는다.

$$
\boxed{\boldsymbol e=\frac12(\boldsymbol I-\boldsymbol F^{-T}\cdot \boldsymbol F^{-1})},
\qquad
d\boldsymbol x\cdot d\boldsymbol x-d\boldsymbol X\cdot d\boldsymbol X
=2d\boldsymbol x\cdot(\boldsymbol e\cdot d\boldsymbol x).
$$

$\boldsymbol F^{-T}=(\boldsymbol F^{-1})^T$다. $\boldsymbol E$와 $\boldsymbol e$는 각각 기준 배치와
현재 배치의 선분으로 같은 길이 변화를 표현하지만 수치는 일반적으로 다르다.
좌표 기술법을 선택하는 것과 변형률 척도를 선택하는 것은 구분해야 한다.

[^squared-length]: 벡터 $\boldsymbol v$의 길이는 $\|\boldsymbol v\|=\sqrt{\boldsymbol v\cdot\boldsymbol v}$이고, 길이의 제곱은 $\|\boldsymbol v\|^2=\boldsymbol v\cdot\boldsymbol v$다. 따라서 선분의 제곱 길이는 각각 $d\boldsymbol X\cdot d\boldsymbol X$와 $d\boldsymbol x\cdot d\boldsymbol x$로 표현된다. 길이 자체 대신 제곱을 사용하면 제곱근 없이 내적과 텐서로 길이 변화를 표현할 수 있다. 실제 길이는 이 값의 제곱근이며, 제곱 길이와 길이는 구분해야 한다. $d\boldsymbol x=\boldsymbol F\cdot d\boldsymbol X$를 대입하면 $d\boldsymbol x\cdot d\boldsymbol x= [d\boldsymbol X]^T[\boldsymbol F]^T[\boldsymbol F][d\boldsymbol X]$가 되어 본문의 관계를 얻는다.

[^line-element-quadratic-form]: 같은 정규직교 기저에서 미소 선분의 성분을 열벡터 $[d\boldsymbol X]$, $[d\boldsymbol x]$로 배열한다. 대괄호는 성분 배열이며, 내적은 $\boldsymbol a\cdot\boldsymbol b=[\boldsymbol a]^T[\boldsymbol b]$다. 위첨자 $T$는 전치(transpose)로, 열벡터를 행벡터로 바꾼다. $[d\boldsymbol x]=[\boldsymbol F][d\boldsymbol X]$에 곱의 전치 규칙 $([\boldsymbol A][\boldsymbol B])^T=[\boldsymbol B]^T[\boldsymbol A]^T$를 적용하면

    $$
    \begin{aligned}
    d\boldsymbol x\cdot d\boldsymbol x
    &=[d\boldsymbol x]^T[d\boldsymbol x]\\
    &=([\boldsymbol F][d\boldsymbol X])^T([\boldsymbol F][d\boldsymbol X])\\
    &=[d\boldsymbol X]^T[\boldsymbol F]^T[\boldsymbol F][d\boldsymbol X].
    \end{aligned}
    $$

    기준 선분에 대해서는 $d\boldsymbol X\cdot d\boldsymbol X=[d\boldsymbol X]^T[\boldsymbol I][d\boldsymbol X]$이므로, 제곱 길이의 차이는

    $$
    \begin{aligned}
    d\boldsymbol x\cdot d\boldsymbol x-d\boldsymbol X\cdot d\boldsymbol X
    &=[d\boldsymbol X]^T([\boldsymbol F]^T[\boldsymbol F]-[\boldsymbol I])[d\boldsymbol X]\\
    &=2[d\boldsymbol X]^T[\boldsymbol E][d\boldsymbol X].
    \end{aligned}
    $$

    이는 **이차형식 (quadratic form)**이다. 3차원에서 배열 크기는 $(1\times3)(3\times3)(3\times1)$이므로 결과는 제곱 길이 단위의 스칼라다. 성분으로는 $dX_i(F_{ki}F_{kj}-\delta_{ij})dX_j$이며, 반복 인덱스에 대해 합한다. 여기서 $\boldsymbol E=(\boldsymbol F^T\cdot\boldsymbol F-\boldsymbol I)/2$다. 특히 $d\boldsymbol X=\ell_0\boldsymbol N$인 선분($\|\boldsymbol N\|=1$)에 대해 $\boldsymbol N\cdot(\boldsymbol E\cdot\boldsymbol N)=[\boldsymbol N]^T[\boldsymbol E][\boldsymbol N]=(\ell^2-\ell_0^2)/(2\ell_0^2)$이므로, 이차형식은 기준 방향 $\boldsymbol N$의 선분이 얼마나 늘어나거나 줄어드는지를 나타낸다. $\ell_0$와 $\ell$은 해당 미소 선분의 변형 전후 길이다.

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

$$
\boldsymbol C=\boldsymbol F^T\cdot \boldsymbol F=\boldsymbol U^2,
\qquad \boldsymbol B=\boldsymbol F\cdot \boldsymbol F^T=\boldsymbol V^2,
$$

$$
\boldsymbol U=\sqrt{\boldsymbol C},
\qquad \boldsymbol V=\sqrt{\boldsymbol B},
\qquad \boldsymbol R=\boldsymbol F\cdot \boldsymbol U^{-1},
\qquad \boldsymbol V=\boldsymbol R\cdot \boldsymbol U\cdot \boldsymbol R^T.
$$

$\boldsymbol C$와 $\boldsymbol B$는 각각 우·좌 Cauchy–Green 변형텐서다.
행렬의 제곱근은 성분마다 제곱근을 취하는 것이 아니다. 예를 들어
$[\boldsymbol C]=[\boldsymbol P]\operatorname{diag}(\Lambda_1^2,\Lambda_2^2,\Lambda_3^2)[\boldsymbol P]^T$에서
$[\boldsymbol P]$가 정규직교 고유벡터를 열로 갖는 행렬이면,
$[\boldsymbol U]=[\boldsymbol P]\operatorname{diag}(\Lambda_1,\Lambda_2,\Lambda_3)[\boldsymbol P]^T$다.

텐서의 거듭제곱은 수축의 반복을 뜻한다. 예를 들어 $\boldsymbol U^2=\boldsymbol U\cdot\boldsymbol U$다.
신장텐서로 유한변형률을 쓰면

$$
\boldsymbol E=\frac12(\boldsymbol U^2-\boldsymbol I),
\qquad \boldsymbol e=\frac12(\boldsymbol I-\boldsymbol V^{-2}).
$$

강체회전에서는 $\boldsymbol U=\boldsymbol V=\boldsymbol I$이므로 변형률은 0이다.
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
변형구배·극분해·Green–Lagrange 변형률의 추가 학습은
[MIT OCW 강의 3](https://ocw.mit.edu/courses/res-2-002-finite-element-procedures-for-solids-and-structures-spring-2010/resources/lecture-3-1/)을 참고한다.

# 4. 요약

| 개념                          | 공식                                                                         |
| ----------------------------- | ---------------------------------------------------------------------------- |
| 두 기술법의 미소변형률 근사 | $\varepsilon = du_L/dX\approx du_E/dx$ |
| 변형구배 | $\boldsymbol F=\partial\boldsymbol x/\partial\boldsymbol X=\boldsymbol I+\nabla_X\boldsymbol u_L$ |
| 체적비 | $J=\det\boldsymbol F$ |
| Green–Lagrange 변형률 | $\boldsymbol E=(\boldsymbol F^T\cdot \boldsymbol F-\boldsymbol I)/2$ |
| Euler–Almansi 변형률 | $\boldsymbol e=(\boldsymbol I-\boldsymbol F^{-T}\cdot \boldsymbol F^{-1})/2$ |
| 극분해 | $\boldsymbol F=\boldsymbol R\cdot \boldsymbol U=\boldsymbol V\cdot \boldsymbol R$ |
