---
layout: page
title: 확산 기초
description: 농도, 확산 플럭스 및 Fick의 제1법칙
target: 2학년 2학기
permalink:
prerequisite: 몰과 농도, 구배, 열전달 기초
toc: false
---

**목차**

* TOC
{:toc}

# 1. 확산이란

확산(diffusion)은 원자나 분자의 무작위 열운동으로 화학종이 이동하는
현상이다. 거시적으로는 농도가 높은 곳에서 낮은 곳으로 순이동이 발생한다.

# 2. 농도의 표현

화학종 A의 몰농도는

$$c_A=\frac{n_A}{V}\quad[\mathrm{mol/m^3}]$$

이고 몰분율은

$$x_A=\frac{n_A}{\sum_i n_i},\qquad \sum_i x_i=1$$

이다. 질량농도, 질량분율 및 원자분율을 사용할 수도 있으므로 계산에서 농도의
정의와 단위를 명확히 해야 한다.

## 2.1. 몰농도, 질량분율 및 단위 환산

A의 몰질량을 $M_A\ [\mathrm{kg/mol}]$, 혼합물 밀도를 $\rho$, 질량분율을
$w_A$라 하면

$$c_A=\frac{\rho w_A}{M_A}.$$

예를 들어 0.20 wt.%는 $w_A=0.0020$이다. 질량분율과 몰분율은 일반적으로
다르므로 숫자를 그대로 대입해서는 안 된다. 밀도가 일정할 때는
$dc_A/dx=(\rho/M_A)dw_A/dx$로 바꿀 수 있지만, 밀도도 변하면 곱의 미분이 필요하다.

침탄 예제에서 wt.% 농도를 직접 사용할 수 있는 것은 밀도를 일정하게
근사하면 정규화 농도비에서 변환 계수가 상쇄되기 때문이다. 그 농도구배를
몰플럭스 계산에 사용할 때는 위 변환을 별도로 수행해야 한다.

# 3. Fick의 제1법칙

일차원에서 A의 확산 몰플럭스는

$$\boxed{J_{A,x}=-D_{AB}\frac{dc_A}{dx}}$$

이다. $J_A$의 단위는 $\mathrm{mol/(m^2\,s)}$, $D_{AB}$의 단위는
$\mathrm{m^2/s}$이다. 음수 부호는 확산이 농도 증가 방향과 반대로 일어난다는
뜻이다.

## 예제

$D=2.0\times10^{-10}\ \mathrm{m^2/s}$이고
$dc_A/dx=-5.0\times10^4\ \mathrm{mol/m^4}$이면

$$J_{A,x}=1.0\times10^{-5}\ \mathrm{mol/(m^2\,s)}$$

이다. 양수이므로 A는 $+x$ 방향으로 확산한다.

## 3.1. 기준 속도와 총플럭스

이성분 혼합물에서 전체 몰농도를 $c=c_A+c_B$, 몰평균 속도를
$\boldsymbol v^*=x_A\boldsymbol v_A+x_B\boldsymbol v_B$라고 정의한다.
몰평균 속도에 대한 확산 플럭스는

$$
\boldsymbol J_A=c_A(\boldsymbol v_A-\boldsymbol v^*),\qquad
\boldsymbol N_A=c_A\boldsymbol v^*+\boldsymbol J_A
$$

이다. $\boldsymbol N_A$는 고정된 관찰자에 대한 총 몰플럭스이며
$\boldsymbol J_A+\boldsymbol J_B=0$이다. 일정 온도·압력의 단순 이성분계에서
$\boldsymbol J_A=-cD_{AB}\nabla x_A$이고, $c$가 일정하면 본문의
$-D_{AB}\nabla c_A$와 같다.

따라서 유체가 움직이는 문제에서는 총플럭스와 확산 플럭스를 구분해야 한다.
정지한 고체의 단순 확산에서는 고체에 고정된 기준을 쓰되, 치환형 합금의
상호확산에서 격자 이동까지 다룰 때는 기준 좌표계에 더 주의해야 한다.

## 3.2. 농도구배 법칙의 적용 범위

온도·응력·전기장 등의 추가 구동력이 없고 단순한 조성 범위에서 Fick 법칙을
사용하면 농도구배의 반대방향으로 확산한다. 더 일반적인 열역학적 구동력은
화학퍼텐셜 구배이다. 비이상 합금이나 다성분계에서는 단순한 일정 $D$ 식으로
설명되지 않는 상향확산이나 결합 확산이 가능하다. 이 강의에서는 우선
일정 온도의 단상 재료에 대한 단순 농도 확산 모델을 사용한다.[^diffusivity]

[^diffusivity]: 자기확산계수, 추적자 확산계수, 고유확산계수, 상호확산계수는 측정과 정의가 다르다. 문헌의 값을 가져올 때에는 원소명뿐 아니라 상, 조성, 온도 범위와 계수의 정의가 현재 문제에 맞는지 확인한다.

# 4. 확산계수

확산계수는 온도와 물질의 조합에 따라 달라진다. 고체에서 흔히 Arrhenius
관계를 따른다.

$$\boxed{D=D_0\exp\left(-\frac{Q_d}{RT}\right)}$$

$D_0$는 빈도인자, $Q_d$는 확산 활성화에너지이다. 온도가 증가하면 일반적으로
$D$가 빠르게 증가한다.

# 5. 열전도와의 비교

| 현상 | 플럭스 | 구동력 | 전달계수 |
|---|---|---|---|
| 열전도 | $q''=-k\nabla T$ | 온도구배 | $k$ |
| 확산 | $\boldsymbol J_A=-D\nabla c_A$ | 농도구배 | $D$ |

두 식의 형태는 비슷하지만 전달되는 물리량과 단위는 다르다.

## 플럭스의 부호 읽기

농도구배와 플럭스의 부호를 다음 순서로 판단하면 쉽다.

1. 좌표의 양의 방향을 확인한다.
2. 두 위치의 농도로 $dc_A/dx$의 부호를 판단한다.
3. Fick 법칙의 음수 부호를 적용한다.
4. $J_A>0$이면 $+x$, $J_A<0$이면 $-x$ 방향으로 해석한다.

예를 들어 오른쪽으로 갈수록 농도가 낮아지면 $dc_A/dx<0$이고 $J_A>0$이다.
따라서 화학종 A는 오른쪽으로 확산한다.

> 농도가 높은 곳의 입자도 낮은 곳의 입자도 무작위로 움직인다. 농도차가 있을
> 때 높은 농도에서 낮은 농도로 이동하는 입자 수가 더 많아 순플럭스가 생긴다.

## 고체에서 원자가 이동하는 방법

결정질 고체에서 원자는 주로 두 가지 기구로 확산한다.

- **공공 확산**(vacancy diffusion): 원자가 이웃의 빈 격자점으로 이동한다.
- **침입형 확산**(interstitial diffusion): 작은 원자가 격자 사이의 빈 공간으로
  이동한다.

탄소처럼 작은 침입형 원자는 철 원자 사이를 이동할 수 있으므로 일반적으로
치환형 원자보다 빠르게 확산한다. 공공의 수가 증가하거나 원자가 이동 장벽을
넘을 확률이 커지면 확산계수가 증가한다. 온도 상승이 확산을 빠르게 만드는
이유도 여기에 있다.

Arrhenius 식의 양변에 자연로그를 취하면

$$
\ln D=\ln D_0-\frac{Q_d}{R}\frac{1}{T}
$$

이다. 따라서 $\ln D$를 $1/T$에 대해 그리면 기울기가 $-Q_d/R$인 직선을
얻는다. 실험으로 여러 온도의 확산계수를 측정하면 이 기울기에서 활성화에너지를
구할 수 있다.

## Arrhenius 식의 단위와 두 온도 비교

$Q_d$가 $\mathrm{J/mol}$이면 $R$도 $\mathrm{J/(mol\,K)}$ 단위를 사용하고
$T$에는 절대온도를 넣어야 한다. $Q_d$를 kJ/mol로 읽고 그대로 대입하면 지수의
크기가 천 배 달라진다. 원자당 활성화에너지를 쓰는 경우에는 $R$ 대신
Boltzmann 상수와 일관된 에너지 단위를 사용한다.

예시 물성으로 $Q_d=100\ \mathrm{kJ/mol}$, $T_1=800\ \mathrm K$,
$T_2=900\ \mathrm K$라 하면

$$
\ln\frac{D_2}{D_1}=\frac{100000}{8.314}
\left(\frac{1}{800}-\frac{1}{900}\right)\approx1.671,
\qquad D_2/D_1\approx5.31.
$$

이 값은 단위 연습을 위한 가정값이며 특정 합금의 실험 물성이 아니다.
같은 확산기구와 상이 유지되는 온도 범위에서 비교해야 한다.

# 6. 연습 문제

1. $D=10^{-9}\ \mathrm{m^2/s}$, $dc/dx=2\times10^5\ \mathrm{mol/m^4}$일 때 플럭스를 구하라.
2. 농도구배가 0이면 Fick의 제1법칙에 따른 확산 플럭스는 얼마인가?
3. 온도가 높아질 때 고체의 확산계수가 일반적으로 어떻게 변하는가?
4. $2\ \mathrm{mol}$의 A가 $0.5\ \mathrm{m^3}$에 들어 있을 때 몰농도를 구하라.
5. 이성분계에서 $x_A=0.35$이면 $x_B$를 구하라.
6. 오른쪽으로 갈수록 농도가 증가할 때 확산 방향을 말하라.

<!--
풀이와 해답:
1. J=-2.0e-4 mol/(m^2 s)이며 -x 방향이다.
2. 0이다.
3. Arrhenius 관계에 따라 증가한다.
4. c_A=n_A/V=4 mol/m^3이다.
5. x_A+x_B=1이므로 x_B=0.65이다.
6. 농도구배가 +x 방향이므로 확산은 반대인 -x 방향이다.
-->

## 관련자료와 이어 읽기

- [MIT OCW 3.205: 확산 관련 강의](https://ocw.mit.edu/courses/3-205-thermodynamics-and-kinetics-of-materials-fall-2006/pages/lecture-notes/): L2의 확산계수 구분, L4의 원자 이동기구와 온도 의존성, L6의 미세조직에 따른 확산을 심화자료로 활용한다.
- [MIT OCW 3.185: Diffusion](https://ocw.mit.edu/courses/3-185-transport-phenomena-in-materials-engineering-fall-2003/resources/chap2/): 평판·원통 확산과 경계조건을 다음 두 강의와 함께 공부한다.

- [제1강: 이동현상 개요]({% link assets/lecture_notes/2_2_transport_phenomena/transport_01_orientation.md %})
- [제9강: 정상상태 확산]({% link assets/lecture_notes/2_2_transport_phenomena/transport_09_steady_diffusion.md %})

---

[이전 강의]({% link assets/lecture_notes/2_2_transport_phenomena/transport_07_transient_heat.md %}) | [강의 목록]({% link _lectures/2_2_transport.md %}) | [다음 강의]({% link assets/lecture_notes/2_2_transport_phenomena/transport_09_steady_diffusion.md %})
