---
layout: page
title: 비정상 확산
description: Fick의 제2법칙과 반무한고체 확산
target: 2학년 2학기
permalink:
prerequisite: 확산 기초, 편미분, 오차함수의 개념
toc: false
---

**목차**

* TOC
{:toc}

# 1. Fick의 제2법칙

일차원 미소 검사체적에서 화학종 A에 대한 보존식을 세우면

$$\frac{\partial c_A}{\partial t}=-\frac{\partial J_A}{\partial x}$$

이다. $J_A=-D\,\partial c_A/\partial x$이고 $D$가 일정하면

$$\boxed{\frac{\partial c_A}{\partial t}
=D\frac{\partial^2c_A}{\partial x^2}}$$

를 얻는다. 이를 Fick의 제2법칙이라고 한다.

## 1.1. 축적항과 플럭스의 발산

단면적 $A$, 두께 $dx$인 영역에 들어오는 몰수와 나가는 몰수의 차이는
$[J_A(x)-J_A(x+dx)]A$이다. 이를 체적 $A\,dx$로 나누면 단위 부피당
농도 변화율이 된다. $D$가 농도나 위치에 의존할 때는

$$
\frac{\partial c_A}{\partial t}
=\frac{\partial}{\partial x}\left(D\frac{\partial c_A}{\partial x}\right)
$$

형태를 유지해야 한다. $D$를 미분 밖으로 꺼내는 것은 일정한 경우에만 가능하다.
또한 화학반응의 순생성률 $r_A$가 있으면 우변에 $r_A$를 더하고, 유동하는
매질에서는 고정 좌표계에 대한 총플럭스 $N_A$로 보존식을 세운다.

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

## 3.1. 초기·경계조건과 무차원 변수

이 해에 대응하는 조건을 명시하면 다음과 같다.

$$
c(x,0)=c_i\ (x>0),\qquad c(0,t)=c_s\ (t>0),\qquad
c(x\to\infty,t)=c_i.
$$

$\eta=x/(2\sqrt{Dt})$는 깊이를 시간에 따라 커지는 확산길이로 나눈 값이다.
다른 시간의 농도분포도 $\eta$에 대해 그리면 하나의 곡선으로 겹친다.
표면농도 일정이라는 조건은 외부에서 충분한 용질을 계속 공급한다는 뜻이다.
얇은 막에 처음 주어진 용질만 확산하는 유한 공급원 문제에는 이 해를 쓸 수 없다.

표면 유입 플럭스와 단위 면적당 누적 유입량은 $c_s>c_i$일 때

$$
J_A(0,t)=(c_s-c_i)\sqrt{\frac{D}{\pi t}},\qquad
\frac{n_{A,\mathrm{in}}(t)}{A}=\int_0^\infty[c(x,t)-c_i]dx
=2(c_s-c_i)\sqrt{\frac{Dt}{\pi}}
$$

이다. 여기서 $n_{A,\mathrm{in}}$은 추가로 들어온 A의 **몰수**이다.
농도가 $\mathrm{mol/m^3}$이면 마지막 식의 단위는 $\mathrm{mol/m^2}$이다.
시간이 갈수록 농도구배가 완만해져 순간 유입률은 줄지만 누적 유입량은 증가한다.

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

## 4.1. 목표 농도에 도달하는 시간 역산

깊이 $x$에서 목표 농도 $c_f$를 얻고 싶다면 먼저

$$\beta=\frac{c_f-c_i}{c_s-c_i},\qquad 0<\beta<1$$

를 계산한다. $\operatorname{erfc}(\eta)=\beta$를 만족하는 $\eta$를 찾으면

$$\boxed{t=\frac{x^2}{4D\eta^2}}$$

이다. 예를 들어 앞과 같은 가정에서 $x=0.5\ \mathrm{mm}$,
$c_f=0.60\ \mathrm{wt\%}$이면 $\beta=0.5$,
$\eta\approx0.47694$이므로 $t\approx2.75\times10^4\ \mathrm s$
(약 7.63 h)이다. 이 값도 일정 $D$ 및 일정 표면농도 모델의 예측값이다.

```python
from math import erfc

beta = 0.5
lo, hi = 0.0, 1.0
while erfc(hi) > beta:
    hi *= 2.0
for _ in range(60):
    mid = (lo + hi) / 2.0
    if erfc(mid) > beta:  # erfc는 eta에 대해 감소한다.
        lo = mid
    else:
        hi = mid
eta = (lo + hi) / 2.0
D, x = 1.0e-11, 0.5e-3
print("time [h]:", x**2 / (4.0 * D * eta**2) / 3600.0)
```

이는 [수치해석의 이분법]({% link assets/lecture_notes/2_1_numerical_analysis/numerical_analysis_04_bisect.md %})을
확산 문제에 적용한 예이다. $\beta$가 0이나 1이면 위 역산의 유한한 양의 시간
해석을 별도로 살펴야 한다.

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

## 열전도에서 배운 수치해석을 확산에 적용하기

일정 $D$의 비정상 확산식을 공간 중앙차분, 시간 전진차분으로 쓰면

$$
c_i^{n+1}=c_i^n+\lambda(c_{i-1}^n-2c_i^n+c_{i+1}^n),\qquad
\lambda=\frac{D\Delta t}{\Delta x^2}.
$$

여기서 아래첨자 $i$는 위치, 위첨자 $n$은 시간단계이다. 이 **일차원 일정 $D$,
균일격자의 명시적 차분법**은 $0\le\lambda\le1/2$에서 안정하다.
이때 새 농도가 이전 단계의 세 농도의 음이 아닌 가중평균으로 표현된다.
공간격자를 절반으로 줄이면 같은 $\lambda$를 유지하기 위해 시간간격은
1/4로 줄여야 한다. 이 조건은 모든 수치해법의 보편적인 시간간격 제한이 아니며,
암시적 방법이나 다른 차원에서는 별도로 분석해야 한다.

계산할 때 매 시간단계마다 경계조건을 적용하고, 반무한 해와 비교하려면 계산
영역을 충분히 길게 잡아 먼 경계의 영향을 줄인다. 안정한 계산이라도 시간·공간
간격이 너무 크면 정확하지 않을 수 있으므로 격자와 시간간격을 함께 줄여
농도분포 및 총 유입량이 수렴하는지 확인한다.

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

## 관련자료와 이어 읽기

- [MIT OCW 3.205: 확산·열방정식 해법](https://ocw.mit.edu/courses/3-205-thermodynamics-and-kinetics-of-materials-fall-2006/pages/lecture-notes/): L3의 Fick 제2법칙 해법을 심화 학습에 활용한다.
- [Python 공식 문서: math.erf와 math.erfc](https://docs.python.org/3/library/math.html#math.erf): 예제에서 사용한 오차함수의 정의와 함수 사용법을 확인한다.

- [제6강: 열전도의 유한차분해석]({% link assets/lecture_notes/2_2_transport_phenomena/transport_06_heat_fdm.md %})
- [제7강: 비정상 열전도]({% link assets/lecture_notes/2_2_transport_phenomena/transport_07_transient_heat.md %})

[이전 강의]({% link assets/lecture_notes/2_2_transport_phenomena/transport_09_steady_diffusion.md %}) | [강의 목록]({% link _lectures/2_2_transport.md %})
