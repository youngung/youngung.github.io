---
layout: page
title: DATA MSE week 08
permalink:
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
# Week 8 (Matplotlib 01)
- 목표
  + axes, figure 를 만들 수 있다.
  + 선(line), 점(dot)으로 이루어진 그래프를 그릴 수 있다.
  + x축, y축의 label, tick, limits을 만들 수 있다.
  + linear scale, logscale을 만들고 이해할 수 있다.
  + 파일로부터 데이터를 불러오고, 이를 graph로 바꿀 수 있다.
## 수업 08-1
  + [Matplotlib](www.matplotlib.org): Python에서 데이터를 시각화하는 가장 널리 쓰이는 라이브러리.
  + 주로 사용되는 인터페이스: pyplot 모듈
  + plt interface
      ```python
      import matplotlib.pyplot as plt
      import matplotlib.pyplot as plt

      x = [0, 1, 2, 3, 4]
      y = [0, 1, 4, 9, 16]

      plt.plot(x, y)          # 선 그래프
      plt.title("Basic Line Plot")
      plt.xlabel("X-axis")
      plt.ylabel("Y-axis")
      ```
    - scatter plot
      ```python
      x = [5, 7, 8, 7, 6, 9, 5, 4, 5, 6]
      y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
      plt.scatter(x, y, color='red')
      plt.title("Scatter Plot")
    ```

    - 그래프 꾸미기
    ```python
    plt.plot([1,2,3],[1,4,9], label=r'$y = x^2$')
    plt.plot([1,2,3],[1,2,3], label=r'$y = x$')
    plt.legend() ## legend
    ```

    - subplot
    ```python
    plt.subplot(1, 2, 1)  # 1행 2열 중 첫 번째
    plt.plot([1,2,3],[1,4,9])
    plt.title("Left")

    plt.subplot(1, 2, 2)  # 두 번째
    plt.plot([1,2,3],[1,2,3])
    plt.title("Right")
    ```

  + Figure / axis objects
    Figure: 그래프 전체 "캔버스"
    Axes: 실제 데이터가 그려지는 "좌표 영역"
    (한 Figure 안에 여러 개의 Axes 가능: subplot)
    ```python
    import matplotlib.pyplot as plt

    # Figure(도화지), Axes(좌표 영역) 생성
    fig, ax = plt.subplots()

    x = [0, 1, 2, 3, 4]
    y = [0, 1, 4, 9, 16]

    # ax 객체를 활용해 데이터 플롯
    ax.plot(x, y, label="y = x^2", color="blue")

    # 그래프 꾸미기
    ax.set_title("Figure & Axes Example")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()
    ax.grid(True)

    plt.show()
    ```
  + 예제
    - Stress vs. strain curve 그리기
    - Tensile strength vs. ductility

## 수업 08-2

