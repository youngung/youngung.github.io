---
layout: distill
title: 주응력과 편차응력
description: 주응력 공간, 편차응력과 von Mises 등가응력
target: 대학원
permalink:
featured: true
prerequisite: 좌표변환, 응력 텐서
toc: false

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

**목차**

* TOC
{:toc}

# 1. 좌표 변환(coordinate transformation)과 주 공간 (principal space)

- 앞서 좌표 변환 방법에 대해서 배웠다.

- 그 중, 주어진 응력 상태에 대해 특별한 좌표계를 생각해보자. 우선 아래와 같은 임의의 응력상태
 를 나타내는 응력텐서가 있다고 하자. 이 응력 텐서가 표현된 좌표계가 $(\boldsymbol e_1, \boldsymbol e_2,\boldsymbol e_3)$ 축으로 구성되어 있을 때, 아래 구성성분 값을 가진다고 하자.

- 즉,
$$
\boldsymbol{\sigma}=\sum_{i=1}^3\sum_{j=1}^3\sigma_{ij}\boldsymbol{e}_i\otimes\boldsymbol{e}_j
$$

- 여기에 좌표변환행렬 $\boldsymbol{R}$ 를 통해 또 다른 좌표축 $(\tilde{\boldsymbol e}_1, \tilde{\boldsymbol e}_2,\tilde{\boldsymbol e}_3)$에 대한 구성성분값을 아래와 같이 구할 수 있다.

$$
\tilde{\sigma}_{ij}=R_{ik}R_{jl} \sigma_{kl}
$$

- 위 성분값들이 아래와 같이 행렬로 표기 될 수 있다.

$$
\tilde{\sigma}=

\begin{bmatrix}
\tilde{\sigma}_{11} & \tilde{\sigma}_{12} &\tilde{\sigma}_{13}\\
\tilde{\sigma}_{21} & \tilde{\sigma}_{22} &\tilde{\sigma}_{23}\\
\tilde{\sigma}_{31} & \tilde{\sigma}_{32} &\tilde{\sigma}_{33}\\
\end{bmatrix}
$$

- 만약 아래와 같이, 전단 성분값이 모두 0이 된다면, 좌표축 $(\tilde{\boldsymbol e}_1, \tilde{\boldsymbol e}_2,\tilde{\boldsymbol e}_3)$로 구성된 공간을 우리는 해당 응력 텐서의 '주 공간'(principal space)이라 부른다

$$
\tilde{\sigma}_{12}=\tilde{\sigma}_{23}=\tilde{\sigma}_{13}=0
$$

- 이런 경우, 좌표축 $(\tilde{\boldsymbol e}_1, \tilde{\boldsymbol e}_2,\tilde{\boldsymbol e}_3)$을
 주축 (principal axis)라고도 부른다.


# 2. 주 응력 (principal stress)

- 따라서, 주어진 한 응력 텐서의 주 응력공간에서 그 성분 값들은 아래와 같이 매트릭스 형태를 가지게 된다.

$$
\begin{bmatrix}
\tilde{\sigma}_{11} & 0 &0\\
0&\tilde{\sigma}_{22} & 0\\
0&0 &\tilde{\sigma}_{33}\\
\end{bmatrix}
$$

- 이를 줄여 아래와 같이 표현한다.

$$
\begin{bmatrix}
\sigma_{1} & 0 &0\\
0&\sigma_{2} & 0\\
0&0 &\sigma_{3}\\
\end{bmatrix}
$$

- 이 성분 값 $\sigma_{1}, \sigma_{2}, \sigma_{3}$를 주 응력값(principal value)이라 부른다.

- 주 공간에서 얻어진 응력 값 $\sigma_1,\sigma_2,\sigma_3$로 이루어진 공간을 '주 응력 공간' (principal stress space)라 부른다.

# 3. 주 응력 값 구하기

주축의 단위벡터를 $\boldsymbol n$, 그 면에 작용하는 주응력을 $\lambda$라 하면
면력은 법선과 평행하므로

$$
\boldsymbol\sigma\boldsymbol n=\lambda\boldsymbol n,
\qquad
(\boldsymbol\sigma-\lambda\boldsymbol I)\boldsymbol n=\boldsymbol0
$$

이다. 따라서 주응력은 응력텐서의 고유값(eigenvalue), 주축은 대응하는 정규화된
고유벡터(eigenvector)이다. $\boldsymbol n\ne\boldsymbol0$인 해가 있으려면 계수행렬이
특이행렬이어야 하므로

$$
\det(\boldsymbol \sigma - \lambda \boldsymbol I)=0
$$

이어야 한다. 행렬식이 0이 아니면 역행렬을 곱해 $\boldsymbol n=\boldsymbol0$만 얻기 때문이다.

## 3.1. 3차 특성방정식과 응력 불변량

대칭인 3차원 응력텐서에 대해 행렬식을 전개하면

$$
\boxed{\lambda^3-I_1\lambda^2+I_2\lambda-I_3=0}
$$

을 얻는다. 계수는 응력 불변량(stress invariants)이며

$$
\begin{aligned}
I_1&=\operatorname{tr}(\boldsymbol\sigma),\\
I_2&=\frac12\left[(\operatorname{tr}\boldsymbol\sigma)^2
-\operatorname{tr}(\boldsymbol\sigma^2)\right],\\
I_3&=\det\boldsymbol\sigma
\end{aligned}
$$

이다. 세 근이 $\sigma_1,\sigma_2,\sigma_3$이며, 좌표축을 회전해도 이 값들과
$I_1,I_2,I_3$는 변하지 않는다. 실수 대칭행렬이므로 세 고유값은 모두 실수이고,
서로 다른 고유값에 대응하는 주축은 서로 직교한다.

## 3.2. 계산 예제와 최대 전단응력

다음 응력상태를 생각하자.

$$
[\boldsymbol\sigma]=
\begin{bmatrix}80&20&0\\20&50&0\\0&0&-30\end{bmatrix}\,\mathrm{MPa}.
$$

특성방정식은

$$
(\lambda-90)(\lambda-40)(\lambda+30)=0
$$

으로 분해되므로 주응력은 $(90,40,-30)\,\mathrm{MPa}$이다. 부호를 포함해
$\sigma_1\ge\sigma_2\ge\sigma_3$으로 정렬하면 3차원 최대 전단응력은

$$
\boxed{\tau_{\max}=\frac{\sigma_1-\sigma_3}{2}}
=60\,\mathrm{MPa}
$$

이다. 평면 내 두 주응력만 사용한 $(90-40)/2=25\,\mathrm{MPa}$와 구분해야 한다.

# 4. 편차 응력(deviatoric stress)

- 모든 응력 상태는 편차 응력($\boldsymbol s$)과, 평균응력($\sigma_m \boldsymbol I$)으로 구분할 수 있다.

$$
\boldsymbol \sigma= \sigma_m \boldsymbol I + \boldsymbol s
$$

- $\boldsymbol I$는 랭크2 단위 텐서이며, 아래와 같은 매트릭스 형태로 표현된다.

$$
[\boldsymbol I] = \begin{bmatrix}1 &0 &0 \\0 &1 &0 \\0 &0 &1 \\\end{bmatrix}
$$

- 평균 응력값 $\sigma_m$은 아래와 같이 정의된다.

$$
\sigma_m = \frac{1}{3}(\sigma_{11}+\sigma_{22}+\sigma_{33})=\frac{1}{3}tr(\boldsymbol\sigma)
$$

- 편차 응력은 응력텐서에서 평균 응력을 뺀 나머지다.

$$
\boldsymbol s = \boldsymbol \sigma - \sigma_m \boldsymbol I
$$

따라서 $\operatorname{tr}(\boldsymbol s)=0$이다. 주응력 좌표계에서는 편차 주응력이

$$
s_i=\sigma_i-\sigma_m,
\qquad
s_1+s_2+s_3=0
$$

을 만족한다. 평균응력은 정수압축 방향 $(1,1,1)$의 성분이고, 편차응력은 그 축에
수직인 편차응력 평면 위의 성분으로 해석할 수 있다.

## 4.1. 평면응력에서의 주의점

평면응력은 $\sigma_{33}=\sigma_{13}=\sigma_{23}=0$인 **3차원 응력상태**다.
따라서 평균응력은 면내 성분만 더해 2로 나누는 것이 아니라

$$
\sigma_m=\frac{\sigma_{11}+\sigma_{22}+0}{3}
$$

으로 계산한다. 이때 $s_{33}=-\sigma_m$이므로 평면응력이라도 편차응력의 면외
성분은 일반적으로 0이 아니다.

# 5. Von Mises 등가 응력

이후 절에서는 주응력과 편차응력의 활용을 미리 살펴본다. 항복 조건의 물리적 의미는
[소성 항복]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_12_plastic_yield.md %})에서 이어서 설명한다.

- Von Mises 등가 응력을 편차 응력에 대한 함수로 아래와 같이 표현할 수 있다.

$$
\sigma^{VM}=\sqrt{\frac{3}{2}\sum_{i=1}^3\sum_{j=1}^3s_{ij}^2}
$$

- 위 등가 응력을 활용한 Von Mises 항복 조건에 따르면, 소성 변형에 '평균응력'이 기여가 없고
  다만 편차 응력만이 소성변형을 일으키는 것으로 해석할 수 있다.


# 6. 주 응력값으로 표현된 Von Mises 항복 함수

- 주 응력 값으로만 Von Mises 등가 응력을 아래와 같이 표현할 수 있다.

$$
\sigma^{VM}=\sqrt{\frac{1}{2}\bigg((\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2\bigg)}
$$


# 7. 항복면으로 이어지는 기하학

- 항복 조건을 만족하는 응력 상태의 모임이 응력공간에서 '면'을 이룬다.

- 이 장에서는 주공간과 편차응력 공간의 기하학까지만 다룬다. 항복면 내부·표면과
  하중경로에 따른 탄성·소성 판정은 다음의
  [소성 항복]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_12_plastic_yield.md %})에서 다룬다.

## 7.1. 응력 불변량과의 연결

$$
I_1=\operatorname{tr}(\boldsymbol\sigma)=3\sigma_m,
\qquad
J_2=\frac{1}{2}\boldsymbol s:\boldsymbol s
$$

이며 von Mises 등가응력은 $\boxed{\sigma^{VM}=\sqrt{3J_2}}$로 쓸 수 있다.
$I_1$은 평균응력 정보를, $J_2$는 편차응력의 크기를 나타내며 좌표계를 회전해도 변하지
않는다. 주응력 공간에서 von Mises 항복면은
$\sigma_1=\sigma_2=\sigma_3$인 정수압축을 중심축으로 하는 원기둥이다.


# 8. 요약

| 개념 | 의미 |
|---|---|
| 주응력 | 전단응력이 0이 되는 좌표계의 수직응력 값 |
| 주축  | 주응력이 작용하는 방향 |
| Principal Stress Space | $(\sigma_1, \sigma_2, \sigma_3)$ 공간 |
| 평균응력 | $\sigma_m=\frac{1}{3}(\sigma_{11}+\sigma_{22}+\sigma_{33})$ |
| Hydrostatic Stress | 평균응력 성분; 탄성 부피변화와 관련된 $\sigma_m\boldsymbol I$ |
| Deviatoric Stress | 형상 변화 유발; $\boldsymbol s = \boldsymbol{\sigma} - \sigma_m\boldsymbol I$ |
| von Mises 응력 | 편차응력 기반 등가응력; $\sigma^{VM}=\sqrt{\frac{3}{2}\sum_{i=1}^3\sum_{j=1}^3s_{ij}^2}$ |

# 9. 연습 문제

## 문제 1

주응력의 물리적 의미를 간단히 설명하라.

<!--
풀이와 해답:
전단응력이 0이 되는 서로 수직인 면들에서의 수직응력이다.
-->

## 문제 2

응력 텐서의 평균응력 $\sigma_m$을 세 주응력으로 나타내라.

<!--
풀이와 해답:
sigma_m=(sigma_1+sigma_2+sigma_3)/3이다.
-->

## 문제 3

주응력이 $(90,60,30)$ MPa일 때 평균응력과 편차 주응력을 구하라.

<!--
풀이와 해답:
평균응력은 60 MPa이고 편차 주응력은 (30,0,-30) MPa이다.
-->

## 문제 4

정수압 응력을 더해도 von Mises 등가응력이 변하지 않는 이유를 설명하라.

<!--
풀이와 해답:
von Mises 등가응력은 편차응력에만 의존하고 정수압 응력은 편차응력을 바꾸지 않기 때문이다.
-->

## 문제 5

주응력이 $(90,40,-30)\,\mathrm{MPa}$일 때 평균응력, 편차 주응력과 최대
전단응력을 구하라.

<!--
풀이와 해답:
평균응력은 100/3 MPa이다. 편차 주응력은 (170/3, 20/3, -190/3) MPa이고,
최대 전단응력은 [90-(-30)]/2=60 MPa이다.
-->

## 문제 6

평면응력 상태에서 $\sigma_{11}=80\,\mathrm{MPa}$,
$\sigma_{22}=20\,\mathrm{MPa}$이고 나머지 성분이 0일 때 $\sigma_m$과
$s_{33}$을 구하라.

<!--
풀이와 해답:
평균응력은 (80+20+0)/3=100/3 MPa이고, s_33=-100/3 MPa이다.
-->

---

[이전 강의](/assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_09_coordinate_transformation.md) · [강의 목록](/_lectures/5_1_polycrystalline_Plasticity.md) · [다음 강의](/assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_11_Mohr_circle.md)
