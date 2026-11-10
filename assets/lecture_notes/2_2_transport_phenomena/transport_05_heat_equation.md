---
layout: page
title: 열전도 방정식
description: 에너지 수지로부터 열전도 지배방정식 유도하기
target: 2학년 2학기
permalink:
prerequisite: 열전달 기초, 편미분, 보존식
toc: false
---

**목차**

* TOC
{:toc}

# 1. 에너지 수지

두께 $dx$, 면적 $A$인 고체 요소에 에너지 보존을 적용한다.

$$q_x''A-q_{x+dx}''A+\dot q'''A\,dx
=\rho c_pA\,dx\frac{\partial T}{\partial t}$$

$\dot q'''$은 단위 부피당 열생성률 $\mathrm{W/m^3}$이다.

## 1.1. 표면 유입량에서 단위 부피당 축적량으로

양쪽 면의 열유속 차이를 $dx$로 나누면

$$
\frac{q_x''-q_{x+dx}''}{dx}+\dot q'''
=\rho c_p\frac{\partial T}{\partial t}.
$$

$dx\to0$일 때 첫 항은 $-\partial q_x''/\partial x$가 된다. 여기에
$q_x''=-k\partial T/\partial x$를 대입하므로 우변의 전도항에 양의 부호가
나타난다. 모든 항의 단위는 $\mathrm{W/m^3}$이다.

이 수지는 정지한 고체에서 기계적 일, 상변태 잠열 등을 별도로 무시하고
열적 저장량 변화를 $\rho c_p\,dT$로 근사한 것이다. 유동하는 유체에서는
이류에 의한 에너지 전달도 추가해야 한다.

# 2. 열전도 방정식

푸리에 법칙을 대입하면

$$\boxed{\rho c_p\frac{\partial T}{\partial t}
=\frac{\partial}{\partial x}\left(k\frac{\partial T}{\partial x}\right)
+\dot q'''}$$

를 얻는다. $k$가 일정하면

$$\frac{\partial T}{\partial t}=\alpha\frac{\partial^2T}{\partial x^2}
+\frac{\dot q'''}{\rho c_p},\qquad \alpha=\frac{k}{\rho c_p}$$

이다. 열확산계수 $\alpha$의 단위는 $\mathrm{m^2/s}$이다.

# 3. 단순화된 경우

| 조건 | 지배방정식 |
|---|---|
| 정상상태, 열생성 없음 | $d^2T/dx^2=0$ |
| 정상상태, 일정한 열생성 | $k\,d^2T/dx^2+\dot q'''=0$ |
| 비정상상태, 열생성 없음 | $\partial T/\partial t=\alpha\,\partial^2T/\partial x^2$ |

# 4. 경계조건과 초기조건

- 지정온도: $T(0,t)=T_0$
- 지정 열유속: $-k\,\partial T/\partial n=q_0''$
- 단열 또는 대칭면: $\partial T/\partial n=0$
- 대류 경계: $-k\,\partial T/\partial n=h(T_s-T_\infty)$
- 초기조건: $T(x,0)=T_i(x)$

## 4.1. 법선 방향과 경계조건의 부호

구간이 $0\le x\le L$이면 바깥쪽 법선은 왼쪽에서 $-\boldsymbol e_x$,
오른쪽에서 $+\boldsymbol e_x$이다. 따라서 **밖으로 나가는** 열유속은

$$
q_{out}''(0)=+k\left.\frac{\partial T}{\partial x}\right|_0,
\qquad
q_{out}''(L)=-k\left.\frac{\partial T}{\partial x}\right|_L.
$$

양쪽 표면 모두 $q_{out}''=h(T_s-T_\infty)$로 쓸 수 있지만, 이를 $x$ 미분으로
옮길 때는 부호가 달라진다. 지정 열유속도 안으로 들어오는 양인지 밖으로
나가는 양인지 먼저 정해야 한다.

공간에 대한 이계 미분방정식에는 일차원 구간의 양 끝에서 각각 하나씩
경계조건이 필요하다. 시간에 대한 일계 미분이 추가된 비정상 문제에는
초기 온도분포도 필요하다. 정상상태의 양 끝을 모두 단열로 두면서 양의
열생성을 지정하면 에너지의 출구가 없어 정상해가 존재하지 않는다.[^insulated]

[^insulated]: 열생성까지 0인 완전 단열 정상 문제에서는 임의의 일정 온도가 해가 된다. 총 에너지나 초기상태 같은 추가 정보가 없으면 그 상수값은 정해지지 않는다.

# 5. 내부 열생성 예제

두께 $2L$인 평판에서 열이 균일하게 생성되고 양면 온도가 $T_s$이면

$$\boxed{T(x)=T_s+\frac{\dot q'''}{2k}(L^2-x^2)}$$

이다. 최대온도는 대칭면 $x=0$에서 나타난다.

$$T_{max}=T_s+\frac{\dot q'''L^2}{2k}$$

## 방정식의 각 항이 뜻하는 것

$$
\underbrace{\rho c_p\frac{\partial T}{\partial t}}_{\text{에너지 축적}}
=
\underbrace{k\frac{\partial^2T}{\partial x^2}}_{\text{전도에 의한 순입력}}
+
\underbrace{\dot q'''}_{\text{내부 열생성}}
$$

온도구배 $\partial T/\partial x$는 열유속을 결정하고, 온도분포의 곡률
$\partial^2T/\partial x^2$은 작은 검사체적에 들어오는 열과 나가는 열의 차이를
결정한다. 정상상태라고 해서 두 항이 각각 0일 필요는 없다. 전도에 의한
순출력과 내부 열생성이 서로 같으면 온도는 시간에 따라 변하지 않는다.

## 다차원 열전도 방정식

직교좌표계의 3차원 열전도 방정식은 $k$가 일정할 때

$$
\rho c_p\frac{\partial T}{\partial t}
=k\left(\frac{\partial^2T}{\partial x^2}
+\frac{\partial^2T}{\partial y^2}
+\frac{\partial^2T}{\partial z^2}\right)+\dot q'''
$$

이다. 괄호 안은 온도의 Laplacian $\nabla^2T$이다. 판이 넓고 두께가 얇으며
양면 온도가 균일하다면 두께 방향 변화만 남겨 일차원 문제로 근사할 수 있다.

모서리, 국부적인 열원, 재료가 급격히 바뀌는 영역에서는 둘 이상의 방향으로
온도가 변할 수 있다. 해를 구하기 전에 형상과 경계조건을 보고 주요 열전달
방향을 판단해야 한다.

## 내부 열생성 해를 직접 확인하기

대칭면 $x=0$, 표면 $x=L$인 절반 영역에서
$kT''+\dot q'''=0$을 적분하면

$$
T'=-\frac{\dot q'''}{k}x+C_1,\qquad
T=-\frac{\dot q'''}{2k}x^2+C_1x+C_2.
$$

대칭조건 $T'(0)=0$에서 $C_1=0$, $T(L)=T_s$에서
$C_2=T_s+\dot q'''L^2/(2k)$이다. 표면 열유속은
$q_{out}''=\dot q'''L$이므로 양면을 통해 나가는 열은
$2A\dot q'''L$이고 전체 체적 $2AL$의 열생성량과 같다.

예를 들어 $L=0.01\ \mathrm m$, $k=10\ \mathrm{W/(mK)}$,
$\dot q'''=10^6\ \mathrm{W/m^3}$이면 $T_{max}-T_s=5\ \mathrm K$이고
각 면의 열유속은 $10^4\ \mathrm{W/m^2}$이다. 표면온도 대신 대류조건을 주면
$T_s-T_\infty=\dot q'''L/h$가 추가되어 중심온도가 더 높아진다.

# 6. 연습 문제

1. $k=40$, $\rho=8000$, $c_p=500$을 SI 단위로 사용할 때 $\alpha$를 구하라.
2. 열생성이 없는 정상 평면벽의 온도분포가 선형인 이유를 설명하라.
3. 대칭면의 경계조건을 쓰시오.
4. 정상상태에서 시간 미분항 $\partial T/\partial t$의 값은 얼마인가?
5. 열생성이 없고 온도분포가 $T(x)=20x+300$일 때 $d^2T/dx^2$를 구하라.
6. $k$, $\rho$, $c_p$ 가운데 열확산계수의 식에 분모로 들어가는 것을 고르라.

<!--
풀이와 해답:
1. alpha=1.0e-5 m^2/s이다.
2. d^2T/dx^2=0을 두 번 적분하면 T=C1*x+C2이다.
3. dT/dn=0이다.
4. 0이다.
5. 일차함수의 이계 미분이므로 0이다.
6. rho와 c_p이며 alpha=k/(rho*c_p)이다.
-->

## 관련자료와 이어 읽기

- [MIT OCW 3.185: Heat Conduction](https://ocw.mit.edu/courses/3-185-transport-phenomena-in-materials-engineering-fall-2003/resources/chap3/): 에너지 수지와 경계조건을 비교하면서 읽을 열전도 보충자료이다.

- [제4강: 열전달 기초]({% link assets/lecture_notes/2_2_transport_phenomena/transport_04_heat_transfer.md %})
- [제6강: 열전도의 유한차분해석]({% link assets/lecture_notes/2_2_transport_phenomena/transport_06_heat_fdm.md %})

---

[이전 강의]({% link assets/lecture_notes/2_2_transport_phenomena/transport_04_heat_transfer.md %}) | [강의 목록]({% link _lectures/2_2_transport.md %}) | [다음 강의]({% link assets/lecture_notes/2_2_transport_phenomena/transport_06_heat_fdm.md %})
