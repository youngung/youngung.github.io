---
layout: distill
title: 물질미분과 ALE 기술법
description: 물질점을 따라 관찰하는 변화율과 계산 격자의 운동
target: 학부 고학년
permalink:
featured: true
prerequisite: 유한변형의 운동학
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

<span id="부록-a-물질미분-material-derivative"></span>

# 1. 물질미분 (material derivative)

<span id="a1-물질점을-따라-관찰하는-변화율"></span>

## 1.1. 물질점을 따라 관찰하는 변화율

**물질미분은 움직이는 물질점이 경험하는 물리량의 변화율**이다.
온도장 $T(\boldsymbol x,t)$에서 고정된 위치의 온도 변화율은
$\left.\partial T/\partial t\right|_{\boldsymbol x}$다. 그러나 물질점은 이동하므로,
다른 온도의 위치로 이동하며 경험하는 변화도 포함해야 한다.

물질점의 운동을 $\boldsymbol x=\boldsymbol\Phi(\boldsymbol X,t)$로 나타내면,
같은 물질점이 경험하는 온도는

$$
T_L(\boldsymbol X,t)=T(\boldsymbol\Phi(\boldsymbol X,t),t)
$$

이다. 물질점의 이름표 $\boldsymbol X$를 고정하고 연쇄법칙을 적용하면

$$
\begin{aligned}
\frac{DT}{Dt}
&=\left.\frac{\partial T_L}{\partial t}\right|_{\boldsymbol X}\\
&=\left.\frac{\partial T}{\partial t}\right|_{\boldsymbol x}
+\frac{\partial T}{\partial x_i}
\left.\frac{\partial\Phi_i}{\partial t}\right|_{\boldsymbol X}\\
&=\left.\frac{\partial T}{\partial t}\right|_{\boldsymbol x}
+v_i\frac{\partial T}{\partial x_i}.
\end{aligned}
$$

여기서 $\boldsymbol v=\left.\partial\boldsymbol\Phi/\partial t\right|_{\boldsymbol X}$는
물질점의 속도다. 반복 첨자 $i$는 세 공간 방향에 대한 합을 뜻하며,
우변은 해당 물질점의 현재 위치에서 평가한다. 벡터 표기로 쓰면

$$
\boxed{\frac{DT}{Dt}
=\left.\frac{\partial T}{\partial t}\right|_{\boldsymbol x}
+\boldsymbol v\cdot\nabla_xT}.
$$

첫 항은 고정된 위치에서의 시간 변화이고, 둘째 항은 물질점의 이동에 의한 변화인
**이송항 (convective term)**이다. 따라서 Lagrangian 기술법에서는 같은 물질점의
시간 미분이 곧 물질미분이며, Eulerian 기술법에서는 고정 위치의 시간 미분에 이송항을 더한다.

<span id="a2-시간에-따라-변하지-않는-온도장에서의-물질미분"></span>

## 1.2. 시간에 따라 변하지 않는 온도장에서의 물질미분

$x$를 m 단위로 측정할 때, 시간에 따라 **변하지 않는** 1차원 온도장을

$$
T(x)=20\,{}^\circ\mathrm C
+\left(10\,{}^\circ\mathrm C/\mathrm m\right)x
$$

라고 하자. 물질점이 $v=2\,\mathrm{m/s}$로 이동하면

$$
\left.\frac{\partial T}{\partial t}\right|_x=0,
\qquad
\frac{DT}{Dt}=v\frac{dT}{dx}
=2\times10=20\,{}^\circ\mathrm C/\mathrm s.
$$

고정된 온도계의 값은 변하지 않지만, 이동하는 물질점은 더 따뜻한 곳으로 가므로
초당 $20\,{}^\circ\mathrm C$의 온도 증가를 경험한다.

![정상 온도장에서 고정 관찰점과 이동하는 물질점이 기록하는 온도의 비교](/assets/img/lecture_notes/displacement/material_derivative_temperature.png)

위 그림의 (a)에서 파란 선은 시간에 따라 변하지 않는 온도장이고, 빨간 점들은
$x(0)=0$에서 출발한 **같은 물질점**의 $t=0,1,2\,\mathrm s$ 위치와 온도를 나타낸다.
초록색 원은 $x=1\,\mathrm m$에 고정된 관찰점이다. (b)는 각 관찰자가 기록하는 온도를
시간에 대해 그린 것으로, 고정점에서는 $30\,{}^\circ\mathrm C$로 일정하지만
이동점에서는 $20,40,60\,{}^\circ\mathrm C$로 상승한다.

<span id="a3-공간과-시간에-모두-의존하는-온도장"></span>

## 1.3. 공간과 시간에 모두 의존하는 온도장

이번에는 A.2의 온도장이 모든 위치에서 시간에 따라 상승하는 경우를 생각하자.
$x$는 m, $t$는 s 단위로 측정하며,

$$
T(x,t)=20\,{}^\circ\mathrm C
+\left(10\,{}^\circ\mathrm C/\mathrm m\right)x
+\left(3\,{}^\circ\mathrm C/\mathrm s\right)t
$$

라고 하자. 고정된 위치에서의 온도 상승률과 공간에 대한 기울기는 각각

$$
\left.\frac{\partial T}{\partial t}\right|_x
=3\,{}^\circ\mathrm C/\mathrm s,
\qquad
\frac{\partial T}{\partial x}=10\,{}^\circ\mathrm C/\mathrm m
$$

이다. 물질점이 $v=2\,\mathrm{m/s}$로 이동하면

$$
\boxed{\frac{DT}{Dt}
=\left.\frac{\partial T}{\partial t}\right|_x
+v\frac{\partial T}{\partial x}
=3+2\times10=23\,{}^\circ\mathrm C/\mathrm s}.
$$

고정된 온도계는 초당 $3\,{}^\circ\mathrm C$의 상승을 측정한다.
이동하는 물질점은 이 시간 변화에 더해 더 따뜻한 위치로 이동하는 효과도 경험하므로,
초당 $23\,{}^\circ\mathrm C$의 상승을 경험한다.

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
$v=-2\,\mathrm{m/s}$로 이동하면 $DT/Dt=3-20=-17\,{}^\circ\mathrm C/\mathrm s$다.
각 위치의 온도는 상승하고 있어도, 물질점은 더 차가운 위치로 빠르게 이동하므로
자신이 경험하는 온도는 감소한다.

<span id="a4-속도의-물질미분과-가속도"></span>

## 1.4. 속도의 물질미분과 가속도

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
| ALE | 격자 품질과 경계조건에 맞게 이동 | $\boldsymbol v-\boldsymbol w$ |

$q_{ALE}(\boldsymbol\xi,t)=q(\boldsymbol\psi(\boldsymbol\xi,t),t)$라고 정의하면,
연쇄법칙에 의해

$$
\frac{Dq}{Dt}=\left.\frac{\partial q_{ALE}}{\partial t}\right|_{\boldsymbol\xi}
+(\boldsymbol v-\boldsymbol w)\cdot\nabla_x q
$$

가 된다. 우변은 대응하는 동일한 위치에서 평가한다. 물질이 격자를 통과하므로
상대속도에 의한 이송을 계산해야 한다.

물질을 따라가는 격자(Lagrangian mesh)는 큰 변형에서 심하게 찌그러질 수 있고, 고정 격자(Eulerian mesh)는 움직이는
경계를 표현하기 어려울 수 있다. ALE는 격자를 조절하여 이 문제를 줄이는 데 사용되며,
압출 같은 큰 소성변형이나 유체–구조 상호작용에서 유용하다.

격자 운동은 경계조건을 만족해야 하며, 격자 사상은 역변환 가능해야 한다.
좌표와 미분에 관한 추가 설명은
[COMSOL 공식 문서](https://doc.comsol.com/6.3/doc/com.comsol.help.comsol/comsol_ref_deformedmeshes.34.07.html)를 참고한다.
