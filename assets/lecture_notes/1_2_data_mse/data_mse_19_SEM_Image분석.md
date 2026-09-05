---
layout: distill
title: SEM 영상 분석 기초
description: SEM 영상의 명암 분포와 간단한 상 분리
target: 1학년 2학기
permalink:
featured: true
prerequisite: NumPy, Matplotlib
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

- [1. 목표](#1-목표)
- [2. 색과 image 그리기](#2-색과-image-그리기)
  - [2.1. 색표현을 설명](#21-색표현을-설명)
  - [2.2. 이미지 그리기](#22-이미지-그리기)
  - [2.3. 미세조직 사진 활용 실습](#23-미세조직-사진-활용-실습)
- [3. 상분리 실습](#3-상분리-실습)

# 1. 목표

- Matplotlib imaging, color-coding, EBSD 데이터 분석
- SEM 데이터를 소개하고, Ferrite와 Martensite로 분류

# 2. 색과 image 그리기

## 2.1. 색표현을 설명

- Gray scale (0~255)
- RGB R(0~~255), G(0~~255), B(0~255)
- RGBA R(0~~2550), G(0~~255), B(0~~255), alpha(0~~1)
- [참고](<https://www.w3schools.com/colors/colors_rgb.asp?color=rgb(102,%20255,%20255)>)

## 2.2. 이미지 그리기

- [imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html) 함수

  ```python
  import matplotlib.pyplot as plt
  import numpy as np

  # 5x5 랜덤 배열
  data = np.random.rand(5, 5)

  plt.imshow(data, cmap='viridis', interpolation='nearest')
  plt.colorbar()  # 값과 색의 대응 막대 추가
  plt.show()
  ```

- Color map (`cmap`) 옵션

  ```python
  import matplotlib.pyplot as plt
  import numpy as np

  # 100x100 배열: 0~255 값 (가상의 화상)
  grain_map = np.random.randint(0, 255, (100, 100))

  fig=plt.figure(figsize=(8,2))
  # 1x3 axes 생성
  ax1=fig.add_subplot(131)
  ax2=fig.add_subplot(132)
  ax3=fig.add_subplot(133)
  #--
  # random하게 만들어진 0~255 사이의 값 확인
  ax1.hist(grain_map.flatten())# histogram
  ##
  cmaps=['jet','gray']
  for i, ax in enumerate([ax2,ax3]):
  	ax.imshow(grain_map, cmap=cmaps[i])
  	ax.set_title(f'color map: {cmaps[i]}')
  ```

## 2.3. 미세조직 사진 활용 실습

- 아래 사진을 [여기](/assets/dat_files/lectures/1_2_data_mse/dualphase_sem.png) 눌러서 다운 받자

![imag](/assets/dat_files/lectures/1_2_data_mse/dualphase_sem.png)

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

fn='../data/dualphase_sem.png' ## file name을 경로를 포함하여 정확하게 기입해야 한다.
img_rgba = Image.open(fn) ## PIL, RGBA
img_gray=img_rgba.convert('L') ## convert image into gray scale
img_gray=np.asarray(img_gray)
plt.imshow(img_gray,cmap='gray')
```

위 사진은 ferrite와 martensite가 같이 존재하는 dual-phase 철강 제품의
주사 전자 현미경 사진이다. 이 사진에서 밝은 부분은 ferrite, 어두운 부분은 martensite
상이다. 이를 구분하여 두 상의 '분율'을 구해보자.

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img=Image.open('../data/dualphase_sem.png')
img=np.asarray(img)
print(img.shape)

## Canvas와 사용할 축을 2x2 grid의 형태로 만들자.
fig=plt.figure(figsize=(7,4))
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)

## 첫번째 axis에는 각 화상(pixel)에서 0~255사이의
# 값들이 어떻게 분포하는지 histogram으로 그리자.
ax1.hist(img.flatten())
# 그리고 그 옆에 불러온 SEM 이미지를 그려보자.
ax2.imshow(img,cmap='gray')

## 아래는 ferrite상과 martensite 상을 구분하는 간단한 예시를 살펴보자.

#newimg=img.copy()
#flg=img>img.mean()
#newimg[flg]=255
#newimg[~flg]=0
#h=ax3.hist(newimg.flatten())
#ax4.imshow(newimg,cmap='gray')
#for i, ax in enumerate([ax1,ax3]):
#    ax.set_ylim(0,300000)

#white,black=h[0][0],h[0][-1]
#ferrite=white/(white+black)
#martensite=black/(white+black)
#print(ferrite,martensite)
```

# 3. 상분리 실습

- 아래 세 이미지는 한 dual-phase 시편 내의 각기 다른 3 위치에서 촬영한 SEM image이다.
  위에서 다뤘던 내용을 익혀 적용하고, 이를 바탕으로 이 시편에서의 ferrite와 martensite
  분율을 고르시오.

  ![imag](/assets/dat_files/lectures/1_2_data_mse/centercenter.png)
  ![imag](/assets/dat_files/lectures/1_2_data_mse/edgecenter.png)
  ![imag](/assets/dat_files/lectures/1_2_data_mse/edgeedge.png)

  - 위 SEM 사진을 다음 링크를 활용해 다운 받자:

  [imag1](/assets/dat_files/lectures/1_2_data_mse/centercenter.png)
  [imag2](/assets/dat_files/lectures/1_2_data_mse/edgecenter.png)
  [imag3](/assets/dat_files/lectures/1_2_data_mse/edgeedge.png)

# 쉬운 연습 문제

## 문제 1

8-bit 회색조 영상의 밝기값 범위를 쓰시오.

<!--
풀이와 해답:
0부터 255까지이다.
-->

## 문제 2

회색조 영상에서 일반적으로 0과 255는 각각 어떤 색에 해당하는가?

<!--
풀이와 해답:
0은 검정, 255는 흰색에 해당한다.
-->

## 문제 3

영상의 밝기값 분포를 확인하는 그래프는 무엇인가?

<!--
풀이와 해답:
히스토그램(histogram)이다.
-->
