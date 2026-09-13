---
layout: distill
title: Eigenstrain의 등가 체적력 유도
description: Navier 방정식에서 eigenstrain을 등가 체적력과 계면력으로 나타내는 방법
target: 대학원 입문
permalink:
featured: false
prerequisite: 선형 탄성, 분포와 Dirac delta의 기초, Eshelby inclusion 문제
toc:
  sidebar: left

mermaid:
  enabled: true
  zoomable: true
typograms: true
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

- [1. 이 보충자료의 질문](#1-이-보충자료의-질문)
- [2. 변형률 분해와 구성식](#2-변형률-분해와-구성식)
- [3. 평형방정식에서 등가 체적력 얻기](#3-평형방정식에서-등가-체적력-얻기)
- [4. 등방성 재료의 Navier 방정식](#4-등방성-재료의-navier-방정식)
- [5. 균일한 eigenstrain과 계면력](#5-균일한-eigenstrain과-계면력)
  - [보충: 특성함수의 분포미분](#보충-특성함수의-분포미분)
- [6. 약한 형식으로 확인](#6-약한-형식으로-확인)
- [7. 1차원 예제](#7-1차원-예제)
- [8. 구형 inclusion의 체적팽창 예제](#8-구형-inclusion의-체적팽창-예제)
- [9. Green 함수 및 Eshelby tensor와의 연결](#9-green-함수-및-eshelby-tensor와의-연결)
- [10. 부호와 물리적 의미](#10-부호와-물리적-의미)
  - [10.1. 부호 관례](#101-부호-관례)
  - [10.2. 순힘과 순모멘트](#102-순힘과-순모멘트)
  - [10.3. 균일한 eigenstrain이 전 공간에 존재하는 경우](#103-균일한-eigenstrain이-전-공간에-존재하는-경우)
- [11. 요약](#11-요약)
- [12. 연습 문제](#12-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
- [참고문헌](#참고문헌)

# 1. 이 보충자료의 질문

Eshelby inclusion 문제에서는 고유변형률(eigenstrain)
$\boldsymbol\varepsilon^*$의 효과를 Navier 방정식의 하중항으로 옮겨

$$
\boxed{
f_i^{\mathrm{eq}}
=-\frac{\partial}{\partial x_j}
\left(C_{ijkl}\varepsilon^*_{kl}\right)}
\tag{1}
$$

과 같은 **등가 체적력(equivalent body force)**으로 표현한다. 이 식이 어디에서
나오는지, 그리고 inclusion 내부에서 균일한 eigenstrain이 왜 계면력으로 나타나는지를
차례대로 유도한다.

등가 체적력은 중력처럼 실제로 추가된 외력이 아니다. Eigenstrain이 포함된 문제를
eigenstrain이 없는 균질 탄성체의 등가 하중 문제로 바꾸기 위한 수학적 표현이다.

# 2. 변형률 분해와 구성식

전체 미소변형률은 탄성변형률과 eigenstrain으로 분해된다.

$$
\boxed{
\varepsilon_{ij}=\varepsilon^e_{ij}+\varepsilon^*_{ij}}
\tag{2}
$$

변위 $u_i$에 의한 전체 미소변형률은

$$
\varepsilon_{ij}
=\frac{1}{2}(u_{i,j}+u_{j,i})
$$

이므로 탄성변형률은

$$
\varepsilon^e_{ij}
=\frac{1}{2}(u_{i,j}+u_{j,i})-\varepsilon^*_{ij}
$$

이다. 여기서 $u_{i,j}=\partial u_i/\partial x_j$이다.

응력은 전체변형률이 아니라 탄성변형률에 의해 결정된다.

$$
\sigma_{ij}
=C_{ijkl}\varepsilon^e_{kl}
=C_{ijkl}
\left[
\frac{1}{2}(u_{k,l}+u_{l,k})-\varepsilon^*_{kl}
\right].
\tag{3}
$$

탄성텐서의 minor symmetry $C_{ijkl}=C_{ijlk}$를 사용하면

$$
C_{ijkl}\frac{1}{2}(u_{k,l}+u_{l,k})
=C_{ijkl}u_{k,l}
$$

이므로

$$
\boxed{
\sigma_{ij}
=C_{ijkl}u_{k,l}-C_{ijkl}\varepsilon^*_{kl}}
\tag{4}
$$

를 얻는다.

Eigenstrain에 탄성텐서를 작용시킨 보조적인 응력을

$$
\boxed{
\sigma^*_{ij}=C_{ijkl}\varepsilon^*_{kl}}
\tag{5}
$$

로 정의한다. 이를 eigenstress 또는 polarization stress라고 부르기도 한다. 식 (4)는

$$
\sigma_{ij}=C_{ijkl}u_{k,l}-\sigma^*_{ij}
$$

가 된다. $\boldsymbol\sigma^*$는 실제 응력이 아니라 eigenstrain의 효과를 하중으로
표현하기 위한 보조량이다. 실제 응력은 항상

$$
\boldsymbol\sigma
=\boldsymbol C:(\boldsymbol\varepsilon-\boldsymbol\varepsilon^*)
$$

로 계산해야 한다.

# 3. 평형방정식에서 등가 체적력 얻기

정적 평형방정식은

$$
\sigma_{ij,j}+b_i=0
\tag{6}
$$

이다. $b_i$는 중력과 같은 체적력(body force)이다. 식 (4)를 대입하면

$$
\left(C_{ijkl}u_{k,l}\right)_{,j}
-\left(C_{ijkl}\varepsilon^*_{kl}\right)_{,j}
+b_i=0.
\tag{7}
$$

이 식을 eigenstrain이 없는 기준 탄성체의 평형방정식

$$
\left(C_{ijkl}u_{k,l}\right)_{,j}
+b_i+f_i^{\mathrm{eq}}=0
\tag{8}
$$

과 비교하면

$$
\boxed{
f_i^{\mathrm{eq}}
=-\left(C_{ijkl}\varepsilon^*_{kl}\right)_{,j}
=-\sigma^*_{ij,j}}
\tag{9}
$$

를 얻는다. 벡터 및 텐서 표기로는

$$
\boxed{
\boldsymbol f^{\mathrm{eq}}
=-\nabla\cdot\boldsymbol\sigma^*
=-\nabla\cdot(\boldsymbol C:\boldsymbol\varepsilon^*)}
\tag{10}
$$

이다.

탄성계수가 공간적으로 일정하면 (즉 $C_{ijkl,j} = 0$)

$$
\boxed{
f_i^{\mathrm{eq}}
=-C_{ijkl}\varepsilon^*_{kl,j}}
\tag{11}
$$

로 단순화된다. 탄성계수가 위치에 따라 변하는 inhomogeneity 문제에서는 단순히
$C_{ijkl}$를 미분하는 것만으로 끝나지 않으며, 균질한 기준재료와 탄성계수 차이에 의한
polarization stress를 함께 정의해야 한다.

# 4. 등방성 재료의 Navier 방정식

등방성 탄성텐서는

$$
C_{ijkl}
=\lambda\delta_{ij}\delta_{kl}
+\mu(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})
$$

이다. 탄성계수가 일정할 때 변위에 관한 항은

$$
C_{ijkl}u_{k,lj}
=\mu u_{i,jj}+(\lambda+\mu)u_{j,ji}
$$

가 된다. 이 전개가 필요한 이유는 평형방정식 (8)의 첫 번째 항을 변위
$\boldsymbol u$에 작용하는 미분연산자로 바꾸기 위해서이다. 이렇게 해야 미지수인 변위와
eigenstrain이 만드는 등가 체적력을 각각 식의 왼쪽과 오른쪽에 분리할 수 있으며, 기존의
탄성 변위 문제와 같은 Navier 연산자를 사용하여 해를 구할 수 있다.

위 식은 등방성 탄성텐서를 직접 대입하면 얻어진다.

$$
\begin{aligned}
C_{ijkl}u_{k,lj}
&=\left[\lambda\delta_{ij}\delta_{kl}
+\mu\left(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}\right)\right]
u_{k,lj} \\
&=\lambda\delta_{ij}\delta_{kl}u_{k,lj}
+\mu\delta_{ik}\delta_{jl}u_{k,lj}
+\mu\delta_{il}\delta_{jk}u_{k,lj} \\
&=\lambda u_{k,ki}+\mu u_{i,jj}+\mu u_{j,ij} \\
&=\mu u_{i,jj}+(\lambda+\mu)u_{j,ji}.
\end{aligned}
$$

여기서 Kronecker delta는 서로 같은 첨자를 선택하는 역할을 한다. 예를 들어
$\delta_{ik}\delta_{jl}u_{k,lj}=u_{i,jj}$이고,
$\delta_{il}\delta_{jk}u_{k,lj}=u_{j,ij}$이다. 마지막 줄에서는 더미 첨자 $k$를
$j$로 바꾸고, 변위장이 충분히 매끄러워 혼합 편미분의 순서를 교환할 수 있다는 관계
$u_{j,ij}=u_{j,ji}$를 사용하였다. 또한

$$
u_{i,jj}=\nabla^2u_i,
\qquad
u_{j,ji}=\frac{\partial}{\partial x_i}
\left(\frac{\partial u_j}{\partial x_j}\right)
=\left[\nabla(\nabla\cdot\boldsymbol u)\right]_i
$$

이므로 첫 번째 항은 변위의 벡터 Laplacian, 두 번째 항은 체적변형과 관련된 변위
발산의 gradient를 나타낸다. 따라서 등방성 재료의 Navier 방정식은

$$
\boxed{
\mu\nabla^2\boldsymbol u
+(\lambda+\mu)\nabla(\nabla\cdot\boldsymbol u)
+\boldsymbol b+\boldsymbol f^{\mathrm{eq}}
=\boldsymbol0}
\tag{12}
$$

이다.

등방성 재료의 eigenstress는

$$
\sigma^*_{ij}
=\lambda\varepsilon^*_{kk}\delta_{ij}
+2\mu\varepsilon^*_{ij}
$$

이므로 등가 체적력은

$$
\boxed{
f_i^{\mathrm{eq}}
=-\lambda\frac{\partial\varepsilon^*_{kk}}{\partial x_i}
-2\mu\frac{\partial\varepsilon^*_{ij}}{\partial x_j}}
\tag{13}
$$

이다. 즉 eigenstrain이 공간적으로 변하는 영역이 Navier 방정식의 source가 된다.

# 5. 균일한 eigenstrain과 계면력

Inclusion 내부에서 eigenstrain이 일정하면

$$
\varepsilon^*_{ij,k}=0
\qquad (\boldsymbol x\in\Omega)
$$

이므로 inclusion의 내부점에서는 $\boldsymbol f^{\mathrm{eq}}=\boldsymbol0$이다. 그러나
eigenstrain은 inclusion 안에서는 일정하고 기지에서는 0이므로 계면에서 불연속이다.

Inclusion의 특성함수(characteristic function)를

$$
\chi_\Omega(\boldsymbol x)=
\begin{cases}
1,&\boldsymbol x\in\Omega,\\
0,&\boldsymbol x\notin\Omega
\end{cases}
$$

로 정의하면 전체 공간의 eigenstrain장은

$$
\varepsilon^*_{kl}(\boldsymbol x)
=\varepsilon^{*0}_{kl}\chi_\Omega(\boldsymbol x)
\tag{14}
$$

이다. $\varepsilon^{*0}_{kl}$은 inclusion 내부의 일정한 값이다.

바깥쪽 단위법선을 $n_j$라고 하면 특성함수의 분포미분은

$$
\boxed{
\chi_{\Omega,j}
=-n_j\delta_{\partial\Omega}}
\tag{15}
$$

이다. $\delta_{\partial\Omega}$는 inclusion 계면에 집중된 surface delta다.

식 (14)--(15)를 식 (11)에 대입하면

$$
\begin{aligned}
f_i^{\mathrm{eq}}
&=-C_{ijkl}\varepsilon^{*0}_{kl}\chi_{\Omega,j}\\
&=C_{ijkl}\varepsilon^{*0}_{kl}n_j
\delta_{\partial\Omega}\\
&=\sigma^{*0}_{ij}n_j\delta_{\partial\Omega}.
\end{aligned}
$$

따라서

$$
\boxed{
f_i^{\mathrm{eq}}
=t_i^*\delta_{\partial\Omega},
\qquad
t_i^*=\sigma^{*0}_{ij}n_j}
\tag{16}
$$

이다. Navier 방정식에서는 체적력항으로 표현되지만, 균일한 inclusion eigenstrain의
경우 그 힘은 실제로 계면에 집중된 등가 표면력과 같다.

## 보충: 특성함수의 분포미분

보통의 미분은 함수가 한 점의 주변에서 매끄럽게 변할 때 그 변화율을 나타낸다. 그러나
$\chi_\Omega$는 계면에서 1에서 0으로 불연속적으로 변하므로, 계면 위에서는 고전적인
의미의 미분을 정의할 수 없다. 분포미분(distributional derivative)은 이러한 불연속의
미분까지 포함하도록 미분의 개념을 확장한 것이다.

먼저 1차원에서 다음 계단함수를 생각하자.

$$
\chi(x)=
\begin{cases}
1,&x<0,\\
0,&x>0.
\end{cases}
$$

$x<0$과 $x>0$에서는 함수가 일정하므로 $d\chi/dx=0$이다. 하지만 $x=0$에서는 함수가
1만큼 감소한다. 이 계면의 급격한 변화를 분포미분으로는

$$
\frac{d\chi}{dx}=-\delta(x)
$$

라고 쓴다. Dirac delta $\delta(x)$는 $x=0$ 이외의 점에서는 0이지만, 적분하면 불연속의
전체 변화량을 남긴다.

$$
\int_{-\infty}^{\infty}\frac{d\chi}{dx}\,dx
=-\int_{-\infty}^{\infty}\delta(x)\,dx=-1.
$$

마이너스 부호는 양의 $x$ 방향으로 계면을 통과할 때 $\chi$가 $1$에서 $0$으로
감소하기 때문에 나타난다.

이를 다차원 inclusion에 확장하면 불연속은 한 점이 아니라 계면
$\partial\Omega$ 전체에서 발생한다. Inclusion의 바깥쪽 단위법선을 $\boldsymbol n$이라고
하면

$$
\nabla\chi_\Omega=-\boldsymbol n\delta_{\partial\Omega}
$$

가 된다. 여기서 surface delta $\delta_{\partial\Omega}$는 체적적분을 계면의 면적분으로
바꾸는 분포로 이해할 수 있다.

$$
\int_V g(\boldsymbol x)\delta_{\partial\Omega}\,dV
=\int_{\partial\Omega}g(\boldsymbol x)\,dS.
$$

따라서 $\nabla\chi_\Omega$는 inclusion 내부나 외부에 퍼져 있는 보통의 함수가 아니라,
계면에서만 작용하는 방향성 있는 변화량이다. 식 (14)를 미분하면

$$
\varepsilon^*_{kl,j}
=\varepsilon^{*0}_{kl}\chi_{\Omega,j}
=-\varepsilon^{*0}_{kl}n_j\delta_{\partial\Omega}
$$

이므로, 균일한 eigenstrain의 공간미분은 내부와 외부에서는 0이고 계면에만 delta
형태로 남는다. 결국 식 (16)은 eigenstrain의 불연속이 만드는 효과를 체적력의 형식으로
기록했지만, 그 작용 위치와 물리적 효과는 계면 traction과 같다는 것을 뜻한다.

# 6. 약한 형식으로 확인

분포미분의 의미는 임의의 매끄러운 시험함수 $\varphi_i$를 사용하면 분명해진다.

$$
f_i^{\mathrm{eq}}
=-\left(\sigma^{*0}_{ij}\chi_\Omega\right)_{,j}
$$

이므로

$$
\int_V f_i^{\mathrm{eq}}\varphi_i\,dV
=-\int_V
\left(\sigma^{*0}_{ij}\chi_\Omega\right)_{,j}
\varphi_i\,dV.
$$

시험함수가 외부 경계에서 0이라고 하고 부분적분하면

$$
\int_V f_i^{\mathrm{eq}}\varphi_i\,dV
=\int_\Omega\sigma^{*0}_{ij}\varphi_{i,j}\,dV.
$$

$\sigma^{*0}_{ij}$가 inclusion 내부에서 일정하므로 발산정리를 적용하면

$$
\boxed{
\int_V f_i^{\mathrm{eq}}\varphi_i\,dV
=\int_{\partial\Omega}
\sigma^{*0}_{ij}n_j\varphi_i\,dS}
\tag{17}
$$

를 얻는다. 이는 등가 체적력과 계면 traction
$t_i^*=\sigma^{*0}_{ij}n_j$이 모든 시험함수에 대해 동일한 일을 한다는 뜻이다.

# 7. 1차원 예제

구간 $0<x<L$에만 일정한 eigenstrain $\varepsilon_0^*$가 존재한다고 하자.

$$
\varepsilon^*(x)
=\varepsilon_0^*[H(x)-H(x-L)]
\tag{18}
$$

여기서 $H(x)$는 Heaviside 함수다. 1차원 구성식과 평형방정식은

$$
\sigma=E(u_{,x}-\varepsilon^*),
\qquad
\sigma_{,x}=0
$$

이므로

$$
Eu_{,xx}-E\varepsilon^*_{,x}=0.
$$

따라서 등가 체적력은

$$
f^{\mathrm{eq}}=-E\varepsilon^*_{,x}
$$

이다. Heaviside 함수의 미분을 이용하면

$$
\varepsilon^*_{,x}
=\varepsilon_0^*[\delta(x)-\delta(x-L)]
$$

이므로

$$
\boxed{
f^{\mathrm{eq}}
=-E\varepsilon_0^*\delta(x)
+E\varepsilon_0^*\delta(x-L)}
\tag{19}
$$

이다. $\varepsilon_0^*>0$이면 왼쪽 끝에서는 왼쪽 방향, 오른쪽 끝에서는 오른쪽 방향의
등가력이 작용한다. 두 힘의 합은 0이지만 서로 반대 방향으로 영역을 팽창시키는
자기평형 하중계(self-equilibrated loading)를 이룬다.

# 8. 구형 inclusion의 체적팽창 예제

구형 inclusion이

$$
\varepsilon^*_{ij}=\varepsilon_0\delta_{ij},
\qquad \varepsilon_0>0
$$

의 등방적인 팽창을 하려 한다고 하자. Eigenstress는

$$
\begin{aligned}
\sigma^*_{ij}
&=\lambda\varepsilon^*_{kk}\delta_{ij}
+2\mu\varepsilon^*_{ij}\\
&=(3\lambda+2\mu)\varepsilon_0\delta_{ij}\\
&=3K\varepsilon_0\delta_{ij},
\end{aligned}
\tag{20}
$$

여기서 $K=\lambda+2\mu/3$은 체적탄성계수다. 계면의 등가 traction은

$$
\begin{aligned}
t_i^*
&=\sigma^*_{ij}n_j\\
&=3K\varepsilon_0n_i
\end{aligned}
$$

이므로

$$
\boxed{
\boldsymbol t^*=3K\varepsilon_0\boldsymbol n}
\tag{21}
$$

이다. 즉 양의 체적 eigenstrain에 해당하는 등가 traction은 구의 바깥쪽을 향한다.
이는 잘라낸 inclusion이 자유롭게 팽창하려는 경향을 나타낸다.

하지만 기지와 다시 결합한 뒤의 실제 inclusion 응력은 등가 traction이 아니다. 기지의
구속으로 결정된 변형률 $\boldsymbol\varepsilon^c$를 사용하여

$$
\boxed{
\boldsymbol\sigma^I
=\boldsymbol C:(\boldsymbol\varepsilon^c-
\boldsymbol\varepsilon^*)}
\tag{22}
$$

로 계산한다. 이 체적팽창 문제에서는 구속된 체적변형률의 계수가 자유팽창 계수보다
작으므로 실제 내부응력은 정수압축 상태가 된다.

# 9. Green 함수 및 Eshelby tensor와의 연결

Navier 연산자를 $\mathcal L_{ik}$라 하고 Green 함수를

$$
\mathcal L_{ik}G_{kj}(\boldsymbol x-\boldsymbol y)
=-\delta_{ij}\delta(\boldsymbol x-\boldsymbol y)
\tag{23}
$$

로 정의하자. 그러면 등가 체적력에 의한 변위는

$$
u_i(\boldsymbol x)
=\int_VG_{ij}(\boldsymbol x-\boldsymbol y)
f_j^{\mathrm{eq}}(\boldsymbol y)\,dV_y
\tag{24}
$$

로 표현된다. 식 (9)를 대입하고 부분적분하면 eigenstress와 Green 함수 미분의 적분으로
바뀐다. 균일한 eigenstress의 경우에는 식 (16)을 사용해 바로

$$
u_i(\boldsymbol x)
=\int_{\partial\Omega}
G_{ij}(\boldsymbol x-\boldsymbol y)
\sigma^*_{jk}n_k\,dS_y
\tag{25}
$$

로 쓸 수 있다.

이 변위를 $\boldsymbol x$에 대해 미분하고 대칭부분을 취하면 구속변형률이 얻어진다.

$$
\varepsilon^c_{ij}
=\frac{1}{2}(u_{i,j}+u_{j,i})
=P_{ijkl}\sigma^*_{kl}.
\tag{26}
$$

마지막으로 $\sigma^*_{kl}=C_{klmn}\varepsilon^*_{mn}$을 사용하면

$$
\varepsilon^c_{ij}
=P_{ijkl}C_{klmn}\varepsilon^*_{mn}
=S_{ijmn}\varepsilon^*_{mn}
$$

이므로

$$
\boxed{
\boldsymbol S=\boldsymbol P:\boldsymbol C}
\tag{27}
$$

를 얻는다. 즉 등가 체적력은 eigenstrain 문제를 Green 함수로 풀고 Eshelby tensor를
구할 수 있게 하는 연결고리다.

# 10. 부호와 물리적 의미

## 10.1. 부호 관례

본 자료는

$$
\sigma_{ij,j}+b_i=0
$$

및 식 (23)의 Green 함수 정의를 사용했다. 평형방정식을
$\mathcal L\boldsymbol u=\boldsymbol f$ 형태로 쓰거나 Green 함수의 부호를 다르게
정의한 문헌에서는 중간식의 부호가 반대로 보일 수 있다. 항상 평형방정식, Green 함수와
법선의 정의를 함께 확인해야 한다.

또한 식 (16)의 $\boldsymbol t^*$는 eigenstrain이 없는 **등가 기준체**에 가하는
traction이다. 절단된 inclusion과 matrix 중 어느 쪽의 자유물체도를 그리는가에 따라
작용ㆍ반작용으로 화살표 방향이 반대가 될 수 있다.

## 10.2. 순힘과 순모멘트

균일한 eigenstress가 만드는 계면력의 합은

$$
\int_{\partial\Omega}\sigma^*_{ij}n_j\,dS
=\sigma^*_{ij}\int_{\partial\Omega}n_j\,dS=0
$$

이다. $\boldsymbol\sigma^*$가 대칭이면 순모멘트도 0이다. 따라서 이 등가 하중은 외부에서
물체 전체를 가속하는 힘이 아니라 내부 불일치를 나타내는 자기평형 하중이다.

## 10.3. 균일한 eigenstrain이 전 공간에 존재하는 경우

동일한 일정 eigenstrain이 무한한 물체 전체에 존재하면 공간 구배도 계면도 없다.

$$
\nabla\boldsymbol\varepsilon^*=\boldsymbol0,
\qquad
\boldsymbol f^{\mathrm{eq}}=\boldsymbol0.
$$

물체 전체가 자유롭게 같은 변형을 할 수 있으므로 응력이 발생하지 않는다. Inclusion
문제에서 응력을 만드는 직접적인 원인은 eigenstrain의 값 자체가 아니라
**eigenstrain의 공간적 불균일성과 주변 기지의 구속**이다.

# 11. 요약

| 단계 | 관계식 | 의미 |
|---|---|---|
| 변형률 분해 | $\boldsymbol\varepsilon=\boldsymbol\varepsilon^e+\boldsymbol\varepsilon^*$ | 전체변형률에서 eigenstrain을 분리 |
| 실제 응력 | $\boldsymbol\sigma=\boldsymbol C:(\boldsymbol\varepsilon-\boldsymbol\varepsilon^*)$ | 응력은 탄성변형률에 의존 |
| Eigenstress | ${\boldsymbol\sigma}^\*=\boldsymbol C:\boldsymbol\varepsilon^*$ | 등가 하중을 만들기 위한 보조량 |
| 등가 체적력 | $\boldsymbol f^{\mathrm{eq}}=-\nabla\cdot\boldsymbol\sigma^*$ | eigenstrain을 Navier 방정식의 source로 변환 |
| 균일한 inclusion | $\boldsymbol f^{\mathrm{eq}}=(\boldsymbol\sigma^*\boldsymbol n)\delta_{\partial\Omega}$ | 계면에 집중된 등가 traction |
| Green 함수 | $\boldsymbol u=\boldsymbol G*\boldsymbol f^{\mathrm{eq}}$ | 등가 하중으로 변위 계산 |
| Eshelby tensor | $\boldsymbol S=\boldsymbol P:\boldsymbol C$ | eigenstrain을 구속변형률로 변환 |

# 12. 연습 문제

## 문제 1

$\sigma_{ij}=C_{ijkl}(\varepsilon_{kl}-\varepsilon^*_{kl})$과
$\sigma_{ij,j}+b_i=0$에서 식 (9)를 유도하시오.

<!--
풀이와 해답:
epsilon_kl=0.5(u_k,l+u_l,k)를 대입하고 C_ijkl=C_ijlk를 사용하면
sigma_ij=C_ijkl u_k,l-C_ijkl epsilon*_kl이다. 이를 평형식에 대입해 eigenstrain 항을
외력항과 묶으면 f_eq_i=-(C_ijkl epsilon*_kl)_,j를 얻는다.
-->

## 문제 2

탄성계수가 일정할 때 등가 체적력이 식 (11)로 단순화되는 이유를 설명하시오.

<!--
풀이와 해답:
곱의 미분을 적용하면
(C_ijkl epsilon*_kl)_,j=C_ijkl,j epsilon*_kl+C_ijkl epsilon*_kl,j이다.
균질한 재료에서는 C_ijkl,j=0이므로 두 번째 항만 남는다.
-->

## 문제 3

균일한 eigenstrain을 갖는 inclusion의 등가 체적력이 내부에서는 0이지만 계면에서는
0이 아닌 이유를 설명하시오.

<!--
풀이와 해답:
Inclusion 내부에서는 eigenstrain의 공간미분이 0이다. 그러나 기지에서는 eigenstrain이
0이므로 계면에서 불연속이 생긴다. 특성함수의 분포미분이
chi_Omega,j=-n_j delta_boundary이므로 계면에 delta 형태의 등가력이 나타난다.
-->

## 문제 4

등방적인 eigenstrain $\varepsilon^*_{ij}=\varepsilon_0\delta_{ij}$에 대응하는
eigenstress와 계면 traction을 구하시오.

<!--
풀이와 해답:
sigma*_ij=lambda epsilon*_kk delta_ij+2mu epsilon*_ij
=(3lambda+2mu)epsilon_0 delta_ij=3K epsilon_0 delta_ij이다.
따라서 t*_i=sigma*_ij n_j=3K epsilon_0 n_i이다.
-->

## 문제 5

등가 체적력이 실제 외력과 다른 이유를 설명하시오.

<!--
풀이와 해답:
등가 체적력은 eigenstrain을 제거한 기준 탄성체가 원래 문제와 같은 변위와 응력장을
만들도록 도입한 수학적 하중이다. 실제로 외부에서 가한 힘이 아니며, 균일한 inclusion의
경우 순힘과 순모멘트가 0인 자기평형 계면력으로 나타난다.
-->

# 참고문헌

1. J. D. Eshelby, “The determination of the elastic field of an ellipsoidal
   inclusion, and related problems,” *Proceedings of the Royal Society A*,
   241, 376--396 (1957). [DOI: 10.1098/rspa.1957.0133](https://doi.org/10.1098/rspa.1957.0133)
2. T. Mura, *Micromechanics of Defects in Solids*, 2nd ed., Martinus Nijhoff
   Publishers (1987).

[구형 Eshelby tensor 유도 자료로 돌아가기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16a_eshelby_sphere_derivation.md %})
