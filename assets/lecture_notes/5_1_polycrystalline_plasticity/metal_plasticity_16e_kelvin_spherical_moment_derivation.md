---
layout: distill
title: Kelvin Green 함수 미분과 구면 모멘트 적분
description: 구형 inclusion의 Hill polarization tensor 계산에 필요한 미분과 등방 구면 적분의 상세 유도
target: 대학원 입문
permalink:
featured: false
prerequisite: Kelvin Green 함수, 텐서와 좌표변환, 구형 inclusion
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
- [2. Kelvin Green 함수의 미분](#2-kelvin-green-함수의-미분)
- [3. 구면 모멘트만 남는 과정](#3-구면-모멘트만-남는-과정)
- [4. 2차 구면 모멘트](#4-2차-구면-모멘트)
- [5. 4차 구면 모멘트](#5-4차-구면-모멘트)

# 1. 이 보충자료의 목표

[구형 inclusion의 Eshelby tensor 유도 자료]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16a_eshelby_sphere_derivation.md %})의
6절에서는 Kelvin Green 함수를 미분한 결과와 구면 모멘트 적분 공식을 사용한다.
이 보충자료에서는 다음 두 계산을 자세히 유도한다.

1. $1/r$과 $r_pr_q/r^3$을 field point $x_j$에 대해 미분하는 과정
2. 2차 및 4차 법선벡터 구면 모멘트를 Kronecker delta로 나타내는 과정

# 2. Kelvin Green 함수의 미분

Kelvin Green 함수를

$$
G_{pq}(\boldsymbol r)
=\alpha\frac{\delta_{pq}}{r}
+\beta\frac{r_p r_q}{r^3},
\qquad
\alpha=\frac{\lambda+3\mu}{8\pi\mu(\lambda+2\mu)},
\qquad
\beta=\frac{\lambda+\mu}{8\pi\mu(\lambda+2\mu)}
$$

로 쓰자. 여기서 $p,q$는 Green 함수 성분을 나타내는 자유첨자이고, $a$는 구형
inclusion의 반지름이다. 첨자와 반지름을 구별하기 위해 성분 첨자로 $a,b$를
사용하지 않는다.

$\boldsymbol r=\boldsymbol x-\boldsymbol y$이고 source point $\boldsymbol y$를
고정하면 $r_m=x_m-y_m$이므로

$$
\frac{\partial r_m}{\partial x_j}=\delta_{mj}.
$$

한편 $r$은 벡터 $\boldsymbol r$의 크기이므로

$$
r=\lVert\boldsymbol r\rVert=(r_mr_m)^{1/2}.
$$

여기서 $m$은 합산되는 더미첨자이다. 연쇄법칙과
$\partial(r_mr_m)/\partial x_j=2r_m\delta_{mj}=2r_j$를 이용하면

$$
\frac{\partial r}{\partial x_j}
=\frac12(r_mr_m)^{-1/2}(2r_j)
=\frac{r_j}{r}
$$

을 얻는다. 따라서

$$
\frac{\partial}{\partial x_j}\left(\frac{1}{r}\right)
=-r^{-2}\frac{\partial r}{\partial x_j}
=-\frac{r_j}{r^3}.
$$

두 번째 항은 $r_pr_q/r^3=r_pr_qr^{-3}$로 쓴 뒤 곱의 미분법을 적용한다.

$$
\begin{aligned}
\frac{\partial}{\partial x_j}\left(\frac{r_p r_q}{r^3}\right)
&=\frac{\partial r_p}{\partial x_j}r_qr^{-3}
+r_p\frac{\partial r_q}{\partial x_j}r^{-3}
+r_pr_q\frac{\partial r^{-3}}{\partial x_j}\\
&=\delta_{pj}r_qr^{-3}
+r_p\delta_{qj}r^{-3}
-3r_pr_qr^{-4}\frac{\partial r}{\partial x_j}\\
&=\frac{\delta_{pj}r_q+\delta_{qj}r_p}{r^3}
-3\frac{r_pr_qr_j}{r^5}.
\end{aligned}
$$

그러므로

$$
G_{pq,j}
=-\alpha\delta_{pq}\frac{r_j}{r^3}
+\beta\frac{\delta_{pj}r_q+\delta_{qj}r_p}{r^3}
-3\beta\frac{r_pr_qr_j}{r^5}.
$$

# 3. 구면 모멘트만 남는 과정

구의 중심을 field point로 택하면 $\boldsymbol r=-a\boldsymbol n$이다. 따라서
$r_p=-an_p$, $r_q=-an_q$, $r=\lVert\boldsymbol r\rVert=a$이고

$$
G_{pq,j}
=\frac{1}{a^2}\left[
\alpha\delta_{pq}n_j
-\beta(\delta_{pj}n_q+\delta_{qj}n_p)
+3\beta n_pn_qn_j
\right].
$$

Hill polarization tensor의 표면적분에 필요한 조합은

$$
\begin{aligned}
G_{ki,j}+G_{kj,i}
=\frac{1}{a^2}\big[&
(\alpha-\beta)(\delta_{ki}n_j+\delta_{kj}n_i)
-2\beta\delta_{ij}n_k
+6\beta n_in_jn_k\big],\\
G_{li,j}+G_{lj,i}
=\frac{1}{a^2}\big[&
(\alpha-\beta)(\delta_{li}n_j+\delta_{lj}n_i)
-2\beta\delta_{ij}n_l
+6\beta n_in_jn_l\big]
\end{aligned}
$$

이다. 첫째 식에 $n_l$, 둘째 식에 $n_k$를 곱하고
$dS_y=a^2d\Omega$를 사용하면 $a^{-2}$와 $a^2$가 소거되어

$$
\begin{aligned}
P_{ijkl}=\frac14\int_{S^2}\big\{&
(\alpha-\beta)(
\delta_{ki}n_jn_l+\delta_{kj}n_in_l
+\delta_{li}n_jn_k+\delta_{lj}n_in_k)\\
&-4\beta\delta_{ij}n_kn_l
+12\beta n_in_jn_kn_l
\big\}\,d\Omega
\end{aligned}
$$

를 얻는다. 따라서 실제로 필요한 적분은 $n_in_j$의 2차 구면 모멘트와
$n_in_jn_kn_l$의 4차 구면 모멘트뿐이다.

# 4. 2차 구면 모멘트

$$
I_{ij}=\int_{S^2}n_in_j\,d\Omega
$$

라고 하자. 구면에는 선호방향이 없으므로 어떤 방향을 좌표축으로 선택하더라도
$I_{ij}$의 성분 형태가 같아야 한다. 여기서 회전은 물체를 실제로 돌리는 능동회전이
아니라, 동일한 텐서를 회전된 좌표계에서 표현하는 **수동적 좌표계 회전**이다.
좌표변환을 $\boldsymbol Q\in SO(3)$[^so3]로 나타내면

$$
I'_{ij}=Q_{ip}Q_{jq}I_{pq},
\qquad
\boldsymbol I'=\boldsymbol Q\cdot \boldsymbol I\cdot \boldsymbol Q^{\mathsf T}.
$$

단위구와 $d\Omega$는 좌표축 방향에 의존하지 않으므로 모든 수동적 좌표계 회전에
대해 $\boldsymbol I'=\boldsymbol I$이어야 한다. $\boldsymbol I$는 대칭텐서이므로
세 고유방향과 세 고유값을 갖는다. 고유값이 서로 다르면 해당 고유방향이 다른
방향과 구별되는 선호방향이 된다. 따라서 세 고유값은 모두 같은 값 $A$이고

$$
I_{ij}=A\delta_{ij}
$$

이다. 양변을 축약하면

$$
I_{ii}=\int_{S^2}n_in_i\,d\Omega
=\int_{S^2}1\,d\Omega=4\pi,
\qquad
A\delta_{ii}=3A
$$

이므로 $A=4\pi/3$이다. 따라서

$$
\int_{S^2}n_in_j\,d\Omega=\frac{4\pi}{3}\delta_{ij}.
$$

$i\ne j$인 성분은 한 좌표의 부호를 반전하는 대칭점끼리 상쇄되어 0이 된다.

[^so3]: $SO(3)$는 3차원 공간의 **특수 직교군**(special orthogonal group)을
    뜻한다. $\boldsymbol Q\in SO(3)$는
    $\boldsymbol Q^{\mathsf T}\cdot \boldsymbol Q=\boldsymbol 1$과
    $\det\boldsymbol Q=+1$을 동시에 만족한다는 의미이다. 첫째 조건은 길이와 각도가
    보존됨을 뜻하고, 둘째 조건은 거울반사를 제외한다. 따라서 $\boldsymbol Q$는
    반사를 포함하지 않는 순수한 3차원 좌표계 회전을 나타낸다.

# 5. 4차 구면 모멘트

$$
I_{ijkl}=\int_{S^2}n_in_jn_kn_l\,d\Omega
$$

도 좌표축의 방향을 바꾸어도 성분 배열이 같은 등방 4차 텐서이다. 등방 텐서는 특정
방향을 나타내는 벡터를 포함할 수 없으므로, 네 자유첨자를 방향과 무관하게 연결하려면
Kronecker delta 두 개를 사용해야 한다. 가능한 기본형은

$$
\delta_{ij}\delta_{kl},
\qquad
\delta_{ik}\delta_{jl},
\qquad
\delta_{il}\delta_{jk}
$$

의 세 가지뿐이다.[^index-pairings] 따라서 가장 일반적인 등방 4차 텐서는

$$
I_{ijkl}
=B_1\delta_{ij}\delta_{kl}
+B_2\delta_{ik}\delta_{jl}
+B_3\delta_{il}\delta_{jk}
$$

이다. 회전 불변성만으로는 세 계수가 같아야 할 필요가 없다. 그러나
$n_in_jn_kn_l$은 네 첨자의 어떠한 순열에도 변하지 않는 완전대칭을 가지므로
$B_1=B_2=B_3=B$이고

$$
I_{ijkl}=B(\delta_{ij}\delta_{kl}
+\delta_{ik}\delta_{jl}
+\delta_{il}\delta_{jk})
$$

로 쓸 수 있다. $i=j$, $k=l$로 두 번 축약하면

$$
I_{iikk}=\int_{S^2}(n_in_i)(n_kn_k)\,d\Omega=4\pi
$$

이고

$$
B(\delta_{ii}\delta_{kk}
+\delta_{ik}\delta_{ik}
+\delta_{ik}\delta_{ki})
=B(9+3+3)=15B
$$

이므로 $B=4\pi/15$이다. 따라서

$$
\int_{S^2}n_in_jn_kn_l\,d\Omega
=\frac{4\pi}{15}(\delta_{ij}\delta_{kl}
+\delta_{ik}\delta_{jl}
+\delta_{il}\delta_{jk}).
$$

[^index-pairings]: 먼저 $i$와 짝을 이룰 첨자를 고르면 $j$, $k$, $l$의 세 가지
    선택지가 있다. $i$의 짝이 정해지면 남은 두 첨자는 자동으로 한 쌍이 되므로
    $(ij)(kl)$, $(ik)(jl)$, $(il)(jk)$를 얻는다. 쌍 안의 순서나 두 쌍의 순서를
    바꾸어도 새로운 조합은 생기지 않는다. 예를 들어
    $\delta_{ji}\delta_{lk}=\delta_{ij}\delta_{kl}$인데, 이는 Kronecker delta가
    대칭이고 스칼라 곱의 순서는 결과에 영향을 주지 않기 때문이다.

[구형 Eshelby tensor 유도 자료로 돌아가기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_16a_eshelby_sphere_derivation.md %})
