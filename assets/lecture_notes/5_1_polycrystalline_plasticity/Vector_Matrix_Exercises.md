---
layout: distill
title: 벡터와 행렬 연습문제
description: 벡터와 행렬의 기본 연산 연습
target: 학부 고학년
permalink:
featured: true
prerequisite: 벡터와 행렬
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

# 1. 다음 두 벡터가 있다. 두 벡터간의 연산 결과를 답하시오.

$$
\boldsymbol a=\begin{bmatrix}2\\2\\-1\end{bmatrix}
$$

$$
\boldsymbol b=\begin{bmatrix}2\\-3\\1\end{bmatrix}
$$

## 1.1. $\boldsymbol a + \boldsymbol b$

<!-- 풀이와 해답: (4,-1,0)^T -->

## 1.2. $\boldsymbol a - \boldsymbol b$

<!-- 풀이와 해답: (0,5,-2)^T -->

## 1.3. $\boldsymbol a \cdot \boldsymbol b$

<!-- 풀이와 해답: -3 -->

## 1.4. $\boldsymbol b - \boldsymbol a$

<!-- 풀이와 해답: (0,-5,2)^T -->

## 1.5. $\boldsymbol a \otimes \boldsymbol b$

<!-- 풀이와 해답: [[4,-6,2],[4,-6,2],[-2,3,-1]] -->

## 1.6. $\boldsymbol b \otimes \boldsymbol a$

<!-- 풀이와 해답: [[4,4,-2],[-6,-6,3],[2,2,-1]] -->

## 1.7. $\boldsymbol b \times \boldsymbol a$

<!-- 풀이와 해답: (1,4,10)^T -->

## 1.8. $\boldsymbol a \times \boldsymbol b$

<!-- 풀이와 해답: (-1,-4,-10)^T -->


## 1.9. $|\boldsymbol a| |\boldsymbol b|$

<!-- 풀이와 해답: 3 sqrt(14) -->

## 1.10. $|\boldsymbol a\cdot \boldsymbol b|$

<!-- 풀이와 해답: 3 -->

# 2. 다음 두 행렬이 있다. 두 행렬간의 연산 결과를 답하시오.



$$
\boldsymbol A=\begin{bmatrix}
 1& 1& -1 \\
 3& 4& -4 \\
 3& 1&  2 \\
\end{bmatrix}
$$

$$
\boldsymbol B=\begin{bmatrix}
  1 &  1& -1 \\
 -1 & -2& -4 \\
 -2 &  2&  2\\
\end{bmatrix}
$$

## 2.1. $\boldsymbol A+ \boldsymbol B$

<!-- 풀이와 해답: [[2,2,-2],[2,2,-8],[1,3,4]] -->

## 2.2. $\boldsymbol A- \boldsymbol B$

<!-- 풀이와 해답: [[0,0,0],[4,6,0],[5,-1,0]] -->

## 2.3. $\boldsymbol B- \boldsymbol A$

<!-- 풀이와 해답: [[0,0,0],[-4,-6,0],[-5,1,0]] -->

## 2.4. $\boldsymbol A \cdot \boldsymbol B$

<!-- 풀이와 해답: [[2,-3,-7],[7,-13,-27],[-2,5,-3]] -->

## 2.5. $\boldsymbol B \cdot \boldsymbol A$

<!-- 풀이와 해답: [[1,4,-7],[-19,-13,1],[10,8,-2]] -->

## 2.6. $\boldsymbol A : \boldsymbol B$

<!-- 풀이와 해답: 같은 위치의 성분을 곱해 모두 더하면 8이다. -->

## 2.7. $\boldsymbol B : \boldsymbol A$

<!-- 풀이와 해답: double contraction은 이 경우 교환 가능하므로 8이다. -->
