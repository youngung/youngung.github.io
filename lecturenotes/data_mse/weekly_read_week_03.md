---
layout: page
title: DATA MSE week 03
permalink:
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
3 (함수, class, module; **import** )
 - 목표
  + 함수와 클래스, 그리고 모듈의 이해
  + 함수를 만들어, 모듈화 시키고 CLI에서 실행할 수 있다.
 ## 수업 03-1
 - 함수란, 특정한 작업(task)를 수행하는 묶음.
    + basics
     ```def```로 정의하며, 재사용 가능하고(reuseable),
    입력(arguments), 출력(return)값을 가질 수 있습니다.
    입력과 출력이 없는 함수도 있어요.

    ```python
    def add(a, b):
        return a + b
    ```

    ```python
    def sayhi():
        print('Hi')
    ```
    + built-in functions
     A full list of built-in functions: [here](https://docs.python.org/3/library/functions.html)

 - class 란
    ```python
    class Atom:
        def __init__(self,name):
            self.name = name
        def add_density(self,density):
            self.density=density
        def add_structure(self,structure):
            self.structure=structure

    ## usage example
    myFe=Atom()
    myFe.add_density(7.87) #7.87g/cm^3
    myFe.add_structure('BCC')

    myAl=Atom()
    myAl.add_density(2.70)
    myAl.add_structure('FCC')
    ```

 - 여러 함수 만들어 보기
   + 위치 인자 (*args); tuple
   + 키워드 인자 (keyword arguments; **kwargs); dictionary 활용
    ```python
    def get_sum(*args):
        sum=0.
        for arg in args:
            sum=sum+arg
        return sum
    get_sum(1,2,3,4,5,6,7) #? what's going to be the correct answer?
    def introduce(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    introduce(name="Alice", age=25, country="Korea")
    ```
## 수업 03-2
 - CLI (command-line interface)
 - 모듈화 (modularization)
   + 프로그램을 기능별로 나뉘어 파일(모듈)로 분리
   + 코드 재사용성(reuseability) 향상, 유지보수 용이, 협업시 효율성 증가
   + 모듈(module)은 ```.py``` 파일을 가르킨다.
   + 패키지는 여러 모듈의 모임이다.
   + 라이브러리(library)는 모듈과 패키지의 모임.
 - 예시/실습
   + ex 01: 가장 간단한 모듈화
    ```python
    # 아래 모듈을 작성 후 mymodule.py로 저장하자.
    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b
    ```
    그 다음 아래를 활용해 mymodule을 불러와 보자.
    ```python
    import mymodel
    mymodule.add(3,4)
    mymodule.multiply(3,4)
    ```

   + ex 02: CLI에서 arguments 받기
    ```python
    # file: ex02.py
    import sys

    if __name__ == "__main__":
        print("Arguments:", sys.argv)
    ```
    Arguments의 역할을 이해하기 위해서 아래 실행

     - (Windows 환경 예시)
     ```sh
     c:\users\user\repo\mse> python ex02.py a b c 1 2 3
     ```
     - (MacOS/Linux 환경 예시)
     ```sh
     ~/repo/mse $ python ex02.py a b c 1 2 3
     ```

    실행 후 출력 결과 살펴보기



