---
layout: page
title: DATA MSE week 04
permalink:
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
4 (file IO / NumPy 01 - 기초 배열(array) 이해)
  - 목표
  - 파일을 활용해 데이터 input/output의 활용 가능하다.
  - NumPy 기초를 이해한다.
## 수업 04-1 기초 (file/IO)
  - 개념
    + Python에서 파일을 다룰 때는 ```open()``` 함수
    + 파일 모드
      * 모드
        - 'r' : read
        - 'w' : write
        - ~~'a' : append~~
        - ~~'b' : binary~~
        - ~~'+' : read & write~~
    + 예시 (텍스트 파일 쓰기)
      ```python
      # 파일 쓰기
      with open("example.txt", "w" encoding="utf-8") as f:
        f.write("안녕하세요!\n")
        f.write("파일 I/O 예제입니다.\n")
      ```
    + 예시 (텍스트 파일 읽기)
      ```python
      # 파일 읽기
      with open("example.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()  # 모든 줄을 리스트로 읽기
      for line in lines:
        print(line.strip())  # strip() → 줄바꿈 제거
      ```
## 수업 04-1 및 04-2
  - 개념
    + [Numpy](www.numpy.org)는 고성능 수치 계산을 위한 library
  - 설치 (인터넷 연결 필요)
    ```sh
    pip install numpy
    ```
  - import
    ```python
    import numpy as np
    ```
  - 배열 생성
    ```python
    # 1차원 배열
    arr1 = np.array([1, 2, 3])
    print(arr1)

    # 2차원 배열
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr2)

    # 0으로 채운 배열
    zeros_arr = np.zeros((2, 3))  # 2행 3열
    print(zeros_arr)

    # 1로 채운 배열
    ones_arr = np.ones((3, 3))
    print(ones_arr)

    # 특정 값으로 채운 배열
    full_arr = np.full((2, 2), 7)
    print(full_arr)

    # 연속된 수
    range_arr = np.arange(0, 10, 2)  # 0부터 10 전까지 2씩 증가
    print(range_arr)

    # 랜덤 배열
    rand_arr = np.random.rand(2, 3)  # 0~1 사이 난수
    print(rand_arr)
    ```
  - 배열 속성
    ```python
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr.shape)   # (2, 3) → 2행 3열
    print(arr.ndim)    # 차원 수 → 2
    print(arr.size)    # 전체 원소 개수 → 6
    print(arr.dtype)   # 데이터 타입 → int64 (환경에 따라 다름)
    ```
  - 배열 연산
    * Vectorized operation (속도 향상)
    * 반복문 필요 없음.
    * element-wise operation 이라도 불림
    ```python
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print(a + b)   # [5 7 9]
    print(a - b)   # [-3 -3 -3]
    print(a * b)   # [ 4 10 18]  (요소별 곱)
    print(a / b)   # [0.25 0.4 0.5]
    print(a ** 2)  # [1 4 9]    (제곱)
    ```
  - Indexing & slicing
    ```python
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    # nested 배열의 각 축을 '행'(가로)과 '열'(세로)이라 하면
    # arr = [  1  2  3 ] # 첫번째 가로
    #.         4  5  6   # 두번째 가로

    print(arr[0, 0])  # 1행 1열 → 1
    print(arr[1, :])  # 2행 전체 → [4 5 6]
    print(arr[:, 1])  # 모든 행의 2열 → [2 5]
    ```
