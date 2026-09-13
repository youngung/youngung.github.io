---
layout: distill
title: Kelvin Green 함수의 유도와 해석
description: 무한 등방 탄성체의 Navier 방정식으로부터 Kelvin 기본해를 구하는 과정
target: 대학원 입문
permalink:
featured: false
prerequisite: 선형 탄성, Fourier 변환, 지수표기법, Dirac delta
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

- [1. 이 보충자료의 목표](#1-이-보충자료의-목표)
- [2. Green 함수의 정의와 부호](#2-green-함수의-정의와-부호)
- [3. Fourier 공간의 Navier 연산자](#3-fourier-공간의-navier-연산자)
- [4. 종방향과 횡방향 성분의 역연산](#4-종방향과-횡방향-성분의-역연산)
- [5. 실공간으로 역변환](#5-실공간으로-역변환)
- [6. Poisson 비를 사용한 Kelvin 해](#6-poisson-비를-사용한-kelvin-해)
- [7. 결과의 물리적 의미](#7-결과의-물리적-의미)
  - [7.1. 두 텐서 항의 역할](#71-두-텐서-항의-역할)
  - [7.2. 거리 감쇠와 차원](#72-거리-감쇠와-차원)
  - [7.3. 원점의 특이성과 분포 해석](#73-원점의-특이성과-분포-해석)
- [8. 간단한 검산](#8-간단한-검산)
- [9. Eshelby 문제와의 연결](#9-eshelby-문제와의-연결)
- [10. 요약](#10-요약)
- [11. 연습 문제](#11-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
- [참고문헌](#참고문헌)

# 1. 이 보충자료의 목표

무한하고 균질한 등방성 선형탄성체에 한 방향의 단위 집중력을 가하면, 그 힘이 만드는
변위가 Kelvin Green 함수로 표현된다. 이 자료에서는 Navier 방정식에서 출발하여

$$
\boxed{
G_{ij}(\boldsymbol r)
=\frac{1}{16\pi\mu(1-\nu)r}
\left[
(3-4\nu)\delta_{ij}
+\frac{r_i r_j}{r^2}
\right]}
\tag{1}
$$

을 유도하고 각 항의 의미를 설명한다. 여기서 $\boldsymbol r=\boldsymbol x-\boldsymbol y$는
힘이 작용하는 점 $\boldsymbol y$에서 관찰점 $\boldsymbol x$로 향하는 벡터이고,
$r=\|\boldsymbol r\|$이다.

# 2. Green 함수의 정의와 부호

등방성 균질 탄성체의 정적 Navier 방정식을

$$
\mu\nabla^2u_i+(\lambda+\mu)u_{k,ki}+b_i=0
$$

라고 쓰자. $j$방향 단위 집중력이 원점에 작용하면

$$
b_i(\boldsymbol r)=\delta_{ij}\delta(\boldsymbol r)
$$

이고, 이때의 $i$방향 변위를 $G_{ij}$라고 정의한다. 따라서 Green 함수는

$$
\boxed{
\mu\nabla^2G_{ij}
+(\lambda+\mu)G_{kj,ki}
=-\delta_{ij}\delta(\boldsymbol r)}
\tag{2}
$$

를 만족한다. 첫 번째 첨자 $i$는 변위 방향이고 두 번째 첨자 $j$는 집중력 방향이다.
식 (2)의 마이너스 부호는 체적력항을 Navier 방정식의 왼쪽에 둔 관례에서 생긴다.
연산자나 하중항을 반대편에 놓는 문헌에서는 Green 함수 정의의 부호가 달라질 수 있다.

# 3. Fourier 공간의 Navier 연산자

다음 Fourier 변환을 사용한다.

$$
\widehat f(\boldsymbol k)
=\int_{\mathbb R^3}f(\boldsymbol r)e^{-i\boldsymbol k\cdot\boldsymbol r}\,dV,
\qquad
f(\boldsymbol r)
=\frac{1}{(2\pi)^3}\int_{\mathbb R^3}
\widehat f(\boldsymbol k)e^{i\boldsymbol k\cdot\boldsymbol r}\,d\boldsymbol k.
$$

> **참고:** 위 식의 3차원은 함수가 정의된 공간의 차원이며, $f$는 스칼라여도 된다.
> $\boldsymbol k\cdot\boldsymbol r=k_1r_1+k_2r_2+k_3r_3$는 두 벡터의 내적으로,
> 위치 $\boldsymbol r$에서 Fourier 파동 성분의 위상을 나타내는 스칼라다.
> 따라서 $e^{-i\boldsymbol k\cdot\boldsymbol r}$도 스칼라이며, 스칼라장과 벡터장 모두에 같은 형태로 사용된다.
> 벡터장 $u_i$나 텐서장 $G_{ij}$는 각 성분에 같은 Fourier 변환을 적용한다.
> 변환 자체는 성분들을 섞지 않으며, 아래의 성분 간 결합은 Navier 연산자에서 생긴다.

여기서 $\boldsymbol k=(k_1,k_2,k_3)$는 공간상의 변화를 파동 성분으로 나타내는
파수벡터다. 공간미분이 Fourier 공간에서 어떻게 바뀌는지 확인하기 위해 $f$가 무한
원방(at infinity)에서 충분히 빠르게 0으로 감소한다고 하자. $r_i$에 대한 미분을 Fourier 변환하고
부분적분하면

$$
\begin{aligned}
\mathcal F\left[\frac{\partial f}{\partial r_i}\right]
&=\int_{\mathbb R^3}
\frac{\partial f}{\partial r_i}
e^{-i\boldsymbol k\cdot\boldsymbol r}\,dV\\
&=\left[f e^{-i\boldsymbol k\cdot\boldsymbol r}\right]_{\text{at infinity}}
-\int_{\mathbb R^3}f
\frac{\partial}{\partial r_i}
\left(e^{-i\boldsymbol k\cdot\boldsymbol r}\right)dV\\
&=ik_i\widehat f(\boldsymbol k).
\end{aligned}
$$

첫 번째 줄의 경계항은 원방(at infinity)에서 $f\rightarrow0$이므로 사라진다. 즉 실공간에서 한 번
미분하는 연산은 Fourier 공간에서 $ik_i$를 곱하는 연산으로 바뀐다. 두 번 미분하면

$$
\mathcal F\left[\frac{\partial^2 f}{\partial r_i\partial r_j}\right]
=(ik_i)(ik_j)\widehat f
=-k_i k_j\widehat f
$$

가 된다. 따라서 공간미분의 변환 규칙은

$$
\frac{\partial}{\partial r_i}\longrightarrow ik_i,
\qquad
\nabla^2\longrightarrow-k^2
$$

가 된다. 여기서 $k^2=k_lk_l$이며, Laplacian은 같은 방향의 두 번째 미분을 모두
더한 것이므로

$$
\mathcal F[\nabla^2f]
=-k_lk_l\widehat f=-k^2\widehat f
$$

이다.

이 규칙을 식 (2)의 각 항에 적용하면

$$
\mathcal F[\mu\nabla^2G_{ij}]
=-\mu k^2\widehat G_{ij},
\qquad
\mathcal F[(\lambda+\mu)G_{kj,ki}]
=-(\lambda+\mu)k_i k_k\widehat G_{kj}.
$$

한편 $\mathcal F[\delta(\boldsymbol r)]=1$이다. 따라서 식 (2)를 Fourier 변환한 뒤
양변에 $-1$을 곱하면

$$
\left[\mu k^2\delta_{ik}+(\lambda+\mu)k_i k_k\right]
\widehat G_{kj}(\boldsymbol k)
=\delta_{ij}
\tag{3}
$$

을 얻는다. 이 변환이 가능한 이유를 조금 더 구체적으로 살펴보자. 하나의 Fourier 성분을

$$
\phi_{\boldsymbol k}(\boldsymbol r)
=e^{i\boldsymbol k\cdot\boldsymbol r}
$$

라고 하면, 이를 미분해도 전혀 다른 모양의 함수가 생기지 않는다.

$$
\frac{\partial\phi_{\boldsymbol k}}{\partial r_i}
=ik_i\phi_{\boldsymbol k},
\qquad
\nabla^2\phi_{\boldsymbol k}
=-k^2\phi_{\boldsymbol k}.
$$

즉 미분 전후에 $\phi_{\boldsymbol k}$의 공간적 모양은 그대로이고, 앞에 $ik_i$ 또는
$-k^2$라는 수만 곱해진다. 선형대수에서 행렬을 어떤 벡터에 작용시켰을 때 같은 벡터에
상수만 곱해져 나오면 그 벡터를 고유벡터라고 부른다. 이와 같은 의미에서
$e^{i\boldsymbol k\cdot\boldsymbol r}$를 공간 미분연산자의 **고유함수**라고 부른다.

일반적인 함수는 이러한 Fourier 성분들의 중첩으로 표현된다.

$$
f(\boldsymbol r)
=\frac{1}{(2\pi)^3}\int_{\mathbb R^3}
\widehat f(\boldsymbol k)
e^{i\boldsymbol k\cdot\boldsymbol r}\,d\boldsymbol k.
$$

따라서 $f$를 미분할 때는 각 Fourier 성분의 진폭 $\widehat f(\boldsymbol k)$에 해당하는
$ik_i$를 곱하면 된다. 중요한 점은 미분으로 인해 파수 $\boldsymbol k$인 성분이 다른
파수 $\boldsymbol k'$인 성분으로 바뀌거나 서로 섞이지 않는다는 것이다. 이것이
“미분연산자가 Fourier 공간에서 대각화된다”는 말의 의미다.

이에 따라 실공간에서 여러 점의 값이 미분으로 연결된 편미분방정식은 Fourier 공간에서
각 $\boldsymbol k$마다 독립된 대수방정식이 된다. 그러나 **공간의 위치에 관한 결합**이
사라졌다는 것이 변위의 세 방향 성분까지 서로 독립이 되었다는 뜻은 아니다.

식 (3)에서

$$
A_{ik}(\boldsymbol k)
=\mu k^2\delta_{ik}+(\lambda+\mu)k_i k_k
$$

라고 정의하면, 고정된 $\boldsymbol k$와 힘의 방향 $j$에 대해 풀어야 하는 식은

$$
A_{ik}\widehat G_{kj}=\delta_{ij}
$$

이다. 이때 $\widehat G_{1j}$, $\widehat G_{2j}$, $\widehat G_{3j}$는 세 개의 미지수다.
예를 들어 첫 번째 방정식에는

$$
\left[\mu k^2+(\lambda+\mu)k_1^2\right]\widehat G_{1j}
+(\lambda+\mu)k_1k_2\widehat G_{2j}
+(\lambda+\mu)k_1k_3\widehat G_{3j}
=\delta_{1j}
$$

가 나타난다. 일반적인 방향의 $\boldsymbol k$에서는 $k_1k_2$, $k_1k_3$과 같은
비대각 성분이 0이 아니므로 한 방향의 변위를 구할 때 다른 두 방향의 변위도 함께
결정해야 한다. 이것이 $k_i k_k$ 항이 변위 성분들을 결합한다는 뜻이다.

이를 행렬로 쓰면

$$
\underbrace{\left[
\mu k^2\mathsf I+(\lambda+\mu)\boldsymbol k\otimes\boldsymbol k
\right]}_{\mathsf A(\boldsymbol k)}
\widehat{\boldsymbol G}_{\cdot j}
=\boldsymbol e_j.
$$

$\widehat{\boldsymbol G}_{\cdot j}$는 $j$방향 단위력에 대한 세 방향 변위응답이고,
$\boldsymbol e_j$는 $j$번째 단위벡터다. 모든 힘 방향 $j=1,2,3$에 대한 응답을 한꺼번에
구하는 것은

$$
\widehat{\mathsf G}(\boldsymbol k)=\mathsf A^{-1}(\boldsymbol k)
$$

을 계산하는 것과 같다. 그래서 각 $\boldsymbol k$에 대해 $3\times3$ 행렬을 역산한다고
표현한다.

다만 좌표축 하나를 $\boldsymbol k$와 나란히 잡으면 구조가 명확해진다. 예를 들어
$\boldsymbol k=(0,0,k)$이면

$$
\mathsf A
=\begin{bmatrix}
\mu k^2&0&0\\
0&\mu k^2&0\\
0&0&(\lambda+2\mu)k^2
\end{bmatrix}.
$$

이 좌표계에서는 $\boldsymbol k$에 수직인 두 횡방향 성분은 강성 $\mu k^2$를, 평행한
종방향 성분은 강성 $(\lambda+2\mu)k^2$를 가지며 서로 분리된다. 다음 절의 종ㆍ횡방향
투영자는 매번 좌표축을 회전하지 않고도 이 분리를 임의의 $\boldsymbol k$ 방향에서
표현하는 방법이다.

# 4. 종방향과 횡방향 성분의 역연산

파수벡터 $\boldsymbol k$에 평행한 종방향(longitudinal) 투영자와 수직인 횡방향
(transverse) 투영자를

$$
P^{\mathrm L}_{ij}=\frac{k_i k_j}{k^2},
\qquad
P^{\mathrm T}_{ij}=\delta_{ij}-\frac{k_i k_j}{k^2}
$$

로 정의한다. 두 투영자는

$$
\mathsf P^{\mathrm L}+\mathsf P^{\mathrm T}=\mathsf I,
\qquad
\mathsf P^{\mathrm L}\mathsf P^{\mathrm T}=\mathsf0,
\qquad
(\mathsf P^{\mathrm L})^2=\mathsf P^{\mathrm L},
\qquad
(\mathsf P^{\mathrm T})^2=\mathsf P^{\mathrm T}
$$

를 만족한다. 식 (3)의 Navier 연산자는 이 투영자들을 사용하여

$$
\mu k^2\mathsf P^{\mathrm T}
+(\lambda+2\mu)k^2\mathsf P^{\mathrm L}
$$

로 분해된다. 따라서 횡방향 고유값은 $\mu k^2$, 종방향 고유값은
$(\lambda+2\mu)k^2$이며, 각 성분의 역수를 취하면

$$
\widehat G_{ij}(\boldsymbol k)
=\frac{P^{\mathrm T}_{ij}}{\mu k^2}
+\frac{P^{\mathrm L}_{ij}}{(\lambda+2\mu)k^2}
\tag{4}
$$

이다. 이를 Kronecker delta와 $k_i$로 다시 쓰면

$$
\boxed{
\widehat G_{ij}(\boldsymbol k)
=\frac{\delta_{ij}}{\mu k^2}
-\frac{\lambda+\mu}{\mu(\lambda+2\mu)}
\frac{k_i k_j}{k^4}}
\tag{5}
$$

를 얻는다. 이 투영자 분해는 등방성 탄성체가 전단형 변형과 팽창형 변형에 서로 다른
강성으로 저항한다는 사실을 나타낸다.

# 5. 실공간으로 역변환

3차원 Fourier 변환의 기본 관계는

$$
\mathcal F^{-1}\left[\frac{1}{k^2}\right]
=\frac{1}{4\pi r}
\tag{6}
$$

이다. 두 번째 항을 역변환하기 위해

$$
H(\boldsymbol r)=\mathcal F^{-1}\left[\frac{1}{k^4}\right]
$$

라고 두자. Fourier 공간에서 $-k^2/k^4=-1/k^2$이므로

$$
\nabla^2H=-\frac{1}{4\pi r}.
$$

$r\ne0$에서 $\nabla^2r=2/r$이므로 상수 또는 조화함수를 제외하면

$$
H=-\frac{r}{8\pi}
$$

로 둘 수 있다. 또한 $k_i k_j$의 곱은 실공간에서 $-\partial_i\partial_j$에 대응하므로

$$
\begin{aligned}
\mathcal F^{-1}\left[\frac{k_i k_j}{k^4}\right]
&=-\frac{\partial^2H}{\partial r_i\partial r_j}\\
&=\frac{1}{8\pi}
\frac{\partial^2r}{\partial r_i\partial r_j}\\
&=\frac{1}{8\pi}
\left(\frac{\delta_{ij}}{r}-\frac{r_i r_j}{r^3}\right).
\end{aligned}
\tag{7}
$$

식 (6)--(7)을 식 (5)에 대입하고 계수를 정리하면

$$
G_{ij}(\boldsymbol r)
=\frac{1}{8\pi\mu(\lambda+2\mu)r}
\left[
(\lambda+3\mu)\delta_{ij}
+(\lambda+\mu)\frac{r_i r_j}{r^2}
\right]
\tag{8}
$$

을 얻는다.

# 6. Poisson 비를 사용한 Kelvin 해

Lamé 상수와 Poisson 비의 관계

$$
\lambda=\frac{2\mu\nu}{1-2\nu}
$$

를 사용하면

$$
\lambda+2\mu=\frac{2\mu(1-\nu)}{1-2\nu},
\qquad
\lambda+3\mu=\frac{\mu(3-4\nu)}{1-2\nu},
\qquad
\lambda+\mu=\frac{\mu}{1-2\nu}
$$

이다. 이를 식 (8)에 대입하면 최종적으로

$$
\boxed{
G_{ij}(\boldsymbol r)
=\frac{1}{16\pi\mu(1-\nu)r}
\left[
(3-4\nu)\delta_{ij}
+\frac{r_i r_j}{r^2}
\right]}
\tag{9}
$$

를 얻는다. 이것이 3차원 무한 등방 탄성체의 Kelvin Green 함수다.

# 7. 결과의 물리적 의미

## 7.1. 두 텐서 항의 역할

집중력 $F_j$가 작용할 때 변위는 $u_i=G_{ij}F_j$이므로

$$
u_i(\boldsymbol r)
=\frac{1}{16\pi\mu(1-\nu)r}
\left[
(3-4\nu)F_i
+\frac{\boldsymbol F\cdot\boldsymbol r}{r^2}r_i
\right]
$$

이다. $\delta_{ij}$ 항은 힘과 같은 방향의 변위를 만들고, $r_i r_j/r^2$ 항은 힘을
관찰점의 방사방향으로 투영하여 방향에 따른 변위 차이를 만든다. 따라서 점하중이 만드는
변위장은 단순히 힘 방향으로 평행한 장이 아니라 관찰 방향에 따라 달라지는 텐서장이다.

## 7.2. 거리 감쇠와 차원

$G_{ij}$는 $1/(\mu r)$에 비례하므로 원점에서 멀어질수록 $1/r$로 감소한다. 응력과
변형률은 변위의 공간미분을 포함하므로 대략 $1/r^2$로 감소한다. 또한

$$
[G_{ij}]=\frac{1}{[\text{응력}][\text{길이}]}
=\frac{[\text{길이}]}{[\text{힘}]}
$$

이므로 $G_{ij}$에 힘을 곱하면 올바르게 변위의 차원이 된다.

## 7.3. 원점의 특이성과 분포 해석

식 (9)는 $r=0$에서 발산한다. 이는 실제 물체의 변위가 무한하다는 예측이라기보다 힘을
부피가 없는 한 점에 집중시킨 이상화에서 생긴 특이성이다. $r\ne0$에서는 Green 함수가
source가 없는 동차 Navier 방정식을 만족한다. 원점을 포함하는 영역 전체에서 식 (2)를
만족하려면 보통 미분이 아니라 Dirac delta를 포함하는 분포의 의미로 해석해야 한다.

실제 접촉하중처럼 유한한 영역에 분포된 힘 $b_j$에 대해서는

$$
u_i(\boldsymbol x)
=\int_{\mathbb R^3}G_{ij}(\boldsymbol x-\boldsymbol y)
b_j(\boldsymbol y)\,d\boldsymbol y
$$

와 같이 적분하므로 점 특이성이 공간적으로 평균화된다.

# 8. 간단한 검산

Kelvin Green 함수는 다음 성질을 만족한다.

1. **상호대칭성:** $G_{ij}(\boldsymbol r)=G_{ji}(\boldsymbol r)$이다.
2. **공간 반전 대칭성:** $G_{ij}(-\boldsymbol r)=G_{ij}(\boldsymbol r)$이다.
3. **원거리 조건:** $r\rightarrow\infty$이면 $G_{ij}\rightarrow0$이다.
4. **비압축 극한:** $\nu\rightarrow1/2$이면

   $$
   G_{ij}longrightarrow
   \frac{1}{8\pi\mu r}
   \left(\delta_{ij}+\frac{r_i r_j}{r^2}\right),
   $$

   으로 유한하다.
5. **회전 공변성:** 결과가 $\delta_{ij}$와 $r_i r_j/r^2$만으로 구성되므로 좌표축을
   회전해도 동일한 등방성 형태를 유지한다.

# 9. Eshelby 문제와의 연결

Green 함수는 임의의 체적력이 만드는 변위를 중첩하여 계산하는 kernel이다. Eigenstrain을
등가 체적력 $f_j^{\mathrm{eq}}$으로 바꾸면

$$
u_i(\boldsymbol x)
=\int_{\mathbb R^3}G_{ij}(\boldsymbol x-\boldsymbol y)
f_j^{\mathrm{eq}}(\boldsymbol y)\,d\boldsymbol y
$$

로 변위를 구할 수 있다. 균일한 inclusion eigenstrain의 등가 체적력은 계면에 집중되므로
이 체적적분은 inclusion 계면의 표면적분으로 바뀐다. 그 결과를 다시 미분하고 대칭부분을
취하면 구속변형률과 Hill polarization tensor를 얻으며, 최종적으로
$\mathsf S=\mathsf P:\mathsf C$를 계산할 수 있다.

# 10. 요약

| 단계 | 핵심 관계 | 의미 |
|---|---|---|
| 집중력 문제 | $\mathcal L_{ik}G_{kj}=-\delta_{ij}\delta$ | Green 함수의 정의 |
| Fourier 변환 | 미분 $\rightarrow$ $ik_i$ | PDE를 대수문제로 변환 |
| 투영자 분해 | $\mu k^2\mathsf P^{\mathrm T}+(\lambda+2\mu)k^2\mathsf P^{\mathrm L}$ | 횡ㆍ종방향 응답 분리 |
| 역연산 | 식 (4)--(5) | Fourier 공간 Green 함수 계산 |
| 역변환 | $1/k^2\rightarrow1/(4\pi r)$ | 실공간의 $1/r$ 기본해 획득 |
| 결과 | 식 (9) | 3차원 Kelvin Green 함수 |

# 11. 연습 문제

## 문제 1

식 (3)의 Navier 연산자를 $\mathsf P^{\mathrm T}$와 $\mathsf P^{\mathrm L}$로 분해하시오.

<!--
풀이와 해답:
delta_ik=P^T_ik+P^L_ik이고 k_i k_k=k^2 P^L_ik를 사용하면
mu k^2 delta_ik+(lambda+mu)k_i k_k
=mu k^2 P^T_ik+(lambda+2mu)k^2 P^L_ik이다.
-->

## 문제 2

$\partial_i\partial_jr=\delta_{ij}/r-r_i r_j/r^3$임을 확인하시오.

<!--
풀이와 해답:
partial_i r=r_i/r이다. 이를 r_j로 미분하면
partial_j(r_i/r)=delta_ij/r-r_i r_j/r^3를 얻는다.
-->

## 문제 3

식 (9)의 차원을 확인하시오.

<!--
풀이와 해답:
mu의 차원은 force/length^2이고 r의 차원은 length이므로
1/(mu r)의 차원은 length/force이다. 따라서 G_ij F_j는 변위의 차원을 갖는다.
-->

## 문제 4

$\boldsymbol F=F\boldsymbol e_1$이고 관찰점이 $\boldsymbol r=r\boldsymbol e_1$ 또는
$\boldsymbol r=r\boldsymbol e_2$에 있을 때 $u_1$을 각각 구하여 비교하시오.

<!--
풀이와 해답:
r가 e1 방향이면 r_1 r_1/r^2=1이므로
u_1=F/[4 pi mu r]이다. r가 e2 방향이면 r_1=0이므로
u_1=(3-4nu)F/[16 pi mu(1-nu)r]이다.
-->

# 참고문헌

1. W. Thomson, “Note on the integration of the equations of equilibrium of
   an elastic solid,” *Cambridge and Dublin Mathematical Journal*, 3,
   87--89 (1848).
2. T. Mura, *Micromechanics of Defects in Solids*, 2nd ed., Martinus Nijhoff
   Publishers (1987).
3. L. D. Landau and E. M. Lifshitz, *Theory of Elasticity*, 3rd ed.,
   Butterworth-Heinemann (1986).

[구형 Eshelby tensor 유도 자료로 돌아가기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16a_eshelby_sphere_derivation.md %})

[Eigenstrain의 등가 체적력 유도 자료 보기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16b_eigenstrain_equivalent_body_force.md %})
