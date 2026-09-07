---
layout: distill
title: 질량분율과 원자분율 변환
description: 합금 조성의 질량분율과 원자분율을 이해하고 변환하기
target: 1학년 2학기
permalink:
featured: true
prerequisite: Python 함수, NumPy 배열 기초
toc:
  sidebar: left
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

- [1. 학습 목표](#1-학습-목표)
- [2. 합금 조성을 나타내는 방법](#2-합금-조성을-나타내는-방법)
- [3. 질량과 원자 개수를 연결하는 몰](#3-질량과-원자-개수를-연결하는-몰)
- [4. 질량분율에서 원자분율로 변환](#4-질량분율에서-원자분율로-변환)
- [5. 원자분율에서 질량분율로 변환](#5-원자분율에서-질량분율로-변환)
- [6. 이원계 합금 계산 예제](#6-이원계-합금-계산-예제)
- [7. 다원계 합금 계산 예제](#7-다원계-합금-계산-예제)
- [8. NumPy로 변환 함수 만들기](#8-numpy로-변환-함수-만들기)
- [9. 보충: 질량분율과 부피분율](#9-보충-질량분율과-부피분율)
- [10. 조성을 읽고 쓸 때 주의할 점](#10-조성을-읽고-쓸-때-주의할-점)
- [11. 핵심 정리](#11-핵심-정리)
- [12. 쉬운 연습 문제](#12-쉬운-연습-문제)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 질량분율과 원자분율의 차이를 설명할 수 있다.
- 원자량을 이용해 질량을 몰수로 바꿀 수 있다.
- 이원계 및 다원계 합금의 질량분율을 원자분율로 변환할 수 있다.
- 원자분율을 질량분율로 역변환할 수 있다.
- NumPy 배열을 이용해 여러 성분의 조성을 한 번에 변환할 수 있다.
- 질량분율, 원자분율과 부피분율을 구분할 수 있다.

# 2. 합금 조성을 나타내는 방법

합금에서 각 원소가 얼마나 들어 있는지는 여러 방법으로 나타낼 수 있다. 먼저 용어를
구분하자.

| 조성 표시 | 비교하는 양 | 흔히 쓰는 기호 | 백분율 표시 |
|---|---|---|---|
| 질량분율 | 각 성분의 질량 | $w_i$ | wt.% 또는 mass% |
| 원자분율 | 각 성분의 원자 개수 | $x_i$ | at.% |
| 몰분율 | 각 성분의 몰수 | $x_i$ | mol.% |
| 부피분율 | 각 성분 또는 상의 부피 | $f_i$ | vol.% |

일상적으로 ‘무게비’라고도 하지만, 물리적으로는 중력에 무관한 **질량분율(mass
fraction)**이라는 표현이 더 정확하다.

## 2.1. 질량분율

성분 $i$의 질량이 $m_i$이고 전체 질량이 $m_{total}$이면 질량분율은

$$
w_i=\frac{m_i}{m_{total}}
=\frac{m_i}{\sum_j m_j}
$$

이다. 질량 백분율은

$$
\mathrm{wt.\%}_i=100w_i
$$

이다.

예를 들어 전체 100 g 중 Al이 90 g, Cu가 10 g이면

$$
w_{Al}=0.90,
\qquad
w_{Cu}=0.10
$$

이므로 Al–10 wt.% Cu 합금이다.

## 2.2. 원자분율과 몰분율

성분 $i$의 원자 개수가 $N_i$이면 원자분율은

$$
x_i=\frac{N_i}{\sum_j N_j}
$$

이다. 같은 종류의 원자 $N_A$개를 1몰이라고 하므로 원소로 이루어진 합금에서는
원자분율과 몰분율의 수치가 같다.

$$
x_i=\frac{n_i}{\sum_j n_j}
$$

여기서 $n_i$는 성분 $i$의 몰수다. 원자 백분율은

$$
\mathrm{at.\%}_i=100x_i
$$

이다.

모든 분율의 합은 1이고 모든 백분율의 합은 100%여야 한다.

$$
\sum_iw_i=1,
\qquad
\sum_ix_i=1
$$

# 3. 질량과 원자 개수를 연결하는 몰

질량분율을 원자분율로 바꾸려면 질량을 원자 개수에 비례하는 몰수로 바꿔야 한다.

$$
\boxed{n_i=\frac{m_i}{M_i}}
$$

여기서 $M_i$는 성분 $i$의 몰질량이다. 원소의 몰질량은 주기율표에 표시된 원자량과
수치가 같고 단위는 일반적으로 g/mol을 사용한다.

예를 들어 Fe 55.845 g은 약 1 mol이고, C 12.011 g도 약 1 mol이다. 두 질량은 크게
다르지만 들어 있는 원자의 개수는 각각 약 1 mol만큼으로 같다.

| 원소 | 기호 | 몰질량 (g/mol) |
|---|---:|---:|
| 알루미늄 | Al | 26.982 |
| 탄소 | C | 12.011 |
| 철 | Fe | 55.845 |
| 니켈 | Ni | 58.693 |
| 구리 | Cu | 63.546 |

원자량이 작은 원소는 같은 질량 안에 더 많은 원자가 들어 있다. 따라서 질량분율과
원자분율은 일반적으로 같지 않다.

# 4. 질량분율에서 원자분율로 변환

질량분율 $w_i$를 알고 있다면 각 성분의 상대적인 몰수는 $w_i/M_i$에 비례한다. 이를
전체 몰수로 나누면 원자분율을 얻는다.

$$
\boxed{
x_i=
\frac{w_i/M_i}{\displaystyle\sum_j w_j/M_j}
}
$$

질량분율 대신 wt.%를 식에 그대로 넣어도 된다. 모든 성분에 공통으로 포함된 100이라는
인자가 분자와 분모에서 소거되기 때문이다.

계산 순서는 다음과 같다.

1. 편의를 위해 합금 전체 질량을 100 g으로 가정한다.
2. 각 원소의 질량을 몰질량으로 나누어 몰수를 구한다.
3. 각 원소의 몰수를 전체 몰수로 나눈다.
4. 결과의 합이 1 또는 100%인지 확인한다.

100 g을 가정하는 것은 계산을 쉽게 하기 위한 것이다. 분율이 같으면 1 g이나 1 kg을
가정해도 최종 원자분율은 같다.

# 5. 원자분율에서 질량분율로 변환

원자분율 $x_i$에 몰질량 $M_i$를 곱하면 각 성분의 상대적인 질량을 얻는다. 따라서

$$
\boxed{
w_i=
\frac{x_iM_i}{\displaystyle\sum_j x_jM_j}
}
$$

이다. at.%를 식에 그대로 넣어도 공통 인자가 소거된다.

계산 순서는 다음과 같다.

1. 편의를 위해 전체 원자 또는 전체 몰수를 100 mol로 가정한다.
2. 각 원소의 몰수에 몰질량을 곱해 질량을 구한다.
3. 각 질량을 전체 질량으로 나눈다.
4. 결과의 합이 1 또는 100%인지 확인한다.

두 변환식의 차이를 기억하는 간단한 방법은 다음과 같다.

- 질량 → 원자: 몰수를 구해야 하므로 몰질량으로 **나눈다**.
- 원자 → 질량: 질량을 구해야 하므로 몰질량을 **곱한다**.

# 6. 이원계 합금 계산 예제

## 6.1. Fe–1 wt.% C를 at.%로 변환

Fe–1 wt.% C 합금 100 g을 가정하면 Fe는 99 g, C는 1 g이다.

$$
n_{Fe}=\frac{99}{55.845}\approx1.773\ \mathrm{mol}
$$

$$
n_C=\frac{1}{12.011}\approx0.0833\ \mathrm{mol}
$$

따라서 탄소의 원자분율은

$$
x_C=\frac{0.0833}{1.773+0.0833}\approx0.0449
$$

이고 철의 원자분율은

$$
x_{Fe}=1-x_C\approx0.9551
$$

이다. 즉,

$$
\boxed{\mathrm{Fe\text{-}1\ wt.\%\ C}
\approx\mathrm{Fe\text{-}4.49\ at.\%\ C}}
$$

이다. C는 Fe보다 원자량이 훨씬 작으므로 1 wt.%라도 원자 개수 기준으로는 약 4.49
at.%가 된다.

## 6.2. Fe–5 at.% C를 wt.%로 변환

전체가 100 mol의 원자라고 가정하면 Fe는 95 mol, C는 5 mol이다. 각 성분의 상대적인
질량은

$$
m_{Fe}=95(55.845)=5305.275
$$

$$
m_C=5(12.011)=60.055
$$

이다. 따라서 탄소의 질량분율은

$$
w_C=\frac{60.055}{5305.275+60.055}\approx0.01119
$$

이므로

$$
\boxed{\mathrm{Fe\text{-}5\ at.\%\ C}
\approx\mathrm{Fe\text{-}1.12\ wt.\%\ C}}
$$

이다.

# 7. 다원계 합금 계산 예제

Al–4 wt.% Cu–2 wt.% Mg 합금을 생각하자. 나머지는 Al이므로 조성은 Al 94 wt.%,
Cu 4 wt.%, Mg 2 wt.%이다. Mg의 몰질량은 24.305 g/mol이다.

100 g의 합금을 가정하면 상대적인 몰수는

$$
\frac{94}{26.982}\approx3.484,
\qquad
\frac{4}{63.546}\approx0.0630,
\qquad
\frac{2}{24.305}\approx0.0823
$$

mol이다. 각각을 전체 몰수로 나누면 대략

$$
x_{Al}=0.9600,
\qquad
x_{Cu}=0.0174,
\qquad
x_{Mg}=0.0227
$$

을 얻는다. 따라서 원자 백분율은 약 Al 96.00 at.%, Cu 1.74 at.%, Mg 2.27 at.%이다.

다원계 합금에서도 계산 원리는 이원계와 같다. 각 성분을 몰수로 바꾼 뒤 전체 합으로
나누면 된다.

# 8. NumPy로 변환 함수 만들기

## 8.1. 질량분율에서 원자분율로

여러 원소의 조성을 NumPy 배열에 같은 순서로 저장하면 한 번에 계산할 수 있다.

~~~python
import numpy as np


def weight_to_atomic(weight_percent, atomic_weight):
    weight_percent = np.asarray(weight_percent, dtype=float)
    atomic_weight = np.asarray(atomic_weight, dtype=float)

    if weight_percent.shape != atomic_weight.shape:
        raise ValueError("composition and atomic weight must have the same shape")
    if np.any(weight_percent < 0):
        raise ValueError("composition cannot be negative")
    if np.any(atomic_weight <= 0):
        raise ValueError("atomic weight must be positive")
    if np.isclose(weight_percent.sum(), 0):
        raise ValueError("the sum of composition must be positive")

    relative_moles = weight_percent / atomic_weight
    atomic_fraction = relative_moles / relative_moles.sum()

    return 100.0 * atomic_fraction


elements = np.array(["Fe", "C"])
weight_percent = np.array([99.0, 1.0])
atomic_weight = np.array([55.845, 12.011])

atomic_percent = weight_to_atomic(weight_percent, atomic_weight)

for element, value in zip(elements, atomic_percent):
    print(f"{element}: {value:.2f} at.%")
~~~

입력 조성의 합이 반드시 100일 필요는 없다. 함수 안에서 전체 상대 몰수로 다시
정규화하기 때문이다. 다만 입력값들이 모두 같은 단위와 기준의 질량값이어야 한다.

## 8.2. 원자분율에서 질량분율로

~~~python
def atomic_to_weight(atomic_percent, atomic_weight):
    atomic_percent = np.asarray(atomic_percent, dtype=float)
    atomic_weight = np.asarray(atomic_weight, dtype=float)

    if atomic_percent.shape != atomic_weight.shape:
        raise ValueError("composition and atomic weight must have the same shape")
    if np.any(atomic_percent < 0):
        raise ValueError("composition cannot be negative")
    if np.any(atomic_weight <= 0):
        raise ValueError("atomic weight must be positive")
    if np.isclose(atomic_percent.sum(), 0):
        raise ValueError("the sum of composition must be positive")

    relative_mass = atomic_percent * atomic_weight
    weight_fraction = relative_mass / relative_mass.sum()

    return 100.0 * weight_fraction


atomic_percent = np.array([95.0, 5.0])
weight_percent = atomic_to_weight(atomic_percent, atomic_weight)

for element, value in zip(elements, weight_percent):
    print(f"{element}: {value:.2f} wt.%")
~~~

## 8.3. 왕복 변환으로 검산하기

변환한 값을 다시 원래 단위로 역변환하면 코드와 원소 순서가 올바른지 확인할 수 있다.

~~~python
original_weight_percent = np.array([94.0, 4.0, 2.0])
atomic_weight_al_cu_mg = np.array([26.982, 63.546, 24.305])

converted_atomic_percent = weight_to_atomic(
    original_weight_percent,
    atomic_weight_al_cu_mg,
)
recovered_weight_percent = atomic_to_weight(
    converted_atomic_percent,
    atomic_weight_al_cu_mg,
)

print(converted_atomic_percent)
print(recovered_weight_percent)
print(np.allclose(original_weight_percent, recovered_weight_percent))
~~~

마지막 결과가 <code>True</code>이면 허용되는 부동소수점 오차 범위에서 원래 조성을
회복한 것이다.

# 9. 보충: 질량분율과 부피분율

원자분율과 부피분율은 서로 다른 개념이다. 부피분율로 변환하려면 원자량이 아니라 각
성분 또는 상의 밀도 $\rho_i$가 필요하다.

질량 $m_i$와 부피 $V_i$의 관계는

$$
V_i=\frac{m_i}{\rho_i}
$$

이므로 질량분율에서 부피분율로의 변환식은

$$
\boxed{
f_i=
\frac{w_i/\rho_i}{\displaystyle\sum_jw_j/\rho_j}
}
$$

이다. 반대 변환은

$$
\boxed{
w_i=
\frac{f_i\rho_i}{\displaystyle\sum_jf_j\rho_j}
}
$$

이다.

이 식은 각 성분 또는 상의 밀도를 알고 있고 부피가 단순히 더해진다고 가정할 때
사용한다. 합금을 구성하는 원소의 밀도를 그대로 사용해 실제 합금상의 부피분율을 정확히
구할 수 있다고 단정해서는 안 된다. 실제 상의 부피분율을 구할 때는 각 **상(phase)의
조성과 밀도**가 필요하다.

# 10. 조성을 읽고 쓸 때 주의할 점

- 숫자만 쓰지 말고 wt.%, at.% 또는 vol.%를 반드시 표시한다.
- 원소 배열과 원자량 배열의 순서를 같게 유지한다.
- 모든 성분의 분율 합이 1 또는 100%인지 확인한다.
- ‘나머지는 Fe’와 같은 표현이 있으면 명시된 원소의 합을 100%에서 빼서 Fe 조성을 구한다.
- 원자분율 변환에는 밀도가 아니라 원자량 또는 몰질량을 사용한다.
- 부피분율 변환에는 원자량이 아니라 밀도를 사용한다.
- 화합물의 몰분율과 화합물 내부 원소의 원자분율을 혼동하지 않는다.
- 원자량은 필요한 유효숫자에 맞게 사용하고, 계산 중간에는 지나치게 일찍 반올림하지 않는다.

예를 들어 ‘Fe–1C’라는 표현만으로는 1 wt.% C인지 1 at.% C인지 알 수 없다. 보고서와
그래프의 축에는 조성 기준을 명확히 써야 한다.

# 11. 핵심 정리

- 질량분율은 질량을, 원자분율은 원자 개수 또는 몰수를 기준으로 한다.
- 질량을 몰수로 바꾸려면 몰질량으로 나눈다.
- 질량분율에서 원자분율로의 변환은
  $x_i=(w_i/M_i)/\sum_j(w_j/M_j)$이다.
- 원자분율에서 질량분율로의 변환은
  $w_i=(x_iM_i)/\sum_j(x_jM_j)$이다.
- 원자량이 작은 원소는 같은 질량 안에 더 많은 원자가 들어 있다.
- 왕복 변환과 조성 합계를 이용하면 계산을 쉽게 검산할 수 있다.
- 부피분율은 밀도를 사용하며 원자분율과 구분해야 한다.

# 12. 쉬운 연습 문제

## 문제 1

전체 200 g의 합금에 Al이 180 g, Cu가 20 g 들어 있다. 각 원소의 질량 백분율을
구하시오.

<!--
풀이와 해답:
Al은 180 / 200 x 100 = 90 wt.%, Cu는 20 / 200 x 100 = 10 wt.%이다.
-->

## 문제 2

어떤 성분의 질량을 몰수로 바꾸려면 무엇으로 나누어야 하는가?

<!--
풀이와 해답:
그 성분의 몰질량 또는 원자량에 해당하는 값으로 나눈다.
-->

## 문제 3

Cu 63.546 g과 Al 26.982 g은 각각 약 1 mol이다. 이 혼합물의 Cu와 Al 원자분율을
구하시오.

<!--
풀이와 해답:
두 원소의 몰수가 각각 1 mol이므로 원자분율은 각각 0.5, 즉 50 at.%이다.
-->

## 문제 4

Fe 55.845 g과 C 12.011 g을 혼합하였다. Fe와 C의 질량 백분율과 원자 백분율을
각각 구하시오.

<!--
풀이와 해답:
전체 질량은 67.856 g이다. Fe는 약 82.30 wt.%, C는 약 17.70 wt.%이다.
두 원소가 각각 1 mol이므로 Fe와 C는 각각 50 at.%이다.
-->

## 문제 5

Fe–1 wt.% C에서 C의 원자 백분율이 1 at.%보다 큰 이유를 설명하시오.

<!--
풀이와 해답:
C의 원자량이 Fe보다 작아 같은 질량 안에 더 많은 C 원자가 들어 있기 때문이다.
실제 변환값은 약 4.49 at.% C이다.
-->

## 문제 6

원자분율에서 질량분율로 변환할 때 원자분율에 몰질량을 곱하는지 나누는지 쓰시오.

<!--
풀이와 해답:
상대적인 질량을 구해야 하므로 원자분율에 몰질량을 곱한다.
-->

## 문제 7

질량분율에서 부피분율을 구하려면 각 성분의 어떤 물성이 필요한가?

<!--
풀이와 해답:
각 성분 또는 상의 밀도가 필요하다.
-->

## 문제 8

NumPy 변환 결과가 올바른지 확인할 수 있는 방법을 두 가지 쓰시오.

<!--
풀이와 해답:
변환된 조성의 합이 100%인지 확인하고, 역변환하여 원래 조성이 회복되는지 확인한다.
-->
