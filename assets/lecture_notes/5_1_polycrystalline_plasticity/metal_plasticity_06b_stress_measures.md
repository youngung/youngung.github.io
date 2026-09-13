---
layout: distill
title: 유한변형의 응력 척도
description: Cauchy, Kirchhoff 및 Piola–Kirchhoff 응력의 비교
target: 대학원
permalink:
featured: true
prerequisite: 힘과 응력, 유한변형의 운동학
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


# 1. 왜 서로 다른 응력 척도를 사용하는가?

[힘과 응력]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_06_force_stress.md %})에서는 현재 변형된 면에 작용하는 Cauchy 응력을 사용했다.
유한변형에서는 면적·방향·체적이 변하므로, 같은 힘도 어느 배치를 기준으로 표현하는지에 따라 응력 척도(stress measure)가 달라진다.

[유한변형의 운동학]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %})의
변형구배 $\boldsymbol F=\partial\boldsymbol x/\partial\boldsymbol X$와 체적비 $J=\det\boldsymbol F>0$를 사용한다.
$\boldsymbol N$, $dA$는 기준 배치의 단위 법선과 면적이고, $\boldsymbol n$, $da$는 대응하는 현재 배치의 값이다.

# 2. 네 가지 응력 척도

| 응력 척도 | 정의·관계식 | 의미 |
| --- | --- | --- |
| Cauchy 응력 $\boldsymbol\sigma$ | $d\boldsymbol f=(\boldsymbol\sigma\cdot\boldsymbol n)da$ | 현재 면적당 현재 힘. 진응력의 텐서 표현 |
| Kirchhoff 응력 $\boldsymbol\tau$ | $\boldsymbol\tau=J\boldsymbol\sigma$ | 체적비로 환산한 공간 응력. $J=1$이면 Cauchy 응력과 동일 |
| 제1 Piola–Kirchhoff 응력 $\boldsymbol P$ | $\boldsymbol P=J\boldsymbol\sigma\cdot\boldsymbol F^{-T}$ | 기준 면적당 현재 힘. 기준·현재 배치를 연결하는 이점 텐서(two-point tensor) |
| 제2 Piola–Kirchhoff 응력 $\boldsymbol S$ | $\boldsymbol S=\boldsymbol F^{-1}\cdot\boldsymbol P=J\boldsymbol F^{-1}\cdot\boldsymbol\sigma\cdot\boldsymbol F^{-T}$ | 힘도 기준 배치로 끌어온 물질 응력. Green–Lagrange 변형률과 짝을 이룸 |

여기서 $\boldsymbol F^{-T}=(\boldsymbol F^{-1})^T$다.
고전적인 연속체에서 응력이 대칭이면 $\boldsymbol\sigma$, $\boldsymbol\tau$, $\boldsymbol S$는 대칭이지만, $\boldsymbol P$는 일반적으로 대칭이 아니다.
또한 $\boldsymbol\tau$는 텐서 응력이므로 슬립계의 스칼라 분해전단응력 $\tau^s$와 구분한다.

제1 Piola–Kirchhoff 응력은 Nanson의 면적 변환식으로 이해할 수 있다.

$$
\boldsymbol n\,da=J\boldsymbol F^{-T}\cdot\boldsymbol N\,dA,
\qquad
d\boldsymbol f=(\boldsymbol\sigma\cdot\boldsymbol n)da
=(\boldsymbol P\cdot\boldsymbol N)dA.
$$

제2 Piola–Kirchhoff 응력의 힘은 실제 현재 힘 자체가 아니라
$\boldsymbol F^{-1}\cdot d\boldsymbol f=(\boldsymbol S\cdot\boldsymbol N)dA$로 변환한 힘이다.
이 정의와 배치 구분은 [Sandia의 응력 척도 설명](https://www.sandia.gov/files/sierra/SM_Theory_5_18/main/stress_measures.html)을 참고한다.

# 3. 변형률속도와의 일률 관계

응력과 변형률을 임의로 짝지으면 같은 일률을 얻지 못한다.
$\boldsymbol D=(\boldsymbol L+\boldsymbol L^T)/2$,
$\boldsymbol L=\dot{\boldsymbol F}\cdot\boldsymbol F^{-1}$,
$\boldsymbol E=(\boldsymbol F^T\cdot\boldsymbol F-\boldsymbol I)/2$일 때

$$
\underbrace{J\boldsymbol\sigma:\boldsymbol D}_{\text{기준 체적당 일률}}
=\boldsymbol\tau:\boldsymbol D
=\boldsymbol P:\dot{\boldsymbol F}
=\boldsymbol S:\dot{\boldsymbol E}.
$$

점은 같은 물질점을 따라가는 시간미분이고, $:$는 이중수축이다.
현재 체적당 일률은 $\boldsymbol\sigma:\boldsymbol D$다.
따라서 $\boldsymbol P$와 $\dot{\boldsymbol F}$, $\boldsymbol S$와 $\dot{\boldsymbol E}$는 기준 체적당 일률을 만드는 짝이다.
관련 유한변형 정식화는 [deal.II의 초탄성 튜토리얼](https://dealii.org/9.4.0/doxygen/deal.II/step_44.html)을 참고한다.

# 4. 1차원 인장과 연결하기

신장비를 $\Lambda=l/l_0$라 하자. 회전 없이 체적을 보존하며 1방향으로 늘어나는 경우

$$
[\boldsymbol F]=\operatorname{diag}(\Lambda,\Lambda^{-1/2},\Lambda^{-1/2}),
\qquad J=1,
\qquad
[\boldsymbol\sigma]=\operatorname{diag}(\sigma,0,0).
$$

이면 $\tau_{11}=\sigma$, $P_{11}=\sigma/\Lambda$, $S_{11}=\sigma/\Lambda^2$다.
예를 들어 $\Lambda=1.5$, $\sigma=150\,\mathrm{MPa}$이면 각각 $150$, $100$, $66.7\,\mathrm{MPa}$다.
일축 인장력의 크기를 $f$라 하면, 이때 $P_{11}$은 공칭응력 $f/A_0$에 해당하고, $\sigma$는 진응력 $f/A$다.
응력 척도의 차이는 다른 하중을 의미하는 것이 아니라 같은 하중을 다른 기준으로 표현한 결과다.

미소변위구배, 즉 $\boldsymbol F\approx\boldsymbol I$, $J\approx1$이면 네 척도의 차이를 무시할 수 있다.
작은 변형률이라도 큰 강체회전이 있으면 이들의 성분이 모두 같다고 할 수는 없다.
