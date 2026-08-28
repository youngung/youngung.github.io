---
layout: distill
title:
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

- [1. Kinematics in VPSC](#1-kinematics-in-vpsc)
  - [1.1. Velocity gradient](#11-velocity-gradient)
  - [1.2. Kinematics](#12-kinematics)
- [2. Deformation gradient](#2-deformation-gradient)
- [3. Polar decomposition](#3-polar-decomposition)
- [4. Velocity of points](#4-velocity-of-points)
- [5. Velocity gradient](#5-velocity-gradient)
- [\\end{bmatrix}](#endbmatrix)


# 1. Kinematics in VPSC

## 1.1. Velocity gradient

$$
\boldsymbol L = \dot{\boldsymbol\varepsilon}^{vp} + \dot{\boldsymbol\omega}
$$

  - $\boldsymbol L$: Velocity gradient tensor
  - $\dot{\boldsymbol \varepsilon}^{vp}$: visco-plastic strain rate tensor
  - $\dot{\boldsymbol\omega}$: Spin tensor

## 1.2. Kinematics

- 운동학; 점의 운동, 물체의 운동, 힘과 변형

- $\boldsymbol X$ : 초기 위치; Reference configuration

- $\boldsymbol x$ : 변화된 위치; current configuration

- $\boldsymbol{X}\rightarrow\boldsymbol{x}(t)$

# 2. Deformation gradient

- $\boldsymbol F=\frac{\partial \boldsymbol x}{\partial \boldsymbol X}$

- Change in infinitesimal line vector ($d\boldsymbol X$)

$$
d\boldsymbol x = \boldsymbol F \cdot d\boldsymbol X
$$

# 3. Polar decomposition

- $\boldsymbol F = \boldsymbol{R} \cdot \boldsymbol{U}=   \boldsymbol{V}\cdot\boldsymbol{R}$

# 4. Velocity of points

- $\boldsymbol v\equiv\boldsymbol v(\boldsymbol x,t)$

# 5. Velocity gradient

- Definition
$$
\boldsymbol L = \nabla \boldsymbol v
$$

$$
\boldsymbol L=
\begin{bmatrix}
\frac{\partial v_1}{\partial x_1} & \frac{\partial v_1}{\partial x_2} & \frac{\partial v_1}{\partial x_3} \\
\frac{\partial v_2}{\partial x_1} & \frac{\partial v_2}{\partial x_2} & \frac{\partial v_2}{\partial x_3} \\
\frac{\partial v_3}{\partial x_1} & \frac{\partial v_3}{\partial x_2} & \frac{\partial v_3}{\partial x_3}
\end{bmatrix}
$$


- Additively decomposition

$$
\boldsymbol L = \dot{\boldsymbol \varepsilon}+\dot{\boldsymbol\omega}
$$

$$
\boldsymbol{\dot\varepsilon} = \frac{1}{2}\big(\boldsymbol L+\boldsymbol L^T\big)
$$

$$
\boldsymbol{\dot\omega} = \frac{1}{2}\big(\boldsymbol L-\boldsymbol L^T\big)
$$

- Matrix form of boundary condition
$$
\begin{bmatrix}
L_{11}&L_{12}&L_{13}\\
L_{21}&L_{22}&L_{23}\\
L_{31}&L_{32}&L_{33}
\end{bmatrix}
$$
$$
\begin{bmatrix}
\sigma_{11}&\sigma_{12}&\sigma_{13}\\
\sigma_{21}&\sigma_{22}&\sigma_{23}\\
\sigma_{31}&\sigma_{32}&\sigma_{33}
\end{bmatrix}
$$


$$
\begin{bmatrix}
\dot{\varepsilon}_{11}\\
\dot{\varepsilon}_{22}\\
\dot{\varepsilon}_{33}\\
\dot{\varepsilon}_{23}\\
\dot{\varepsilon}_{13}\\
\dot{\varepsilon}_{12}
\end{bmatrix}
=
\begin{bmatrix}
C_{111} & C_{1122} & ... & C_{1112} \\
.\\
.\\
.\\
.\\
C_{1211} & C_{1222} & ... & C_{1212}
\end{bmatrix}
\begin{bmatrix}
\sigma_{11}\\
\sigma_{22}\\
\sigma_{33}\\
\sigma_{23}\\
\sigma_{13}\\
\sigma_{12}
\end{bmatrix}
$$