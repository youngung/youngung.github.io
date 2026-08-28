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

- [1. 좌표 변환](#1-좌표-변환)
- [2. n차 랭크 텐서의 좌표변환](#2-n차-랭크-텐서의-좌표변환)


# 1. 좌표 변환

- 한벡터 $\boldsymbol v$는 다음과 같이 주어진 좌표계의 세축 ($\boldsymbol e_1,\boldsymbol e_2, \boldsymbol e_3$)를 활용해 표현할 수 있다.

$$
\boldsymbol v = v_1 \boldsymbol e_1 + v_2 \boldsymbol e_2 +v_3 \boldsymbol e_3 =\sum_i^3 v_i\boldsymbol e_i
$$

-  위 동일한 벡터를 또 다른 좌표계의 세축 ($\tilde{\boldsymbol e}_1,\tilde{\boldsymbol e}_2, \tilde{\boldsymbol e}_3$)을 활용해 위와 같이 표현하자면 아래와 같다.

$$
\boldsymbol v = \tilde{v}_1 \tilde{\boldsymbol e}_1 + \tilde{v}_2 \tilde{\boldsymbol e}_2 +\tilde{v}_3 \tilde{\boldsymbol e}_3 =\sum_i^3 \tilde{v}_i\tilde{\boldsymbol e}_i
$$

- 위를 우리는 좌표계 불변성(coordinate invariance)이라 하자.

- 벡터는 대상이되는 물리량의 '방향성'을 포함하므로, 그 방향성이 선택된 좌표에 따라 달라져서는 안된다.
  따라서 서로 다른 좌표계를 활용하여도 두 표현은 동일해야 한다.

$$
\boldsymbol v = v_1 \boldsymbol e_1 + v_2 \boldsymbol e_2 +v_3 \boldsymbol e_3
= \tilde{v}_1 \tilde{\boldsymbol e}_1 + \tilde{v}_2 \tilde{\boldsymbol e}_2 +\tilde{v}_3 \tilde{\boldsymbol e}_3
$$

- 더 이어지는 논의를 위해서 아래 관계를 염두에 두자.

$$v_1=\boldsymbol v \cdot \boldsymbol{e}_1$$

즉,

$$v_i=\boldsymbol v \cdot \boldsymbol{e}_i\ \ \text{    for any } i$$

마찬가지로

$$\tilde{v}_i=\boldsymbol v \cdot \tilde{\boldsymbol e}_i\ \ \text{    for any } i$$

- 위 관계를 앞선 좌표계 불변성에 대입하면

$$
\boldsymbol v=
(\boldsymbol {v} \cdot \boldsymbol{e}_1 ) \boldsymbol{e}_1+
(\boldsymbol {v} \cdot \boldsymbol{e}_2 ) \boldsymbol{e}_2+
(\boldsymbol {v} \cdot \boldsymbol{e}_3 ) \boldsymbol{e}_3
\ \ \ \text{ Eq. 1}
$$

$$
\boldsymbol v=
(\boldsymbol {v} \cdot \tilde{\boldsymbol{e}}_1 ) \tilde{\boldsymbol{e}}_1+
(\boldsymbol {v} \cdot \tilde{\boldsymbol{e}}_2 ) \tilde{\boldsymbol{e}}_2+
(\boldsymbol {v} \cdot \tilde{\boldsymbol{e}}_3 ) \tilde{\boldsymbol{e}}_3
\ \ \ \text{ Eq. 2}
$$

- Eq. 1의 양변에 한 basis vector $\tilde{\boldsymbol{e}}_1$을 내적하면

$$
\boldsymbol v \cdot \tilde{\boldsymbol e}_1=
(\boldsymbol {v} \cdot \boldsymbol{e}_1 )\boldsymbol{e}_1 \cdot \tilde{\boldsymbol e}_1+
(\boldsymbol {v} \cdot \boldsymbol{e}_2 )\boldsymbol{e}_2 \cdot \tilde{\boldsymbol e}_1+
(\boldsymbol {v} \cdot \boldsymbol{e}_3 )\boldsymbol{e}_3 \cdot \tilde{\boldsymbol e}_1
$$

- 정리하면 아래와 같다.

$$
\tilde{v}_1=
v_1 \boldsymbol{e}_1 \cdot \tilde{\boldsymbol e}_1+
v_2 \boldsymbol{e}_2 \cdot \tilde{\boldsymbol e}_1+
v_3 \boldsymbol{e}_3 \cdot \tilde{\boldsymbol e}_1
=\sum_j^3 v_j\boldsymbol{e}_j \cdot\tilde{\boldsymbol e}_{1}

=\tilde{\boldsymbol e}_{1} \cdot \sum_j^3 v_j\boldsymbol{e}_j
$$

- 모든 basis vector 경우로 정리하면

$$
\tilde{v}_i=
\tilde{\boldsymbol e}_{i} \cdot \sum_j^3 v_j\boldsymbol{e}_j\ \ \ \text{ with } i=1,2,3
$$

- 위를 더욱 간결하게 표현하기 위해, 다음과 같은 매트릭스 $\boldsymbol R$을 도입하고, 이를
아래와 같이 정의하자.

$$
R_{ij}=\tilde{\boldsymbol e}_i \cdot \boldsymbol e_j \text{  with  } i=1,2,3,\ \ \ j=1,2,3
$$

- 위 매트릭스는 ($\boldsymbol e_1,\boldsymbol e_2,\boldsymbol e_3$)로 이루어진 좌표계로부터
  ($\tilde{\boldsymbol e}_1,\tilde{\boldsymbol e}_2,\tilde{\boldsymbol e}_3$) 좌표계로
  변환하는 좌표변환 매트릭스(coordinate transformation matrix)라 한다.

- 이를 활용하면 $\tilde{v}_i$ 와  $v_j$와의 관계를 아래와 같이 더욱 매끄럽게 표현할 수 있다.

$$
\tilde{v}_i = \sum_j^3 R_{ij} v_j, \text{ with } i=1,2,3
$$

- 좌표 변환 매트릭스는 다음과 같은 성질을 가진다.

$$
\boldsymbol{R}^{-1}=\boldsymbol{R}^T
$$

# 2. n차 랭크 텐서의 좌표변환

- 좌표 변환을 더욱 일반화시켜 적용해보자. 마찬가지로
  ($\boldsymbol e_1,\boldsymbol e_2,\boldsymbol e_3$)로 이루어진 좌표계로부터
  ($\tilde{\boldsymbol e}_1,\tilde{\boldsymbol e}_2,\tilde{\boldsymbol e}_3$)
  좌표계로 변환하는 좌표변환 매트릭스(coordinate transformation matrix)를
  아래와 같이 정의하자.

$$
R_{ij}=\tilde{\boldsymbol e}_i \cdot \boldsymbol e_j
$$

- 0차 랭크 텐서는 스칼라를 의미한다. 스칼라 물리량은 따로 좌표 변환이 적용되지 않는다.

- 1차 랭크 텐서는 벡터를 의미한다.

$$
\tilde{v}_{i} = \sum_j^3 R_{ij} v_{j}, \text{ with } i=1,2,3
$$

- 2차 랭크 텐서 $\boldsymbol \sigma$의 좌표 변환은 아래와 같다.

$$
\tilde{\sigma}_{ij} = \sum_k^3\sum_l^3 R_{ik} R_{jl} \sigma_{kl}, \text{ with } i=1,2,3\ \ \ j=1,2,3
$$

- 4차 랭크 텐서 $\boldsymbol E$의 좌표 변환은 아래와 같다.

$$
\tilde{E}_{ijkl} = \sum_m^3 \sum_n^3 \sum_o^3 \sum_p^3 R_{im}R_{jn}R_{ko}R_{lp}E_{mnop}, \text{ with } i=1,2,3\ \ \ j=1,2,3\ \ \ k=1,2,3 \ \ \ \ l=1,2,3
$$
