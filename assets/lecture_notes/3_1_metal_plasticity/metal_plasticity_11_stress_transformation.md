---
layout: distill
title: 좌표변환과 주응력의 기초
description: 항복 조건에 필요한 좌표변환, 주응력과 편차응력
target: 학부 3학년
permalink:
featured: true
prerequisite: 힘과 응력, 행렬과 텐서 연산
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

# 1. 같은 응력을 다른 방향에서 바라보기

한 물체를 수평 방향으로 당기더라도, 그 물체 안의 비스듬한 면에는 수직응력과 전단응력이 함께 작용할 수 있다.
이때 좌표축을 바꾸면 같은 응력 상태를 다른 성분으로 표현할 수 있다.
**좌표변환은 물체나 하중을 바꾸는 것이 아니라, 같은 물리량을 나타내는 기준 방향을 바꾸는 과정**이다.
이를 수동적 변환(passive transformation)이라 한다.

이 강의에서는 기존 기저 $$\lbrace\boldsymbol e_1,\boldsymbol e_2,\boldsymbol e_3\rbrace$$와
새 기저 $$\lbrace\tilde{\boldsymbol e}_1,\tilde{\boldsymbol e}_2,\tilde{\boldsymbol e}_3\rbrace$$가
모두 오른손 직교정규 기저라고 가정한다. 즉, 각 기저벡터의 길이는 1이고 서로 수직이다.
대괄호 $$[\,\cdot\,]_{\mathrm{old}}$$, $$[\,\cdot\,]_{\mathrm{new}}$$는 각각 기존 기저와 새 기저에서의 성분 배열을 나타낸다.

# 2. 좌표변환 행렬은 어떻게 만드는가?

## 2.1. 성분은 기저 방향으로의 투영이다

벡터 $$\boldsymbol v$$를 기존 기저로 쓰면

$$
\boldsymbol v=v_1\boldsymbol e_1+v_2\boldsymbol e_2+v_3\boldsymbol e_3
$$

이다. 새 기저의 첫 번째 성분은 같은 벡터를 $$\tilde{\boldsymbol e}_1$$ 방향으로 투영하여 구한다.

$$
\begin{aligned}
\tilde v_1
&=\tilde{\boldsymbol e}_1\cdot\boldsymbol v\\
&=(\tilde{\boldsymbol e}_1\cdot\boldsymbol e_1)v_1
 +(\tilde{\boldsymbol e}_1\cdot\boldsymbol e_2)v_2
 +(\tilde{\boldsymbol e}_1\cdot\boldsymbol e_3)v_3.
\end{aligned}
$$

따라서 **새 기저 방향과 기존 기저 방향 사이의 내적**을 모으면 좌표성분을 변환하는 행렬을 만들 수 있다.

$$
\boxed{R_{ij}=\tilde{\boldsymbol e}_i\cdot\boldsymbol e_j},
\qquad
[\boldsymbol R]=
\begin{bmatrix}
\tilde{\boldsymbol e}_1\cdot\boldsymbol e_1&\tilde{\boldsymbol e}_1\cdot\boldsymbol e_2&\tilde{\boldsymbol e}_1\cdot\boldsymbol e_3\\
\tilde{\boldsymbol e}_2\cdot\boldsymbol e_1&\tilde{\boldsymbol e}_2\cdot\boldsymbol e_2&\tilde{\boldsymbol e}_2\cdot\boldsymbol e_3\\
\tilde{\boldsymbol e}_3\cdot\boldsymbol e_1&\tilde{\boldsymbol e}_3\cdot\boldsymbol e_2&\tilde{\boldsymbol e}_3\cdot\boldsymbol e_3
\end{bmatrix}.
$$

단위벡터 사이의 내적은 두 방향 사이 각도의 코사인이므로 $$R_{ij}$$를 **방향코사인(direction cosine)**이라고도 한다.
행 첨자 $$i$$는 새 방향, 열 첨자 $$j$$는 기존 방향에 해당한다.
특히 **$$i$$번째 행은 새 기저벡터 $$\tilde{\boldsymbol e}_i$$를 기존 기저로 표현한 성분**이다.

세 성분의 투영식을 모으면

$$
\boxed{[\boldsymbol v]_{\mathrm{new}}=[\boldsymbol R][\boldsymbol v]_{\mathrm{old}}},
\qquad
\tilde v_i=\sum_{j=1}^3R_{ij}v_j
$$

를 얻는다. 행렬을 암기하기보다, 먼저 새 기저벡터를 기존 기저로 표현하고 그 성분을 행에 배치하면 된다.

## 2.2. 평면에서 좌표축을 반시계방향으로 회전시키기

기존 $$\boldsymbol e_1$$축에서 $$\boldsymbol e_2$$축으로 향하는 반시계방향을 양의 회전으로 정한다.
새 좌표축을 $$\theta$$만큼 회전시키면

$$
\begin{aligned}
\tilde{\boldsymbol e}_1&=\cos\theta\,\boldsymbol e_1+\sin\theta\,\boldsymbol e_2,\\
\tilde{\boldsymbol e}_2&=-\sin\theta\,\boldsymbol e_1+\cos\theta\,\boldsymbol e_2.
\end{aligned}
$$

예를 들어 $$\theta=90^\circ$$이면 새 첫 번째 축은 기존 두 번째 축 방향이고,
새 두 번째 축은 기존 첫 번째 축의 반대 방향이다. 따라서 두 번째 행의 첫 성분에는 음수가 붙는다.
위 두 벡터의 성분을 행으로 쓰면

$$
\boxed{[\boldsymbol R]=\begin{bmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{bmatrix}}.
$$

3차원에서 $$\boldsymbol e_3$$축을 그대로 두고 같은 회전을 하면

$$
[\boldsymbol R]=\begin{bmatrix}\cos\theta&\sin\theta&0\\-\sin\theta&\cos\theta&0\\0&0&1\end{bmatrix}
$$

이다. 물체 자체를 고정된 좌표계 안에서 반시계방향으로 회전시키는 **능동적 회전(active rotation)**은
여기서 다루는 좌표축의 회전과 다르다. 이 관례에서 같은 각도의 능동적 회전에는 $$[\boldsymbol R]^T$$가 사용된다.

## 2.3. 역변환과 벡터 계산 예제

$$\theta=90^\circ$$이고 기존 성분이 $$(3,4)^T$$라면

$$
[\boldsymbol v]_{\mathrm{new}}
=\begin{bmatrix}0&1\\-1&0\end{bmatrix}\begin{bmatrix}3\\4\end{bmatrix}
=\begin{bmatrix}4\\-3\end{bmatrix}.
$$

새 첫 번째 축 방향의 성분은 4, 새 두 번째 축 방향의 성분은 $$-3$$이다.
두 성분 배열은 다르지만, 벡터의 길이는 모두 $$\sqrt{3^2+4^2}=5$$다.

직교정규 기저로 만든 $$[\boldsymbol R]$$의 각 행은 길이가 1이고 서로 수직이므로

$$
[\boldsymbol R][\boldsymbol R]^T=[\boldsymbol I],
\qquad [\boldsymbol R]^{-1}=[\boldsymbol R]^T.
$$

따라서 새 성분에서 기존 성분으로 돌아가는 역변환은

$$
[\boldsymbol v]_{\mathrm{old}}=[\boldsymbol R]^T[\boldsymbol v]_{\mathrm{new}}
$$

이다. 두 기저가 모두 오른손 기저이면 $$\det[\boldsymbol R]=+1$$도 만족한다.

# 3. 응력텐서에는 왜 행렬을 두 번 곱하는가?

## 3.1. 면의 방향과 면력의 방향을 함께 변환하기

응력텐서는 면의 단위법선 $$\boldsymbol n$$을 그 면에 작용하는 면력 $$\boldsymbol t$$로 연결한다.
기존 기저에서 Cauchy 면력 공식은

$$
[\boldsymbol t]_{\mathrm{old}}=[\boldsymbol\sigma]_{\mathrm{old}}[\boldsymbol n]_{\mathrm{old}}
$$

이다. 면력과 법선은 모두 벡터이므로

$$
[\boldsymbol t]_{\mathrm{new}}=[\boldsymbol R][\boldsymbol t]_{\mathrm{old}},
\qquad
[\boldsymbol n]_{\mathrm{old}}=[\boldsymbol R]^T[\boldsymbol n]_{\mathrm{new}}
$$

를 대입하면

$$
\begin{aligned}
{}[\boldsymbol t]_{\mathrm{new}}
&=[\boldsymbol R][\boldsymbol\sigma]_{\mathrm{old}}[\boldsymbol R]^T[\boldsymbol n]_{\mathrm{new}}\\
&=[\boldsymbol\sigma]_{\mathrm{new}}[\boldsymbol n]_{\mathrm{new}}
\end{aligned}
$$

를 얻는다. 따라서

$$
\boxed{[\boldsymbol\sigma]_{\mathrm{new}}=[\boldsymbol R][\boldsymbol\sigma]_{\mathrm{old}}[\boldsymbol R]^T},
\qquad
\tilde\sigma_{ij}=\sum_{k=1}^3\sum_{l=1}^3R_{ik}R_{jl}\sigma_{kl}.
$$

응력은 면력의 성분 방향과 면의 법선 방향이라는 **두 방향**을 연결하므로, 두 첨자에 각각 좌표변환이 필요하다.
왼쪽의 $$[\boldsymbol R]$$은 면력 성분을 새 기저로 바꾸고,
오른쪽의 $$[\boldsymbol R]^T$$는 새 기저의 법선 성분을 기존 기저의 성분으로 바꾸는 역할을 한다.

## 3.2. 평면 응력성분의 변환식

평면 내 기존 응력과 변환 행렬을

$$
[\boldsymbol\sigma]_{\mathrm{old}}=\begin{bmatrix}\sigma_{11}&\sigma_{12}\\\sigma_{12}&\sigma_{22}\end{bmatrix},
\qquad c=\cos\theta,\quad s=\sin\theta
$$

로 쓰자. 먼저 왼쪽 행렬곱을 계산하면

$$
[\boldsymbol R][\boldsymbol\sigma]_{\mathrm{old}}
=\begin{bmatrix}
c\sigma_{11}+s\sigma_{12}&c\sigma_{12}+s\sigma_{22}\\
-s\sigma_{11}+c\sigma_{12}&-s\sigma_{12}+c\sigma_{22}
\end{bmatrix}.
$$

여기에 전치행렬

$$
[\boldsymbol R]^T=\begin{bmatrix}c&-s\\s&c\end{bmatrix}
$$

를 오른쪽에서 곱하면

$$
\begin{aligned}
\tilde\sigma_{11}&=c^2\sigma_{11}+2cs\sigma_{12}+s^2\sigma_{22},\\
\tilde\sigma_{22}&=s^2\sigma_{11}-2cs\sigma_{12}+c^2\sigma_{22},\\
\tilde\sigma_{12}&=cs(\sigma_{22}-\sigma_{11})+(c^2-s^2)\sigma_{12}.
\end{aligned}
$$

$$\tilde\sigma_{11}$$은 새 첫 번째 축에 수직인 면의 수직응력이며,
$$\tilde\sigma_{12}=\tilde\sigma_{21}$$은 새 좌표축에서의 전단응력 성분이다.
새 첫 번째 축에 수직인 면의 면력 성분은 $$(\tilde\sigma_{11},\tilde\sigma_{21})^T$$이다.

## 3.3. 45° 회전의 수치 예제와 검산

기존 평면 응력이

$$
[\boldsymbol\sigma]_{\mathrm{old}}=\begin{bmatrix}80&20\\20&50\end{bmatrix}\,\mathrm{MPa}
$$

이고 새 좌표축을 반시계방향으로 $$45^\circ$$ 회전시키면 $$c=s=1/\sqrt2$$이므로

$$
\begin{aligned}
\tilde\sigma_{11}&=\tfrac12(80)+20+\tfrac12(50)=85\,\mathrm{MPa},\\
\tilde\sigma_{22}&=\tfrac12(80)-20+\tfrac12(50)=45\,\mathrm{MPa},\\
\tilde\sigma_{12}&=\tfrac12(50-80)+0(20)=-15\,\mathrm{MPa}.
\end{aligned}
$$

따라서

$$
[\boldsymbol\sigma]_{\mathrm{new}}=\begin{bmatrix}85&-15\\-15&45\end{bmatrix}\,\mathrm{MPa}.
$$

전단응력의 부호와 수직응력 성분은 바뀌었지만, 같은 물리적 응력 상태다.
검산을 위해 두 평면 내 성분행렬의 대각합과 행렬식을 비교하면

$$
80+50=85+45=130\,\mathrm{MPa},
$$

$$
80(50)-20^2=85(45)-(-15)^2=3600\,\mathrm{MPa}^2
$$

으로 같다. 좌표변환 전후에는 응력텐서의 대각합, 행렬식, 고유값이 보존된다.
위 행렬식은 $$2\times2$$ 평면 내 부분행렬의 값이며, 면외 성분까지 포함한 $$3\times3$$ 평면응력 행렬의 행렬식은 0이다.

# 4. 주응력과 최대 전단응력

전단응력 성분이 0이 되는 좌표축을 **주축 (principal axes)**이라 한다.
이 축에 대한 수직응력이 **주응력 (principal stresses)**이며, 응력텐서의 고유값이다.
평면의 두 주응력은

$$
\sigma_{\pm}=\frac{\sigma_{11}+\sigma_{22}}{2}
\pm\sqrt{\left(\frac{\sigma_{11}-\sigma_{22}}{2}\right)^2+\sigma_{12}^2}
$$

로 구한다. 평면응력에서는 면외 주응력 0도 포함해 세 주응력을 크기순으로 정리한다.
3차원 최대 전단응력은 $$\tau_{\max}=(\sigma_{\max}-\sigma_{\min})/2$$다.

예를 들어

$$
[\boldsymbol\sigma]=\begin{bmatrix}80&20&0\\20&50&0\\0&0&0\end{bmatrix}\,\mathrm{MPa}
$$

이면 평면 내 주응력은 $$65\pm25$$, 즉 $$90$$과 $$40\,\mathrm{MPa}$$다.
세 주응력은 $$(90,40,0)\,\mathrm{MPa}$$이므로 최대 전단응력은 $$45\,\mathrm{MPa}$$다.
평면 내 최대 전단응력 $$25\,\mathrm{MPa}$$와 구분해야 한다.

위 예제에서 주축의 방향도 좌표변환 행렬로 구할 수 있다. $$\tilde\sigma_{12}=0$$인 조건을 쓰면

$$
0=-\frac{\sigma_{11}-\sigma_{22}}{2}\sin2\theta_p+\sigma_{12}\cos2\theta_p,
\qquad
\tan2\theta_p=\frac{2\sigma_{12}}{\sigma_{11}-\sigma_{22}}=\frac{40}{30}.
$$

이 예제에서는 $$\theta_p\simeq26.565^\circ$$를 선택하면
$$\cos\theta_p=2/\sqrt5$$, $$\sin\theta_p=1/\sqrt5$$다. 따라서

$$
[\boldsymbol R_p]=\frac1{\sqrt5}\begin{bmatrix}2&1\\-1&2\end{bmatrix},
\qquad
[\boldsymbol R_p]\begin{bmatrix}80&20\\20&50\end{bmatrix}[\boldsymbol R_p]^T
=\begin{bmatrix}90&0\\0&40\end{bmatrix}.
$$

이 좌표계에서는 전단응력이 0이고, 대각성분이 주응력이 된다.

일반적으로 주축 방향은 $$90^\circ$$ 차이로 두 개 존재한다. 탄젠트 식만으로는 어느 축이 최대 주응력 방향인지 정해지지 않으므로,
구한 각도를 변환식에 대입해 확인한다. 평면 내 응력이 $$\sigma_{11}=\sigma_{22}$$, $$\sigma_{12}=0$$이면 모든 평면 내 방향이 주축이다.

# 5. 평균응력과 편차응력

응력은 평균응력과 나머지 부분으로 나눈다.

$$
\sigma_m=\frac{\sigma_{11}+\sigma_{22}+\sigma_{33}}{3},
\qquad \boldsymbol s=\boldsymbol\sigma-\sigma_m\boldsymbol I.
$$

$$\boldsymbol I$$는 단위텐서이고, $$\boldsymbol s$$는 **편차응력 (deviatoric stress)**이다.
다음 항복 조건 자료에서는 주응력으로 Tresca 조건을, 편차응력으로 von Mises 조건을 이해한다.

# 6. 연습 문제

## 문제 1: 평균응력과 최대 전단응력

주응력이 $$(120,60,0)\,\mathrm{MPa}$$일 때 평균응력과 3차원 최대 전단응력을 구하시오.

<!--
풀이와 해답:
평균응력=(120+60+0)/3=60 MPa.
최대 전단응력=(120-0)/2=60 MPa.
-->

## 문제 2: 기저벡터로 행렬 만들기

새 기저가 $$\tilde{\boldsymbol e}_1=(\boldsymbol e_1+\boldsymbol e_2)/\sqrt2$$,
$$\tilde{\boldsymbol e}_2=(-\boldsymbol e_1+\boldsymbol e_2)/\sqrt2$$일 때 좌표변환 행렬을 구하라.
기존 성분이 $$(10,0)^T$$인 벡터의 새 성분과 크기를 구하라.

<!--
풀이와 해답:
R=(1/sqrt(2))[[1,1],[-1,1]]이다.
새 성분은 (5 sqrt(2), -5 sqrt(2))^T이고 크기는 10으로 보존된다.
-->

## 문제 3: 일축 인장 상태의 좌표변환

평면응력 상태에서 $$\sigma_{11}=100\,\mathrm{MPa}$$이고 나머지 성분은 모두 0이다.
새 좌표축을 반시계방향으로 $$45^\circ$$ 회전시켰을 때 평면 내 응력성분을 구하라.
수직응력과 전단응력이 함께 나타나는 이유를 면의 방향과 연결하여 설명하라.

<!--
풀이와 해답:
새 평면 내 응력행렬은 [[50,-50],[-50,50]] MPa이다.
비스듬한 면의 면력은 새 법선 방향과 접선 방향 성분을 모두 갖기 때문이다.
하중이나 물리적 응력 상태가 바뀐 것은 아니다. 주응력은 여전히 (100,0,0) MPa이다.
-->

## 문제 4: 올바른 좌표변환 행렬 고르기

다음 두 행렬 중 이 강의의 반시계방향 $$30^\circ$$ **좌표축 회전**에 해당하는 행렬을 고르고,
새 첫 번째 기저벡터의 방향을 근거로 설명하라. 다른 행렬이 나타내는 좌표축 회전 각도도 구하라.

$$
[\boldsymbol A]=\begin{bmatrix}\sqrt3/2&1/2\\-1/2&\sqrt3/2\end{bmatrix},
\qquad
[\boldsymbol B]=\begin{bmatrix}\sqrt3/2&-1/2\\1/2&\sqrt3/2\end{bmatrix}.
$$

<!--
풀이와 해답:
A이다. 첫 행의 성분에 따라 새 첫 번째 기저벡터는 (sqrt(3)/2)e_1+(1/2)e_2이며,
기존 첫 번째 축에서 반시계방향으로 30도 기울어져 있다.
B는 시계방향 30도, 즉 theta=-30도의 좌표축 회전에 해당하며 B=A^T=A^{-1}이다.
-->

## 문제 5: 직교성 확인과 역변환

좌표변환 행렬과 새 기저에서의 벡터 성분이 다음과 같다.

$$
[\boldsymbol R]=\frac15\begin{bmatrix}3&4\\-4&3\end{bmatrix},
\qquad
[\boldsymbol v]_{\mathrm{new}}=\begin{bmatrix}5\\0\end{bmatrix}.
$$

1. 각 행벡터의 길이와 두 행벡터의 내적을 구하여 직교성을 확인하라.
2. 전치행렬을 이용하여 기존 기저에서의 성분을 구하라.
3. 변환 전후 벡터의 크기를 비교하라.

<!--
풀이와 해답:
두 행의 길이 제곱은 각각 (9+16)/25=1, (16+9)/25=1이다.
두 행의 내적은 (-12+12)/25=0이므로 RR^T=I이다.
기존 성분은 R^T(5,0)^T=(3,4)^T이다. 크기는 두 기저 모두 5이다.
-->

## 문제 6: 90° 응력 변환과 역변환

기존 평면 내 응력성분이 다음과 같다.

$$
[\boldsymbol\sigma]_{\mathrm{old}}
=\begin{bmatrix}60&15\\15&20\end{bmatrix}\,\mathrm{MPa}.
$$

1. 새 좌표축을 반시계방향으로 $$90^\circ$$ 회전시켰을 때 응력성분을 구하라.
2. 두 평면 내 성분행렬의 대각합과 행렬식을 비교하라.
3. $$[\boldsymbol R]^T[\boldsymbol\sigma]_{\mathrm{new}}[\boldsymbol R]$$을 계산하여 기존 성분으로 돌아오는지 확인하라.

<!--
풀이와 해답:
R=[[0,1],[-1,0]]이다.
R sigma_old=[[15,20],[-60,-15]] MPa이고,
sigma_new=[[20,-15],[-15,60]] MPa이다.
대각합은 두 행렬 모두 80 MPa이며, 행렬식은 60(20)-15^2=975 MPa^2이다.
R^T sigma_new=[[15,-60],[20,-15]] MPa이고,
여기에 R을 오른쪽에서 곱하면 [[60,15],[15,20]] MPa를 얻는다.
-->

## 문제 7: 순수전단 상태의 주축

평면응력 상태가 다음과 같이 주어져 있다.

$$
[\boldsymbol\sigma]_{\mathrm{old}}
=\begin{bmatrix}0&30&0\\30&0&0\\0&0&0\end{bmatrix}\,\mathrm{MPa}.
$$

1. 면외 축은 고정하고 평면 내 좌표축을 반시계방향으로 $$45^\circ$$ 회전시켰을 때 $$3\times3$$ 응력행렬을 구하라.
2. 세 주응력을 큰 순서로 정리하고 3차원 최대 전단응력을 구하라.
3. 전단응력 성분이 모두 0이 된 좌표계에서도 최대 전단응력이 0이 아닌 이유를 설명하라.

<!--
풀이와 해답:
새 응력행렬은 diag(30,-30,0) MPa이다.
크기순 주응력은 (30,0,-30) MPa이고 최대 전단응력은 (30-(-30))/2=30 MPa이다.
새 좌표축에 수직인 면에서 전단응력이 0이라는 뜻이지 모든 방향의 면에서 0이라는 뜻은 아니다.
최대 전단응력은 가능한 모든 면의 방향에 대해 정해지는 값이며 좌표변환으로 바뀌지 않는다.
-->

## 문제 8: 평면 내 최대 전단응력과 3차원 최대 전단응력

평면응력 상태에서 두 평면 내 주응력이 $$100\,\mathrm{MPa}$$와 $$40\,\mathrm{MPa}$$이다.

1. 세 주응력을 큰 순서로 정리하라.
2. 평면 내 최대 전단응력과 3차원 최대 전단응력을 각각 구하라.
3. 두 값이 다른 이유를 면외 주응력과 연결하여 설명하라.

<!--
풀이와 해답:
평면응력이므로 면외 주응력은 0이고, 세 주응력은 (100,40,0) MPa이다.
평면 내 최대 전단응력은 (100-40)/2=30 MPa이다.
3차원 최대 전단응력은 (100-0)/2=50 MPa이다.
3차원에서는 면외 방향을 포함한 면도 고려하므로 최대와 최소 주응력의 쌍이 달라진다.
-->

## 문제 9: 평균응력과 편차응력의 검산

평면응력 상태가 다음과 같다.

$$
[\boldsymbol\sigma]
=\begin{bmatrix}90&0&0\\0&30&0\\0&0&0\end{bmatrix}\,\mathrm{MPa}.
$$

1. 평균응력과 편차응력 행렬을 구하고 편차응력의 대각합이 0인지 확인하라.
2. 평면 내 좌표축을 반시계방향으로 $$45^\circ$$ 회전시킨 응력행렬을 구하라.
3. 변환된 응력행렬에서 다시 평균응력과 편차응력을 구하라.
4. 평면응력 상태에서도 편차응력의 면외 성분이 0이 아닐 수 있는 이유를 설명하라.

<!--
풀이와 해답:
평균응력은 (90+30+0)/3=40 MPa이다.
편차응력은 diag(50,-10,-40) MPa이며 대각합은 0이다.
변환된 응력행렬은 [[60,-30,0],[-30,60,0],[0,0,0]] MPa이다.
평균응력은 여전히 40 MPa이고 편차응력은 [[20,-30,0],[-30,20,0],[0,0,-40]] MPa이다.
평면응력은 전체 응력의 sigma_33=0이라는 조건이다.
s_33=sigma_33-sigma_m=-40 MPa이므로 편차응력까지 면외 성분이 0일 필요는 없다.
-->

## 문제 10: 면력으로 응력 변환 검산하기

기존 평면 내 응력성분은 다음과 같다.

$$
[\boldsymbol\sigma]_{\mathrm{old}}
=\begin{bmatrix}80&20\\20&50\end{bmatrix}\,\mathrm{MPa}.
$$

새 기저벡터를
$$\tilde{\boldsymbol e}_1=(2\boldsymbol e_1+\boldsymbol e_2)/\sqrt5$$,
$$\tilde{\boldsymbol e}_2=(-\boldsymbol e_1+2\boldsymbol e_2)/\sqrt5$$로 정한다.
새 첫 번째 축에 수직인 면을 생각하자.

1. 이 면의 단위법선을 두 기저에서 각각 나타내라.
2. 기존 기저에서 $$[\boldsymbol t]_{\mathrm{old}}=[\boldsymbol\sigma]_{\mathrm{old}}[\boldsymbol n]_{\mathrm{old}}$$를 계산하라.
3. 면력의 성분을 새 기저로 변환하고, 이 면에 작용하는 수직응력과 전단응력을 구하라.
4. 본문의 주응력 계산 결과와 비교하라.

<!--
풀이와 해답:
법선의 기존 성분은 (2,1)^T/sqrt(5), 새 성분은 (1,0)^T이다.
면력의 기존 성분은 (180,90)^T/sqrt(5) MPa이다.
R=(1/sqrt(5))[[2,1],[-1,2]]이므로 면력의 새 성분은 (90,0)^T MPa이다.
이 면의 수직응력은 90 MPa, 전단응력은 0이다.
새 첫 번째 축이 최대 주응력 90 MPa에 해당하는 주축이므로 본문의 결과와 일치한다.
-->

다음 자료: [소성 항복]({% link assets/lecture_notes/3_1_metal_plasticity/metal_plasticity_12_plastic_yield.md %})

[이전 강의]({% link assets/lecture_notes/3_1_metal_plasticity/metal_plasticity_10_plane_condition.md %}) | [강의 목록]({% link _lectures/3_1_metal_plasticity.md %}) | [다음 강의]({% link assets/lecture_notes/3_1_metal_plasticity/metal_plasticity_12_plastic_yield.md %})
