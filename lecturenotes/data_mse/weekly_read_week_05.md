---
layout: page
title: DATA MSE week 05
permalink:
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
5 (NumPy 02 - 배열 연산(산술, 내적, 외적), 브로드캐스팅, 그외 기타 함수)
  - 목표
    + 벡터/행렬 연산을 할 수 있다.
    + 브로드 캐스팅을 이해한다.
    + Determination, Eigen value 등을 계산할 수 있다.
## 수업 05-1
  - 벡터의 내적
    $$\boldsymbol a \cdot \boldsymbol b=a_1b_1+a_2b_2+a_3b_3=\sum_i^3a_ib_i$$
    List, len, range를 활용한다면 아래와 같이 표현 가능
    ```python
    a=[1,2,3]
    b=[4,5,6]
    dotprod=0.
    for i in range(3):
      dotprod=dotprod+a[i]*b[i]
      ## 위를 `dotprod+=a[i]*b[i]`로 줄여서 표현 가능
    ```

    NumPy의 배열을 활용한다면?
    ```python
    a=np.array([1,2,3])
    b=np.array([4,5,6])
    dotprod=0.
    for i in range(3):
      dotprod+=a[i]*b[i]
      ## 위를 `dotprod+=a[i]*b[i]`로 줄여서 표현 가능
    ```
  - 행렬간의 dot product

    $$
    \begin{bmatrix}
    1 & 2 \\
    3 & 4
    \end{bmatrix}
    \cdot
    \begin{bmatrix}
    2 & 0 \\
    1 & 3
    \end{bmatrix}
    = ?
    $$
    ```python
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[2, 0], [1, 3]])

    print(A @ B)          # 행렬 곱
    print(np.dot(A, B))   # 동일
    ```

    두 2x2 행렬 $\boldsymbol A$와 $\boldsymbol B$의 곱 결과가 또 다른 2x2행렬 $\boldsymbol C$라면
    $$
    \boldsymbol A\cdot\boldsymbol B = \boldsymbol C
    $$
    이를 **index**를 활용한 방식으로 표현가능하다.
    $$
    \sum_k^3A_{ik}B_{kj}=C_{ij}, \text{ for } i=1,2,3.
    $$
  - 외적
    $$
    \boldsymbol c = \boldsymbol a \times \boldsymbol b
    \newline
    c_i=\epsilon_{ijk}a_jb  _k
    $$

    ```python
    import numpy as np

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    c = np.cross(a, b)
    print(c)  # [-3  6 -3]
    ```
    예시 - tetrahedral site & octaheral site 크기 구하기
  - Broadcasting
    * 브로드캐스팅은 서로 다른 shape의 배열끼리 연산할 때 NumPy가 자동으로 차원을 맞춰주는 기능
    * 예시 (1차원+0차원(스칼라))
      ```python
      arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
      print(arr + 10)  # [11 12 13 ... 19]
      ```
    * 예시 (2차원 + 1차원)
      ```python
      mat = np.array([[1, 2, 3],
                      [4, 5, 6]])
      vec = np.array([10, 20, 30])

      print(mat + vec)
      # [[11 22 33]
      #  [14 25 36]]
      ```
    * 주의
      뒤에서부터 비교하며 차원이 같거나 1이면 확장 가능
      하나라도 불가능하면 에러 발생
  - Other various features
    ```python
    arr = np.array([1, 4, 9, 16])

    print(np.sqrt(arr))   # 제곱근 → [1. 2. 3. 4.]
    print(np.exp(arr))    # e^x
    print(np.log(arr))    # 자연로그
    print(np.sin(arr))    # 사인 함수
    print(np.mean(arr))   # 평균
    print(np.sum(arr))    # 합
    print(np.min(arr))    # 최소값
    print(np.max(arr))    # 최대값
    print(np.std(arr))    # 표준편차

    arr = np.array([3, 1, 2])

    print(np.sort(arr))        # 정렬된 배열
    print(np.argsort(arr))     # 정렬 인덱스
    print(np.argmax(arr))      # 최대값 인덱스
    print(np.argmin(arr))      # 최소값 인덱스

    ind=np.argsort(arr)
    arr[ind] ## sorting 이 된 배열

    # 추가 예제
    names=['Michael','Jim','Pam','Dwight','Kevin','Creed']
    scores=[5, 30, 20, 40, 10, 25]

    inds=np.argsort(scores)
    print(names[inds]) ## score에 따라 정렬된 배열
    ```
## 수업 05-2
  - Einstein summation
    + 벡터 스케일링 (스칼라 곱)
      $$
      c\boldsymbol a=\boldsymbol b
      $$
      이를 index 표기법으로 나타내면
      $$
      b_i=ca_i \text{ with } i=1,2,3
      $$
      ```python
      ## List로 구현
      c=0.3
      a=[1,2,3]
      b=[] # empty list
      for i in range(3): ## iteration
        b.append(c*a[i])

      ## Numpy로 구현
      c=0.3
      a=np.array([1,2,3])
      b=c*a ## broadcasting
      ```
    + 벡터 내적
      $$
      \boldsymbol a \cdot \boldsymbol b = \sum_i^3 a_ib_i=c
      $$
      위를 Einstein summation convention으로 표기하면
      $$
      \boldsymbol a \cdot \boldsymbol b = a_ib_i=c
      $$
      summation 기호($\sum$)가 생략되어 있음에 주목하시오.

      ```python
      ## Numpy없이 구현
      a=[1,2,3]
      b=[4,5,6]
      c=0.
      for i in range(3):
        c+=a[i]*b[i]

      ## Numpy로 구현
      a=np.array([1,2,3])
      b=np.array([4,5,6])
      c=a*b  ## element-wise operation되는 것을 유념하라.
             ## 즉 c=np.array([a[0]*b[0],a[1]*b[1],a[2]*b[2]])
      c=c.sum()

      #혹은 마지막 두 줄을 줄여서 아래와 같은 한줄의 명령어로 바꿀 수 있겠다.
      c=(a*b).sum()
      ```
    + 행렬 벡터 곱
      $$
      \boldsymbol c = \boldsymbol A \cdot \boldsymbol v
      \newline
      c_i = \sum_j^3A_{ij}v_j \ \text{ for } i=1,2,3
      $$
      위를 Einstein summation convention으로 표기하면
      $$
      c_i=A_{ij}v_j
      $$
    + 행렬 곱 (single dot)
      $$
      \boldsymbol C = \boldsymbol A\cdot \boldsymbol B
      \newline
      C_{ij} = \sum_k^3 A_{ik}B_{kj} \text{ for } (i,j) \text{ of } (1,1), (1,2), ... , (3,2), (3,3)
      $$

      NumPy를 사용하지 않는다면 아래와 같은 예시로 표현될 수 있겠다.
      ```python
      A=[[1,2,3],[4,5,6],[7,8,9]]
      B=[[3,2,1],[6,5,4],[9,8,7]]
      C=[]
      for i in range(3):
        C.append([])
        for j in range(3):
          C[i].append(0)
          for k in range(3):
            C[i][j]+=A[i][k]*B[k][j]
      ```

      NumPy를 활용한다면?
      ```python
      import numpy as np
      A=np.array([[1,2,3],[4,5,6],[7,8,9]])
      B=np.array([[3,2,1],[6,5,4],[9,8,7]])
      C=np.zeros((3,3))
      for i in range(3):
          for j in range(3):
              for k in range(3):
                  C[i,j]+=A[i,k]*B[k,j] ## Nested-list와 달리 ',' 콤마 기호로 각 축의 index를 활용한다.
      print(C)
      # 혹은 dot 활용하여
      C=np.dot(A,B)
      print(C)
      # 혹은 더 줄여서 (python 3.5이상)
      C=A@B # dtype 이 float로 바뀜
      print(C)
      ```
    + 행렬 곱 (double dot)
      $$
      c=\boldsymbol A : \boldsymbol B
      \newline
      c=\sum_i\sum_jA_{ij}B_{ij}=\sum_j\sum_iA_{ij}B_{ij}=\sum_j\sum_iB_{ij}A_{ij}=\sum_i\sum_jB_{ij}A_{ij}
      $$

      파이썬 코드로 바꾸면...
      ```python
      A=[[1,2,3],[4,5,6],[7,8,9]]
      B=[[3,2,1],[6,5,4],[9,8,7]]
      ## 1
      c=0.
      for i in range(3): # i is outer
        for j in range(3): # j is inner
          c+=A[i][j]*B[i][j]
      print(c)
      ## 2, 안/바깥 for-loop 바뀜.
      c=0.
      for j in range(3): # j is outer
        for i in range(3): # i is inner
          c+=A[i][j]*B[i][j]
      print(c)
      ## 3. 안/바깥 for-loop 바뀜, 그리고 A와 B의 순서 바뀜
      c=0.
      for j in range(3): # j is outer
        for i in range(3): # i is inner
          c+=B[i][j]*A[i][j] # A[i][j] x B[i][j] 혹은 B[i][j] x A[i][j]
      print(c)
      ## 4. A와 B의 순서 바뀜
      c=0.
      for i in range(3): # i is outer
        for j in range(3): # j is inner
          c+=B[i][j]*A[i][j] # A[i][j] x B[i][j] 혹은 B[i][j] x A[i][j]
      print(c)
      ```

      ```numpy```를 활용해서 표현해보자.
      ```python
      A=np.array([[1,2,3],[4,5,6],[7,8,9]])
      B=np.array([[3,2,1],[6,5,4],[9,8,7]])
      ##
      c=0.
      for i in range(3): # i is outer
        for j in range(3): # j is inner
          c+=A[i,j]*B[i,j]
      ```

