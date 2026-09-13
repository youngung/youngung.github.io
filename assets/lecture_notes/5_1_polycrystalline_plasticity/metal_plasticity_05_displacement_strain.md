---
layout: distill
title: 변위와 미소변형률
description: 1·2차원 변위장과 미소변형률의 정의 및 예제
target: 학부 고학년
permalink:
featured: true
prerequisite: 벡터와 좌표계, 행렬과 텐서 연산
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


관련 자료는 다음 순서로 읽을 수 있다.

- [변위와 미소변형률]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05_displacement_strain.md %})
- [변위와 미소변형률 연습문제]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %})
- [유한변형의 운동학]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %})
- [물질미분과 ALE 기술법]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %})

# 1. 위치 (position)와 변위 (displacement)

3차원 공간의 위치는 벡터로 표현한다. 정규직교 기저 $\boldsymbol e_1,\boldsymbol e_2,\boldsymbol e_3$에 대해

$$
\boldsymbol x=x_1\boldsymbol e_1+x_2\boldsymbol e_2+x_3\boldsymbol e_3
$$

이다. 같은 물질점의 변형 전 위치를 $\boldsymbol X$, 변형 후 위치를 $\boldsymbol x$라고 하면,
**변위**는 두 위치의 차이다.

$$
\boxed{\boldsymbol u=\boldsymbol x-\boldsymbol X}.
$$

여기서 **물질점 (material point)**은 물체를 이루는 작은 부분을 하나의 점으로 이상화한 것이다.
물체에 표시한 점을 떠올리면 된다. 변형 중에도 같은 물질점을 추적하며,
$\boldsymbol X$와 $\boldsymbol x$는 서로 다른 두 점이 아니라 그 점의 변형 전후 위치다.

# 2. 변위와 변형의 차이

변위는 한 점의 위치 변화이고, **변형 (deformation)**은 물체 내부의 점들 사이에서
거리나 각도가 바뀌는 현상이다. 따라서 변위가 있어도 변형은 없을 수 있다.

| 상황 | 변위 발생 여부 | 변형 발생 여부 |
| ---- | -------------- | -------------- |
| 물체 전체가 평행이동함 | 발생함 | 발생하지 않음 |
| 물체 전체가 회전함 | 회전축 밖의 점에서 발생함 | 발생하지 않음 |
| 물체의 길이가 늘어남 | 일부 또는 모든 점에서 발생함 | 발생함 |

변형률은 절대적인 변위의 크기보다 **이웃한 점들의 상대적인 변위**와 관련된다.

# 3. 강체운동 (rigid body motion)

강체운동은 내부의 거리와 각도를 유지하는 운동으로, 평행이동과 회전이 있다.
평행이동에서는 모든 점의 변위가 같고, 회전에서는 위치에 따라 변위가 달라진다.
두 경우 모두 실제 길이와 각도가 변하지 않으므로 정확한 변형률은 0이다.

뒤에서 배우는 **미소변형률 (infinitesimal strain)**은 변위구배가 작다는 근사에 기초한다.
따라서 강체회전도 회전각이 작을 때만 올바르게 처리한다.
큰 회전에서도 변형률이 0이 되는 이유는 [유한변형률]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#11-유한변형률-finite-strain)에서 확인한다.

# 4. 변위장 (displacement field)

물체의 변위는 점마다 다를 수 있다. 각 점에 변위벡터를 대응시키는 함수를 **변위장**이라고 한다.
우선 변형 전 위치 $\boldsymbol X$를 기준으로 표현하자.

$$
\boldsymbol u=\boldsymbol u(\boldsymbol X),
\qquad
\boldsymbol x(\boldsymbol X)=\boldsymbol X+\boldsymbol u(\boldsymbol X).
$$

이 식은 기준 위치가 $\boldsymbol X$인 물질점의 현재 위치를 알려 준다.
5–9절의 변위장은 모두 이 기준 좌표를 사용하며, 특정 시점의 변형을 다루므로 시간 변수($t$)는 생략한다.
현재 위치 $\boldsymbol x$를 기준으로 표현하는 방법은 [Lagrangian과 Eulerian 기술법]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %})에서 비교한다.

# 5. 1차원 공간에서의 변위와 변형률

1차원에서는 위치 $X,x$와 변위 $u=x-X$를 스칼라로 표현할 수 있다.
막대의 두 물질점 $a,b$에 대해 $X^b>X^a$라고 하자.
초기 길이와 변형 후 길이는 각각

$$
l_0=X^b-X^a,\qquad l=x^b-x^a
$$

이고, 길이 변화는

$$
\Delta l=l-l_0=(x^b-x^a)-(X^b-X^a)=u^b-u^a
$$

이다. **공칭변형률 또는 공학변형률 (engineering strain)**은 이 길이 변화를 초기 길이로 나눈 값이다.

$$
\varepsilon_{\mathrm{eng}}=\frac{\Delta l}{l_0}
=\frac{u^b-u^a}{X^b-X^a}.
$$

두 점의 간격을 0으로 보내면 국소 공칭변형률을 얻는다.

$$
\boxed{\varepsilon_{\mathrm{eng}}(X)
=\lim_{X^b\to X^a}\frac{u^b-u^a}{X^b-X^a}
=\frac{du}{dX}}.
$$

변형 전후 점의 순서가 유지되는 1차원 운동에서 이 관계는 정확하다.
변위구배가 작을 때는 이를 **미소변형률**로 사용한다.
양의 값은 인장, 음의 값은 압축을 나타내며, 변형률은 길이를 길이로 나누므로 무차원이다.

# 6. 1차원 예제

변위장이 기준 위치에 대해 선형으로 증가하는 경우를 생각하자.

$$
u(X)=0.01X,\qquad x(X)=1.01X.
$$

변위구배와 미소변형률은

$$
\varepsilon=\frac{du}{dX}=0.01
$$

이다. 초기 길이가 $100\,\mathrm{mm}$인 구간은 $101\,\mathrm{mm}$가 되어,
$1\%$ 인장을 나타낸다.

다음 두 경우도 비교해 보자. $X$와 $u$는 mm 단위로 측정한다.

| 변위장 | 변위구배 $du/dX$ | 의미 |
| ------ | ---------------- | ---- |
| $u(X)=0$ | $0$ | 위치 변화가 없음 |
| $u(X)=0.02\,\mathrm{mm}$ | $0$ | 모든 점이 같은 양만큼 평행이동함 |

일정한 변위는 변형률을 만들지 않는다. **변위장의 기울기**가 길이 변화와 연결된다는 점이 핵심이다.

# 7. 2차원 공간에서의 변위와 미소변형률

2차원 변위장은 기준 위치에 따라 두 변위 성분을 준다.

$$
[\boldsymbol X]=\begin{bmatrix}X_1\\X_2\end{bmatrix},
\qquad
\boldsymbol u(\boldsymbol X)=\begin{bmatrix}u_1(X_1,X_2)\\u_2(X_1,X_2)\end{bmatrix}.
$$

기준좌표에 대한 **변위구배 (displacement gradient)**를 $\nabla_X\boldsymbol u$[^reference-gradient]로 나타내고, 성분은

$$
(\nabla_X\boldsymbol u)_{ij}=u_{i,j}=\frac{\partial u_i}{\partial X_j}
$$

로 정의한다. 여기서 쉼표 뒤의 $j$는 $X_j$에 대한 미분을 뜻한다.
$\|\nabla_X\boldsymbol u\|\ll1$인 미소변형에서 수직변형률(normal strain) 성분은

$$
\varepsilon_{11}=\frac{\partial u_1}{\partial X_1},
\qquad
\varepsilon_{22}=\frac{\partial u_2}{\partial X_2}
$$

이다. 전단변형률은 먼저 간단한 형상의 각도 변화로 이해해 보자.

높이 $H$인 직사각형의 아랫면을 고정하고, 윗면을 $X_1$방향으로 $\Delta$만큼
이동시키는 **단순전단 (simple shear)**을 생각하자. 높이는 그대로 유지하며,
변위장은

$$
u_1(X_1,X_2)=\frac{\Delta}{H}X_2,
\qquad u_2(X_1,X_2)=0
$$

이다. 원래 수직이던 선분이 수직 방향에서 $\theta$만큼 기울어지면

$$
\tan\theta=\frac{\Delta}{H}
=\frac{\partial u_1}{\partial X_2}
$$

가 된다. 원래 수평이던 선분은 그대로이므로, 처음에 직교하던 두 선분 사이의
각도는 $\pi/2$에서 $\pi/2-\theta$로 줄어든다. 여기서는 $\Delta>0$인 경우를 설명하며,
반대 방향의 전단은 부호로 구분한다.

각도를 **라디안 (radian)**으로 측정하고 $|\theta|\ll1$이면 $\tan\theta\approx\theta$다.
따라서 이 단순전단의 **공학전단변형률 (engineering shear strain)**은

$$
\gamma_{12}=\frac{\Delta}{H}=\tan\theta\approx\theta
$$

로 표현된다. 즉 작은 변형에서는 공학전단변형률을 두 선분 사이의 각도 감소량으로
해석할 수 있다. 큰 각도에서는 $\tan\theta$와 $\theta$를 구분해야 한다.

일반적인 미소변형에서는 두 선분이 모두 기울 수 있다. 원래 $X_2$방향인 선분의
기울어짐에는 $\partial u_1/\partial X_2$가, 원래 $X_1$방향인 선분의 기울어짐에는
$\partial u_2/\partial X_1$이 기여한다. 두 기여를 부호와 함께 합하면

$$
\gamma_{12}=u_{1,2}+u_{2,1}
=\frac{\partial u_1}{\partial X_2}+\frac{\partial u_2}{\partial X_1}
$$

이다. **텐서 전단변형률 (tensor shear strain)**은 이 값의 절반으로 정의한다.

$$
\varepsilon_{12}=\varepsilon_{21}
=\frac12({u_{1,2}+u_{2,1}})=\frac12\left(\frac{\partial u_1}{\partial X_2}
+\frac{\partial u_2}{\partial X_1}\right)
$$

따라서 $\gamma_{12}=2\varepsilon_{12}$이며, 위 단순전단에서는
$\varepsilon_{12}=\tfrac12\tan\theta\approx\theta/2$다.
작은 강체회전에서는 두 기여가 서로 상쇄되어 전단변형률이 0이 된다.

아래 그림은 다음 두 변위장이 만드는 형상을 비교한다.

$$
\text{(a)}\quad u_1=0.2X_1,\quad u_2=0.3X_2,
$$

$$
\text{(b)}\quad u_1=0.1X_1+0.05X_2,\quad u_2=0.2X_1+0.05X_2.
$$

![두 가지 선형 변위장에 의한 2차원 물체의 변형 전후 형상](/assets/img/lecture_notes/displacement/displacement_field_2d_examples.png)

점선은 기준 형상, 실선은 $\boldsymbol x=\boldsymbol X+\boldsymbol u(\boldsymbol X)$로 계산한 현재 형상이다.
빨간 화살표는 기준 형상 오른쪽 위 꼭짓점의 변위다.
형상 차이를 보기 쉽게 계수를 크게 잡았으므로, 이 예제에서 미소변형률 공식으로 구한 값은
정확한 유한변형률과 구분해야 한다. 정확한 길이 변화는 [유한변형률 자료]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %})에서 다룬다.

[^reference-gradient]: $\nabla_X$는 변형 전 기준좌표 $\boldsymbol X=(X_1,X_2,X_3)$에 대한 공간미분 연산자로, $\nabla_X=\boldsymbol e_1\partial/\partial X_1+\boldsymbol e_2\partial/\partial X_2+\boldsymbol e_3\partial/\partial X_3$이다. 스칼라장에 적용하면 기울기 벡터를, 변위 벡터장에 적용하면 변위구배 텐서를 얻는다. 이 자료에서는 $(\nabla_X\boldsymbol u)_{ij}=\partial u_i/\partial X_j$로 정의하므로, 행 $i$는 변위 성분, 열 $j$는 미분하는 기준좌표 방향을 나타낸다. 아래첨자 $X$는 벡터의 성분 첨자가 아니라 **미분에 사용하는 좌표**를 표시한다. 현재좌표 $\boldsymbol x$에 대한 연산자 $\nabla_x$와는 구분하며, 두 구배의 차이는 [Lagrangian과 Eulerian 기술법]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %})에서 설명한다. 2차원 문제에서는 $X_1,X_2$ 방향의 미분만 사용한다.

# 8. 변위구배의 대칭부분과 반대칭부분

7절에서 정의한 변위구배 $\nabla_X\boldsymbol u$는 대칭부분(symmetric part)과 반대칭부분(antisymmetric part; or skew-symmetric part)으로 나눌 수 있다.

$$
\nabla_X\boldsymbol u=\boldsymbol\varepsilon+\boldsymbol\omega,
$$

$$
\boldsymbol\varepsilon
=\frac12\left(\nabla_X\boldsymbol u+(\nabla_X\boldsymbol u)^T\right),
\qquad
\boldsymbol\omega
=\frac12\left(\nabla_X\boldsymbol u-(\nabla_X\boldsymbol u)^T\right).
$$

이 additive 분해 자체는 정확한 행렬 항등식이다. 다만 대칭부분을 변형률, 반대칭부분을 회전으로
해석하는 것은 작은 변위구배를 가정한 근사다. 그 근사에서 $\boldsymbol\varepsilon$은
길이와 각도의 변화를, $\boldsymbol\omega$는 **미소회전 (infinitesimal rotation)**을 나타낸다.
유한회전(finite rotation)과 신장(stretch)의 분리는 [극분해(polar decomposition)]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#12-극분해-polar-decomposition)로 다룬다.

**공학전단변형률 (engineering shear strain)**과 텐서 전단변형률의 관계는

$$
\gamma_{12}=2\varepsilon_{12}
$$

이다. Voigt 표기(Voigt notation)[^voigt-notation]에서 공학전단변형률을 사용할 때 이 2의 계수를 빠뜨리지 않도록 한다.

[^voigt-notation]: Voigt 표기는 대칭인 2차 텐서의 독립 성분을 하나의 열벡터로 배열하는 방법이다. 3차원에서는 독립 성분이 6개이며, 흔히 성분 순서를 $(11,22,33,23,13,12)$로 정한다. 공학전단변형률을 사용하는 변형률 벡터는 $[\boldsymbol\varepsilon]_V=(\varepsilon_{11},\varepsilon_{22},\varepsilon_{33},2\varepsilon_{23},2\varepsilon_{13},2\varepsilon_{12})^T$이고, 대응하는 응력 벡터는 $[\boldsymbol\sigma]_V=(\sigma_{11},\sigma_{22},\sigma_{33},\sigma_{23},\sigma_{13},\sigma_{12})^T$이다. 전단변형률에는 2를 곱하지만 전단응력에는 곱하지 않는다. 이 정의에서는 $[\boldsymbol\sigma]_V^T[\boldsymbol\varepsilon]_V=\boldsymbol\sigma:\boldsymbol\varepsilon$가 되어 응력과 변형률의 텐서 이중내적을 그대로 표현한다. 2차원에서는 $(\varepsilon_{11},\varepsilon_{22},2\varepsilon_{12})^T$로 배열할 수 있다. 성분 순서와 전단성분의 배율은 문헌이나 프로그램에 따라 다르므로, 구성행렬을 사용할 때 같은 관례인지 확인해야 한다. 여기서 열벡터는 텐서 성분을 계산 편의상 배열한 것으로, 공간상의 방향을 나타내는 위치·변위 벡터와는 구분한다.

# 9. 2차원 예제

좌표와 변위를 mm 단위로 측정한다. 다음 균일 변위장에서 미소변형률 텐서를 구하시오.

$$
u_1(X_1,X_2)=0.005X_1,\qquad u_2(X_1,X_2)=-0.005X_2.
$$

두 수직변형률과 두 전단변형률을 계산하고, 어느 방향으로 늘어나거나 줄어드는지 설명하시오.

이 선형 변위장의 계수 $0.005$는 무차원이다. 길이인 $X_1$ 또는 $X_2$에 곱해져
길이인 변위를 만들기 때문이다.

다음은 비균일 변위장이다. $X_1,X_2,u_1,u_2$를 mm 단위로 측정한다.

$$
u_1(X_1,X_2)=\left(0.005\,\mathrm{mm}^{-1}\right)X_1X_2,
\qquad u_2(X_1,X_2)=0.01X_2.
$$

$X_1X_2$의 단위는 $\mathrm{mm}^2$이므로, $u_1$이 mm 단위를 갖도록 그 계수에는
$\mathrm{mm}^{-1}$가 필요하다. 반면 $u_2$의 계수 $0.01$은 무차원이다.
미분 후에도 위치에 곱해지는 계수의 단위를 유지해야 한다. 예를 들어

$$
\varepsilon_{11}=\left(0.005\,\mathrm{mm}^{-1}\right)X_2,
\qquad
\varepsilon_{12}=\left(0.0025\,\mathrm{mm}^{-1}\right)X_1
$$

이며, 각 변형률은 $\mathrm{mm}^{-1}\times\mathrm{mm}=1$로 무차원이 된다.

미소변형률 성분을 위치의 함수로 구하고, $(X_1,X_2)=(2,1)\,\mathrm{mm}$에서 평가하시오.
이 예제는 해당 위치 주변에서 변위구배가 작다고 가정한다.

<span id="13-요약"></span>

# 10. 요약

| 개념                          | 공식                                                                         |
| ----------------------------- | ---------------------------------------------------------------------------- |
| 변위                          | $u = x - X$                                                                  |
| 1차원 미소변형률                  | $\varepsilon = du/dX$                                                        |
| $\boldsymbol{e}_1$방향 수직변형률 | $\varepsilon_{11} = \partial u_1/\partial X_1$                               |
| $\boldsymbol{e}_2$방향 수직변형률 | $\varepsilon_{22} = \partial u_2/\partial X_2$                               |
| 전단변형률                    | $\varepsilon_{12} =0.5(\partial u_1/\partial X_2+\partial u_2/\partial X_1)$ |


<details markdown="1">
<summary>분리 이전 절 링크 안내</summary>

이전 자료의 절 링크로 들어온 경우 아래에서 이동한 내용을 찾을 수 있다.

<span id="10-lagrangian과-eulerian-기술법"></span>

[10. Lagrangian과 Eulerian 기술법]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#10-lagrangian과-eulerian-기술법)

<span id="101-같은-물질점과-같은-공간-위치"></span>

[10.1. 같은 물질점과 같은 공간 위치]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#101-같은-물질점과-같은-공간-위치)

<span id="102-앞의-1차원-인장을-두-기술법으로-표현하기"></span>

[10.2. 앞의 1차원 인장을 두 기술법으로 표현하기]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#102-앞의-1차원-인장을-두-기술법으로-표현하기)

<span id="11-유한변형률-finite-strain"></span>

[11. 유한변형률 (finite strain)]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#11-유한변형률-finite-strain)

<span id="111-변형구배-deformation-gradient"></span>

[11.1. 변형구배 (deformation gradient)]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#111-변형구배-deformation-gradient)

<span id="112-길이-변화로부터-정의하는-유한변형률"></span>

[11.2. 길이 변화로부터 정의하는 유한변형률]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#112-길이-변화로부터-정의하는-유한변형률)

<span id="113-1차원-인장과-강체회전의-비교"></span>

[11.3. 1차원 인장과 강체회전의 비교]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#113-1차원-인장과-강체회전의-비교)

<span id="12-극분해-polar-decomposition"></span>

[12. 극분해 (polar decomposition)]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#12-극분해-polar-decomposition)

<span id="121-회전과-신장의-분리"></span>

[12.1. 회전과 신장의 분리]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#121-회전과-신장의-분리)

<span id="122-신장-후-회전하는-예제"></span>

[12.2. 신장 후 회전하는 예제]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#122-신장-후-회전하는-예제)

<span id="14-연습-문제"></span>

[14. 연습 문제]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#14-연습-문제)

<span id="문제-1"></span>

[문제 1]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-1)

<span id="문제-2"></span>

[문제 2]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-2)

<span id="문제-3"></span>

[문제 3]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-3)

<span id="문제-4"></span>

[문제 4]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-4)

<span id="문제-5"></span>

[문제 5]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-5)

<span id="문제-6"></span>

[문제 6]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-6)

<span id="문제-7"></span>

[문제 7]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-7)

<span id="문제-8"></span>

[문제 8]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-8)

<span id="문제-9"></span>

[문제 9]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-9)

<span id="문제-10"></span>

[문제 10]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-10)

<span id="문제-11"></span>

[문제 11]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-11)

<span id="문제-12"></span>

[문제 12]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-12)

<span id="문제-13"></span>

[문제 13]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-13)

<span id="문제-14"></span>

[문제 14]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-14)

<span id="문제-15"></span>

[문제 15]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-15)

<span id="문제-16"></span>

[문제 16]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %}#문제-16)

<span id="부록-a-물질미분-material-derivative"></span>

[부록 A. 물질미분 (material derivative)]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %}#부록-a-물질미분-material-derivative)

<span id="a1-물질점을-따라-관찰하는-변화율"></span>

[A.1. 물질점을 따라 관찰하는 변화율]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %}#a1-물질점을-따라-관찰하는-변화율)

<span id="a2-시간에-따라-변하지-않는-온도장에서의-물질미분"></span>

[A.2. 시간에 따라 변하지 않는 온도장에서의 물질미분]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %}#a2-시간에-따라-변하지-않는-온도장에서의-물질미분)

<span id="a3-공간과-시간에-모두-의존하는-온도장"></span>

[A.3. 공간과 시간에 모두 의존하는 온도장]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %}#a3-공간과-시간에-모두-의존하는-온도장)

<span id="a4-속도의-물질미분과-가속도"></span>

[A.4. 속도의 물질미분과 가속도]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %}#a4-속도의-물질미분과-가속도)

<span id="부록-b-ale-기술법"></span>

[부록 B. ALE 기술법]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %}#부록-b-ale-기술법)

</details>

<span id="fn:squared-length"></span>
<span id="fnref:squared-length"></span>

[유한변형률 각주: 선분의 제곱 길이]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#fn:squared-length)

<span id="fn:line-element-quadratic-form"></span>
<span id="fnref:line-element-quadratic-form"></span>

[유한변형률 각주: 이차형식의 계산]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %}#fn:line-element-quadratic-form)
