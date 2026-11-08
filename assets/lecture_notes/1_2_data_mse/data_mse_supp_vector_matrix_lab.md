---
layout: distill
title: 벡터·행렬 종합 실습 — 기울어진 격자와 원자 이동
description: 분율좌표, 실제 위치, 변위, 투영, 면적과 역변환을 연결하는 NumPy 실습
target: 1학년 2학기
prerequisite: 벡터 연산 기초, 행렬 연산 기초
toc: false
hidden: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

**목차**

* TOC
{:toc}

# 1. 실습 목표와 입력 데이터

[제11강 벡터 연산]({% link assets/lecture_notes/1_2_data_mse/data_mse_11_벡터연산기초.md %})과
[제12강 행렬 연산]({% link assets/lecture_notes/1_2_data_mse/data_mse_12_행렬연산기초.md %})을 함께 사용해 보자.
아래 코드를 위에서부터 순서대로 실행한다. 각 배열의 shape, 각 행과 열의 의미, 단위를 먼저 예상한 다음 결과를 확인하자.

세 격자벡터를 다음과 같이 정한다. 길이 단위는 nm다.

$$
\boldsymbol a=(2,0,0),\qquad
\boldsymbol b=(1,3,0),\qquad
\boldsymbol c=(0,0,4).
$$

격자벡터를 열에 배치한 $[\boldsymbol L]$과 분율좌표 $[\boldsymbol p]$ 사이의 관계는
$[\boldsymbol r]=[\boldsymbol L][\boldsymbol p]$다.
분율좌표는 각 격자벡터를 몇 배씩 더하는지 나타내는 무차원 계수다.

~~~python
import numpy as np

L = np.array([
    [2.0, 1.0, 0.0],
    [0.0, 3.0, 0.0],
    [0.0, 0.0, 4.0],
])
P_before = np.array([
    [0.0, 0.0, 0.0],
    [0.5, 0.5, 0.0],
    [0.0, 0.0, 0.5],
])
P_after = np.array([
    [0.1, 0.0, 0.0],
    [0.5, 0.6, 0.0],
    [0.0, 0.0, 0.6],
])
~~~

각 좌표 배열은 행마다 한 점을 저장하며, 이동 전후 같은 행은 같은 점에 대응한다.
이 실습에서는 격자행렬이 이동 전후 일정하다고 가정한다.

# 2. 실제 위치와 변위 계산

점을 행마다 저장했으므로 오른쪽에 <code>L.T</code>를 곱한다.

~~~python
R_before = P_before @ L.T
R_after = P_after @ L.T
U = R_after - R_before
lengths = np.linalg.norm(U, axis=1)

print(R_before)
print(U)
print(lengths)
~~~

이동 전 위치는 $(0,0,0)$, $(1.5,1.5,0)$, $(0,0,2)\,\mathrm{nm}$다.
변위는 각각 $(0.2,0,0)$, $(0.1,0.3,0)$, $(0,0,0.4)\,\mathrm{nm}$이며,
크기는 약 $0.2$, $0.316228$, $0.4\,\mathrm{nm}$다.

이 계산은 지정된 위치 사이의 직접 변위를 구한다.
주기적 경계를 넘어간 원자의 이동을 추적할 때는 경계 통과 이력 등을 별도로 처리해야 한다.

# 3. 특정 방향으로 이동한 양 구하기

$\boldsymbol b$ 방향으로 이동한 **부호 있는 성분**을 구하자.
먼저 방향벡터를 단위벡터로 만든다.

~~~python
b_vector = L[:, 1]
n = b_vector / np.linalg.norm(b_vector)
components = U @ n
U_parallel = components[:, None] * n
U_perpendicular = U - U_parallel

print(components)
print(np.allclose(U_parallel + U_perpendicular, U))
print(np.allclose(U_perpendicular @ n, 0.0))
~~~

성분은 약 $0.063246$, $0.316228$, $0\,\mathrm{nm}$다.
두 번째 점의 변위는 $\boldsymbol b$와 평행하므로 평행 성분이 전체 변위와 같다.
세 번째 점은 $\boldsymbol b$와 수직으로 이동하므로 이 방향의 성분이 0이다.
<code>components[:, None]</code>은 세 스칼라 성분을 열 배열로 바꿔 각 행의 단위벡터에 곱하도록 한다.

# 4. 격자면 넓이와 셀 부피

~~~python
a_vector = L[:, 0]
c_vector = L[:, 2]
area_vector = np.cross(a_vector, b_vector)
area = np.linalg.norm(area_vector)
normal = area_vector / area
volume = abs(np.dot(area_vector, c_vector))
volume_from_det = abs(np.linalg.det(L))

print(area_vector, area, normal)
print(volume, volume_from_det)
print(np.isclose(volume, volume_from_det))
~~~

$\boldsymbol a\times\boldsymbol b=(0,0,6)\,\mathrm{nm}^2$이며 면적은 $6\,\mathrm{nm}^2$다.
단위법선은 $(0,0,1)$이고 셀 부피는

$$
V=|(\boldsymbol a\times\boldsymbol b)\cdot\boldsymbol c|
=|\det[\boldsymbol L]|=24\,\mathrm{nm}^3
$$

다. 외적의 크기는 면적이고, 여기에 세 번째 벡터의 법선 방향 성분을 곱하면 부피가 된다.
현재 입력에서는 면적이 0이 아니므로 단위법선을 구할 수 있다.

# 5. 분율좌표로 돌아가서 검산하기

한 점의 실제 위치가 주어졌을 때 분율좌표를 구하는 것은
$[\boldsymbol L][\boldsymbol p]=[\boldsymbol r]$를 푸는 문제다.

~~~python
recovered = np.linalg.solve(L, R_after[1])
print(recovered)  # [0.5, 0.6, 0.0]
print(np.allclose(recovered, P_after[1]))
print(np.allclose(L @ recovered, R_after[1]))
~~~

역행렬을 직접 만들지 않고도 원래 좌표를 복원할 수 있다.
이 복원이 유일하려면 세 격자벡터가 독립이어야 한다.

# 6. 추가 과제

## 문제 1: 가장 많이 이동한 점

<code>lengths</code>를 이용하여 가장 많이 이동한 점의 행 인덱스와 변위 크기를 구하라.

<!--
풀이와 해답:
index = np.argmax(lengths)이므로 인덱스는 2, 크기는 0.4 nm이다.
-->

## 문제 2: 단위 변환

격자벡터의 수치를 nm에서 Å로 바꾸기 위해 <code>L_angstrom = 10 * L</code>로 정의하라.
변위 크기, 격자면 넓이, 셀 부피의 수치가 각각 몇 배 되는지 예상하고 검산하라.

<!--
풀이와 해답:
길이는 10배, 넓이는 100배, 부피는 1000배다.
단위 변환이므로 물리적 크기가 달라진 것이 아니다.
-->

## 문제 3: 투영 방향 뒤집기

3절에서 <code>n</code>을 <code>-n</code>으로 바꾸면
스칼라 성분과 벡터 투영이 각각 어떻게 되는가? 수식과 코드로 설명하라.

<!--
풀이와 해답:
스칼라 성분 U @ (-n)은 기존 값의 음수다.
벡터 투영은 (U @ (-n))[:,None] * (-n)이므로 두 부호가 상쇄되어 그대로다.
같은 직선에 대한 벡터 투영은 방향의 부호 선택에 의존하지 않는다.
-->

## 문제 4: 격자벡터의 독립성

<code>L_bad = L.copy()</code>로 복사한 뒤
<code>L_bad[:, 2] = L_bad[:, 0] + L_bad[:, 1]</code>로 바꾸어라.
셀 부피와 좌표 복원의 유일성에 어떤 문제가 생기는가?

<!--
풀이와 해답:
세 번째 열이 앞의 두 열의 합이므로 세 벡터가 한 평면에 놓이고 부피는 0이다.
셀은 3차원 공간을 만들지 못한다. 원래 분율좌표를 유일하게 복원할 수 없다.
L_bad의 상은 z=0 평면이므로 z가 0이 아닌 실제 위치는 표현할 수 없고,
z=0 평면의 위치를 표현하는 분율좌표는 무한히 많다.
-->

# 7. 관련 문서

- [NumPy: 벡터·배열의 norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)
- [NumPy: cross product](https://numpy.org/doc/stable/reference/generated/numpy.cross.html)
- [NumPy: 연립방정식 solve](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)

[벡터 강의]({% link assets/lecture_notes/1_2_data_mse/data_mse_11_벡터연산기초.md %}) | [강의 목록]({% link _lectures/1_2_data_mse.md %}) | [행렬 강의]({% link assets/lecture_notes/1_2_data_mse/data_mse_12_행렬연산기초.md %})
