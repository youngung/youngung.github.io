---
layout: distill
title: 소성 유동법칙
description: 변형률 분해, 항복함수와 소성 유동법칙
target: 학부 고학년
permalink:
featured: true
prerequisite: 소성 항복, 선형 탄성
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

# 1. 영구 변형 (permanent deformation)

- 경화가 없는 탄소성 거동 재료의 stress vs. strain 곡선:


<img src="/assets/lecture_notes/3_1_metal_plasticity/elasto-plastic.jpeg" alt="흰색 배경의 응력-변형률 그래프. 세로축은 응력, 가로축은 변형률을 나타내며, 곡선은 초기의 직선 탄성 구간을 지나 항복점에 도달한 뒤 거의 수평인 소성 변형 구간으로 이어진다. 그래프에는 탄성 및 소성 거동의 구분이 표시되어 있다." width="400"/>

- 탄성변형은 하중을 제거하면 회복되지만 소성변형은 영구적으로 남는다.
  단순한 일축 탄소성 모델에서는 $|\sigma|=\sigma_y$에 도달할 때 소성변형이 시작된다.

# 2. 변형률 분해

- 전체 변형률은 탄성 변형률과 소성 변형률의 '합'으로 이해된다.

$$
\varepsilon=\varepsilon^{el}+\varepsilon^{pl}
$$

- 텐서의 경우에도 마찬가지

$$
\boldsymbol{\varepsilon}=\boldsymbol{\varepsilon}^{el}+\boldsymbol{\varepsilon}^{pl}
$$

# 3. Hooke 법칙
- 탄성 변형률은 Hooke 법칙 따른다

$$
\boldsymbol{\sigma} = \boldsymbol{E}:\boldsymbol{\varepsilon}^{el}
$$

$$
\sigma_{ij} =\sum_{k=1}^3\sum_{l=1}^3 E_{ijkl}\varepsilon^{el}_{kl} \text{ with }\ \ i=1,2,3 \ \ \ j=1,2,3
$$

# 4. 유동법칙 (flow rule)

- 소성 변형률의 변화는 flow rule을 따른다.

- 가장 널리 활용되는 flow rule은, 'normality' rule (혹은 associated flow rule)이다.

$$
d\boldsymbol{\varepsilon}^{pl}=d\lambda\frac{\partial f}{\partial\boldsymbol{\sigma}}
$$

$$
f: \text{ plastic potential},\qquad
d\lambda: \text{ plastic multiplier increment}
$$

- 소성 변형률 텐서 increment(즉 $d\boldsymbol\varepsilon^{pl}$)의 방향은 $\frac{\partial f}{\partial \boldsymbol\sigma}$가 결정하고, 그 크기($|d\boldsymbol\varepsilon^{pl}|$)는 $d\lambda$가 결정한다.

- 주응력 공간에서 위는 아래와 같이 표현된다.

$$
d{\varepsilon}^{pl}_i=d\lambda\frac{\partial f}{\partial{\sigma_i}} \text{ with } i=1,2,3
$$

- Von mises 등가 응력값을 plastic potential에 활용한다면

$$
f=\sqrt{\frac{1}{2}\bigg((\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2\bigg)}
$$

# 5. 전위 슬립과 Schmid 법칙

- 금속에서 소성 변형은 전위의 슬립 메커니즘으로 수용된다.

- 한 슬립계는 슬립면 법선 $\boldsymbol n$과 슬립방향 $\boldsymbol b$로 이루어진다.

- Schmid 법칙

  - 외부 응력 $\boldsymbol \sigma$가 가해졌을 때, 슬립계 s에 전달되는 분해 전단 응력은 아래와 같이 구한다.

$$
\tau^s=({\boldsymbol\sigma}\cdot {\boldsymbol n}^s)\cdot \boldsymbol b^s=\sum_{i=1}^3\sum_{j=1}^3\sigma_{ij}n_i^sb_j^s
$$

  - 이를 Schmid tensor $\boldsymbol m$을 활용해 표현할 수 있다.

$$
\boldsymbol m^s = \frac{1}{2}(\boldsymbol{n}^s\otimes\boldsymbol{b}^s+
\boldsymbol{b}^s\otimes\boldsymbol{n}^s)
$$

$$
m^s_{ij}=\frac{1}{2}(n_i^sb_j^s+n_j^sb_i^s), \text{ with } i=1,2,3 \ \ \ j=1,2,3
$$

- 응력텐서의 특징 $\sigma_{ij}=\sigma_{ji}$로 인해 아래를 만족한다.

$$
\tau^s=({\boldsymbol\sigma}\cdot {\boldsymbol n}^s)\cdot \boldsymbol b^s=\sum_{i=1}^3\sum_{j=1}^3\sigma_{ij}n_i^sb_j^s=\sum_{i=1}^3\sum_{j=1}^3\sigma_{ij}m_{ij}^s
$$

- double contraction 활용해 더욱 간략히 표기할 수 있다.

$$
\tau^s=\boldsymbol\sigma:\boldsymbol m^s
$$

# 6. 전위 슬립 조건

- 모든 슬립계의 CRSS값, $\tau_c$가 동일하다면, 소성 변형의 시작은 최대 분해 전단 응력값이 $\tau^{crss}$ 값과 같을 때 발생한다.

$$
|\max_s\{\tau^s\}|=\tau_c
$$

# 7. 속도 의존형 정식화

- 앞서 논의한 아래와 같은 항복 조건을 좀 더 유연하게 적용한 경우가 있다.

$$
|\max_s\{\tau^s\}|=\tau_c
$$

- 각 슬립계에서, 다음과 같은 '멱함수'의 형태로 각 전단 변형률 속도와 연계된다.

- 우선 각 슬립계의 전달 변형률 속도를 각 슬립계에 작용하는 분해전단 응력,
  그리고 각 슬립계의 임계 분해 전단 응력의 함수로 표현한다.

$$
\dot\gamma^s/\dot{\gamma_0}=(\tau^s/\tau_c^s)^n
$$

- 위 식의 문제는 $\pm$ 전단 방향을 제대로 고려하지 못한다는 점이다.
  - $\tau^s<0$ 일 때 항상 $\dot\gamma^s<0$을 만족하지 못한다.
  - 이는 $n$값이 짝수냐 홀수냐에 따라 영향을 받는다.

- 아래 표현이 더욱 적절하다.

$$
\dot\gamma^s/\dot{\gamma_0}=(|\tau^s|/\tau_c^s)^n\text{sgn}(\tau^s)
$$

- 멱함수 안의 전단응력 크기는 항상 양수로 두고, $\text{sgn}(\tau^s)$를 곱하여 $\dot\gamma^s$와 $\tau^s$의 부호를 일치시킨다.

# 8. 결정립 내 변형률

- 한 결정립 내 여러 슬립계가 12개 있다면

$$
\dot{\boldsymbol\varepsilon}^{pl}=\sum_s^{12} \dot\gamma^s \boldsymbol{m}^s
$$

- 따라서, 앞선 전단 변형 속도 식을 대입하면

$$
\dot{\boldsymbol\varepsilon}^{pl}=\sum_s^{12} \dot\gamma_0\bigg(\frac{|\tau^s|}{\tau_c^s}\bigg)^n\text{sgn}(\tau^s) \boldsymbol{m}^s
$$

- Schmid law를 대입하면

$$
\dot{\boldsymbol\varepsilon}^{pl}=\sum_s^{12} \dot\gamma_0\bigg(\frac{|\boldsymbol m^s:\boldsymbol\sigma|}{\tau_c^s}\bigg)^n\text{sgn}(\boldsymbol m^s:\boldsymbol\sigma) \boldsymbol{m}^s
$$


- 위 식을 index를 활용해 표기하면 더 이해에 도움된다?


$$
\dot{\varepsilon}^{pl}_{ij}
=\sum_{s=1}^{12}\dot\gamma_0
\left(\frac{|\tau^s|}{\tau_c^s}\right)^n
\operatorname{sgn}(\tau^s)m^s_{ij},
\qquad
\tau^s=\sum_{k=1}^{3}\sum_{l=1}^{3}m^s_{kl}\sigma_{kl}
$$

# 9. 연습 문제

## 문제 1

소성변형률 증분을 탄성변형률 증분과 전체 변형률 증분으로 나타내라.

<!--
풀이와 해답:
d epsilon^p=d epsilon-d epsilon^e이다.
-->

## 문제 2

연관 유동법칙에서 소성변형률 증분의 방향은 무엇으로 결정되는가?

<!--
풀이와 해답:
항복함수의 응력에 대한 gradient, 즉 항복면의 법선방향으로 결정된다.
-->

## 문제 3

Schmid 법칙에서 분해전단응력이 임계분해전단응력에 도달하면 무엇이 시작되는가?

<!--
풀이와 해답:
해당 슬립계에서 전위 슬립이 시작된다.
-->

## 문제 4

소성승수는 소성변형이 발생하지 않을 때 어떤 값을 갖는가?

<!--
풀이와 해답:
0이다.
-->
