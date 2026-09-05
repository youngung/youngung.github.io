---
layout: distill
title: 질량분율과 원자분율 변환
description: 합금 조성의 질량분율·원자분율 변환
target: 1학년 2학기
permalink:
featured: true
prerequisite: Python 함수, NumPy
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

# 1. 목표

- 무게비 원자비를 이해하고 이를 상호 호환할 수 있는 모듈을 만들 수 있다.

## 1.1. 수업 11-1 (무게비 원자비 변환)

- 무게비 (weight fraction)

  $$
  w_a=\frac{W_a}{W_a+W_b}\times 100 (wt.\%)
  $$

  $$
  W_a, W_b
  $$

  는 각각

  $$
  a
  $$

  원소와

  $$
  b
  $$

  원소의 질량 (혹은 무게).
  마찬가지로, 부피비는 다음과 같이 표현이 가능하겠다.

  $$
  f_a=\frac{V_a}{V_a+V_b}\times 100 (vol.\%)
  $$

  $$
  V_a, V_b
  $$

  는 각각

  $a$ 원소와 $b$ 원소의 부피

- 무게비 <-> 변환?

  - 원소 $a$의 무게는 밀도 $\rho_a$
    와 부피 $V_a$의 관계로 설명가능하다.

    $$
    \rho_a=\frac{W_a}{V_a}
    $$

    $$
    w_a=\frac{W_a}{W_a+W_b}\times 100 =\frac{\rho_aV_a}{\rho_aV_a+\rho_bV_b}\times 100
    $$

    $$
    \rightarrow w_a=\frac{1}{1+\frac{\rho_bV_b}{\rho_aV_a}}\times 100
    $$

    $$
    \rightarrow 1+\frac{\rho_bV_b}{\rho_aV_a}=\frac{100}{w_a}
    \rightarrow \frac{\rho_bV_b}{\rho_aV_a}=\frac{100}{w_a} -1
    $$

    $$
    \therefore
    \frac{V_b}{V_a}=(\frac{100}{w_a} -1)\frac{\rho_a}{\rho_b}
    $$

    마지막 관계식을 활용하여 부피비를 다시 표현하면

    $$
    f_a=\frac{V_a}{V_a+V_b}\times 100=\frac{1}{1+V_b/V_a}\times 100=\frac{1}{1+(\frac{100}{w_a} -1)\frac{\rho_a}{\rho_b}}\times 100
    $$

    따라서 각 원소의 밀도

    $$
    \rho_a,\rho_b
    $$

    그리고 무게비

    $$
    w_a [\%]
    $$

    를 알면 백분율 부피비를 구할 수 있다.

    $$
    a
    $$

    원소와

    $$
    b
    $$

    원소의 자리르 바꾸면

    $$
    f_b=\frac{1}{1+(\frac{100}{w_b} -1)\frac{\rho_b}{\rho_a}}\times 100
    $$

    ```python
    def convert_a(wa,rhoa,rhob): ## get f_a
    	return 1/(1+(100/w_a-1)*(rhoa/rhob))*100
    def convert_b(wb,rhoa,rhob): ## get f_a
    	return 1/(1+(100/w_b-1)*(rhob/rhoa))*100
    ```

- 유용한 패키지 [periodic table](https://pypi.org/project/periodictable/),
  [Github page](https://github.com/python-periodictable/periodictable)
  [Documentation](https://periodictable.readthedocs.io/en/latest/)

  ```bash
  c:\users\user> pip install periodictable
  ```

- 예제
  한 철강 제품의 무게비가 다음과 같았다.

  $$
  Fe:C = 0.99: 0.01
  $$

  철의 부피비,

  $$
  v_{Fe}
  $$

  는 얼마인가?

  ```python

  ```

# 2. CLI용 모듈 만들기

# 쉬운 연습 문제

## 문제 1

질량이 30 g과 70 g인 두 성분의 전체 질량을 구하라.

<!--
풀이와 해답:
100 g이다.
-->

## 문제 2

전체 질량 100 g 중 A가 30 g이면 A의 질량분율을 구하라.

<!--
풀이와 해답:
0.30, 즉 30 wt.%이다.
-->

## 문제 3

원자분율 계산에서 각 성분의 질량을 나누어야 하는 물리량은 무엇인가?

<!--
풀이와 해답:
각 성분의 원자량 또는 몰질량이다.
-->
