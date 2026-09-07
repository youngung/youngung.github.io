---
layout: page
title: 비정상 확산
description: Fick의 제2법칙과 반무한고체 확산
target: 2학년 2학기
permalink:
prerequisite: 확산 기초, 편미분, 오차함수의 개념
toc:
  sidebar: left
---

- [1. Fick의 제2법칙](#1-fick의-제2법칙)
- [2. 확산 시간척도](#2-확산-시간척도)
- [3. 반무한고체의 해](#3-반무한고체의-해)
- [4. 침탄 예제](#4-침탄-예제)
- [5. 열전도와 확산의 유사성](#5-열전도와-확산의-유사성)
  - [반무한고체 해석 순서](#반무한고체-해석-순서)
  - [적용 가정](#적용-가정)
  - [온도와 처리 시간의 영향](#온도와-처리-시간의-영향)
- [6. 연습 문제](#6-연습-문제)

# 1. Fick의 제2법칙

일차원 미소 검사체적에서 화학종 A에 대한 보존식을 세우면

$$\frac{\partial c_A}{\partial t}=-\frac{\partial J_A}{\partial x}$$

이다. $J_A=-D\,\partial c_A/\partial x$이고 $D$가 일정하면

$$\boxed{\frac{\partial c_A}{\partial t}
=D\frac{\partial^2c_A}{\partial x^2}}$$

를 얻는다. 이를 Fick의 제2법칙이라고 한다.

# 2. 확산 시간척도

확산이 거리 $L$만큼 진행되는 데 필요한 대표 시간은

$$t_c\sim\frac{L^2}{D}$$

이고 대표 확산거리는

$$L_d\sim\sqrt{Dt}$$

이다. 확산거리를 두 배로 늘리려면 대략 네 배의 시간이 필요하다.

# 3. 반무한고체의 해

처음 농도가 $c_i$로 균일한 반무한고체의 표면농도를 $t>0$에서 $c_s$로
유지하면

$$\boxed{\frac{c(x,t)-c_s}{c_i-c_s}
=\operatorname{erf}\left(\frac{x}{2\sqrt{Dt}}\right)}$$

이다. 또는 보완오차함수를 사용하여

$$\frac{c(x,t)-c_i}{c_s-c_i}
=\operatorname{erfc}\left(\frac{x}{2\sqrt{Dt}}\right)$$

로 쓸 수 있다. 두 식은 $\operatorname{erfc}(z)=1-\operatorname{erf}(z)$
관계로 서로 같다.

# 4. 침탄 예제

강의 초기 탄소농도를 $c_i=0.20\ \mathrm{wt\%}$, 표면농도를
$c_s=1.00\ \mathrm{wt\%}$로 유지한다고 하자. $D=10^{-11}\ \mathrm{m^2/s}$,
$t=10\ \mathrm h$, $x=0.5\ \mathrm{mm}$에서 농도를 계산하는 코드는 다음과
같다.

```python
from math import erfc, sqrt

c_initial = 0.20
c_surface = 1.00
D = 1.0e-11
time = 10.0*3600.0
x = 0.5e-3

eta = x/(2.0*sqrt(D*time))
concentration = c_initial + (
    c_surface - c_initial
)*erfc(eta)

print(f"c = {concentration:.3f} wt.%")
```

이 단순 해에서는 확산계수가 농도에 무관하고 표면농도가 일정하다고 가정한다.

# 5. 열전도와 확산의 유사성

$$\frac{\partial T}{\partial t}=\alpha\frac{\partial^2T}{\partial x^2},
\qquad
\frac{\partial c}{\partial t}=D\frac{\partial^2c}{\partial x^2}$$

두 방정식은 같은 수학적 형태를 갖는다. 따라서 같은 형상과 같은 종류의
초기·경계조건에서는 $T$와 $c$, $\alpha$와 $D$를 서로 대응시켜 해를 이해할
수 있다.

## 반무한고체 해석 순서

1. 초기농도 $c_i$와 일정하게 유지되는 표면농도 $c_s$를 구분한다.
2. 시간과 거리의 단위를 각각 s와 m로 바꾼다.
3. 무차원 변수 $\eta=x/(2\sqrt{Dt})$를 계산한다.
4. `erf` 또는 `erfc` 값을 구하고 농도를 계산한다.
5. 계산된 농도가 $c_i$와 $c_s$ 사이인지 확인한다.

$x=0$에서는 항상 $c=c_s$이고, 고체 안쪽으로 충분히 멀리 가면 $c\rightarrow
c_i$이다. 또한 $t$가 증가하면 같은 위치의 농도가 표면농도에 가까워진다.

## 적용 가정

- 확산계수 $D$가 농도와 위치에 무관하다.
- 확산은 한 방향으로만 일어난다.
- 표면농도는 처리 시간 동안 일정하다.
- 확산의 영향이 반대편 경계에 도달하지 않는다.

## 온도와 처리 시간의 영향

대표 확산거리는 $\sqrt{Dt}$이다. 처리 시간을 네 배로 늘리면 확산거리는 두
배가 되지만, 확산계수는 Arrhenius 관계를 따르므로 온도를 조금 높여도 크게
증가할 수 있다.

두 온도 $T_1$, $T_2$에서 확산계수의 비는

$$
\frac{D_2}{D_1}
=\exp\left[-\frac{Q_d}{R}
\left(\frac{1}{T_2}-\frac{1}{T_1}\right)\right]
$$

이다. $T_2>T_1$이면 괄호가 음수이므로 $D_2/D_1>1$이다. 따라서 침탄이나
균질화 처리에서는 온도 조절이 처리시간에 매우 큰 영향을 줄 수 있다.

다만 온도를 높이면 상변태, 결정립 성장, 산화와 같은 다른 현상도 일어날 수
있다. 실제 열처리 조건은 확산속도만으로 정하지 않고 재료의 조직 변화와 함께
판단해야 한다.

# 6. 연습 문제

1. $D=10^{-10}\ \mathrm{m^2/s}$이고 대표거리 $L=1\ \mathrm{mm}$일 때 $L^2/D$를 구하라.
2. 시간이 9배가 되면 대표 확산거리는 몇 배가 되는가?
3. 반무한고체 해에서 $x=0$일 때 농도가 $c_s$가 되는지 확인하라.
4. 위 Python 예제를 실행하여 10시간 후 농도를 구하라.
5. 2시간은 몇 초인가?
6. $D=4\times10^{-12}\ \mathrm{m^2/s}$, $t=2500\ \mathrm s$일 때 $\sqrt{Dt}$를 구하라.
7. 침탄 중 표면에서 아주 멀리 떨어진 곳의 농도는 어떤 값에 가까운가?

<!--
풀이와 해답:
1. 10000 s, 즉 약 2.78 h이다.
2. sqrt(9)=3배이다.
3. erf(0)=0이므로 c(0,t)=c_s이다.
4. eta는 약 0.4167이고 농도는 약 0.645 wt.%이다.
5. 2*3600=7200 s이다.
6. sqrt(4e-12*2500)=sqrt(1e-8)=1e-4 m, 즉 0.1 mm이다.
7. 아직 확산의 영향을 받지 않았으므로 초기농도 c_i에 가까워진다.
-->
