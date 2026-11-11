---
layout: page
title: 정상상태 확산
description: 평판과 원통에서의 정상 확산 및 물질전달 저항
target: 2학년 2학기
permalink:
prerequisite: 확산 기초, 적분, 정상상태 보존식
toc: false
---

**목차**

* TOC
{:toc}

# 1. 정상상태 물질수지

정지한 매질에서 화학반응이 없고 단면적이 일정한 일차원 정상 확산에서

$$\frac{dJ_A}{dx}=0$$

이므로 플럭스는 위치에 따라 일정하다. $D$가 일정하면 Fick의 법칙으로부터

$$\frac{d^2c_A}{dx^2}=0$$

을 얻는다.

# 2. 평판을 통한 확산

두께 $L$인 평판의 양면 농도가 $c_{A,1}$과 $c_{A,2}$이면

$$c_A(x)=c_{A,1}+\frac{c_{A,2}-c_{A,1}}{L}x$$

이고

$$\boxed{J_A=D\frac{c_{A,1}-c_{A,2}}{L}}$$

이다. 면적 $A$를 통과하는 몰전달률은 $\dot n_A=J_AA$이다.

## 예제

$D=10^{-10}\ \mathrm{m^2/s}$, $L=1\ \mathrm{mm}$,
$c_{A,1}-c_{A,2}=100\ \mathrm{mol/m^3}$이면

$$J_A=10^{-5}\ \mathrm{mol/(m^2\,s)}$$

이다.

# 3. 원통벽을 통한 확산

길이 $L_z$, 안쪽 반지름 $r_1$, 바깥 반지름 $r_2$인 원통벽에서 방사방향
정상 확산의 몰전달률은

$$\boxed{\dot n_A=
\frac{2\pi L_zD(c_{A,1}-c_{A,2})}{\ln(r_2/r_1)}}$$

이다. 원통에서는 전달면적 $2\pi rL_z$가 위치에 따라 변하므로 농도분포가
$r$에 대해 선형이 아니라 $\ln r$에 대해 선형이다.

## 3.1. 원통에서 일정한 것은 총 전달률이다

동심 원통면 사이에서 축적과 반응이 없으면

$$\dot n_A=2\pi rL_zJ_{A,r}=-2\pi rL_zD\frac{dc_A}{dr}$$

가 모든 $r$에서 같다. 이를 변수분리하여 적분하면

$$
\int_{c_{A,1}}^{c_A(r)}dc_A
=-\frac{\dot n_A}{2\pi L_zD}\int_{r_1}^{r}\frac{dr}{r},
$$

$$
c_A(r)=c_{A,1}+(c_{A,2}-c_{A,1})
\frac{\ln(r/r_1)}{\ln(r_2/r_1)}.
$$

따라서 $J_{A,r}=\dot n_A/(2\pi rL_z)$는 바깥쪽으로 갈수록 감소한다.
정상상태에서 플럭스가 일정하다는 말은 단면적이 일정한 경우에만 성립한다.
얇은 원통벽 $r_2-r_1\ll r_1$에서는 로그항을 전개하여 평판 근사를 회복할 수 있다.

# 4. 물질전달 저항

평판의 확산 저항을

$$R_m=\frac{L}{DA}$$

로 정의하면

$$\dot n_A=\frac{c_{A,1}-c_{A,2}}{R_m}$$

이다. 여러 층이 직렬로 놓이면 각 층의 저항을 더할 수 있다. 확산계수가 작은
층이 전체 전달속도를 크게 제한한다.

## 평판 문제 풀이 순서

1. 두 표면의 농도와 확산거리를 확인한다.
2. 농도 단위를 $\mathrm{mol/m^3}$로, 길이를 m로 통일한다.
3. 농도차의 부호로 확산 방향을 먼저 판단한다.
4. Fick의 제1법칙으로 플럭스를 계산한다.
5. 총 전달률이 필요하면 플럭스에 면적을 곱한다.

정상상태에서는 화학종이 내부에 축적되지 않으므로 반응이 없다면 모든 단면을
통과하는 총 몰전달률이 같다. 평판은 면적이 일정하여 플럭스도 일정하지만,
원통에서는 면적이 반지름에 따라 변하므로 플럭스가 일정하지 않을 수 있다.

## 두 층으로 이루어진 평판 예제

면적이 $A=1\ \mathrm{m^2}$인 두 층이 직렬로 놓여 있다. 첫 번째 층은
$L_1=1\ \mathrm{mm}$, $D_1=2\times10^{-10}\ \mathrm{m^2/s}$이고 두 번째
층은 $L_2=2\ \mathrm{mm}$, $D_2=1\times10^{-10}\ \mathrm{m^2/s}$이다.
전체 농도차가 $120\ \mathrm{mol/m^3}$이면

$$
R_1=\frac{L_1}{D_1A}=5.0\times10^6\ \mathrm{s/m^3}
$$

$$
R_2=\frac{L_2}{D_2A}=2.0\times10^7\ \mathrm{s/m^3}
$$

이다. 따라서 총 몰전달률은

$$
\dot n_A=\frac{120}{R_1+R_2}
=4.8\times10^{-6}\ \mathrm{mol/s}
$$

이다. 두 번째 층이 전체 저항의 80%를 차지하므로 전체 확산속도를 주로
제한한다. 복합재료나 산화막에서는 가장 큰 확산저항을 가진 층을 찾는 것이
중요하다.

## 복합층에서 농도는 반드시 연속인가?

위의 두 층 예제는 동일한 기준의 농도를 사용하고, 계면에서 농도가 연속이며,
계면 자체의 전달 저항과 반응이 없다고 가정한다. 이 경우 각 층의 농도강하는
$\Delta c_i=\dot n_AR_i$이고 예제에서는 각각 24, 96 $\mathrm{mol/m^3}$이다.

서로 다른 상 사이에서는 국소 평형이어도 용해도 차이로 농도가 불연속일 수
있다. 예를 들어 계면의 분배계수를 $K=c_{2,int}/c_{1,int}$라 하면

$$
\dot n_A=\frac{D_1A}{L_1}(c_{left}-c_{1,int})
=\frac{D_2A}{L_2}(Kc_{1,int}-c_{right}).
$$

이를 정리하면

$$
\dot n_A=\frac{Kc_{left}-c_{right}}{KR_1+R_2}.
$$

$K=1$일 때만 앞의 단순한 $R_1+R_2$ 식으로 돌아간다. 계면에서 연속인 것은
반응·축적이 없을 때의 총 전달률이며 농도 자체는 추가 조건이 필요하다.
산화막이나 코팅층에 모델을 적용할 때는 $D$만 비교하지 말고 용해도와 계면
조건도 확인한다.

## 정상상태가 형성되기까지

처음 균일했던 평판 양면의 농도를 갑자기 바꾸면 즉시 선형 농도분포가 되는
것은 아니다. 대표 완화시간 $L^2/D$에 비해 충분히 긴 시간이 지나고 경계농도가
유지될 때 정상해에 가까워진다. 시간이 짧으면
[제10강의 비정상 확산식](/assets/lecture_notes/2_2_transport_phenomena/transport_10_transient_diffusion.md)을
사용해야 한다. 표면 공급이 느리면 일정 표면농도 대신
$N_A=k_m(c_{bulk}-c_s)$ 같은 표면 전달조건이 필요하다. 이때
$k_m$의 단위는 $\mathrm{m/s}$이며 $D\ [\mathrm{m^2/s}]$와 구분한다.

# 5. 연습 문제

1. 평판 두께가 두 배가 되면 같은 농도차에서 확산 플럭스는 어떻게 되는가?
2. $J_A=2\times10^{-6}\ \mathrm{mol/(m^2s)}$, $A=0.5\ \mathrm{m^2}$일 때 몰전달률을 구하라.
3. 두 층의 저항이 각각 2와 3 $\mathrm{s/m^3}$이면 전체 저항을 구하라.
4. $1\ \mathrm{mm}$를 m로 바꾸시오.
5. 농도차가 두 배가 되고 다른 조건이 같다면 정상 확산 플럭스는 몇 배가 되는가?
6. 플럭스와 총 몰전달률의 차이를 단위와 함께 설명하라.

<!--
풀이와 해답:
1. 플럭스는 절반이 된다.
2. n_dot=J*A=1.0e-6 mol/s이다.
3. 직렬 저항의 합은 5 s/m^3이다.
4. 1e-3 m이다.
5. J=D*Delta c/L이므로 두 배가 된다.
6. 플럭스는 단위 면적당 전달률로 mol/(m^2 s), 총 몰전달률은 면적 전체를 통과하는 양으로 mol/s이다.
-->

## 관련자료와 이어 읽기

- [MIT OCW 3.185: Diffusion](https://ocw.mit.edu/courses/3-185-transport-phenomena-in-materials-engineering-fall-2003/resources/chap2/): PDF의 2.1절에서 평판과 원통의 정상 확산을 비교한다.

- [제4강: 열전달 기초](/assets/lecture_notes/2_2_transport_phenomena/transport_04_heat_transfer.md)
- [제10강: 비정상 확산](/assets/lecture_notes/2_2_transport_phenomena/transport_10_transient_diffusion.md)

---

[이전 강의](/assets/lecture_notes/2_2_transport_phenomena/transport_08_diffusion_basics.md) · [강의 목록](/_lectures/2_2_transport.md) · [다음 강의](/assets/lecture_notes/2_2_transport_phenomena/transport_10_transient_diffusion.md)
