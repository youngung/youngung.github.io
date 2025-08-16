---
layout: page
title: DATA MSE week 06
permalink:
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
# Week 6 (NumPy 03 - ANN, Eigen value)
## 수업 06-1 (ANN, Activation)
  - Basic structure of Artificial Neural Network
    + 행렬곱과 더하기 조합. 아래 수식은 실제로 Artifical Neutral Network(ANN)에서 널리 활용되는 형태의 연산이다.
      $$
      \boldsymbol y=\boldsymbol W\cdot \boldsymbol x + \boldsymbol b
      $$
      $$
      y_i=\bigg(\sum_j^mW_{ij}x_j\bigg)+b_i=W_{ij}x_j+b_i \text{ with } i=1,2, ..., n
      $$

      ```python
      W=np.array([[1,2,3,4],[5,6,7,8]]) ## 2x4 행렬 (with n and m beging 2 and 4, respectively)
      x=np.array([5.5,0.1,0.3,1.0])     ## 4 (nested 가 아님. 1차원 임에 유의)
      b=np.array([-0.5,+0.5])

      n=2
      m=4
      y=np.zeros(n) # 주의 정수 n은 2이다.

      for i in range(n): ## i=1,2,...,n
        for j in range(m):
          y[i]+=W[i,j]*x[j]+b[i]
      print(y)
      ## 위 표현은 틀렸다.
      ## 올바른 표현의 예는 아래와 같다. 무엇이 고쳐졌는가?
      n=2
      m=4
      y=np.zeros(n)
      for i in range(n): ## i=1,2,...,n
        y[i]+=b[i]
        for j in range(m):
          y[i]+=W[i,j]*x[j]
      print(y)
      ```

    + 예시 ```W[n,m]```행렬과 ```x[m]```벡터, 그리고 ```b[n]```벡터로 구성된
      배열을 활용해 위 수식 $\boldsymbol v=\boldsymbol W\cdot \boldsymbol x + \boldsymbol b$을
      계산하여 리턴하는 함수를 만드시오.

      ```python
      def neuron(w,x,b):
          """
          Arguments
          ---------
          W: ndarray
           [m x n] matrix (weight)
          b: ndarray
           [n] vector (bias)

          Returns
          -------
          W.x + b
          """
          n,m=w.shape() # tuple
          y=np.zeros(n)
          for i in range(n):
            y[i]+=b[i]
            for j in range(m):
              y[i]+=w[i,j]*x[j]
          return y
      ```
  - Activation
    + neutral network에 쓰이는 일반적인 neutron은 다음 형태를 가지는 경우가 많다.
      $$
      y_k=\phi\bigg(\sum_{j}^mw_{kj}x_j+b_k\bigg)
      $$
      이 때 $\phi$는 activation function이라 불리며 다양한 형태가 사용되고 있다.
      우리는 이를 element-wise로 적용되는 함수라 보자.
    + Activation function
      * Binary step
        $$
        \phi(x_i)=0 \text{ if } x_i<0
        $$
        $$
        \phi(x_i)=1 \text{ if } x_i\geq0
        $$

        ```python
        def act_func_binary(x):
          """
          Binary function as the activation function for neuron
          """
          flg=x>=0
          y=np.zeros(x.shape)
          y[flg]=1.
          return y
        ```
      * 예시 (Logistic function)
        $$
        \phi(x_i)=\frac{1}{1+e^{-x_i}}
        $$
      * 예시: Rectified linear unit (ReLU)
        $$
        \phi(x_i)=\frac{x+|x|}{2}
        $$
## 수업 06-2 (Eigen value)
  - 개념
    + 고유값(eigen value): 행렬(특히 선형변환)을 적용했을 때, 크기만 변하고 방향은 변하지 않는 벡터의 크기 변화 비율.
    + 고유벡터(eigen vector): 그 “변하지 않는 방향”을 가지는 벡터.
    + 수식:
      $$
      \boldsymbol A\cdot \boldsymbol v = \lambda \boldsymbol v
      $$
      를 만족시키는 스칼라 $$\lambda$$ 값을 고유값이라 한다.

      위 관계를 만족시키는 고유값 세개가 각각 $$\lambda_1,\lambda_2,\lambda_3$$라면

      $$\lambda_1\boldsymbol v,\lambda_2\boldsymbol v,\lambda_3\boldsymbol v$$
      를 고유 벡터라 한다.
  - 예시
    + 2차원 예시01
      $$
      \begin{bmatrix}
      A_{11}&A_{12}\\
      A_{21}&A_{22}
      \end{bmatrix}
      \begin{bmatrix}
      v_1\\
      v_2
      \end{bmatrix}
      =
      \lambda
      \begin{bmatrix}
      v_1\\
      v_2
      \end{bmatrix}
      $$

      $$
      A_{11}v_1+A_{12}v_2=\lambda v_1\ \ \ \ (1)
      $$
      $$
      A_{21}v_1+A_{22}v_2=\lambda v_2\ \ \ \ (2)
      $$
      (1)식을 고치면,
      $$
      (A_{11}-\lambda)v_1=-A_{12}v_2
      $$
      따라서
      $$
      v_1=\frac{-A_{12}}{A_{11}-\lambda}v_2
      $$
      (2)에 대입하면
      $$
      \frac{-A_{21}A_{12}}{A_{11}-\lambda}v_2+A_{22}v_2=\lambda v_2\ \ \ \ (3)
      $$

      (3)의
      $$
      v_2=0
      $$
      인 해는 trivial. 이걸 제외하면,

      $$
      \frac{-A_{21}A_{12}}{A_{11}-\lambda}+A_{22}=\lambda
      $$
      정리하면
      $$
      -A_{21}A_{12}+A_{22}(A_{11}-\lambda)=\lambda(A_{11}-\lambda)
      $$

      위는 $\lambda$에 대한 2차 방정식이며

      $$
      \lambda^2-(A_{11}-A_{22})\lambda-A_{21}A_{12}+A_{22}A_{11}=0
      $$
    + 2차원 예시02
      $$
      \boldsymbol A\cdot \boldsymbol v = \lambda \boldsymbol v
      \ \ \
      \rightarrow
      \ \ \
      (\boldsymbol A-\lambda\boldsymbol I)\cdot v=0
      $$

      $$
      \boldsymbol A =
      \begin{bmatrix}
      A_{11}& A_{12}\\
      A_{21}& A_{22}
      \end{bmatrix}
      $$
      그리고
      $$
      \boldsymbol I =
      \begin{bmatrix}
      1& 0\\
      0& 1
      \end{bmatrix}
      $$

      고유값 $\lambda$는 아래와 같이 구해진다.
      $$
      \det(\boldsymbol A-\lambda\boldsymbol I)=0
      $$


      ```python
      import numpy as np
      def eig2x2(A):
          a=A[0,0]
          b=A[0,1]
          c=A[1,0]
          d=A[1,1]
          tr = a + d
          det = a*d - b*c
          disc = tr*tr - 4*det
          lam1 = (tr + np.sqrt(disc)) / 2
          lam2 = (tr - np.sqrt(disc)) / 2
          return lam1, lam2

      A = np.array([[3,2],[2,1]], dtype=float)
      lam1, lam2 = eig2x2(A)
      print("manual:", lam1, lam2)
      print("numpy :", np.linalg.eigvals(A))
      ```

    - 예시
      주어진 [파일](data/matrix_03.txt)의 매트릭스의 값들을 활용해서 각 파일에서 고유값들을 구해서
      출력하시오.
      ```python
      import numpy as np
      def eig2x2(A):
          a=A[0,0]
          b=A[0,1]
          c=A[1,0]
          d=A[1,1]
          tr = a + d
          det = a*d - b*c
          disc = tr*tr - 4*det
          lam1 = (tr + np.sqrt(disc)) / 2
          lam2 = (tr - np.sqrt(disc)) / 2
          return lam1, lam2
      d=np.loadtxt('../data/matrix_03.txt',skiprows=1)
      for i, mat2x2 in enumerate(d):
          mat=mat2x2.reshape(2,2)
          print(eig2x2(mat)) ## nan 은 어던 경우인가?
      ```
