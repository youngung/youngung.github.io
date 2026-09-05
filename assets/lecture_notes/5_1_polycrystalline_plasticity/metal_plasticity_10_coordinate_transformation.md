---
layout: distill
title: 좌표변환
description: 벡터와 텐서 성분의 좌표변환
target: 학부 고학년
permalink:
featured: true
prerequisite: 벡터와 행렬, 응력 텐서
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

- [1. 좌표 변환](#1-좌표-변환)
- [2. n차 랭크 텐서의 좌표변환](#2-n차-랭크-텐서의-좌표변환)


# 1. 좌표 변환

- 한벡터 $\boldsymbol v$는 다음과 같이 주어진 좌표계의 세축 ($\boldsymbol e_1,\boldsymbol e_2, \boldsymbol e_3$)를 활용해 표현할 수 있다.

$$
\boldsymbol v = v_1 \boldsymbol e_1 + v_2 \boldsymbol e_2 +v_3 \boldsymbol e_3 =\sum_{i=1}^3 v_i\boldsymbol e_i
$$

-  위 동일한 벡터를 또 다른 좌표계의 세축 ($\tilde{\boldsymbol e}_1,\tilde{\boldsymbol e}_2, \tilde{\boldsymbol e}_3$)을 활용해 위와 같이 표현하자면 아래와 같다.

$$
\boldsymbol v = \tilde{v}_1 \tilde{\boldsymbol e}_1 + \tilde{v}_2 \tilde{\boldsymbol e}_2 +\tilde{v}_3 \tilde{\boldsymbol e}_3 =\sum_{i=1}^3 \tilde{v}_i\tilde{\boldsymbol e}_i
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
=\sum_{j=1}^3 v_j\boldsymbol{e}_j \cdot\tilde{\boldsymbol e}_{1}

=\tilde{\boldsymbol e}_{1} \cdot \sum_{j=1}^3 v_j\boldsymbol{e}_j
$$

- 모든 basis vector 경우로 정리하면

$$
\tilde{v}_i=
\tilde{\boldsymbol e}_{i} \cdot \sum_{j=1}^3 v_j\boldsymbol{e}_j\ \ \ \text{ with } i=1,2,3
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
\tilde{v}_i = \sum_{j=1}^3 R_{ij} v_j, \text{ with } i=1,2,3
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
\tilde{v}_{i} = \sum_{j=1}^3 R_{ij} v_{j}, \text{ with } i=1,2,3
$$

- 2차 랭크 텐서 $\boldsymbol \sigma$의 좌표 변환은 아래와 같다.

$$
\tilde{\sigma}_{ij} = \sum_{k=1}^3\sum_{l=1}^3 R_{ik} R_{jl} \sigma_{kl}, \text{ with } i=1,2,3\ \ \ j=1,2,3
$$

- 4차 랭크 텐서 $\boldsymbol E$의 좌표 변환은 아래와 같다.

$$
\tilde{E}_{ijkl} = \sum_{m=1}^3 \sum_{n=1}^3 \sum_{o=1}^3 \sum_{p=1}^3 R_{im}R_{jn}R_{ko}R_{lp}E_{mnop}, \text{ with } i=1,2,3\ \ \ j=1,2,3\ \ \ k=1,2,3 \ \ \ \ l=1,2,3
$$

# 3. 연습 문제

## 문제 1

직교 좌표변환 행렬 $\boldsymbol R$이 만족하는 역행렬 관계를 쓰시오.

<!--
풀이와 해답:
R의 역행렬은 전치행렬과 같으므로 R^{-1}=R^T이다.
-->

## 문제 2

벡터의 좌표성분은 좌표계를 회전하면 변할 수 있다. 벡터 자체도 변하는지 설명하라.

<!--
풀이와 해답:
좌표성분은 변하지만 벡터가 나타내는 물리량 자체는 변하지 않는다.
-->

## 문제 3

2차 텐서 $\boldsymbol A$의 변환된 성분을 $\boldsymbol R$로 나타내라.

<!--
풀이와 해답:
강의에서 정의한 좌표변환 관례에 따라 A'=R A R^T로 나타낸다.
-->
