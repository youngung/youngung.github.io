---
layout: distill
title: 평균장 다결정 소성 모델
description: 결정립 거동의 평균화와 VPSC의 secant 선형화
target: 대학원
permalink:
featured: true
prerequisite: 소성 유동법칙, 경화와 이방성, Eshelby inclusion
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


이 자료는 [Eshelby inclusion]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16_eshelby_inclusion.md %}) 이후에 읽는다.
결정립의 국소 거동과 다결정의 평균 거동을 연결하고, secant 선형화를 소개한다.
결정립의 형상과 방위 갱신은 [VPSC의 운동학]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_15_kinematics.md %})에서 이어서 다룬다.

# 1. 평균장 다결정 소성 모델

<span id="4-평균장-다결정-소성-모델"></span>

- 각 결정립의 평균적인 거동을 바탕으로, 여러 결정립으로 이루어진 다결정의 평균 거동을 계산할 필요가 있다.

- FE 모델의 경우(Type I), 각 유한요소에 다른 결정 방위를 부과하여 다결정의 거동을 계산하는 방법이 있다.

- VPSC 모델의 경우, Homogeneous Effective Medium 방법을 활용해 계산한다.

  - 아래 비선형 거동을 응력에 대한 선형 관계로 나타낸다. 계수는 현재 응력상태에 의존한다.

여기서 $\boldsymbol m^s$는 대칭 Schmid 텐서, $\dot\gamma_0$는 기준 전단속도,
$\tau_c$는 모든 슬립계에 같다고 가정한 임계분해전단응력, $n$은 속도 민감도를 나타내는 지수다.
슬립계별 강도가 다른 경우에는 $\tau_c^s$를 사용한다.

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
\dot{\boldsymbol\varepsilon}^{pl}
=\left[
\dot\gamma_0\sum_s
\frac{\boldsymbol m^s\otimes\boldsymbol m^s}{\tau_c}
\left(\frac{|\boldsymbol m^s:\boldsymbol\sigma|}{\tau_c}\right)^{n-1}
\right]:\boldsymbol\sigma
$$

대괄호 안은 현재 응력상태에 의존하는 4차 secant compliance 역할을 한다.
