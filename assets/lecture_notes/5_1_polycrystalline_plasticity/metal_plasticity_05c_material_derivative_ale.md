---
layout: distill
title: 물질미분과 ALE 기술법
description: 물질점을 따라 관찰하는 변화율과 계산 격자의 운동
target: 학부 고학년
permalink:
featured: true
prerequisite: 유한변형의 운동학
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

**Contents**

* TOC
{:toc}

관련 자료는 다음 순서로 읽을 수 있다.

- [변위와 미소변형률]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05_displacement_strain.md %})
- [변위와 미소변형률 연습문제]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05d_displacement_strain_exercises.md %})
- [유한변형의 운동학]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %})
- [물질미분과 ALE 기술법]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05c_material_derivative_ale.md %})

<span id="부록-a-물질미분-material-derivative"></span>

# 1. 물질미분 (material derivative)

<span id="a1-물질점을-따라-관찰하는-변화율"></span>

## 1.1. 물질점을 따라 관찰하는 변화율

**물질미분은 움직이는 물질점이 경험하는 물리량의 변화율**이다.
온도장 $T(\boldsymbol x,t)$에서 고정된 위치의 온도 변화율은
$\left.\partial T/\partial t\right\vert_{\boldsymbol x}$이다. 그러나 물질점은 이동하므로,
다른 온도의 위치로 이동하며 경험하는 변화도 포함해야 한다.

물질점의 운동을 $\boldsymbol x=\boldsymbol\Phi(\boldsymbol X,t)$로 나타내면,
같은 물질점이 경험하는 온도는

$$
T_L(\boldsymbol X,t)=T_E(\boldsymbol\Phi(\boldsymbol X,t),t)
$$

이다.

앞으로 공간좌표 $\boldsymbol x$로 표현한 Eulerian 온도 $T_E(\boldsymbol x,t)$를 단순히 $T$라 쓰겠다.

물질미분 연산자를 $D/Dt$로 표기하겠다.

물질점의 이름표 $\boldsymbol X$를 고정하고 연쇄법칙(chain rule)을 적용하면

$$
\begin{aligned}
\frac{DT}{Dt}
&=\left.\frac{\partial T_L}{\partial t}\right|_{\boldsymbol X}\\
&=\left.\frac{\partial T}{\partial t}\right|_{\boldsymbol x}
+\frac{\partial T}{\partial x_i}
\left.\frac{dx_i}{dt}\right|_{\boldsymbol X}\\
&=\left.\frac{\partial T}{\partial t}\right|_{\boldsymbol x}
+v_i\frac{\partial T}{\partial x_i}.
\end{aligned}
$$

$\left.\partial T_L/\partial t\right\vert_{\boldsymbol X}$는 물질점의 이름표
$\boldsymbol X$를 고정하고 같은 물질점을 따라 관찰하는 시간변화율을 의미한다. 이를 **Lagrangian 기술법에서의 시간 미분**이라고 부르기도 한다.
그런데, 이를 공간에 고정된 관찰점에서의 시간 변화율로 바꾸면, 이송항을 더해야 한다. 즉, 공간에
고정된 위치에서의 시간에 대한 변화율($\left.\frac{\partial T}{\partial t}\right\vert_{\boldsymbol x}$) 더하기, 이송항($\boldsymbol v\cdot\nabla_xT=\sum_i v_i \frac{\partial T}{\partial x_i}$)으로 표현할 수 있다.

여기서 $\left.d\boldsymbol x/dt\right\vert_{\boldsymbol X}$는 **같은 물질점
$\boldsymbol X$를 따라가며 현재 위치를 시간미분한 값**, 즉 물질점의 속도다.
$\boldsymbol x=\boldsymbol\Phi(\boldsymbol X,t)$이므로 두 표기는 다음과 같이 연결된다.

$$
\boldsymbol v
=\left.\frac{d\boldsymbol x}{dt}\right|_{\boldsymbol X}
=\left.\frac{\partial\boldsymbol\Phi}{\partial t}\right|_{\boldsymbol X}.
$$

반복 첨자 $i$는 공간 방향에 대한 합을 뜻한다(3차원에서는 $i=1,2,3$).
우변은 해당 물질점의 현재 위치에서 평가한다. 벡터 표기로 쓰면

$$
\boxed{\frac{DT}{Dt}
=\left.\frac{\partial T}{\partial t}\right|_{\boldsymbol x}
+\boldsymbol v\cdot\nabla_xT}.
$$

첫 항($\left.\frac{\partial T}{\partial t}\right\vert_{\boldsymbol x}$)은 고정된 위치에서의 시간 변화이고, 둘째 항은 물질점의 이동에 의한 변화인
**이송항 (convective term)**이다. 따라서 Lagrangian 기술법에서는 같은 물질점의
시간 미분이 곧 물질미분이며, Eulerian 기술법에서는 고정 위치의 시간 미분($\left.\frac{\partial T}{\partial t}\right\vert_{\boldsymbol x}$)에 이송항($\boldsymbol v\cdot\nabla_xT$)을 더한다.

<span id="a2-시간에-따라-변하지-않는-온도장에서의-물질미분"></span>

## 1.2. 시간에 따라 변하지 않는 온도장에서의 물질미분

$x$를 m 단위로 측정할 때, 시간에 따라 **변하지 않는** 1차원 온도장을

$$
T(x)=20\,{}^\circ\mathrm C
+\left(10\,{}^\circ\mathrm C/\mathrm m\right)x
$$

라고 하자. 한 물질점이 $v=2\,\mathrm{m/s}$로 이동하면

$$
\left.\frac{\partial T}{\partial t}\right|_x=0,
\qquad
\frac{DT}{Dt}=v\frac{dT}{dx}
=2\,\mathrm{m/s}\times 10\,{}^\circ\mathrm C/\mathrm m=20\,{}^\circ\mathrm C/\mathrm s.
$$

고정된 위치에 붙어있는 온도계의 값은 변하지 않지만, 공간에서 2 $\mathrm{m/s}$의 속도로
이동하는 물질점은 더 따뜻한 곳으로 가므로, 초당 $20\,{}^\circ\mathrm C$의 온도 증가를 경험한다.

![정상 온도장에서 고정 관찰점과 이동하는 물질점이 기록하는 온도의 비교](/assets/img/lecture_notes/displacement/material_derivative_temperature.png)

위 그림의 (a)에서 파란 선은 각 고정 위치에서 시간에 따라 변하지 않는 온도장
$T(x)$를 나타낸다. 온도는 위치 $x$에 따라 달라진다. 그에 비해 빨간 점들은 $x(0)=0$에서 출발한
**같은 물질점**의 $t=0,1,2\,\mathrm s$ 위치와 온도를 나타낸다.
초록색 원은 공간에 고정된 관찰점($x=1\,\mathrm m$)이다. (b)는 (a)의 녹색점에 고정된 관찰자
그리고 물질과 함께 이동하는 관찰자(빨간 점)가 기록하는 온도를 시간에 대해 그린 것으로,
녹색 고정점에서는 $30\,{}^\circ\mathrm C$로 시간에 따라 달라지지 않는 온도를 관찰하지만
빨간색 이동점에서는 시간이 0, 1, 2초로 흐름에 따라 온도가 $20,40,60\,{}^\circ\mathrm C$로 상승한다.

<span id="a3-공간과-시간에-모두-의존하는-온도장"></span>

## 1.3. 공간과 시간에 모두 의존하는 온도장

이번에는 앞의 1.2절에서 사용한 온도장에 시간에 따른 온도 상승을 추가하자.
공간에 따른 온도 기울기는 그대로 두고, 모든 고정 위치에서 온도가 초당
$3\,{}^\circ\mathrm C$씩 상승한다고 가정한다. $x$는 m, $t$는 s 단위로 측정하며,

$$
T(x,t)=20\,{}^\circ\mathrm C
+\left(10\,{}^\circ\mathrm C/\mathrm m\right)x
+\left(3\,{}^\circ\mathrm C/\mathrm s\right)t
$$

라고 하자. 공간 $\boldsymbol x$에 고정된 한 위치에서의 온도 상승률과 공간에 대한
온도 변화에 대한 기울기는 각각

$$
\left.\frac{\partial T}{\partial t}\right|_x
=3\,{}^\circ\mathrm C/\mathrm s,
\qquad
\frac{\partial T}{\partial x}=10\,{}^\circ\mathrm C/\mathrm m
$$

이다. 물질점이 $v=2\,\mathrm{m/s}$로 이동하면

$$
\begin{aligned}
\frac{DT}{Dt}
&=\left.\frac{\partial T}{\partial t}\right|_x
+v\frac{\partial T}{\partial x}\\
&=3\,{}^\circ\mathrm C/\mathrm s
+\left(2\,\mathrm{m/s}\right)\left(10\,{}^\circ\mathrm C/\mathrm m\right)\\
&=\boxed{23\,{}^\circ\mathrm C/\mathrm s}.
\end{aligned}
$$

공간 $\boldsymbol x$에 고정된 온도계는 $3\,{}^\circ\mathrm C/\mathrm s$의 온도 상승률을 측정한다.
이동하는 물질점은 이 시간 변화에 더해 더 따뜻한 위치로 이동하는 효과도 경험하므로,
$23\,{}^\circ\mathrm C/\mathrm s$의 온도 상승률을 경험한다.

물질점의 경로에 온도장을 직접 대입해도 같은 결과를 확인할 수 있다.
$t=0$에서 $x=X$인 물질점의 운동은 $x(X,t)=X+vt$이므로,

$$
\begin{aligned}
T_L(X,t)&=T(X+vt,t)\\
&=20\,{}^\circ\mathrm C
+\left(10\,{}^\circ\mathrm C/\mathrm m\right)X
+\left(23\,{}^\circ\mathrm C/\mathrm s\right)t,\\
\left.\frac{\partial T_L}{\partial t}\right|_X
&=23\,{}^\circ\mathrm C/\mathrm s.
\end{aligned}
$$

두 효과가 항상 같은 부호인 것은 아니다. 같은 온도장에서 물질점이 반대 방향으로
$v=-2\,\mathrm{m/s}$로 이동하면 물질미분은
$DT/Dt=3\,{}^\circ\mathrm C/\mathrm s-20\,{}^\circ\mathrm C/\mathrm s=-17\,{}^\circ\mathrm C/\mathrm s$다.
각 위치의 온도는 상승하고 있어도, 물질점은 더 차가운 위치로 빠르게 이동하므로
자신이 경험하는 온도는 감소한다.

## 1.4. 2차원 온도장에서의 물질미분

이번에는 온도가 두 공간 좌표 $x_1$, $x_2$에 따라 달라지는 경우를 생각하자.
고정된 직교좌표계에서 $x_1$, $x_2$는 m, $t$는 s 단위로 측정하며, 온도장을

$$
T(x_1,x_2,t)=20\,{}^\circ\mathrm C
+\left(10\,{}^\circ\mathrm C/\mathrm m\right)x_1
-\left(5\,{}^\circ\mathrm C/\mathrm m\right)x_2
+\left(3\,{}^\circ\mathrm C/\mathrm s\right)t
$$

로 둔다. 즉, $x_1$이 증가하는 방향으로는 따뜻해지고, $x_2$가 증가하는 방향으로는
차가워진다. 고정된 위치에서는 온도가 초당 $3\,{}^\circ\mathrm C$씩 상승한다.
물질점의 속도는 일정한 벡터

$$
\boldsymbol v=(v_1,v_2)=(2,1)\,\mathrm{m/s}
$$

라고 하자. 2차원에서는 이송항에 두 방향의 기여가 모두 들어가므로

$$
\begin{aligned}
\frac{DT}{Dt}
&=\left.\frac{\partial T}{\partial t}\right|_{x_1,x_2}
+v_1\frac{\partial T}{\partial x_1}
+v_2\frac{\partial T}{\partial x_2}\\
&=3\,{}^\circ\mathrm C/\mathrm s
+\left(2\,\mathrm{m/s}\right)\left(10\,{}^\circ\mathrm C/\mathrm m\right)
+\left(1\,\mathrm{m/s}\right)\left(-5\,{}^\circ\mathrm C/\mathrm m\right)\\
&=\boxed{18\,{}^\circ\mathrm C/\mathrm s}.
\end{aligned}
$$

$x_1$ 방향의 이동은 $20\,{}^\circ\mathrm C/\mathrm s$의 온도 상승률에,
$x_2$ 방향의 이동은 $5\,{}^\circ\mathrm C/\mathrm s$의 온도 감소율에 기여한다.
따라서 이송항은 $15\,{}^\circ\mathrm C/\mathrm s$이고, 고정 위치의 시간 변화율
$3\,{}^\circ\mathrm C/\mathrm s$를 더하면 물질점이 경험하는 변화율은
$18\,{}^\circ\mathrm C/\mathrm s$이다.

물질점의 이름표를 $\boldsymbol X=(X_1,X_2)$, 즉 $t=0$에서의 위치로 두면,
그 물질점의 경로는

$$
x_1(\boldsymbol X,t)=X_1+\left(2\,\mathrm{m/s}\right)t,
\qquad
x_2(\boldsymbol X,t)=X_2+\left(1\,\mathrm{m/s}\right)t
$$

이다. 이 경로를 온도장에 직접 대입하면

$$
\begin{aligned}
T_L(\boldsymbol X,t)
&=T\bigl(x_1(\boldsymbol X,t),x_2(\boldsymbol X,t),t\bigr)\\
&=20\,{}^\circ\mathrm C
+\left(10\,{}^\circ\mathrm C/\mathrm m\right)X_1
-\left(5\,{}^\circ\mathrm C/\mathrm m\right)X_2
+\left(18\,{}^\circ\mathrm C/\mathrm s\right)t,\\
\left.\frac{\partial T_L}{\partial t}\right|_{\boldsymbol X}
&=18\,{}^\circ\mathrm C/\mathrm s
=\frac{DT}{Dt}.
\end{aligned}
$$

여기서 $\boldsymbol X$를 고정한다는 것은 $X_1$, $X_2$를 모두 고정하여 같은 물질점을
따라간다는 뜻이다. 반면 $x_1$, $x_2$를 고정하면 공간의 같은 위치를 관찰하므로
온도 변화율은 $3\,{}^\circ\mathrm C/\mathrm s$이다.

<span id="a4-속도의-물질미분과-가속도"></span>

## 1.5. 속도의 물질미분과 가속도

물질미분은 벡터장의 각 성분에도 적용할 수 있다.
고정된 Cartesian(직교) 좌표계에서 속도의 물질미분은 물질점의 가속도다.

$$
\boxed{\boldsymbol a=\frac{D\boldsymbol v}{Dt}
=\left.\frac{\partial\boldsymbol v}{\partial t}\right|_{\boldsymbol x}
+(\boldsymbol v\cdot\nabla_x)\boldsymbol v},
\qquad
 a_i=\frac{\partial v_i}{\partial t}+v_j\frac{\partial v_i}{\partial x_j}.
$$

속도장이 시간에 따라 일정해도, 물질점이 공간적으로 속도 크기나 방향이 다른 곳으로
이동하면 가속도가 생길 수 있다. 예를 들어 정상 유동이 좁아지는 통로를 지나며
빨라지는 경우에는 시간에 대한 편미분이 0이어도 이송항에 의한 가속도가 존재한다.

<span id="부록-b-ale-기술법"></span>

# 2. ALE 기술법

[Lagrangian과 Eulerian 기술법]({% link assets/lecture_notes/5_1_polycrystalline_plasticity/metal_plasticity_05b_descriptions_finite_strain.md %})과 1절의 물질미분을 바탕으로, 계산 격자의 운동을 별도로 다루는
방법을 살펴보자.

**ALE (Arbitrary Lagrangian–Eulerian, 임의 Lagrangian–Eulerian) 기술법**에서는
계산 격자(computational mesh)의 운동을 물질의 운동과 별도로 정한다.
격자좌표 $\boldsymbol\xi$를 사용하여

$$
\boldsymbol x=\boldsymbol\psi(\boldsymbol\xi,t),
\qquad
\boldsymbol w=\left.\frac{\partial\boldsymbol\psi}{\partial t}\right|_{\boldsymbol\xi}
$$

라고 쓰면, $\boldsymbol w$는 격자 속도이고 $\boldsymbol v$는 물질 속도다.

| 기술법 | 격자의 운동 | 물질의 격자에 대한 상대속도 |
| ------ | ----------- | -------------------------- |
| Lagrangian | 물질과 함께 이동: $\boldsymbol w=\boldsymbol v$ | $\boldsymbol 0$ |
| Eulerian | 공간에 고정: $\boldsymbol w=\boldsymbol 0$ | $\boldsymbol v$ |
| ALE | 격자 품질과 경계조건에 맞게 격자 속도 $\boldsymbol w$를 정한다. | $\boldsymbol v-\boldsymbol w$ |

![Eulerian, Lagrangian, ALE 기술법에서 같은 물질점과 격자점의 이동 비교](/assets/img/lecture_notes/displacement/ale_mesh_comparison.png)

위 그림은 같은 물질점이 $\boldsymbol v=(2,1)\,\mathrm{m/s}$로 이동할 때,
격자 속도를 다르게 선택한 세 결과(Eulerian, Lagrangian, ALE)를 비교하여 보여준다.
빨간 점은 같은 물질점, 파란 원은 처음에 그 물질점과 겹쳐 있던 같은 격자점이다.
각 패널의 위와 아래는 각각 $t=0$과 $t=1\,\mathrm s$이며, 아래의 옅은 점선은 초기
격자와 물질점 위치를 나타낸다.

Eulerian에서는 격자가 고정되어 물질점만 이동한다. Lagrangian에서는 물질점과
격자점이 함께 이동하므로 두 표시가 계속 겹친다. ALE에서는 격자가
$\boldsymbol w=(1,0)\,\mathrm{m/s}$로 이동하므로 물질점은 격자에 대해
$\boldsymbol v-\boldsymbol w=(1,1)\,\mathrm{m/s}$로 이동한다.
오른쪽 아래의 속도 삼각형은
$\boldsymbol v=\boldsymbol w+(\boldsymbol v-\boldsymbol w)$를 보여준다.
이 그림은 격자와 물질의 상대운동을 설명하기 위한 균일 병진운동의 예이다.

물리량 $q$를 격자좌표로 표현하여
$q_{ALE}(\boldsymbol\xi,t)=q(\boldsymbol\psi(\boldsymbol\xi,t),t)$로 정의하자.
이때 $\boldsymbol\xi$를 고정한 시간미분
$\left.\partial q_{ALE}/\partial t\right\vert_{\boldsymbol\xi}$는
같은 격자점을 따라 관찰하는 변화율이다. 격자좌표가 고정되어 있어도
그 격자점의 공간 위치는 이동할 수 있다. 연쇄법칙(chain rule)을 적용하면

$$
\left.\frac{\partial q_{ALE}}{\partial t}\right|_{\boldsymbol\xi}
=\left.\frac{\partial q}{\partial t}\right|_{\boldsymbol x}
+\frac{\partial q}{\partial x_i}
\left.\frac{\partial\psi_i}{\partial t}\right|_{\boldsymbol\xi}
=\left.\frac{\partial q}{\partial t}\right|_{\boldsymbol x}
+\boldsymbol w\cdot\nabla_xq
$$

이다. 따라서 $Dq/Dt=\left.\partial q/\partial t\right\vert_{\boldsymbol x}+\boldsymbol v\cdot\nabla_xq$에서 고정 위치의 시간미분을 위 식으로 대체하면

$$
\frac{Dq}{Dt}=\left.\frac{\partial q_{ALE}}{\partial t}\right|_{\boldsymbol\xi}
+(\boldsymbol v-\boldsymbol w)\cdot\nabla_x q
$$

가 된다. 두 식의 우변은 모두 $\boldsymbol x=\boldsymbol\psi(\boldsymbol\xi,t)$인
동일한 공간 위치와 시각에서 평가하며, $\nabla_xq$는 **공간좌표에 대한 기울기**이다.
$\boldsymbol w=\boldsymbol v$이면 이송항이 사라지고, $\boldsymbol w=\boldsymbol0$이면
Eulerian 표현으로 돌아간다. 즉, Lagrangian과 Eulerian은 ALE의 두 특수한 선택이다.

여기서 $\boldsymbol v-\boldsymbol w$는 공간좌표로 표현한 상대속도이다.
일반적인 변형 격자에서는 이것을 물질점의 격자좌표 변화율 $D\boldsymbol\xi/Dt$와
그대로 동일시할 수 없다. 아래 예제처럼 격자가 균일하게 병진하고 두 좌표계의
축 방향과 길이 척도가 같을 때에는 두 값이 일치한다.

물질을 따라가는 격자(Lagrangian mesh)는 큰 변형에서 심하게 찌그러질 수 있고, 고정 격자(Eulerian mesh)는 움직이는
경계를 표현하기 어려울 수 있다. ALE는 격자를 조절하여 이 문제를 줄이는 데 사용되며,
압출 같은 큰 소성변형이나 유체–구조 상호작용에서 유용하다.

격자 운동은 경계조건을 만족해야 하며, 격자 사상은 역변환 가능해야 한다.[^mesh-inverse]

## 2.1. 이동하는 격자에서 온도를 관찰하는 예제

1.4절의 2차원 온도장과 물질 속도를 다시 사용하자.

$$
T(x_1,x_2,t)=20\,{}^\circ\mathrm C
+\left(10\,{}^\circ\mathrm C/\mathrm m\right)x_1
-\left(5\,{}^\circ\mathrm C/\mathrm m\right)x_2
+\left(3\,{}^\circ\mathrm C/\mathrm s\right)t,
\qquad
\boldsymbol v=(2,1)\,\mathrm{m/s}.
$$

이번에는 계산 격자를 $x_1$ 방향으로 $1\,\mathrm{m/s}$의 속도로 이동시킨다.
격자좌표 $\boldsymbol\xi=(\xi_1,\xi_2)$를 길이 단위 m로 정의하면 격자의 운동은

$$
x_1=\xi_1+\left(1\,\mathrm{m/s}\right)t,
\qquad x_2=\xi_2,
\qquad \boldsymbol w=(1,0)\,\mathrm{m/s}
$$

이다. $\boldsymbol\xi$를 고정한다는 것은 **같은 격자점을 따라간다**는 뜻이다.
이 예제에서는 격자점의 속도 $\boldsymbol w$와 물질점의 속도 $\boldsymbol v$가
다르므로, 같은 격자점을 따라가는 관찰자는 계속 같은 물질점을 관찰하는 것이 아니다.

먼저 격자의 경로를 온도장에 대입하면

$$
\begin{aligned}
T_{ALE}(\boldsymbol\xi,t)
&=T\bigl(\xi_1+(1\,\mathrm{m/s})t,\xi_2,t\bigr)\\
&=20\,{}^\circ\mathrm C
+\left(10\,{}^\circ\mathrm C/\mathrm m\right)\xi_1
-\left(5\,{}^\circ\mathrm C/\mathrm m\right)\xi_2
+\left(13\,{}^\circ\mathrm C/\mathrm s\right)t.
\end{aligned}
$$

따라서 같은 격자점에서 기록하는 온도의 시간 변화율은

$$
\left.\frac{\partial T_{ALE}}{\partial t}\right|_{\boldsymbol\xi}
=13\,{}^\circ\mathrm C/\mathrm s
$$

이다. 이 값에는 고정 위치의 온도 상승률 $3\,{}^\circ\mathrm C/\mathrm s$에 더해,
격자 자체가 따뜻한 쪽으로 이동하는 효과 $10\,{}^\circ\mathrm C/\mathrm s$가 포함된다.

물질의 격자에 대한 상대속도는

$$
\boldsymbol v-\boldsymbol w=(1,1)\,\mathrm{m/s}
$$

이므로, 격자를 기준으로 물질이 이동하면서 경험하는 추가 변화율은

$$
\begin{aligned}
(\boldsymbol v-\boldsymbol w)\cdot\nabla_xT
&=\left(1\,\mathrm{m/s}\right)\left(10\,{}^\circ\mathrm C/\mathrm m\right)
+\left(1\,\mathrm{m/s}\right)\left(-5\,{}^\circ\mathrm C/\mathrm m\right)\\
&=5\,{}^\circ\mathrm C/\mathrm s.
\end{aligned}
$$

두 항을 더하면 물질미분은

$$
\boxed{\frac{DT}{Dt}
=\left.\frac{\partial T_{ALE}}{\partial t}\right|_{\boldsymbol\xi}
+(\boldsymbol v-\boldsymbol w)\cdot\nabla_xT
=13+5=18\,{}^\circ\mathrm C/\mathrm s}
$$

가 된다. 이는 1.4절에서 물질점을 직접 따라가며 계산한 결과와 같다.

같은 온도장과 물질 운동에 대해 격자 속도를 달리 선택하면 다음과 같다.
표의 변화율 단위는 모두 ${}^\circ\mathrm C/\mathrm s$이다.

| 기술법 | 격자 속도 $\boldsymbol w$ ($\mathrm{m/s}$) | 같은 격자점의 온도 변화율 | 상대속도에 의한 이송항 | 물질미분 $DT/Dt$ |
| ------ | --------------------------------------- | ----------------------- | --------------------- | --------------- |
| Eulerian | $(0,0)$ | $3$ | $15$ | $18$ |
| 이 예제의 ALE | $(1,0)$ | $13$ | $5$ | $18$ |
| Lagrangian | $(2,1)=\boldsymbol v$ | $18$ | $0$ | $18$ |

즉, **격자 속도에 따라 두 항에 나뉘어 들어가는 값은 달라져도, 같은 물질점의
물질미분은 변하지 않는다.** 특히 ALE 격자점에서의 시간 변화율 $13$을 그대로
물질미분으로 사용하면 상대속도에 의한 변화율 $5$를 빠뜨리게 된다.


## 2.2. 압출에서 ALE가 유용한 이유

압출(extrusion)은 램(ram)이 소재를 밀어 좁은 금형 출구로 통과시키는 공정이다.
소재가 금형 입구에서 방향을 바꾸고 단면이 줄어들면서 큰 소성변형이 발생한다.
이처럼 공간적으로 변형이 불균일한 경우에는, 앞의 균일 병진운동 예제와 달리
재료를 따라가는 격자가 크게 찌그러질 수 있다.

![같은 압출 형상에서 Eulerian 고정 격자, Lagrangian 변형 격자, ALE 조정 격자를 비교한 개념도](/assets/img/lecture_notes/displacement/extrusion_three_descriptions.png)

위 그림은 **같은 순간의 재료 형상과 금형을 세 기술법으로 표현한 개념도**이며,
실제 해석 결과는 아니다. 빨간 윤곽선은 재료 경계, 파란 선은 계산 격자,
빗금 영역은 고정된 금형이다. 세 패널은 시간에 따른 연속 장면이 아니다.

- **(a) Eulerian:** 재료가 고정된 배경 격자를 통과한다. 재료 경계는 격자선과 일치할 필요가 없으며, 경계가 요소 내부를 지날 수 있다. 금형 영역에 겹쳐 보이는 배경 격자는 재료가 금형 내부로 흐른다는 뜻이 아니다.
- **(b) Lagrangian:** 격자가 재료를 따라 움직인다. 재료 경계를 따라가지만, 금형 입구에서 불균일한 변형을 받아 요소의 형상이 심하게 찌그러질 수 있다.
- **(c) ALE:** 재료 경계를 표현하면서 내부 격자의 운동을 조절한다. 격자가 물질점을 그대로 따라갈 필요가 없으므로 요소의 왜곡을 줄일 수 있으며, 상대운동에 따른 재료 이력의 이송이 필요하다.

Lagrangian 기술법은 재료의 표면과 이력을 따라가기 쉽지만, 변형이 집중되면 요소의
심한 왜곡이 계산의 정확도와 안정성에 영향을 줄 수 있다. Eulerian 기술법에서는
격자가 고정되므로 재료 변형에 따른 격자 왜곡은 없지만, 움직이는 재료 표면과
금형 접촉을 별도로 표현해야 한다. ALE에서는 경계조건에 맞게 경계 격자의 운동을
정하면서 내부 격자의 운동을 조절하여, 재료 형상 표현과 격자 품질을 함께 고려할 수 있다.

여기서 $\boldsymbol n$을 경계의 단위 법선벡터라 하자.
고정된 금형과 접촉하는 경계에서는 격자가 금형을 관통하지 않도록 하되,
접선 방향 이동은 허용할 수 있다. 재료의 자유표면을 추적하는 경계에서는 격자와
재료의 법선 속도를 일치시키고(즉 $\boldsymbol v\cdot\boldsymbol n=\boldsymbol w\cdot\boldsymbol n$), 내부에서는 요소의 왜곡을 줄이도록 격자점을 이동시킬 수 있다.
자유표면의 접선 방향 격자 속도는 경계 형상을 유지하는 범위에서 조절할 수 있다. 따라서 ALE의 격자 속도는
경계조건과 격자 품질을 고려하여 정하며, 모든 곳에서 물질 속도와 격자 속도가 같을 필요는 없다.

## 2.3. 격자 재배치와 재료 이력의 전달

소성변형 해석에서는 적분점에 응력, 누적 소성변형률, 경화변수 등 재료의 현재 상태와
이력이 저장된다. 격자점을 이동시키면 적분점의 공간 위치도 바뀌므로, 기존 값을
같은 요소·적분점 번호에 그대로 남겨두어서는 재료 이력을 올바르게 표현할 수 없다.
**재료에 대해 격자를 재배치할 때는 기존 재료 상태를 새 격자에 전달하는 remapping도 필요하다.**

![압출에서 격자 재배치 전후와 적분점 상태변수 전달을 비교한 개념도](/assets/img/lecture_notes/displacement/ale_extrusion_remapping.png)

위 그림은 앞의 세 기술법 비교와 달리 **ALE에서 격자를 재배치하기 전과 후**를
비교한다. 왼쪽은 재료를 따라 찌그러진 격자이고, 오른쪽은 **같은 물리적 시각과
같은 재료 형상에서** 내부 격자점을 재배치한 상태이다. 이 과정은 재료의 추가적인
압출이나 변형을 뜻하지 않는다. 두 패널의 요소 수와 연결 관계는 같으며,
격자선의 배치만 달라진다.

격자 재배치와 이송을 분리하는 ALE 구현은 다음과 같이 이해할 수 있다.

1. **재료의 변형 계산:** 한 시간 증분 동안 재료를 따라 운동과 구성식을 계산하여 응력과 상태변수를 갱신한다.
2. **격자 재배치(rezoning):** 해당 시각의 재료 형상을 유지하면서 격자점을 이동시켜 요소의 모양을 개선한다.
3. **상태 전달(remapping):** 기존 격자에서 표현한 물리량과 재료 이력을 새 격자로 옮긴다.

위 격자 재배치 그림의 빨간 점과 원은 재배치 전후에 상태를 저장하는 적분점을 개념적으로
표시한다. 같은 재료 이력을 표현해야 하지만, 전후의 적분점을 번호에 따라 일대일로
대응시켜 값을 복사한다는 뜻은 아니다. 기존 상태의 공간 분포로부터 새 적분점에
필요한 값을 재구성해야 한다. 배경의 같은 색 분포는 재배치만으로 물리적 상태가
바뀌어서는 안 된다는 의도를 나타내며, 실제 전달에는 수치 오차가 생길 수 있다.

이 과정은 앞의 ALE 식에서 상대속도 $\boldsymbol v-\boldsymbol w$에 의한 이송을
수치적으로 처리하는 것과 연결된다. 다만 모든 ALE 구현이 위의 세 단계를 별도로
수행하는 것은 아니며, 이송항을 방정식에서 직접 처리하는 구현도 있다.
상태 전달에서는 질량·운동량·에너지의 보존과 재료 모델의 상태변수 사이의 일관성을
고려해야 한다. 특히 이력 의존성이 강한 재료 모델에서는 단순한 값의 보간만으로
충분한지 검토해야 하므로, ALE에는 격자 품질 개선의 이점과 함께 추가 계산 및 전달 오차가 따른다.

# 3. 연습문제

## 문제 1: 무엇을 고정하는가?

온도장 $T(\boldsymbol x,t)$에 대해 다음 세 시간미분이 각각 어떤 관찰자를 뜻하는지 설명하라.
격자좌표를 고정한 관찰자가 항상 같은 물질점을 따라가는지도 설명하라.

1. $\left.\partial T/\partial t\right\vert_{\boldsymbol x}$
2. $\left.\partial T_L/\partial t\right\vert_{\boldsymbol X}$
3. $\left.\partial T_{ALE}/\partial t\right\vert_{\boldsymbol\xi}$

<!--
풀이와 해답:
1은 공간의 같은 위치에서 관찰하는 온도 변화율이다.
2는 같은 물질점을 따라 관찰하는 온도 변화율이며 물질미분 DT/Dt와 같다.
3은 같은 격자점을 따라 관찰하는 온도 변화율이다.
격자점과 물질점의 속도가 다르면 같은 격자점은 같은 물질점을 계속 따라가지 않는다.
w=v이면 두 관찰이 일치한다. 격자좌표가 고정되어도 공간 위치는 이동할 수 있다.
-->

## 문제 2: 정상 온도장에서의 이동

시간에 따라 변하지 않는 1차원 온도장이 다음과 같다.

$$
T(x)=30\,{}^\circ\mathrm C+\left(4\,{}^\circ\mathrm C/\mathrm m\right)x
$$

한 물질점이 $v=-1.5\,\mathrm{m/s}$로 이동한다. 고정 위치에서의 시간 변화율과
물질미분을 각각 구하고, 결과의 부호가 뜻하는 바를 설명하라.

<!--
풀이와 해답:
온도장이 시간에 의존하지 않으므로 고정 위치의 시간 변화율은 0이다.
DT/Dt=v dT/dx=(-1.5) 곱하기 4=-6 deg C/s이다.
물질점이 x가 감소하는 방향, 즉 더 차가운 쪽으로 이동하므로 경험하는 온도는 감소한다.
-->

## 문제 3: 2차원 온도장의 물질미분

온도장과 일정한 물질 속도가 다음과 같이 주어진다.

$$
T(x_1,x_2,t)=25\,{}^\circ\mathrm C
+\left(6\,{}^\circ\mathrm C/\mathrm m\right)x_1
-\left(2\,{}^\circ\mathrm C/\mathrm m\right)x_2
+\left(1\,{}^\circ\mathrm C/\mathrm s\right)t,
\qquad
\boldsymbol v=(1,2)\,\mathrm{m/s}.
$$

고정 위치의 시간 변화율, 두 방향의 이송항, 물질미분을 각각 구하라.
또한 $t=0$에 $\boldsymbol X=(X_1,X_2)$에 있던 물질점의 경로를 온도장에
대입하여, $\boldsymbol X$를 고정한 시간미분으로 검산하라.

<!--
풀이와 해답:
고정 위치의 시간 변화율은 1 deg C/s이다.
x_1 방향의 기여는 1 곱하기 6=6 deg C/s이고,
x_2 방향의 기여는 2 곱하기 (-2)=-4 deg C/s이다.
따라서 이송항은 2 deg C/s, 물질미분은 1+6-4=3 deg C/s이다.
경로는 x_1=X_1+(1 m/s)t, x_2=X_2+(2 m/s)t이다.
이를 대입하면 T_L=25 deg C+(6 deg C/m)X_1-(2 deg C/m)X_2+(3 deg C/s)t이다.
X_1, X_2를 고정하고 시간미분하면 3 deg C/s로 일치한다.
-->

## 문제 4: 같은 물질 운동을 서로 다른 격자로 관찰하기

문제 3의 온도장과 물질 속도를 사용한다. 일정한 격자 속도 $\boldsymbol w$를
다음과 같이 선택할 때 빈칸을 채워라. 변화율의 단위는 모두 ${}^\circ\mathrm C/\mathrm s$이다.

| 기술법 | $\boldsymbol w$ ($\mathrm{m/s}$) | 같은 격자점의 온도 변화율 | 상대속도에 의한 이송항 | 물질미분 |
| ------ | ------------------------------ | ----------------------- | --------------------- | -------- |
| Eulerian | $(0,0)$ | ? | ? | ? |
| ALE | $(0,1)$ | ? | ? | ? |
| Lagrangian | $(1,2)$ | ? | ? | ? |

다음 관계를 이용하고, 격자 속도가 달라도 마지막 열의 값이 같은 이유를 설명하라.

$$
\left.\frac{\partial T_{ALE}}{\partial t}\right|_{\boldsymbol\xi}
=\left.\frac{\partial T}{\partial t}\right|_{\boldsymbol x}
+\boldsymbol w\cdot\nabla_xT
$$

<!--
풀이와 해답:
Eulerian: 같은 격자점의 변화율 1, 상대속도 이송항 2, 물질미분 3이다.
ALE: 같은 격자점의 변화율 1+0 곱하기 6+1 곱하기 (-2)=-1이다.
상대속도는 v-w=(1,1) m/s이고, 이송항은 6-2=4이므로 물질미분은 -1+4=3이다.
Lagrangian: 같은 격자점의 변화율은 1+6-4=3이고 상대속도가 0이므로 이송항은 0이다.
격자 속도는 관찰 방법을 바꾸지만 주어진 물질 운동과 온도장을 바꾸지 않으므로
같은 물질점이 경험하는 온도 변화율은 모두 3 deg C/s이다.
-->

## 문제 5: 시간에 따라 변하지 않는 속도장과 가속도

1차원 속도장이 $v(x)=k x$로 주어지고 $k=0.5\,\mathrm{s^{-1}}$이다.
물질점이 $x=4\,\mathrm m$를 지나는 순간의 속도와 가속도를 구하라.
속도장이 시간에 의존하지 않는데도 가속도가 생기는 이유를 설명하라.

<!--
풀이와 해답:
v=0.5 곱하기 4=2 m/s이다.
고정 위치의 속도 시간미분은 0이고 dv/dx=k=0.5 /s이다.
물질점의 가속도 Dv/Dt=v dv/dx=2 곱하기 0.5=1 m/s^2이다.
물질점이 이동하면서 공간적으로 더 큰 속도를 갖는 위치로 가기 때문에 가속된다.
-->

[^mesh-inverse]: 격자 사상 $\boldsymbol x=\boldsymbol\psi(\boldsymbol\xi,t)$의 역변환 $\boldsymbol\xi=\boldsymbol\psi^{-1}(\boldsymbol x,t)$는 같은 시각의 공간 위치에서 격자좌표를 찾는 것이다. 예를 들어 일정한 격자 속도 $w_1$에 대해 $x_1=\xi_1+w_1t$, $x_2=\xi_2$이면 $\xi_1=x_1-w_1t$, $\xi_2=x_2$이다. 이는 물질점의 이름표 $\boldsymbol X$를 구하는 것과 다르다. 미분 가능한 국소 역변환에는 $\det(\partial\boldsymbol\psi/\partial\boldsymbol\xi)\ne0$이 필요하며, 전체 영역에서는 격자가 겹치지 않는 일대일 대응도 확보해야 한다.
