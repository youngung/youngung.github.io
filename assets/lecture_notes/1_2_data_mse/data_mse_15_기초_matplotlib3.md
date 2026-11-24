---
layout: distill
title: Matplotlib 기초 3
description: 2차원 벡터장, 3차원 결정방향과 결정격자
target: 1학년 2학기
permalink:
featured: true
prerequisite: Matplotlib 기초 2, 벡터 연산 기초
toc: false
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

**목차**

* TOC
{:toc}

# 1. 학습 목표

- 위치 좌표와 벡터 성분을 구분하여 2차원 벡터장을 그릴 수 있다.
- 결정방향을 단위벡터로 바꾸어 3차원 공간에 표현할 수 있다.
- SC·BCC·FCC의 분율좌표로 단위격자와 반복 격자를 그릴 수 있다.
- HCP와 FCC의 적층 순서를 비교하고 HCP의 육각기둥 구조를 그릴 수 있다.
- 원자 중심을 나타내는 산점도와 반지름을 갖는 경구 모형을 구분할 수 있다.

# 2. 위치마다 벡터를 그리기

앞 장에서는 각 격자점 $(x,y)$에 온도 같은 스칼라값 하나를 대응시켰다.
이번에는 각 위치에 가로 성분과 세로 성분을 가진 벡터 $(U,V)$를 대응시킨다.
이렇게 위치마다 벡터가 정해지는 분포를 **벡터장(vector field)**이라고 한다.
화살표는 해당 위치에서 벡터가 가리키는 방향과 크기를 보여 준다.

## 2.1. 세 위치의 변위 그리기

<code>ax.quiver(X, Y, U, V)</code>에서 <code>X</code>, <code>Y</code>는
화살표의 **시작점** 좌표이고, <code>U</code>, <code>V</code>는 가로·세로 성분이다.
아래 예제에서는 좌표와 변위의 단위가 모두 mm다.
두 번째 화살표는 $(1,0)$에서 $(-0.4,0.6)$만큼 이동하므로
끝점은 $(1-0.4,\;0+0.6)=(0.6,0.6)$이다.

~~~python
import matplotlib.pyplot as plt

X, Y = [0, 1, 2], [0, 0, 0]
U, V = [0.6, -0.4, 0.0], [0.4, 0.6, 0.7]

fig, ax = plt.subplots(figsize=(6, 3.4), constrained_layout=True)
ax.quiver(X, Y, U, V, angles="xy", scale_units="xy", scale=1,
          pivot="tail", color="#176892", zorder=2)
ax.scatter(X, Y, color="#333333", s=18, zorder=3, label="Start")
ax.set(xlim=(-0.3, 2.4), ylim=(-0.3, 1.0), xlabel="x (mm)", ylabel="y (mm)")
ax.set_aspect("equal")
ax.grid(alpha=0.25)
ax.legend(loc="upper left")
plt.show()
~~~

![세 변위 화살표가 각각 오른쪽 위, 왼쪽 위, 바로 위를 가리킨다. 검은 점은 화살표의 시작점이다.](/assets/img/lecture_notes/data_mse/matplotlib15_quiver_displacements.png){: width="560" style="max-width: 100%; height: auto;"}

- <code>angles="xy"</code>는 화살표의 방향을 데이터 좌표축 기준으로 정한다.
- <code>scale_units="xy", scale=1</code>은 좌표와 성분이 같은 단위일 때 성분만큼 화살표를 그린다.
- <code>pivot="tail"</code>은 시작 좌표에 화살표의 꼬리를 놓는다.
- <code>set_aspect("equal")</code>은 화면에서 가로 1 mm와 세로 1 mm를 같은 길이로 표시한다.

위치가 m이고 벡터가 m/s인 속도 지도라면, 화살표 길이를 이동거리로 읽으려면
시간 간격이 필요하다. 속도가 그 시간 동안 거의 일정하다고 볼 수 있을 때,
속도에 시간 간격을 곱해 변위로 바꿀 수 있다.

## 2.2. 격자 위의 회전형 벡터장

가로 좌표 5개와 세로 좌표 4개에 [앞 장의 meshgrid](/assets/lecture_notes/1_2_data_mse/data_mse_15_기초_matplotlib2.md)를
적용하면 <code>X</code>, <code>Y</code>, <code>U</code>, <code>V</code>의
shape은 모두 <code>(4, 5)</code>이다. 같은 행·열의 네 값이 화살표 하나를
정한다. 아래에서는 <code>U = -0.25 * Y</code>, <code>V = 0.25 * X</code>로
두어 벡터가 원점을 기준으로 반시계 방향을 향하게 했다.
<code>np.hypot(U, V)</code>는 각 화살표의 크기 $\sqrt{U^2+V^2}$를
계산한다. 이 배열을 다섯 번째 인수로 넘기면 크기에 따라 색을 입힐 수 있다.

~~~python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 3)
y = np.array([-1.5, -0.5, 0.5, 1.5])
X, Y = np.meshgrid(x, y)
U = -0.25 * Y
V = 0.25 * X
magnitude = np.hypot(U, V)
print(X.shape, Y.shape, U.shape, V.shape)  # 모두 (4, 5)

fig, ax = plt.subplots(figsize=(6.3, 4.9), constrained_layout=True)
arrows = ax.quiver(X, Y, U, V, magnitude, angles="xy",
                   scale_units="xy", scale=1, pivot="tail", cmap="viridis")
ax.set(xlim=(-2.65, 2.65), ylim=(-2.1, 2.1), xlabel="x (mm)", ylabel="y (mm)")
ax.set_aspect("equal")
ax.grid(alpha=0.25)
fig.colorbar(arrows, ax=ax, label="Displacement magnitude (mm)")
plt.show()
~~~

![격자점 20개의 회전형 변위장. 원점에서 멀수록 화살표가 길고 밝아진다.](/assets/img/lecture_notes/data_mse/matplotlib15_quiver_vector_field.png){: width="600" style="max-width: 100%; height: auto;"}

예를 들어 <code>X[2, 4] = 2</code>, <code>Y[2, 4] = 0.5</code>인 점의
가로·세로 성분은 각각 $-0.125$ mm와 $0.5$ mm다. 따라서 이 화살표는 왼쪽
위로 향하고 세로 이동량이 가로 이동량보다 크다.

3차원에서는 시작점의 $z$ 좌표와 벡터의 $z$ 성분도 넘긴다. 다음 결정방향
예제에서는 화살표가 모두 원점에서 출발하며, 방향을 비교하기 위해 벡터를
단위벡터로 바꾼다. 2차원 옵션은 [Matplotlib quiver 공식 문서](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html)를 참고한다.

# 3. 재료공학 예제: 결정방향과 격자

## 3.1. 결정방향을 화살표로 그리기

11장의 입방정 결정방향을 다시 사용한다. 서로 직교하는 결정축을 같은 길이 척도로 표현하면,
[입방정(cubic crystal system)](https://en.wikipedia.org/wiki/Cubic_crystal_system)의 결정방향 $[uvw]$는 벡터 $(u,v,w)$와 나란하다. 방향을
표현하기 위해 다음과 같이 단위벡터로 바꾼다.

$$
\widehat{\boldsymbol d}
=\frac{1}{\sqrt{u^2+v^2+w^2}}
\begin{bmatrix}u\\v\\w\end{bmatrix}
$$

~~~python
def unit_direction(uvw):
    direction = np.asarray(uvw, dtype=float)
    if direction.shape != (3,):
        raise ValueError("uvw must contain exactly three components")
    magnitude = np.linalg.norm(direction)
    if magnitude == 0:
        raise ValueError("[000] has no direction")
    return direction / magnitude


print(unit_direction([1, 1, 0]))
~~~

$[100]$, $[010]$, $[001]$, $[110]$ 방향을 화살표로 나타내자.

~~~python
directions = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
])
labels = ["[100]", "[010]", "[001]", "[110]"]

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")

for direction, label in zip(directions, labels):
    vector = unit_direction(direction)
    ax.quiver(0, 0, 0, *vector, arrow_length_ratio=0.12)
    ax.text(*(1.08 * vector), label)

ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.2)
ax.set_zlim(0, 1.2)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Directions in a Cubic Crystal")
ax.set_box_aspect((1, 1, 1))
fig.tight_layout()
plt.show()
~~~

![입방정의 네 결정방향을 단위벡터 화살표로 표시](/assets/img/lecture_notes/data_mse/matplotlib15_crystal_directions.png){: style="width: 840px; max-width: 100%; height: auto;"}

![여러 시점에서 본 입방정의 결정방향의 회전 영상](/assets/img/lecture_notes/data_mse/matplotlib15_crystal_directions_rotation.gif){: style="width: 720px; max-width: 100%; height: auto;"}

<code>np.asarray()</code>는 리스트 등의 입력을 NumPy 배열로 다룰 수 있게 하며,
여기서는 실수형 3성분 배열인지도 확인한다.
<code>zip(directions, labels)</code>는 방향과 이름을 같은 위치끼리 하나씩 짝짓는다.[^zip-for-loop]
<code>*vector</code>는 세 성분을 개별 인자로 풀어 쓰는 문법이다. 예를 들어
<code>ax.quiver(0, 0, 0, *vector)</code>는
<code>ax.quiver(0, 0, 0, vector[0], vector[1], vector[2])</code>와 같다.
화살표의 시작점이 원점이고, 뒤의 세 값이 방향 성분이다.
<code>set_box_aspect((1, 1, 1))</code>와 동일한 세 축 범위는 공간적 비율을 읽는 데 도움이 된다.
음의 성분을 가진 방향을 추가하면 축 범위도 음수까지 넓혀야 한다.
비입방정에서는 12장의 격자행렬처럼 격자벡터를 이용해 실제 좌표 성분으로 바꾼 뒤 정규화해야 한다.

[^zip-for-loop]: <code>zip(A, B)</code>는 두 반복 가능한 객체(iterable)의 원소를
    <code>(A[0], B[0])</code>, <code>(A[1], B[1])</code>, …처럼 튜플로 묶어 차례로
    내놓는 반복자(iterator)를 만든다. 따라서
    <code>for a, b in zip(A, B):</code>에서 각 튜플은 변수 <code>a</code>와 <code>b</code>로
    바로 풀린다. 두 객체의 길이가 다르면 기본 <code>zip()</code>은 더 짧은 쪽이
    끝나는 순간 반복을 멈춘다. 예를 들어
    <code>list(zip([1, 2, 3], ["A", "B"]))</code>의 결과는
    <code>[(1, "A"), (2, "B")]</code>이다.

결정면의 극점도(pole figure)와 입체투영(stereographic projection)은 별도의 결정학
강의에서 다룬다.

## 3.2. 분율좌표로 SC·BCC·FCC 만들기

결정구조를 배웠다면 원자의 좌표를 직접 만들고 그리는 실습을 해 보자.
여기서는 각 격자점에 같은 종류의 원자가 하나씩 놓인 구조를 다룬다.
SC는 단순입방(simple cubic), BCC는 체심입방(body-centered cubic),
FCC는 면심입방(face-centered cubic) 구조를 뜻한다.
이 경우 격자점이 곧 원자의 중심 위치에 해당한다.
입방체의 변 길이는 격자상수(lattice parameter) $a$이고, [분율좌표(fractional coordinates)](https://en.wikipedia.org/wiki/Fractional_coordinates) $(p,q,r)$에 대응하는 실제 위치는

$$
(x,y,z)=a(p,q,r)
$$

이다. 이는 12장의 격자행렬이 $a\boldsymbol I$인 경우다.
아래에서는 결정의 대칭성을 알아보기 쉽도록 정한 입방체 모양의
**[관용 단위격자(conventional unit cell)](https://en.wikipedia.org/wiki/Primitive_cell#Conventional_cell)**를 사용한다.
격자점 하나에 해당하는 부피를 갖는 **[원시 단위격자(primitive unit cell)](https://en.wikipedia.org/wiki/Primitive_cell#Primitive_cell)**와는 구분한다.
BCC와 FCC의 관용 단위격자에는 경계의 공유 비율을 고려했을 때 각각 격자점 2개와 4개가 포함된다.

각 축 방향으로 격자상수의 정수배만큼 평행이동하여 전체 구조를 만들 수 있도록, 기준 원자 위치를 다음처럼 정한다.

| 구조 | 정수 평행이동으로 반복할 분율좌표 |
|---|---|
| SC | $(0,0,0)$ |
| BCC | $(0,0,0)$, $(1/2,1/2,1/2)$ |
| FCC | $(0,0,0)$, $(0,1/2,1/2)$, $(1/2,0,1/2)$, $(1/2,1/2,0)$ |

예를 들어 FCC의 $(0,1/2,1/2)$를 $x$ 방향으로 한 셀 옮기면
$(1,1/2,1/2)$가 되어 반대쪽 면의 중심이 나온다.
표에는 평행이동으로 반복할 기준 원자 위치만 적었다.
단위격자의 경계에 보이는 모든 원자 중심을 나열한 것은 아니다.

~~~python
cubic_sites = {
    "SC": np.array([[0.0, 0.0, 0.0]]),
    "BCC": np.array([
        [0.0, 0.0, 0.0],
        [0.5, 0.5, 0.5],
    ]),
    "FCC": np.array([
        [0.0, 0.0, 0.0],
        [0.0, 0.5, 0.5],
        [0.5, 0.0, 0.5],
        [0.5, 0.5, 0.0],
    ]),
}


def cubic_points(structure, repeats=1):
    # 0 <= p, q, r <= repeats인 닫힌 영역의 원자 중심을 만든다.
    points = []
    for i in range(repeats + 1):
        for j in range(repeats + 1):
            for k in range(repeats + 1):
                shifted = cubic_sites[structure] + np.array([i, j, k])
                inside = np.all(shifted <= repeats, axis=1)
                points.extend(shifted[inside])
    return np.array(points)


for structure in cubic_sites:
    points = cubic_points(structure)
    print(structure, points.shape)
# SC (8, 3), BCC (9, 3), FCC (14, 3)
~~~

배열의 각 행은 원자 중심 하나, 각 열은 $p,q,r$ 성분을 나타낸다.
<code>cubic_sites[structure]</code>의 shape은 <code>(m, 3)</code>이며,
<code>[i, j, k]</code>를 더하면 10장에서 배운 브로드캐스팅으로 기준 위치 $m$개를 함께 옮긴다.
<code>np.all(..., axis=1)</code>은 각 좌표의 세 성분이 모두 범위 안에 있는지 검사한다.
영역의 바깥 경계도 그리기 위해 평행이동 횟수에 <code>repeats</code>를 포함한다. 다만
범위를 벗어난 원자 중심은 불리언 인덱싱, 즉 조건을 만족하는 원소만 선택하는 방법으로 제외한다.

**그림의 점 개수와 단위격자당 유효 원자 수는 다르다.**
입방체의 내부와 경계에 표시한 점은 SC 8개, BCC 9개, FCC 14개다.
하지만 꼭짓점 원자는 이웃 셀 8개가, 면 중심 원자는 이웃 셀 2개가 공유하므로
원자를 공유하는 비율을 고려한 단위격자당 원자 수는 다음과 같다.

$$
N_{\mathrm{SC}}=8\times\frac18=1,\qquad
N_{\mathrm{BCC}}=8\times\frac18+1=2,\qquad
N_{\mathrm{FCC}}=8\times\frac18+6\times\frac12=4.
$$

구조와 원자 수는 [Cambridge의 입방정 구조 자료](https://www.gan.msm.cam.ac.uk/resources/crystalmodels/cubic)도 참고하자.

## 3.3. 세 단위격자를 나란히 비교하기

먼저 셀의 12개 모서리를 그리는 함수를 만든다.
두 꼭짓점의 좌표 중 한 성분만 다르면 같은 모서리의 양 끝이다.

~~~python
def draw_cubic_cell(ax, origin, length):
    corners = np.array([
        [i, j, k]
        for i in (0, 1)
        for j in (0, 1)
        for k in (0, 1)
    ])
    for index, start in enumerate(corners):
        for end in corners[index + 1:]:
            if np.count_nonzero(start != end) == 1:
                edge = np.array(origin) + length * np.array([start, end])
                ax.plot(edge[:, 0], edge[:, 1], edge[:, 2],
                        color="gray", linewidth=0.8, alpha=0.6)


fig = plt.figure(figsize=(12, 4))
for index, structure in enumerate(cubic_sites):
    ax = fig.add_subplot(1, 3, index + 1, projection="3d")
    points = cubic_points(structure)
    ax.scatter(points[:, 0], points[:, 1], points[:, 2],
               s=70, color="tab:blue", depthshade=False)
    draw_cubic_cell(ax, origin=[0, 0, 0], length=1.0)
    ax.set(xlabel="x/a", ylabel="y/a", zlabel="z/a", title=structure,
           xlim=(-0.1, 1.1), ylim=(-0.1, 1.1), zlim=(-0.1, 1.1))
    ax.set_xticks([0, 0.5, 1])
    ax.set_yticks([0, 0.5, 1])
    ax.set_zticks([0, 0.5, 1])
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=20, azim=30)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.12, top=0.88, wspace=0.25)
plt.show()
~~~

![SC·BCC·FCC 관용 단위격자의 원자 중심을 3차원 산점도로 비교](/assets/img/lecture_notes/data_mse/cubic_unit_cells.png){: style="width: 1100px; max-width: 100%; height: auto;"}

![여러 시점에서 본 SC·BCC·FCC 단위격자의 회전 영상](/assets/img/lecture_notes/data_mse/cubic_unit_cells_rotation.gif){: style="width: 1100px; max-width: 100%; height: auto;"}

<code>ax.scatter(x, y, z)</code>는 3차원 점을 그린다.
여기서는 좌표를 $a$로 나눈 무차원 좌표로 표시했다.
회색 선은 단위격자의 테두리이며 원자 사이의 결합을 뜻하지 않는다.
점은 원자 중심의 위치를 나타낸다. <code>s=70</code>은 화면의 표식 크기이며 실제 원자 반지름이 아니다.
<code>view_init()</code>의 <code>elev</code>와 <code>azim</code>은 시선의 고도각과 방위각을 도(degree) 단위로 지정한다.

## 3.4. FCC를 2×2×2셀로 반복하기

격자상수를 $a=0.4$ nm로 가정하고 각 방향에 셀을 2개씩 배치하자.
이는 특정 원소의 실측값이 아니라 분율좌표를 길이로 환산하기 위한 예제 설정이다.

~~~python
repeats = 2
a = 0.4  # nm
fractional_points = cubic_points("FCC", repeats=repeats)
positions = a * fractional_points

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2],
           s=45, color="tab:blue", depthshade=False)
for i in range(repeats):
    for j in range(repeats):
        for k in range(repeats):
            draw_cubic_cell(ax, origin=a * np.array([i, j, k]), length=a)
ax.set(xlabel="x (nm)", ylabel="y (nm)", zlabel="z (nm)",
       title="FCC: 2 x 2 x 2 conventional cells",
       xlim=(-0.05, repeats * a + 0.05),
       ylim=(-0.05, repeats * a + 0.05),
       zlim=(-0.05, repeats * a + 0.05))
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=20, azim=30)
fig.tight_layout()
plt.show()

print(positions.shape)  # (63, 3)
~~~

![FCC 관용 단위격자를 각 방향에 2개씩 배치한 원자 중심의 위치](/assets/img/lecture_notes/data_mse/fcc_repeated_lattice.png){: style="width: 720px; max-width: 100%; height: auto;"}

![여러 시점에서 본 FCC 반복 격자의 회전 영상](/assets/img/lecture_notes/data_mse/fcc_repeated_lattice_rotation.gif){: style="width: 720px; max-width: 100%; height: auto;"}

그린 원자 중심의 좌표 범위는 각 방향으로 0–0.8 nm다.
표시한 63개는 바깥 경계의 원자 중심도 모두 하나씩 센 점의 개수다.
경계에서 원자를 공유하는 비율까지 고려해 계산한 원자 수 $8\times4=32$와 구분하자.
이 코드는 같은 위치의 원자 중심을 셀마다 중복해서 만들지 않는다.
<code>"FCC"</code>를 <code>"SC"</code>나 <code>"BCC"</code>로 바꾸면 같은 방법으로 다른 구조도 비교할 수 있다.

## 3.5. HCP와 FCC의 조밀충전층 적층 비교하기

[조밀충전(close packing)](https://www.iucr.org/what-we-do/education/pamphlets/close-packed-structures)은
같은 크기의 구를 빈 공간이 작도록 배열하는 방법이다.
한 층에서 원자 중심을 삼각 격자(triangular lattice)로 배열하고,
다음 층의 원자를 그 아래층의 세 원자 사이 오목한 자리에 놓으면 조밀충전층을 쌓을 수 있다.

첫 층의 가로 위치를 A, 두 번째 층의 위치를 B라고 하자.
세 번째 층이 첫 층과 같은 가로 위치로 돌아오면 **ABAB…**인
**조밀육방구조(hexagonal close-packed structure, HCP)**가 된다.
반면 세 번째 층을 A·B와 다른 위치 C에 놓으면 **ABCABC…**인 FCC가 된다.
A·B·C는 원자의 종류가 아니라, 위에서 보았을 때 층이 놓이는 서로 다른 위치다.

| 구조 | 층의 반복 순서 | 조밀충전층 | 층을 쌓는 방향 |
|---|---|---|---|
| HCP | ABAB… | 기저면(basal plane) $(0001)$ | $[0001]$ |
| FCC | ABCABC… | $(111)$면 | $[111]$ |

아래 그림에서는 두 구조의 **적층 방향을 모두 화면의 $z$축**으로 맞추었다.
따라서 FCC 그림의 $z$축은 앞 절의 입방체 $[001]$ 방향이 아니라 $[111]$ 방향이다.
HCP의 $(0001)$, $[0001]$은 육방정에서 사용하는 네 지수 표기이며,
이 실습에서는 각각 바닥면과 그 수직 방향이라고 이해하면 된다.

여기서는 같은 층의 최근접 원자 중심 사이 거리를 $a=1$로 놓아 좌표를 무차원화한다.
이 $a$는 HCP의 바닥면 격자상수와 같지만, FCC 입방체의 격자상수 $a_{\mathrm{FCC}}$와는
$a_{\mathrm{FCC}}=\sqrt{2}a$의 관계가 있다.
같은 크기의 구가 맞닿는 이상적인 모델에서는 이웃 층 사이 거리가

$$
h=\sqrt{\frac{2}{3}}a
$$

이고, HCP에서 A층이 다시 나오는 높이는

$$
c=2h,\qquad \frac{c}{a}=\sqrt{\frac{8}{3}}\approx1.633
$$

이다. 실제 HCP 재료의 $c/a$는 이 이상적인 값과 다를 수 있다.

~~~python
a = 1.0  # 같은 층의 최근접 원자 중심 간 거리로 좌표를 정규화
u = np.array([a, 0.0, 0.0])
v = np.array([a / 2, np.sqrt(3) * a / 2, 0.0])
layer_spacing = np.sqrt(2 / 3) * a

base_layer = np.array([
    i * u + j * v
    for i in range(-1, 2)
    for j in range(-1, 2)
])
layer_offsets = {
    "A": np.array([0.0, 0.0, 0.0]),
    "B": (u + v) / 3,
    "C": 2 * (u + v) / 3 - u,
}
layer_colors = {"A": "tab:blue", "B": "tab:orange", "C": "tab:green"}


def stacked_layers(sequence):
    return np.array([
        base_layer + layer_offsets[letter]
        + np.array([0.0, 0.0, k * layer_spacing])
        for k, letter in enumerate(sequence)
    ])


fig = plt.figure(figsize=(12, 6))
for panel, (name, sequence) in enumerate([
    ("HCP", "ABABAB"), ("FCC", "ABCABC"),
]):
    ax = fig.add_subplot(1, 2, panel + 1, projection="3d")
    layers = stacked_layers(sequence)  # shape: (6, 9, 3)
    for k, (letter, points) in enumerate(zip(sequence, layers)):
        ax.scatter(points[:, 0] / a, points[:, 1] / a, points[:, 2] / a,
                   color=layer_colors[letter], s=60, depthshade=False,
                   label=letter if k == sequence.index(letter) else None)
    ax.plot([0, 0], [0, 0], [0, 5 * layer_spacing / a],
            linestyle="--", color="gray", alpha=0.5)
    ax.set(xlabel="x/a", ylabel="y/a", zlabel="z/a",
           title=f"{name}: {sequence}",
           xlim=(-1.8, 2.2), ylim=(-1.1, 1.6), zlim=(-0.2, 4.4))
    ax.set_zticks(np.arange(6) * layer_spacing / a)
    ax.set_zticklabels([f"{k * layer_spacing / a:.2f} {letter}"
                        for k, letter in enumerate(sequence)], fontsize=8)
    ax.set_xticks([-1, 0, 1, 2])
    ax.set_yticks([-1, 0, 1])
    ax.set_box_aspect((4.0, 2.7, 4.6))
    ax.view_init(elev=15, azim=-65)
    ax.legend(loc="upper left", title="Layer position")
fig.subplots_adjust(left=0.06, right=0.90, bottom=0.10, top=0.90, wspace=0.30)
plt.show()
~~~

![HCP의 ABABAB 적층과 FCC의 ABCABC 적층을 층별 색으로 비교](/assets/img/lecture_notes/data_mse/hcp_fcc_stacking.png){: style="width: 1100px; max-width: 100%; height: auto;"}

![여러 시점에서 본 HCP와 FCC의 적층 순서 비교](/assets/img/lecture_notes/data_mse/hcp_fcc_stacking_rotation.gif){: style="width: 1100px; max-width: 100%; height: auto;"}

<code>layers</code>의 세 축은 순서대로 층, 그 층의 원자, 좌표 성분을 뜻한다.
한 층에 원자 중심 9개를 표시했고, 구조를 읽기 쉽게 6개 층만 그렸다.
회색 점선은 같은 가로 좌표를 확인하기 위한 수직 기준선이며 결합선이 아니다.
HCP에서는 두 층 뒤에, FCC에서는 세 층 뒤에 같은 색의 원자 배열이 같은 가로 위치로 돌아오는지 확인하자.
위에서 보면 겹치는 점도 있으므로 옆에서 본 그림과 회전 영상을 함께 비교하는 것이 좋다.
이 그림은 적층 순서를 보여 주기 위한 유한한 영역의 원자 중심 배치이며, 원자 반지름을 나타낸 그림은 아니다.

## 3.6. HCP의 육각기둥 구조 그리기

이번에는 HCP의 A–B–A 세 층을 육각기둥(hexagonal prism) 안에 표시한다.
아래·위 A층에는 육각형의 꼭짓점 6개와 중심 1개가 있고,
중간 B층에는 원자 중심 3개가 있다.
파란 점과 주황 점은 각각 A·B층을 구분하며, 서로 다른 원소를 뜻하지 않는다.

**HCP 구조 자체를 하나의 브라베 격자(Bravais lattice)와 동일시하면 안 된다.**
HCP는 육방 브라베 격자에 원자 2개를 기본 원자 배열(basis, motif)로 붙여 만든 구조다.
앞 절의 두 벡터 $\boldsymbol u,\boldsymbol v$처럼 바닥면 벡터 사이 각도를 $60^\circ$로 잡으면,
세 격자벡터는 $\boldsymbol u,\boldsymbol v,c\boldsymbol e_z$이고,
그에 대한 기본 원자 배열의 분율좌표는 $(0,0,0)$, $(1/3,1/3,1/2)$로 쓸 수 있다.
문헌에서 바닥면 벡터를 $120^\circ$로 잡으면 분율좌표의 표기도 달라지므로,
좌표만 비교하기 전에 어떤 격자벡터를 사용했는지 확인해야 한다.
이때 원자 배열을 뜻하는 basis는 11장의 공간 좌표축을 정하는 기저벡터(basis vector)와 구분하자.

교과서에서 자주 그리는 **큰 육각기둥은 원자 2개짜리 셀 3개에 해당하는 부피**를 갖는다.
따라서 경계의 원자를 공유하는 비율까지 고려하면 이 큰 육각기둥의 원자 수는

$$
N=12\times\frac16+2\times\frac12+3=6
$$

이다. 꼭짓점 원자 12개는 각각 이웃 육각기둥 6개가 공유하고,
위·아래 면 중심의 원자 2개는 각각 두 육각기둥이 공유한다.
기둥 내부 B층의 원자 3개는 모두 포함된다.
그림에 표시한 원자 중심은 $12+2+3=17$개지만, 공유 비율을 고려한 원자 수는 6개다.

~~~python
c = 2 * layer_spacing  # 이상적인 HCP의 c/a = sqrt(8/3)
angles = np.arange(6) * np.pi / 3
hexagon = a * np.column_stack([
    np.cos(angles), np.sin(angles), np.zeros(6),
])
base_sites = np.vstack([hexagon, np.zeros(3)])
a_sites = np.vstack([base_sites, base_sites + np.array([0.0, 0.0, c])])
b_sites = np.array([
    (hexagon[k] + hexagon[(k + 1) % 6]) / 3
    + np.array([0.0, 0.0, c / 2])
    for k in (0, 2, 4)
])

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")
for height in (0.0, c):
    ring = np.vstack([hexagon, hexagon[0]]) + np.array([0.0, 0.0, height])
    ax.plot(ring[:, 0] / a, ring[:, 1] / a, ring[:, 2] / a,
            color="gray", linewidth=1)
for corner in hexagon:
    ax.plot([corner[0] / a] * 2, [corner[1] / a] * 2, [0, c / a],
            color="gray", linewidth=1)
ax.scatter(a_sites[:, 0] / a, a_sites[:, 1] / a, a_sites[:, 2] / a,
           s=90, color=layer_colors["A"], depthshade=False, label="A layers")
ax.scatter(b_sites[:, 0] / a, b_sites[:, 1] / a, b_sites[:, 2] / a,
           s=90, color=layer_colors["B"], depthshade=False, label="B layer")
ax.set(xlabel="x/a", ylabel="y/a", zlabel="z/a",
       title="HCP: A-B-A in a hexagonal prism",
       xlim=(-1.3, 1.3), ylim=(-1.3, 1.3), zlim=(-0.15, c / a + 0.15))
ax.set_box_aspect((2.6, 2.6, c / a + 0.3))
ax.view_init(elev=20, azim=-55)
ax.legend(loc="upper left")
fig.subplots_adjust(left=0.12, right=0.84, bottom=0.12, top=0.88)
plt.show()
~~~

![HCP 구조의 아래와 위 A층 및 중간 B층을 표시한 육각기둥](/assets/img/lecture_notes/data_mse/hcp_hexagonal_prism.png){: style="width: 840px; max-width: 100%; height: auto;"}

![여러 시점에서 본 HCP 육각기둥의 A–B–A 원자 배열](/assets/img/lecture_notes/data_mse/hcp_hexagonal_prism_rotation.gif){: style="width: 840px; max-width: 100%; height: auto;"}

<code>np.column_stack()</code>은 좌표 성분을 열로 묶고,
<code>np.vstack()</code>은 원자 좌표들을 행 방향으로 이어 붙인다.
모서리의 회색 선은 육각기둥의 테두리이며 원자 사이 결합을 뜻하지 않는다.
HCP의 두 원자 기본 배열은 [TU Graz의 HCP 강의자료](https://lampz.tugraz.at/~hadley/ss1/crystalstructure/structures/hcp/hcp.php),
큰 육각기둥의 원자 수는 [IIT Bombay의 결정구조 강의자료](https://homepages.iitb.ac.in/~alsangle/MM219_Lectures_23-24.html)를 참고하자.

## 3.7. 원자를 경구 모형으로 표현하기

앞의 산점도는 원자 **중심의 위치**만 보여 주었다.
이번에는 원자를 반지름이 일정하고 서로 겹치지 않는 구로 나타내는
**경구 모형(hard-sphere model)**으로 원자의 접촉과 빈 공간을 살펴보자.
실제 원자는 딱딱한 공이 아니며, 이 모형은 결정구조의 기하학적 관계를 이해하기 위한 근사다.

3.5절의 $a$는 같은 층에서 가장 가까운 원자 중심 사이 거리이므로,
구들이 맞닿으려면 반지름을 $R=a/2$로 정한다.
이는 <code>scatter(..., s=...)</code>의 점 크기를 키우는 것과 다르다.
산점도 표식은 화면에서의 크기인 반면, 아래 구의 반지름은 **원자 좌표와 같은 길이 단위**를 사용한다.

구의 중심을 $(x_0,y_0,z_0)$라고 할 때 표면의 좌표는

$$
x=x_0+R\sin\theta\cos\phi,\qquad
y=y_0+R\sin\theta\sin\phi,\qquad
z=z_0+R\cos\theta
$$

로 계산할 수 있다. 여기서 $0\le\theta\le\pi$, $0\le\phi\le2\pi$다.
15장 앞부분의 <code>meshgrid()</code>와 <code>plot_surface()</code>를 함께 사용해 보자.
이 절의 코드는 3.5·3.6절에서 만든 좌표와 색상 설정을 이어서 사용한다.

~~~python
from matplotlib.patches import Patch


def draw_hard_sphere(ax, center, radius, color):
    phi = np.linspace(0, 2 * np.pi, 49)
    theta = np.linspace(0, np.pi, 25)
    PHI, THETA = np.meshgrid(phi, theta)
    x = center[0] + radius * np.sin(THETA) * np.cos(PHI)
    y = center[1] + radius * np.sin(THETA) * np.sin(PHI)
    z = center[2] + radius * np.cos(THETA)
    ax.plot_surface(x, y, z, color=color, linewidth=0,
                    antialiased=True, shade=True)
~~~

### 세 번째 층의 위치를 구로 비교하기

가려지는 원자를 줄이기 위해 HCP는 ABA, FCC는 ABC의 **세 층만** 그린다.
위쪽 층에 가려지는 원자도 있으므로 회전 영상과 앞의 원자 중심 그림을 함께 보자.
색은 층의 가로 위치를 구분하며, 원소의 종류를 구분하지 않는다.

~~~python
radius = a / 2
fig = plt.figure(figsize=(12, 6))
for panel, (name, sequence) in enumerate([("HCP", "ABA"), ("FCC", "ABC")]):
    ax = fig.add_subplot(1, 2, panel + 1, projection="3d")
    for letter, points in zip(sequence, stacked_layers(sequence)):
        for center in points:
            draw_hard_sphere(ax, center, radius, layer_colors[letter])
    ax.set(xlabel="x/a", ylabel="y/a", zlabel="z/a",
           title=f"{name}: {sequence} (hard spheres)",
           xlim=(-2.1, 2.6), ylim=(-1.5, 2.0), zlim=(-0.6, 2.3))
    ax.set_box_aspect((4.7, 3.5, 2.9))
    ax.set_xticks([-1, 0, 1, 2])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([0, layer_spacing, 2 * layer_spacing])
    ax.set_zticklabels([f"{z / a:.2f}" for z in [0, layer_spacing, 2 * layer_spacing]])
    ax.view_init(elev=25, azim=-65)
    ax.legend(handles=[Patch(facecolor=layer_colors[letter], label=letter)
                       for letter in dict.fromkeys(sequence)], loc="upper left")
fig.subplots_adjust(left=0.06, right=0.90, bottom=0.10, top=0.90, wspace=0.30)
plt.show()
~~~

![HCP의 ABA와 FCC의 ABC 세 층을 실제 접촉 반지름의 구로 비교](/assets/img/lecture_notes/data_mse/hcp_fcc_hard_spheres.png){: style="width: 1100px; max-width: 100%; height: auto;"}

![천천히 회전하며 비교하는 HCP와 FCC의 경구 모형](/assets/img/lecture_notes/data_mse/hcp_fcc_hard_spheres_rotation.gif){: style="width: 1100px; max-width: 100%; height: auto;"}

두 모형 모두 같은 층과 이웃 층의 최근접 원자가 맞닿는다.
원자 중심 그림과 비교하여 세 번째 층의 위치와 층 사이 빈 공간을 찾아보자.
반투명 구를 사용하지 않았으므로 뒷면의 원자는 앞쪽 구에 가려진다.

### HCP 육각기둥을 경구 모형으로 보기

3.6절에서 만든 A·B층의 중심 좌표를 그대로 사용한다.
원자 중심 사이 거리와 구의 반지름을 같은 비율로 그려야 하므로,
세 축의 **단위 길이가 화면에서도 같도록** 표시 범위와 <code>set_box_aspect()</code>를 함께 맞춘다.

~~~python
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")
for points, color in [(a_sites, layer_colors["A"]), (b_sites, layer_colors["B"])]:
    for center in points:
        draw_hard_sphere(ax, center, radius, color)
for height in (0.0, c):
    ring = np.vstack([hexagon, hexagon[0]]) + np.array([0.0, 0.0, height])
    ax.plot(ring[:, 0], ring[:, 1], ring[:, 2], color="gray", linewidth=0.8)
for corner in hexagon:
    ax.plot([corner[0]] * 2, [corner[1]] * 2, [0, c], color="gray", linewidth=0.8)
ax.set(xlabel="x/a", ylabel="y/a", zlabel="z/a",
       title="HCP hexagonal prism: hard spheres",
       xlim=(-1.6, 1.6), ylim=(-1.6, 1.6), zlim=(-0.6, c + 0.6))
ax.set_box_aspect((3.2, 3.2, c + 1.2))
ax.view_init(elev=20, azim=-55)
ax.legend(handles=[Patch(facecolor=layer_colors["A"], label="A layers"),
                   Patch(facecolor=layer_colors["B"], label="B layer")], loc="upper left")
fig.subplots_adjust(left=0.12, right=0.84, bottom=0.12, top=0.88)
plt.show()
~~~

![HCP 육각기둥의 원자를 중심 간 거리와 같은 길이 단위의 구로 표현](/assets/img/lecture_notes/data_mse/hcp_prism_hard_spheres.png){: style="width: 840px; max-width: 100%; height: auto;"}

![천천히 회전하는 HCP 육각기둥의 경구 모형](/assets/img/lecture_notes/data_mse/hcp_prism_hard_spheres_rotation.gif){: style="width: 840px; max-width: 100%; height: auto;"}

이 그림은 경계의 원자를 잘라 내지 않고 **구 전체**를 그렸다.
따라서 꼭짓점과 위·아래 면 중심의 구는 육각기둥의 테두리 밖으로도 나온다.
기둥 안에 포함되는 원자 수를 계산할 때는 여전히 3.6절의 공유 비율을 적용한다.
앞에서 그린 FCC 입방체에 경구 모형을 적용한다면,
입방체 격자상수 $a_{\mathrm{FCC}}$에 대해 $R=a_{\mathrm{FCC}}/(2\sqrt{2})$를 사용해야 한다.
층 내부의 최근접 거리 $a$와 입방체의 격자상수를 혼동하지 않도록 주의하자.
관련 설명은 [IIT Bombay의 경구 모형과 결정구조 강의자료](https://homepages.iitb.ac.in/~alsangle/MM219_Lectures_23-24.html)를 참고한다.

# 4. 자주 하는 실수

- <code>U</code>, <code>V</code>에는 시작점에서 끝점까지의 성분을 넣는다.
- 영벡터 $[000]$은 방향을 나타내지 않는다.
- 격자 그림에 표시된 점의 개수와 단위격자당 유효 원자 수를 혼동하지 않는다.
- HCP·FCC 적층 그림의 색을 서로 다른 원소로 해석하지 않는다.
- FCC의 적층 방향 $[111]$을 입방체의 $[001]$ 방향과 혼동하지 않는다.

# 5. 정리

- 2차원 벡터장은 각 시작점과 해당 벡터의 두 성분을 화살표로 그린다.
- 3차원에서는 시작 좌표와 벡터 성분이 각각 세 개다.
- 원자 중심 좌표를 정수만큼 평행이동해 반복 격자를 그린다.

다음 16장에서는 최소자승법으로 측정값에 맞는 모델의 계수를 구한다.

# 6. 연습 문제

## 문제 1: 화살표의 성분과 끝점

회전형 벡터장에서 <code>X[1, 0]</code>, <code>Y[1, 0]</code>에 놓인
화살표의 성분과 끝점을 구하고 그림에서 방향을 확인하시오.

<!--
풀이와 해답:
시작점은 (-2, -0.5) mm, 성분은 (0.125, -0.5) mm이다.
화살표는 오른쪽 아래의 (-1.875, -1.0) mm를 향한다.
-->

## 문제 2: 단위격자의 점과 원자 수

FCC 단위격자 그림에는 점이 14개 보인다. 단위격자당 원자 수가 4인 이유를 설명하시오.
또한 <code>cubic_points("BCC", repeats=1)</code>의 shape을 쓰시오.

<!--
풀이와 해답:
FCC는 꼭짓점 8개×1/8 + 면 중심 6개×1/2 = 4개다.
그림의 14개는 경계 공유를 고려하지 않고 표시한 원자 중심의 개수다.
BCC 함수의 결과 shape은 (9, 3)이다. 꼭짓점 8개와 체심 1개를 그린다.
-->

## 문제 3: 격자상수와 실제 좌표

FCC에서 원점과 분율좌표 $(0,1/2,1/2)$인 원자 중심 사이의 거리를,
격자상수 $a=0.4$ nm일 때 NumPy로 구하시오.
$2\times2\times2$ 격자의 <code>positions</code>를 만든 뒤 $a$만 0.5로 바꾸면
이미 계산한 좌표도 자동으로 바뀌는지 설명하시오.

<!--
풀이와 해답:
displacement = 0.4 * np.array([0.0, 0.5, 0.5])
distance = np.linalg.norm(displacement)
거리 = a/sqrt(2) ≈ 0.2828 nm다.
a를 바꿔도 기존 positions 배열은 바뀌지 않는다.
positions = a * fractional_points를 다시 실행해야 한다.
-->

## 문제 4: 세 번째 층의 위치

첫 두 조밀충전층이 AB일 때, 세 번째 층을 어디에 놓으면 HCP가 되고 어디에 놓으면 FCC가 되는가?
또한 이 예제의 FCC 그림에서 $z$축이 입방체의 $[001]$ 방향인지 설명하시오.

<!--
풀이와 해답:
세 번째 층을 첫 층과 같은 가로 위치 A에 놓으면 ABA…, 즉 HCP가 된다.
A·B와 다른 위치 C에 놓으면 ABC…, 즉 FCC가 된다.
FCC 그림의 z축은 조밀충전 (111)면에 수직인 [111] 방향이다.
-->

## 문제 5: HCP의 두 셀과 원자 수

원자 중심이 17개 표시된 큰 HCP 육각기둥의 유효 원자 수를 계산하시오.
이것이 원자 2개짜리 셀의 원자 수와 다른 이유도 설명하시오.

<!--
풀이와 해답:
꼭짓점 12×1/6 + 위·아래 면 중심 2×1/2 + 내부 3 = 6개다.
큰 육각기둥의 부피는 원자 2개짜리 셀의 3배이므로 모순이 아니다.
그림에 표시한 중심의 개수와 경계 공유를 고려한 원자 수는 다르다.
-->

---

[이전 강의](/assets/lecture_notes/1_2_data_mse/data_mse_15_기초_matplotlib2.md) · [강의 목록](/_lectures/1_2_data_mse.md) · [다음 강의](/assets/lecture_notes/1_2_data_mse/data_mse_16_git_github.md)
