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

#  문자열 포매팅
## 퍼센트 (%) 방식

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

## ~~str.format()~~는 다루지 않겠다.

## f-string
%를 활용한 방법만큼 널리 쓰이는 포매팅 기법은 f-string 기법이다. 아래와 같이, 문자열이 시작되는 따옴표에 앞서 ```f```로 f-string형식을 활용함을 밝히고, 문자열내에 ```{``` 및 ```}```쌍 내부에 변수의 이름을 직접 적는 방식이다. %기법은 대체되는 변수가 문자열 바깥에 기입되는 반면, f-string은 문자열 내부에 기입되어 있어 코드를 읽기가 더욱 수월하다는 장점이 있다.

```python
print(f'9/6 = {9/6:.1f}')
print(f'9/6 = {9/6:.5f}')
val=9/6
print(f'9/6 = {val:.1f}')
print(f'9/6 = {val:.5f}')
```


## 파일 쓰기 연습
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

## 파일 읽기 연습
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