---
layout: distill
title: 함수 활용과 클래스 기초
description: 재료공학 계산 함수와 간단한 클래스 작성
target: 1학년 2학기
permalink:
featured: true
prerequisite: 함수 기초
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
- [2. 함수를 안전하게 작성하기](#2-함수를-안전하게-작성하기)
  - [2.1. 의미 있는 변수 이름과 단위](#21-의미-있는-변수-이름과-단위)
  - [2.2. 허용되지 않는 입력 검사](#22-허용되지-않는-입력-검사)
- [3. 재료공학 계산 함수](#3-재료공학-계산-함수)
  - [3.1. Hooke 법칙](#31-hooke-법칙)
  - [3.2. 전위 밀도와 항복강도](#32-전위-밀도와-항복강도)
  - [3.2. 공칭변형률과 진변형률](#32-공칭변형률과-진변형률)
  - [3.3. Schmid 법칙](#33-schmid-법칙)
- [4. 클래스가 필요한 이유](#4-클래스가-필요한-이유)
- [5. 클래스의 기본 구조](#5-클래스의-기본-구조)
- [6. Alloy 클래스 만들기](#6-alloy-클래스-만들기)
- [7. 여러 객체 다루기](#7-여러-객체-다루기)
- [8. 함수와 클래스의 선택](#8-함수와-클래스의-선택)
- [9. 연습 문제](#9-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 함수에 설명과 입력값 검사를 추가할 수 있다.
- 응력, 변형률과 Schmid 법칙을 함수로 계산할 수 있다.
- 클래스, 객체, 속성과 메서드의 차이를 설명할 수 있다.
- 간단한 재료 데이터 클래스를 만들 수 있다.
- 함수와 클래스를 언제 사용할지 구분할 수 있다.

# 2. 함수를 안전하게 작성하기

## 2.1. 의미 있는 변수 이름과 단위

다음 함수는 계산은 가능하지만 변수의 뜻을 알기 어렵다.

~~~python
def f(a, b):
    return a / b
~~~

변수 이름과 docstring에 물리량과 단위를 나타내면 함수의 의도가 분명해진다.

~~~python
def calculate_density(mass_g, volume_cm3):
    """Calculate density in g/cm^3 from mass and volume."""
    return mass_g / volume_cm3
~~~

```docstring```은 아래와 같이 호출하여 함수의 설명을 확인할 수 있다.
~~~python
# 직접 docstring을 출력하거나
print(calculate_density.__doc__)
# 혹은 help 함수 활용
help(calculate_density)
~~~

## 2.2. 허용되지 않는 입력 검사

부피가 0 이하이면 밀도를 계산할 수 없다. <code>raise</code>를 사용하여 잘못된
입력을 바로 알릴 수 있다.

~~~python
def calculate_density(mass_g, volume_cm3):
    """Calculate density in g/cm^3 from mass and volume."""
    if volume_cm3 <= 0:
        raise ValueError("volume_cm3 must be positive")

    return mass_g / volume_cm3
~~~

처음에는 모든 예외를 처리하려고 하기보다, 계산을 불가능하게 만드는 중요한 입력부터
검사하면 된다.

# 3. 재료공학 계산 함수

## 3.1. Hooke 법칙

일축 선형탄성에서 응력($\sigma$)과 변형률($\varepsilon$)은

$$
\sigma=E\varepsilon
$$

의 관계를 갖는다.

~~~python
def elastic_stress(modulus_gpa, strain):
    """Return stress in GPa."""
    return modulus_gpa * strain


stress_gpa = elastic_stress(200.0, 0.001)
print(stress_gpa)
~~~

입력한 탄성계수가 GPa이므로 결과도 GPa이다. 결과는 0.2 GPa, 즉 200 MPa이다.

## 3.2. 전위 밀도와 항복강도

전위 밀도($\rho$)와 항복강도($\sigma_y$)는 다음 관계를 갖는다.

$$
\sigma=\alpha G b \sqrt{\rho}
$$

$G$: 전단계수, $b$: 버거스 벡터 크기, $\alpha$: 상수

아래 재료의 항복 강도를 계산하는 함수를 작성하면 다음과 같다.

~~~python
def yield_stress(alpha, shear_modulus_gpa, burgers_vector_nm, dislocation_density_per_m2):
    """Return yield stress in GPa."""
    return (
        alpha
        * shear_modulus_gpa
        * burgers_vector_nm
        * (dislocation_density_per_m2 ** 0.5)
    )
~~~

- 아래 세 재료의 경우에 해당하는 항복 강도를 구하시오.

| 재료 | $\alpha$ | $G$ (GPa) | $b$ (nm) | $\rho$ ($\mathrm{m^{-2}}$) |
|------|----------|------------|----------|-----------------------------|
| Al   | 0.5      | 26         | 0.286    | $1\times10^{12}$           |
| Fe   | 0.5      | 80         | 0.248    | $1\times10^{12}$           |
| Cu   | 0.5      | 48         | 0.256    | $1\times10^{12}$           |


## 3.2. 공칭변형률과 진변형률

초기 길이 $l_0$와 현재 길이 $l$로부터 공칭변형률을 계산하면

$$
e=\frac{l-l_0}{l_0}
$$

이다. 균일한 일축변형에서 진변형률은

$$
\varepsilon=\ln(1+e)=\ln\left(\frac{l}{l_0}\right)
$$

이다.

~~~python
import math


def engineering_strain(initial_length, final_length):
    if initial_length <= 0:
        raise ValueError("initial_length must be positive")

    return (final_length - initial_length) / initial_length


def true_strain(initial_length, final_length):
    if initial_length <= 0 or final_length <= 0:
        raise ValueError("lengths must be positive")

    return math.log(final_length / initial_length)


print(engineering_strain(50.0, 55.0))
print(true_strain(50.0, 55.0))
~~~

## 3.3. Schmid 법칙

일축응력($\sigma$)가 작용할 때 분해전단응력($\tau$)은

$$
\tau=\sigma\cos\phi\cos\lambda
$$

이다. 응력 방향과 결정면 법선 방향의 사잇각을 $\phi$, 응력 방향과 전위 슬립 방향의 사잇각을
$\lambda$로 나타내고, 각도 단위를 명확히 하기 위해 함수 이름에 degree를 나타낸다. (각은
degree 혹은 radian 단위로 나타낼 수 있다.)

~~~python
import math

def resolved_shear_stress(stress_mpa, phi_deg, lambda_deg):
    phi_rad = math.radians(phi_deg)
    lambda_rad = math.radians(lambda_deg)

    return (
        stress_mpa
        * math.cos(phi_rad)
        * math.cos(lambda_rad)
    )


tau = resolved_shear_stress(100.0, 45.0, 45.0)
print(tau)
~~~

결과는 약 50 MPa이다.

# 4. 클래스가 필요한 이유

함수는 하나의 작업을 묶는 데 적합하다. 재료의 이름, 밀도, 탄성계수처럼 서로 관련된
여러 데이터와 그 데이터를 사용하는 동작을 함께 묶으려면 클래스(class)가 편리하다.

클래스는 객체를 만들기 위한 설계도이고, 클래스로 만든 각각의 실체를 객체(object) 또는
인스턴스(instance)라고 한다.

예를 들어 Al과 Fe 객체는 같은 Material 클래스로 만들 수 있지만 서로 다른 밀도와
결정구조를 가질 수 있다. 따라서 Al과 Fe에 해당하는 각자 다른 인스턴스를 만들 수 있다.
각 인스턴스는 서로 다른 속성(attribute) 값을 갖는다.

# 5. 클래스의 기본 구조

~~~python
class Material:
    def __init__(self, name, density):
        self.name = name
        self.density = density

    def describe(self):
        return f"{self.name}: {self.density} g/cm^3"


aluminum = Material("Aluminum", 2.70)
print(aluminum.name)
print(aluminum.describe())
~~~

각 부분의 의미는 다음과 같다.

- <code>Material</code>: 클래스 이름
- <code>__init__</code>: 객체를 만들 때 실행되는 초기화 메서드
- <code>self</code>: 현재 객체 자신
- <code>self.name</code>, <code>self.density</code>: 객체의 속성(attribute)
- <code>describe</code>: 객체가 수행할 수 있는 메서드(method)
- <code>aluminum</code>: Material 클래스의 객체

메서드를 정의할 때 첫 번째 매개변수로 <code>self</code>를 적어야 한다.

# 6. Alloy 클래스 만들기

~~~python
class Alloy:
    def __init__(
        self,
        name,
        tensile_strength_mpa,
        density_g_cm3,
    ):
        self.name = name
        self.tensile_strength_mpa = tensile_strength_mpa
        self.density_g_cm3 = density_g_cm3

    def specific_strength(self):
        return (
            self.tensile_strength_mpa
            / self.density_g_cm3
        )

    def describe(self):
        return (
            f"{self.name}: "
            f"strength={self.tensile_strength_mpa} MPa, "
            f"density={self.density_g_cm3} g/cm^3"
        )


alloy = Alloy("Ti-6Al-4V", 900.0, 4.4)

print(alloy.describe())
print(alloy.specific_strength())
~~~

비강도(specific strength)는 여기서 인장강도를 밀도로 나눈 비교용 값이다. 서로 같은
단위를 사용한 재료끼리 비교해야 한다.

# 7. 여러 객체 다루기

같은 클래스로 만든 객체를 리스트에 저장하면 반복문으로 비교할 수 있다.

~~~python
alloys = [
    Alloy("Ni-Cu", 450.0, 8.9),
    Alloy("Al-Mg", 320.0, 2.7),
    Alloy("Ti-6Al-4V", 900.0, 4.4),
]

for alloy in alloys:
    print(
        alloy.name,
        alloy.specific_strength(),
    )
~~~

비강도가 가장 큰 객체는 다음과 같이 찾을 수 있다.

~~~python
best = max(
    alloys,
    key=lambda alloy: alloy.specific_strength(),
)

print(best.name)
~~~

<code>getattr</code>를 사용하면 속성 이름을 문자열로 지정할 수도 있다.

~~~python
property_name = "tensile_strength_mpa"

for alloy in alloys:
    value = getattr(alloy, property_name)
    print(alloy.name, value)
~~~

초급 단계에서는 <code>alloy.tensile_strength_mpa</code>처럼 속성을 직접 쓰는 것이
더 읽기 쉽다. 속성 이름을 실행 중에 선택해야 할 때 <code>getattr</code>가 유용하다.

# 8. 함수와 클래스의 선택

- 입력값으로 한 번 계산하여 결과를 반환하면 함수가 적합하다.
- 서로 관련된 여러 데이터만 저장한다면 딕셔너리도 사용할 수 있다.
- 데이터와 그 데이터를 사용하는 여러 동작을 함께 묶으면 클래스가 적합하다.
- 간단한 문제를 억지로 클래스로 만들 필요는 없다.

예를 들어 밀도 하나를 계산하는 작업은 함수로 충분하다. 여러 합금의 이름, 밀도,
강도와 비교 동작을 함께 관리한다면 클래스가 편리하다.

# 9. 연습 문제

## 문제 1

Young 계수가 70 GPa이고 탄성변형률이 0.002일 때
<code>elastic_stress</code> 함수가 반환하는 응력을 구하라.

<!--
풀이와 해답:
70 곱하기 0.002는 0.14이므로 0.14 GPa, 즉 140 MPa이다.
-->

## 문제 2

초기 길이가 100 mm이고 현재 길이가 102 mm일 때 공칭변형률을 구하라.

<!--
풀이와 해답:
(102-100)/100=0.02이다.
-->

## 문제 3

클래스와 객체의 관계를 한 문장으로 설명하라.

<!--
풀이와 해답:
클래스는 객체를 만들기 위한 설계도이고 객체는 그 클래스로 만든 실제 인스턴스이다.
-->

## 문제 4

다음 코드에서 클래스, 객체와 속성을 각각 하나씩 쓰시오.

~~~python
iron = Material("Iron", 7.87)
~~~

<!--
풀이와 해답:
클래스는 Material, 객체는 iron이며 속성의 예로 name 또는 density를 쓸 수 있다.
-->

## 문제 5

<code>Material</code> 객체 <code>iron</code>의 밀도를 읽는 표현을 쓰시오.

<!--
풀이와 해답:
iron.density
-->

## 문제 6

메서드를 정의할 때 첫 번째 매개변수로 일반적으로 사용하는 이름은 무엇인가?

<!--
풀이와 해답:
self이다.
-->
