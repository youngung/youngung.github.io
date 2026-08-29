---
layout: distill
title: 소성가공
description: 금속 소성 가공 역학 기초
target: 3학년 1학기
permalink:
featured: true
prerequisite:

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

- [1. 선형 탄성 (linear elasticity) 거동](#1-선형-탄성-linear-elasticity-거동)
- [2. Young's modulus (영률)](#2-youngs-modulus-영률)
- [3. 포아송 효과 (Poisson effect)](#3-포아송-효과-poisson-effect)
- [4. 3차원으로 확장하여 표현되는 Hooke의 법칙](#4-3차원으로-확장하여-표현되는-hooke의-법칙)
- [5. 등방성 재료의 경우](#5-등방성-재료의-경우)
- [6. 선형 등방 Hooke 법칙 상세 설명](#6-선형-등방-hooke-법칙-상세-설명)
- [7. 선형 등방 Hooke 법칙에서의 상수 관계](#7-선형-등방-hooke-법칙에서의-상수-관계)
- [8. Voigt 표현법](#8-voigt-표현법)
- [9. Compliance matrix](#9-compliance-matrix)
- [10. Plane stress와  plane strain 조건에서의 Hooke 법칙](#10-plane-stress와--plane-strain-조건에서의-hooke-법칙)
- [\\end{bmatrix}](#endbmatrix)

# 1. 선형 탄성 (linear elasticity) 거동

- 힘->응력
- 변위->변형류

- 응력과 변형률로 표현된 자극과 반응 사이의 관계는?
  - 많은 금속 재료의 경우, 매우 높은 수준의 응력을 가해지는 게 아니라면 탄성 거동만을 보인다.
  - 즉 응력이 가해지는 동안에만 변형률이 보이고, 응력이 사라지면 변형률이 사라진다.
  - 그리고 많은 금속 재료들은 탄성을 보일 때, 응력과 변형률이 선형 비례한다.

- 위 거동을 만족시키는 응력과 변형률의 관계는 아래와 같이 표현된다.

$$\sigma=E\varepsilon$$

- 위 관계를 처음 보인 Hooke의 이름을 따서, 위 식을 Hooke의 법칙이라고도 부른다.

- 만약 응력과 변형률이 모두 스칼라라면 기울기 $E$도 스칼라가 된다.

# 2. Young's modulus (영률)

- Hooke의 법칙에서 보이는 스칼라 $E$를 영률이라 부른다.

- 변형률이 단위가 없으므로, 영률은 응력과 같은 단위를 가진다 ($Pa, MPa$ 등)

- 영률은 재료의 성질이다. 강철과 고무에 동일한 응력을 가했을 때, 강철의 변형률이 훨씬 작다. 따라서 강철의 영률이 고무의 영률에 비해 매우 크다.

# 3. 포아송 효과 (Poisson effect)

- 인장하는 길이가 $\mathbf e_1$ 방향일 때, 수직 변형이 $\mathbf e_1$축으로만 발생하지 않는다. 그에 수직한 방향, 예를 들어 $\mathbf e_2$로는 길이가 줄어드는 수직 변형이 발생할 수 있다.

- 이럴 때, 적어도 두 수직 변형률 성분 $\varepsilon_{11}$, $\varepsilon_{22}$가 0이 아님을 알 수 있다. 더욱 구체적으로는 아래와 같은 값의 범위를 가지게 된다.

  - $\varepsilon_{11}>0$
  - $\varepsilon_{22}<0$

- 이때 발생하는 두 수직 변형률 성분의 비를 poisson 비로 정의한다.

$$\nu=-\frac{\varepsilon_{22}}{\varepsilon_{11}}$$

# 4. 3차원으로 확장하여 표현되는 Hooke의 법칙

- 응력텐서 $\mathbf \sigma$와 변형률 텐서 $\mathbf \varepsilon$의 선형 관계를 표현해야 하겠다. 이를 아래와 같이 표현할 수 있다.

$$ \sigma_{ij} = \sum_{k}^3\sum_{l}^3 E_{ijkl} \varepsilon _{kl} \text{ with } i=1,2,3\ \ \ j=1,2,3$$

- 응력과 변형률 텐서는 각각 랭크2의 매트릭스로, 탄성계수 텐서 $E$는 랭크 4의 매트릭스로 표현됨을 알 수 있다.

# 5. 등방성 재료의 경우

- 재료의 물성이 방향에 관계 없을 때, 앞선 3차원 Hooke의 법칙에 활용된 랭크4의 $E$텐서를 두 스칼라 $\lambda$와 $G$로 표현할 수 있다.

$$
\mathbf \sigma = \lambda tr(\mathbf \varepsilon) \mathbf I + 2G \mathbf \varepsilon
$$

- 위를 인덱스를 활용해 표현하면

$$
\sigma_{ij} = \lambda  \delta_{ij} \sum_k^3(\varepsilon_{kk}) + 2G\varepsilon_{ij}, \text{ with } i=1,2,3\ \ \ j=1,2,3
$$

- $tr(\mathbf\varepsilon)$는 체적 변형률이며 아래와 같이 정의된다.
  $$tr(\mathbf\varepsilon)=\sum_k^3\varepsilon_{kk}=\varepsilon_{11}+\varepsilon_{22}+\varepsilon_{33} $$

- $\mathbf I$는 랭크2 단위 텐서이며, 아래와 같은 매트릭스 형태로 표현된다.

$$
\mathbf I = \begin{bmatrix}
1 &0 &0 \\
0 &1 &0 \\
0 &0 &1 \\
\end{bmatrix}
$$

- $\delta_{ij}$는 크로네커 델타로 불리며 아래 성질을 가진다.

  - $\delta_{ij}=0, \text{ if } i\ne j$
  - $\delta_{ij}=1, \text{ if } i=j$
  - 따라서 $\delta_{ij}$는 $\mathbf I$와 동일한 역할을 수행한다.

- G는 전단 탄성계수이다.

- $\lambda$는 Lame의 제1 상수이다.

# 6. 선형 등방 Hooke 법칙 상세 설명

- 위 Hooke의 법칙에서

  - $\lambda tr(\mathbf \varepsilon) \mathbf I$은 체적변형과 관련된 응력
  - $2G \mathbf \varepsilon$은 형태 변화에 의한 응력으로 볼 수 있다.

- 응력 성분을 각기 풀어 표현하면

  - 수직 성분의 경우
    $$\sigma_{11}=\lambda (\varepsilon_{11}+\varepsilon_{22}+\varepsilon_{33}) + 2G\varepsilon_{11}$$

$$\sigma_{22}=\lambda (\varepsilon_{11}+\varepsilon_{22}+\varepsilon_{33}) + 2G\varepsilon_{22}$$

$$\sigma_{33}=\lambda (\varepsilon_{11}+\varepsilon_{22}+\varepsilon_{33}) + 2G\varepsilon_{33}$$

- 전단 성분의 경우

$$ \sigma_{12}=2G\varepsilon_{12} $$

$$ \sigma_{13}=2G\varepsilon_{13} $$

$$ \sigma_{23}=2G\varepsilon_{23} $$

# 7. 선형 등방 Hooke 법칙에서의 상수 관계

- 등방성을 고려하지 않은 Hooke 법칙에서 랭크 4의 탄성계수 텐서$E_{ijkl}$가 81개의 성분을 가질 수 있는 것으로 보인다 (3x3x3x3=81).
- 하지만 등방성을 고려한 Hooke의 법칙에서는 단 2개의 스칼라 값을 활용했다 ($\lambda, G$)
- 사실 $\lambda$와 $G$ 의 패어 보다 영률 $E$와 포아송 비 $\nu$를 활용하는 경우가 더 많다. 그리고 이는 $G$와 $\lambda$와 관계된다.

$$G=\frac{E}{2(1+\nu)}$$

$$\lambda = \frac{E\nu}{(1+\nu)(1-2\nu)}$$

# 8. Voigt 표현법

- 삼차원으로 확장하여 표현한 Hooke의 법칙은 아래와 같다.
  $$ \sigma_{ij} = \sum_{k}^3\sum_{l}^3 E_{ijkl} \varepsilon _{kl} \text{ with } i=1,2,3\ \ \ j=1,2,3$$

- 응력과 변형률 텐서 모두 6개의 독립 성분만을 가지므로, 6성분을 가지는 랭크1의 행렬로 표현하여 표기하기도 한다.

- 그러한 방법중 Voigt표현을 활용하여 아래와 같이 표현한다.

$$ \mathbf\sigma^{voigt}=
\begin{bmatrix}
\sigma_{11}\\
\sigma_{22}\\
\sigma_{33}\\
\sigma_{23}\\
\sigma_{13}\\
\sigma_{12}\\
\end{bmatrix}$$


$$\mathbf\varepsilon^{voigt}=
\begin{bmatrix}
\varepsilon_{11}\\
\varepsilon_{22}\\
\varepsilon_{33}\\
2\varepsilon_{23}\\
2\varepsilon_{13}\\
2\varepsilon_{12}\\
\end{bmatrix}$$

- 위 방법을 확장하며 Hooke의 법칙을 새로 인덱스로 표기하면

$$
\sigma_i^{voigt}=\sum_{j}^6 E_{ij}^{voigt}\varepsilon_j^{voigt}
$$

로 간략히 표기할 수 있겠다. 그리고 이때 탄성계수 텐서가 2랭크 $6\times6$행렬 형태로 표기된다.

- 등방성 재료에서 $E_{ij}^{voigt}$의 각 성분은 아래와 같다.

$$
\mathbf E^{voigt}=
\begin{bmatrix}
\lambda + 2G & \lambda &\lambda &0 &0 &0 \\
\lambda &\lambda + 2G & \lambda &0 &0 &0 \\
\lambda & \lambda &\lambda + 2G &0 &0 &0 \\
0 & 0 &0 &G &0 &0 \\
0 & 0 &0 &0 &G &0 \\
0 & 0 &0 &0 &0 &G \\
\end{bmatrix}
$$

# 9. Compliance matrix

- Hooke의 법칙을 역으로 표현할 수 있다.

$$
\varepsilon=\mathbf S \mathbf \sigma
$$

- Voigt 표현을 활용하면

$$
\mathbf S^{voigt}=
\begin{bmatrix}
1/ E& -\nu/E & -\nu/E &0 &0 &0 \\
-\nu/E &1/E & -\nu/E &0 &0 &0 \\
-\nu/E & -\nu/E &1/E &0 &0 &0 \\
0 & 0 &0 &1/G &0 &0 \\
0 & 0 &0 &0 &1/G &0 \\
0 & 0 &0 &0 &0 &1/G \\
\end{bmatrix}
$$


# 10. Plane stress와  plane strain 조건에서의 Hooke 법칙

$$
\begin{bmatrix}
\sigma_{11}\\
\sigma_{22}\\
\sigma_{12}\\
\end{bmatrix}
=
\begin{bmatrix}
\frac{E}{1-\nu^2} & \frac{E}{1-\nu^2} & 0 \\
\frac{E}{1-\nu^2} & \frac{E}{1-\nu^2} & 0 \\
0 & 0 & G
\end{bmatrix}
\begin{bmatrix}
\varepsilon_{11}\\
\varepsilon_{22}\\
2\varepsilon_{12}
\end{bmatrix}
$$
