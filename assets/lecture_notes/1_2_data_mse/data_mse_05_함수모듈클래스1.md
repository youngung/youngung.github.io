---
layout: distill
title: 함수 기초
description: 함수의 정의, 매개변수, 반환값과 재사용
target: 1학년 2학기
permalink:
featured: true
prerequisite: 조건문과 반복문
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
- [2. 함수가 필요한 이유](#2-함수가-필요한-이유)
- [3. 함수의 기본 구조](#3-함수의-기본-구조)
- [4. 매개변수와 인자](#4-매개변수와-인자)
- [5. return과 print의 차이](#5-return과-print의-차이)
- [6. 기본값과 키워드 인자](#6-기본값과-키워드-인자)
- [7. 변수의 범위](#7-변수의-범위)
- [8. 재료공학 예제](#8-재료공학-예제)
  - [8.1. 밀도 계산](#81-밀도-계산)
  - [8.2. 여러 측정값의 평균](#82-여러-측정값의-평균)
  - [8.3. 표준편차](#83-표준편차)
  - [8.4. 온도에 따른 vacancy 농도](#84-온도에-따른-vacancy-농도)
- [9. 여러 입력값 받기](#9-여러-입력값-받기)
- [10. 함수를 작성할 때의 점검 사항](#10-함수를-작성할-때의-점검-사항)
- [11. 연습 문제](#11-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)
- [12. 프로젝트형 연습문제: 이진수 변환기를 함수로 만들기](#12-프로젝트형-연습문제-이진수-변환기를-함수로-만들기)
  - [12.1. 함수의 입력과 반환값](#121-함수의-입력과-반환값)
  - [12.2. 구현 요구사항](#122-구현-요구사항)
  - [12.3. 확인 사례와 제출물](#123-확인-사례와-제출물)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- <code>def</code>를 사용하여 간단한 함수를 정의할 수 있다.
- 매개변수(parameter)와 인자(argument)를 구분할 수 있다.
- <code>return</code>으로 계산 결과를 반환할 수 있다.
- 기본값과 키워드 인자를 사용할 수 있다.
- 반복되는 재료공학 계산을 함수로 만들 수 있다.

# 2. 함수가 필요한 이유

원의 넓이를 여러 번 계산한다고 생각해 보자.

~~~python
radius1 = 2.0
area1 = 3.141592 * radius1**2

radius2 = 3.0
area2 = 3.141592 * radius2**2
~~~

반복되는 계산을 함수로 만들면 계산식을 한 번만 작성해도 된다.

~~~python
def circle_area(radius):
    return 3.141592 * radius**2


area1 = circle_area(2.0)
area2 = circle_area(3.0)

print(area1)
print(area2)
~~~

함수(function)는 특정 작업을 수행하도록 이름을 붙인 코드의 묶음이다. 함수를 사용하면

- 같은 코드를 반복해서 작성하지 않아도 되고,
- 계산식의 의미가 명확해지며,
- 오류를 한 곳에서 수정할 수 있다.

# 3. 함수의 기본 구조

함수는 다음과 같은 형태로 정의한다.

~~~text
def 함수이름(매개변수):
    실행할 문장 1
    실행할 문장 2
    실행할 문장 ...
    return 결과
~~~

두 수를 더하는 함수는 다음과 같다.

~~~python
def add(a, b):
    result = a + b
    return result

value = add(3, 5)
print(value)
~~~

함수 정의에서 중요한 점은 다음과 같다.

- 함수 이름 뒤에 괄호```(```, ```)```와 콜론```:```을 쓴다.
- 함수 본문은 들여쓴다 (indentation).
- 함수는 정의한 뒤 호출(call)해야 실행된다.
- 함수 이름은 수행하는 작업을 알 수 있게 짓는다.

# 4. 매개변수와 인자

다음 함수에서 <code>mass</code>와 <code>volume</code>은 매개변수(parameter)이다.

~~~python
def density(mass, volume):
    return mass / volume
~~~

함수를 호출할 때 전달하는 7.8과 1.0은 인자(argument)이다.

~~~python
rho = density(7.8, 1.0)
print(rho)
~~~

정리하면

- 매개변수: 함수를 정의할 때 입력을 받을 변수
- 인자: 함수를 호출할 때 실제로 전달하는 값

이다.

# 5. return과 print의 차이

<code>print</code>는 값을 화면에 보여준다. <code>return</code>은 값을 함수 밖으로
돌려주어 다른 계산에 사용할 수 있게 한다.

~~~python
def show_double(x):
    print(2 * x)

def calculate_double(x):
    return 2 * x

show_double(4)
value = calculate_double(4)
result = value + 1
print(result)
~~~

계산용 함수에서는 일반적으로 결과를 <code>return</code>한다.


하나의 함수가 여러 값을 반환할 수도 있다.

~~~python
def minimum_maximum(values):
    return min(values), max(values)


smallest, largest = minimum_maximum([3, 7, 2, 5])
print(smallest, largest)
~~~

# 6. 기본값과 키워드 인자

매개변수에 기본값(default value)을 지정할 수 있다.

~~~python
def power(base, exponent=2):
    return base**exponent


print(power(3))
print(power(3, 3))
print(power(base=2, exponent=4))
~~~

기본값이 없는 매개변수는 기본값이 있는 매개변수보다 앞에 놓아야 한다.

~~~python
def valid_function(c, d, a=3, b=5):
    return a * b * c * d
~~~

다음과 같은 정의는 허용되지 않는다.

~~~text
def invalid_function(a=3, b=5, c, d):
    ...
~~~

# 7. 변수의 범위

함수 안에서 만든 변수는 기본적으로 함수 밖에서 직접 사용할 수 없다. 이를 지역변수
(local variable)라고 한다.

~~~python
def engineering_strain(initial_length, final_length):
    length_change = final_length - initial_length
    strain = length_change / initial_length
    return strain


epsilon = engineering_strain(50.0, 51.0)
print(epsilon)
~~~

위 코드에서 <code>length_change</code>와 <code>strain</code>은 함수 안의 지역변수이고,
<code>epsilon</code>은 함수 밖의 변수이다.

함수 안에서 전역변수(global variable)를 변경하는 방식보다 필요한 값을 인자로 전달하고 결과를 반환하는
방식이 이해하기 쉽고 오류도 적다.

# 8. 재료공학 예제

## 8.1. 밀도 계산

밀도는 질량을 부피로 나누어 계산한다.

$$
\rho=\frac{m}{V}
$$

~~~python
def calculate_density(mass_g, volume_cm3):
    """Return density in g/cm^3."""
    return mass_g / volume_cm3


al_density = calculate_density(27.0, 10.0)
print(f"density = {al_density:.2f} g/cm^3")
~~~

단위가 서로 맞는지 확인해야 한다. 변수 이름에 단위를 포함하면 실수를 줄일 수 있다.

## 8.2. 여러 측정값의 평균

~~~python
def mean(values):
    total = 0.0

    for value in values:
        total += value

    return total / len(values)


masses = [6.01, 6.05, 5.93, 6.03]
average_mass = mean(masses)
print(average_mass)
~~~

Python이 제공하는 <code>sum</code>을 사용하면 더 간단히 작성할 수도 있다.

~~~python
def mean(values):
    return sum(values) / len(values)
~~~

## 8.3. 표준편차

$n$개의 값을 모집단으로 보고 표준편차(standard deviation)를 계산하면

$$
s=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar{x})^2}
$$

이다.

~~~python
def population_std(values):
    average = sum(values) / len(values)
    squared_sum = 0.0

    for value in values:
        squared_sum += (value - average)**2

    return (squared_sum / len(values))**0.5


print(population_std(masses))
~~~

## 8.4. 온도에 따른 vacancy 농도

결정 내 vacancy(원자 공공 결함)의 평형 농도(정확히는 전체 격자점 중 vacancy가 차지하는 분율)를
간단한 모델로 계산해 보자. 형성 엔트로피를 무시하면 vacancy 분율은 다음과 같이 쓸 수 있다.

$$
c_v = \exp\left(-\frac{Q_v}{k_B T}\right)
$$

여기서 $Q_v$는 vacancy 형성 에너지 (vacancy formation energy; 단위: eV), $k_B$는 볼츠만 상수
($8.617\times10^{-5}$ eV/K), $T$는 절대온도(K)이다. 온도는 섭씨가 아니라 반드시
켈빈으로 변환해서 식에 넣어야 한다.

~~~python
import math

def vacancy_fraction(formation_energy_ev, temperature_c):
    """Return the equilibrium vacancy fraction for a temperature in Celsius."""
    boltzmann_constant_ev_per_k = 8.617e-5
    temperature_k = temperature_c + 273.15
    return math.exp(-formation_energy_ev /
                    (boltzmann_constant_ev_per_k * temperature_k))

vacancy_formation_energy = 1.0
temperatures_c = [20, 300, 600, 900]

for temperature_c in temperatures_c:
    fraction = vacancy_fraction(vacancy_formation_energy, temperature_c)
    print(f"{temperature_c:>3} degC: c_v = {fraction:.3e}")
~~~

온도가 높아질수록 지수의 음수 크기가 작아지므로 vacancy 분율이 증가한다. 이 예제에서
함수의 매개변수는 형성 에너지와 온도이고, 함수의 반환값은 계산된 vacancy 분율이다.
온도 목록을 바꾸어도 같은 함수를 반복해서 사용할 수 있다. 이 모델은 형성 엔트로피와
상호작용을 무시한 단순한 근사이므로 실제 재료의 정량적인 값보다는 온도에 따른 경향을
이해하는 데 사용한다.

# 9. 여러 입력값 받기

입력값의 개수를 미리 정하기 어렵다면 <code>*args</code>를 사용할 수 있다.
<code>args</code>는 함수 안에서 튜플로 다룬다.

~~~python
def add_all(*args):
    return sum(args)

print(add_all(1, 2))
print(add_all(1, 2, 3, 4))
~~~

키워드와 값을 여러 개 받으려면 <code>**kwargs</code>를 사용할 수 있다.
<code>kwargs</code>는 딕셔너리이다.

~~~python
def print_material(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_material(name="Aluminum", structure="FCC", density=2.70)
~~~

처음 함수를 배울 때는 일반 매개변수를 우선 사용하고, 입력 개수가 달라지는 경우에만
<code>*args</code>나 <code>**kwargs</code>를 사용하는 것이 좋다.

# 10. 함수를 작성할 때의 점검 사항

- 함수 이름이 하는 일을 잘 나타내는가?
- 입력값과 반환값이 분명한가?
- 계산을 수행할 때 사용하는 단위가 일관적인가?
- 같은 계산이 함수 안에서 불필요하게 반복되지 않는가?
- 간단한 입력값으로 결과를 직접 확인했는가?
- 0으로 나누는 경우(혹은 자연로그 0, 즉 $\ln 0$)처럼 허용되지 않는 입력은 없는가?

# 11. 연습 문제

## 문제 1

두 수를 곱하여 반환하는 함수 <code>multiply</code>를 작성하라.

<!--
풀이와 해답:
def multiply(a, b):
    return a * b
-->

## 문제 2

다음 코드의 출력값을 구하라.

~~~python
def subtract(a, b):
    return a - b

print(subtract(7, 2))
~~~

<!--
풀이와 해답:
5가 출력된다.
-->

## 문제 3

다음 함수에서 매개변수와 인자(argument)를 각각 쓰시오.

~~~python
def square(x):
    return x**2

square(4)
~~~

<!--
풀이와 해답:
매개변수는 x이고 인자는 4이다.
-->

## 문제 4

다음 코드의 두 출력값을 구하라.

~~~python
def power(base, exponent=2):
    return base**exponent

print(power(3))
print(power(3, 3))
~~~

<!--
풀이와 해답:
각각 9와 27이 출력된다.
-->

## 문제 5

질량이 15 g이고 부피가 5 cm³인 재료의 밀도를
<code>calculate_density</code> 함수로 계산하라.

<!--
풀이와 해답:
calculate_density(15, 5)의 결과는 3 g/cm^3이다.
-->

## 문제 6

함수에서 <code>return</code>이 필요한 이유를 한 문장으로 설명하라.

<!--
풀이와 해답:
계산 결과를 함수 밖으로 돌려주어 변수에 저장하거나 다음 계산에 사용할 수 있게 하기 위해서이다.
-->

# 12. 프로젝트형 연습문제: 이진수 변환기를 함수로 만들기

[4장 조건문과 반복문]({% link assets/lecture_notes/1_2_data_mse/data_mse_04_조건문과_반복문.md %})의
‘프로젝트 1. 10진수 → 2진수 변환기’를 함수로 바꾸시오.
앞 프로젝트에서는 변수에 저장된 값을 변환하고 바로 출력했다. 이번에는 입력을 **인자**로 받고,
변환 결과를 **반환값**으로 돌려주어 여러 곳에서 재사용할 수 있게 만든다.

## 12.1. 함수의 입력과 반환값

함수 이름은 `decimal_to_binary`로 정한다. 입력 `number`는 정수라고 가정한다.

| 입력 | 반환값 |
| --- | --- |
| 양의 정수 | 해당 수의 2진수 문자열 |
| 0 | 문자열 `'0'` |
| 음의 정수 | `None`: 이 프로젝트에서 지원하지 않는 입력 |

숫자 0과 문자열 `'0'`은 서로 다른 자료형이다. 정상적인 변환 결과는 항상 **문자열**로 반환한다.
함수 안에서는 결과를 출력하지 않고, 호출한 곳에서 반환값을 확인해 출력한다.

## 12.2. 구현 요구사항

1. 기존 변환 코드를 `def decimal_to_binary(number):` 안으로 옮긴다.
2. `while`, `//`, `%`를 사용한다. `bin()`이나 이진수 형식 지정 기능은 사용하지 않는다.
3. 계산 중 사용할 몫과 결과 문자열은 함수 안의 지역변수로 만든다. 함수 밖의 변수에 의존하지 않는다.
4. 양수·0·음수의 각 경우에 정해진 값을 `return`한다.
5. 함수 밖에서 여러 값을 반복하여 함수에 전달하고, 반환값을 출력한다. 음수이면 안내를 출력한다.

예를 들어 함수를 완성한 뒤 다음 호출 코드를 실행할 수 있어야 한다.

~~~python
numbers = [0, 1, 2, 13, 32, -3]

for number in numbers:
    result = decimal_to_binary(number)
    if result is None:
        print(number, ': 음수는 지원하지 않습니다.')
    else:
        print(number, '->', result)
~~~

`None`은 변환 결과가 없다는 표시다. `result is None`은 그 표시를 검사한다.
`print`만 사용하는 함수로 만들면 화면에 결과가 보여도 반환값을 다음 작업에 사용할 수 없다는 점에 주의한다.

## 12.3. 확인 사례와 제출물

| 호출 | 기대하는 반환값 |
| --- | --- |
| `decimal_to_binary(0)` | `'0'` |
| `decimal_to_binary(1)` | `'1'` |
| `decimal_to_binary(2)` | `'10'` |
| `decimal_to_binary(13)` | `'1101'` |
| `decimal_to_binary(32)` | `'100000'` |
| `decimal_to_binary(-3)` | `None` |

같은 함수를 `13 → 2 → 13`의 순서로 호출해도 각각 `'1101'`, `'10'`, `'1101'`을 반환하는지 확인한다.
이전 호출의 계산 결과가 다음 호출에 남아 있으면 안 된다.

**제출물:** 함수 정의, 여러 입력을 처리하는 호출 코드, 확인 사례별 결과, 그리고
‘4장의 프로그램과 비교해 매개변수·지역변수·반환값이 어떤 역할을 하는가?’에 대한 짧은 설명.

<!--
풀이 예시:
def decimal_to_binary(number):
    if number < 0:
        return None
    if number == 0:
        return '0'

    remaining = number
    binary = ''
    while remaining > 0:
        remainder = remaining % 2
        binary = str(remainder) + binary
        remaining = remaining // 2
    return binary

numbers = [0, 1, 2, 13, 32, -3]
for number in numbers:
    result = decimal_to_binary(number)
    if result is None:
        print(number, ': 음수는 지원하지 않습니다.')
    else:
        print(number, '->', result)

설명:
number는 입력을 받는 매개변수다. remaining과 binary는 호출마다 새로 계산하는 지역변수다.
return으로 문자열을 돌려주면 호출한 곳에서 저장하거나 출력할 수 있다.
함수의 계산과 출력 처리를 분리하므로 같은 변환 기능을 여러 입력에 재사용할 수 있다.
-->
