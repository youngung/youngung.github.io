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

- [1. Plastic work](#1-plastic-work)
- [2. 일 (work)](#2-일-work)
- [3. Equivalent strain (동등 변형률)](#3-equivalent-strain-동등-변형률)

# 1. Plastic work

- 항복 이후 금속은 어떻게 에너지를 소비하는가?
- 외부 힘이 가해져 변형이되면, 에너지가 전달된다.
- 에너지를 어떻게 저장하는 것인가?

# 2. 일 (work)

$$
dW=Fdx
$$

- 단위 부피당 일은?

$$
dW=\sigma d\varepsilon
$$

- 그런데 응력과 변형률은 텐서 물리량이다.

$$
dW=\boldsymbol \sigma d\boldsymbol \varepsilon
=\sum_i^3 \sum_j^3\sigma_{ij}\varepsilon_{ij}
$$

- 부피당 일의 단위 ($J/m^3$)
$$
[J/m^3]=[N m /m^3]=[N/m^2]=[Pa]
$$

- 총 일(total work)

$$
dW=dW^{el}+dW^{pl}
$$

- 탄성일 $dW^{el}$은 저장됨
- 소성일 $dW^{pl}$은 대부분 열로 변환되거나, 결함(dislocation, grain boundary)으로 저장된다.

- Plastic work

$$
dW^{pl}=\sum_i^3\sum_j^3\sigma_{ij}d\varepsilon_{ij}^{pl}
$$

# 3. Equivalent strain (동등 변형률)

텐서물리량인 다양한 변형률의 스칼라 '크기'만으로 환산하여 나타낸 값.
- 예를 들어, von Mises 동등 변형률은
$$
\varepsilon^{eq}=\sqrt{\frac{2}{3}\sum_i^3\sum_j^3\varepsilon_{ij}^{pl}\varepsilon_{ij}^{pl}}
$$

- 왜 $\frac{2}{3}$이 나오나? 일축인장과 동일한 값이 되도록 정규화 한 것이다.
