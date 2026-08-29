---
layout: distill
title:
description:
target:
permalink:
featured: true
prerequisite:

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

- [1. 좌표 변환 행렬 복습](#1-좌표-변환-행렬-복습)
- [2. 평면 응력상태의 좌표 변환](#2-평면-응력상태의-좌표-변환)
- [3. 삼각함수 정리](#3-삼각함수-정리)
- [4. Mohr Circle, 원의 방정식](#4-mohr-circle-원의-방정식)


# 1. 좌표 변환 행렬 복습

- ($\boldsymbol e_1,\boldsymbol e_2,\boldsymbol e_3$)로 이루어진 좌표계로부터
  ($\tilde{\boldsymbol e}_1,\tilde{\boldsymbol e}_2,\tilde{\boldsymbol e}_3$)
  좌표계로 변환하는 좌표변환 매트릭스(coordinate transformation matrix)는
  아래와 같이 정의된다.

$$
R_{ij}=\tilde{\boldsymbol e}_i \cdot \boldsymbol e_j \text{  with  } i=1,2,3,\ \ \ j=1,2,3
$$

- 두 좌표계의 축들 사이의 내적을 사이에 끼인 각을 활용해 나타낼 수 있다.
  즉,
  $$\tilde{\boldsymbol e}_i$$
  와
  $$\boldsymbol{e}_j$$
  사이의 끼인각을
  $\theta_{ij}$ 라 하면, 아래와 같은 관계식을 얻을 수 있다.

$$
\cos\theta_{ij} |\tilde{\boldsymbol e}_i| |\boldsymbol e_j|=\tilde{\boldsymbol e}_i \cdot \boldsymbol e_j  \text{  with  } i=1,2,3,\ \ \ j=1,2,3
$$

- 그런데, 좌표축의 크기가 모두 1인 unit vector로 이루어진 직각 좌표계라 한정 지으면 위 식은
아래가 되며

$$
\cos\theta_{ij} =\tilde{\boldsymbol e}_i \cdot \boldsymbol e_j  \text{  with  } i=1,2,3,\ \ \ j=1,2,3
$$

따라서, 좌표 변환 매트릭스는 $\cos \theta_{ij}$로 이루어져 있음을 알 수 있다.

$$
\boldsymbol{R} = \begin{bmatrix}
\cos\theta_{11}&\cos\theta_{12}&\cos\theta_{13}\\
\cos\theta_{21}&\cos\theta_{22}&\cos\theta_{23}\\
\cos\theta_{31}&\cos\theta_{32}&\cos\theta_{33}\\
\end{bmatrix}
$$



# 2. 평면 응력상태의 좌표 변환

- $\boldsymbol e_3$ 축으로 방향이 매우 얇은 판재를 가정하고 따라서 plane stress 상태라면,
  응력상태는 아래 $2\times2$ 행렬로 표현할 수 있다.

$$
\boldsymbol\sigma=
\begin{bmatrix}
\sigma_{11} &\sigma_{12}\\
\sigma_{12} &\sigma_{22}\\
\end{bmatrix}
$$

- 좌표 변환 매트릭스의 경우, $\boldsymbol e_3=\tilde{\boldsymbol e}_3$으로 고정된 경우,

$$
\boldsymbol{R} = \begin{bmatrix}
\cos\theta_{11}&\cos\theta_{12}&0\\
\cos\theta_{21}&\cos\theta_{22}&0\\
0&0&1\\
\end{bmatrix}
$$

이 되고, 이는 응력과 마찬가지로 $2\times2$행렬로 축약하여

$$
\boldsymbol{R} = \begin{bmatrix}
\cos\theta_{11}&\cos\theta_{12}\\
\cos\theta_{21}&\cos\theta_{22}\\
\end{bmatrix}
$$

가 된다. 그런데 먄약 $\theta_{11}$를 기준이되는 회전된 각도 $\theta$라 하면

$$
\boldsymbol{R} = \begin{bmatrix}
\cos\theta&\cos{(90^\circ-\theta)}\\
\cos(90^\circ+\theta)&\cos\theta\\
\end{bmatrix}

= \begin{bmatrix}
\cos\theta&\sin{\theta}\\
-\sin\theta&\cos\theta\\
\end{bmatrix}
$$

- 자 이제, 랭크 2 텐서의 좌표 변환법칙을 적용해보자.

$$
\tilde{\sigma}_{ij} = \sum_k^2\sum_l^2 R_{ik} R_{jl} \sigma_{kl}, \text{ with } i=1,2\ \ \ j=1,2
$$


- $\tilde{\sigma}_{11}$:
$$
\tilde{\sigma}_{11} = \sum_k^2\sum_l^2 R_{1k} R_{1l} \sigma_{kl}
$$

$$
=R_{11} R_{11} \sigma_{11}+R_{11} R_{12} \sigma_{12}
$$

$$
+R_{12} R_{11} \sigma_{21}+R_{12} R_{12} \sigma_{22}
$$

$$
=\cos\theta \cos\theta\sigma_{11}+\cos\theta\sin\theta\sigma_{12}
$$

$$
+\sin\theta\cos\theta\sigma_{12}+\sin\theta\sin\theta\sigma_{22}
$$

$$
\therefore
\tilde{\sigma}_{11}=\cos^2\theta \sigma_{11}
+\sin^2\theta\sigma_{22}
+2\cos\theta\sin\theta\sigma_{12}
$$


- $\tilde{\sigma}_{22}$:

$$
\tilde{\sigma}_{22} = \sum_k^2\sum_l^2 R_{2k} R_{2l} \sigma_{kl}
$$

$$
=R_{21} R_{21} \sigma_{11}+R_{21} R_{22} \sigma_{12}
$$

$$
+R_{22} R_{21} \sigma_{21}+R_{22} R_{22} \sigma_{22}
$$

$$
=\sin^2\theta\sigma_{11}-\sin\theta\cos\theta\sigma_{12}
$$

$$
-\cos\theta\sin\theta\sigma_{12}+\cos^2\theta\sigma_{22}
$$

$$
\therefore
\tilde{\sigma}_{22}=
\sin^2\theta\sigma_{11}+\cos^2\theta\sigma_{22}-2\sin\theta\cos\theta\sigma_{12}
$$


- $\tilde{\sigma}_{12}$:

$$
\tilde{\sigma}_{12} = \sum_k^2\sum_l^2 R_{1k} R_{2l} \sigma_{kl}
$$

$$
=R_{11} R_{21} \sigma_{11}+R_{11} R_{22} \sigma_{12}
$$

$$
+R_{12} R_{21} \sigma_{21}+R_{12} R_{22} \sigma_{22}
$$

$$
=-\cos\theta\sin\theta\sigma_{11}+\cos^2\theta\sigma_{12}
-\sin^2\theta\sigma_{12}+\sin\theta\cos\theta\sigma_{22}
$$

$$
=(\sigma_{22}-\sigma_{11})\cos\theta\sin\theta+\sigma_{12}(\cos^2\theta-\sin^2\theta)
$$

$$
\therefore
\tilde{\sigma}_{12}=(\sigma_{22}-\sigma_{11})\cos\theta\sin\theta+\sigma_{12}(\cos^2\theta-\sin^2\theta)
$$

# 3. 삼각함수 정리
- 아래 삼각함수 항등식을 활용하자.
  - $\cos^2\theta=\frac{1+\cos 2\theta}{2}$
  - $\sin^2\theta=\frac{1-\cos 2\theta}{2}$
  - $2\sin\theta\cos\theta=\sin 2\theta$
  - $\cos^2\theta-\sin^2\theta=\cos 2\theta$

- 위 항등식을 활용하면

$$
\tilde{\sigma}_{11}=\cos^2\theta \sigma_{11}
+\sin^2\theta\sigma_{22}
+2\cos\theta\sin\theta\sigma_{12}
$$

$$
=\frac{1+\cos 2\theta}{2}\sigma_{11}
+\frac{1-\cos 2\theta}{2}\sigma_{22}+\sin 2\theta\sigma_{12}
$$

$$
=\frac{\sigma_{11}+\sigma_{22}}{2}
+\frac{\sigma_{11}-\sigma_{22}}{2} \cos 2\theta
+\sigma_{12}\sin 2\theta
$$

$$
\tilde{\sigma}_{12}=(\sigma_{22}-\sigma_{11})\cos\theta\sin\theta+\sigma_{12}(\cos^2\theta-\sin^2\theta)
$$

$$
=-\frac{\sigma_{11}-\sigma_{22}}{2}\sin 2\theta+\sigma_{12}\cos 2\theta
$$

# 4. Mohr Circle, 원의 방정식

- 원의 중심
$$
C=\frac{\sigma_{11}+\sigma_{22}}{2}
$$

- 반지름
$$
R=\sqrt{\bigg(\frac{\sigma_{11}-\sigma_{22}}{2}\bigg)^2+\sigma_{12}}
$$

- 원의 방정식

$$
(\sigma-C)^2-\sigma_{12}^2=R^2
$$