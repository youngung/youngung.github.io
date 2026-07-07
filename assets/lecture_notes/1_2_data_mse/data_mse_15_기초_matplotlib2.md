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

- 임의의 3차원 벡터 생성과 stereographic projection.

cubic crystal structure내의 결정 방위 [h,k,l]에 해당하는 단위 벡터를 그려보자. Cubic crystal의 경우 Miller index $[uvw]$가 한 결정 방향이라면 그 방향에 해당하는 벡터 $\boldsymbol b$는 아래와 같이 구할 수 있다.
$$
\boldsymbol b = (b_1,b_2,b_3)=\bigg(\frac{h}{\sqrt{h^2+k^2+l^2}},\frac{h}{\sqrt{h^2+k^2+l^2}},\frac{h}{\sqrt{h^2+k^2+l^2}}\bigg)
$$
이를 계산하는 함수를 작성해보면
```python
def get_direct(uvw=np.array([1,1,0])):
  """
  Argument
  --------
  uvw: as in <ndarray> or <list>

  Return
  ------
  uvw/deno
  """
  ##
  if type(uvw).__name__=='list':
    uvw=np.array(uvw)

  deno=(uvw**2).sum() # demoniator: 분모, numerator: 분자
  deno=np.sqrt(deno)
  return uvw/deno

## 테스트 해보자.
get_direct([1,1,0])
get_direct([1,1,1])
```

꼭 List 타입으로 주는 방식이 싫다면 아래와 같은 형태도 괜찮은 대안이 될 수 있겠다.
```python
def get_direct(v1,v2,v3):
  """
  Argument
  --------
  v1,v2,v3

  Return
  ------
  """
  ##
  uvw=np.array([v1,v2,v3])
  deno=(uvw**2).sum() # demoniator: 분모, numerator: 분자
  deno=np.sqrt(deno)
  return uvw/deno
```

위 함수를 활용해 결정학적으로 같이 $[100],[010],[001],[\bar{1}00],[0\bar{1}0],[00\bar{1}]$을 3차원 그래프로 표현해보자. 3차원 점들을 표현하기 위해서는 3차원 axis가 필요하다. 이를 위해서 fig의 add_subplot 매소드에 'projection=3d' 파라미터를 입력하여 3차원 axis를 만들자. 그 다음, 앞서 생성한 점들을 'scatter'함수를 활용해 아래와 같이 표현해보자.
```python
%matplotlib widget
fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')
vs=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
for i, v in enumerate(vs):
    uvw=get_direct2(*v)
    ax1.scatter(*uvw,marker='o',color='k')
```

3차원 공간인지 사실 한눈에 살펴보기 어렵다. 따라서, 원점(0,0,0)에서부터 각 지점까지 화살표로 이어보는게 더 좋겠다. 화살표를 그리기 위해서 [```quiver```](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html)매소드를 활용하였다.
```python
%matplotlib widget
import matplotlib.pyplot as plt
fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')
vs=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
orig=[0,0,0]
for i, v in enumerate(vs):
    uvw=get_direct2(*v)
    ax1.scatter(*uvw,marker='o',color='k')
    ax1.quiver(*orig,*uvw,arrow_length_ratio=0.2,color='r')
```

3차원 방향을 좀 더 명확히 살펴보기 위해, 반지름 1인 구(sphere)를 같이 그려보면 좋겠다. 이를 위해서는 [구면 좌표계(spherical coordinate system)](https://ko.wikipedia.org/wiki/구면좌표계)를 활용하면 더욱 쉽게 구를 그릴 수 있다. $(r,\theta,\phi)$의 좌표계에서 $r=1$로 고정하면, 반지름이 1인 구의 면에 해당한다. 아래 범위 내의 경우를 활용하면 되겠다.
- $\theta=[0,\pi]$
- $\phi=[0,2\pi]$

주어진 구 좌표계는 다음과 같이 직교 좌표계 $(x,y,z)$로 아래와 같이 변환된다.

- $x=r\times \sin\theta\cos\phi$
- $y=r\times \sin\theta\sin\phi$
- $z=r\cos\theta$

[```np.mgrid```](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html)기능을 활용하면 쉽게 그리드를 만들 수 있다. np.linspace와 유사하나, 다차원으로 확장가능하며, grid를 만들기에 적합하다.

```python
import numpy as np
theta,phi=np.mgrid[0:np.pi:10j,0:2*np.pi:10j]
```
위에 만들어진 theta와 phi를 직교좌표계로 바꾸면
```python
import numpy as np
theta,phi=np.mgrid[0:np.pi:10j,0:2*np.pi:10j]
r=1 # radius가 1이다.
## 직교 좌표계로 아래와 같이 변환할 수 있다.
x=r*np.sin(theta)*np.cos(phi)
y=r*np.sin(theta)*np.sin(phi)
z=r*np.cos(theta)
```

이제 grid된 x,y,z좌표와 matplotlib의 plot_wireframe을 활용해서 3D 구면을 그려보자.

```python
import numpy as np
theta,phi=np.mgrid[0:np.pi:10j,0:2*np.pi:10j]
r=1 # radius가 1이다.
## 직교 좌표계로 아래와 같이 변환할 수 있다.
x=r*np.sin(theta)*np.cos(phi)
y=r*np.sin(theta)*np.sin(phi)
z=r*np.cos(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x,y,z,alpha=0.2,lw=0.9) ## alpha: 투명도, lw: linewidth
```

나아가, 그 위에 앞서 구한 결정방향들을 올려보자.

```python
import numpy as np
theta,phi=np.mgrid[0:np.pi:20j,0:2*np.pi:20j]
r=1 # radius가 1이다.
## 직교 좌표계로 아래와 같이 변환할 수 있다.
x=r*np.sin(theta)*np.cos(phi)
y=r*np.sin(theta)*np.sin(phi)
z=r*np.cos(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x,y,z,alpha=0.2,lw=0.9)

##
vs=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
orig=[0,0,0]
for i, v in enumerate(vs):
    uvw=get_direct2(*v)
    ax.scatter(*uvw,marker='o',color='k')
    ax.quiver(*orig,*v,arrow_length_ratio=0.2,color='r')
```

그런데 사실, 3차원으로 그린 그래프 툴이 개발되기 전에도 많은 재료공학자들이 3차원 정보를 표현해야만 했다. 그들은 3차원 정보를 2차원면에 표현하기 위해 stereographic projection법을 활용하였다.

```python
%matplotlib widget
#%matplotlib inline
fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')
vs=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
orig=[0,0,0]
for i, v in enumerate(vs):
    uvw=get_direct2(*v)
    ## quiver 메소드를 활용하였다.
    ax1.quiver(*orig,*v,arrow_length_ratio=0.2,color='r')

d=1.2
ax1.set_xlim(-d,d)
ax1.set_ylim(-d,d)
ax1.set_zlim(-d,d)
```
