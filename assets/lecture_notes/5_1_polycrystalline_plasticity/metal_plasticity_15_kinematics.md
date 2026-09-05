---
layout: distill
title: 유한변형 운동학
description: 속도구배, 변형구배와 극분해
target: 학부 고학년
permalink:
featured: true
prerequisite: 벡터와 행렬, 변위와 변형률
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
- [3. 극분해](#3-극분해)
- [4. 점의 속도](#4-점의-속도)
- [5. 속도구배](#5-속도구배)
- [6. 연습 문제](#6-연습-문제)


# 1. 운동학 개요

## 1.1. 속도구배

$$
\boldsymbol L = \boldsymbol D + \boldsymbol W
$$

  - $\boldsymbol L$: 속도구배 텐서(velocity gradient tensor)
  - $\boldsymbol D$: 변형률속도 텐서(rate-of-deformation tensor)
  - $\boldsymbol W$: 스핀 텐서(spin tensor)

## 1.2. 운동학

- 운동학; 점의 운동, 물체의 운동, 힘과 변형

- $\boldsymbol X$ : 초기 위치; Reference configuration

- $\boldsymbol x$ : 변화된 위치; current configuration

- $\boldsymbol{X}\rightarrow\boldsymbol{x}(t)$

# 2. 변형구배

- $\boldsymbol F=\frac{\partial \boldsymbol x}{\partial \boldsymbol X}$

- Change in infinitesimal line vector ($d\boldsymbol X$)

$$
d\boldsymbol x = \boldsymbol F \cdot d\boldsymbol X
$$

# 3. 극분해

- $\boldsymbol F = \boldsymbol{R} \cdot \boldsymbol{U}=   \boldsymbol{V}\cdot\boldsymbol{R}$

# 4. 점의 속도

- $\boldsymbol v\equiv\boldsymbol v(\boldsymbol x,t)$

# 5. 속도구배

- Definition
$$
\boldsymbol L = \nabla \boldsymbol v
$$

$$
\boldsymbol L=
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

극분해에서 변형구배를 회전과 신장으로 분해하는 식을 하나 쓰시오.

<!--
풀이와 해답:
예를 들어 F=R U로 쓸 수 있다. R은 회전 텐서이고 U는 우 신장 텐서이다.
-->
