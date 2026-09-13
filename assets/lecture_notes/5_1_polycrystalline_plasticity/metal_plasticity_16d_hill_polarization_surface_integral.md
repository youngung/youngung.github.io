---
layout: distill
title: Hill polarization tensor의 표면적분 유도
description: Green 함수와 등가 체적력으로부터 Hill polarization tensor의 표면적분 표현을 얻는 과정
target: 대학원 입문
permalink:
featured: false
prerequisite: 선형 탄성, Kelvin Green 함수, eigenstrain의 등가 체적력
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
- [2. 표면적분 표현의 단계별 유도](#2-표면적분-표현의-단계별-유도)
- [3. 유도의 핵심](#3-유도의-핵심)

# 1. 이 보충자료의 질문

구형 inclusion의 Eshelby tensor를 계산할 때 Hill polarization tensor는

$$
\varepsilon^c_{ij}=P_{ijkl}\sigma^*_{kl}
$$

로 eigenstress와 구속변형률을 연결한다. 이 자료에서는 Green 함수에 의한 변위 표현에서
출발하여 $P_{ijkl}$의 표면적분식이 어떻게 나오며, 식 앞의 계수가 왜 $1/4$인지
설명한다. 무한하고 균질한 등방성 선형탄성체, 균일한 inclusion eigenstrain 및 완전접합을
가정한다.

# 2. 표면적분 표현의 단계별 유도

Polarization tensor의 표면적분 표현을 단계별로 유도한다. 먼저 이 절에서 반복해서
사용하는 두 위치벡터를 구분하자.

- $\boldsymbol x$는 변위 $\boldsymbol u(\boldsymbol x)$, 구속변형률
  $\boldsymbol\varepsilon^c(\boldsymbol x)$ 및 polarization tensor
  $\mathsf P(\boldsymbol x)$를 구하려는 **관찰점(field point)**이다. Inclusion 내부의
  polarization tensor를 구할 때는 $\boldsymbol x\in\Omega$로 둔다.
- $\boldsymbol y$는 등가 체적력 또는 계면 traction이 작용하는 **하중점(source
  point)**이다. 적분을 수행하는 동안 $\boldsymbol y$가 inclusion의 체적 $V$ 또는 계면
  $\partial\Omega$ 위를 움직이므로 적분변수는 $\boldsymbol y$다.

두 점을 연결하는 상대위치벡터는

$$
\boldsymbol r=\boldsymbol x-\boldsymbol y
$$

이며, Green 함수 $G_{ip}(\boldsymbol x-\boldsymbol y)$는 $\boldsymbol y$에 가한
$p$방향 단위력이 $\boldsymbol x$에서 만드는 $i$방향 변위를 뜻한다. 또한
$\boldsymbol n(\boldsymbol y)$과 $dS_y$는 각각 source point $\boldsymbol y$에서의
바깥쪽 단위법선과 미소면적이다. 이후의 표기

$$
G_{ip,j}
=\frac{\partial G_{ip}(\boldsymbol x-\boldsymbol y)}{\partial x_j}
$$

에서 쉼표 뒤의 첨자는 적분변수 $\boldsymbol y$가 아니라 field point
$\boldsymbol x$에 대한 미분을 나타낸다.

이제 inclusion 내부의 일정한 eigenstress를 $\sigma^*_{pq}$라고 하면, 앞 절의 등가
체적력은 계면에 집중된

$$
f_p^{\mathrm{eq}}(\boldsymbol y)
=\sigma^*_{pq}n_q(\boldsymbol y)\delta_{\partial\Omega}(\boldsymbol y)
$$

로 쓸 수 있다. Green 함수와 등가 체적력의 convolution은

$$
u_i(\boldsymbol x)
=\int_V G_{ip}(\boldsymbol x-\boldsymbol y)
f_p^{\mathrm{eq}}(\boldsymbol y)\,dV_y
$$

이다. 이 적분이 변위를 주는 이유는 Green 함수의 정의와 선형탄성의 중첩원리에서 알 수
있다. $G_{ip}(\boldsymbol x-\boldsymbol y)$는 $\boldsymbol y$에서 $p$방향으로 작용하는
**단위 집중력**이 $\boldsymbol x$에 만드는 $i$방향 변위다. Source point
$\boldsymbol y$ 주위의 미소체적 $dV_y$에 작용하는 등가 힘은

$$
dF_p=f_p^{\mathrm{eq}}(\boldsymbol y)\,dV_y
$$

이므로, 이 미소 힘이 만드는 변위 증분은

$$
du_i(\boldsymbol x)
=G_{ip}(\boldsymbol x-\boldsymbol y)dF_p
=G_{ip}(\boldsymbol x-\boldsymbol y)
f_p^{\mathrm{eq}}(\boldsymbol y)\,dV_y
$$

이다. 선형탄성에서는 서로 다른 위치의 하중이 만드는 변위를 그대로 더할 수 있다.
따라서 모든 source point $\boldsymbol y$의 변위 증분을 적분하면 위의 $u_i$가 된다.

같은 사실을 Navier 방정식으로도 확인할 수 있다. Navier 연산자를

$$
\mathcal L_{mi}
=\mu\delta_{mi}\nabla^2
+(\lambda+\mu)\frac{\partial^2}{\partial x_m\partial x_i}
$$

라고 쓰면, 현재 부호 관례에서 Green 함수는

$$
\mathcal L_{mi}^{(\boldsymbol x)}
G_{ip}(\boldsymbol x-\boldsymbol y)
=-\delta_{mp}\delta(\boldsymbol x-\boldsymbol y)
$$

를 만족한다. 위의 적분 표현에 $\mathcal L_{mi}^{(\boldsymbol x)}$를 작용시키면

$$
\begin{aligned}
\mathcal L_{mi}^{(\boldsymbol x)}u_i(\boldsymbol x)
&=\int_V
\mathcal L_{mi}^{(\boldsymbol x)}G_{ip}(\boldsymbol x-\boldsymbol y)
f_p^{\mathrm{eq}}(\boldsymbol y)\,dV_y\\
&=-\int_V\delta_{mp}\delta(\boldsymbol x-\boldsymbol y)
f_p^{\mathrm{eq}}(\boldsymbol y)\,dV_y\\
&=-f_m^{\mathrm{eq}}(\boldsymbol x).
\end{aligned}
$$

즉 이 적분으로 얻은 변위는

$$
\mathcal L_{mi}u_i+f_m^{\mathrm{eq}}=0
$$

이라는 원래의 평형방정식을 정확히 만족한다. Green 함수는 Navier 연산자의 역연산자
역할을 하는 셈이다. 또한 무한하고 균질한 재료에서는 응답이 $\boldsymbol x$와
$\boldsymbol y$ 각각이 아니라 두 점의 차이 $\boldsymbol x-\boldsymbol y$에만 의존하므로,
이 적분을 특별히 convolution이라고 부른다.

이제 surface delta의 성질을 사용하면 체적적분이 계면의 표면적분으로 바뀐다.

$$
u_i(\boldsymbol x)
=\int_{\partial\Omega}
G_{ip}(\boldsymbol x-\boldsymbol y)
\sigma^*_{pq}n_q(\boldsymbol y)\,dS_y.
$$

균일한 eigenstrain과 일정한 탄성계수를 가정했으므로 $\sigma^*_{pq}$는
$\boldsymbol y$에 무관한 상수이며 적분 밖으로 꺼낼 수 있다. 따라서

$$
u_i(\boldsymbol x)
=\left[
\int_{\partial\Omega}
G_{ip}(\boldsymbol x-\boldsymbol y)n_q\,dS_y
\right]\sigma^*_{pq}.
$$

구속변형률은 변위 gradient의 대칭부분이므로

$$
\varepsilon^c_{ij}
=\frac{1}{2}(u_{i,j}+u_{j,i})
$$

이다. 여기서 $u_{i,j}$는 field point의 좌표 $x_j$에 대한 $u_i$의 미분,

$$
u_{i,j}=\frac{\partial u_i}{\partial x_j}
$$

을 뜻한다. 표면적분에서 적분변수는 source point $\boldsymbol y$다. 따라서
$n_q(\boldsymbol y)$, $dS_y$ 및 적분영역 $\partial\Omega$는 field point
$\boldsymbol x$를 움직여도 변하지 않는다. $\boldsymbol x$에 의존하는 항은
$G_{ip}(\boldsymbol x-\boldsymbol y)$뿐이므로 미분을 적분 안으로 옮기면

$$
\begin{aligned}
u_{i,j}(\boldsymbol x)
&=\frac{\partial}{\partial x_j}
\left[
\int_{\partial\Omega}
G_{ip}(\boldsymbol x-\boldsymbol y)n_q\,dS_y
\right]\sigma^*_{pq}\\
&=\int_{\partial\Omega}
\frac{\partial G_{ip}(\boldsymbol x-\boldsymbol y)}{\partial x_j}
n_q\,dS_y\,\sigma^*_{pq}\\
&=\int_{\partial\Omega}
G_{ip,j}(\boldsymbol x-\boldsymbol y)n_q\,dS_y\,\sigma^*_{pq}.
\end{aligned}
$$

따라서 $G_{ip,j}$는 새로운 Green 함수가 아니라 기존 $G_{ip}$를 관찰점 좌표
$x_j$로 미분한 것이다. 마찬가지로 먼저 변위의 자유첨자 $i$를 $j$로 바꾸면

$$
u_j(\boldsymbol x)
=\left[
\int_{\partial\Omega}
G_{jp}(\boldsymbol x-\boldsymbol y)n_q\,dS_y
\right]\sigma^*_{pq}
$$

이고, 이를 $x_i$로 미분하면

$$
u_{j,i}(\boldsymbol x)
=\int_{\partial\Omega}
G_{jp,i}(\boldsymbol x-\boldsymbol y)n_q\,dS_y\,\sigma^*_{pq}
$$

를 얻는다. 즉 $G_{ip,j}$는 $u_{i,j}$에서, $G_{jp,i}$는 $u_{j,i}$에서 각각
나타난다. 이 두 식을 변형률 정의에 대입하면

$$
\varepsilon^c_{ij}
=\frac{1}{2}\int_{\partial\Omega}
\left(G_{ip,j}+G_{jp,i}\right)n_q\,dS_y\,
\sigma^*_{pq}
$$

를 얻는다. 이 식만으로도 eigenstress에서 구속변형률로 가는 선형 관계가 보인다. 다만
eigenstress는 대칭텐서이므로 $\sigma^*_{pq}=\sigma^*_{qp}$이다. 따라서 그 앞의 계수에서
$p$와 $q$를 바꾼 식을 평균해도 contraction의 값은 변하지 않는다.

$$
\begin{aligned}
\varepsilon^c_{ij}
=\frac{1}{4}\int_{\partial\Omega}
\big[&
(G_{ip,j}+G_{jp,i})n_q\\
&+(G_{iq,j}+G_{jq,i})n_p
\big]\,dS_y\,\sigma^*_{pq}.
\end{aligned}
$$

이 평균은 polarization tensor가 마지막 두 첨자에 대해
$P_{ijpq}=P_{ijqp}$의 대칭성을 명시적으로 갖게 한다. 이제 더미 첨자 $p,q$를 $k,l$로
바꾸고, 등방성 무한체 Green 함수의 상호대칭성 $G_{ij}=G_{ji}$를 사용하면

$$
\varepsilon^c_{ij}=P_{ijkl}\sigma^*_{kl}
$$

에서 polarization tensor를 다음과 같이 정의할 수 있다.

$$
\begin{aligned}
P_{ijkl}(\boldsymbol x)
=\frac{1}{4}\int_{\partial\Omega}
\big[&
(G_{ki,j}+G_{kj,i})n_l\\
&+(G_{li,j}+G_{lj,i})n_k
\big]\,dS_y.
\end{aligned}
\tag{4}
$$

식 (4)의 앞쪽 첨자 $i,j$는 결과인 구속변형률의 성분을, 뒤쪽 첨자 $k,l$은 입력인
eigenstress의 성분을 나타낸다. 계수 $1/4$는 변형률을 만들 때 $i,j$를 대칭화하여 생기는
$1/2$와 대칭 eigenstress에 맞춰 $k,l$을 다시 대칭화하여 생기는 $1/2$의 곱이다.
$n_i$는 inclusion 경계의 바깥쪽 단위법선이다.

Green 함수의 부호를 정의하는 방식에 따라 중간식의 부호가 반대로 보일 수 있지만,
등가 체적력, Green 함수 및 법선의 정의를 일관되게 사용하면 식 (2)의
$\mathsf S=\mathsf P:\boldsymbol C$와 같은 최종 관계를 얻는다.

# 3. 유도의 핵심

전체 과정은 다음과 같이 정리할 수 있다.

$$
\text{eigenstress}
\longrightarrow
\text{계면의 등가 체적력}
\longrightarrow
\text{Green 함수에 의한 변위}
\longrightarrow
\text{변위 gradient의 대칭부분}
\longrightarrow
\mathsf P.
$$

Surface delta는 하중의 위치를 inclusion 계면으로 제한하고, Green 함수는 각 계면
점하중의 변위응답을 제공한다. 이후 $i,j$와 $k,l$을 각각 대칭화하면 대칭 변형률과 대칭
응력 사이를 연결하는 4차 polarization tensor가 얻어진다.

[구형 Eshelby tensor 유도 자료로 돌아가기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16a_eshelby_sphere_derivation.md %})

[Eigenstrain의 등가 체적력 유도 자료 보기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16b_eigenstrain_equivalent_body_force.md %})

[Kelvin Green 함수 유도 자료 보기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16c_kelvin_green_function_derivation.md %})
