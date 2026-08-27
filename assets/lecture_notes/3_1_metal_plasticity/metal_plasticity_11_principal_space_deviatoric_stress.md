---
layout: distill
title: 소성가공
description:
target: 3학년 1학기
permalink:
featured: true
prerequisite: 재료공학개론1, 대학수학, 데이터 재료과학, 수치해석
#toc:
#sidebar: left
#- name: Orientation
#- name: Week1
#- name: Week2
#- name: Week3
#- name: Week4
#- name: Week5
#- name: Week6

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


- [1. 좌표 변환와 주 공간](#1-좌표-변환와-주-공간)
- [2. 주 응력](#2-주-응력)
- [3. 주 응력 값 구하기](#3-주-응력-값-구하기)
- [4. 편차 응력(deviatoric stress)](#4-편차-응력deviatoric-stress)
- [5. Von Mises 등가 응력](#5-von-mises-등가-응력)
- [6. 요약](#6-요약)


# 1. 좌표 변환와 주 공간

- 앞서 좌표 변환 방법에 대해서 배웠다.

- 그 중, 주어진 응력 상태에 대해 특별한 좌표계를 생각해보자. 우선 아래와 같은 임의의 응력상태
 를 나타내는 응력텐서가 있다고 하자. 이 응력 텐서가 표현된 좌표계가 $(\mathbf e_1, \mathbf e_2,\mathbf e_3)$ 축으로 구성되어 있을 때, 아래 구성성분 값을 가진다고 하자.

- 즉,
$$
\mathbf{\sigma}=\sum_i^3\sum_j^3\sigma_{ij}\mathbf{e}_i\otimes\mathbf{e}_j
$$

- 여기에 좌표변환행렬 $\mathbf{R}$ 를 통해 또 다른 좌표축 $(\tilde{\mathbf e}_1, \tilde{\mathbf e}_2,\tilde{\mathbf e}_3)$에 대한 구성성분값을 아래와 같이 구할 수 있다.

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

- 만약 아래와 같이, 전단 성분값이 모두 0이 된다면, 좌표축 $(\tilde{\mathbf e}_1, \tilde{\mathbf e}_2,\tilde{\mathbf e}_3)$로 구성된 공간을 우리는 해당 응력 텐서의 '주 공간'(principal space)이라 부른다

$$
\tilde{\sigma}_{12}=\tilde{\sigma}_{23}=\tilde{\sigma}_{13}=0
$$

- 이런 경우, 좌표축 $(\tilde{\mathbf e}_1, \tilde{\mathbf e}_2,\tilde{\mathbf e}_3)$을
 주축 (principal axis)라고도 부른다.


# 2. 주 응력

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

- 주 응력값은 고유값(eigenvalue)이며 아래를 풀이하여 얻을 수 있다.

$$
\det(\mathbf \sigma - \lambda \mathbf I)=0
$$

- 위에서 $\lambda$는 eigenvalue이며, 위 식의 해가 주 응력값이 된다.

# 4. 편차 응력(deviatoric stress)

- 모든 응력 상태는 편차 응력($\mathbf s$)과, 평균응력($\sigma_m \mathbf I$)으로 구분할 수 있다.

$$
\mathbf \sigma= \sigma_m \mathbf I + \mathbf s
$$

- $\mathbf I$는 랭크2 단위 텐서이며, 아래와 같은 매트릭스 형태로 표현된다.

$$
\mathbf I = \begin{bmatrix}1 &0 &0 \\0 &1 &0 \\0 &0 &1 \\\end{bmatrix}
$$

- 평균 응력값 $\sigma_m$은 아래와 같이 정의된다.

$$
\sigma_m = \frac{1}{3}(\sigma_{11}+\sigma_{22}+\sigma_{33})=\frac{1}{3}tr(\mathbf\sigma)
$$

- 편차 응력은 응력텐서에서 평균 응력을 뺀 나머지다.

$$
\mathbf s = \mathbf \sigma - \sigma_m \mathbf I
$$

# 5. Von Mises 등가 응력

- Von Mises 등가 응력을 편차 응력에 대한 함수로 아래와 같이 표현할 수 있다.


$$
\sigma^{VM}=\sqrt{\frac{3}{2}\sum_i^3\sum_j^3s_{ij}}
$$

- 위 등가 응력을 활용한 Von Mises 항복 조건에 따르면, 소성 변형에 '평균응력'이 기여가 없고
  다만 편차 응력만이 소성변형을 일으키는 것으로 해석할 수 있다.


# 6. 요약

| 개념 | 의미 |
|---|---|
| 주응력 | 전단응력이 0이 되는 좌표계의 수직응력 값 |
| 주축  | 주응력이 작용하는 방향 |
| Principal Stress Space | $(\sigma_1, \sigma_2, \sigma_3)$ 공간 |
| 평균응력 | $\sigma_m=\frac{1}{3}(\sigma_{11}+\sigma_{22}+\sigma_{33})$ |
| Hydrostatic Stress | 부피 변화 유발; $\sigma_m\mathbf I$ |
| Deviatoric Stress | 형상 변화 유발; $\mathbf s = \mathbf{\sigma} - \sigma_m\mathbf I$ |
| von Mises 응력 | 편차응력 기반 등가응력; $\sigma^{VM}=\sqrt{\frac{3}{2}\sum_i^3\sum_j^3s_{ij}}$ |
