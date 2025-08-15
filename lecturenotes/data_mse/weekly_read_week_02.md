---
layout: page
title: DATA MSE week 02
permalink:
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
2 (자료구조, 제어, 반복)
 - 목표
  + List, Tuple, Dictionary, set
  + 조건문과 (conditions), 반복문 (loop) 이해
## 수업 02-1
 - list, tuple, dictionary 생성/수정/조회
  + List
     * 특징:
       + 수정 가능(mutable): 추가, 삭제, 변경 가능
       + 중복 허용
       + 순서 있음 (ordered)
       + 여러 자료형 혼합해서 저장 가능
     * 리스트 생성 - 대괄호 사용 ```[]```
       ```python
       elements = ["H", "He", "Li", "Be"]
       ```
     * 요소 접근 (인덱싱; indexing); 0에서 부터 시작
       ```python
       print(elements[0])   # H
       ```
     * 요소 변경
       ```python
       elements[1] = "Helium"
       print(elements)     #elements = ["H", "Helium", "Li", "Be"]
       ```
     * 요소 추가 / 삭제
       ```python
       elements.append("B")   #elements = ["H", "Helium", "Li", "Be", "B"]
       elements.remove("Li")  #elements = ["H", "Helium", "Be", "B"]
       ```
     * 중복 허용
       ```python
       elements = ['H','He','H']
       print(elements)
       ```
     * 여러 자료형 혼합
       ```python
       myList=['H',203,2.3,['H','He']]
       myMatrix=[[1,2,3],[4,5,6],[7,8,9]] ##중첩된 리스트
       ```
     * 언패킹 (unpacking)
       ```python
       a,b,c,d=[1,3,4,5]
       ```

  + tuple
     * 특징
       + 수정 불가능 (immutable); 한번 만들어지면 이후 변경 불가능
       + 중복 허용
       + 순서 있음
       + 여러 자료형 혼합해서 저장 가능
     * 튜플 생성 - 소괄호 ```()``` 사용
       ```python
       colors = ("red", "green", "blue")
       # 요소 접근
       print(colors[1])   # green

       # 변경 불가 → 아래 코드는 오류 발생
       # colors[1] = "yellow"

       # 튜플 언패킹
       r, g, b = colors
       print(r, g, b)     # red green blue
       ```
  + set
    * 특징
      + 중복제거: 같은 값이 입력되어도 하나만 남게 됨
      + 순서없음
      + 인덱싱 불가: list나 tuple과 다름
      + 수정 가능 (mutable)
      + 원소의 타입에 제한 **있음**:
      + 실습1: 생성
        ```python
        # 중괄호 {} 사용
        s1 = {1, 2, 3}
        print(s1)  # {1, 2, 3}

        # set() 함수 사용
        s2 = set([1, 2, 2, 3])
        print(s2)  # {1, 2, 3} (중복 제거)

        # 빈 set 생성 시는 set()만 가능
        empty_set = set()
        print(empty_set)  # set()
        ```
      + 실습2: 변경
        ```python
        s = {1, 2, 3}

        # 추가
        s.add(4)           # {1, 2, 3, 4}
        s.update([5, 6])   # {1, 2, 3, 4, 5, 6} (여러 개 추가)

        # 삭제
        s.remove(3)        # {1, 2, 4, 5, 6} (없는 값 제거 시 오류 발생)
        s.discard(10)      # 없는 값 제거해도 오류 없음
        s.pop()            # 임의의 값 제거 후 반환 (순서 없으니 랜덤)
        ```

  + ```len``` built-in function중 하나
    ```python
    a=[3,4,5,'a','b']
    len(a) # 정수 5
    ```
  - List slicing
  - 1족 원소 기호를 순서대로 포함한 리스트 만들기 (수소, 리튬, 나트륨, 칼륨, 루비듐, 세슘, 프랑슘)
  - 실습 예시
    * Calister 예제 2.1)
        ```python
        #세륨의 동위원소는 4가지 존재한다:
        # 각 동위원소의 분율은 아래와 같다.
        Ce_f= [0.185, 0.251, 88.450, 11.114]  #[%]
        # 각 동위원소의 원자량은 아래와 같다.
        Ce_w = [135.907, 137.906, 139.905, 141.909]
        # 세륨의 평균 원자량은 얼마인가?
        avg=(Ce_f[0]*Ce_w[0]+ Ce_f[1]*Ce_w+[1]+ Ce_f[2]*Ce_w+[2]+ Ce_f[3]*Ce_w+[3])/(Ce_f[0]+Ce_f[1]+Ce_f[2]+Ce_f[3])
        ## average
        print(avg)
        ```


## 수업 02-2
 - ```if```, ```elif```, ```else``` 조건문 이해
    * 기본 구조
    ```python
    if 조건식:
        실행할 명령문1
        실행할 명령문2
        ...
    elif 다른조건식:
        실행할 명령문1
        실행할 명령문2
        ...
    else:
        실행할 명령문1
        실행할 명령문2
        ...
    ```
    * 주의
      + indent, dedent 에 주의!!
      + 콜론 기호 ':' 빼먹지 말 것!
    * 예시
      + 예1
        ```python
        # 예: 순수 알루미늄의 녹는점
        melting_point = 660  #Celcius degree
        temperature = 700    #Celcius degree

        if temperature < melting_point:
            print("Solid state")
        elif temperature == melting_point:
            print("Solid and liquid co-exist")
        else:
            print("Liquid state")
        ```

 - ```for``` 반복문
    * 기초 설명
      파이썬의 for 반복문은 **순서가 있는 데이터(시퀀스)**나 **반복 가능한 객체(iterable)**를 순차적으로 꺼내면서 코드를 실행하는 구문.
    * 기본 구조
       ```python
       for 변수 in 반복가능객체:
            실행할 명령문1
            실행할 명령문2
            ...
       ```
    * 대표적으로 **순서가 있는 데이터 시쿼스**로는 List, Tuple, Dictionary 타입의 변수가 있다.
      + 예1
       ```python
       a=[3,4,5] #list type
       for e in a:
           print(e)
       ```
      + 예2
       ```python
       a=('3',[34343],5) # tuple type
       for e in a:
           print(e)
       ```
      + 예3
       ```python
       a=dict(a='b',b='1',d=3,z=[]) # dictionary (Python 3.7>)
       for e in a:
           print(e)
       ```
    * 주의
      + indent, dedent 에 주의!!
      + 콜론 기호 ':' 빼먹지 말 것!

 - Built-in function인 ```range```, ```len```를 ```for```와 함께 조합!
    * 개념
      + ```len()``` -> 시퀀스 (List, 문자열, 튜플 등)의 **길이(요소 개수)**를 반환
      + ```range()``` → 지정한 범위의 숫자 시퀀스를 생성 (반복문에서 자주 사용)
      + 둘을 함께 쓰면 인덱스 기반 반복이 가능
      + 예시
         - 예시1
            ```python
            fruits = ["apple", "banana", "cherry"]

            for i in range(len(fruits)):  # 0 ~ len(fruits)-1
                print(f"Index {i}: {fruits[i]}")
            ```
         - 예시 2
            ```python
            specimen_lengths = [10.0, 12.3, 9.8, 11.5]  # cm

            for i in range(len(specimen_lengths)):
                length = specimen_lengths[i]
                print(f"Specimen {i+1}: {length} cm")
            ```
         - 예시 3
            ```python
            word = "steel"

            for i in range(len(word)):
                print(f"Index {i} → {word[i]}")
            ```

 - 실습 예시
      * 구구단 출력하기 (x단 입력하면 ... )
      * 학생 점수 데이터에서, 산술 평균, 최고점과 최저점 학생 이름 찾기 (조건문과 loop 활용)
      * 1부터 100사이의 정수합 구하기 (loop)
      * 주어진 List에서 최대값과 최소값 찾기 (조건문과 loop 활용)
      * 주양자수 $n$에 의해 결정되는 부 양자수 $l,m_l$ 출력하기.
        ```python
        # Calister 책의 표 2.1
        n=3 ## 주양자수,
        print('n:',n)
        no_electrons=0
        for l_value in range(0, n): # 0, 1, .., (n-1) 까지
            print('\tl:',l_value) #주의 '\t' string은 키보드의 탭기호를 뜻한다.
            low=-l_value
            up=+l_value
            print('\t\tml:',)
            for i in range(low,up+1): # -l, -l+1, ... 1, 0, 1, ... l-1, l
                print('\t\t\t',i)
                no_electrons=no_electrons+2 # 각 state마다 up/down spin 전자, 따라서 2개씩.
        print('total number of electrons:',no_electrons)
        ```
