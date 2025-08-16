---
layout: page
title: DATA MSE week 01
permalink:
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
# Week 1 (개요, 설치, 변수 및 연산자) -
## 수업 01-1
 - 목표
   + 수업 개요 및 진행, 규칙 설명
 - Orientation
   + 수업 개론
   + 수업 내용 소개
   + 수업 진행 방식
 - 개념 설명
 - 실습
   + 반드시 스스로 실습하기 원칙
   + 물에 몸을 담그지 않고 수영을 배울 수 없다.
   + 스스로 실습하지 않고서는 배울 수 없음.
     * 반드시 개인용 컴퓨터 필요 - 실습
     * 없다면 학교에서 대여
   + 친구/가족에게 빌리거나, 구매 필요함.
   + 그외 기타 사정으로 수업을 듣고 싶으나 노트북 준비가 어렵다면
          교수에게 상담 요청하시오.
 - 평가 방법
   + 출석과 결석
   + 중간/기말 평가
 - 과제
   * 파이썬 설치 및 환경 설정 완성 (Python 3.12, JuPyter, VS code, pip)
## 수업 01-2
 - 오늘 목표
   * 파이썬 설치 및 환경 설정 완성 (Python 3.12, JuPyter, VS code, pip)
   * VS code에서 JuPyter 셋업 & 구동할 수 있다.
   * Hello, world
   * 실습 예시를 모두 이해하고 풀 수 있다.
   * 'Traceback'이해하고 대처할 수 있다.
 - 수업 내용
   * Jupyter notebook 간단한 키조작 가능
   * 셀(cell) 만들기, 지우기, 입력, 이동(navigation)
      + 코드 셀
      + Markdown 셀
   * 주석(comment)과 명령문(statement) 구분하기
   * 변수 선언과 자료형 (```int```, ```float```, ```str```, ```bool```) 이해하기
   * 연산자 이해하기
      + 산술 연산자 (더하기, 빼기, 곱하기, 나누기, 지수, 나머지, 몫 ... )
      + 비교 연산자 (==, !=, <, >, >=, <=, is, is not, in, not in)
      + 논리 연산자 (and or)
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

        # 3. 포함 여부
        text = "Fe2O3"
        print("F" in text)      # True  ('a'가 문자열에 포함됨)
        print("O" not in text)  # True  ('z'가 문자열에 없음)

        numbers = [1, 2, 3]
        print(2 in numbers)     # True  (리스트에 2가 포함됨)
        print(5 not in numbers) # True  (리스트에 5가 없음)
       ```
 - 실습 예시
   * pip 활용하여 NumPy 설치하고, package directory 찾기.
   * 인치(inch_leng) 길이를 센치미터(cmeter_leng)로 바꿔서 계산. 센치 미터를 인치로
     계산해보기.
     + 25 cm는 몇 inch인가?
     + 170 cm는 몇 inch인가?
     + 15 inch에다가 50 cm를 더하면 총 길이가 얼마인가?
   * 섭씨(cent_deg)를 화씨(fahr_deg)로, 그리고 화씨(fahr_deg)를 섭씨(cent_deg)로 계산해보기.
        ```python
        ## 예시
        c = float(input("섭씨 온도: "))
        f = c * 9/5 + 32
        print(f"{c:.2f}C= {f:.2f}F")
        ```
     + 섭씨 25도는 화씨로 몇도인가?
     + 화씨 35도는 섭씨 몇도인가?
     + 화씨 20도에 섭씨 -5도를 더하면 화씨와 섭씨로 각각 몇도인가?
   * 한쪽이 30 cm 다른 한변이 40 inch라면 총 면적은 어떻게 되나?
   * 세륨의 평균 원자량 계산 (Fundamentals of Materials Science and Engineering, Calister 예제 2.1)
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
