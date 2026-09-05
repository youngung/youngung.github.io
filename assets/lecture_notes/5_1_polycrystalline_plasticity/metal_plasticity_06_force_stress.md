---
layout: distill
title: 힘과 응력
description: 면에 작용하는 힘과 Cauchy 응력 텐서
target: 학부 고학년
permalink:
featured: true
prerequisite: 벡터와 행렬
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

- [1. 힘](#1-힘)
- [2. 응력](#2-응력)
- [3. 수직 및 전단 응력](#3-수직-및-전단-응력)
- [4. 응력 텐서](#4-응력-텐서)
- [5. 요약](#5-요약)

# 1. 힘

- 힘이 가해지면 운동 상태의 변화나 변형이 발생한다. 소성 역학에서 우리는 변형 발생에 초점을 둔다.

- 벡터 물리량이며, 크기(magnitude)와 방향성 가진다.

- SI 단위로 표현하면 $[N]=[kg m/s^2]$

# 2. 응력

- 단위 면적당 작용하는 힘

$\mathbf \sigma = \mathbf F/ \mathbf A$

- 텐서 나누기 텐서? 그러한 operation 자체는 없다!

- 단위

| 단위 | 의미     |
| ---- | -------- |
| Pa   | N/m²     |
| kPa  | 1,000 Pa |
| MPa  | 10⁶ Pa   |
| GPa  | 10⁹ Pa   |

# 3. 수직 및 전단 응력

- 수직 응력: 면에 수직으로 작용하는 힘에 의한 응력

- 전단 응력: 면과 평행하게 작용하는 힘에 의한 응력
  - 가위
  - 리벳
  - 볼트
  - 전위의 슬립

# 4. 응력 텐서

- 응력 텐서를 랭크 2 매트릭스로 표현할 수 있다.

$$ \sigma =\begin{bmatrix}
\sigma_{11} & \sigma_{12} & \sigma_{13} \\
\sigma_{21} & \sigma_{22} & \sigma_{23} \\
\sigma_{31} & \sigma_{32} & \sigma_{33}
 \end{bmatrix}$$


- 응력 텐서 성분의 의미
예: $\sigma_{ij}$ 는 $\mathbf e_{i}$ 축과 나란한 방향의 법선을 가진 면에 $\mathbf e_{j}$ 축 방향으로 작용하는 힘에 의한 응력이라는 뜻


# 5. 요약

| 개념 | 공식 |
|------|------|
| 힘 | $\mathbf F = m\mathbf a$ |
| 응력 성분 의미 | $\mathbf\sigma_{ij} = F_{i} / A_{j}$??   $\boldsymbol e_i$축과 나란한 힘 방향 $\boldsymbol e_j$축과 나란한 수직성을 가진 면|
| 수직 및 전단응력 | 힘과 면의 수직 방향이 같은 방향이나, 혹은 수직이냐에 따라 구분 |
| 응력의 단위 | $1 Pa = 1 N/m²$ |
| 전단응력의 대칭성 | $\sigma_{12} = \sigma_{21}$ 모멘트(힘) 평형에 의한 결과|

# 6. 연습 문제

## 문제 1

단면적이 50 mm²인 면에 수직방향으로 5000 N의 힘이 작용한다. 수직응력을 구하라.

<!--
풀이와 해답:
응력은 5000/50=100 N/mm²=100 MPa이다.
-->

## 문제 2

면에 평행하게 작용하는 단위면적당 힘을 무엇이라고 하는가?

<!--
풀이와 해답:
전단응력(shear stress)이라고 한다.
-->

## 문제 3

응력 텐서 $\boldsymbol\sigma$와 단위법선벡터 $\boldsymbol n$으로 면력벡터를 나타내라.

<!--
풀이와 해답:
Cauchy 공식에 따라 t(n)=sigma n이다.
-->

## 문제 4

각운동량 평형을 만족하는 고전적 연속체에서 응력 텐서가 갖는 대칭성을 쓰시오.

<!--
풀이와 해답:
sigma_ij=sigma_ji이므로 응력 텐서는 대칭이다.
-->
