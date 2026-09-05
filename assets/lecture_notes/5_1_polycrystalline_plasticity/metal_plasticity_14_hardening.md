---
layout: distill
title: 경화와 이방성
description: 소성 경화, 이방성 항복조건과 결정소성 개요
target: 학부 고학년
permalink:
featured: true
prerequisite: 소성 항복, 소성 유동법칙
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


- [1. Hardening](#1-hardening)
  - [1.1. Phenomenological plasticity에서의 가공경화](#11-phenomenological-plasticity에서의-가공경화)
  - [1.2. strain hardening described in crystal plasticity framework.](#12-strain-hardening-described-in-crystal-plasticity-framework)
- [2. Anisotropy](#2-anisotropy)
  - [2.1. Hill's yield criterion](#21-hills-yield-criterion)
  - [2.2. Barlat's yield criterion](#22-barlats-yield-criterion)
- [3. Slip system \& crystal orientation](#3-slip-system--crystal-orientation)
- [4. 평균장 다결정 소성 모델](#4-평균장-다결정-소성-모델)

# 1. Hardening

- 소성 변형이 증가할 수록 강도가 증가한다.

- 전위 밀도가 증가하며, 항복 응력이 소성 변형량의 증가함에 따라 함께 높아진다.

## 1.1. Phenomenological plasticity에서의 가공경화

- Isotropic hardening

  - 항복 조건

    $$
    f(\boldsymbol\sigma)=\sigma^Y
    $$

    $$
    \rightarrow f(\boldsymbol\sigma)-\sigma^Y=0
    $$

  - 항복면이 동일한 모양을 유지하면서 커진다. 이를 통해 경화 거동을 설명한다.
    따라서

    $\sigma^Y \equiv \sigma^Y(\boldsymbol\varepsilon^{pl})$

    $$
    \boldsymbol\varepsilon^{pl} \uparrow, \sigma^Y \uparrow
    $$

  - 가령 예를 들어, Hollomon의 경화 모형을 활용한다면 아래와 같이 항복 강도를
   소성변형률의 크기($|\boldsymbol\varepsilon^{eq}|$)의 변화에 대한 함수로
   표현할 수 있겠다 - **실제로 소성 변형률의 단순 크기를 활용하진 않는다**.

    $$
    \sigma^Y = \sigma^Y_0 +K(|\boldsymbol\varepsilon^{pl}|)^n
    $$

- Kinematic hardening

  - 항복면을 응력 공간에서 '이동'시켜 경화현상 설명

- Combination of isotropic & kinematic hardening

## 1.2. strain hardening described in crystal plasticity framework.

- By expressing $\tau_c$ as a function of strains accumulcated in grain,
 one can describe the strain hardening.

- For example, let's say the strain of a grain is expressed as below:

$$
\dot{\boldsymbol\varepsilon}^{pl}=\dot\gamma_0\sum_s\boldsymbol m^s\bigg(\frac{|\boldsymbol m^s : \boldsymbol \sigma|}{\tau_c}\bigg)^n \text{sgn}(\boldsymbol m^s : \boldsymbol \sigma)
$$

- The CRSS $\tau_c$ can be expressed as slip shears accumulcated within grains via:

$$
\tau_c\equiv\tau_c\bigg(\sum_s\int_0^{t}\dot\gamma^s dt\bigg)
$$

# 2. Anisotropy

## 2.1. Hill's yield criterion

- Von Mises의 등가 응력에 계수를 도입하여, 이방성을 고려하였다. 이때 활용하는 응력 텐서 성분값은, 재료의 '압연' 공정 방향 좌표축을 활용한다. 즉, $\boldsymbol e_1 || \text{RD}, \boldsymbol e_2||\text{TD}, \boldsymbol e_3||\text{ND}$

$$
\sigma^{Hill} = \sqrt{F(\sigma_{22}-\sigma_{33})^2+G(\sigma_{33}-\sigma_{11})^2+H(\sigma_{11}-\sigma_{22})^2+2L\sigma_{23}^2+2M\sigma_{13}^2+2N\sigma_{12}^2}
$$

$$
\sigma^{Hill}-\sigma^Y=0 \text{ :  yield criterion}
$$


$$
\sigma^{Hill}-\sigma^Y<0 \text{ :  pure elastic behavior}
$$

## 2.2. Barlat's yield criterion

- Barlat yield criterion은 응력 텐서의 '선형 변환'된 값을 활용한다. 선형 변환 매트릭스 $\boldsymbol L$을 활용하여 응력 텐서를 변환하고, 이를 Hosford 등가 응력 표현에 활용하여, 해당 등가 응력을 항복의 기준으로 삼는다.


$$
f(\tilde{\boldsymbol s})=\sigma^Y
$$

where $\tilde{\boldsymbol s}$ is a transformed stress tensor, via a linear mapping of the cauchy stress tensor:

$$
\tilde{\boldsymbol s}=\boldsymbol L : \boldsymbol\sigma
$$

One can then use the same form of Hosford yield function such that:

$$
f(\boldsymbol\sigma)=(|s_1 - s_2|^a+|s_2 - s_3|^a+|s_1 - s_3|^a)^{1/a}
$$

so that

$$
(|s_1 - s_2|^a+|s_2 - s_3|^a+|s_1 - s_3|^a)^{1/a} = \sigma^Y : \text{yield criterion}
$$


$$
(|s_1 - s_2|^a+|s_2 - s_3|^a+|s_1 - s_3|^a)^{1/a} < \sigma^Y : \text{elastic behavior}
$$


# 3. Slip system & crystal orientation

전위 슬립계가 simple shear 변형을 받아드리면서 lattice 회전이 발생할 수 있다. 이는 집합조직 발달로 이어진다.


# 4. 평균장 다결정 소성 모델

- 각 결정립의 평균적인 거동을 바탕으로, 여러 결정립으로 이루어진 다결정의 평균 거동을 계산할 필요가 있다.

- FE 모델의 경우(Type I), 각 유한요소에 다른 결정 방위를 부과하여 그 평균 값을 계산을 통해 하는 방법이 있다.

- VPSC 모델의 경우, Homogeneous Effective Medium 방법을 활용해 계산한다.

  - 우선 아래 비선형 거동을 선형화 형태로 나타내어야 한다.

$$
\dot{\boldsymbol\varepsilon}^{pl}=\dot\gamma_0\sum_s\boldsymbol m^s\bigg(\frac{|\boldsymbol m^s : \boldsymbol \sigma|}{\tau_c}\bigg)^n \text{sgn}(\boldsymbol m^s : \boldsymbol \sigma)
$$

  - 다양한 방법중 Secant 방법을 소개하겠다.

$$
\dot{\boldsymbol\varepsilon}^{pl}=\dot\gamma_0\sum_s\boldsymbol m^s\bigg(\frac{|\boldsymbol m^s : \boldsymbol \sigma|}{\tau_c}\bigg)^{n-1} \bigg(\frac{|\boldsymbol m^s : \boldsymbol \sigma|}{\tau_c}\bigg)\text{sgn}(\boldsymbol m^s : \boldsymbol \sigma)
$$

$$
=\dot\gamma_0\sum_s\boldsymbol m^s\bigg(\frac{|\boldsymbol m^s : \boldsymbol \sigma|}{\tau_c}\bigg)^{n-1} \bigg(\frac{\boldsymbol m^s : \boldsymbol \sigma}{\tau_c}\bigg)
$$

$$
=\dot\gamma_0\sum_s\frac{\boldsymbol m^s\otimes \boldsymbol m^s}{\tau_c}\bigg(\frac{|\boldsymbol m^s : \boldsymbol \sigma|}{\tau_c}\bigg)^{n-1} \bigg(\frac{\boldsymbol m^s : \boldsymbol \sigma}{\tau_c}\bigg)
$$

# 5. 연습 문제

## 문제 1

가공경화가 진행될 때 일반적으로 이후의 항복응력은 어떻게 변하는가?

<!--
풀이와 해답:
소성변형이 누적될수록 이후의 항복응력은 증가한다.
-->

## 문제 2

등방경화에서 항복면의 크기와 중심은 각각 어떻게 변하는가?

<!--
풀이와 해답:
항복면의 크기는 증가하고 중심은 변하지 않는다.
-->

## 문제 3

이동경화에서 항복면은 응력공간에서 어떻게 변하는가?

<!--
풀이와 해답:
항복면의 중심이 이동한다.
-->

## 문제 4

결정소성에서 경화를 미시적으로 나타내는 대표적인 내부변수를 하나 쓰시오.

<!--
풀이와 해답:
예를 들어 슬립계의 임계분해전단응력 또는 전위밀도를 사용할 수 있다.
-->
