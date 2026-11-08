---
layout: page
title: 열전달 기초
description: 전도, 대류, 복사 및 열저항
target: 2학년 2학기
permalink:
prerequisite: 에너지와 온도, 미분, 단위 환산
toc: false
---

**목차**

* TOC
{:toc}

# 1. 열과 온도

온도는 물체의 열적 상태를 나타내는 스칼라 장변수이다. 열은 온도차 때문에
계의 경계를 통과하는 에너지이다. 열전달률 $\dot Q$의 단위는 W이고, 열유속
$q''=\dot Q/A$의 단위는 $\mathrm{W/m^2}$이다.

# 2. 열전달의 세 방식

| 방식 | 주요 관계식 | 특징 |
|---|---|---|
| 전도 | $q''=-k\,dT/dx$ | 물질 내부의 온도구배 |
| 대류 | $q''=h(T_s-T_\infty)$ | 표면과 움직이는 유체 사이 |
| 복사 | $q''=\varepsilon\sigma(T_s^4-T_{sur}^4)$ | 전자기파에 의한 전달 |

이 강의에서는 고체 내부의 전도를 중심으로 다룬다.

## 2.1. 각 계수의 의미와 사용 온도

전도는 물질의 거시적 이동 없이 일어나며, 유체의 대류 열전달에는 유동과 표면
근처의 전도가 함께 관여한다. $h$는 재료만의 물성이 아니라 유속, 형상,
유체 물성과 유동상태에 따라 달라지는 열전달계수이다.

복사식의 $\varepsilon$은 방사율, $\sigma$는 Stefan–Boltzmann 상수이다.
표에 제시한 복사식은 작은 회색 표면이 온도 $T_{sur}$인 매우 큰 등온 주변면에
둘러싸인 경우의 순복사 교환에 해당한다. 여러 유한한 면 사이의 교환에는
형상계수와 주변면의 방사 특성도 필요하다. **복사식의 네제곱에는 절대온도 K를
사용한다.** 전도·대류의 온도차는 K 차이와 섭씨 차이의 수치가 같다.

# 3. 푸리에의 열전도법칙

$$\boxed{q_x''=-k\frac{dT}{dx}}$$

열전도도 $k$의 단위는 $\mathrm{W/(m\,K)}$이다. 음수 부호는 열이 온도가
감소하는 방향으로 흐른다는 뜻이다.

$k=20\ \mathrm{W/(m\,K)}$, $dT/dx=-50\ \mathrm{K/m}$이면
$q_x''=1000\ \mathrm{W/m^2}$이고 열은 $+x$ 방향으로 흐른다.

# 4. 평면벽(slab)의 정상 열전도

두께 $L$, 면적 $A$, 일정한 $k$인 벽의 양면 온도가 $T_1$, $T_2$일 때
열생성이 없는 정상상태 온도분포와 열전달률은

$$T(x)=T_1+\frac{T_2-T_1}{L}x,$$

$$\boxed{\dot Q=\frac{kA}{L}(T_1-T_2)}$$

이다.

## 4.1. 선형 온도분포의 유도와 한계

정상상태이고 벽 내부에서 열이 생성되지 않으면 같은 면적을 통과하는 열유속은
일정하다. 따라서 $-k\,dT/dx=q''=\text{일정}$이고, $k$도 일정하면

$$
\int_{T_1}^{T(x)}dT=-\frac{q''}{k}\int_0^x dx,
\qquad T(x)=T_1-\frac{q''}{k}x.
$$

$x=L$에서 $T=T_2$를 적용하면 앞의 열전달률 식을 얻는다. 열생성이 있거나
$k$가 온도에 따라 크게 바뀌면 온도분포는 일반적으로 선형이 아니다.
정상상태라는 조건 하나만으로 선형분포를 가정해서는 안 된다.

# 5. 열저항

$$R_{cond}=\frac{L}{kA},\qquad \dot Q=\frac{T_1-T_2}{R_{cond}}$$

여러 층이 직렬로 놓이면

$$R_{total}=\sum_i\frac{L_i}{k_iA},\qquad
\dot Q=\frac{T_{hot}-T_{cold}}{R_{total}}$$

이다. 열전도도가 작거나 두께가 큰 층에서 온도강하가 크게 나타난다.

## 전도 문제의 해석 순서

1. 고온면과 저온면을 정하고 열의 양의 방향을 정한다.
2. 각 층의 두께, 열전도도, 면적을 SI 단위로 바꾼다.
3. 층별 열저항을 계산하고 직렬 저항을 더한다.
4. 전체 온도차를 전체 열저항으로 나누어 열전달률을 구한다.
5. $\dot Q/A$로 열유속을 계산하고 부호가 물리적 방향과 맞는지 확인한다.

정상상태의 직렬 벽에서는 모든 층을 통과하는 열전달률이 같다. 각 층의
온도강하는 $\Delta T_i=\dot Q R_i$이므로 열저항이 큰 층에서 더 크다.

## 전도와 대류가 함께 있는 벽

벽의 양쪽에 유체가 흐르면 유체에서 벽 표면까지는 대류, 벽 내부에서는 전도가
일어난다. 대류 열저항은 $R_{conv}=1/(hA)$이다. 평면벽 하나를 사이에 둔 두
유체 사이의 전체 열저항은

$$
R_{total}=\frac{1}{h_1A}+\frac{L}{kA}+\frac{1}{h_2A}
$$

이고 $\dot Q=(T_{\infty,1}-T_{\infty,2})/R_{total}$이다.

예를 들어 $A=1\ \mathrm{m^2}$, $h_1=h_2=10\ \mathrm{W/(m^2K)}$,
$L=0.02\ \mathrm m$, $k=0.5\ \mathrm{W/(mK)}$이면
$R_{total}=0.24\ \mathrm{K/W}$이다. 유체 온도차가 24 K이면
$\dot Q=100\ \mathrm W$이다. 벽에서 4 K, 양쪽 대류층에서 각각 10 K의
온도강하가 발생한다.

## 열저항 모델을 적용하기 전에 확인할 조건

직렬 열저항의 합은 일차원 정상상태이며 각 경로에서 열생성이 없고 옆면으로
열이 새지 않을 때 사용한다. 완전한 접촉면에서는 온도가 연속이고, 두 재료의
$k$가 다르면 같은 열유속을 유지하기 위해 온도구배가 달라진다.

실제 접촉면에 온도 도약이 생기면 면적당 접촉 열저항 $R_c''$를 사용하여

$$\Delta T_c=q''R_c'',\qquad R_c=R_c''/A$$

를 추가한다. $R_c''$의 단위는 $\mathrm{m^2K/W}$이다.

원통형 단열층에서는 면적이 $r$에 따라 달라지므로 평면벽의 $L/(kA)$를 그대로
쓸 수 없다. 길이 $L_z$인 원통의 정상 전도에 대해

$$
\dot Q=-k(2\pi rL_z)\frac{dT}{dr},\qquad
R_{cyl}=\frac{\ln(r_2/r_1)}{2\pi kL_z}
$$

이다. 이것은 [제9강의 원통 확산]({% link assets/lecture_notes/2_2_transport_phenomena/transport_09_steady_diffusion.md %})과
동일한 적분 구조를 갖는다.

# 6. 연습 문제

1. $k=10\ \mathrm{W/(m\,K)}$, $dT/dx=30\ \mathrm{K/m}$일 때 열유속과 방향을 구하라.
2. $L=0.1\ \mathrm m$, $A=2\ \mathrm{m^2}$, $k=5\ \mathrm{W/(m\,K)}$인 벽의 열저항을 구하라.
3. 위 벽의 양면 온도가 400 K와 300 K일 때 열전달률을 구하라.
4. 열전달률이 50 W이고 면적이 $0.25\ \mathrm{m^2}$일 때 열유속을 구하라.
5. 같은 재료와 면적에서 벽의 두께를 두 배로 하면 전도 열저항은 어떻게 되는가?
6. 열전도도가 큰 재료와 작은 재료 중 단열재에 더 적합한 재료를 고르라.

<!--
풀이와 해답:
1. q''=-300 W/m^2이며 -x 방향이다.
2. R=0.01 K/W이다.
3. Qdot=10000 W이다.
4. q''=Qdot/A=200 W/m^2이다.
5. R=L/(kA)이므로 두 배가 된다.
6. 같은 두께에서 열저항이 더 큰, 열전도도가 작은 재료가 적합하다.
-->

## 관련자료와 이어 읽기

- [MIT OCW 3.185: Heat Conduction](https://ocw.mit.edu/courses/3-185-transport-phenomena-in-materials-engineering-fall-2003/resources/chap3/): PDF의 multilayer wall 및 radiation 부분을 연결해 읽는다.

- [제5강: 열전도 방정식]({% link assets/lecture_notes/2_2_transport_phenomena/transport_05_heat_equation.md %})
- [제9강: 정상상태 확산]({% link assets/lecture_notes/2_2_transport_phenomena/transport_09_steady_diffusion.md %})

[이전 강의]({% link assets/lecture_notes/2_2_transport_phenomena/transport_03_newtonian_viscosity.md %}) | [강의 목록]({% link _lectures/2_2_transport.md %}) | [다음 강의]({% link assets/lecture_notes/2_2_transport_phenomena/transport_05_heat_equation.md %})
