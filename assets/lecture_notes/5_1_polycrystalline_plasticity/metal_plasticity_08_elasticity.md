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

- 변형률이 단위가 없으므로, 영률은 응력과 같은 단위를 가진다 ($Pa, MPa$ 등)

- 영률은 재료의 성질이다. 강철과 고무에 동일한 응력을 가했을 때, 강철의 변형률이 훨씬 작다. 따라서 강철의 영률이 고무의 영률에 비해 매우 크다.

# 3. 포아송 효과 (Poisson effect)

- 인장하는 길이가 $\mathbf e_1$ 방향일 때, 수직 변형이 $\mathbf e_1$축으로만 발생하지 않는다. 그에 수직한 방향, 예를 들어 $\mathbf e_2$로는 길이가 줄어드는 수직 변형이 발생할 수 있다.

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

- $\delta_{ij}$는 크로네커 델타로 불리며 아래 성질을 가진다.

  - $\delta_{ij}=0, \text{ if } i\ne j$
  - $\delta_{ij}=1, \text{ if } i=j$
  - 따라서 $\delta_{ij}$는 $\boldsymbol I$와 동일한 역할을 수행한다.

- G는 전단 탄성계수이다.

- $\lambda$는 Lame의 제1 상수이다.

# 6. 선형 등방 Hooke 법칙 상세 설명

- 체적변형과 형상변형의 역할을 정확히 나누려면 변형률을 평균성분과 편차성분으로
  분해하는 것이 좋다. 체적탄성계수를 $K=\lambda+2G/3$라 하면

$$
[\boldsymbol\sigma]
=K \boldsymbol I\operatorname{tr}(\boldsymbol\varepsilon)
+2G[\boldsymbol\varepsilon]
$$

이다. 첫 항은 체적변화에, 두 번째 항은 형상변화에 대응한다. 원래 식의
$2G\boldsymbol\varepsilon$에는 체적성분도 포함되므로 그 항 전체를 형상변화 성분이라고
부르면 정확하지 않다.

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

- 등방성을 고려하지 않은 Hooke 법칙에서 랭크 4의 탄성계수 텐서$E_{ijkl}$가 81개의 성분을 가질 수 있는 것으로 보인다 (3x3x3x3=81).
- 하지만 등방성을 고려한 Hooke의 법칙에서는 단 2개의 스칼라 값을 활용했다 ($\lambda, G$)
- 실제로는 $\lambda$와 $G$의 쌍보다 영률 $E$와 Poisson 비 $\nu$를 활용하는 경우가
  많으며, 두 상수 집합은 서로 변환할 수 있다.

$$G=\frac{E}{2(1+\nu)}$$

$$\lambda = \frac{E\nu}{(1+\nu)(1-2\nu)}$$

등방 선형탄성체의 에너지가 안정하려면 일반적으로 $E>0$이고
$-1<\nu<0.5$여야 한다. 금속의 Poisson 비는 흔히 약 0.3이며, $\nu$가 0.5에
가까울수록 탄성 체적변화에 더 강하게 저항한다.

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


# 10. 연습 문제

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
