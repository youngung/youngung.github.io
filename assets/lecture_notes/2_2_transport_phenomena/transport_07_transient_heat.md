---
layout: page
title: 비정상 열전도
description: 시간에 따른 온도 변화와 반무한고체 해
target: 2학년 2학기
permalink:
prerequisite: 열전도 방정식, 지수함수, 오차함수의 개념
toc: false
---

**목차**

* TOC
{:toc}

# 1. 비정상상태

고체의 온도가 시간에 따라 변하면 축적항을 포함해야 한다.

$$\frac{\partial T}{\partial t}=\alpha\nabla^2T$$

온도장을 구하려면 초기조건(initial condition)과 경계조건(boundary condition)이 모두 필요하다.

# 2. 열확산 시간척도

열이 거리 $L$만큼 퍼지는 데 필요한 대표 시간은

$$t_c\sim\frac{L^2}{\alpha}$$

이다. 같은 길이에서 $\alpha$가 큰 재료일수록 온도 변화가 내부로 빠르게
전달된다. Fourier 수는 무차원 시간이다.

$$\mathrm{Fo}=\frac{\alpha t}{L^2}$$

# 3. 집중용량법

물체 내부 온도차가 무시할 만큼 작으면 전체 물체를 하나의 온도 $T(t)$로
나타낼 수 있다. 대류로 냉각되는 물체의 에너지 수지는

$$\rho c_pV\frac{dT}{dt}=-hA_s(T-T_\infty)$$

이고 해는

$$\boxed{\frac{T(t)-T_\infty}{T_i-T_\infty}
=\exp\left(-\frac{hA_s}{\rho c_pV}t\right)}$$

이다.

## 3.1. Biot 수로 내부 온도차를 판단하기

집중용량법에서 사용하는 특성길이는 $L_c=V/A_s$이고,

$$\mathrm{Bi}=\frac{hL_c}{k}$$

이다. Bi는 내부 전도 저항과 표면 대류 저항의 상대적인 크기를 나타낸다.
$\mathrm{Bi}\ll1$이면 표면에서 열을 빼앗기는 속도에 비해 내부의 열전도가
빨라 내부 온도차가 작다. 보통 $\mathrm{Bi}<0.1$을 집중용량 근사의 판단
기준으로 사용하지만 허용오차와 형상도 함께 고려한다.

반지름 $R$인 구는 $L_c=R/3$, 옆면으로만 열을 교환하는 긴 원기둥은
$L_c=R/2$, 양쪽 넓은 면으로 열을 교환하는 두께 $2L$인 평판은 $L_c=L$이다.
Fourier 수에서 사용하는 길이도 문제마다 명시해야 하며, 항상 $V/A_s$인 것은 아니다.

앞의 에너지 수지에서 $\theta=T-T_\infty$로 놓으면
$d\theta/\theta=-dt/\tau$, $\tau=\rho c_pV/(hA_s)$이다. 이를 초기상태부터
적분하면 $\ln(\theta/\theta_i)=-t/\tau$가 되어 지수함수 해를 얻는다.
목표 온도 $T_f$까지 냉각하는 시간은

$$t=\tau\ln\left(\frac{T_i-T_\infty}{T_f-T_\infty}\right)$$

이다. 여기서는 주변온도와 $h$, 물성이 일정하고 복사 및 열생성이 없다고 가정한다.

# 4. 반무한고체

가열 또는 냉각의 영향이 아직 반대쪽 경계에 도달하지 않은 두꺼운 고체를
반무한고체로 근사할 수 있다. 처음 온도가 $T_i$이고 $t>0$에서 표면온도가
$T_s$로 갑자기 바뀌어 유지되면

$$\boxed{\frac{T(x,t)-T_s}{T_i-T_s}
=\operatorname{erf}\left(\frac{x}{2\sqrt{\alpha t}}\right)}$$

이다. 온도 변화가 침투한 거리의 크기는 대략 $\sqrt{\alpha t}$에 비례한다.

```python
from math import erf, sqrt

alpha = 1.0e-5
x = 0.02
t = 100.0
T_initial = 300.0
T_surface = 500.0

eta = x/(2.0*sqrt(alpha*t))
temperature = T_surface + (T_initial - T_surface)*erf(eta)
print(temperature)
```

## 두 해를 구분하는 기준

집중용량법은 물체 내부의 온도를 하나의 값으로 볼 수 있을 때 사용한다. 반면
반무한고체 해는 표면 근처에 온도구배가 생기지만 열의 영향이 아직 반대쪽
경계에 도달하지 않았을 때 사용한다.

| 근사 | 내부 온도구배 | 대표 판단 기준 |
|---|---|---|
| 집중용량법 | 무시 | $\mathrm{Bi}<0.1$ |
| 반무한고체 | 고려 | 열 침투깊이가 고체 두께보다 충분히 작음 |

계산 결과는 $t=0$의 초기조건과 표면의 경계조건을 만족하는지 확인해야 한다.

## 집중용량법 계산 예제

질량이 $2\ \mathrm{kg}$이고 비열이 $500\ \mathrm{J/(kgK)}$인 금속 물체가
$200\ ^\circ\mathrm C$에서 시작한다. 표면적은 $0.10\ \mathrm{m^2}$이고
$20\ ^\circ\mathrm C$ 공기 중에서 $h=20\ \mathrm{W/(m^2K)}$로 냉각된다.
내부 온도차를 무시할 수 있다면 시간상수는

$$
\tau=\frac{mc_p}{hA_s}
=\frac{2(500)}{20(0.10)}=500\ \mathrm s
$$

이다. $t=500\ \mathrm s$에서 무차원 온도는 $e^{-1}\approx0.368$이므로

$$
T=20+(200-20)(0.368)\approx86.2\ ^\circ\mathrm C
$$

이다. 시간상수는 초기 온도차가 약 36.8%로 줄어드는 데 걸리는 시간이다.

## 오차함수와 반무한 근사를 해석하기

오차함수는 다음 적분으로 정의한다.

$$\operatorname{erf}(\eta)=\frac{2}{\sqrt\pi}\int_0^\eta e^{-u^2}\,du.$$

$\operatorname{erf}(0)=0$, $\operatorname{erf}(\infty)=1$이므로 표면에서는
$T=T_s$, 멀리서는 $T=T_i$를 만족한다. $t\to0^+$에서 **고정된 $x>0$**의
온도는 $T_i$로 수렴한다. 표면 $x=0$에서는 $t>0$에 즉시 $T_s$를 지정하므로
초기조건과 경계조건이 만나는 점에는 이상적인 온도 불연속이 있다.

침투깊이에 정확한 경계가 있는 것은 아니다. 표면에서 두께 $H$만큼 떨어진
반대면의 온도 변화가 전체 온도차의 1% 미만이기를 원한다면

$$
\frac{\lvert T(H,t)-T_i\rvert}{\lvert T_s-T_i\rvert}
=\operatorname{erfc}\left(\frac{H}{2\sqrt{\alpha t}}\right)<0.01
$$

을 반무한 근사의 판단 기준으로 삼을 수 있다. 예를 들어
$H/(2\sqrt{\alpha t})\ge2$이면 이 비율은 약 0.0047 이하이다.
이는 유한 두께 문제의 오차에 대한 엄밀한 상한이라기보다 반대면 영향이
작은지를 판단하는 실용적인 기준이다.

표면을 통해 들어가는 열유속은 위의 해를 미분하여

$$q_{in}''(t)=\frac{k(T_s-T_i)}{\sqrt{\pi\alpha t}}$$

로 얻는다. 초기의 $t^{-1/2}$ 발산은 표면온도를 순간적으로 바꾼 이상화의
결과이다. 실제로는 표면 열전달 저항이나 가열 장치의 응답시간이 존재한다.

# 5. 연습 문제

1. $L=0.01\ \mathrm m$, $\alpha=10^{-5}\ \mathrm{m^2/s}$일 때 $L^2/\alpha$를 구하라.
2. 집중용량법에서 $T_i=400$ K, $T_\infty=300$ K이고 무차원 온도가 0.5이면 $T$를 구하라.
3. 반무한고체에서 시간이 네 배가 되면 대표 침투깊이는 몇 배가 되는가?
4. $\alpha=2\times10^{-5}\ \mathrm{m^2/s}$, $t=5\ \mathrm s$일 때 $\sqrt{\alpha t}$를 구하라.
5. Biot 수가 0.02인 물체에 집중용량법을 적용할 수 있는지 판단하라.
6. 냉각 중인 물체에서 $T_i>T_\infty$일 때 무차원 온도는 처음에 얼마인가?

<!--
풀이와 해답:
1. 10 s이다.
2. (T-300)/(400-300)=0.5이므로 T=350 K이다.
3. 침투깊이는 sqrt(t)에 비례하므로 2배이다.
4. sqrt(2e-5*5)=sqrt(1e-4)=0.01 m이다.
5. 0.02<0.1이므로 일반적으로 적용할 수 있다.
6. t=0에서 (T_i-T_inf)/(T_i-T_inf)=1이다.
-->

## 관련자료와 이어 읽기

- [MIT OCW 3.185: Heat Conduction](https://ocw.mit.edu/courses/3-185-transport-phenomena-in-materials-engineering-fall-2003/resources/chap3/): Newtonian cooling 부분을 본문의 집중용량 에너지 수지와 연결해 읽는다.
- [MIT OCW 3.205: 확산·열방정식 해법](https://ocw.mit.edu/courses/3-205-thermodynamics-and-kinetics-of-materials-fall-2006/pages/lecture-notes/): L3의 Solutions to the Diffusion/Heat Equation은 해법을 더 공부하기 위한 심화자료이다.

- [제5강: 열전도 방정식](/assets/lecture_notes/2_2_transport_phenomena/transport_05_heat_equation.md)
- [제10강: 비정상 확산](/assets/lecture_notes/2_2_transport_phenomena/transport_10_transient_diffusion.md)

---

[이전 강의](/assets/lecture_notes/2_2_transport_phenomena/transport_06_heat_fdm.md) · [강의 목록](/_lectures/2_2_transport.md) · [다음 강의](/assets/lecture_notes/2_2_transport_phenomena/transport_08_diffusion_basics.md)
