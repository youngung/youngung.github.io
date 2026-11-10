---
layout: distill
title: 소성 항복
description: 항복응력과 Tresca, von Mises 및 Hosford 항복조건
target: 대학원
permalink:
featured: true
prerequisite: 선형 탄성, 주응력과 편차응력, Mohr 원
toc: false

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

**목차**

* TOC
{:toc}

# 1. 탄성 한계와 항복(yielding)

- 'to yield' means 'to surrender', 'to stop resisting a force'.

- 더이상 탄성변형으로만 변형을 모두 수용하지 못하게 될 때, 소성 변형이 발생하기 시작한다.

- 소성 변형의 발생한다고해서 탄성 변형이 멈추는 것은 아니다!

- 아래 Hooke의 법칙만으로 소성변형까지 설명할 수 없다.
$$
\sigma=E\varepsilon
$$

- 소성 변형이 발생하기 시작하는 조건 (yield condition; yield criterion)을 '항복 조건'이라 한다.

전체 변형률은 탄성변형률과 소성변형률의 합으로 분해한다.

$$
\boldsymbol\varepsilon
=\boldsymbol\varepsilon^e+\boldsymbol\varepsilon^p.
$$

항복 이후에도 $\boldsymbol\varepsilon^e$는 존재한다. 하중을 제거하면 탄성분은 회복되지만
$\boldsymbol\varepsilon^p$는 잔류한다. 또한 항복은 소성변형의 시작이고 파괴는 균열이나
분리에 의해 하중전달능력을 잃는 현상이므로 서로 구분해야 한다.

# 2. 항복 응력 (yield stress)

- 항복(plastic yielding)은 소성변형이 발생하기 시작하는 현상이다. 소성변형이 생긴
  뒤에도 탄성변형 성분은 함께 존재할 수 있다.

- 보통 응력이 임계값에 도달하면 소성변형이 나타나기 시작한다.

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
\boxed{f(\boldsymbol\sigma)=\sigma_{eq}(\boldsymbol\sigma)-\sigma^Y}
$$

- 이때 $f(\boldsymbol\sigma)$를 우리는 항복 함수(yield function)이라 부르며 아래와 조건을 만족해야 한다.

  - $f(\boldsymbol\sigma)<0$: 응력상태가 항복면 안에 있어 탄성 거동을 한다.
  - $f(\boldsymbol\sigma)=0$: 응력상태가 항복면 위에 있다.
  - $f(\boldsymbol\sigma)>0$: 속도 비의존 모델에서는 허용되지 않으며 소성보정이 필요하다.

## 5.1. 응력공간, 항복면과 하중경로

대칭 응력텐서는 여섯 개의 독립성분을 가지므로 하나의 응력상태를 6차원 응력공간의
점으로 볼 수 있다. 주응력으로 표현하면 $(\sigma_1,\sigma_2,\sigma_3)$의 3차원
주응력 공간을 사용한다. $f=0$은 항복면, $f<0$은 탄성영역이다.

응력상태가 시간에 따라 이동하는 궤적을 하중경로(stress path)라 한다. 같은 최종
응력점이라도 재료의 경화와 이력에 따라 소성변형은 달라질 수 있다. 특히
$f=0$이라는 사실만으로 소성변형률이 반드시 증가하는 것은 아니다. 항복면에서
안쪽으로 향하는 제하(unloading)는 탄성일 수 있고, 바깥쪽으로 진행하려는 하중은
소성보정과 경화를 요구한다.

비례하중 $\boldsymbol\sigma=\alpha\boldsymbol\sigma_0$에서는 von Mises와 Tresca처럼
응력에 대해 1차 동차인 등가응력에 대해

$$
\sigma_{eq}(\alpha\boldsymbol\sigma_0)
=\alpha\sigma_{eq}(\boldsymbol\sigma_0),
\qquad
\alpha_Y=\frac{\sigma^Y}{\sigma_{eq}(\boldsymbol\sigma_0)}
$$

이므로 최초 항복 배율을 바로 구할 수 있다.

# 6. 등가 응력 (equivalent stress)

- 재료가 겪는 응력 상태(stress state)는 응력 텐서 물리량으로 표현되어야 한다. 이는 응력의 방향성과 세기를 모두 표현하기 위해서이다. 그런데 만약 응력의 '세기'만이 항복 조건으로 활용될 수 있다면, 응력의 세기를 표현하는 '스칼라'로 환산된 값을 활용해 항복함수를 표현할 수 있겠다.

- 이렇게 응력의 세기를 표현한 스칼라 값을 '등가 응력'이라 부른다.

# 7. Tresca 항복 조건

Tresca 조건은 최대 전단응력이 임계값에 도달할 때 항복한다고 본다. 주응력을
$\sigma_1\ge\sigma_2\ge\sigma_3$으로 정렬하면

$$
\tau_{\max}=\frac{\sigma_1-\sigma_3}{2}.
$$

일축 인장 $(\sigma^Y,0,0)$으로 보정하면 $\tau_{\max}=\sigma^Y/2$이므로

$$
\boxed{\sigma^{T}
=\max\{\lvert\sigma_1-\sigma_2\rvert,
\lvert\sigma_2-\sigma_3\rvert,
\lvert\sigma_3-\sigma_1\rvert\}},
\qquad
f_T=\sigma^T-\sigma^Y
$$

로 쓸 수 있다. 순수전단의 주응력은 $(\tau,0,-\tau)$이므로 Tresca의 전단
항복응력은 $\tau^Y=\sigma^Y/2$이다.

# 8. Von Mises 항복 조건

- Von Mises의 등가 응력, $\sigma^{VM}$은 아래와 같이 정의된다.

$$
\sigma^{VM}=\sqrt{\frac{1}{2}\big[(\sigma_{11}-\sigma_{22})^2+(\sigma_{22}-\sigma_{33})^2+(\sigma_{33}-\sigma_{11})^2+6(\sigma_{12}^2+\sigma_{13}^2+\sigma_{23}^2)\big]}
$$

- Von Mises 항복 조건은 아래와 같다.
  - $\sigma^{VM}<\sigma^Y$: 재료가 탄성 거동을 한다.
  - $\sigma^{VM}=\sigma^Y$: 재료가 소성 변형도 한다.

주응력 또는 편차응력으로는 같은 값을 다음처럼 쓸 수 있다.

$$
\sigma^{VM}
=\sqrt{\frac{(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2
+(\sigma_3-\sigma_1)^2}{2}}
=\sqrt{\frac32\boldsymbol s:\boldsymbol s}
=\sqrt{3J_2}.
$$

일축 인장에서 $\sigma^{VM}=\lvert\sigma\rvert$가 되도록 계수가 정해져 있다.
순수전단에서는 $\sigma^{VM}=\sqrt3\tau$이므로
$\tau^Y=\sigma^Y/\sqrt3\approx0.577\sigma^Y$이다. 따라서 같은 일축 항복응력으로
보정했을 때 Tresca가 순수전단 항복을 더 이르게 예측한다.

## 8.1. 다축 응력 판정 예제

주응력이 $(120,40,-20)\,\mathrm{MPa}$이고 $\sigma^Y=100\,\mathrm{MPa}$라 하자.
Tresca와 von Mises 등가응력은 각각

$$
\sigma^T=120-(-20)=140\,\mathrm{MPa},
$$

$$
\sigma^{VM}
=\sqrt{\frac{(120-40)^2+(40+20)^2+(-20-120)^2}{2}}
=\sqrt{14800}\approx121.7\,\mathrm{MPa}
$$

이다. 두 조건 모두 초기 항복면 밖의 시험 응력상태라고 판정한다. 속도 비의존
탄소성 계산에서는 이 상태를 그대로 허용하는 것이 아니라 항복면으로 되돌리는
소성보정이 필요하다.

## 8.2. 항복에서 평균응력과 편차응력의 역할

응력은 $\boldsymbol\sigma=\sigma_m\boldsymbol I+\boldsymbol s$로 분해할 수 있다.
연성금속의 von Mises 항복은 형상변화를 일으키는 편차응력 $\boldsymbol s$에만 의존한다.
따라서 모든 주응력에 같은 정수압 응력을 더해도 von Mises 등가응력은 변하지 않는다.
다만 정수압 응력은 연성파괴, 공극 성장과 압력 의존 재료의 항복에는 영향을 줄 수 있다.

# 9. Hosford 항복 함수

## 9.1. 정의와 지수의 의미

von Mises 항복조건은 여러 응력상태를 하나의 등가응력으로 표현하지만, 항복면의
형태가 정해져 있다. Hosford 항복함수는 **지수 $a$로 항복면의 형태를 조절하는
등방성 항복모델**이다. 세 주응력 $\sigma_1,\sigma_2,\sigma_3$
(응력 텐서의 고유값)을 이용하여 다음과 같이 정의한다.

$$
\boxed{\sigma^{H}=\left[\frac{
|\sigma_1-\sigma_2|^a+|\sigma_2-\sigma_3|^a+|\sigma_3-\sigma_1|^a
}{2}\right]^{1/a}},\qquad a\geq1
$$

$$
\boxed{f_H(\boldsymbol\sigma)=\sigma^{H}-\sigma^Y}
$$

여기서 $a$는 무차원 재료 매개변수이고 $\sigma^Y$는 일축 인장 항복응력이다.
$f_H<0$이면 항복면 내부, $f_H=0$이면 항복면 위이다.
위 식의 $\sigma_i$는 임의 좌표계에서의 수직응력 $\sigma_{ii}$와 구분해야 한다.
전단응력이 존재하면 먼저 주응력을 구한 뒤 대입한다.

일축 인장 $(\sigma,0,0)$에서는

$$
\sigma^{H}=\left[\frac{|\sigma|^a+0+|\sigma|^a}{2}\right]^{1/a}
=|\sigma|
$$

이므로 모든 $a$에 대해 같은 일축 항복응력으로 보정된다.
또한 주응력의 **차이**만 사용하므로 정수압 응력에 무관하고,
주응력의 순서나 응력의 부호를 모두 바꾸어도 값이 같다.
따라서 이 모델은 등방성이며 인장과 압축의 항복강도가 같다.

## 9.2. von Mises 및 Tresca 조건과의 관계

$a=2$를 대입하면

$$
\sigma^{H}\big|_{a=2}
=\sqrt{\frac{(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2}{2}}
=\sigma^{VM}
$$

로서 von Mises 등가응력과 정확히 일치한다. 이는 8절의 식을 주응력 좌표계에서
쓴 것이다. $a=4$도 세 주응력 차이 사이의 대수적 관계로 인해 von Mises와
일치하므로, 지수를 바꾸면 항상 다른 항복면이 생기는 것은 아니다.
한편 $a\to\infty$이면 가장 큰 주응력 차이가 지배하여

$$
\lim_{a\to\infty}\sigma^{H}
=\max\{|\sigma_1-\sigma_2|,|\sigma_2-\sigma_3|,|\sigma_3-\sigma_1|\}
=\sigma_{\max}-\sigma_{\min}
$$

이 되어 Tresca 조건으로 수렴한다.
정수압축에 수직인 편차응력 평면에서 von Mises 항복면의 단면은 원이며,
$a=6,8$인 Hosford 단면은 이 원과 Tresca의 내접 정육각형 사이에 놓인다.

| 비교 항목 | von Mises | Hosford |
| --- | --- | --- |
| 항복면 형태의 조절 | 별도의 형상 매개변수 없음 | 지수 $a$로 조절 |
| 정수압 응력의 영향 | 없음 | 없음 |
| 방향에 따른 항복강도 | 동일 (등방성) | 동일 (등방성) |
| 같은 일축 항복응력으로 보정 후 다축 예측 | 고정된 형태 | $a$에 따라 달라짐 |

무작위 결정방위를 가진 입방정 다결정의 항복면을 근사할 때
BCC에는 $a=6$, FCC에는 $a=8$이 흔히 사용된다.
이는 결정구조만으로 모든 재료의 지수가 확정된다는 뜻은 아니며,
실제 적용에서는 다축 항복 데이터와 비교해야 한다.
집합조직에 의한 방향별 항복강도 차이는 이 등방성 식만으로 표현할 수 없다.

## 9.3. 순수전단에서의 수치 비교

순수전단 $\sigma_{12}=\sigma_{21}=\tau$이고 나머지 성분이 0이면,
주응력은 $(\tau,0,-\tau)$이다 ($\tau\geq0$).
따라서

$$
\sigma^{H}=\left[\frac{\tau^a+\tau^a+(2\tau)^a}{2}\right]^{1/a}
=(1+2^{a-1})^{1/a}\tau
$$

이므로 전단 항복응력 $\tau^Y$는

$$
\boxed{\frac{\tau^Y}{\sigma^Y}=(1+2^{a-1})^{-1/a}}
$$

이다. 같은 일축 항복응력 $\sigma^Y=100\ \mathrm{MPa}$로 보정하면 다음과 같다.

| 항복조건 | $\tau^Y/\sigma^Y$ | $\tau^Y$ (MPa) |
| --- | --- | --- |
| von Mises ($a=2$) | $1/\sqrt{3}\approx0.5774$ | 57.74 |
| Hosford ($a=6$) | $33^{-1/6}\approx0.5584$ | 55.84 |
| Hosford ($a=8$) | $129^{-1/8}\approx0.5453$ | 54.53 |
| Tresca ($a\to\infty$) | $1/2$ | 50.00 |

예를 들어 $\tau=56\ \mathrm{MPa}$이면 von Mises 등가응력은
$\sqrt{3}\times56\approx97.0\ \mathrm{MPa}$이므로 항복면 내부이다.
반면 $a=6$인 Hosford 등가응력은 $33^{1/6}\times56\approx100.3\ \mathrm{MPa}$로
항복면을 넘는다. 속도 비의존 탄소성 모델에서는 소성보정이 필요하다.
이처럼 **일축 인장에서는 일치해도 순수전단 등 다축 응력상태에서는 항복 예측이 달라진다.**

참고: [Hosford (1972), *A Generalized Isotropic Yield Criterion*](https://doi.org/10.1115/1.3422732),
[Sandia Sierra/SM 사용자 설명서의 Hosford 모델](https://www.sandia.gov/files/sierra/SM_Users_5_30/user_manual/materials/materials.html).

# 10. 연습 문제

## 문제 1

일축 인장시험에서 응력이 항복응력보다 작을 때 하중을 제거하면 변형은 어떻게 되는가?

<!--
풀이와 해답:
이상적인 탄소성 구분에서는 탄성변형이 회복되어 원래 상태로 돌아간다.
-->

## 문제 2

주응력이 $(100,0,0)$ MPa일 때 von Mises 등가응력을 구하라.

<!--
풀이와 해답:
일축 응력상태이므로 von Mises 등가응력은 100 MPa이다.
-->

## 문제 3

정수압 응력만 작용할 때 von Mises 항복이 발생하지 않는 이유를 설명하라.

<!--
풀이와 해답:
von Mises 항복은 형상변화를 일으키는 편차응력에 의존하며 정수압 응력의 편차성분은 0이기 때문이다.
-->

## 문제 4

Tresca 항복조건이 사용하는 주응력의 조합을 설명하라.

<!--
풀이와 해답:
최대 주응력과 최소 주응력의 차이, 즉 최대전단응력에 해당하는 값을 사용한다.
-->

## 문제 5

기준 응력상태의 von Mises 등가응력이 $80\,\mathrm{MPa}$이고 일축 항복응력이
$120\,\mathrm{MPa}$일 때, 비례하중의 최초 항복 배율을 구하라.

<!--
풀이와 해답:
alpha_Y=120/80=1.5이다.
-->

## 문제 6

일축 항복응력이 $100\,\mathrm{MPa}$인 재료에 순수전단
$\tau=55\,\mathrm{MPa}$가 작용한다. Tresca와 von Mises 조건의 항복 여부를 비교하라.

<!--
풀이와 해답:
Tresca 등가응력은 2 tau=110 MPa이므로 항복한다.
von Mises 등가응력은 sqrt(3) tau 약 95.3 MPa이므로 탄성영역이다.
-->

---

[이전 강의]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_11_Mohr_circle.md %}) | [강의 목록]({% link _lectures/5_1_polycrystalline_Plasticity.md %}) | [다음 강의]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_13_flow_rule.md %})
