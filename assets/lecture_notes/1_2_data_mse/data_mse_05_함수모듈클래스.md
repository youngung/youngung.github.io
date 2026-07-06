---
layout: distill
title: 데이터 재료과학 (제 5강)
description: 함수
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


# 5. 제 5강: 함수, class, module
- 함수 (function), module & import, class
- 목표
  - 함수와 클래스, 그리고 모듈의 이해
  - 함수를 만들어, 모듈화 시키고 CLI에서 실행할 수 있다.

## 5.1. 함수

- 특정한 작업(task)를 수행하는 묶음.

- basics:
  `def`로 정의하며, **재사용** 가능하고(reuseable),
  입력(arguments), 출력(return)값을 가질 수 있다.
  입력과 출력이 없는 함수도 있다.

- 예시1: 기초 형태 (template)

```python
def add(a, b): #함수의 이름이 'add', 입력은 a와 b
   return a + b # 출력은 a+b
```

- 예시2

```python
def sayhi(): # 함수의 이름이 'sayhi', 입력과 출력 없음
   print('Hi')
```

- 예시3

```python
def func(a=3,b=5): # 함수의 이름이 'func', 입력 a와 b의 default가 있음.
  """
  a and b are the two arguments of this function
  and this function calculates a+b, then return the result as output
  """
  return a+b
```

아래 실행해보자
```python
## default value 활용됨
print(func())

print(func(3,5))

print(func(5,3))

print(func(a=3,b=6))

print(func(b=6,a=3))

print(func.__doc__) ## docstring 출력
print(help(func))
print(help(help))
```

- 예시 4: 아래 함수를 정의하면 에러가 발생한다. 에러를 읽어보고 이해해보자.

```python
def f(a=3,b=5,c,d):
   print(a+b)
   print(c+d)
   return a*b*c*d
```

## 5.2. Built-in functions (no import / no declaration required)

- 특징
  - built-in 함수는 파이썬이 기본적으로 제공하는 함수
  - 별도의 **import** 없이 언제든 바로 사용 가능; 예 (print, help, ...)
  - 약 70여 개의 built-in 함수: A full list of built-in functions: [here](https://docs.python.org/3/library/functions.html)

- 입력(input)과 출력(output) I/O
  - ```print``` 함수
  - ```input``` 함수

- 출력 예시
  ```python
  # 1. 단순 문자열 출력
  print("안녕하세요, 파이썬!")

  # 2. 숫자 출력 및 연산 결과 출력
  print(2026)
  print(10 + 20)

  # 3. 여러 값 동시에 출력 (쉼표로 구분하면 한 칸씩 띄어서 출력돼요)
  print("올해는", 2026, "년입니다.")
  ```

- 입력 예시
  ```python
  # 1. 입력 받기
  age_str = input("당신의 현재 나이를 입력하세요: ")

  # 2. 형변환 (문자열로 들어온 나이를 계산할 수 있게 정수(int)로 바꿔줘요)
  age = int(age_str)

  # 3. 계산하기
  next_year_age = age + 1

  # 4. 결과 출력하기
  print("내년에 당신은", next_year_age, "살이 됩니다!")
  ```

## 5.3. 모듈(module)과 import

- 위 함수 중 하나를 모듈로 만들고 import 해보기

- 한 재료의 부피와 질량을 측정해 밀도를 계산하려고 한다. 각 측정값에 오차가 있어, 측정을
 여러번 되풀이 한 다음 평균 값을 계산해 밀도를 구하려고 한다. 아래의 예시를 직접 작성해보고
 이를 활용해보자.

  - 'calc_dens.py` 모듈 작성
  ```python
  # 이 코드를 파일명 `calc_dens.py`로 작성하여 저장하자.
  def calc_dens(mass, volume):
    """
    질량은 g 단위로, 부피는 mm^3으로
    """
    density = mass / volume
    return density
  ```

  - 'main.py' 모듈 작성
  ``` python
  # 이 코드를 `main.py`로 작성하여 저장하자.

  ## 밀도 계산 프로그램

  ## Raw data
  mass=[6.01, 6.05, 5.93, 6.03]
  vol=[3.11, 3.20, 3.09, 3.15]

  import calc_dens ## calc_dens.py 모듈을 import

  dens=[] ## list 자료 생성
  for i in range(len(mass)):
    val=calc_dens(mass=mass[i],volume=vol[i]) ## calc_dens.py 모듈 내의 함수
    dens.append(val) ## list 자료에 값 저장

  average=0.
  for i in range(len(dens)):
    average=average+dens[i]
  average=average/len(dens)
  ```

  - 위 생성된 모듈을 활용해서 표준 편차 구해보기.
   $std(v_i)=\sum_i^n (\bar{v} - v_i)^2$

  - 측정된 질량에서의 표준 편차는 얼마인가?
  - 측정된 부피내의 표준 편차는 얼마인가?
  - 밀도의 표준 편차는 얼마인가?
  - 표준편차를 계산하는 함수를 만들어서 활용해보자.


### 5.3.1. Class

- 개념

  - 클래스(class)는 객체(object)를 만드는 틀(설계도)
  - 클래스를 활용해 데이터와 기능을 한꺼번에 통합
  - 객체지향 프로그래밍(OOP, Object-Oriented Programming)의 핵심 개념
  - 클래스 안에는 속성(변수, attribute)과 메서드(함수, method)
  - Creating a new class creates a new type of object, allowing new instances of that type to be made.

- 예시

```python
	class Atom:
		def __init__(self,name):
			self.name = name
		def add_density(self,density):
			self.density=density
		def add_structure(self,structure):
			self.structure=structure

	## usage examples
	myFe=Atom() # Atom 클래스를 활용
	myFe.add_density(7.87) #7.87g/cm^3
	myFe.add_structure('BCC')

	myAl=Atom()
	myAl.add_density(2.70)
	myAl.add_structure('FCC')
```

- `getattr` built-in 함수

  - 기본문법

  ```python
  getattr(object, name[, default])
  ```

  - object : 속성을 가져올 대상 객체
  - name : 속성 이름 (문자열로 지정)
  - default (선택적) : 해당 속성이 없을 경우 반환할 기본값 (없으면 AttributeError 발생)

### 5.3.2. 클래스 예제

- 합금(Alloy) 클래스 만들기

  - 설계: 공통 속성 나열해보기
    - 합금은 모두 '이름' 가지고 있음
    - '인장강도'
    - '연성'
    - '밀도'

```python
class Alloy:
	def __init__(self, name, tensile_strength, ductility, density):
		self.name = name
		self.tensile_strength = tensile_strength  # MPa
		self.ductility = ductility                # %
		self.density = density                    # g/cm^3

# 합금 데이터
a1 = Alloy("Ni-Cu", 450, 35, 8.9)
a2 = Alloy("Al-Mg", 320, 25, 2.7)
a3 = Alloy("Ti-6Al-4V", 900, 14, 4.4)

alloys = [a1, a2, a3]

# 특정 물성(property) 가져오기
property_to_check = "tensile_strength"  # 여기만 바꾸면 됨

for alloy in alloys:
	  value = getattr(alloy, property_to_check, "N/A")
	  print(f"{alloy.name}: {property_to_check} = {value}")
```

- List type은 클래스다.

  ```python
  numbers = [1, 2, 3]   # new instance of 'List' object (internal data)

  numbers.append(4) # append is one of the methods in List class.
  				  # It changes the internal data
  ```

- 새로운 리스트와 비슷한 타입을 데이터/클래스를 다음과 같이 작성할 수도 있다!

  ```python
  class MyList:
  	def __init__(self, items=None):
  		if items is None:
  			self.items = []
  		else:
  			self.items = items

  	def append(self, value):
  		self.items += [value]

  	def __len__(self):
  		return len(self.items)

  	def __getitem__(self, index):
  		return self.items[index]

  	def __str__(self):
  		return str(self.items)
  ```

  그리고 아래에 괕이 실습해보자.

  ```python
  mylist = MyList([1, 2, 3]) ## 앞서 선언된 MyList 클래스.
  print(mylist)          # [1, 2, 3]

  mylist.append(4)
  print(mylist)          # [1, 2, 3, 4]

  print(len(mylist))     # 4
  print(mylist[2])       # 3
  ```

### 5.3.3. 여러 함수 만들어 보기

- Hooke's law

  $$
  \sigma = E \varepsilon
  $$

  ```python
  def hooke(modulus,epsilon):
  return modulus * epsilon
  ```

- 개념:

수식을 Python함수로 만들려면, 각 물리량을 뜻하는 기호에 적당한 이름을 붙여 변수로 지정해야 겠다. 나는 앞의 예제에서, 우선 첫번째로, 함수의 이름을 `hooke`이라 지었다. 그리고 변형률을 저장할 변수를 그에 해당하는 기호 $\varepsilon$ (epsilon)을 말 그대로 `epsilon`이라 지었고, 탄성계수(elastic modulus)에서 `modulus`를 사용했다. 같은 함수를 아래와 같이 작성할 수 있고, 정확히 같은 기능을 수행한다. 하지만, 전혀 추천되지 않는 이름들을 사용했다. 프로그램이 작고 간단할 때는 큰 문제가 되지 않을 수 있으나, 점점 프로그램이 커지고 복잡해지면 이와 같은 너무 간단한 이름은 선언될 때 본디 뜻하던 변수를 기억하기 쉽지 않고, 실수를 범하게 쉽게 만든다.

```python
def a(b,c):
return a*b
```

- Engineering strain & true strain

  $$
  \epsilon=\frac{\Delta l}{l_0}
  $$

  ```python
  def calc_engi_strain(l0,l1):
  delta_l=l1-l0
  return delta_l/l0
  ```

- True strain

  $$
  \varepsilon=\ln(\epsilon+1)
  $$

  ```python
  def calc_true_strain(engi_eps):
  import math
  true_eps=math.log(1+engi_eps) ## log function with base of e.
  return true_eps
  ```

- 예시: 길이 변화를 주면 true strain을 계산하는 함수를 작성하시오.

- Schmid law

  $$
  \tau=\sigma \cos\phi \cos\lambda
  $$

  ```python
  def schmid(sigma,phi,lamb):
  """
  Arguments
  ---------
  sigma: float
    uniaxial stress
  phi: float (in radian)
    angle between the slip plane normal and the loading direction
  lamb: float (in radian)
    angle between the slip direction and the loading direction

  Returns
  -------
  Schmid factor
  """
  import math
  return sigma*math.cos(phi)*math.cos(lamb)
  ```

- 위치 인자 (\*args); tuple

  ```python
  def poly(x,*args):
    """
    polynomial function

    y = a x^n + b x^(n-1) + c x^(n-2) ... z x^0

    Arguments
    ---------
    x,*args

    Returns
    -------
    y
    """
    n=len(args)-1 # highest order
    y=0.
    print('n,i,arg')
    for i, arg in enumerate(args):
  	  # print(n,i,arg)
  	  y+=arg*(x**n) #
  	  n-=1          # in descending order
    return y
  ```

- 키워드 인자 (keyword arguments; \*\*kwargs); dictionary 활용

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

## 5.4. 수업 03-2 (모듈 만들기)

### 5.4.1. 개념

- CLI (command-line interface)
- 모듈화 (modularization)
  - 프로그램을 기능별로 나뉘어 파일(모듈)로 분리
  - 코드 재사용성(reuseability) 향상, 유지보수 용이, 협업시 효율성 증가
  - 모듈(module)은 `.py` 파일을 가르킨다.
  - 패키지는 여러 모듈의 모임이다.
  - 라이브러리(library)는 모듈과 패키지의 모임.

### 5.4.2. 실습

#### 5.4.2.1. ex 01: 간단한 모듈 만들기 (더하기 곱하기)

1. 모듈 작성

```python
# 아래 모듈을 작성 후 mymodule.py로 저장하자.
def add(valuea, valueb):
	  return valuea + valueb

def multiply(valuea, valueb):
	  return valuea * valueb

def power(valuea, valueb):
	  return valuea ** valueb
```

2. 그 다음 아래를 활용해 mymodule을 불러와 보자.

```python
import mymodel
mymodule.add(3,4)
mymodule.multiply(3,4)
mymodule.power(3,4)
```

3. etc

- 작성된 모듈이 저장된 위치가 중요하다!
- 개개인이 활용하는 시스템:computer:의 환경변수 (windows의 경우)에 의해 행동이 달라질 수 있다.
- Linux/macOS의 경우에는 활용하는 shell의 닷 파일 (.sh, .bash, .zsh 등등)에서 지정된 $PATH 등의 변수에 의해 달라질 수 있다.

#### 5.4.2.2. ex 02: CLI에서 arguments 받기

- 1. 기초 모듈 작성

  ```python
  # file: ex02.py
  import sys
  if __name__ == "__main__":
    print("Arguments:", sys.argv)
  ```

- 2. Arguments의 역할을 이해하기 위해서 아래 실행

  - 2-1. Windows 환경

  ```sh
  c:\users\user\repo\mse> python ex02.py a b c 1 23
  ```

  - 2-2. MacOS/Linux 환경

  ```sh
  ~/repo/mse $ python ex02.py a b c 1 2 3
  ```

- 3. 실행 후 출력 결과 살펴보기

- 4. 더 상세한 argument parsing

  - 4-1. Argument parse 읽을 거리

  * [Argparse](https://docs.python.org/ko/3.7/library/argparse.html) 활용
  * [Argparse 자습서](https://docs.python.org/ko/3.7/howto/argparse.html#id1)

  - 4-2. 단계별로 작성해보기.

  * 4-2-1. 간단한 작동

    아래를 myprogram.py 파일(모듈)로 작성하여 저장하자.

    ```python
    import argparse
    if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.parse_args()
    ```

    그 다음 CLI에서 아래와 같이 명령문을 쳐보자.

    ```batch
    c:/users/user> python myprogram.py --help
    usage: main.py [-h]

    options:
    -h, --help  show this help message and exit
    ```

  * 4-2-2. positional argument

    다음으로 myprogram.py을 열어서 다음과 같이 수정해봅시다.
    `x` argument를 추가하였고, $x^2$을 출력합니다.

    ```python
    import argparse
    if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="the base")
    args=parser.parse_args()

    print(args.x**2)
    ```

  * 4-2-3. `--help` 기능

    아래와 같이 명령문을 입력하면 ...

    ```dos
    c:\users\user> python myprogram.py --help
    ```

    다음과 같이 출력되었나? 출력된 결과물을 살펴보자.

    ```dos
    usage: main.py [-h] x

    positional arguments:
    x           the base

    options:
    -h, --help  show this help message and exit

    ```

  * 4-2-4. 변경된 영향 확인

    명령어를 바꿔 다음과 같이 입력해보자.

    ```sh
    c:\users\user> python myprogram.py 3
    given x: 3
    x^2: 9
    ```

  * 4-2-5. Additional options

    a. 다음으로 myprogram.py을 열어서 다음과 같이 수정해봅시다.

    ```python
    import argparse

    def add(x,y):
      return x+y

    if __name__=='__main__':
      parser=argparse.ArgumentParser()
      parser.add_argument('x',type=int,help='the 1st base')
      parser.add_argument('y',type=int,help='the 2nd base')
      parser.add_argument('--myname',type=str,help='My Name')
      args=parser.parse_args()

      print('Myname:',args.myname)
      print('given x:', args.x)
      print('given y:', args.y)
      multiplied=add(args.x,args.y)
      print('x times y:', multiplie)
    ```

    b. CLI에서 아래를 실행하면

    ```dos
    c:\users\user> python main.py --help
    ```

    다음과 같이 `positional arguments`와 `options`이 출력된다.

    ```dos
    usage: main.py [-h] [--myname MYNAME] x y

    positional arguments:
    x                the 1st base
    y                the 2nd base

    options:
    -h, --help       show this help message and exit
    --myname MYNAME  My Name
    ```

    `--myname`옵션의 경우 `MYNAME`이라는 입력이 필요함을 알 수 있다.

    c. 실행해보자.

    ```dos
    c:\users\user> python main.py 3 4 --myname mike
    Myname: mike
    given x: 3
    given y: 4
    x times y: 7
    ```

#### 5.4.2.3. 예제

- 주어진 정수에 대한 구구단을 출력하는 CLI용 프로그램 만들어 보자.




<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

---