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

# 목표
 - Python 모듈을 이해하고 만들 수 있다.

# 개념

- CLI (command-line interface)
- 모듈화 (modularization)
  - 프로그램을 기능별로 나뉘어 파일(모듈)로 분리
  - 코드 재사용성(reuseability) 향상, 유지보수 용이, 협업시 효율성 증가
  - 모듈(module)은 `.py` 파일을 가르킨다.
  - 패키지는 여러 모듈의 모임이다.
  - 라이브러리(library)는 모듈과 패키지의 모임.

# 실습

## ex 01: 간단한 모듈 만들기 (더하기 곱하기)

1. 모듈 작성

```python
# 아래 모듈을 작성 후 mymodule.py로 저장하자.
def add(valuea, valueb):
    return valuea + valueb

def multiply(valuea, valueb):
    return valuea * valueb

def power(valuea, valueb):
    return valuea ** valueb
```

2. 그 다음 아래를 활용해 mymodule을 불러와 보자.

```python
import mymodel
mymodule.add(3,4)
mymodule.multiply(3,4)
mymodule.power(3,4)
```

3. etc

- 작성된 모듈이 저장된 위치가 중요하다!
- 개개인이 활용하는 시스템:computer:의 환경변수 (windows의 경우)에 의해 행동이 달라질
  수 있다.
- Linux/macOS의 경우에는 활용하는 shell의 닷 파일 (.sh, .bash, .zsh 등등)에서
  지정된 $PATH 등의 변수에 의해 달라질 수 있다.

## ex 02: CLI에서 arguments 받기

- 1. 기초 모듈 작성

  ```python
  # file: ex02.py
  import sys
  if __name__ == "__main__":
    print("Arguments:", sys.argv)
  ```

- 2. Arguments의 역할을 이해하기 위해서 아래 실행

  - 2-1. Windows 환경

  ```sh
  c:\users\user\repo\mse> python ex02.py a b c 1 23
  ```

  - 2-2. MacOS/Linux 환경

  ```sh
  ~/repo/mse $ python ex02.py a b c 1 2 3
  ```

- 3. 실행 후 출력 결과 살펴보기

- 4. 더 상세한 argument parsing

  - 4-1. Argument parse 읽을 거리

  * [Argparse](https://docs.python.org/ko/3.7/library/argparse.html) 활용
  * [Argparse 자습서](https://docs.python.org/ko/3.7/howto/argparse.html#id1)

  - 4-2. 단계별로 작성해보기.

  * 4-2-1. 간단한 작동

    아래를 myprogram.py 파일(모듈)로 작성하여 저장하자.

    ```python
    import argparse
    if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.parse_args()
    ```

    그 다음 CLI에서 아래와 같이 명령문을 쳐보자.

    ```batch
    c:/users/user> python myprogram.py --help
    usage: main.py [-h]

    options:
    -h, --help  show this help message and exit
    ```

  * 4-2-2. positional argument

    다음으로 myprogram.py을 열어서 다음과 같이 수정해봅시다.
    `x` argument를 추가하였고, $x^2$을 출력합니다.

    ```python
    import argparse
    if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="the base")
    args=parser.parse_args()

    print(args.x**2)
    ```

  * 4-2-3. `--help` 기능

    아래와 같이 명령문을 입력하면 ...

    ```dos
    c:\users\user> python myprogram.py --help
    ```

    다음과 같이 출력되었나? 출력된 결과물을 살펴보자.

    ```dos
    usage: main.py [-h] x

    positional arguments:
    x           the base

    options:
    -h, --help  show this help message and exit

    ```

  * 4-2-4. 변경된 영향 확인

    명령어를 바꿔 다음과 같이 입력해보자.

    ```sh
    c:\users\user> python myprogram.py 3
    given x: 3
    x^2: 9
    ```

  * 4-2-5. Additional options

    a. 다음으로 myprogram.py을 열어서 다음과 같이 수정해봅시다.

    ```python
    import argparse

    def add(x,y):
      return x+y

    if __name__=='__main__':
      parser=argparse.ArgumentParser()
      parser.add_argument('x',type=int,help='the 1st base')
      parser.add_argument('y',type=int,help='the 2nd base')
      parser.add_argument('--myname',type=str,help='My Name')
      args=parser.parse_args()

      print('Myname:',args.myname)
      print('given x:', args.x)
      print('given y:', args.y)
      multiplied=add(args.x,args.y)
      print('x times y:', multiplie)
    ```

    b. CLI에서 아래를 실행하면

    ```dos
    c:\users\user> python main.py --help
    ```

    다음과 같이 `positional arguments`와 `options`이 출력된다.

    ```dos
    usage: main.py [-h] [--myname MYNAME] x y

    positional arguments:
    x                the 1st base
    y                the 2nd base

    options:
    -h, --help       show this help message and exit
    --myname MYNAME  My Name
    ```

    `--myname`옵션의 경우 `MYNAME`이라는 입력이 필요함을 알 수 있다.

    c. 실행해보자.

    ```dos
    c:\users\user> python main.py 3 4 --myname mike
    Myname: mike
    given x: 3
    given y: 4
    x times y: 7
    ```

# 예제 (take-home)

- 주어진 정수에 대한 구구단을 출력하는 CLI용 프로그램 만들어 보자.