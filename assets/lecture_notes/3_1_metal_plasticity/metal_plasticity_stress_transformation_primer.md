---
layout: distill
title: 좌표변환과 주응력의 기초
description: 항복 조건에 필요한 좌표변환, 주응력과 편차응력
target: 학부 3학년
permalink:
featured: true
prerequisite: 힘과 응력, 행렬과 텐서 연산
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


# 1. 같은 응력을 다른 방향에서 바라보기

응력텐서의 성분은 좌표축을 돌리면 달라진다. 물체에 작용하는 응력 상태 자체가 달라지는 것은 아니다.
평면에서 새 기저를 기존 기저에 대해 $\theta$만큼 회전시키면

$$
[\boldsymbol R]=\begin{bmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{bmatrix},
\qquad
[\boldsymbol\sigma]_{\mathrm{new}}=[\boldsymbol R][\boldsymbol\sigma]_{\mathrm{old}}[\boldsymbol R]^T.
$$

대괄호는 같은 기저에서의 성분 배열이며, $T$는 전치다.
$R_{ij}$는 새 기저의 $i$번째 단위벡터와 기존 기저의 $j$번째 단위벡터의 내적이다.

# 2. 주응력과 최대 전단응력

전단응력 성분이 0이 되는 좌표축을 **주축 (principal axes)**이라 한다.
이 축에 대한 수직응력이 **주응력 (principal stresses)**이며, 응력텐서의 고유값이다.
평면의 두 주응력은

$$
\sigma_{\pm}=\frac{\sigma_{11}+\sigma_{22}}{2}
\pm\sqrt{\left(\frac{\sigma_{11}-\sigma_{22}}{2}\right)^2+\sigma_{12}^2}
$$

로 구한다. 평면응력에서는 면외 주응력 0도 포함해 세 주응력을 크기순으로 정리한다.
3차원 최대 전단응력은 $\tau_{\max}=(\sigma_{\max}-\sigma_{\min})/2$다.

예를 들어

$$
[\boldsymbol\sigma]=\begin{bmatrix}80&20&0\\20&50&0\\0&0&0\end{bmatrix}\,\mathrm{MPa}
$$

이면 평면 내 주응력은 $65\pm25$, 즉 $90$과 $40\,\mathrm{MPa}$다.
세 주응력은 $(90,40,0)\,\mathrm{MPa}$이므로 최대 전단응력은 $45\,\mathrm{MPa}$다.
평면 내 최대 전단응력 $25\,\mathrm{MPa}$와 구분해야 한다.

# 3. 평균응력과 편차응력

응력은 평균응력과 나머지 부분으로 나눈다.

$$
\sigma_m=\frac{\sigma_{11}+\sigma_{22}+\sigma_{33}}{3},
\qquad \boldsymbol s=\boldsymbol\sigma-\sigma_m\boldsymbol I.
$$

$\boldsymbol I$는 단위텐서이고, $\boldsymbol s$는 **편차응력 (deviatoric stress)**이다.
다음 항복 조건 자료에서는 주응력으로 Tresca 조건을, 편차응력으로 von Mises 조건을 이해한다.

# 4. 연습 문제

주응력이 $(120,60,0)\,\mathrm{MPa}$일 때 평균응력과 3차원 최대 전단응력을 구하시오.

<!--
풀이와 해답:
평균응력=(120+60+0)/3=60 MPa.
최대 전단응력=(120-0)/2=60 MPa.
-->

다음 자료: [소성 항복]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_09_plastic_yield.md %})
