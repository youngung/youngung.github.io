---
layout: distill
title:
description:
target:
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

- [1. 평면 조건](#1-평면-조건)
- [2. 평면 응력 조건](#2-평면-응력-조건)
- [3. 평면 변형 조건](#3-평면-변형-조건)

## 1. 평면 조건

- 실제 구조물은 3차원이지만, 2차원 변형이나 2차원 응력 상태로 근사할 수 있는 경우가 많다.
  - 예: 6면체 구조물의 세 모서리 중 한 모서리가 다른 두 모서리에 비해 매우 짧다면 평면 응력 조건을 활용할 수 있다 (판재 성형; sheet forming).
  - 예: 6면체 구조물의 세 모서리 중 한 모서리가 다른 두 모서리의 길이에 비해 매우 길때, 평면 변형 조건이 활용되는 경우가 있다 (압연; rolling).
- 3차원 응력 텐서를 매트릭스로 표현하고, 대칭성을 활용하면 $\sigma_{ij}=\sigma_{ji}$,

$$ \sigma =\begin{bmatrix}
\sigma_{11} & \sigma_{12} & \sigma_{13} \\
\sigma_{12} & \sigma_{22} & \sigma_{23} \\
\sigma_{13} & \sigma_{23} & \sigma_{33}
 \end{bmatrix}$$
로 표현되고, 6개의 독립성분 $\sigma_{11}, \sigma_{22},\sigma_{33},\sigma_{12}, \sigma_{13}, \sigma_{23}$이 존재한다.


- 3차원 변형률 텐서를 매트릭스로 표현하고, 대칭성을 활용하면 $\varepsilon_{ij}=\varepsilon_{ji}$,

$$\varepsilon =\begin{bmatrix}
\varepsilon_{11} & \varepsilon_{12} & \varepsilon_{13} \\
\varepsilon_{12} & \varepsilon_{22} & \varepsilon_{23} \\
\varepsilon_{13} & \varepsilon_{23} & \varepsilon_{33}
 \end{bmatrix}$$

로 표현되고, 6개의 독립성분 $\varepsilon_{11}, \varepsilon_{22},\varepsilon_{33},\varepsilon_{12}, \varepsilon_{13}, \varepsilon_{23}$이 존재한다.


## 2. 평면 응력 조건

- 만약 $\mathbf{e}_3$ 축방향이 짧은 모서리 방향이라면, 평면 응력 조건에서
응력텐서는 아래와 같다.
$$\sigma =\begin{bmatrix}
\sigma_{11} & \sigma_{12} & 0 \\
\sigma_{12} & \sigma_{22} & 0 \\
0 & 0 & 0
 \end{bmatrix}$$

- 왜냐면, 그 짧은 모서리 방향으로 응력이 build되기 어렵기 때문이다.

## 3. 평면 변형 조건


- 만약 $\mathbf{e}_3$ 축방향으로 변형이 거의 발생하지 않는 평면 변형 조건이라면
그에 해당하는 변형률 텐서는 아래와 같다.
$$\varepsilon =\begin{bmatrix}
\varepsilon_{11} & \varepsilon_{12} & 0 \\
\varepsilon_{12} & \varepsilon_{22} & 0 \\
0 & 0 & 0
 \end{bmatrix}$$

- 왜냐면, 그 짧은 모서리 방향으로 응력이 build되기 어렵기 때문이다.
$$
