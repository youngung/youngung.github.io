---
layout: distill
title: 선형 탄성
description: 등방 선형탄성과 Hooke 법칙
target: 학부 고학년
permalink:
featured: true
prerequisite: 응력과 변형률, 벡터와 행렬
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

# 1. 선형 탄성 (linear elasticity) 거동

- 힘->응력
- 변위->변형률

- 응력과 변형률로 표현된 자극과 반응 사이의 관계는?
  - 많은 금속 재료의 경우, 매우 높은 응력 값이 가해지는 게 아니라면 탄성 거동만을 보인다.
  - 그럴경우 응력이 가해지는 동안에만 변형률이 보이고, 응력이 사라지면 변형률이 사라진다.
  - 그리고 많은 금속 재료들은 탄성을 보일 때, 응력과 변형률이 선형 비례한다.

- 위 거동을 만족시키는 응력과 변형률의 관계는 아래와 같이 표현된다.

$$\boldsymbol\sigma=\boldsymbol E : \boldsymbol \varepsilon$$

- 위 관계를 처음 보인 Hooke의 이름을 따서, 위 식을 Hooke의 법칙이라고도 부른다.

- 만약 응력과 변형률이 모두 스칼라라면 기울기 $E$도 스칼라가 된다.

# 2. Young's modulus (영률)

- Hooke의 법칙에서 보이는 스칼라 $E$를 영률이라 부른다.

- 변형률이 단위가 없으므로, 영률은 응력과 같은 단위를 가진다 (Pa, MPa 등)

- 영률은 재료의 성질이다. 강철과 고무에 동일한 응력을 가했을 때, 강철의 변형률이 훨씬 작다. 따라서 강철의 영률이 고무의 영률에 비해 매우 크다.

# 3. 포아송 효과 (Poisson effect)

- 인장하는 길이가 $\mathbf {\boldsymbol{e}}_1$ 방향일 때, 수직 변형이 $\mathbf {\boldsymbol{e}}_1$축으로만 발생하지 않는다. 그에 수직한 방향, 예를 들어 $\mathbf {\boldsymbol{e}}_2$로는 길이가 줄어드는 수직 변형이 발생할 수 있다.

- 이럴 때, 적어도 두 수직 변형률 성분 $\varepsilon_{11}$, $\varepsilon_{22}$가 0이 아님을 알 수 있다. 더욱 구체적으로는 아래와 같은 값의 범위를 가지게 된다.

  - $\varepsilon_{11}>0$
  - $\varepsilon_{22}<0$

- 이때 발생하는 두 수직 변형률 성분의 비를 poisson 비로 정의한다.

$$\nu=-\frac{\varepsilon_{22}}{\varepsilon_{11}}$$

# 4. 3차원으로 확장하여 표현되는 Hooke의 법칙

- 응력텐서 $\boldsymbol \sigma$와 변형률 텐서 $\boldsymbol \varepsilon$의 선형 관계를 표현해야 하겠다. 이를 아래와 같이 표현할 수 있다.

$$ [\boldsymbol\sigma]_{ij} = \sum_{k=1}^3\sum_{l=1}^3 [\boldsymbol E]_{ijkl} [\boldsymbol\varepsilon] _{kl} \text{ with } i=1,2,3\ \ \ j=1,2,3$$

- 응력과 변형률 텐서는 각각 랭크2의 매트릭스로, 탄성계수 텐서 $E$는 랭크 4의 매트릭스로 표현됨을 알 수 있다.

# 5. 등방성 재료의 경우

- 재료의 물성이 방향에 관계 없을 때, 앞선 3차원 Hooke의 법칙에 활용된 랭크4의 $E$텐서를 두 스칼라 $\lambda$와 $G$로 표현할 수 있다.

$$
\boldsymbol \sigma = \lambda  \boldsymbol I tr(\boldsymbol \varepsilon) + 2G \boldsymbol \varepsilon
$$

- 위를 인덱스를 활용해 표현하면

$$
\sigma_{ij} = \lambda  \delta_{ij} \sum_{k=1}^3(\varepsilon_{kk}) + 2G\varepsilon_{ij}, \text{ with } i=1,2,3\ \ \ j=1,2,3
$$

- $tr(\boldsymbol\varepsilon)$는 체적 변형률이며 아래와 같이 정의된다.
  $$tr(\boldsymbol\varepsilon)=\sum_{k=1}^3\varepsilon_{kk}=\varepsilon_{11}+\varepsilon_{22}+\varepsilon_{33} $$

- $\boldsymbol I$는 랭크2 단위 텐서이며, 아래와 같은 매트릭스 형태로 표현된다.

$$
\boldsymbol I = \begin{bmatrix}
1 &0 &0 \\
0 &1 &0 \\
0 &0 &1 \\
\end{bmatrix}
$$

- $\delta_{ij}$는 크로네커 델타(Kronecker delta)로 불리며 아래 성질을 가진다.

  - $\delta_{ij}=0, \text{ if } i\ne j$
  - $\delta_{ij}=1, \text{ if } i=j$
  - 따라서 $\delta_{ij}$는 $\boldsymbol I$와 동일한 역할을 수행한다.

- G는 전단 탄성계수이다.

- $\lambda$는 Lame의 제1 상수이다.

# 6. 선형 등방 Hooke 법칙 상세 설명

- 체적탄성계수를 $K=\lambda+2G/3$라 하면, 세 수직응력의 평균(평균응력)은
  체적변화율 $\operatorname{tr}(\boldsymbol\varepsilon)$와 다음 관계를 갖는다.

$$
\frac{\operatorname{tr}(\boldsymbol\sigma)}{3}=K\operatorname{tr}(\boldsymbol\varepsilon)
$$

  전단 성분은 체적변화와 무관하게 $\sigma_{ij}=2G\varepsilon_{ij}\ (i\ne j)$로
  주어진다.

- 응력 성분을 각기 풀어 표현하면

  - 수직 성분의 경우
    $$\sigma_{11}=\lambda (\varepsilon_{11}+\varepsilon_{22}+\varepsilon_{33}) + 2G\varepsilon_{11}$$

$$\sigma_{22}=\lambda (\varepsilon_{11}+\varepsilon_{22}+\varepsilon_{33}) + 2G\varepsilon_{22}$$

$$\sigma_{33}=\lambda (\varepsilon_{11}+\varepsilon_{22}+\varepsilon_{33}) + 2G\varepsilon_{33}$$

- 전단 성분의 경우

$$ \sigma_{12}=2G\varepsilon_{12} $$

$$ \sigma_{13}=2G\varepsilon_{13} $$

$$ \sigma_{23}=2G\varepsilon_{23} $$

# 7. 선형 등방 Hooke 법칙에서의 상수 관계

여기서는 **등방 선형탄성체의 기계적 응력–변형률 관계**에 사용하는 탄성상수들을
정리한다. 아래 변환식은 이방성 재료의 방향별 탄성계수에 그대로 적용할 수 없다.

| 기호 | 이름 | 의미와 정의 |
| ---- | ---- | ----------- |
| $E$ | 영률 또는 Young 계수 (Young's modulus) | 일축 응력에서 축 방향 응력과 변형률의 비: $E=\sigma_{11}/\varepsilon_{11}$ |
| $\nu$ | Poisson 비 (Poisson's ratio) | 일축 응력에서 축 방향 변형률에 대한 횡변형률의 음의 비: $\nu=-\varepsilon_{22}/\varepsilon_{11}$ |
| $G=\mu$ | 전단탄성계수, Lamé의 제2 상수 (shear modulus) | 전단응력과 공학전단변형률의 비: $G=\sigma_{12}/\gamma_{12}$, $\gamma_{12}=2\varepsilon_{12}$ |
| $K$ | 체적탄성계수 (bulk modulus) | 정수압에 대한 체적변형의 저항: $K=-p/\varepsilon_v$, $\varepsilon_v=\operatorname{tr}(\boldsymbol\varepsilon)$ |
| $\lambda$ | Lamé의 제1 상수 (first Lamé parameter) | $\boldsymbol\sigma=\lambda\boldsymbol I\operatorname{tr}(\boldsymbol\varepsilon)+2G\boldsymbol\varepsilon$에서 체적변형률에 곱해지는 상수 |
| $M$ | 구속탄성계수 또는 P파 탄성계수 (constrained / P-wave modulus) | 횡방향 변형을 막은 일축 변형률 상태에서 $M=\sigma_{11}/\varepsilon_{11}$ |

$E$, $G$, $K$, $\lambda$, $M$의 단위는 모두 응력과 같은 Pa이며,
$\nu$는 단위가 없는 비이다. $\mu$는 $G$의 다른 기호이므로 별도의 독립 상수가 아니다.
체적탄성계수의 역수 $\beta=1/K$는 **압축률(compressibility)**이며 단위는
$\mathrm{Pa^{-1}}$이다.

$E$와 $\nu$의 정의에서 일축 응력이란 $\sigma_{11}$만 0이 아닌 상태이다.
반면 $M$의 정의에서는 $\varepsilon_{11}$만 0이 아니며, 횡방향 응력이 발생할 수 있다.
따라서 **횡방향이 자유로운 인장시험의 $E$와 횡변형을 구속한 경우의 $M$은 다르다.**

일반적인 이방성 탄성체에서는 탄성계수 텐서에 최대 21개의 독립 상수가 필요하지만,
등방 선형탄성체에서는 **서로 독립인 두 탄성상수**로 나머지를 결정할 수 있다.
대표적인 선택은 $(E,\nu)$, $(K,G)$, $(\lambda,G)$이다.

**영률 $E$와 Poisson 비 $\nu$를 알고 있을 때**

$$
G=\mu=\frac{E}{2(1+\nu)},
\qquad
K=\frac{E}{3(1-2\nu)}
$$

$$
\lambda=\frac{E\nu}{(1+\nu)(1-2\nu)},
\qquad
M=\frac{E(1-\nu)}{(1+\nu)(1-2\nu)}
$$

**체적탄성계수 $K$와 전단탄성계수 $G$를 알고 있을 때**

$$
E=\frac{9KG}{3K+G},
\qquad
\nu=\frac{3K-2G}{2(3K+G)}
$$

$$
\lambda=K-\frac{2G}{3},
\qquad
M=K+\frac{4G}{3}
$$

**Lamé 상수 $\lambda$와 $G=\mu$를 알고 있을 때**

$$
E=\frac{G(3\lambda+2G)}{\lambda+G},
\qquad
\nu=\frac{\lambda}{2(\lambda+G)}
$$

$$
K=\lambda+\frac{2G}{3},
\qquad
M=\lambda+2G
$$

위 관계에서 자주 사용하는 식을 모으면 다음과 같다.

$$
\boxed{E=2G(1+\nu)=3K(1-2\nu)}
$$

$$
\boxed{M=\lambda+2G=K+\frac{4G}{3}},
\qquad
\frac{1}{E}=\frac{1}{9K}+\frac{1}{3G}
$$



예를 들어 $E=210\,\mathrm{GPa}$, $\nu=0.30$이면

$$
\begin{aligned}
G&\approx80.77\,\mathrm{GPa}, & K&=175\,\mathrm{GPa},\\
\lambda&\approx121.15\,\mathrm{GPa}, & M&\approx282.69\,\mathrm{GPa}.
\end{aligned}
$$

이다. 이 값들을 $E=9KG/(3K+G)$에 대입하면 원래 영률 $210\,\mathrm{GPa}$를 얻는다.

등방 선형탄성체의 탄성에너지가 양의 정부호이려면 $K>0$, $G>0$이어야 한다.
이는 $E>0$, $-1<\nu<0.5$와 동등하다. $\lambda$는 이 조건 안에서도 음수가 될 수 있다.
$E$를 고정하고 $\nu$가 $0.5$에 가까워지면 $K$가 커져 체적변형이 어려워진다.
정확히 비압축성인 $\nu=0.5$에는 위의 분모가 있는 변환식을 직접 대입할 수 없다.

<!--
탄성상수의 기본 관계는
[A. F. Bower, Applied Mechanics of Solids, 3.2절](https://solidmechanics.org/Text/Chapter3_2/Chapter3_2.php)을,
$M=\lambda+2G$를 포함한 변환 구현은
[SfePy의 탄성계수 변환 코드](https://sfepy.org/doc/_modules/sfepy/mechanics/matcoefs.html)를 참고할 수 있다.
-->

## 7.1. 정수압과 체적탄성계수 {#hydrostatic-pressure}

정수압(hydrostatic pressure)은 물체의 모든 면에 수직으로, 방향에 관계없이 같은
크기로 작용하는 압력이다. 예를 들어 물속에 잠긴 작은 물체를 생각하면, 물이 물체의
표면을 사방에서 안쪽으로 누른다. 여기서는 높이에 따른 압력 차이를 무시하고,
물체 전체에 균일한 압력이 작용하는 경우를 생각한다.

이 강의에서는 **인장응력을 양(+)으로, 압축응력을 음(-)으로** 정한다.
반면 압력 $p$는 압축일 때 양으로 정의하므로, $p>0$인 정수압에 의한 응력은 다음과 같다.

$$
\boldsymbol\sigma=-p\boldsymbol I
=\begin{bmatrix}
-p & 0 & 0 \\
0 & -p & 0 \\
0 & 0 & -p
\end{bmatrix}
$$

즉, 세 수직응력 성분이 모두 $-p$이고 전단응력은 모두 0이다. 이 응력 상태는 좌표축을
회전해도 동일하다. $p<0$이면 세 수직응력이 모두 $-p>0$이므로, 사방으로 당기는 균일한 삼축 인장 상태이다.

등방 선형탄성체에 정수압이 작용하면 세 방향의 수직변형률도 같은 값
$\varepsilon_h$가 된다. 미소변형 범위에서 체적변형률은

$$
\varepsilon_v=\operatorname{tr}(\boldsymbol\varepsilon)
=3\varepsilon_h\approx\frac{\Delta V}{V_0}
$$

이다. 여기서 $V_0$는 변형 전 체적이고 $\Delta V$는 체적의 변화량이다.
등방 Hooke 법칙의 수직 성분에 대입하면

$$
-p=\lambda(3\varepsilon_h)+2G\varepsilon_h
=\left(\lambda+\frac{2G}{3}\right)\varepsilon_v
$$

를 얻는다. 따라서 **체적탄성계수(bulk modulus)** $K$를 이용하면

$$
K=\lambda+\frac{2G}{3}=\frac{E}{3(1-2\nu)},
\qquad
\varepsilon_v=-\frac{p}{K},
\qquad
\varepsilon_h=-\frac{p}{3K}
$$

로 표현할 수 있다. $K$의 단위는 응력과 같고, $K$가 클수록 같은 압력에 의한
체적 감소가 작다. 등방 선형탄성체에서는 정수압에 의해 각 방향이 같은 비율로
줄어들므로, 미소변형 범위에서 형상은 유지되면서 체적이 감소한다.

예를 들어 $E=210\ \mathrm{GPa}$, $\nu=0.3$이면

$$
K=\frac{210}{3(1-0.6)}=175\ \mathrm{GPa}
$$

이다. 여기에 $p=70\ \mathrm{MPa}$가 작용하면 단위를 MPa로 맞추어

$$
\varepsilon_v=-\frac{70}{175000}=-0.0004,
\qquad
\varepsilon_h=\frac{-0.0004}{3}\approx-0.0001333
$$

을 얻는다. 체적변형률이 음수라는 것은 체적이 약 $0.04\%$ 감소함을 뜻한다.

# 8. Voigt 표현법

- 삼차원으로 확장하여 표현한 Hooke의 법칙은 아래와 같다.
  $$ [\boldsymbol\sigma]_{ij} = \sum_{k=1}^3\sum_{l=1}^3 [\boldsymbol E]_{ijkl} [\boldsymbol\varepsilon]_{kl} \text{ with } i=1,2,3\ \ \ j=1,2,3$$

- 응력과 변형률 텐서 모두 6개의 독립 성분만을 가지므로, 6성분을 가지는 랭크1의 행렬로 표현하여 표기하기도 한다.

- 그러한 방법중 Voigt표현을 활용하여 아래와 같이 표현한다.

$$ [\boldsymbol\sigma]^{voigt}=
\begin{bmatrix}
\sigma_{11}\\
\sigma_{22}\\
\sigma_{33}\\
\sigma_{23}\\
\sigma_{13}\\
\sigma_{12}\\
\end{bmatrix}$$


$$ [\boldsymbol\varepsilon]^{voigt}=
\begin{bmatrix}
\varepsilon_{11}\\
\varepsilon_{22}\\
\varepsilon_{33}\\
2\varepsilon_{23}\\
2\varepsilon_{13}\\
2\varepsilon_{12}\\
\end{bmatrix}$$

- 위 방법을 확장하며 Hooke의 법칙을 새로 인덱스로 표기하면

$$
\ [\boldsymbol\sigma]_i^{voigt}=\sum_{j}^6 [\boldsymbol E]_{ij}^{voigt} [\boldsymbol\varepsilon]_j^{voigt}
$$

로 간략히 표기할 수 있겠다. 그리고 이때 탄성계수 텐서가 2랭크 $6\times6$행렬 형태로 표기된다.

- 등방성 재료에서 $[\boldsymbol E]_{ij}^{voigt}$의 각 성분은 아래와 같다.

$$
[\boldsymbol E]^{voigt}=
\begin{bmatrix}
\lambda + 2G & \lambda &\lambda &0 &0 &0 \\
\lambda &\lambda + 2G & \lambda &0 &0 &0 \\
\lambda & \lambda &\lambda + 2G &0 &0 &0 \\
0 & 0 &0 &G &0 &0 \\
0 & 0 &0 &0 &G &0 \\
0 & 0 &0 &0 &0 &G \\
\end{bmatrix}
$$

# 9. Compliance matrix

- Hooke의 법칙을 역으로 표현할 수 있다.

$$
\boldsymbol \varepsilon=\boldsymbol S : \boldsymbol \sigma
$$

- Voigt 표현을 활용하면

$$
[\boldsymbol S]^{voigt}=
\begin{bmatrix}
1/ E& -\nu/E & -\nu/E &0 &0 &0 \\
-\nu/E &1/E & -\nu/E &0 &0 &0 \\
-\nu/E & -\nu/E &1/E &0 &0 &0 \\
0 & 0 &0 &1/G &0 &0 \\
0 & 0 &0 &0 &1/G &0 \\
0 & 0 &0 &0 &0 &1/G \\
\end{bmatrix}
$$


# 10. VPSC에서 사용하는 b-basis

Voigt 표기는 대칭 텐서를 6성분 벡터로 나타내는 방법이다. 그러나 이 강의의 Voigt
변형률 벡터에는 공학전단변형률 $2\varepsilon_{ij}$가 들어가므로, 응력과 변형률의
전단 성분에 서로 다른 배율을 적용한다. VPSC에서 사용하는 **b-basis**는 대칭
2차 텐서 공간에 정규직교 기저를 두어 응력과 변형률에 같은 변환을 적용하는 방법이다.
여기서 b-basis는 공간의 세 좌표축을 바꾸는 것이 아니라, **대칭 텐서를 표현하는
6개의 기저 텐서를 선택하는 것**이다.

**기저 텐서의 정의**

고정된 직교좌표계의 단위벡터를 $\boldsymbol e_1$, $\boldsymbol e_2$,
$\boldsymbol e_3$라 하자. $\boldsymbol e_i\otimes\boldsymbol e_j$는
$(i,j)$ 성분만 1인 기저 텐서이다. VPSC8의 <code>CHG_BASIS</code>에서 사용하는
부호와 순서에 맞추면 다음과 같다.

$$
\begin{aligned}
\boldsymbol b^{(1)}&=\frac{-\boldsymbol e_1\otimes\boldsymbol e_1+\boldsymbol e_2\otimes\boldsymbol e_2}{\sqrt2},\\
\boldsymbol b^{(2)}&=\frac{-\boldsymbol e_1\otimes\boldsymbol e_1-\boldsymbol e_2\otimes\boldsymbol e_2+2\boldsymbol e_3\otimes\boldsymbol e_3}{\sqrt6}.
\end{aligned}
$$

$$
\begin{aligned}
\boldsymbol b^{(3)}&=\frac{\boldsymbol e_2\otimes\boldsymbol e_3+\boldsymbol e_3\otimes\boldsymbol e_2}{\sqrt2},\\
\boldsymbol b^{(4)}&=\frac{\boldsymbol e_1\otimes\boldsymbol e_3+\boldsymbol e_3\otimes\boldsymbol e_1}{\sqrt2},\\
\boldsymbol b^{(5)}&=\frac{\boldsymbol e_1\otimes\boldsymbol e_2+\boldsymbol e_2\otimes\boldsymbol e_1}{\sqrt2},\\
\boldsymbol b^{(6)}&=\frac{\boldsymbol I}{\sqrt3}.
\end{aligned}
$$

이 기저는 이중수축에 대해 정규직교한다.

$$
\boldsymbol b^{(\alpha)}:\boldsymbol b^{(\beta)}=\delta_{\alpha\beta},
\qquad \alpha,\beta=1,\ldots,6
$$

따라서 대칭 텐서 $\boldsymbol A$의 b-basis 성분과 역변환은

$$
A_\alpha^{(b)}=\boldsymbol A:\boldsymbol b^{(\alpha)},
\qquad
\boldsymbol A=\sum_{\alpha=1}^{6}A_\alpha^{(b)}\boldsymbol b^{(\alpha)}
$$

이며, 실제 6성분 벡터는 다음과 같다.

$$
[\boldsymbol A]^{(b)}=
\begin{bmatrix}
(A_{22}-A_{11})/\sqrt2\\
(2A_{33}-A_{11}-A_{22})/\sqrt6\\
\sqrt2 A_{23}\\
\sqrt2 A_{13}\\
\sqrt2 A_{12}\\
(A_{11}+A_{22}+A_{33})/\sqrt3
\end{bmatrix}
$$

**대각합이 0인 5성분과 구형 1성분**

첫 다섯 기저의 대각합은 0이므로 처음 5성분은 체적변화와 무관한 부분을 나타낸다.
6번째 성분은 $A_6^{(b)}=\operatorname{tr}(\boldsymbol A)/\sqrt3$으로,
구형 부분 $\frac{\operatorname{tr}(\boldsymbol A)}{3}\boldsymbol I$을 나타낸다.
체적변화가 없는 소성 변형률속도처럼 대각합이 0인 텐서는 5성분으로 표현할 수 있다.
VPSC의 응력–소성 변형률속도 관계는 이 5차원 표현을 활용할 수 있지만,
**일반적인 탄성 응력과 변형률을 표현할 때는 구형 성분을 포함한 6성분이 필요하다.**
코드의 <code>KDIM=5</code>와 <code>KDIM=6</code>은 이 차이에 대응한다.

예를 들어 정수압 응력 $\boldsymbol\sigma=-p\boldsymbol I$는

$$
[\boldsymbol\sigma]^{(b)}=
\begin{bmatrix}0&0&0&0&0&-\sqrt3p\end{bmatrix}^{T}
$$

이므로, 첫 다섯 성분만으로는 정수압을 나타낼 수 없다.

**Voigt 표기와 다른 점: 전단 배율과 내적 보존**

b-basis에서는 응력과 변형률의 전단 성분 모두에 $\sqrt2$를 곱한다.
예를 들어 $\sigma_{12}=\sigma_{21}=\tau$만 0이 아닌 순수 전단응력에서는
$\sigma_5^{(b)}=\sqrt2\tau$이다. $\tau=30\,\mathrm{MPa}$이면
$\sigma_5^{(b)}\approx42.43\,\mathrm{MPa}$이고 다른 성분은 모두 0이다.

정규직교성 때문에 대칭 텐서의 이중수축은 b-basis 벡터의 보통 내적과 같다.

$$
\boldsymbol A:\boldsymbol B
=\sum_{\alpha=1}^{6}A_\alpha^{(b)}B_\alpha^{(b)},
\qquad
\boldsymbol A:\boldsymbol A
=\sum_{\alpha=1}^{6}\left(A_\alpha^{(b)}\right)^2
$$

따라서 탄성에너지 밀도도

$$
W=\frac12\boldsymbol\sigma:\boldsymbol\varepsilon
=\frac12\sum_{\alpha=1}^{6}\sigma_\alpha^{(b)}\varepsilon_\alpha^{(b)}
$$

로 계산할 수 있다. 이 강의의 응력 Voigt 벡터와 공학전단변형률 Voigt 벡터 사이의
내적도 일률 밀도 또는 에너지 계산에 사용할 수 있지만, 각각의 Voigt 벡터의
유클리드 노름이 텐서의 노름과 같지는 않다. b-basis는 같은 정규직교 변환으로
내적과 노름을 모두 보존한다.

**b-basis에서의 탄성 stiffness와 compliance**

탄성계수 텐서를 $\mathbb C$라 쓰면, 기저 변환한 행렬 성분은

$$
C_{\alpha\beta}^{(b)}
=b_{ij}^{(\alpha)}C_{ijkl}b_{kl}^{(\beta)},
\qquad
[\boldsymbol\sigma]^{(b)}=[\mathbb C]^{(b)}[\boldsymbol\varepsilon]^{(b)}
$$

이다. $[\mathbb S]^{(b)}$도 같은 기저로 변환하며,
$[\mathbb S]^{(b)}=\left([\mathbb C]^{(b)}\right)^{-1}$이다.
**등방 선형탄성체**에서는 처음 5성분(대각합이 0인 변형)에 $2G$, 구형 변형에 $3K$가 대응하므로

$$
[\mathbb C]^{(b)}=\operatorname{diag}(2G,2G,2G,2G,2G,3K)
$$

$$
[\mathbb S]^{(b)}
=\operatorname{diag}\left(\frac1{2G},\frac1{2G},\frac1{2G},\frac1{2G},\frac1{2G},\frac1{3K}\right)
$$

가 된다. 앞의 Voigt stiffness에서 전단 대각성분이 $G$였던 것과 달리,
b-basis에서는 $2G$이다. 이는 물성이 달라진 것이 아니라 **변형률 성분의 정의가
공학전단변형률에서 정규직교 성분으로 바뀌었기 때문**이다.
이방성 탄성체에서는 b-basis를 사용해도 stiffness가 일반적으로 대각행렬은 아니다.

기저의 부호·순서는 구현에 따라 달라질 수 있으므로 실제 코드와 일치시켜야 한다.
위 정의는 [LANL VPSC8의 CHG_BASIS 원본](https://github.com/lanl/VPSC_code/blob/main/vpsc8sub.for#L182-L284)에 맞췄다.

# 11. 연습 문제

## 문제 1

Young 계수가 200 GPa인 재료에 0.001의 일축 탄성변형률이 생겼다. 응력을 구하라.

<!--
풀이와 해답:
sigma=E epsilon=200 GPa 곱하기 0.001=0.2 GPa=200 MPa이다.
-->

## 문제 2

일축 인장변형률이 0.01이고 Poisson 비가 0.3일 때 횡변형률을 구하라.

<!--
풀이와 해답:
횡변형률은 -nu epsilon=-0.3 곱하기 0.01=-0.003이다.
-->

## 문제 3

등방 선형탄성체를 나타내는 독립적인 탄성상수는 몇 개인가?

<!--
풀이와 해답:
두 개이다. 예를 들어 Young 계수 E와 Poisson 비 nu를 사용할 수 있다.
-->

## 문제 4: 탄성상수의 변환

등방 선형탄성체의 Young 계수가 $E=210\ \mathrm{GPa}$, Poisson 비가
$\nu=0.3$이다. 전단탄성계수 $G$와 Lamé의 제1 상수 $\lambda$를 구하라. 아래의 관계식을 활용할 수 있다.

$$
G=\frac{E}{2(1+\nu)}
$$

$$
\lambda=\frac{E \nu}{(1+\nu)(1-2\nu)}
$$

<!--
풀이와 해답:
G=E/[2(1+nu)]=210/2.6=80.77 GPa이다.
lambda=E nu/[(1+nu)(1-2nu)]=63/(1.3 곱하기 0.4)=121.15 GPa이다.
-->

## 문제 5: Voigt 표현과 응력 계산

등방 선형탄성체의 탄성상수가 $\lambda=120\ \mathrm{GPa}$,
$G=80\ \mathrm{GPa}$이고, 변형률 텐서가 다음과 같다.

$$
\boldsymbol\varepsilon=
\begin{bmatrix}
0.001 & 0.0002 & 0 \\
0.0002 & -0.0003 & 0 \\
0 & 0 & -0.0003
\end{bmatrix}
$$

이 강의의 성분 순서에 따라 ($[\sigma^{voigt}]=[\sigma_{11}, \sigma_{22}, \sigma_{33}, \sigma_{23}, \sigma_{13},\sigma_{12}]^T$) 변형률의 Voigt 벡터를 쓰고, 응력 텐서의 모든 독립 성분을 구하라.

<!--
풀이와 해답:
Voigt 성분 순서는 11, 22, 33, 23, 13, 12이다.
변형률 Voigt 벡터는 (0.001, -0.0003, -0.0003, 0, 0, 0.0004)^T이다.
tr(epsilon)=0.001-0.0003-0.0003=0.0004이다.
lambda tr(epsilon)=120 GPa 곱하기 0.0004=48 MPa이다.
sigma_11=48+160000 곱하기 0.001=208 MPa이다.
sigma_22=sigma_33=48+160000 곱하기 (-0.0003)=0 MPa이다.
sigma_12=160000 곱하기 0.0002=32 MPa이며 sigma_23=sigma_13=0이다.
응력 Voigt 벡터는 (208, 0, 0, 0, 0, 32)^T MPa이다.
-->

## 문제 6: 정수압과 체적변형률

[7.1절의 정수압과 체적탄성계수](#hydrostatic-pressure)를 참고하여 다음을 구하라.

$E=210\ \mathrm{GPa}$, $\nu=0.3$인 등방 선형탄성체에
$p=100\ \mathrm{MPa}$의 정수압이 작용한다. 인장응력을 양으로 정하면
$\sigma_{11}=\sigma_{22}=\sigma_{33}=-p=-100\ \mathrm{MPa}$이고 전단응력은 모두 0이다.
각 수직변형률과 미소 체적변형률 $\operatorname{tr}(\boldsymbol\varepsilon)$을 구하라.
또한 $K=\lambda+2G/3$를 이용하여 체적변형률을 검산하라.

<!--
풀이와 해답:
각 수직변형률은 (-p+2 nu p)/E=-(1-2nu)p/E이다.
epsilon_11=epsilon_22=epsilon_33=-0.4 곱하기 100/210000
=-0.000190476이다.
tr(epsilon)=3 곱하기 (-0.000190476)=-0.000571429이다.
G=80.7692 GPa, lambda=121.1538 GPa이므로 K=175 GPa이다.
-p/K=-100/175000=-0.000571429로 앞의 결과와 일치한다.
체적변형률이 음수이므로 체적이 감소한다.
-->
