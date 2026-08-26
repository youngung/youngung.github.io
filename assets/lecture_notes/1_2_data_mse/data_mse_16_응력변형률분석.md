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

# 1. 목표

- Force vs. Disp curve 분석, 최소 자승법
- 목표
  - force vs. displacement 파일로 불러올 수 있다.
  - 응력 변형률로 데이터를 분석하고 이를 진응력 진변형률로 바꿀 수 있다.
  - Hollomon equation의 파라미터 구하기

# 2. Force vs. displ 데이터 -> 응력 선도

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

# Hollomon Equation

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
