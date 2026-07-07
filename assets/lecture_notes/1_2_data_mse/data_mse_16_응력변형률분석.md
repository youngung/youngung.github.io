---
layout: distill
title: 데이터 재료과학 (제 7강)
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

# 목표
- Force vs. Disp curve 분석, 최소 자승법
- 목표
  - force vs. displacement 파일로 불러올 수 있다.
  - 응력 변형률로 데이터를 분석하고 이를 진응력 진변형률로 바꿀 수 있다.
  - 최소 자승법을 이해하고 활용할 수 있다.

## Force vs. displ 데이터 -> 응력 선도

- 실습을 위해 필요한 다음 [calibration1](/assets/dat_files/lectures/1_2_data_mse/calibration1.txt),
  [calibration2](/assets/dat_files/lectures/1_2_data_mse/calibration2.txt)
  파일을 다운로드 받자.
- 첫번째 calibration file은 변위 측정 장치에서 측정된 voltage 변화를 mm 단위의 변위로 '변환'해준다.
- 두번째 calibration file은 로드셀 (load)장치에서 측정된 voltage 변화를 kN 단위의 힘으로 '변환'해준다.

  ```python
  import matplotlib.pyplot as plt
  c1=np.loadtxt('calibration1.txt')
  c2=np.loadtxt('calibration2.txt')

  fig=plt.figure()
  ax1=fig.add_subplot(121)
  ax2=fig.add_subplot(122)

  y=c1[:,0] # extension in [mm]
  x=c1[:,1] # voltage
  ## 뒤죽박죽 시행된 calibration sheet의 데이터를 X(voltage)기준으로 정렬하자.
  ind=np.argsort(x)
  y=y[ind]
  x=x[ind]
  # 정렬된 calibration sheet 데이터를 그리자.
  ax1.plot(x,y,'-o',mfc='None',label='Calibration')

  ## let's find out what y=ax+b fits this equation well.
  a1=0.1
  b1=0.1 ## a1 과  b1 을 바꿔가며 calibration 해보자.
  xs=np.linspace(-4,2)
  ys=xs*a1+b1
  ax1.plot(xs,ys,label='fit')
  ax1.legend()

  y=c2[:,0] # force in kN
  x=c2[:,1] # voltage
  # .... 이어 계속해서 프로그래밍 해보자.
  ```

  이렇게 얻어진 데이터를 가지고 폭과 두께, 그리고 gauge length를 안다면
  응력 vs. 변형률 데이터로 변환 가능하다.

- 다음으로, 위에서 구한 힘과 변위를 활용해 응력 vs. 변형률 데이터로 바꿔보자.

  - 폭이 12.695 mm, 두께가 1.193 mm, 게이즈가 20 mm라 가정하자.
  - 공칭 응력

  $$
  \sigma^{engi}=\frac{force}{Area}
  $$

  - 공칭 변형률

  $$
  \epsilon^{engi}=\frac{\Delta l}{l_0}
  $$

  - 진 변형

  $$
  \varepsilon=\ln(1+\epsilon)
  $$

  - 진 응력

  $$
  \sigma^{true}=\sigma^{engi}(1+\epsilon)
  $$

  ```python
  ## algorithm
  # 1. 파일로부터 Numpy를 활용해 데이터를 불러온다.
  # 2. 주어진 시편의 폭과 두께로부터 초기단면적을 구한다.
  # 3. 초기 단면적과 힘을 활용해 공칭 응력을 구한다.
  # 4. 초기 게이지 길이와 변위를 활용해 공칭 변형률을 구한다.
  # 5. 진 변형률을 구한다.
  # 7. 진 응력을 구한다.
  # 8. 진응력 vs. 진 변형률 곡선을 구한다.
  # 9. 최대 하중 이후의 데이터를 trimming 해본다.
  ```

- Hollomon Equation으로 바꿔본다.

$$
\sigma=k\varepsilon^n
$$

적절한 k값과 n값을 앞서 calibration sheet의 $ a$ 그리고 $ b $에 해당하는 값을 찾기 위해서는
$\log$ 함수의 활용이 유용하다.

$$
\log\sigma=\log k + n\log \varepsilon
$$

밑(base)이 자연수(2.713...)인 로그 함수를 활용한다면

$$
ln\sigma=\ln{k}+n\ln\varepsilon
$$

이를 활용해 적절한 $k$ 값 및 $n$ 값을 구해보자.

```python
# np.log 함수를 활용해 밑이 자연수인 로그 함수를 활용하자.
# np.log(sigma), np.log(epsilon)
# plt.plot 활용해 직선 그려보기
# a값 그리고 b값 찾기.
# log (a) 그리고 log (b)로부터 a, b값을 역산(거꾸로 계산) 해보자.
```

- 복잡한 형태의 데이터 파일의 경우를 생각해보자.
  이미 calibration된 이후 얻어진 [힘/변위 데이터](/assets/dat_files/lectures/1_2_data_mse/force_vs_displ.txt)를
  살펴보고, 분석해보자.

  ```python
  np.loadtxt('filename') # 이 명령어가 적용되지 않는 여러 이유가 있다. 그 이유를 파일을 직접 살펴보고 고민해보자.
  #with open(fn,'r') as fo:
  #    cnt=fo.read()
  #    blocks=cnt.split('Data Acquisition')
  #    blocks=blocks[1:]

  #for ib,block in enumerate(blocks):
  #    lines=block.split('\n')
  #    lines=lines[3:-2] ##??
  #    bl=''
  #    dmaster=np.zeros((len(lines),4),dtype='float')
  #    for i, line in enumerate(lines):
  #        dmaster[i,:]=np.array(line.split('\t'),dtype='float')

  #    plt.plot(dmaster[:,1],dmaster[:,2])
  ```

## 11.2. 수업 09-2 (노이즈가 있는 데이터로부터 최소자승법을 활용한 선형회귀)

- 목표

  - 최소 자승법을 이해한다.
  - 09-1의 데이터의 활용헤서 '최소자승법'을 활용해본다.

- 개념

  - 주어진$$n$$ 쌍의의 데이터가 아래와 같이 표현될 수 있다.

  $$
  (x_i,y_i) \text{ with } i=1,2,...,n
  $$

  이때 위 $$n$$쌍의 데이터를 우리가 구하는 직선의 방정식이 매우 잘 대표해야 하겠다.

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