---
layout: distill
title: 변형경화
description: 소성변형에 따른 금속의 유동응력 변화
target: 3학년 1학기
permalink:
featured: true
prerequisite: 응력과 변형률, 소성일
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

- [1. 학습 목표와 수업 구성](#1-학습-목표와-수업-구성)
- [2. 변형경화란 무엇인가?](#2-변형경화란-무엇인가)
- [3. 인장시험에서 관찰하는 변형경화](#3-인장시험에서-관찰하는-변형경화)
- [4. 유동응력과 소성변형률](#4-유동응력과-소성변형률)
- [5. Hollomon 경화법칙](#5-hollomon-경화법칙)
- [6. 경화지수의 의미](#6-경화지수의-의미)
- [7. 소성일과 변형경화](#7-소성일과-변형경화)
- [8. 다른 경화식과 모델의 한계](#8-다른-경화식과-모델의-한계)
- [9. 소성가공에서 변형경화가 중요한 이유](#9-소성가공에서-변형경화가-중요한-이유)
- [10. Python 실습](#10-python-실습)
  - [10.1. 소성변형률에 따른 유동응력](#101-소성변형률에-따른-유동응력)
  - [10.2. 실험값으로 $K$와 $n$ 구하기](#102-실험값으로-k와-n-구하기)
- [11. 핵심 정리](#11-핵심-정리)
- [12. 연습 문제](#12-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)
  - [문제 7](#문제-7)

# 1. 학습 목표와 수업 구성

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 변형경화(strain hardening)의 의미를 설명할 수 있다.
- 인장시험의 진응력–진변형률 곡선에서 변형경화 구간을 찾을 수 있다.
- 전체 변형률과 소성변형률을 구분할 수 있다.
- Hollomon 경화법칙의 $K$와 $n$이 무엇을 의미하는지 설명할 수 있다.
- 주어진 소성변형률에서 유동응력과 소성일을 계산할 수 있다.
- 변형경화가 소성가공 공정에 미치는 영향을 설명할 수 있다.


# 2. 변형경화란 무엇인가?

금속을 항복 이후까지 소성변형시키려면 변형이 증가할수록 일반적으로 더 큰 응력이
필요하다. 이 현상을 **변형경화(strain hardening)** 또는 **가공경화(work hardening)**라
한다.

> 변형경화는 소성변형이 누적됨에 따라 금속의 유동응력이 증가하는 현상이다.

여기서 유동응력(flow stress)은 재료가 현재 상태에서 소성변형을 계속하는 데 필요한
응력이다. 처음 항복할 때의 응력만을 뜻하지 않는다.

변형경화를 전위(dislocation)의 관점에서 간단히 설명하면 다음과 같다.

1. 소성변형이 진행되면 전위가 이동한다.
2. 변형이 누적되면서 전위의 수와 전위 사이의 상호작용이 증가한다.
3. 전위의 이동이 점차 어려워진다.
4. 소성변형을 계속하려면 더 큰 응력이 필요하다.

따라서 냉간가공된 금속은 일반적으로 가공 전보다 강도(strength)와 경도(hardness)가 증가하고 연성은
감소한다. 이 설명은 변형경화의 대표적인 미세조직적 해석이며, 실제 거동에는 결정구조,
온도, 변형속도와 회복 등의 영향도 함께 작용한다.

# 3. 인장시험에서 관찰하는 변형경화

인장시험에서 항복 이후 최대하중에 도달하기 전까지 응력이 증가하는 구간에서 변형경화를
관찰할 수 있다. 재료의 소성 거동을 식으로 나타낼 때는 일반적으로 공칭값보다 진응력과
진변형률을 사용한다.

균일변형 중 부피가 일정하다고 가정하면 공칭응력 $s$, 공칭변형률 $e$로부터

$$
\sigma=s(1+e),
\qquad
\varepsilon=\ln(1+e)
$$

와 같이 진응력 $\sigma$와 진변형률 $\varepsilon$을 구할 수 있다.

예를 들어 $e=0.10$, $s=300$ MPa이면

$$
\varepsilon=\ln(1.10)\approx0.0953,
\qquad
\sigma=300(1.10)=330\ \mathrm{MPa}
$$

이다.

이 변환은 시편이 균일하게 늘어나는 구간에서 사용한다. 네킹(necking)이 시작되면 변형이
국부적으로 집중되므로 단순한 변환식만으로 국부 진응력을 정확히 구할 수 없다.

# 4. 유동응력과 소성변형률

인장시험에서 측정한 전체 진변형률은 탄성변형률과 소성변형률의 합이다.

$$
\varepsilon=\varepsilon^{el}+\varepsilon^{pl}
$$

일축 탄성관계 $\varepsilon^{el}=\sigma/E$를 사용하면 소성변형률은

$$
\varepsilon^{pl}=\varepsilon-\frac{\sigma}{E}
$$

이다. 여기서 $E$는 영률(Young's modulus)이다.

예를 들어 $E=200$ GPa인 금속이 $\sigma=400$ MPa,
$\varepsilon=0.020$의 상태에 있다면

$$
\varepsilon^{el}=\frac{400}{200,000}=0.002,
\qquad
\varepsilon^{pl}=0.020-0.002=0.018
$$

이다. 응력과 영률의 단위는 모두 MPa로 통일하였다.

변형경화식은 보통 유동응력과 누적된 소성변형률의 관계를 나타낸다. 다축응력 상태에서는
이를 동등응력 $\bar\sigma$와 동등소성변형률 $\bar\varepsilon^{pl}$의 관계로 확장한다.

# 5. Hollomon 경화법칙

금속의 균일 소성변형 구간을 나타내는 간단한 경험식으로 Hollomon 법칙을 자주 사용한다.

$$
\boxed{\sigma=K(\varepsilon^{pl})^n}
$$

- $\sigma$: 유동응력
- $\varepsilon^{pl}$: 소성변형률
- $K$: 강도계수(strength coefficient)
- $n$: 변형경화지수(strain-hardening exponent)

예를 들어 $K=600$ MPa, $n=0.20$인 재료가
$\varepsilon^{pl}=0.10$까지 변형되었다면

$$
\sigma
=600(0.10)^{0.20}
\approx379\ \mathrm{MPa}
$$

이다.

Hollomon 식의 양변에 자연로그를 취하면

$$
\ln\sigma=\ln K+n\ln\varepsilon^{pl}
$$

이 된다. 따라서 $\ln\varepsilon^{pl}$을 $x$축, $\ln\sigma$를 $y$축으로 그렸을 때
직선의 기울기가 $n$이고 절편이 $\ln K$이다.

Hollomon 식은 간단하지만 $\varepsilon^{pl}=0$에서 유동응력이 0이 된다는 한계가 있다.
그러므로 초기 항복 부근보다 충분한 소성변형이 진행된 구간을 근사하는 데 더 적합하다.

# 6. 경화지수의 의미

Hollomon 식을 소성변형률로 미분하면

$$
\frac{d\sigma}{d\varepsilon^{pl}}
=Kn(\varepsilon^{pl})^{n-1}
$$

이다. 이 기울기가 양수이면 소성변형이 증가할수록 유동응력이 증가한다.

같은 $K$와 소성변형률에서 $n$이 큰 재료는 대체로 더 강한 변형경화를 보인다. 또한
인장시험에서 변형경화 능력이 크면 국부적인 단면 감소에 저항하여 균일변형을 더 오래
유지할 수 있다.

다만 $K$와 $n$은 독립적인 재료상수이므로 $n$만 보고 두 재료의 모든 응력 수준을
비교해서는 안 된다. 실제 곡선은 $K$와 $n$을 함께 사용해 비교해야 한다.

# 7. 소성일과 변형경화

앞선 소성일 강의에서 단위 부피당 소성일 증분을

$$
dW^{pl}=\sigma\,d\varepsilon^{pl}
$$

로 정의하였다. 따라서 소성변형률이 0에서 $\varepsilon^{pl}$까지 증가할 때 누적 소성일은
유동응력–소성변형률 곡선 아래의 면적이다.

$$
W^{pl}=\int_0^{\varepsilon^{pl}}\sigma\,d\varepsilon^{pl}
$$

Hollomon 식을 대입하면

$$
W^{pl}
=\int_0^{\varepsilon^{pl}}K(\varepsilon^{pl})^n\,d\varepsilon^{pl}
=\frac{K}{n+1}(\varepsilon^{pl})^{n+1}
$$

이다. 예를 들어 $K=600$ MPa, $n=0.20$이고 최종 소성변형률이 0.10이면

$$
W^{pl}\approx31.5\ \mathrm{MPa}=31.5\ \mathrm{MJ/m^3}
$$

이다. 응력–변형률 곡선 아래 면적은 단위 부피당 에너지이며,
$1\ \mathrm{MPa}=1\ \mathrm{MJ/m^3}$이다.

# 8. 다른 경화식과 모델의 한계

초기 항복응력을 자연스럽게 포함하려면 Swift 식을 사용할 수 있다.

$$
\sigma=K(\varepsilon_0+\varepsilon^{pl})^n
$$

여기서 $\varepsilon_0$는 초기 소성변형률 오프셋이다. 매우 큰 변형에서 유동응력이 일정한
값에 가까워지는 재료에는 Voce 식을 사용할 수 있다.

$$
\sigma=\sigma_s-(\sigma_s-\sigma_0)
\exp(-b\varepsilon^{pl})
$$

- $\sigma_0$: 초기 유동응력
- $\sigma_s$: 포화 유동응력
- $b$: 포화에 접근하는 속도를 조절하는 상수

이 시간에는 세 식을 모두 외우기보다 다음 차이에 주목한다.

| 경화식 | 특징 |
|---|---|
| Hollomon | 간단한 거듭제곱식, 초기 항복 표현에 한계 |
| Swift | 초기 소성변형률 오프셋을 포함 |
| Voce | 큰 변형에서 유동응력이 포화값에 접근 |

또한 이 식들은 현재까지 누적된 소성변형의 크기로 유동응력을 나타내는 등방경화(isotropic
hardening)의 기초 형태다. 하중 방향이 바뀔 때 나타나는 Bauschinger 효과를 설명하려면
이동경화(kinematic hardening)와 같은 추가 개념이 필요하다.

# 9. 소성가공에서 변형경화가 중요한 이유

변형경화는 소성가공 중 필요한 하중과 가공 후 성질을 함께 변화시킨다.

- 압연, 인발, 단조가 진행될수록 유동응력이 증가하여 더 큰 가공하중이 필요할 수 있다.
- 냉간가공 후 제품의 강도와 경도는 증가하지만 남은 연성은 감소할 수 있다.
- 변형경화 능력은 인장 중 변형이 한 위치에 집중되는 것을 늦출 수 있다.
- 중간 소둔(intermediate annealing)은 경화된 재료의 연성을 회복시켜 추가 가공을
  가능하게 한다.
- 공정해석에서는 유동응력 곡선이 하중, 에너지와 변형 분포의 예측에 직접 사용된다.

즉, 변형경화는 단순히 “재료가 강해지는 현상”이 아니라 **공정에 필요한 힘과 최종
제품의 성질을 연결하는 핵심 재료거동**이다.

# 10. Python 실습

## 10.1. 소성변형률에 따른 유동응력

$K=600$ MPa이고 $n=0.10$, $0.20$, $0.30$인 세 경우를 비교해 보자.

~~~python
import numpy as np
import matplotlib.pyplot as plt


plastic_strain = np.linspace(0.001, 0.30, 200)
strength_coefficient = 600.0  # MPa
hardening_exponents = [0.10, 0.20, 0.30]

fig, ax = plt.subplots(figsize=(6, 4))

for exponent in hardening_exponents:
    flow_stress = strength_coefficient * plastic_strain**exponent
    ax.plot(
        plastic_strain,
        flow_stress,
        label=f"n = {exponent:.2f}",
    )

ax.set_xlabel("Plastic strain")
ax.set_ylabel("Flow stress (MPa)")
ax.set_title("Hollomon Hardening Law")
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
plt.show()
~~~

그래프를 보면 $n$에 따라 곡선의 모양이 달라진다. 다만 모든 곡선에 같은 $K$를
사용했기 때문에 작은 변형률 구간의 응력 순서는 단순히 “$n$이 클수록 크다”가 아니다.
이 점이 $K$와 $n$을 함께 비교해야 하는 이유다.

## 10.2. 실험값으로 $K$와 $n$ 구하기

다음은 소성변형 구간에서 얻었다고 가정한 진응력–진소성변형률 데이터다. 로그를 취하고
<code>np.polyfit()</code>으로 직선을 맞추면 $n$과 $K$를 구할 수 있다.

~~~python
plastic_strain_data = np.array([0.02, 0.04, 0.08, 0.12, 0.18])
true_stress_data = np.array([280, 322, 370, 402, 435])  # MPa

log_strain = np.log(plastic_strain_data)
log_stress = np.log(true_stress_data)

hardening_exponent, log_strength_coefficient = np.polyfit(
    log_strain,
    log_stress,
    1,
)
strength_coefficient = np.exp(log_strength_coefficient)

print(f"n = {hardening_exponent:.3f}")
print(f"K = {strength_coefficient:.1f} MPa")
~~~

구한 상수로 예측 곡선을 그리고 실험값과 비교하자.

~~~python
strain_for_curve = np.linspace(0.01, 0.20, 200)
predicted_stress = (
    strength_coefficient * strain_for_curve**hardening_exponent
)

fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(
    plastic_strain_data,
    true_stress_data,
    color="black",
    label="Experimental data",
)
ax.plot(
    strain_for_curve,
    predicted_stress,
    color="tab:red",
    label="Hollomon fit",
)
ax.set_xlabel("Plastic strain")
ax.set_ylabel("True stress (MPa)")
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
plt.show()
~~~

모델이 모든 측정점을 정확히 지나지 않아도 전체적인 변형경화 경향을 잘 나타내는지
확인해야 한다. 적용할 변형률 범위 밖으로 지나치게 외삽하지 않도록 주의한다.

# 11. 핵심 정리

- 변형경화는 소성변형이 누적될수록 유동응력이 증가하는 현상이다.
- 유동응력 곡선에는 공칭값보다 진응력과 진소성변형률을 사용한다.
- Hollomon 법칙은 $\sigma=K(\varepsilon^{pl})^n$이다.
- $K$는 응력의 크기, $n$은 곡선의 경화 특성을 결정하며 둘을 함께 보아야 한다.
- 유동응력–소성변형률 곡선 아래의 면적은 단위 부피당 소성일이다.
- 변형경화는 가공하중, 성형성, 가공 후 강도와 연성에 영향을 준다.

# 12. 연습 문제

## 문제 1

변형경화를 한 문장으로 설명하시오.

<!--
풀이와 해답:
소성변형이 누적됨에 따라 금속의 유동응력이 증가하는 현상이다.
-->

## 문제 2

공칭변형률이 0.20일 때 진변형률을 계산하시오.

<!--
풀이와 해답:
진변형률은 ln(1 + 0.20) = ln(1.20)이며 약 0.182이다.
-->

## 문제 3

$E=200$ GPa, $\sigma=300$ MPa, 전체 진변형률이 0.010일 때 소성변형률을 구하시오.

<!--
풀이와 해답:
E = 200000 MPa이므로 탄성변형률은 300 / 200000 = 0.0015이다.
따라서 소성변형률은 0.010 - 0.0015 = 0.0085이다.
-->

## 문제 4

Hollomon 식에서 $K$와 $n$의 이름을 각각 쓰시오.

<!--
풀이와 해답:
K는 강도계수이고 n은 변형경화지수이다.
-->

## 문제 5

$K=500$ MPa, $n=0.20$, $\varepsilon^{pl}=0.10$일 때 유동응력을 계산하시오.

<!--
풀이와 해답:
sigma = 500(0.10)^0.20이며 약 315.5 MPa이다.
-->

## 문제 6

냉간가공으로 변형경화된 금속의 강도, 경도와 연성은 일반적으로 어떻게 변하는가?

<!--
풀이와 해답:
강도와 경도는 증가하고 연성은 감소한다.
-->

## 문제 7

Hollomon 식을 로그 형태의 직선식으로 바꾸고, 직선의 기울기가 무엇인지 쓰시오.

<!--
풀이와 해답:
ln(sigma) = ln(K) + n ln(epsilon_pl)이다. 직선의 기울기는 n이다.
-->
