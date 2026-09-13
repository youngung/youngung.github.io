---
layout: distill
title: 변위와 미소변형률 연습문제
description: 변위장과 미소변형률의 복습 문제
target: 학부 고학년
permalink:
featured: true
prerequisite: 변위와 미소변형률
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

<span id="14-연습-문제"></span>

# 1. 연습 문제

## 문제 1

모든 점이 같은 크기와 방향으로 이동하는 병진운동에서 미소변형률이 0인 이유를 설명하시오.

<!--
풀이와 해답:
점 사이의 상대적인 거리와 각도가 변하지 않고 변위의 공간 미분도 0이기 때문이다.
-->

## 문제 2

1차원 막대의 변위가 $u(X)=0.01X$일 때 미소변형률을 구하시오.

<!--
풀이와 해답:
epsilon=du/dX=0.01이다.
-->

## 문제 3

좌표와 변위를 mm 단위로 측정한다. 변위가 $u(X)=(0.002\,\mathrm{mm}^{-1})X^2$일 때
$X=10\,\mathrm{mm}$에서의 미소변형률을 구하시오.

<!--
풀이와 해답:
epsilon=du/dX=0.004X이므로 X=10에서 0.04이다.
-->

## 문제 4

강체회전이 물체의 변형률을 만들지 않는 이유를 한 문장으로 설명하시오.

<!--
풀이와 해답:
강체회전은 물체 내부의 길이와 각도를 바꾸지 않기 때문이다.
-->

## 문제 5

한 점의 변형 전 위치가 $\boldsymbol X=(1,2,3)^T$ mm이고 변형 후 위치가
$\boldsymbol x=(2,4,3)^T$ mm이다. 변위벡터를 구하시오.

<!--
풀이와 해답:
u=x-X=(2-1,4-2,3-3)^T=(1,2,0)^T mm이다.
-->

## 문제 6

초기 위치가 $X^a=0$ mm, $X^b=100$ mm인 두 점의 변위가 각각
$u^a=2$ mm, $u^b=3$ mm이다. 두 점 사이의 공칭변형률을 구하시오.

<!--
풀이와 해답:
두 점의 상대변위는 3-2=1 mm이고 초기 거리는 100 mm이다.
따라서 변형률은 1/100=0.01이다. 두 점에 공통인 2 mm 병진성분은 변형률에 기여하지 않는다.
-->

## 문제 7

1차원 변위장이 $u(X)=5$ mm로 위치와 관계없이 일정하다. 미소변형률을 구하고 이 운동을
설명하시오.

<!--
풀이와 해답:
du/dX=0이므로 변형률은 0이다. 모든 점이 같은 양만큼 이동하는 강체 병진이다.
-->

## 문제 8

좌표와 변위를 mm 단위로 측정한다. 1차원 변위장이 $u(X)=(0.001\,\mathrm{mm}^{-1})X^2$일 때
미소변형률 분포를 구하고 $X=10\,\mathrm{mm}$에서의 값을 계산하시오.

<!--
풀이와 해답:
epsilon=du/dX=0.002X이다. X=10에서는 epsilon=0.02이다.
위치에 따라 변형률이 달라지는 비균일 변형이다.
-->

## 문제 9

다음 2차원 변위장에서 변위구배와 미소변형률 텐서를 구하시오.

$$
u_1=0.02X_1,
\qquad
u_2=-0.01X_2
$$

<!--
풀이와 해답:
변위구배는 [[0.02,0],[0,-0.01]]이다. 이미 대칭이므로 변형률 텐서도
[[0.02,0],[0,-0.01]]이다. 1방향은 인장되고 2방향은 압축된다.
-->

## 문제 10

다음 단순전단 변위장에서 $\varepsilon_{12}$와 공학전단변형률 $\gamma_{12}$를
구하시오.

$$
u_1=0.04X_2,
\qquad
u_2=0
$$

<!--
풀이와 해답:
partial u1/partial X2=0.04이고 partial u2/partial X1=0이다.
따라서 epsilon_12=(0.04+0)/2=0.02이고 gamma_12=2epsilon_12=0.04이다.
-->

## 문제 11

다음 미소 강체회전 변위장의 변형률 텐서가 0임을 보이시오. 여기서 $\theta$는 작은
회전각이다.

$$
u_1=-\theta X_2,
\qquad
u_2=\theta X_1
$$

<!--
풀이와 해답:
변위구배는 [[0,-theta],[theta,0]]으로 반대칭이다.
대칭부분 (grad u + grad u^T)/2는 영행렬이므로 변형률 텐서는 0이다.
반대칭부분에는 강체회전만 남는다.
-->

## 문제 12

다음 변위장에서 미소변형률 텐서와 미소회전 텐서를 구하시오.

$$
u_1=0.01X_1-0.02X_2+1,
\qquad
u_2=0.02X_1+0.03X_2-2
$$

<!--
풀이와 해답:
변위구배는 [[0.01,-0.02],[0.02,0.03]]이다.
대칭부분인 변형률은 [[0.01,0],[0,0.03]]이고,
반대칭부분인 회전은 [[0,-0.02],[0.02,0]]이다.
상수 1과 -2는 병진이므로 두 텐서에 영향을 주지 않는다.
-->

## 문제 13

3차원 변위장이 다음과 같을 때 체적변형률의 미소변형 근사
$\varepsilon_v=\operatorname{tr}(\boldsymbol\varepsilon)$를 구하시오.

$$
u_1=0.01X_1,
\qquad
u_2=0.02X_2,
\qquad
u_3=-0.005X_3
$$

<!--
풀이와 해답:
수직변형률은 각각 0.01, 0.02, -0.005이다.
따라서 체적변형률은 trace(epsilon)=0.01+0.02-0.005=0.025이다.
-->

## 문제 14

다음 변위장이 미소 비압축성 조건을 만족하도록 상수 $a$를 구하시오.

$$
u_1=0.02X_1,
\qquad
u_2=-0.01X_2,
\qquad
u_3=aX_3
$$

<!--
풀이와 해답:
미소 비압축성 조건은 trace(epsilon)=0이다.
0.02-0.01+a=0이므로 a=-0.01이다.
-->

## 문제 15

좌표와 변위를 mm 단위로 측정한다. 다음 비균일 변위장에서 미소변형률 성분을 구하고
$(X_1,X_2)=(2,1)\,\mathrm{mm}$에서 평가하시오.

$$
u_1=\left(0.005\,\mathrm{mm}^{-1}\right)X_1X_2,
\qquad
u_2=0.01X_2
$$

<!--
풀이와 해답:
epsilon_11=partial u1/partial X1=(0.005 mm^{-1})X2,
epsilon_22=partial u2/partial X2=0.01,
epsilon_12=(partial u1/partial X2+partial u2/partial X1)/2=(0.0025 mm^{-1})X1이다.
(X1,X2)=(2,1) mm에서는 epsilon_11=0.005, epsilon_22=0.01,
epsilon_12=0.005이다.
-->

## 문제 16

변위장에 임의의 상수 병진벡터 $\boldsymbol c$를 더해
$\boldsymbol u^{new}(\boldsymbol X)=\boldsymbol u(\boldsymbol X)+\boldsymbol c$로 만들었다.
변형률 텐서가 바뀌는지 설명하시오.

<!--
풀이와 해답:
상수벡터 c의 공간미분은 0이므로 변위구배와 변형률 텐서는 바뀌지 않는다.
변형률은 절대변위가 아니라 위치에 따른 상대변위 변화로 결정된다.
-->
