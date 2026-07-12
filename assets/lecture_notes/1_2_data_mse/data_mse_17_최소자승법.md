---
layout: distill
title: 데이터 재료과학 (제 17강)
description: IO
target: 1학년 2학기
permalink:
featured: true
prerequisite: 재료공학개론1
toc:
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

- [1. 목표](#1-목표)
- [2. 개념](#2-개념)


# 1. 목표

  - 최소 자승법을 이해한다.
  - 09-1의 데이터의 활용헤서 '최소자승법'을 활용해본다.

#  2. 개념

 주어진 $n$ 쌍의의 데이터가 아래와 같이 표현될 수 있다.

  $$
  (x_i,y_i) \text{ with } i=1,2,...,n
  $$

  이때 위 $n$쌍의 데이터를 우리가 구하는 직선의 방정식이 매우 잘 대표해야 하겠다.

  $$
  y=ax+b
  $$

  그러한 직선의 방정식을 구하기 위해서는 데이터와 계산된 값 사이의 차이를 최소화시켜야겠다.

  - 예시.

    - 실제로는 2.5x + 5가 데이터인데, 가상의 노이즈를 부과해보자.

      ```python
      import numpy as np
      import matplotlib.pyplot as plt

      # example data with noise
      xs = np.linspace(0, 10, 20)
      # 실제로는 2.5x + 5가 데이터인데, 가상의 노이즈를 부과해보자.
      a=2.5
      b=5
      y_true = a * xs + b
      ## 정규 분포를 따르는 인위적 노이즈를 부과해보자.
      noise = np.random.normal(0, 3, size=xs.shape) ## 정규분포 mean:0, std: 3
      ys = y_true + noise
      ```

    - 그 다음, 정확한 $a, b$ 값을 모른다 가정하고, 각 추측된 값
      $\tilde a,\tilde b$ 값을 사용해보자. 그리고 추측된 값과, 노이즈가 있는 값
      들 사이에 차이를 아래와 같이 정의하여 살펴보자.

      $$
      \epsilon_i=y_i-(\tilde a x_i+\tilde b)
      $$

    - 각 쌍

      $$
      (x_i,y_i)
      $$

      에 따라 음의 차이 혹은 양의 차이가 있을 수 있으므로, 자승(square)값을 구하고
      그 자승 값의 총 합을 살펴보자. 즉

      $$
      \sum_i^n(\epsilon_i)^2
      $$

      값을 찾아 보자.

    - 여기까지의 과정은 아래와 같이 Python으로 구현될 수 있다.

      ```python
      plt.plot(xs,ys,'rx',label='Data with noise')
      #plt.plot(xs,y_true,'k-',label='True data')

      tilde_a=2.2
      tilde_b=5
      plt.plot(xs,tilde_a*xs+tilde_b,'m--',label='Guessed fit')
      epsilon=np.zeros(xs.shape)
      for i, x in enumerate(xs):
      	y=x*tilde_a+tilde_b
      	epsilon[i]=y-ys[i]
      	plt.plot([x,x],[ys[i],y],'-b')
      print(f'residual: {(epsilon**2).sum()}')
      leg=plt.legend()
      ```

    - 이제 자승값의 합을 최소화 시키는 $\tilde a, \tilde b$ 값을 어떻게
      구할 수 있을지 고민해보자.

    - 가장 적절한 $\tilde a, \tilde b$ 값을 구하기 위해 우선

      $$
      S=\sum_i^n(\epsilon_i)^2
      $$

      라 하고, 이를 풀어서 표현하면

      $$
      S=\sum_i^n(\epsilon_i)^2=\sum_i^n(y_i-(\tilde ax_i+\tilde b))^2
      $$

      가 된다. 위 표현은 위 코드 박스에서

      ```python
      (epsilon**2).sum()
      ```

      에 해당한다.

      제곱 항을 전개하면

      $$
      S=\sum_i^n(y_i-(\tilde ax_i+\tilde b))^2
      =\sum_i^n\bigg(y_i^2+(\tilde ax_i-2y_i(\tilde ax_i+\tilde b)+\tilde b)^2\bigg)
      $$

      가 된다. 이때

      $$
      \frac{\partial S}{\partial \tilde a}=0
      $$

      그리고

      $$
      \frac{\partial S}{\partial \tilde b}=0
      $$

      를 만족하는 $\tilde a, \tilde b$ 값이 최소자승법에 의해 구해진다.
      따라서 각 미분 값을 구해보면

      $$
      \frac{\partial S}{\partial \tilde a}
      =\sum_i^n\frac{\partial \bigg((y_i-(\tilde ax_i+\tilde b))^2\bigg) }{\partial \tilde a}
      =\sum_i^n{\bigg(2(y_i-(\tilde ax_i+\tilde b))(-x_i)\bigg)}
      $$

      위 미분값이 0이 되는 조건을 더욱 정리해보면

      $$
      \frac{\partial S}{\partial \tilde a}
      =-2\sum_i^n{\bigg((x_iy_i-\tilde ax_ix_i-\tilde bx_i)\bigg)}=0
      $$

      따라서

      $$
      \frac{\partial S}{\partial \tilde a}
      =-2\sum_i^n{\bigg((x_iy_i-\tilde ax_i^2-\tilde bx_i)\bigg)}=0
      \newline
      \rightarrow \bigg(\sum_i^nx_iy_i\bigg)-\tilde a\bigg(\sum_i^nx_i^2\bigg)-\tilde b\bigg(\sum_i^nx_i\bigg)=0
      $$

      마찬가지로

      $$
      \frac{\partial S}{\partial\tilde b}=\sum_i^n\bigg(2(y_i-\tilde a x_i-\tilde b)\bigg)
      $$

      가 되며, 최적 조건은

      $$
      \bigg(\sum_i^ny_i\bigg)-\tilde a\bigg(\sum_i^nx_i\bigg)-n\tilde b=0
      $$

      으로 표현된다. 두 최적 조건을 나타내는 식을 '연립 방정식'으로 표현할 수 있으며, 이는

      $$
      \begin{bmatrix}
      \sum_i^nx_i^2 & \sum_i^nx_i\\
      \sum_i^nx_i & n
      \end{bmatrix}
      \begin{bmatrix}
      \tilde a\\
      \tilde b
      \end{bmatrix}
      =
      \begin{bmatrix}
      \sum_i^nx_iy_i\\
      \sum_i^ny_i
      \end{bmatrix}
      $$

      따라서, 위 연립 방정식을 풀이하면 $$S$$를 최소화하는
      $\tilde a, \tilde b$ 쌍을 구할 수 있다.

      ```python
      import numpy as np
      import matplotlib.pyplot as plt

      # example data with noise
      xs = np.linspace(0, 10, 10)
      a=2.5
      b=5
      y_true = a * xs + b
      ## artificial noise added.
      noise = np.random.normal(0, 3, size=xs.shape) ## 정규분포 mean:0, std: 3
      ys = y_true + noise

      plt.plot(xs,ys,'ro',label='Data with noise')
      #plt.plot(xs,y_true,'k-',label='True data')

      tilde_a=2
      tilde_b=5

      epsilon=np.zeros(xs.shape)
      for i, x in enumerate(xs):
      	y=x*tilde_a+tilde_b
      	epsilon[i]=y-ys[i]
      	plt.plot([x,x],[ys[i],y],'-')
      plt.plot(xs,tilde_a*xs+tilde_b,'m--',label='manual fit')
      print(f'residual: {(epsilon**2).sum()}')
      plt.legend()

      ## least square
      # the 2x2 matrix
      matrix=np.zeros((2,2))
      matrix[0,0]=(xs**2).sum()
      matrix[0,1]=xs.sum()
      matrix[1,0]=xs.sum()
      matrix[1,1]=len(xs)
      # the 2d vector on the right-hand-side.
      c=np.zeros(2)
      c[0]=(xs*ys).sum()
      c[1]=ys.sum()
      # obtain inverse matrix and multiply it with c
      a_lsq,b_lsq=np.linalg.inv(matrix)@c ## m^{-1} . c
      ```