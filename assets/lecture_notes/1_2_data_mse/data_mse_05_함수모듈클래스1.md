---
layout: distill
title: 데이터 재료과학 (제 5강)
description: 함수
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
- [2. 함수란](#2-함수란)
- [3. 모듈(module)과 import](#3-모듈module과-import)
- [4. Built-in functions (no import / no declaration required)](#4-built-in-functions-no-import--no-declaration-required)
- [5. 가변 인자 (\*args)](#5-가변-인자-args)
- [6. 키워드 가변인자 (\*\*kwargs)](#6-키워드-가변인자-kwargs)
- [7. 예시](#7-예시)
  - [7.1. 주어진 모든 가변인자를 순서대로 곱하여 출력하는 함수 만들기](#71-주어진-모든-가변인자를-순서대로-곱하여-출력하는-함수-만들기)
  - [7.2. 주어진 모든 가변인자의 개수를 출력하고, 그 가변인자의 총합과 평균을 구하는 함수 만들기](#72-주어진-모든-가변인자의-개수를-출력하고-그-가변인자의-총합과-평균을-구하는-함수-만들기)

# 1. 목표
 - 함수와 클래스, 그리고 모듈의 이해
 - 함수를 만들어, 모듈화 시키고 CLI에서 실행할 수 있다.

# 2. 함수란

- 특정한 작업(task)를 수행하는 묶음.

- basics:
  `def`로 정의하며, **재사용** 가능하고(reuseable),
  입력(arguments), 출력(return)값을 가질 수 있다.
  입력과 출력이 없는 함수도 있다.

- 예시1: 기초 형태 (template)

```python
def add(a, b): #함수의 이름이 'add', 입력은 a와 b
   return a + b # 출력은 a+b
```

- 예시2

```python
def sayhi(): # 함수의 이름이 'sayhi', 입력과 출력 없음
   print('Hi')
```

- 예시3

```python
def func(a=3,b=5): # 함수의 이름이 'func', 입력 a와 b의 default가 있음.
  """
  a and b are the two arguments of this function
  and this function calculates a+b, then return the result as output
  """
  return a+b
```

아래 실행해보자
```python
## default value 활용됨
print(func())

print(func(3,5))

print(func(5,3))

print(func(a=3,b=6))

print(func(b=6,a=3))

print(func.__doc__) ## docstring 출력
print(help(func))
print(help(help))
```

- 예시 4: 아래 함수를 정의하면 에러가 발생한다. 에러를 읽어보고 이해해보자.

```python
def f(a=3,b=5,c,d):
   print(a+b)
   print(c+d)
   return a*b*c*d
```
# 3. 모듈(module)과 import

- 위 함수 중 하나를 모듈로 만들고 import 해보기

- 한 재료의 부피와 질량을 측정해 밀도를 계산하려고 한다. 각 측정값에 오차가 있어, 측정을
 여러번 되풀이 한 다음 평균 값을 계산해 밀도를 구하려고 한다. 아래의 예시를 직접 작성해보고
 이를 활용해보자.

  - 'calc_dens.py` 모듈 작성
  ```python
  # 이 코드를 파일명 `calc_dens.py`로 작성하여 저장하자.
  def calc_dens(mass, volume):
    """
    질량은 g 단위로, 부피는 mm^3으로
    """
    density = mass / volume
    return density
  ```

  - 'main.py' 모듈 작성
  ``` python
  # 이 코드를 `main.py`로 작성하여 저장하자.

  ## 밀도 계산 프로그램

  ## Raw data
  mass=[6.01, 6.05, 5.93, 6.03]
  vol=[3.11, 3.20, 3.09, 3.15]

  import calc_dens ## calc_dens.py 모듈을 import

  dens=[] ## list 자료 생성
  for i in range(len(mass)):
    val=calc_dens(mass=mass[i],volume=vol[i]) ## calc_dens.py 모듈 내의 함수
    dens.append(val) ## list 자료에 값 저장

  average=0.
  for i in range(len(dens)):
    average=average+dens[i]
  average=average/len(dens)
  ```

  - 위 생성된 모듈을 활용해서 표준 편차 구해보기.
   $std(v_i)=\sum_i^n (\bar{v} - v_i)^2$

  - 측정된 질량에서의 표준 편차는 얼마인가?
  - 측정된 부피내의 표준 편차는 얼마인가?
  - 밀도의 표준 편차는 얼마인가?
  - 표준편차를 계산하는 함수를 만들어서 활용해보자.

# 4. Built-in functions (no import / no declaration required)

- 특징
  - built-in 함수는 파이썬이 기본적으로 제공하는 함수
  - 별도의 **import** 없이 언제든 바로 사용 가능; 예 (print, help, ...)
  - 약 70여 개의 built-in 함수: A full list of built-in functions: [here](https://docs.python.org/3/library/functions.html)

- 입력(input)과 출력(output) I/O
  - ```print``` 함수
  - ```input``` 함수

- 출력 예시
  ```python
  # 1. 단순 문자열 출력
  print("안녕하세요, 파이썬!")

  # 2. 숫자 출력 및 연산 결과 출력
  print(2026)
  print(10 + 20)

  # 3. 여러 값 동시에 출력 (쉼표로 구분하면 한 칸씩 띄어서 출력돼요)
  print("올해는", 2026, "년입니다.")
  ```

- 입력 예시
  ```python
  # 1. 입력 받기
  age_str = input("당신의 현재 나이를 입력하세요: ")

  # 2. 형변환 (문자열로 들어온 나이를 계산할 수 있게 정수(int)로 바꿔줘요)
  age = int(age_str)

  # 3. 계산하기
  next_year_age = age + 1

  # 4. 결과 출력하기
  print("내년에 당신은", next_year_age, "살이 됩니다!")
  ```

# 5. 가변 인자 (*args)

```python
def add_all(*args):
    # args는 입력된 모든 숫자가 담긴 튜플 형태. 예: (1, 2, 3)
    return sum(args)

# 인자의 개수를 자유롭게 넣을 수 있습니다.
print(add_all(1, 2))        # 결과: 3
print(add_all(1, 2, 3, 4))  # 결과: 10
```

# 6. 키워드 가변인자 (**kwargs)
```python
def print_info(**kwargs):
    # kwargs는 dictionary 형태. 예: {'name': 'Alice', 'age': 30}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 키워드 형태로 인자를 자유롭게 넘깁니다.
print_info(name="Alice", age=30, role="Professor")
# 출력:
# name: Alice
# age: 30
# role: Professor
```

# 7. 예시

## 7.1. 주어진 모든 가변인자를 순서대로 곱하여 출력하는 함수 만들기

## 7.2. 주어진 모든 가변인자의 개수를 출력하고, 그 가변인자의 총합과 평균을 구하는 함수 만들기