---
layout: distill
title: 압연의 기초
description: 압연공정의 기하학, 변형, 마찰과 하중
target: 3학년 1학기
permalink:
featured: true
prerequisite: 응력과 변형률, 변형경화, 소성일
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
- [2. 압연이란 무엇인가?](#2-압연이란-무엇인가)
- [3. 압연공정의 기본 기하학](#3-압연공정의-기본-기하학)
- [4. 체적 일정과 압연속도](#4-체적-일정과-압연속도)
- [5. 압연변형률](#5-압연변형률)
- [6. 마찰과 롤 바이트](#6-마찰과-롤-바이트)
  - [\*\* 롤의 기하학적 관계\*\*](#-롤의-기하학적-관계)
  - [\*\* 작은 물림각에 대한 근사\*\*](#-작은-물림각에-대한-근사)
  - [\*\* 물림 조건 적용\*\*](#-물림-조건-적용)
- [7. 중립점과 마찰 방향](#7-중립점과-마찰-방향)
- [8. 압연하중, 토크와 동력](#8-압연하중-토크와-동력)
  - [8.1. 압연하중: 접촉압력을 더한 힘](#81-압연하중-접촉압력을-더한-힘)
  - [8.2. 토크: 힘과 유효 모멘트 팔](#82-토크-힘과-유효-모멘트-팔)
  - [8.3. 동력: 단위 시간당 회전하는 데 필요한 일](#83-동력-단위-시간당-회전하는-데-필요한-일)
- [9. 열간압연과 냉간압연](#9-열간압연과-냉간압연)
- [10. 압연 결함과 공정 설계](#10-압연-결함과-공정-설계)
- [11. Python 실습](#11-python-실습)
  - [11.1. 압연 기본량 계산](#111-압연-기본량-계산)
  - [11.2. 마찰계수와 최대 압하량](#112-마찰계수와-최대-압하량)
  - [11.3. 압연하중과 동력 추정](#113-압연하중과-동력-추정)
- [12. 핵심 정리](#12-핵심-정리)
- [13. 연습 문제](#13-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)
  - [문제 7](#문제-7)
  - [문제 8](#문제-8)

# 1. 학습 목표와 수업 구성

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 압연(rolling)의 기본 원리를 설명할 수 있다.
- 압하량, 압하율과 접촉길이를 계산할 수 있다.
- 체적 일정 조건으로 소재의 입구 및 출구 속도를 연결할 수 있다.
- 판재 압연의 두께방향 진변형률과 동등변형률을 계산할 수 있다.
- 마찰이 소재의 물림과 중립점에 미치는 영향을 설명할 수 있다.
- 간단한 근사식을 이용해 압연하중, 토크와 동력을 추정할 수 있다.
- 열간압연과 냉간압연의 차이를 설명할 수 있다.

# 2. 압연이란 무엇인가?

압연은 회전하는 두 롤(roll) 사이에 소재를 통과시켜 두께를 감소시키고 원하는 단면
형상을 만드는 소성가공 공정이다.

판재의 평압연(flat rolling)에서는 다음 과정이 일어난다.

1. 롤과 소재 사이의 마찰이 소재를 롤 사이로 끌어들인다.
2. 롤의 압축력으로 소재의 두께가 감소한다.
3. 소성변형으로 길이가 증가한다.
4. 폭 변화가 작다면 소재의 폭은 거의 일정하다고 근사할 수 있다.

압연으로 후판, 박판, 봉재, 레일 등 다양한 제품을 생산한다. 이번 강의에서는
두께만 감소하는 가장 단순한 **평압연**을 중심으로 다룬다.

# 3. 압연공정의 기본 기하학

![평압연의 롤 회전, 두께 감소, 투영 접촉길이와 중립점 전후의 마찰 방향](/assets/img/lecture_notes/rolling/rolling_geometry.png)

위 그림에서 소재는 왼쪽에서 오른쪽으로 이동한다. 위아래 롤은 서로 반대로 회전하며
(위: 반 시계방향; 아래: 시계 방향),
소재 두께는 $h_0$에서 $h_f$로 감소한다. $L$은 접촉호 자체의 길이가 아니라
압연 방향으로 투영한 접촉길이이다. 오른쪽 확대 개념도에서 빨간 화살표는
**롤이 소재에 가하는 마찰력**의 방향이다.

<!-- [TikZ 소스 다운로드](/assets/tikz/metal_plasticity/rolling_geometry.tex) ·
[벡터 PDF 다운로드](/output/pdf/rolling_geometry.pdf) -->

압연 전후의 두께를 각각 $h_0$와 $h_f$라 하자. 한 패스(pass)에서 감소한 두께를
압하량이라 한다.

$$
\boxed{\Delta h=h_0-h_f}
$$

초기 두께에 대한 감소 비율을 압하율(reduction)이라 한다.

$$
\boxed{r=-\frac{h_f-h_0}{h_0}}
$$

백분율로 나타내려면 $r$에 100을 곱한다. 예를 들어 두께가 10 mm에서 8 mm로
감소하면

$$
\Delta h=2\ \mathrm{mm},
\qquad
r=\frac{2}{10}=0.20=20\%
$$

이다.

롤 반지름이 $R$이고 압하량이 롤 반지름보다 매우 작으면 롤과 소재의 투영 접촉길이
$L$을 다음과 같이 근사할 수 있다.[^rolling-contact-length]

$$
\boxed{L\approx\sqrt{R\Delta h}}
$$

예를 들어 $R=200$ mm, $\Delta h=2$ mm이면

$$
L\approx\sqrt{200\times2}=20\ \mathrm{mm}
$$

이다. 롤 반지름이나 압하량이 증가하면 접촉길이도 증가한다.

# 4. 체적 일정과 압연속도

금속의 소성변형 중 밀도 변화는 매우 작으므로 체적이 일정하다고 근사한다. 정상상태에서
단위 시간에 입구와 출구를 통과하는 소재의 체적은 같다.

$$
w_0h_0v_0=w_fh_fv_f
$$

여기서 $w$는 폭, $h$는 두께, $v$는 소재 속도이며 아래첨자 0과 $f$는 각각 입구와
출구를 뜻한다. 폭 변화가 작아 $w_0\approx w_f$이면

$$
\boxed{h_0v_0=h_fv_f}
$$

이다. 따라서 두께가 감소하면 출구 소재 속도는 입구 속도보다 커진다.

예를 들어 $h_0=10$ mm, $h_f=8$ mm이고 $v_0=1.0$ m/s이면

$$
v_f=\frac{h_0}{h_f}v_0
=\frac{10}{8}(1.0)
=1.25\ \mathrm{m/s}
$$

이다.

# 5. 압연변형률

두께방향 진변형률은

$$
\varepsilon_h=\ln\left(\frac{h_f}{h_0}\right)
$$

이다. 두께가 감소하므로 이 값은 음수다. 압연 변형의 크기를 표현할 때는 다음과 같이
양의 압축변형률을 사용할 수 있다.

$$
\boxed{\varepsilon_c=\ln\left(\frac{h_0}{h_f}\right)}
$$

폭방향 변형이 0인 평면변형(plane strain) 압연과 체적 일정 조건을 가정하면

$$
\varepsilon_1=\ln\left(\frac{h_0}{h_f}\right),
\qquad
\varepsilon_2=0,
\qquad
\varepsilon_3=-\varepsilon_1
$$

로 나타낼 수 있다. 이때 [von Mises 동등변형률]({% link assets/lecture_notes/3_1_metal_plasticity/metal_plasticity_plastic_work.md %})은

$$
\boxed{
\bar\varepsilon
=\frac{2}{\sqrt{3}}
\ln\left(\frac{h_0}{h_f}\right)
}
$$

이다.

10 mm에서 8 mm로 압연하면

$$
\varepsilon_c=\ln(10/8)\approx0.223,
\qquad
\bar\varepsilon\approx0.258
$$

이다. 이 동등변형률을 변형경화식에 사용하면 압연 중 유동응력의 변화를 근사할 수 있다.

# 6. 마찰과 롤 바이트

롤과 소재가 접촉하는 영역을 롤 바이트(roll bite)라고 한다. 소재가 롤 사이로 들어가려면
마찰력이 소재를 안쪽으로 끌어당길 수 있어야 한다.

![대칭면 위쪽의 압연 소재 형상과 물림점에서의 수직항력 및 마찰력 성분](/assets/img/lecture_notes/rolling/rolling_bite_force.png)

그림 (a)는 위아래 대칭을 이용하여 위쪽 롤과 소재의 윗부분만 나타낸 것이다.
대칭면에서 소재 표면까지의 거리는 입구에서 $h_0/2$, 출구에서 $h_f/2$이다.
물림각 $\alpha$는 롤 중심에서 접촉 시작점 $P$로 향하는 반경과 수직선 사이의 각이다.

그림 (b)는 입구 접촉점 $P$에서 **롤이 소재에 가하는 힘**을 확대하여 나타낸 것이다.
수직항력 $N$의 수평 성분 $N\sin\alpha$는 소재를 입구 쪽으로 밀어내고,
마찰력 $\mu N$의 수평 성분 $\mu N\cos\alpha$는 소재를 롤 사이로 끌어들인다.
외부에서 소재를 밀어 넣는 힘이나 장력이 없을 때, 스스로 물려 들어가기 위한 한계 조건은

$$
\mu N\cos\alpha\geq N\sin\alpha
$$

이다. 아래쪽 접촉점도 대칭이므로 수평 성분은 같은 방향으로 작용한다.
양쪽 롤을 함께 고려해도 두 항에 동일하게 2가 곱해져 물림 조건은 변하지 않는다.

롤 바이트 입구의 물림각(angle of bite)을 $\alpha$, 마찰계수를 $\mu$라 하면 단순한
Coulomb 마찰 조건에서 물림 조건은

$$
\boxed{\tan\alpha\leq\mu}
$$

이다. 이 조건으로부터 최대 압하량을 다음과 같이 구할 수 있다.

## ** 롤의 기하학적 관계**

압하량은 소재의 두께 감소량 $\Delta h=h_0-h_f$이다. 위 그림의 위쪽 절반을 보면,
롤 중심에서 출구 표면까지의 수직 거리는 $R$, 입구 접촉점 $P$까지의 수직 거리는
$R\cos\alpha$이다. 두 거리의 차이는 두께 감소량의 절반이므로

$$
\frac{\Delta h}{2}=R-R\cos\alpha
\quad\Longrightarrow\quad
\boxed{\Delta h=2R(1-\cos\alpha)}
$$

이다. 계수 2는 소재의 위아래가 대칭으로 변형되는 것을 반영한다.

## ** 작은 물림각에 대한 근사**

물림각이 충분히 작으면, $\alpha$를 라디안으로 나타낼 때

$$
\cos\alpha\approx1-\frac{\alpha^2}{2}
$$

이므로

$$
\Delta h\approx2R\left[1-\left(1-\frac{\alpha^2}{2}\right)\right]
=R\alpha^2
$$

이다.

## ** 물림 조건 적용**

작은 각도에서는 $\tan\alpha\approx\alpha$이므로 물림 조건은 근사적으로
$\alpha\lesssim\mu$가 된다. 물림 한계에서 $\alpha_{max}\approx\mu$를 대입하면

$$
\boxed{\Delta h_{max}\approx\mu^2R}
$$

을 얻는다. 즉, 마찰계수가 같다면 롤 반경이 클수록 더 큰 압하량으로 물릴 수 있다.

예를 들어 $R=200$ mm, $\mu=0.10$이면

$$
\Delta h_{max}\approx(0.10)^2(200)=2.0\ \mathrm{mm}
$$

이다. 작은 각도 근사를 사용하지 않고 $\alpha_{max}=\tan^{-1}\mu$를
기하학적 관계에 직접 대입하면

$$
\Delta h_{max}
=2R\left(1-\frac{1}{\sqrt{1+\mu^2}}\right)
$$

을 얻는다. 같은 예에서는 약 $1.985$ mm로, 근사값 $2.0$ mm와 가깝다.

여기서 구한 값은 강체 롤, Coulomb 마찰, 외부 밀어넣기 힘이나 장력이 없는
대칭 압연을 가정한 **물림 한계**이다. 실제 가능한 압하량은 압연기의 하중과 동력
한계에도 영향을 받는다.

마찰이 너무 작으면 소재가 롤 사이로 들어가지 못한다. 반대로 마찰이 지나치게 크면
압연하중과 동력 소모가 증가하고 표면 손상이 생길 수 있다. 따라서 마찰은 단순히 작을수록
좋거나 클수록 좋은 값이 아니다.

# 7. 중립점과 마찰 방향

롤 표면의 선속도를 $v_R$이라 하자. 일반적으로 소재는 입구에서 롤 표면보다 느리고,
출구에서는 롤 표면보다 빠르다.

$$
v_0<v_R<v_f
$$

롤 바이트 안에는 소재 속도와 롤 표면 속도가 같아지는 위치가 존재한다. 이를 중립점
(neutral point) 또는 무미끄럼점(no-slip point)이라 한다.

- 입구에서 중립점까지: 롤 표면이 소재보다 빠르므로 마찰력이 소재를 출구 방향으로 민다.
- 중립점에서 출구까지: 소재가 롤 표면보다 빠르므로 소재에 작용하는 마찰 방향이 입구
  방향으로 바뀐다.

즉, 롤 바이트 전체에서 마찰 방향이 같은 것은 아니다. 마찰 방향은 중립점에서 바뀐다.

출구 소재 속도와 롤 표면 속도의 차이를 전방미끄럼(forward slip)으로 나타낼 수 있다.

$$
s_f=\frac{v_f-v_R}{v_R}
$$

일반적인 압연 조건에서는 $v_f>v_R$이므로 전방미끄럼은 양수다.

# 8. 압연하중, 토크와 동력

압연하중은 롤이 소재를 누르는 힘, 토크는 롤을 돌리는 데 필요한 회전 모멘트,
동력은 단위 시간에 공급해야 하는 에너지이다. 아래에서 $F$는 **한쪽 롤에 작용하는
롤 분리력의 크기**, $T$는 **롤 하나의 토크**를 뜻한다. 위아래 롤에 각각 $F$가
작용한다고 해서 통상적인 압연하중을 $2F$로 표시하지는 않는다.

## 8.1. 압연하중: 접촉압력을 더한 힘

![상부 롤에 작용하는 접촉압력과 압력 분포의 적분으로 구하는 압연하중](/assets/img/lecture_notes/rolling/rolling_load.png)

그림 (a)의 빨간 화살표는 소재가 위쪽 롤에 가하는 수직항력을 나타낸다.
소재에는 이와 반대 방향의 힘이 작용한다. 위쪽으로 표시한 $F$는 롤 분리력의
방향을 나타내며, 그 화살표 위치가 토크의 모멘트 팔을 뜻하지는 않는다.
그림 (b)에서 작은 띠의 면적 $p(x)dx$에 소재 폭 $w$를 곱하면 미소 힘 $dF$가 된다.
전체 곡선 아래 면적에 $w$를 곱하여 압연하중을 추정한다. 압력 분포의 모양은 개념도이다.

폭 방향으로 압력이 일정하다고 가정하고, 투영 접촉구간을 $0\leq x\leq L$로 잡자.
미소 접촉면적을 $dA$, 그 위치의 접촉면 기울기를 $\theta$라 하면
$dA\cos\theta=w\,dx$이다. 수직항력의 수직 성분은

$$
dF=p(x)dA\cos\theta=p(x)w\,dx
$$

이다. 마찰력의 수직 성분을 무시하는 작은 접촉각 근사에서 이를 합하면

$$
F\approx w\int_0^L p(x)\,dx,
\qquad
\bar p=\frac{1}{L}\int_0^L p(x)\,dx
$$

이므로 아래 식을 얻는다. 즉, 압연하중은 대략 **평균 압력 × 투영 접촉면적**이다.

롤과 소재 사이의 압력은 접촉 위치에 따라 달라진다. 기초적인 공정 추정에서는 평균
압연압력 $\bar p$를 사용하여 롤 분리력(rolling force)을 다음과 같이 근사할 수 있다.

$$
\boxed{F\approx\bar p\,wL}
$$

여기서 $w$는 소재 폭이고 $L\approx\sqrt{R\Delta h}$는 투영 접촉길이다.

예를 들어 $\bar p=300$ MPa, $w=500$ mm, $L=20$ mm이면

$$
F\approx300\times500\times20
=3.0\times10^6\ \mathrm{N}
=3.0\ \mathrm{MN}
$$

이다. $1\ \mathrm{MPa}=1\ \mathrm{N/mm^2}$를 사용하였다.

## 8.2. 토크: 힘과 유효 모멘트 팔

힘의 회전 효과는 힘의 크기에 회전 중심에서 힘의 작용선까지의 수직 거리를 곱하여
계산한다. 압연에서는 접촉력 분포의 회전 효과를 **유효 모멘트 팔** $a$로 표현하여

$$
T\approx Fa
$$

로 추정한다. 기초 계산에서는 $a\approx L/2$라고 가정하므로

$$
\boxed{T\approx\frac{FL}{2}}
$$

이다. $L/2$는 보편적인 정확한 값이 아니라 접촉력 분포를 단순화한 근사이다.
실제 유효 모멘트 팔은 마찰, 중립점, 압력 분포와 장력 등에 따라 달라진다.

여기서 주의할 점은 원형 롤 표면의 **수직항력 자체는 롤 중심을 향하므로 중심에 대한
토크가 0**이라는 것이다. 실제 접촉 토크는 접선 방향의 마찰력이 만든다.
마찰응력 $\tau$에 의한 미소 힘이 $\tau dA$이면 미소 토크는 $R\tau dA$이다.
따라서 접선 방향의 부호를 일관되게 정하여

$$
T_{\mathrm{contact}}=R\int_A\tau\,dA
$$

로 계산하며, 정상 회전에 필요한 구동 토크는 이 저항 토크를 상쇄한다.
중립점 전후에서는 마찰 방향이 반대이므로 부호를 고려해야 한다.
$T\approx FL/2$는 이 상세 계산을 대신하는 공학적 추정식이다.

앞 예의 $F=3.0\times10^6$ N, $L=20$ mm $=0.020$ m를 사용하면

$$
T\approx\frac{(3.0\times10^6)(0.020)}{2}
=3.0\times10^4\ \mathrm{N\,m}
=30\ \mathrm{kN\,m}
$$

이다. 이는 롤 하나에 필요한 토크이다.

## 8.3. 동력: 단위 시간당 회전하는 데 필요한 일

롤이 작은 각도 $d\phi$만큼 회전할 때 토크가 하는 일은 $dW=T\,d\phi$이다.
이를 시간으로 나누면 롤 하나의 동력은

$$
P_{\mathrm{roll}}=\frac{dW}{dt}
=T\frac{d\phi}{dt}=T\omega
$$

이다. 두 롤이 동일한 토크와 각속도 크기로 구동되면 전체 동력은

$$
\boxed{P\approx2T\omega}
$$

이다. 토크 계산에서 $F$가 N이면 $L$은 반드시 m로 바꾸어야 $T$가 N·m로 계산된다.

두 롤은 서로 반대 방향으로 회전하지만, 각각 구동 토크와 회전 방향이 같아 소비 동력은
더해진다. $T\approx FL/2$를 대입하면 $P\approx FL\omega$로도 쓸 수 있다.

회전수가 $n$ rpm이면 1회전은 $2\pi$ rad, 1분은 60초이므로

$$
\omega=\frac{2\pi n}{60},
\qquad
P\approx2T\frac{2\pi n}{60}
$$

이다. 앞 예에서 $n=60$ rpm이면 $\omega=2\pi$ rad/s이므로

$$
P\approx2(3.0\times10^4)(2\pi)
\approx3.77\times10^5\ \mathrm{W}=377\ \mathrm{kW}
$$

이다. 이 값은 두 롤에 공급하는 기계적 동력이다. 전달 효율이 $\eta$이면 필요한
입력 동력은 $P_{\mathrm{in}}=P/\eta$로 추정한다. 예를 들어 $\eta=0.90$이면
약 $419$ kW가 필요하다.

실제 평균 압연압력은 재료의 유동응력뿐 아니라 마찰, 롤 반지름, 두께, 전후방 장력과
변형경화의 영향을 받는다. 따라서 위 식은 개념 이해와 초기 추정을 위한 근사식이다.

참고: [NPTEL 압연 토크와 동력 설명(강의 26 정정 안내)](https://onlinecourses-archive.nptel.ac.in/noc17_me21/announcements).
회전수를 rpm으로 사용할 때는 위와 같이 반드시 60으로 나누어 초 단위로 환산한다.

# 9. 열간압연과 냉간압연

재료의 재결정온도를 기준으로 열간압연과 냉간압연을 구분할 수 있다.

| 구분 | 열간압연 | 냉간압연 |
|---|---|---|
| 가공온도 | 재결정온도보다 높음 | 재결정온도보다 낮음 |
| 변형저항 | 비교적 작음 | 비교적 큼 |
| 큰 압하 | 비교적 쉬움 | 제한적 |
| 변형경화 | 회복·재결정으로 감소 가능 | 뚜렷하게 축적됨 |
| 표면 상태 | 산화와 스케일 발생 가능 | 일반적으로 우수함 |
| 치수 정밀도 | 비교적 낮음 | 일반적으로 높음 |
| 가공 후 성질 | 미세조직 변화가 큼 | 강도·경도 증가, 연성 감소 |

열간과 냉간이라는 말은 단순히 만졌을 때 뜨겁거나 차갑다는 의미가 아니라 재결정온도에
대한 상대적인 가공온도를 뜻한다.

# 10. 압연 결함과 공정 설계

압연 중 폭방향과 두께방향으로 변형이 균일하지 않으면 형상 및 내부 결함이 발생할 수
있다.

- **물결 모양 가장자리(wavy edge)**: 가장자리가 중앙보다 더 길게 늘어난 경우
- **중앙 좌굴(center buckle)**: 중앙부가 가장자리보다 더 길게 늘어난 경우
- **가장자리 균열(edge crack)**: 가장자리의 낮은 연성이나 과도한 인장변형으로 발생
- **중앙부 균열(center crack)**: 내부의 인장응력과 재료 건전성의 영향으로 발생
- **악어입 균열(alligatoring)**: 소재가 두께방향으로 벌어지는 결함

롤의 탄성변형, 소재 폭 방향의 불균일한 유동과 온도 분포가 판 형상에 영향을 준다.
실제 공정에서는 롤 크라운, 롤 벤딩, 장력, 냉각과 패스 스케줄을 조절하여 두께와 평탄도를
관리한다.

# 11. Python 실습

## 11.1. 압연 기본량 계산

초기 두께 10 mm인 폭 500 mm 판재를 반지름 200 mm인 롤로 최종 두께 8 mm까지
압연한다고 하자.

~~~python
import numpy as np


initial_thickness = 10.0  # mm
final_thickness = 8.0     # mm
roll_radius = 200.0       # mm
entry_speed = 1.0         # m/s

draft = initial_thickness - final_thickness
reduction = draft / initial_thickness
contact_length = np.sqrt(roll_radius * draft)
exit_speed = initial_thickness / final_thickness * entry_speed
compressive_strain = np.log(initial_thickness / final_thickness)
equivalent_strain = 2.0 / np.sqrt(3.0) * compressive_strain

print(f"Draft: {draft:.2f} mm")
print(f"Reduction: {100 * reduction:.1f}%")
print(f"Contact length: {contact_length:.2f} mm")
print(f"Exit speed: {exit_speed:.2f} m/s")
print(f"Equivalent strain: {equivalent_strain:.3f}")
~~~

## 11.2. 마찰계수와 최대 압하량

롤 반지름이 일정할 때 마찰계수에 따라 가능한 최대 압하량이 어떻게 달라지는지 그려
보자.

~~~python
import matplotlib.pyplot as plt


friction_coefficient = np.linspace(0.02, 0.20, 100)
maximum_draft = friction_coefficient**2 * roll_radius

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(friction_coefficient, maximum_draft)
ax.set_xlabel("Friction coefficient")
ax.set_ylabel("Maximum draft (mm)")
ax.set_title("Biting Limit")
ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
~~~

이 단순 모델에서는 마찰계수가 두 배가 되면 최대 압하량은 네 배가 된다. 하지만 실제
공정에서는 마찰 증가에 따른 하중과 표면 품질의 변화도 함께 고려해야 한다.

## 11.3. 압연하중과 동력 추정

평균 압연압력이 300 MPa, 판 폭이 500 mm, 롤 회전속도가 60 rpm이라고 하자.

~~~python
mean_pressure = 300.0  # MPa = N/mm^2
strip_width = 500.0    # mm
roll_speed_rpm = 60.0

rolling_force = mean_pressure * strip_width * contact_length
contact_length_m = contact_length / 1000.0
torque_per_roll = rolling_force * contact_length_m / 2.0
angular_speed = 2.0 * np.pi * roll_speed_rpm / 60.0
total_power = 2.0 * torque_per_roll * angular_speed

print(f"Rolling force: {rolling_force / 1e6:.2f} MN")
print(f"Torque per roll: {torque_per_roll / 1000:.1f} kN m")
print(f"Total power: {total_power / 1000:.1f} kW")
~~~

계산 결과는 단순 근사에 기반한다. 특히 정확한 평균 압연압력을 얻으려면 재료거동과
마찰을 포함한 압연이론이 필요하다.

# 12. 핵심 정리

- 압하량은 $\Delta h=h_0-h_f$, 압하율은 $r=\Delta h/h_0$이다.
- 투영 접촉길이는 $L\approx\sqrt{R\Delta h}$로 근사할 수 있다.
- 폭 변화가 작으면 체적 일정 조건은 $h_0v_0=h_fv_f$이다.
- 평면변형 압연의 동등변형률은
  $\bar\varepsilon=(2/\sqrt{3})\ln(h_0/h_f)$이다.
- 물림 조건은 $\tan\alpha\leq\mu$이고 최대 압하량은
  $\Delta h_{max}\approx\mu^2R$로 근사한다.
- 소재와 롤의 속도가 같은 중립점에서 마찰 방향이 바뀐다.
- 압연하중은 $F\approx\bar p wL$로 근사할 수 있다.
- 냉간압연에서는 변형경화가 축적되고, 열간압연에서는 회복과 재결정이 일어날 수 있다.

# 13. 연습 문제

## 문제 1

두께가 12 mm에서 9 mm로 감소하였다. 압하량과 압하율을 구하시오.

<!--
풀이와 해답:
압하량은 12 - 9 = 3 mm이다. 압하율은 3 / 12 = 0.25, 즉 25%이다.
-->

## 문제 2

롤 반지름이 100 mm이고 압하량이 4 mm일 때 투영 접촉길이를 구하시오.

<!--
풀이와 해답:
L = sqrt(100 x 4) = 20 mm이다.
-->

## 문제 3

폭 변화가 없는 압연에서 $h_0=6$ mm, $h_f=4$ mm, $v_0=2$ m/s이다. 출구 속도를
구하시오.

<!--
풀이와 해답:
h0 v0 = hf vf이므로 vf = (6 / 4) x 2 = 3 m/s이다.
-->

## 문제 4

두께가 10 mm에서 8 mm로 감소할 때 양의 두께 압축진변형률을 구하시오.

<!--
풀이와 해답:
epsilon_c = ln(10 / 8) = 약 0.223이다.
-->

## 문제 5

롤 반지름이 250 mm이고 마찰계수가 0.10일 때 최대 압하량을 추정하시오.

<!--
풀이와 해답:
Delta h_max = mu^2 R = 0.10^2 x 250 = 2.5 mm이다.
-->

## 문제 6

롤 바이트에서 마찰 방향이 바뀌는 위치를 무엇이라 하는가?

<!--
풀이와 해답:
중립점 또는 무미끄럼점이라 한다.
-->

## 문제 7

평균 압연압력 200 MPa, 폭 300 mm, 접촉길이 15 mm일 때 압연하중을 구하시오.

<!--
풀이와 해답:
F = 200 x 300 x 15 = 900000 N = 0.9 MN이다.
-->

## 문제 8

냉간압연 후 금속의 강도와 연성은 일반적으로 어떻게 변하는가?

<!--
풀이와 해답:
변형경화 때문에 강도는 증가하고 연성은 감소한다.
-->

[^rolling-contact-length]: 위쪽과 아래쪽 롤이 각각 전체 압하량의 절반인
    $\Delta h/2$만큼 소재를 누른다고 생각하자. 롤 중심, 접촉 시작점과 출구점을
    연결하면 빗변이 $R$, 두 직각변이 $L$과 $R-\Delta h/2$인 직각삼각형을 얻는다.
    따라서 피타고라스 정리에 의해

    $$
    R^2=L^2+\left(R-\frac{\Delta h}{2}\right)^2
    $$

    이고, 이를 정리하면 정확한 투영 접촉길이는

    $$
    L=\sqrt{R\Delta h-\frac{(\Delta h)^2}{4}}
    $$

    이다. 일반적인 압연에서는 $\Delta h\ll R$이므로
    $(\Delta h)^2/4$가 $R\Delta h$보다 매우 작다. 이 항을 무시하면
    $L\approx\sqrt{R\Delta h}$를 얻는다. 예를 들어 $R=200$ mm,
    $\Delta h=2$ mm이면 정확한 값은 약 $19.975$ mm이고 근삿값은 $20.000$ mm이다.
