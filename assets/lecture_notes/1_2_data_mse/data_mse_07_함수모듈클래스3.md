---
layout: distill
title: 모듈과 명령행 프로그램
description: Python 모듈, import와 argparse를 이용한 CLI 기초
target: 1학년 2학기
permalink:
featured: true
prerequisite: 함수 기초
toc:
  sidebar: left
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

- [1. 학습 목표](#1-학습-목표)
- [2. 모듈(module)이란](#2-모듈module이란)
- [3. 간단한 모듈 만들기](#3-간단한-모듈-만들기)
  - [3.1. calculator.py](#31-calculatorpy)
  - [3.2. main.py](#32-mainpy)
- [4. import 방법](#4-import-방법)
- [5. 모듈을 찾는 위치](#5-모듈을-찾는-위치)
- [6. 메인 프로그램과 ```__name__```](#6-메인-프로그램과-__name__)
- [7. 명령행 인자](#7-명령행-인자)
- [8. argparse 기초](#8-argparse-기초)
  - [8.1. 위치 인자 하나 받기](#81-위치-인자-하나-받기)
  - [8.2. 선택 인자 추가하기](#82-선택-인자-추가하기)
- [9. 재료공학 CLI 예제](#9-재료공학-cli-예제)
- [10. 오류를 만났을 때](#10-오류를-만났을-때)
- [11. 연습 문제](#11-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- Python 모듈과 패키지의 의미를 설명할 수 있다.
- 직접 만든 모듈을 다른 파일에서 불러올 수 있다.
- ```if __name__ == "__main__"```의 역할을 설명할 수 있다.
- <code>argparse</code>로 간단한 명령행 프로그램을 만들 수 있다.
- 입력값을 받아 재료 물성을 계산하는 프로그램을 실행할 수 있다.

# 2. 모듈(module)이란

모듈(module)은 Python 코드를 저장한 <code>.py</code> 파일이다. 함수와 클래스를
모듈에 저장하면 다른 프로그램에서 다시 사용할 수 있다.

- 모듈: 하나의 <code>.py</code> 파일
- 패키지(package): 관련된 여러 모듈을 묶은 것
- 라이브러리(library): 재사용할 수 있도록 제공되는 모듈과 패키지의 모음 (math, scipy, numpy, pandas 등)
- CLI(command-line interface): 터미널에서 명령어로 사용하는 프로그램

모듈로 나누면 긴 프로그램을 기능별로 정리하고 같은 코드를 여러 프로그램에서 사용할 수 있다.

# 3. 간단한 모듈 만들기

같은 폴더에 다음 두 파일을 만든다.

## 3.1. calculator.py

~~~python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def power(base, exponent):
    return base**exponent
~~~

## 3.2. main.py

~~~python
import calculator


print(calculator.add(3, 4))
print(calculator.multiply(3, 4))
print(calculator.power(3, 4))
~~~

터미널에서 <code>main.py</code>가 있는 폴더로 이동한 뒤 실행한다.

~~~sh
python main.py
~~~

예상 출력은 7, 12, 81이다.

모듈 이름과 호출 이름이 모두 <code>calculator</code>로 같은지 확인한다. 파일 이름이
<code>calculator.py</code>이면 <code>import calculator</code>라고 써야 한다.

# 4. import 방법

같은 모듈을 여러 방식으로 불러올 수 있다.

~~~python
import math

print(math.sqrt(9))
~~~

~~~python
from math import sqrt

print(sqrt(9))
~~~

~~~python
import math as m

print(m.sqrt(9))
~~~

처음에는 <code>import math</code>처럼 모듈 이름을 남기는 방식이 함수의 출처를
알아보기 쉽다. <code>from module import *</code>는 이름 충돌이 생길 수 있으므로
사용하지 않는 편이 좋다.

# 5. 모듈을 찾는 위치

직접 만든 모듈을 불러오지 못한다면 다음을 확인한다.

1. 파일 이름이 정확히 <code>calculator.py</code>인가?
2. <code>main.py</code>와 <code>calculator.py</code>가 같은 폴더에 있는가?
3. 터미널의 현재 폴더가 두 파일이 있는 위치인가?
4. 다른 파일이나 폴더가 같은 이름을 사용하고 있지 않은가?

현재 폴더는 터미널에서 다음 명령으로 확인할 수 있다.

~~~sh
pwd # pring working directory
~~~

Windows 명령 프롬프트에서는 다음 명령을 사용할 수 있다.

~~~bat
REM current directory
cd
~~~

# 6. 메인 프로그램과 ```__name__```

다음 코드를 <code>example.py</code>에 저장하자.

~~~python
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("student"))
~~~

<code>python example.py</code>로 직접 실행하면 조건문 안의 코드가 실행된다.
다른 파일에서 <code>import example</code>로 불러오면 조건문 안은 실행되지 않는다.

따라서 함수와 클래스를 정의하는 부분과 프로그램을 직접 실행하는 부분을 분리할 수 있다.

# 7. 명령행 인자

명령행 인자(command-line argument)는 프로그램을 실행할 때 함께 전달하는 값이다.

다음 코드를 <code>show_args.py</code>에 저장한다.

~~~python
import sys


if __name__ == "__main__":
    print(sys.argv)
~~~

다음과 같이 실행해 보자.

~~~sh
python show_args.py aluminum 27
~~~

<code>sys.argv</code>의 첫 번째 원소는 파일 이름이고 그 뒤에 입력값들이 **문자열**로 저장된다.
간단히 확인할 때는 유용하지만 입력값의 의미와 자료형을 관리하려면
<code>argparse</code>가 더 편리하다.

# 8. argparse 기초

## 8.1. 위치 인자 하나 받기

다음 코드를 <code>square.py</code>에 저장한다.

~~~python
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Calculate the square of an integer."
    )
    parser.add_argument(
        "x",
        type=int,
        help="integer to be squared",
    )
    args = parser.parse_args()

    print(args.x**2)


if __name__ == "__main__":
    main()
~~~

도움말과 계산은 각각 다음처럼 실행한다.

~~~sh
python square.py --help
python square.py 3
~~~

두 번째 명령은 9를 출력한다. <code>type=int</code>를 지정했기 때문에 입력 문자열을
정수로 변환한다.

## 8.2. 선택 인자 추가하기

~~~python
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=float)
    parser.add_argument("y", type=float)
    parser.add_argument(
        "--operation",
        choices=["add", "multiply"],
        default="add",
    )
    args = parser.parse_args()

    if args.operation == "add":
        result = args.x + args.y
    else:
        result = args.x * args.y

    print(result)


if __name__ == "__main__":
    main()
~~~

~~~sh
python calculate.py 3 4
python calculate.py 3 4 --operation multiply
~~~

첫 명령은 기본 연산인 덧셈 결과 7을, 두 번째 명령은 곱셈 결과 12를 출력한다.

# 9. 재료공학 CLI 예제

질량과 부피를 입력받아 밀도를 계산하는 프로그램을 만들어 보자.
다음 코드를 <code>density_cli.py</code>에 저장한다.

~~~python
import argparse

def density(mass_g, volume_cm3):
    if volume_cm3 <= 0:
        raise ValueError("volume must be positive")

    return mass_g / volume_cm3

def main():
    parser = argparse.ArgumentParser(
        description="Calculate density."
    )
    parser.add_argument(
        "mass",
        type=float,
        help="mass in g",
    )
    parser.add_argument(
        "volume",
        type=float,
        help="volume in cm^3",
    )
    args = parser.parse_args()

    rho = density(args.mass, args.volume)
    print(f"density = {rho:.3f} g/cm^3")


if __name__ == "__main__":
    main()
~~~

다음 명령을 실행하면 밀도 2.700 g/cm³가 출력된다.

~~~sh
python density_cli.py 27 10
~~~

함수 <code>density</code>는 계산만 담당하고 <code>main</code>은 입력 해석과 출력을
담당한다. 이렇게 역할을 분리하면 계산 함수를 다른 모듈에서도 재사용하기 쉽다.

# 10. 오류를 만났을 때

- <code>ModuleNotFoundError</code>: 파일 이름과 현재 폴더를 확인한다.
- <code>AttributeError</code>: 모듈에 해당 함수가 정의되어 있는지 확인한다.
- <code>NameError</code>: 변수 이름의 철자가 앞뒤에서 같은지 확인한다.
- <code>TypeError</code>: 인자의 개수와 자료형을 확인한다.
- <code>IndentationError</code>: 조건문과 함수 본문의 들여쓰기를 확인한다.

오류 메시지의 마지막 줄부터 읽으면 오류 종류와 원인을 찾기 쉽다.

# 11. 연습 문제

## 문제 1

Python 모듈 파일의 확장자를 쓰시오.

<!--
풀이와 해답:
.py이다.
-->

## 문제 2

<code>tools.py</code>라는 모듈을 불러오는 문장을 쓰시오.

<!--
풀이와 해답:
import tools
-->

## 문제 3

<code>calculator</code> 모듈의 <code>add</code> 함수에 2와 5를 전달하는 표현을 쓰시오.

<!--
풀이와 해답:
calculator.add(2, 5)
-->

## 문제 4

명령행 프로그램의 사용법을 확인할 때 사용하는 기본 선택 사항은 무엇인가?

<!--
풀이와 해답:
--help이다.
-->

## 문제 5

<code>argparse</code>에서 입력값을 정수로 변환하도록 지정하는 표현은 무엇인가?

<!--
풀이와 해답:
type=int이다.
-->

## 문제 6

다음 명령에서 명령행 인자 두 개를 쓰시오.

~~~sh
python density_cli.py 27 10
~~~

<!--
풀이와 해답:
27과 10이다. 각각 질량과 부피로 전달된다.
-->
