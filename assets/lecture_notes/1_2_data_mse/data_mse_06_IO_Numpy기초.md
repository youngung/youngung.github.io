---
layout: distill
title: 데이터 재료과학 (제 6강)
description: IO
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

- INPUT/OUTPUT 개념 이해
- 파일을 활용해 데이터 input/output의 활용
- NumPy 기초를 이해 및 활용


# 개념

Python에서 파일을 통한 I/O는 `open()` 함수 활용한다 - 자세한 설명은
[여기](https://docs.python.org/3/library/functions.html#open)를 참고바람.

```open```함수를 통해 파일 오브젝트를 생성하고, 이를 통해 파일로 data를 입력하거나,
파일로부터 data를 불러올 수 있다. open의 경우 파일을 여는 여러가지 모드가 있다.

```open```함수에 arguments로 filename을 입력하고, 모드를 지정한다.

{% tabs 파일모드 %}
{% tab 파일모드 read %}
myFile = open(file='filenamehere', mode='r')
{% endtab %}
{% tab 파일모드 write %}
myFile = open(file='filenamehere', mode='w')
{% endtab %}
{% tab 파일모드 append %}
myFile = open(file='filenamehere', mode='a')
{% endtab %}
{% tab 파일모드 binary %}
myFile = open(file='filenamehere', mode='binary')
{% endtab %}
{% endtabs %}


# 예시

- 예시 0. (화면에 출력, 기보드로 입력)

  ```python
  # 키보드를 통한 입력
  my_value1=input("하나의 값을 입력하시오")
  my_value2=input("하나의 값을 입력하시오")

  print(my_value1+my_value2)
  # 화면에 출력
  ```

- 예시 1. 입력된 값을 모두 더하기
  ```python
  val=0.
  while True:
    inp = input("?")
    if len(inp)==0: break
    else:
      val=val+float(inp)

  print("총 합은", val, "입니다.")
  ```

- 예시 2. 위 예시 1을 바꿔서, 입력된 총 값의 평균을 구하는 Script를 작성해보자.

- 예시 3. (텍스트 파일 **쓰기**)

  이번 예시를 통해 `example.txt`라는 파일을 만들고 글을 적는다.

  ```python
  # 파일 쓰기
  with open("example.txt", "w" encoding="utf-8") as f:
      f.write("Hi people in Changwon National University!\n")
      f.write("This is an example text file!\n")
  ```

- 예시 4. (텍스트 파일 **읽기**)

  ```python
  # 파일 읽기
  with open("example.txt", "r", encoding="utf-8") as f:
      lines = f.readlines()  # 모든 줄을 리스트로 읽기
  for line in lines:
      print(line.strip())  # strip() → 줄바꿈 제거
  ```

- 예시 5. (성적 처리)
  다음 [파일](/assets/dat_files/lectures/1_2_data_mse/score_records/score_record_2017_MF_final_analysis.txt)
  을 읽고 평균, 표준 편차, 그리고 최고점과 최저점을 받은 학생 번호를 찾는
  파이썬 프로그램을 만들어 보자.

  ```txt
  ID Score
  --------------
  xxxx5093  14.0
  xxxx5298  53.0
  xxxx3374  28.0
  xxxx3374  41.0
  xxxx5116  15.0
  xxxx5122  16.0
  xxxx5102  10.0
  xxxx6114   6.0
  xxxx5108  26.0
  xxxx6135  22.0
  xxxx4246  12.0
  xxxx1513  11.0
  xxxx5115  42.0
  xxxx5140  41.0
  xxxx5105  44.0
  xxxx4254  67.0
  xxxx3341  47.0
  xxxx5100  48.0
  xxxx4264  55.0
  xxxx5127  53.0
  xxxx4235  44.0
  xxxx4249  67.0
  xxxx4257  41.0
  xxxx5146  53.0
  xxxx4273  62.0
  xxxx4275  64.0
  xxxx4258  62.0
  xxxx4282  58.0
  xxxx4236  77.0
  xxxx4269  38.0
  xxxx4445  50.0
  xxxx5142  53.0
  ```

- 예시 6.
  예시 5과 같은 파일이 여럿 주어진다면, 각 파일마다 예시3의 작업을 반복 수행하는 CLI에서
  활용 가능한 Python module을 만들자. 실습을 위해 아래 파일을 활용하자.
 [파일](/assets/dat_files/lectures/1_2_data_mse/score_records/all_scores/scores.zip)


- 예시 7. (모든 파일의 이름 바꾸기)
  다음 [압축파일](/assets/dat_files/lectures/1_2_data_mse/tensile_test_results.zip)을 풀어서 살펴보자.
  여기서 파일 이름에서 'WZ'를 모두 'EX'로 바꾸고 싶다. 어떻게 해야할까?

  ```dos
  c:\users\user> ren 00_DD_WZ_01.csv 00_DD_EX_01.csv
  c:\users\user> ren 00_DD_WZ_02.csv 00_DD_EX_02.csv
  ...
  ```

  혹은 복사?

  ```dos
  c:\users\user> cp 00_DD_WZ_01.csv 00_DD_EX_01.csv
  c:\users\user> cp 00_DD_WZ_02.csv 00_DD_EX_02.csv
  ...
  ```

  혹은 마우스로 일일이 눌러서 바꿀 수도 있겠다. Python으로 가능할까?

  ```python
  # os.copy
  # glob
  # os.getcwd()
  # os.listdir(os.getcwd())
  # `str`의 split을 찾거나, 혹은 index를 활용해 바꿀 수도 있겠다.
  ```

### 6.1.2. 문자열 포매팅
#### 6.1.2.1. 퍼센트 (%) 방식

문자열에 ```%s```, ```%d```, ```%i```, ```%f```기호를 삽입하여 문자나 값을 대체하여 넣을 수 있다. 아래 예문을 보면, ```name```과 ```density```를 ```print```가 되는 문자열 속에 특정 위치에 삽입 후 출력하는 것을 확인할 수 있다.

```python
name='Iron'
density=7.87
print('The density of %s is %d g/cm^3'%(name,density))
```

{% tabs strform %}
{% tab strform 문자 %}
%s
{% endtab %}
{% tab strform 정수1 %}
%d
{% endtab %}
{% tab strform 정수2 %}
%i
{% endtab %}
{% tab strform 실수 %}
%f
{% endtab %}
{% endtabs %}

문자열 속의 실수(float)의 경우 소수점자리를 수정하여 표현할 수 있다. 아래 예제를 살펴보면, 첫번째 ```print```문은 소수점 첫째자리까지, 그리고 두번째 ```print```는 소수점 다섯째자리까지 출력하는 것을 확인할 수 있다.

```python
print('9 / 6 = %.1f'%(9/6))
print('9 / 6 = %.5f'%(9/6))
```

#### 6.1.2.2. ~~str.format()~~는 다루지 않겠다.

#### 6.1.2.3. f-string
%를 활용한 방법만큼 널리 쓰이는 포매팅 기법은 f-string 기법이다. 아래와 같이, 문자열이 시작되는 따옴표에 앞서 ```f```로 f-string형식을 활용함을 밝히고, 문자열내에 ```{``` 및 ```}```쌍 내부에 변수의 이름을 직접 적는 방식이다. %기법은 대체되는 변수가 문자열 바깥에 기입되는 반면, f-string은 문자열 내부에 기입되어 있어 코드를 읽기가 더욱 수월하다는 장점이 있다.

```python
print(f'9/6 = {9/6:.1f}')
print(f'9/6 = {9/6:.5f}')
val=9/6
print(f'9/6 = {val:.1f}')
print(f'9/6 = {val:.5f}')
```


#### 6.1.2.4. 파일 쓰기 연습
1에서부터 100까지 모든 정수가 한줄에 하나씩 쓰여진 파일을 만들어보자. 반복되는 작업이 예상되므로 ```for```구문이 필요하겠다. 아래와 같은 코드를 `화면`에 출력하게 되겠다.
```python
for i in range(1,101):
   print(i)
```
화면에 출력하지 않고, 파일 `one2hund.txt`를 만들어 같은 방식의 출력을 다음과 같은 예시를 통해 수행할 수 있다.
```python
myfile = open('one2hund.txt','w') # file 열기
for i in range(1,101):
  myfile.write(f'{i}') # myfile instance의 write method 활용
myfile.close() # file 닫기
```
이후 파일을 열어보면, 가로로 모든 숫자가 붙은채로 아래와 유사하게 출력되는 것을 확인할 수 있다.
```txt
123456789101112131415161718...
```
각각의 정수를 개개의 줄로 출력이 되게끔 줄바꿈기호 '\n'를 활용하여 파일에 출력해보자.
```python
myfile = open('one2hund.txt','w') # file 열기
for i in range(1,101):
  myfile.write(f'{i}\n') # myfile instance의 write method 활용
myfile.close() # file 닫기
```

파일을 열기(open)하고 닫지 않는다면 예상하지 못한 일이 발생할 수 있다. 따라서 파일 오브젝트를 ```open```으로 생성한 뒤, 쓰임이 다하면 ```close```메소드로 닫아야 한다. 따라서, ```open```과 ```close```는 짝으로 쓰일때가 많다. ```open``` 활용 이후 ```close```구문을 깜빡하지 않게 강제시켜주는 좋은 습관은 ```with```구문을 함께 활용하는 것이다. 아래 에제를 보자.

```python
with open('one2hund.txt','w') as myFile # file 열기
   for i in range(1,101):
      myfile.write(f'{i}\n') # write method 활용
```
with와 indented된 구역으로 나누어 구성되어, 더욱 세련되게 코드 작성을 도와주고 읽기 쉽게 만들어준다.

#### 6.1.2.5. 파일 읽기 연습
위 쓰기에 이어서, 생성된 파일을 읽어보자.
```python
myfile= open('one2hund.txt','w') # file 열기
for i in range(1,101):
  myfile.write(f'{i}\n') # myfile instance의 write method 활용
myfile.close() # file 닫기

myfile = open('one2hund.txt','r') # file 열기
cnt=myfile.read()
print(cnt)
```


<br/><br/><br/><br/>

## 6.2. 수업 04-2 (NumPy 기초)

### 6.2.1. 기초 개념
- [NumPy](https://numpy.org)는 파이썬 환경에서, 고성능 수치 계산을 위한 library이다. 사실 빠른 연산을 위해 최적화된 [C](https://www.c-language.org)나 [FORTRAN](https://fortran-lang.org) library를 활용한다.
- 공식 사이트에서 더욱 상세히 배울 수 있다: [링크](https://numpy.org/devdocs/user/quickstart.html).

불행하게도, 많은 인터넷 자료가 그렇듯이, 문서가 영어로 작성되어 있다. 다행히도 최신 브라우저들은 번역 기능이 탑재되어 있으니 활용하면 좋겠다.

앞서 List를 활용하여, math package를 함께 사용하면, 스칼라, 벡터, 행렬 등을 대상으로 다양한 수학적 연산을 수행할 수 있다. 하지만 Python의 built-in 기능으로는 빠른 수학적 연산처리가 어렵다. 이를 보완하고자 연산속도가 빠르면서도 다양한 수학적 기능을 도와주는 [NumPy](https://numpy.org)패키지가 개발되었다. NumPy설치를 위해서는 ```pip```를 활용할 수 있다. 인터넷이 연결된 컴퓨터의 CLI환경에서 다음과 같이 명령어를 입력하면 설치가 가능하다. 인터넷으로 연결된 시스템의 터미널에서 아래와 같이 입력하면 설치된다.
```sh
c:/users/user/myrepo> pip install numpy
```
이후 파이썬 환경에서 NumPy패키지를 import해 사용하면 되겠다. 많은 경우, 아래와 같이 ```np```라는 이름으로 불러오는 경우가 많다.
```python
import numpy as np
```
다른 많은 Python 패키지들과 마찬가지로, open source 프로젝트로 개발되었으며, 현재로 활발히 업데이트가 되고 있다. 따라서 새로운 기능이 추가되거나, 종전의 기능이 없어지는 경우가 있으므로, 어떠한 버전을 활용하고 있는지 확인이 필요할 때가 있다. 그리고 한 시스템내에서 다양한 위치에 서로다른 패키지가 설치될 때가 있으므로, 사용되는 NumPy패키지의 위치를 확인할 필요가 있다. 아래의 두 경우를 살펴보자.
```python
import numpy as np
print(np.__version__)
print(np.__file__)
```

List로 생성된 값의 모임을 간단히 NumPy배열 형식 ```numpy.ndarray```로 간편히 바꿀 수 있다. 아래 예시들을 살펴보자.
```python
# 1차원 배열
arr1 = np.array([1, 2, 3])  # np.array 클래스 생성.
print(arr1)

# 2차원 배열
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# 0으로 채운 배열
zeros_arr = np.zeros((2, 3))  # zeros method활용하여 2x3배열
print(zeros_arr)

# 1로 채운 배열
ones_arr = np.ones((3, 3)) # 3x3배열
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

```numpy.ndarray```형식은 NumPy의 array클래스의 instance로써, 다양한 속성(attributes)와 매서드(method) 갖고 있다. 아래의 attributes와 매서드가 자주 쓰인다. 그 쓰임을 익힐 필요가 있다.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)   # (2, 3) → 2행 3열
print(arr.ndim)    # 차원 수 → 2
print(arr.size)    # 전체 원소 개수 → 6
print(arr.dtype)   # 데이터 타입 → int64 (환경에 따라 다름)
print(arr.ravel()) ## memory-efficient
print(arr.flatten()) ## independent copy
print(arr.ravel().sum())
print(arr.flatten().sum())
```

NumPy의 배열간의 연산은 벡터화되어 속도가 빠르다. 많은 경우, `for`, `range` 등의 일반적인 반복문 필요없어, 간단한 형태로 표기되어, list를 활용한 것보다 수식 표현과 연산속도에 유리하다.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a * b)   # [ 4 10 18]  (요소별 곱)
print(a / b)   # [0.25 0.4 0.5]
print(a ** 2)  # [1 4 9]    (제곱)


## 각각의 경우 List를 활용했을 때 훨씬 많은 코딩 필요함.
c=[] # +
for i in range(a):
  c.append(a[i]+b[i])

c=[] # -
for i in range(a):
  c.append(a[i]-b[i])

c=[] # *
for i in range(a):
  c.append(a[i]*b[i])

c=[] # /
for i in range(a):
  c.append(a[i]/b[i])

c=[] # **
for i in range(a):
  c.append(a[i]**2)

##?
print((a**2).sum())
```

List를 활용한 방식과 NumPy의 속도 비교를 위해 아래 예제를 활용해보자. 우선 0에서부터 100까지 정수가 담겨있는 ```List```와 ```numpy.ndarray``` 형식의 자료를 만들자.
```python
mylist=list(range(101))
mylist ## The list type object
myarray=np.array(mylist)
myarray ## The numpy type object
```
아래와 같이 각각의 연산을 JuPyter의 매직 키워드 ```%%timeit```를 활용해 7번 반복 연산해 평균 연산 속도를 측정해보자.
```python
%%timeit
s=0.
for i in range(100):
    s=s+mylist[i]
```
그리고 ```sum``` 매소드를 활용한 결과를 비교해보자.

```python
%%timeit
s=myarray.sum()
```

나의 경우에는 전자는
$$1.85 \mu s = 1.85 \times 10^{-6} s$$
그리고 후자는
$$539 ns = 538\times 10^{-9} s = 0.538 10^{-6} s$$
결과가 나왔다. 후자는 전자에 비해 약 1/3 정도의 시간만 필요하였다.

### 6.2.2. 차원과 축: NumPy 배열을 바라보는 두가지 관점
NumPy배열의 '차원'(dimension, 혹은 rank)는 배열이 몇 겹으로 중첩되어 있는지를 의미한다. 쉽게 말해, 데이터가 몇 단계의 리스트로 레이어로 감싸져 있는지에 따라 차원이 달라진다. 아래를 살펴보자.

```python
import numpy as np

a = np.array(5)                  # 스칼라 (0차원)
b = np.array([1, 2, 3])          # 벡터 (1차원)
c = np.array([[1, 2, 3],
              [4, 5, 6]])        # 행렬 (2차원)
d = np.array([[[1], [2], [3]],
              [[4], [5], [6]]])  # 행렬 (3차원) ... 혹은 ML/AI 관련 문헌에서 '텐서'라 불림 - 수학/물리 문헌의 '텐서'와 다름.
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
```

차원과 다르게 '축'(axis)의 관점에서 배열을 바라보는 관점도 있다. 이때 '축'은 배열의 index방향을 의미한다. 즉, 다차원 배열에서 데이터를 접근하거나 연산할 때 어느 방향을 기준으로 하느냐에 따라 축이 달라진다. 다음 배열은 차원의 관점에서는 2차원임을 알 수 있다.
```python
c = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
```
이 경우 축이 2개인 것으로 이해할 수 있다. 첫번째 축 ```0```은 행을 따라 내려가는 방향 (세로, column-wise)이 되며, 축 ```1```은 열을 따라 가로로 가는 방향 (가로, row-wise)로 이해된다. 아래 각 열, 그리고 행 '축'을 따라 덧셈을 하는 경우를 살펴보자.

```python
c = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(c.sum(axis=0))  # 열별 합 → [12 15 18]
print(c.sum(axis=1))  # 행별 합 → [ 6 15 24]
```

3D 배열에서 축 번호는 '바깥'부터 '안쪽' 순으로 0, 1, 2, ... 순으로 이어진다.

```python
d = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
```
```d.shape```은 ```(2,2,2)```이고, ```d.ndim```은 3이다. 즉 3차원이고, 총 세 축으로 이루어진다. 각 축을 따라 2개씩 element가 있는 구조로 이해할 수 있다. 이때
- ```axis=0``` 은 가장 바깥 차원
- ```axis=1``` 은 중간 차원 (row)
- ```axis=2``` 는 가장 안쪽 차원 (column)
로 이해된다.

아래 경우를 더 살펴보자.
```python
a = np.arange(15)
```
위 결과로 1D 배열에 0에서부터 14까지 15개의 element 숫자가 자료가 ```a```에 저장된다. 이를 (3x5) 형태의 2D 배열로 형태를 바꿀 수 있다. ```reshape``` method를 활용한다.
```python
b=a.reshape(3,5)
```
이때 두 축이 활용된 것으로 볼 수 있고, 첫번째 축 ```axis=0```은 3 요소를, 두번째 축 ```axis=1```은 5 요소를 가진 것으로 이해할 수 있다. 그 결과를 ```b```로 저장했고 그 결과를 출력해보자
```python
print(b)
```
다음과 같이 출력이 될것이다.
```
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
```
첫번째 축(```axis=0```)의 첫 요소는 [0,1,2,3,4], 그 다음은 [5,6,7,8,9], 마지막 세번째는 [10,11,12,13,14]가 된다. 이를 인덱싱 해보면
```python
print(b[0,:])
print(b[1,:])
print(b[2,:])
```

이번에는 두번째 축 (```axis==1```)을 따라 살펴보자.
첫 요소는 [0,5,10], 그 다음은 [1,6,11], [2,7,12], [3,8,13], 마지막 5번째 요소는 [4,9,14]가 될 것이다.
```python
print(b[:,0])
print(b[:,1])
print(b[:,2])
```

### 6.2.3. Indexing & slicing
List 타입의 자료에서도 indexing과 slicing이 사용된다. [시작,끝,스텝]형태의 인덱싱이 NumPy 배열에도 동일하게 적용된다.
```python
mylist=List((3,3,4,3,3,4,5,6))
#mylist[시작:끝:스텝] 형태로 index가 적용되는 것 처럼 ..
```


```python
myarray=np.array((3,3,4,3,3,4,5,6))
myarray[2:6:2] #3번째부터 6번째까지, 2칸씩 띄어 넘으며 ..
#mylist[시작:끝:스텝] 형태로 index가 적용되는 것 처럼 ..
```
위 결과는 아래와 같을 것이다.
```python
array([ 5, 10])
```

NumPy 배열에 경우에는 이러한 indexing이 각 '축'에 깔끔히 적용될 수 있다. 아래 2차원 배열 (혹은 2축으로 구성된 배열)을 살펴보자.
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

위의 경우, 첫번째 축(axis=0)은 2개의 요소 그 다음 축(axis=1)은 3개의 요소로 이루어진 것을 알 수 있다. 즉

```python
# nested 배열의 각 축을 '행'(가로)과 '열'(세로)이라 하면
# arr = [  1  2  3 ] # 첫번째 가로
#.         4  5  6   # 두번째 가로

print(arr[0, 0])  # 1행 1열 → 1
print(arr[1, :])  # 2행 전체 → [4 5 6]
print(arr[:, 1])  # 모든 행의 2열 → [2 5]
```

각 축마다 begin, end, step이 적용되므로, 복잡한 slicing을 할 수 있다. 아래를 보자.
```python
## 각 '축'에서 List indexing 적용가능. 예를 들어
print(arr[1::,1::])
print(arr[::2,::2])

#
print(arr[::-1,::])  #행만 거꾸로
print(arr[::,::-1])  #열만 거꾸로
print(arr[::-1,::-1]) #행과 열을 모두 거꾸로
```

아래 경우를 하나씩 입력 후 차근차근 살펴보며 실습해보자.
```python
a=np.arange(100)
a=a.reshape(10,10)
a[:,::2]  # 각 10자리에서 짝수로만 이루어진 2차원 배열
a[0::2,::] # 10자리수가 짝수로 이루어진 2차원 배열
a[1::2,::] # 10자리수가 홀수로 이루어진 2차원 배열
a[::,1::2] # 1의 자리수가 홀수로 이루어진 2차원 배열
a[::,0::3] # 1의 자리수가 0, 3, 6, 9로 끝나는 수로 이루어진 2차원 배열
a[0::3,::] # 10의 자리수가 0, 3, 6, 9로 끝나는 수로 이루어진 2차원 배열
```

다음 3차원의 경우도 살펴보자.

```python
a=np.arange(1000)
a=a.reshape(10,10,10) #
a[::5,::,::] #?
```


- 예제: 데이터 파일
  Use data in here [matrix_01.txt](/assets/dat_files/lectures/1_2_data_mse/matrix_01.txt)

  ```python
  import numpy as np

  # 공백 구분 텍스트 불러오기
  matrix = np.loadtxt("matrix.txt")

  print("불러온 행렬:")
  print(matrix)

  print("shape:", matrix.shape)   # (3, 3)
  print("dtype:", matrix.dtype)   # ?
  ```

- 예제: csv file
  Use data in here [matrix_01.csv](/assets/dat_files/lectures/1_2_data_mse/matrix_01.csv)

  ```python
  import numpy as np

  # 공백 구분 텍스트 불러오기
  matrix = np.loadtxt("matrix.txt")

  print("불러온 행렬:")
  print(matrix)

  print("shape:", matrix.shape)   # (3, 3)
  print("dtype:", matrix.dtype)   # ?
  ```


- 예제: 저장하기
<aside><p>%d 와 %f로 정수는 각각 정수와 실수 형식 저장에 쓰인다.</p></aside>

```python
# 행렬 저장하기 (공백 구분)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt("save_matrix.txt", matrix, fmt="%.2f")

# CSV로 저장
np.savetxt("save_matrix.csv", matrix, delimiter=",", fmt="%d")
```

<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
