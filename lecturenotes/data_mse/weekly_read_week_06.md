---
layout: page
title: DATA MSE week 06
permalink:
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
6 (NumPy 03 - ANN, Eigen value)
## 수업 06-1 (ANN, Activation)
  - Basic structure of Artificial Neural Network
    + 행렬곱과 더하기 조합. 아래 수식은 실제로 Artifical Neutral Network(ANN)에서 널리 활용되는 형태의 연산이다.
      $$
      \boldsymbol y=\boldsymbol W\cdot \boldsymbol x + \boldsymbol b
      \newline
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
        \newline
        \phi(x_i)=1 \text{ if } x_i\geq0
        $$

        ```python
        def act_func_binary(x):
          """
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

## 수업 06-2 (Eigen value)
