---
layout: distill
title: 소성가공
description:
target: 3학년 1학기
permalink:
featured: true
prerequisite: 재료공학개론1, 대학수학, 데이터 재료과학, 수치해석
#toc:
#sidebar: left
#- name: Orientation
#- name: Week1
#- name: Week2
#- name: Week3
#- name: Week4
#- name: Week5
#- name: Week6

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
  - [1.1. strain hardening depicted in phenomonlogical plasticity](#11-strain-hardening-depicted-in-phenomonlogical-plasticity)
  - [1.2. strain hardening described in crystal plasticity framework.](#12-strain-hardening-described-in-crystal-plasticity-framework)
- [2. Anisotropy](#2-anisotropy)
  - [2.1. Hill's yield criterion](#21-hills-yield-criterion)
  - [2.2. Barlat's yield criterion](#22-barlats-yield-criterion)
- [3. Slip system \& crystal orientation](#3-slip-system--crystal-orientation)

# 1. Hardening

- 소성 변형이 증가할 수록 강도가 증가한다.

- 전위 밀도가 증가하며, 항복 응력이 소성 변형량의 증가함에 따라 함께 높아진다.

## 1.1. strain hardening depicted in phenomonlogical plasticity

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
\sigma^{Hill} = F(\sigma_{22}-\sigma_{33})^2+G(\sigma_{33}-\sigma_{11})^2+H(\sigma_{11}-\sigma_{22})^2+2L\sigma_{23}^2+2M\sigma_{13}^2+2N\sigma_{12}^2
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
f(\boldsymbol\sigma)=|s_1 - s_2|^a+|s_2 - s_3|^a+|s_1 - s_3|^a
$$

so that

$$
|s_1 - s_2|^a+|s_2 - s_3|^a+|s_1 - s_3|^a = \sigma^Y : \text{yield criterion}
$$


$$
|s_1 - s_2|^a+|s_2 - s_3|^a+|s_1 - s_3|^a <> \sigma^Y : \text{elastic behavior}
$$


# 3. Slip system & crystal orientation

전위 슬립계가 simple shear 변형을 받아드리면서 lattice 회전이 발생할 수 있다. 이는 집합조직 발달로 이어진다.
