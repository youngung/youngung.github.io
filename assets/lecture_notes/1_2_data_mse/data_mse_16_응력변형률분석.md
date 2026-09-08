---
layout: distill
title: 응력–변형률 데이터 분석
description: 인장시험 데이터의 교정, 변환, 시각화와 기계적 성질 계산
target: 1학년 2학기
permalink:
featured: true
prerequisite: NumPy 배열, 파일 입출력, Matplotlib 기초
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
- [2. 인장시험에서 측정하는 값](#2-인장시험에서-측정하는-값)
- [3. 센서 신호 교정](#3-센서-신호-교정)
- [4. 공칭응력과 공칭변형률](#4-공칭응력과-공칭변형률)
  - [계산 예제](#계산-예제)
- [5. 힘–변위 데이터를 공칭곡선으로 변환](#5-힘변위-데이터를-공칭곡선으로-변환)
- [6. 공칭값에서 진값으로 변환](#6-공칭값에서-진값으로-변환)
- [7. 응력–변형률 곡선에서 읽을 수 있는 성질](#7-응력변형률-곡선에서-읽을-수-있는-성질)
- [8. 탄성계수 구하기](#8-탄성계수-구하기)
- [9. 0.2% 오프셋 항복강도](#9-02-오프셋-항복강도)
- [10. 소성구간과 Hollomon 식](#10-소성구간과-hollomon-식)
- [11. 실제 데이터 파일 다루기](#11-실제-데이터-파일-다루기)
- [12. 분석 순서와 검산](#12-분석-순서와-검산)
- [13. 핵심 정리](#13-핵심-정리)
- [14. 쉬운 연습 문제](#14-쉬운-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)
  - [문제 7](#문제-7)
  - [문제 8](#문제-8)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 인장시험에서 직접 측정하는 값과 계산하는 값을 구분할 수 있다.
- 전압 교정식을 이용해 센서 신호를 변위와 힘으로 변환할 수 있다.
- 힘과 변위로부터 공칭응력과 공칭변형률을 계산할 수 있다.
- 균일변형 구간의 공칭값을 진응력과 진변형률로 변환할 수 있다.
- 응력–변형률 곡선에서 영률, 항복강도, 인장강도와 연신율을 설명할 수 있다.
- NumPy와 Matplotlib으로 간단한 인장시험 데이터를 분석할 수 있다.
- 계산 결과의 단위와 물리적 타당성을 검산할 수 있다.

# 2. 인장시험에서 측정하는 값

인장시험기는 시편을 잡아당기면서 일반적으로 다음 값을 기록한다.

- **하중(load 또는 force)**: 로드셀(load cell)로 측정한다.
- **변위(displacement)**: 시험기 크로스헤드 또는 신율계(extensometer)로 측정한다.
- **시간(time)**: 데이터가 기록된 시점을 나타낸다.

응력과 변형률은 시험기가 직접 측정하는 값이 아니라 측정된 하중과 변위를 시편의 초기
치수로 정규화하여 계산한 값이다.

| 구분 | 시험에서 얻는 값 | 분석에 필요한 시편 정보 | 계산 결과 |
|---|---|---|---|
| 하중 방향 | 힘 $F$ | 초기 단면적 $A_0$ | 공칭응력 $s$ |
| 길이 방향 | 길이 변화 $\Delta L$ | 초기 표점거리 $L_0$ | 공칭변형률 $e$ |

시편마다 폭, 두께와 표점거리가 다를 수 있으므로 힘–변위 곡선만으로 서로 다른 시편의
재료특성을 직접 비교하면 안 된다. 응력–변형률로 변환해야 시편 크기의 영향을 줄일 수
있다.

# 3. 센서 신호 교정

센서는 힘이나 변위를 전압으로 출력할 수 있다. 전압 $V$를 실제 물리량 $q$로 바꾸는
간단한 선형 교정식은

$$
q=aV+b
$$

이다. 기울기 $a$는 전압 한 단위가 물리량 몇 단위에 해당하는지 나타내고, 절편 $b$는
영점 보정을 나타낸다.

다음 교정 파일을 사용해 보자.

- [변위 교정 데이터](/assets/dat_files/lectures/1_2_data_mse/calibration1.txt)
- [하중 교정 데이터](/assets/dat_files/lectures/1_2_data_mse/calibration2.txt)

두 파일 모두 첫 번째 열은 실제 물리량, 두 번째 열은 센서 전압이다.

~~~python
import numpy as np
import matplotlib.pyplot as plt


displacement_calibration = np.loadtxt("calibration1.txt")
force_calibration = np.loadtxt("calibration2.txt")

displacement = displacement_calibration[:, 0]  # mm
displacement_voltage = displacement_calibration[:, 1]
force = force_calibration[:, 0]                # kN
force_voltage = force_calibration[:, 1]

displacement_slope, displacement_intercept = np.polyfit(
    displacement_voltage,
    displacement,
    1,
)
force_slope, force_intercept = np.polyfit(
    force_voltage,
    force,
    1,
)

print(
    f"Displacement = {displacement_slope:.5f} V + "
    f"{displacement_intercept:.5f} mm"
)
print(
    f"Force = {force_slope:.5f} V + "
    f"{force_intercept:.5f} kN"
)
~~~

위 출력에서 <code>V</code>는 수식의 전압 변수를 뜻한다. 적합된 교정선을 측정점과 함께
그려 확인하자.

~~~python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

voltage_line_1 = np.linspace(
    displacement_voltage.min(),
    displacement_voltage.max(),
    100,
)
axes[0].scatter(displacement_voltage, displacement, label="Calibration data")
axes[0].plot(
    voltage_line_1,
    displacement_slope * voltage_line_1 + displacement_intercept,
    color="tab:red",
    label="Linear fit",
)
axes[0].set_xlabel("Voltage (V)")
axes[0].set_ylabel("Displacement (mm)")
axes[0].grid(True, alpha=0.3)
axes[0].legend()

voltage_line_2 = np.linspace(force_voltage.min(), force_voltage.max(), 100)
axes[1].scatter(force_voltage, force, label="Calibration data")
axes[1].plot(
    voltage_line_2,
    force_slope * voltage_line_2 + force_intercept,
    color="tab:red",
    label="Linear fit",
)
axes[1].set_xlabel("Voltage (V)")
axes[1].set_ylabel("Force (kN)")
axes[1].grid(True, alpha=0.3)
axes[1].legend()

fig.tight_layout()
plt.show()
~~~

교정점을 전압 순서로 정렬하지 않아도 산점도와 직선 적합은 가능하다. 측정점을 선으로
연결하려면 먼저 전압을 기준으로 정렬해야 선이 뒤엉키지 않는다. 직선 적합의 원리는 다음
최소제곱법 강의에서 자세히 다룬다.

# 4. 공칭응력과 공칭변형률

공칭응력(engineering stress)은 현재 면적이 아니라 변형 전 초기 단면적 $A_0$를
사용한다.

$$
\boxed{s=\frac{F}{A_0}}
$$

직사각형 단면의 폭이 $w_0$, 두께가 $t_0$이면

$$
A_0=w_0t_0
$$

이다. 힘을 N, 면적을 $\mathrm{mm^2}$로 사용하면

$$
1\ \mathrm{N/mm^2}=1\ \mathrm{MPa}
$$

이므로 응력은 바로 MPa로 계산된다. 힘이 kN이면 먼저 1000을 곱하여 N으로 바꿔야 한다.

공칭변형률(engineering strain)은 초기 표점거리 $L_0$에 대한 길이 변화의 비다.

$$
\boxed{e=\frac{L-L_0}{L_0}=\frac{\Delta L}{L_0}}
$$

변형률은 길이를 길이로 나눈 값이므로 단위가 없다. 흔히 백분율로 표시할 때는 100을
곱한다.

## 계산 예제

폭 10 mm, 두께 2 mm, 표점거리 50 mm인 시편에 10 kN의 힘이 작용하고 표점부가
0.50 mm 늘어났다고 하자.

$$
A_0=(10)(2)=20\ \mathrm{mm^2}
$$

$$
s=\frac{10\,000}{20}=500\ \mathrm{MPa}
$$

$$
e=\frac{0.50}{50}=0.010=1.0\%
$$

# 5. 힘–변위 데이터를 공칭곡선으로 변환

다음은 설명을 위해 단순화한 인장시험 데이터다. 초기 폭은 6 mm, 두께는 2 mm,
표점거리는 50 mm이다.

~~~python
displacement_mm = np.array([0.00, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00, 4.00])
force_n = np.array([0, 1650, 3300, 5900, 7200, 7900, 8500, 8200])

initial_width_mm = 6.0
initial_thickness_mm = 2.0
initial_gauge_length_mm = 50.0
initial_area_mm2 = initial_width_mm * initial_thickness_mm

engineering_strain = displacement_mm / initial_gauge_length_mm
engineering_stress_mpa = force_n / initial_area_mm2

print(engineering_strain)
print(engineering_stress_mpa)
~~~

계산한 공칭응력–공칭변형률 곡선을 그려 보자.

~~~python
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(engineering_strain, engineering_stress_mpa, marker="o")
ax.set_xlabel("Engineering strain")
ax.set_ylabel("Engineering stress (MPa)")
ax.set_title("Engineering Stress–Strain Curve")
ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
~~~

마지막 데이터에서 힘이 감소하므로 공칭응력도 감소한다. 이 데이터만으로 정확한 네킹
시작점을 정하기에는 점의 수가 부족하지만, 일반적인 인장시험에서는 최대하중 부근에서
네킹이 시작된다.

# 6. 공칭값에서 진값으로 변환

진변형률(true strain)은 순간적인 길이 증가율을 누적한 값이다.

$$
\varepsilon=\int_{L_0}^{L}\frac{dL}{L}
=\ln\left(\frac{L}{L_0}\right)
$$

$L=L_0(1+e)$이므로

$$
\boxed{\varepsilon=\ln(1+e)}
$$

이다.

진응력(true stress)은 현재 단면적 $A$를 사용한다.

$$
\sigma=\frac{F}{A}
$$

균일변형 중 체적이 일정하고 폭과 두께가 균일하게 변한다고 가정하면

$$
AL=A_0L_0
$$

이므로 다음 변환식을 얻는다.

$$
\boxed{\sigma=s(1+e)}
$$

NumPy에서는 다음과 같이 모든 데이터에 원소별 연산을 적용한다.

~~~python
true_strain = np.log1p(engineering_strain)
true_stress_mpa = engineering_stress_mpa * (1.0 + engineering_strain)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(engineering_strain, engineering_stress_mpa, marker="o", label="Engineering")
ax.plot(true_strain, true_stress_mpa, marker="s", label="True")
ax.set_xlabel("Strain")
ax.set_ylabel("Stress (MPa)")
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
plt.show()
~~~

<code>np.log1p(e)</code>는 <code>np.log(1 + e)</code>와 같은 계산을 하며, $e$가 매우
작을 때 더 안정적으로 계산할 수 있다.

> 위 진응력 변환식은 변형이 표점부에 균일하게 분포하는 **네킹 이전 구간**에서
> 사용한다. 네킹 이후에는 최소단면적을 직접 측정해야 하며 목 부분의 다축응력 상태도
> 고려해야 한다.

# 7. 응력–변형률 곡선에서 읽을 수 있는 성질

일반적인 공칭응력–공칭변형률 곡선에서는 다음 기계적 성질을 구할 수 있다.

| 기계적 성질 | 의미 | 곡선에서 찾는 방법 |
|---|---|---|
| 영률 $E$ | 탄성변형에 대한 저항 | 초기 탄성구간의 기울기 |
| 항복강도 | 뚜렷한 소성변형이 시작되는 응력 | 항복점 또는 0.2% 오프셋법 |
| 인장강도 UTS | 최대 공칭응력 | 공칭응력 배열의 최댓값 |
| 균일연신율 | 네킹 전까지의 연신율 | 최대하중 부근의 공칭변형률 |
| 파단연신율 | 파단 후 전체 연신 정도 | 파단 후 표점거리로 계산 |
| 인성 | 파단까지 흡수한 단위부피당 에너지 | 응력–변형률 곡선 아래 면적 |

인장강도와 그때의 데이터 인덱스는 NumPy로 쉽게 찾을 수 있다.

~~~python
uts_index = np.argmax(engineering_stress_mpa)
uts_mpa = engineering_stress_mpa[uts_index]
strain_at_uts = engineering_strain[uts_index]

print(f"UTS: {uts_mpa:.1f} MPa")
print(f"Engineering strain at UTS: {strain_at_uts:.3f}")
~~~

파단 데이터가 충분히 포함되어 있다면 곡선 아래 면적을 수치적분하여 인성을 근사할 수
있다.

~~~python
toughness_mpa = np.trapz(
    engineering_stress_mpa,
    engineering_strain,
)

print(f"Approximate toughness: {toughness_mpa:.2f} MJ/m^3")
~~~

변형률은 무차원이고 $1\ \mathrm{MPa}=1\ \mathrm{MJ/m^3}$이므로 적분값의 수치는
$\mathrm{MJ/m^3}$로 해석할 수 있다. 현재 예제는 파단점까지의 조밀한 실제 데이터가
아니므로 학습용 근삿값이다.

# 8. 탄성계수 구하기

탄성구간에서는 Hooke 법칙

$$
\sigma=E\varepsilon
$$

이 성립한다. 실제 측정값에는 작은 오차와 영점 편차가 있으므로 선택한 탄성구간에 직선을
적합하여 기울기를 구할 수 있다.

~~~python
elastic_strain = np.array([0.0000, 0.0005, 0.0010, 0.0015, 0.0020])
elastic_stress = np.array([1.0, 35.0, 70.0, 104.0, 140.0])  # MPa

youngs_modulus_mpa, stress_intercept_mpa = np.polyfit(
    elastic_strain,
    elastic_stress,
    1,
)

print(f"Young's modulus: {youngs_modulus_mpa / 1000:.1f} GPa")
print(f"Intercept: {stress_intercept_mpa:.2f} MPa")
~~~

이 예제에서는 약 69 GPa가 계산된다. <code>np.polyfit()</code>을 이용한 직선 적합의
원리는 다음 최소제곱법 강의에서 자세히 다룬다.

탄성계수를 구할 때는 다음을 주의한다.

- 눈으로 보아 직선인 탄성구간만 선택한다.
- 초기 장착 유격이나 미끄러짐이 포함된 구간을 점검한다.
- 크로스헤드 변위보다 신율계로 측정한 표점부 변형률이 일반적으로 더 적합하다.
- 시편과 시험기의 정렬 상태를 확인한다.

# 9. 0.2% 오프셋 항복강도

뚜렷한 항복점이 없는 재료에는 0.2% 오프셋 항복강도를 자주 사용한다.

1. 탄성구간의 기울기 $E$를 구한다.
2. 탄성 직선을 변형률축의 양의 방향으로 0.002만큼 평행이동한다.
3. 이동한 직선과 응력–변형률 곡선의 교점을 찾는다.
4. 교점의 응력을 0.2% 오프셋 항복강도로 정의한다.

절편을 포함한 탄성 적합식이 $\sigma=E\varepsilon+b$라면 오프셋 직선은

$$
\sigma_{offset}=E(\varepsilon-0.002)+b
$$

이다. 실제 데이터에서는 두 곡선의 차이 부호가 바뀌는 구간을 찾아 교점을 보간하는 것이
좋다. 단순히 가장 가까운 데이터 한 점만 선택하면 데이터 간격에 따른 오차가 생길 수 있다.

# 10. 소성구간과 Hollomon 식

Hollomon 식은 균일 소성변형 구간의 유동응력을 다음과 같이 근사한다.

$$
\sigma=K(\varepsilon^{pl})^n
$$

- $K$: 강도계수
- $n$: 변형경화지수
- $\varepsilon^{pl}$: 진소성변형률

전체 진변형률은 탄성변형률과 소성변형률의 합이므로

$$
\varepsilon^{pl}
=\varepsilon-\varepsilon^{el}
=\varepsilon-\frac{\sigma}{E}
$$

이다. Hollomon 식에는 전체 변형률이 아니라 소성변형률을 사용하는 것이 더 정확하다.

양변에 자연로그를 취하면

$$
\ln\sigma=\ln K+n\ln\varepsilon^{pl}
$$

이므로 로그 좌표에서 직선 적합을 이용해 $n$과 $K$를 구할 수 있다.

~~~python
plastic_strain = np.array([0.02, 0.04, 0.08, 0.12, 0.18])
flow_stress_mpa = np.array([280, 322, 370, 402, 435])

hardening_exponent, log_strength_coefficient = np.polyfit(
    np.log(plastic_strain),
    np.log(flow_stress_mpa),
    1,
)
strength_coefficient_mpa = np.exp(log_strength_coefficient)

print(f"n: {hardening_exponent:.3f}")
print(f"K: {strength_coefficient_mpa:.1f} MPa")
~~~

로그를 계산할 수 있도록 응력과 소성변형률은 모두 양수여야 한다. 네킹 이후에는 단순한
공칭–진 변환이 유효하지 않으므로 일반적인 Hollomon 상수 적합에서는 제외한다.

# 11. 실제 데이터 파일 다루기

[힘–변위 데이터](/assets/dat_files/lectures/1_2_data_mse/force_vs_displ.txt)는 파일 앞부분의
시험 정보와 여러 개의 데이터 블록을 포함한다. 따라서 파일 전체에
<code>np.loadtxt()</code>를 바로 적용하면 문자열을 실수로 바꿀 수 없다는 오류가 발생한다.

파일을 열어 보면 각 데이터 블록은 다음 구조를 갖는다.

~~~text
Data Acquisition ...
Time    Axial Displacement    Axial Force    Axial Strain
Sec     mm                    N              mm/mm
숫자 데이터 ...
~~~

첫 번째 데이터 블록처럼 시작 행과 행 개수를 알고 있다면 다음과 같이 일부만 읽을 수
있다.

~~~python
first_block = np.loadtxt(
    "force_vs_displ.txt",
    skiprows=19,
    max_rows=190,
)

time_s = first_block[:, 0]
axial_displacement_mm = first_block[:, 1]
axial_force_n = first_block[:, 2]
axial_strain = first_block[:, 3]

print(first_block.shape)
print(first_block[:3])
~~~

이 방법은 파일 구조가 고정되어 있을 때만 안전하다. 여러 블록을 모두 자동으로 읽으려면
다음 순서를 사용한다.

1. <code>with open(...)</code>으로 파일을 연다.
2. <code>Data Acquisition</code> 문자열을 찾아 블록 시작 위치를 결정한다.
3. 열 이름과 단위 행을 건너뛴다.
4. 다음 빈 행 또는 다음 블록 표시 전까지 숫자 행만 변환한다.
5. 각 블록의 열 개수와 단위를 확인한 뒤 배열을 합친다.

복잡한 파일은 먼저 텍스트 편집기로 구조를 확인하고, 몇 행을 시험적으로 읽은 다음 전체
데이터로 확장하는 것이 안전하다.

# 12. 분석 순서와 검산

인장시험 데이터는 다음 순서로 분석할 수 있다.

1. 파일의 열 이름과 단위를 확인한다.
2. 센서 전압이라면 교정식을 적용해 힘과 변위로 바꾼다.
3. 힘과 변위의 영점을 확인하고 필요하면 보정한다.
4. 시편의 초기 폭, 두께와 표점거리로 $A_0$와 $L_0$를 정한다.
5. 공칭응력과 공칭변형률을 계산한다.
6. 원자료와 공칭응력–공칭변형률 곡선을 그려 이상값을 확인한다.
7. 탄성구간을 선택하여 영률을 구한다.
8. 필요한 경우 항복강도, 인장강도와 연신율을 계산한다.
9. 네킹 이전 구간만 공칭값에서 진값으로 변환한다.
10. 목적에 따라 소성변형률과 변형경화 상수를 계산한다.

다음 항목으로 결과를 검산한다.

- 변형 전 첫 데이터에서 응력과 변형률이 0에 가까운가?
- 모든 배열의 길이가 같은가?
- 힘, 길이와 면적의 단위가 일관적인가?
- 인장시험의 변형률이 예상대로 양수인가?
- 금속의 영률과 강도가 물리적으로 가능한 범위인가?
- 인장강도 인덱스가 실제 최대하중 인덱스와 같은가?
- 네킹 이후 데이터에 균일변형 변환식을 적용하지 않았는가?

# 13. 핵심 정리

- 시험기는 힘과 변위를 측정하고, 응력과 변형률은 시편 치수를 사용해 계산한다.
- 공칭응력은 $s=F/A_0$, 공칭변형률은 $e=\Delta L/L_0$이다.
- 균일변형 구간에서는 $\varepsilon=\ln(1+e)$와 $\sigma=s(1+e)$를 사용한다.
- 공칭응력의 최댓값이 인장강도이며 일반적으로 그 부근에서 네킹이 시작된다.
- 영률은 탄성구간의 응력–변형률 기울기다.
- 0.2% 오프셋 항복강도는 탄성 직선을 변형률 0.002만큼 평행이동하여 구한다.
- Hollomon 식에는 진소성변형률을 사용하고 네킹 이전의 균일변형 데이터를 적합한다.
- 단위, 영점, 데이터 구간과 파일 구조를 먼저 확인해야 한다.

# 14. 연습 문제

## 문제 1

힘이 2000 N이고 초기 단면적이 $10\ \mathrm{mm^2}$일 때 공칭응력을 구하시오.

<!--
풀이와 해답:
s = 2000 / 10 = 200 N/mm^2 = 200 MPa이다.
-->

## 문제 2

초기 표점거리가 50 mm인 시편이 1 mm 늘어났다. 공칭변형률과 백분율을 구하시오.

<!--
풀이와 해답:
e = 1 / 50 = 0.02이며 백분율로는 2%이다.
-->

## 문제 3

공칭변형률이 0.10이고 공칭응력이 300 MPa일 때 균일변형을 가정하여 진변형률과
진응력을 구하시오.

<!--
풀이와 해답:
진변형률은 ln(1.10) = 약 0.0953이고 진응력은 300 x 1.10 = 330 MPa이다.
-->

## 문제 4

힘을 kN, 면적을 $\mathrm{mm^2}$로 알고 있다. 응력을 MPa로 계산하기 전에 힘에 어떤
단위 변환이 필요한가?

<!--
풀이와 해답:
kN에 1000을 곱하여 N으로 변환해야 한다.
-->

## 문제 5

공칭응력 배열이 <code>[0, 100, 250, 320, 300]</code> MPa일 때 인장강도와 그 배열
인덱스를 구하시오. Python 인덱스는 0부터 시작한다.

<!--
풀이와 해답:
인장강도는 320 MPa이고 인덱스는 3이다.
-->

## 문제 6

0.2% 오프셋법에서 탄성 직선을 변형률축으로 얼마만큼 이동하는가?

<!--
풀이와 해답:
0.002, 즉 0.2%만큼 양의 변형률 방향으로 이동한다.
-->

## 문제 7

네킹 이후에 $\sigma=s(1+e)$를 그대로 적용하기 어려운 이유를 설명하시오.

<!--
풀이와 해답:
네킹 이후에는 변형과 단면적 감소가 목 부분에 집중되어 표점부가 균일하게 변형한다는
가정이 성립하지 않기 때문이다.
-->

## 문제 8

영률을 구할 때 응력–변형률 곡선의 어느 구간을 사용해야 하는가?

<!--
풀이와 해답:
초기의 선형 탄성구간을 사용해야 한다.
-->
