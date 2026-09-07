---
layout: distill
title: 네킹과 소성불안정
description: 인장시험의 최대하중과 Considère 조건
target: 3학년 1학기
permalink:
featured: true
prerequisite: 응력과 변형률, 변형경화
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
- [2. 네킹이란 무엇인가?](#2-네킹이란-무엇인가)
- [3. 인장시험 곡선과 네킹](#3-인장시험-곡선과-네킹)
- [4. 변형경화와 단면 감소의 경쟁](#4-변형경화와-단면-감소의-경쟁)
- [5. Considere 조건의 유도](#5-considere-조건의-유도)
- [6. Hollomon 법칙과 균일진변형률](#6-hollomon-법칙과-균일진변형률)
- [7. 공칭변형률과 균일연신율](#7-공칭변형률과-균일연신율)
- [8. 네킹 이후에는 무엇이 달라지는가?](#8-네킹-이후에는-무엇이-달라지는가)
- [9. 소성가공에서 네킹이 중요한 이유](#9-소성가공에서-네킹이-중요한-이유)
- [10. Python 실습](#10-python-실습)
  - [10.1. 유동응력, 단면적과 하중 계산](#101-유동응력-단면적과-하중-계산)
  - [10.2. 진응력과 하중을 함께 그리기](#102-진응력과-하중을-함께-그리기)
  - [10.3. 경화지수와 균일연신율 비교](#103-경화지수와-균일연신율-비교)
- [11. 핵심 정리](#11-핵심-정리)
- [12. 쉬운 연습 문제](#12-쉬운-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)
  - [문제 7](#문제-7)

# 1. 학습 목표와 수업 구성

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 균일변형과 네킹(necking)을 구분할 수 있다.
- 공칭응력 곡선의 최대점과 네킹 시작의 관계를 설명할 수 있다.
- 변형경화와 단면 감소가 인장하중에 미치는 영향을 설명할 수 있다.
- Considere 조건을 유도하고 물리적 의미를 설명할 수 있다.
- Hollomon 법칙으로부터 네킹 시작 변형률을 구할 수 있다.
- 네킹 이후 단순한 진응력 변환식을 사용할 때의 한계를 설명할 수 있다.

# 2. 네킹이란 무엇인가?

인장시험편이 항복한 뒤에도 처음에는 표점부 전체가 비교적 고르게 늘어난다. 이를
**균일변형(uniform deformation)**이라 한다. 변형이 더 진행되면 어느 한 부분의 단면이
주변보다 빠르게 감소하기 시작한다. 이와 같이 변형이 좁은 영역에 집중되는 현상을
**네킹(necking)**이라 한다.

> 네킹은 인장변형이 시편 전체에 균일하게 분포하지 않고 특정 위치에 집중되는
> 소성불안정(plastic instability) 현상이다.

네킹이 시작된 뒤에는 목 부분의 단면적이 빠르게 감소하고, 대부분의 추가 변형이 이
영역에 집중된다. 결국 목 부분에서 파단(fracture)이 발생한다.

네킹과 파단은 같은 사건이 아니다.

- **네킹 시작**: 변형이 한 위치에 집중되기 시작한다.
- **파단**: 재료가 실제로 분리된다.

따라서 네킹이 시작된 뒤에도 어느 정도의 추가 변형이 일어난 다음 파단될 수 있다.

# 3. 인장시험 곡선과 네킹

공칭응력 $s$는 하중 $F$를 초기 단면적 $A_0$로 나눈 값이다.

$$
s=\frac{F}{A_0}
$$

$A_0$는 시험 중 변하지 않는 상수이므로 공칭응력이 최대가 되는 지점은 하중이 최대가
되는 지점과 같다.

$$
s_{\max}=\frac{F_{\max}}{A_0}
$$

일반적인 인장시험에서 균일 네킹(diffuse necking)은 최대하중 부근에서 시작된다.
이때의 공칭응력을 인장강도(ultimate tensile strength, UTS)라고 한다.

공칭응력은 최대점 이후 감소하지만, 이것이 재료 자체의 유동응력이 반드시 감소했다는
뜻은 아니다. 실제 단면적이 급격히 감소하여 시험편이 지탱하는 전체 하중이 줄었기
때문일 수 있다.

진응력은 현재 단면적 $A$를 사용한다.

$$
\sigma=\frac{F}{A}
$$

따라서 네킹을 이해하려면 **재료의 강도 증가**와 **현재 단면적 감소**를 함께 살펴봐야
한다.

# 4. 변형경화와 단면 감소의 경쟁

인장 중 하중은 다음과 같다.

$$
F=\sigma A
$$

소성변형이 증가하면 두 가지 변화가 동시에 일어난다.

1. 변형경화 때문에 유동응력 $\sigma$가 증가한다.
2. 시편이 길어지면서 단면적 $A$가 감소한다.

변형경화 효과가 단면 감소 효과보다 크면 하중은 계속 증가하며 변형이 비교적 균일하게
유지된다. 반대로 단면 감소의 영향이 더 커지면 한 부분의 단면 감소가 스스로 가속된다.

예를 들어 어떤 위치가 주변보다 조금 가늘어졌다고 생각하자. 같은 하중에서 이 위치의
진응력은 더 커지고, 따라서 소성변형이 더 많이 발생한다. 그러면 단면이 더 작아지고
응력이 다시 증가한다. 변형경화가 이 과정을 충분히 억제하지 못하면 네킹이 성장한다.

# 5. Considere 조건의 유도

네킹 시작을 최대하중 조건으로 생각하자. 진변형률을 $\varepsilon$이라 하면 최대하중에서

$$
\frac{dF}{d\varepsilon}=0
$$

이다. 하중 $F=\sigma A$를 미분하면

$$
\frac{dF}{d\varepsilon}
=A\frac{d\sigma}{d\varepsilon}
+\sigma\frac{dA}{d\varepsilon}
$$

이다.

균일한 일축 소성변형 중 체적이 일정하다고 가정하자.

$$
AL=A_0L_0
$$

진변형률의 정의 $\varepsilon=\ln(L/L_0)$를 사용하면

$$
L=L_0e^\varepsilon,
\qquad
A=A_0e^{-\varepsilon}
$$

를 얻는다. 따라서

$$
\frac{dA}{d\varepsilon}=-A
$$

이다. 이를 하중의 미분식에 대입하면

$$
\frac{dF}{d\varepsilon}
=A\left(\frac{d\sigma}{d\varepsilon}-\sigma\right)
$$

이다. 최대하중에서 $dF/d\varepsilon=0$이고 $A\neq0$이므로

$$
\boxed{\frac{d\sigma}{d\varepsilon}=\sigma}
$$

를 얻는다. 이것이 일축인장에서의 **Considère 조건**이다.

- $d\sigma/d\varepsilon>\sigma$: 경화가 단면 감소를 충분히 보상하므로 하중이 증가한다.
- $d\sigma/d\varepsilon=\sigma$: 최대하중에 도달하며 네킹이 시작된다.
- $d\sigma/d\varepsilon<\sigma$: 단면 감소의 영향이 더 커져 하중이 감소한다.

이 유도에서는 탄성변형을 무시하고 진변형률을 소성변형률로 근사한다. 탄성변형까지
정확히 포함하면 식을 더 세심하게 다뤄야 하지만, 금속의 충분한 소성변형 구간에서는 이
근사가 유용하다.

# 6. Hollomon 법칙과 균일진변형률

앞선 변형경화 강의에서 Hollomon 법칙을 다음과 같이 정의하였다.

$$
\sigma=K(\varepsilon^{pl})^n
$$

탄성변형을 무시하여 $\varepsilon\approx\varepsilon^{pl}$로 두면

$$
\sigma=K\varepsilon^n
$$

이다. 이를 미분하면

$$
\frac{d\sigma}{d\varepsilon}
=Kn\varepsilon^{n-1}
$$

이고, Considère 조건을 적용하면

$$
Kn\varepsilon^{n-1}=K\varepsilon^n
$$

이다. $K\varepsilon^{n-1}$을 소거하면

$$
\boxed{\varepsilon_{neck}=n}
$$

을 얻는다. 즉, 이상적인 Hollomon 재료에서는 네킹이 시작될 때의 균일진변형률이
변형경화지수 $n$과 같다.

예를 들어 $n=0.20$이면

$$
\varepsilon_{neck}\approx0.20
$$

이다. 이는 변형경화 능력이 큰 재료가 일반적으로 네킹을 더 늦게 시작한다는 뜻이다.
다만 이 관계는 Hollomon 법칙, 균일한 일축변형, 체적 일정과 탄성변형 무시라는 가정
아래에서 성립한다.

# 7. 공칭변형률과 균일연신율

진변형률과 공칭변형률의 관계는

$$
\varepsilon=\ln(1+e)
$$

이다. 따라서 네킹 시작 진변형률이 $n$이면 공칭 균일변형률은

$$
\boxed{e_{uniform}=e^n-1}
$$

이다. 예를 들어 $n=0.20$이면

$$
e_{uniform}=e^{0.20}-1\approx0.221
$$

이므로 이상적인 조건에서 약 22.1%의 균일연신율에 해당한다.

여기서 지수함수의 밑 $e$와 공칭변형률 기호 $e$가 혼동될 수 있다. 식의
$e^n$에서 $e$는 자연상수이고, $e_{uniform}$의 $e$는 공칭변형률을 뜻한다.

# 8. 네킹 이후에는 무엇이 달라지는가?

네킹 이전에는 표점부의 변형이 비교적 균일하므로

$$
\sigma=s(1+e),
\qquad
\varepsilon=\ln(1+e)
$$

를 사용하여 공칭값을 진값으로 변환할 수 있다. 네킹 이후에는 다음 이유로 이 변환의
정확성이 떨어진다.

- 변형이 목 부분에 집중되어 표점부 전체가 균일하지 않다.
- 목 부분의 실제 최소단면적을 측정해야 한다.
- 목 부분에는 단순한 일축응력이 아니라 다축응력 상태가 형성된다.

네킹 이후의 평균 축방향 진응력을 단순히 계산하려면

$$
\sigma_{avg}=\frac{F}{A_{min}}
$$

처럼 현재 최소단면적 $A_{min}$을 사용한다. 그러나 이 값도 목 내부의 응력 삼축성을
완전히 보정한 재료의 일축 유동응력은 아니다. 정밀한 유동곡선 측정에는 단면 형상 측정,
Bridgman 보정 또는 유한요소 역해석 등이 필요할 수 있다.

# 9. 소성가공에서 네킹이 중요한 이유

네킹은 인장시험에만 나타나는 흥미로운 현상이 아니라 판재 성형과 제품 설계에도 직접
연결된다.

- 인장 부품에서는 네킹이 시작되면 단면 감소와 파손 위험이 국부적으로 커진다.
- 판재 성형에서는 변형의 국부화가 균열 발생의 전조가 될 수 있다.
- 변형경화 능력이 크면 변형이 더 넓게 분산되어 균일한 성형에 유리할 수 있다.
- 공정설계에서는 한 부위에 인장변형이 집중되지 않도록 형상, 마찰과 변형 경로를
  조절한다.
- 성형한계도(forming limit diagram)는 판재의 국부 네킹 한계를 평가하는 데 사용된다.

이번 강의의 Considere 조건은 일축인장의 균일 네킹을 설명하는 기초 조건이다. 판재의
다축 변형에서 발생하는 국부 네킹은 응력상태와 변형경로를 함께 고려해야 한다.

# 10. Python 실습

## 10.1. 유동응력, 단면적과 하중 계산

Hollomon 재료에 대해 진변형률이 증가할 때 유동응력, 단면적과 하중이 어떻게 변하는지
계산해 보자. 초기 단면적은 $100\ \mathrm{mm^2}$, $K=600$ MPa, $n=0.20$으로 둔다.

~~~python
import numpy as np
import matplotlib.pyplot as plt


true_strain = np.linspace(0.001, 0.60, 500)
strength_coefficient = 600.0  # MPa
hardening_exponent = 0.20
initial_area = 100.0          # mm^2

true_stress = strength_coefficient * true_strain**hardening_exponent
current_area = initial_area * np.exp(-true_strain)
load = true_stress * current_area  # N because MPa = N/mm^2

necking_strain = hardening_exponent
necking_index = np.argmax(load)

print(f"Calculated maximum-load strain: {true_strain[necking_index]:.3f}")
print(f"Considere prediction: {necking_strain:.3f}")
~~~

수치적으로 계산한 최대하중 변형률이 $n=0.20$과 가까운지 확인한다.

## 10.2. 진응력과 하중을 함께 그리기

유동응력은 계속 증가하지만 하중은 최대점 이후 감소할 수 있다. 두 값을 별도의 Axes에
그려 비교하자.

~~~python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(true_strain, true_stress, color="tab:blue")
axes[0].axvline(necking_strain, color="black", linestyle="--")
axes[0].set_xlabel("True strain")
axes[0].set_ylabel("True stress (MPa)")
axes[0].set_title("Flow Stress")
axes[0].grid(True, alpha=0.3)

axes[1].plot(true_strain, load / 1000.0, color="tab:red")
axes[1].axvline(necking_strain, color="black", linestyle="--", label="Necking")
axes[1].set_xlabel("True strain")
axes[1].set_ylabel("Load (kN)")
axes[1].set_title("Tensile Load")
axes[1].grid(True, alpha=0.3)
axes[1].legend()

fig.tight_layout()
plt.show()
~~~

왼쪽 그림에서는 변형경화 때문에 진응력이 계속 증가한다. 오른쪽 그림에서는 진변형률이
약 0.20일 때 하중이 최대가 되고 이후 감소한다. 이것이 “공칭응력이 감소하므로 재료가
즉시 약해졌다”라고 해석하면 안 되는 이유다.

## 10.3. 경화지수와 균일연신율 비교

~~~python
hardening_exponents = np.array([0.10, 0.20, 0.30, 0.40])
uniform_true_strain = hardening_exponents
uniform_engineering_strain = np.exp(hardening_exponents) - 1.0

for exponent, elongation in zip(
    hardening_exponents,
    uniform_engineering_strain,
):
    print(f"n = {exponent:.2f}: uniform elongation = {100 * elongation:.1f}%")
~~~

이상적인 Hollomon 재료에서는 $n$이 증가할수록 균일연신율도 증가한다.

# 11. 핵심 정리

- 네킹은 인장변형이 특정 위치에 집중되는 소성불안정 현상이다.
- 일반적인 인장시험에서 균일 네킹은 최대하중 부근에서 시작된다.
- 변형경화는 하중을 증가시키고 단면 감소는 하중을 감소시키는 방향으로 작용한다.
- Considère 조건은 $d\sigma/d\varepsilon=\sigma$이다.
- Hollomon 재료에서는 $\varepsilon_{neck}\approx n$이다.
- 대응하는 공칭 균일변형률은 $e_{uniform}=e^n-1$이다.
- 네킹 이후에는 변형과 응력이 불균일하므로 단순한 공칭–진 변환에 주의해야 한다.

# 12. 쉬운 연습 문제

## 문제 1

네킹과 파단의 차이를 간단히 설명하시오.

<!--
풀이와 해답:
네킹은 변형이 특정 위치에 집중되기 시작하는 현상이고, 파단은 재료가 실제로 분리되는
현상이다. 네킹이 시작된 뒤 추가 변형을 거쳐 파단될 수 있다.
-->

## 문제 2

공칭응력이 최대가 되는 지점이 최대하중 지점과 같은 이유를 설명하시오.

<!--
풀이와 해답:
공칭응력 s = F/A0에서 초기 단면적 A0는 일정하므로 F가 최대일 때 s도 최대가 된다.
-->

## 문제 3

Considère 조건을 쓰시오.

<!--
풀이와 해답:
d sigma / d epsilon = sigma이다.
-->

## 문제 4

Hollomon 경화지수가 $n=0.25$인 재료의 네킹 시작 진변형률을 추정하시오.

<!--
풀이와 해답:
Hollomon 재료에서 epsilon_neck = n이므로 약 0.25이다.
-->

## 문제 5

$n=0.25$일 때 공칭 균일변형률과 균일연신율(%)을 계산하시오.

<!--
풀이와 해답:
e_uniform = exp(0.25) - 1 = 약 0.284이다. 따라서 균일연신율은 약 28.4%이다.
-->

## 문제 6

네킹 이전에 하중이 증가하기 위한 조건을 변형경화율 $d\sigma/d\varepsilon$과 진응력
$\sigma$를 사용하여 쓰시오.

<!--
풀이와 해답:
d sigma / d epsilon > sigma일 때 하중이 증가한다.
-->

## 문제 7

네킹 이후에 $\sigma=s(1+e)$를 그대로 적용하기 어려운 이유를 쓰시오.

<!--
풀이와 해답:
네킹 이후에는 변형이 목 부분에 집중되어 표점부의 변형과 단면적이 균일하지 않기
때문이다.
-->
