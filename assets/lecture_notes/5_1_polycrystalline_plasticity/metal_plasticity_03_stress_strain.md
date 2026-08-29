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

- [1. 소성 역학에서 물성 정의](#1-소성-역학에서-물성-정의)
- [2. 정량적 물리량 표현을 위한 단위계](#2-정량적-물리량-표현을-위한-단위계)
- [3. 일축 인장 시험](#3-일축-인장-시험)
- [4. 공칭 변형률, 공칭 응력으로부터 진응력, 진변형률 구하기](#4-공칭-변형률-공칭-응력으로부터-진응력-진변형률-구하기)
- [5. 재료의 다양한 기계적 성질](#5-재료의-다양한-기계적-성질)

# 1. 소성 역학에서 물성 정의

- 물질에 대한 자극과 그로 인한 반응 사이의 관계를 '성질'로 나타낸다.

- 다양한 자극과 반응 중, 우리의 관심은 '기계적' 자극과 '기계적' 반응이다.

- 힘, 물질의 운동 상태 변화(위치, 속도, 가속도) 혹은 형태의 변화(변형)가 기계적 자극과 반응으로 쓰일 수 있다.

- 소성 가공 공정에서, 힘과 형태의 변화(변형)가 주된 기계적 자극/반응이다.

- 그런데 힘과 변형은 '크기' 물리량이며, 우리는 그에 상응하는 '세기'물리량을 활용해 성질을
  정의한다.

- 따라서, 힘은 응력(stress)으로 변형은 변형률(strain)으로 대신하여 사용한다.

# 2. 정량적 물리량 표현을 위한 단위계

- SI 단위계에서 활용하는 m (미터), kg (킬로그램), s (초)를 활용해 '응력'과 변형률의
  단위를 파악할 수 있어야한다. 응력은 $kg/ m s^2$ 이 되며, 이를 줄여 우리는 $Pa$ (파스칼) 단위를 사용한다.
- 변형률은 단위가 없다 (dimensionless)
- 재료의 응력을 표현할 때 자주 사용되는 접두어 $M$ (메가)와 $G$(기가)는 각각 $10^6$, $10^9$을 뜻한다.

# 3. 일축 인장 시험

- 일축 인장 시험에서 센서를 통해 얻어진 신호를 바탕으로 힘과 위치의 변화, 즉 변위(displacement)를 측정하고 이를 각각 응력과 변형률로 바뀐다.

- 기록된 응력과 변형률을 활용해 다양한 물질의 성질을 측정할 수 있다.

- 변형률과 응력은 측정되는 방법에 따라 **공칭**과 **진**으로 나뉜다 (공칭 변형률, 공칭 응력, 진변형률, 진응력)

- 또한, 변형률과 응력 수직(normal)과 전단(shear) 성분으로 나뉜다.

# 4. 공칭 변형률, 공칭 응력으로부터 진응력, 진변형률 구하기

- 공칭 변형률

$$
\varepsilon^{engi} = \frac{\Delta l}{l_0}
$$

- 공칭 응력

$$
\sigma^{engi}=F/A_0
$$

- 진 변형률

$$
\varepsilon^{true} = \ln (1+\varepsilon^{engi})
$$

- 진 응력

$$
\sigma^{true} = \sigma^{engi} (1+\varepsilon^{engi})
$$

# 5. 재료의 다양한 기계적 성질

- 탄성 계수 (Elastic modulus)

- 전단 탄성 계수 (Shear modulus)

- 푸아송 비 (Poisson ratio)

- 항복 강도 (yield strength)

- 인장 강도 (tensile strength)
