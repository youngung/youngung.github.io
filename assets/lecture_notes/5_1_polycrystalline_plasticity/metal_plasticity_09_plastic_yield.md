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

- [1. 탄성 한계와 항복(yielding)](#1-탄성-한계와-항복yielding)
- [2. 항복 응력 (yield stress)](#2-항복-응력-yield-stress)
- [3. 항복 응력의 중요성](#3-항복-응력의-중요성)
- [4. 항복 조건 (스칼라 응력 환경)](#4-항복-조건-스칼라-응력-환경)
- [5. 항복 조건](#5-항복-조건)
- [6. 등가 응력 (equivalent stress)](#6-등가-응력-equivalent-stress)
- [7. Tresca 항복 조건](#7-tresca-항복-조건)
- [8. Von Mises 항복 조건](#8-von-mises-항복-조건)

# 1. 탄성 한계와 항복(yielding)

- 'to yield' means 'to surrender', 'to stop resisting a force'.

- 더이상 탄성변형으로만 변형을 모두 수용하지 못하게 될 때, 소성 변형이 발생하기 시작한다.

- 소성 변형의 발생한다고해서 탄성 변형이 멈추는 것은 아니다!

- 아래 Hooke의 법칙만으로 소성 번형까지 설명할 수 없다.
$$
\sigma=E\varepsilon
$$

- 소성 변형이 발생하기 시작하는 조건 (yield condition; yield criterion)을 '항복 조건'이라 한다.

# 2. 항복 응력 (yield stress)

- 항복(plastic yielding)은 소성 번형이 발생하기 시작하는 현상이다. (다시 한번 말하지만, 소성 변형이 생겼다고해서 탄성 변형이 나타나지 않는 것이 아니다.)

- 보통 일정 이상의 임계 응력 이상이 가해질 소성 변형이 나타나기 시작한다.

- 따라서, 항복 조건을 주로 '응력' 기준으로 표현한다. 소성 변형이 발생하기 시작하는 응력값을 '항복응력'(yield stress)라 부른다.

# 3. 항복 응력의 중요성

- 항복 응력을 다르게 해석할 수도 있다. 높은 항복 응력값을 가진 재료는, 소성 변형에 대한 '저항'이 높은 것으로 이해할 수 있다. 따라서 형태가 유지되는 것이 중요한 '구조물'의 경우, 항복 응력값이 높을 수록 안정적이라 볼 수 있다.

- 항복 응력(yield stress)을 항복 강도(yield strength)라 부르는 이유는 이러한 해석에서 비롯된다 볼 수 있다.

- 응력과 변형률이 스칼라 물리량이라면 항복의 표현은 매우 간단해진다.

# 4. 항복 조건 (스칼라 응력 환경)
- 항복 강도가 100 MPa이라면, 항복이 발생하는 조건은 아래 등식으로 표현될 수 있다.

$$
|\sigma|=100\ MPa
$$

- 항복 조건을 만족하지 않는 조건은 아래와 같다.

$$
|\sigma|<100\ MPa
$$

- 임의의 항복 응력을 $\sigma^Y$라 표기하면, 스칼라 응력 환경(예 1축 인장)에서의 항복 조건은 아래와 같다.

$$
|\sigma|<\sigma^Y
$$

# 5. 항복 조건

- 하지만 앞서 다루었던 응력은 스칼라 물리량으로 충분히 표현되지 않는다. 일반적인 텐서 응력환경에서 항복 조건은 따라서, 응력 텐서를 활용해서 아래와 같이 표현되어야 겠다.

$$
f(\boldsymbol\sigma)=\sigma^Y
$$

- 이때 $f(\boldsymbol\sigma)$를 우리는 항복 함수(yield function)이라 부르며 아래와 조건을 만족해야 한다.

  - $f(\boldsymbol\sigma)<\sigma^Y$: 재료가 탄성 거동을 한다.
  - $f(\boldsymbol\sigma)=\sigma^Y$: 재료가 소성 변형도 한다.
  - $f(\boldsymbol\sigma)>\sigma^Y$: 허용되지 않는다.

# 6. 등가 응력 (equivalent stress)

- 재료가 겪는 응력 상태(stress state)는 응력 텐서 물리량으로 표현되어야 한다. 이는 응력의 방향성과 세기를 모두 표현하기 위해서이다. 그런데 만약 응력의 '세기'만이 항복 조건으로 활용될 수 있다면, 응력의 세기를 표현하는 '스칼라'로 환산된 값을 활용해 항복함수를 표현할 수 있겠다.

- 이렇게 응력의 세기를 표현한 스칼라 값을 '등가 응력'이라 부른다.

# 7. Tresca 항복 조건

- 최대 전단 응력값이 임계값에 도달하는 조건
- 이해를 위해 주응력(principal stress)와 좌표변환을 이애할 필요가 있다.

# 8. Von Mises 항복 조건

- Von Mises의 등가 응력, $\sigma^{VM}$은 아래와 같이 정의된다.

$$
\sigma^{VM}=\sqrt{0.5\big[(\sigma_{11}-\sigma_{22})^2+(\sigma_{22}-\sigma_{33})^2+(\sigma_{33}-\sigma_{11})^2+3(\sigma_{12}^2+\sigma_{13}^2+\sigma_{23}^2)\big]}
$$

- Von Mises 항복 조건은 아래와 같다.
  - $\sigma^{VM}<\sigma^Y$: 재료가 탄성 거동을 한다.
  - $\sigma^{VM}=\sigma^Y$: 재료가 소성 변형도 한다.
