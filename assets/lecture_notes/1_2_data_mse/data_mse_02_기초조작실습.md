---
layout: distill
title: 데이터 재료과학 (제 2강)
description: 데이터 분석/해석 및 시각화(그래프) 등 기초 컴퓨터 활용 능력
target: 1학년 2학기
permalink:
featured: true
prerequisite: 재료공학개론1
# toc:
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
- [2. Python 환경 확인](#2-python-환경-확인)
  - [2.1. 파이썬](#21-파이썬)
  - [2.2. VS code에서 JuPyter 셋업 \& 구동되어 있는가?](#22-vs-code에서-jupyter-셋업--구동되어-있는가)
  - [2.3 CLI (command line interface 기초)](#23-cli-command-line-interface-기초)
- [3. 모듈 만들기 및 실습](#3-모듈-만들기-및-실습)
- [4. 간단한 조작 실습](#4-간단한-조작-실습)
- [5. 변수와 연산자](#5-변수와-연산자)
- [6. 예시](#6-예시)
  - [6.1. 실습 예시 2-1](#61-실습-예시-2-1)
  - [6.2. 실습 예시 2-2](#62-실습-예시-2-2)
  - [6.3. 실습 예시 2-3](#63-실습-예시-2-3)
  - [6.4. 실습 예시 2-4](#64-실습-예시-2-4)


# 1. 목표
- 원활한 강의 위한 선행 조건이 만족 되었는가?
  - Python 설치 완료?
  - Internet 환경 세팅 완료?
  - VS code 설치 완료?

# 2. Python 환경 확인

  ## 2.1. 파이썬
   - 파이썬 설치 및 환경 설정 완성 (Python 3.12, [JuPyter](https://jupyter.org), [VS code](https://code.visualstudio.com), pip)이 되어 있고, terminal에서 다음과 같이 Python 환경 실행 가능한가?

   - Windows 예시

    ```batch
    Microsoft Windows [Version 10.0.26200.8655]
    (c) Microsoft Corporation. All rights reserved.

    C:\Users\Youngung> python
    Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

   - MacOS 예시
    ```terminal
    Youngungs-MacBook-Pro➜  ~  ᐅ  python
    Python 3.12.2 (main, Mar 29 2024, 06:39:27)   [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

  ## 2.2. VS code에서 JuPyter 셋업 & 구동되어 있는가?
   * 몇몇 유용한 extension을 설치하면 더욱 도움이 된다.

  ## 2.3 CLI (command line interface 기초)
   * https://www.youtube.com/watch?v=hNdAQQeqkYU

# 3. 모듈 만들기 및 실습

- Hello, world 실습. 아래를 작성하여 "hello.py" 모듈 (파일)로 저장하기
  ```python
  print('Hello, world')
  ```
- Module 실행
  ```batch
  C:\Users\Youngung> python hello.py
  Hello, world
  ```

- 'Traceback'이해하고 대처할 수 있다: 실습간에 예상했던 대로 결과가 나오지 않고, 예를 들어
 아래와 같은 에러 메시지 직접 읽고 대처할 수 있도록 노력 필요.

 에러 메시지 1.
 ```batch
  Traceback (most recent call last):
    File "/Users/youngung/repo/lectures/1_2_data_mse/ex/01_Hello/hello.py", line 1, in <module>
      xprint('Hello, world')
      ^^^^^^
  NameError: name 'xprint' is not defined. Did you mean: 'print'?
 ```

 에러 메시지 2.
 ```txt
/Users/youngung/.pyenv/versions/3.12.2/bin/python: can't open file '/Users/youngung/repo/youngung.github.io/mdim.py': [Errno 2] No such file or directory
  ```

# 4. 간단한 조작 실습

- JuPyter notebook 간단한 키조작 가능

- 셀(cell) 만들기, 지우기, 입력, 이동(navigation)
  - 코드 셀
  - markdown 셀
- 주석(comment)과 명령문(statement) 구분하기
  ```python
  print('Hello, world')
  # print('I am fine')
  print('What did you say?')
  ```

# 5. 변수와 연산자
- 변수 선언과 자료형 (`int`, `float`, `str`, `bool`) 이해하기
   - integer
   - float
   - str
   - bool
- 연산자(operator) 이해하기
  - 산술 연산자 (더하기, 빼기, 곱하기, 나누기, 지수, 나머지, 몫 ... )
  - 비교 연산자 (==, !=, <, >, >=, <=, is, is not, in, not in)
  - 논리 연산자 (and, or, not, ...)
    ```python
    # 1. 값 비교
    print(5 == 5)       # True (값이 같음)
    print(5 != 3)       # True (값이 다름)
    print(7 > 2)        # True (7이 2보다 큼)
    print(3 < 7)        # True (3이 7보다 작음)
    print(5 >= 5)       # True (5가 5보다 크거나 같음)
    print(4 <= 6)       # True (4가 6보다 작거나 같음)

    # 2. 객체 동일성 비교
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print(a == b)       # True  (값이 같음)
    print(a is b)       # False (메모리 주소 다름)
    print(a is c)       # True  (같은 객체)
    print(a is not b)   # True  (다른 객체)

    # 3. 한 문자(character)가 문자열에 포함되었는지 확인
    text = "Fe2O3"
    print("F" in text)      # True  ('F'가 문자열에 포함됨)
    print("O" not in text)  # True  ('O'가 문자열에 없음)

    numbers = [1, 2, 3]
    print(2 in numbers)     # True  (리스트에 2가 포함됨)
    print(5 not in numbers) # True  (리스트에 5가 없음)
    ```

# 6. 예시

## 6.1. 실습 예시 2-1

- [pip](https://pypi.org/project/pip/) 활용하여 아래 패키지 설치
  - [NumPy](https://numpy.org)
  - [SciPy](https://scipy.org)
  - [matplotlib](https://matplotlib.org)
  - [JuPyter](https://jupyter.org)
- 위 package가 설치된 directory 찾아 보기
- (Windows) 환경변수 살펴보기
- (Linux/macOS), zsh, bash 등 dotfile 살펴보기

## 6.2. 실습 예시 2-2

- 인치(inch_leng) 길이를 센치미터(cmeter_leng)로 바꿔서 계산. 센치 미터를 인치로
  계산해보기.

- 25 cm는 몇 inch인가?

$$25 \text{ cm} \times \frac{0.393 \text{ inch}}{1 \text{ cm}}=25 \text{ cm} \times \frac{0.393 \bcancel{\text{ ch}}}{1 \bcancel{\text{cm}}}$$

$$=25 \text{ cm} \times 0.393= 9.825 \text{ cm}.$$

- 알고리즘 - 규칙성 찾기:  (in 출력값) = (cm 입력값 ) $\times$ 0.393

- 170 cm는 몇 inch인가?

- 15 inch에다가 50 cm를 더하면 총 길이가 얼마인가?

- 한쪽이 30 cm 다른 한변이 40 inch라면 총 면적은 어떻게 되나?

## 6.3. 실습 예시 2-3

- 각도 degree 를 radian으로 바꾸기

{% tabs ex3-1 %}

{% tab ex3-1 30도를 라디안으? %}

```python
deg2rad=3.141592/180.
angle_in_degree = 30 ##
angle_in_radian = angle_in_degree * deg2rad
```

{% endtab %}

{% tab ex3-1 0.5 radian을 각도로? %}

```python
rad2deg=180/3.141592
angle_in_radian = 0.5 ##
angle_in_angle = angle_in_radian * rad2deg2
```

{% endtab %}
{% endtabs %}

```python
## 예시
c = float(input("섭씨 온도: "))
f = c * 9/5 + 32
print(f"{c:.2f}C= {f:.2f}F")
```

- 섭씨 25도는 화씨로 몇도인가?

- 화씨 35도는 섭씨 몇도인가?

- 화씨 20도에 섭씨 -5도를 더하면 화씨와 섭씨로 각각 몇도인가?

## 6.4. 실습 예시 2-4

- 세륨의 평균 원자량 계산 (Fundamentals of Materials Science and Engineering, Calister 예제 2.1)

  ```python
  #세륨의 동위원소는 4가지 존재한다:
  # 각 동위원소의 분율은 아래와 같다.
  Ce136_f =  0.185  #[%]
  Ce138_f =  0.251  #[%]
  Ce140_f = 88.450  #[%]
  Ce142_f = 11.114  #[%]
  # 각 동위원소의 원자량은 아래와 같다.
  Ce136_w = 135.907 #[amu.]
  Ce138_w = 137.906 #[amu.]
  Ce140_w = 139.905 #[amu.]
  Ce142_w = 141.909 #[amu.]

  # 세륨의 평균 원자량은 얼마인가?

  ```

  가상의 원소 M의 평균 원자량 구하는 방법

  $$
  \bar{A}_M=\sum_if_{i_M}A_{i_M}
  $$

  단순 평균이라면...

  $$\frac{w^{^{136}Ce}+w^{^{138}Ce}+w^{^{140}Ce}+w^{^{142}Ce}}{4}$$

  로 구했겠지만, 서로 다른량이 존재하므로 주어진 분율을 활용해야겠다. 즉

  $$\frac{w^{^{136}Ce}f^{^{136}Ce}+w^{^{138}Ce}f^{^{138}Ce}+w^{^{140}Ce}f^{^{140}Ce}+w^{^{142}Ce}f^{^{142}Ce}}{f^{^{136}Ce}+f^{^{138}Ce}+f^{^{140}Ce}+f^{^{142}Ce}}$$
