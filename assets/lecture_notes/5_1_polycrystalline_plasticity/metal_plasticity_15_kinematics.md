---
layout: distill
title: VPSC의 운동학
description: VPSC의 속도구배, 결정립 형상 변화와 격자 회전
target: 대학원
permalink:
featured: true
prerequisite: 유한변형의 운동학, 결정소성의 슬립과 항복 조건, 평균장 다결정 소성 모델
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

- [1. 운동학 개요](#1-운동학-개요)
  - [1.1. 속도구배](#11-속도구배)
  - [1.2. 운동학](#12-운동학)
- [2. 변형구배](#2-변형구배)
- [3. 결정립의 누적 변형과 형상](#3-결정립의-누적-변형과-형상)
- [4. 점의 속도](#4-점의-속도)
- [5. 속도구배](#5-속도구배)
- [6. 연습 문제](#6-연습-문제)


이 자료는 VPSC (Visco-Plastic Self-Consistent)에서 사용하는 속도구배, 결정립 형상 변화와 격자 회전을 다룬다.
기본적인 유한변형의 정의는
[유한변형의 운동학]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %})을 참고한다.

# 1. 운동학 개요

## 1.1. 속도구배

$$
\boldsymbol L = \boldsymbol D + \boldsymbol W
$$

  - $\boldsymbol L$: 속도구배 텐서(velocity gradient tensor)
  - $\boldsymbol D$: 변형률속도 텐서(rate-of-deformation tensor)
  - $\boldsymbol W$: 스핀 텐서(spin tensor)

## 1.2. 운동학

VPSC에서는 거시적 속도구배와 결정립별 국소 속도구배를 구분한다.
결정립의 국소 변형률속도와 회전은 자기일관성 계산으로 결정하므로,
모든 결정립에 같은 속도구배를 부과한다고 가정하지 않는다.

- $\boldsymbol X$ : 초기 위치; Reference configuration

- $\boldsymbol x$ : 변화된 위치; current configuration

- $\boldsymbol{X}\rightarrow\boldsymbol{x}(t)$

# 2. 변형구배

- $\boldsymbol F=\frac{\partial \boldsymbol x}{\partial \boldsymbol X}$

- Change in infinitesimal line vector ($d\boldsymbol X$)

$$
d\boldsymbol x = \boldsymbol F \cdot d\boldsymbol X
$$

- 체적비는 $J=\det\boldsymbol F=dv/dV$로 나타낸다. 물리적으로 허용되는 변형에서는
  $J>0$이어야 하고, 비압축성 변형에서는 $J=1$이다.

<span id="3-극분해"></span>

# 3. 결정립의 누적 변형과 형상

결정립별 속도구배 $\boldsymbol L^g$로 누적 변형구배 $\boldsymbol F^g$를 갱신한다.
여기서 $g$는 결정립을 나타낸다.

$$
\dot{\boldsymbol F}^g=\boldsymbol L^g\cdot\boldsymbol F^g.
$$

이 누적 변형은 결정립을 나타내는 타원체의 형상과 방향을 갱신하는 데 사용된다.
타원체 축의 회전과 결정격자의 회전은 구분한다.

# 4. 점의 속도

국소 속도장은 $\boldsymbol v\equiv\boldsymbol v(\boldsymbol x,t)$이며, 그 공간미분이 결정립의 속도구배다.

# 5. 속도구배

- 정의: $(\nabla_x\boldsymbol v)_{ij}=\partial v_i/\partial x_j$. 위의 점은 같은 물질점을 따라가는 시간미분이다.
$$
\boldsymbol L = \nabla_x \boldsymbol v=\dot{\boldsymbol F}\cdot\boldsymbol F^{-1}
$$

$$
[\boldsymbol L]=
\begin{bmatrix}
\frac{\partial v_1}{\partial x_1} & \frac{\partial v_1}{\partial x_2} & \frac{\partial v_1}{\partial x_3} \\
\frac{\partial v_2}{\partial x_1} & \frac{\partial v_2}{\partial x_2} & \frac{\partial v_2}{\partial x_3} \\
\frac{\partial v_3}{\partial x_1} & \frac{\partial v_3}{\partial x_2} & \frac{\partial v_3}{\partial x_3}
\end{bmatrix}
$$


- 속도구배의 가산 분해

$$
\boldsymbol L = \boldsymbol D+\boldsymbol W
$$

$$
\boldsymbol D = \frac{1}{2}\big(\boldsymbol L+\boldsymbol L^T\big)
$$

$$
\boldsymbol W = \frac{1}{2}\big(\boldsymbol L-\boldsymbol L^T\big)
$$

- 경계조건에서는 $\boldsymbol L$의 성분이나 응력 $\boldsymbol\sigma$의 성분 중
  일부를 지정할 수 있다. 한 성분에 두 조건을 동시에 부과하지 않도록 주의한다.

$$
\begin{bmatrix}
L_{11}&L_{12}&L_{13}\\
L_{21}&L_{22}&L_{23}\\
L_{31}&L_{32}&L_{33}
\end{bmatrix}
$$

<span id="유한변형-소성에서의-곱셈-분해"></span>

## 슬립에 의한 변형과 격자 회전

동일한 시료 좌표계에서, 전단에 의한 속도구배는

$$
\boldsymbol L^{\mathrm{slip},g}
=\sum_s\dot\gamma^{s,g}\boldsymbol b^{s,g}\otimes\boldsymbol n^{s,g}
$$

로 쓴다. $\boldsymbol b^{s,g}$와 $\boldsymbol n^{s,g}$는 각각 단위 슬립 방향과 면 법선이다.
$\dot\gamma^{s,g}$는 해당 계의 전단속도다. 이 절은 슬립을 중심으로 설명한다.

$$
\boldsymbol W^{\mathrm{slip},g}
=\frac12(\boldsymbol L^{\mathrm{slip},g}-(\boldsymbol L^{\mathrm{slip},g})^T),
\qquad
\boldsymbol W^{\mathrm{lat},g}
=\boldsymbol W^g-\boldsymbol W^{\mathrm{slip},g}.
$$

격자 스핀 $\boldsymbol W^{\mathrm{lat},g}$은 결정립의 전체 스핀에서 슬립 스핀을 뺀 값이다.
따라서 결정방위의 변화는 전체 스핀만으로 결정되지 않는다.
이는 탄성 변형률속도를 별도로 풀지 않는 점소성 VPSC의 설명이며,
탄성·소성 변형구배의 곱셈 분해를 사용하는 모델과 구분한다.

VPSC8의 구현은 [공식 소스의 UPDATE_ORIENTATION 및 UPDATE_FIJ](https://github.com/lanl/VPSC_code/blob/main/vpsc8sub.for)를 참고한다.
쌍정에 의한 별도의 방위 재배향과 결정립 간 공동 회전은 추가 규칙으로 처리된다.

# 6. 연습 문제

## 문제 1

변형구배 $\boldsymbol F$가 단위행렬이면 물체의 국소적인 변형은 어떤 상태인가?

<!--
풀이와 해답:
기준배치와 동일하여 국소적인 늘어남이나 회전이 없는 상태이다.
-->

## 문제 2

속도구배 $\boldsymbol L$을 대칭부분과 반대칭부분으로 분해하여 쓰시오.

<!--
풀이와 해답:
L=D+W이며 D=(L+L^T)/2, W=(L-L^T)/2이다.
-->

## 문제 3

$\boldsymbol D$와 $\boldsymbol W$가 각각 나타내는 운동학적 의미를 쓰시오.

<!--
풀이와 해답:
D는 변형률속도 텐서이고 W는 스핀 텐서로 국소 회전을 나타낸다.
-->

## 문제 4

슬립 스핀이 0이 아닐 때 결정립의 전체 스핀과 격자 스핀이 같은지 설명하시오.

<!--
풀이와 해답:
같지 않다. 격자 스핀은 전체 스핀에서 슬립 스핀을 뺀 값이다.
-->
