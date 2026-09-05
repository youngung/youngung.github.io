---
layout: distill
title: 함수와 클래스 활용
description: 재료공학 계산 함수와 간단한 클래스
target: 1학년 2학기
permalink:
featured: true
prerequisite: 함수 기초
toc:
  sidebar: left

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

- [1. 목표](#1-목표)
- [2. 클래스](#2-클래스)
- [3. 클래스 예제](#3-클래스-예제)
- [4. 여러 함수 만들어 보기](#4-여러-함수-만들어-보기)
  - [4.1. Hooke's law](#41-hookes-law)
  - [4.2. 공칭변형률과 진변형률](#42-공칭변형률과-진변형률)
  - [4.3. 길이 변화를 주면 true strain을 계산하는 함수](#43-길이-변화를-주면-true-strain을-계산하는-함수)
  - [4.4. Schmid law](#44-schmid-law)
  - [4.5. 위치 인자 (\*args)를 활용한 다항함수(polynomial function) 구하기](#45-위치-인자-args를-활용한-다항함수polynomial-function-구하기)
  - [4.6. 키워드 인자 (keyword arguments; \*\*kwargs) 활용 예시](#46-키워드-인자-keyword-arguments-kwargs-활용-예시)
  - [4.7. 여러 슬립계로 이루어진 재료에 가해진 응력에 따라, 가장 큰 분해 전단 응력을 가진 슬립계 찾기](#47-여러-슬립계로-이루어진-재료에-가해진-응력에-따라-가장-큰-분해-전단-응력을-가진-슬립계-찾기)

# 1. 목표

- 클래스를 이해한다.

# 2. 클래스

파이썬에서 클래스(Class)는 나만의 새로운 데이터 타입이나 객체를 만들기 위한 ‘설계도’라고
생각할 수 있다. 이 설계도를 바탕으로 실제로 만들어진 실체를 인스턴스(Instance) 또는 객체
(Object)라고 부른다.

```python
class Atom:
    def __init__(self):
        pass
    def add_density(self,val):
        self.density=val
    def add_structure(self,val):
        self.structure=val

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

  ```text
  getattr(object, name[, default])
  ```

  - object : 속성을 가져올 대상 객체
  - name : 속성 이름 (문자열로 지정)
  - default (선택적) : 해당 속성이 없을 경우 반환할 기본값 (없으면 AttributeError 발생)

# 3. 클래스 예제

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

# 4. 여러 함수 만들어 보기

## 4.1. Hooke's law

- 응력($\sigma$)와 변형률($\varepsilon$) 사이의 선형 관계 법칙

$$
\sigma = E \varepsilon
$$

```python
def hooke(modulus,epsilon):
  return modulus * epsilon
```

- 개념:

수식을 Python함수로 만들려면, 각 물리량을 뜻하는 기호에 적당한 이름을 붙여 변수로
지정해야겠다. 나는 앞의 예제에서, 우선 첫번째로, 함수의 이름을 `hooke`이라 지었다.
그리고 변형률을 저장할 변수를 그에 해당하는 기호 $\varepsilon$ (epsilon)을 말 그대로
`epsilon`이라 지었고, 탄성계수(elastic modulus)에서 `modulus`를 사용했다. 같은
함수를 아래와 같이 작성할 수 있고, 정확히 같은 기능을 수행한다. 하지만, 전혀 추천되지 않는
이름들을 사용했다. 프로그램이 작고 간단할 때는 큰 문제가 되지 않을 수 있으나, 점점 프로그램이
커지고 복잡해지면 이와 같은 너무 간단한 이름은 선언될 때 본디 뜻하던 변수를 기억하기 쉽지 않고,
실수를 범하게 쉽게 만든다.

```python
def a(b,c):
  return a*b
```

## 4.2. 공칭변형률과 진변형률

- 변형전 길이($l_0$)와 그 길이의 변화($\Delta l$)로 부터 공칭변형률 ($\epsilon$)
  구하기.

$$
\epsilon=\frac{\Delta l}{l_0}
$$

```python
def calc_engi_strain(l0,l1):
  delta_l=l1-l0
  return delta_l/l0
```

- True strain
  공칭 변형률로부터 진 변형률 계산하기

  $$
  \varepsilon=\ln(\epsilon+1)
  $$

```python
def calc_true_strain(engi_eps):
  import math
  # math.log: log function with base of Euler's number, 2.718...
  true_eps=math.log(1+engi_eps)
  return true_eps
```

## 4.3. 길이 변화를 주면 true strain을 계산하는 함수

## 4.4. Schmid law

- Schmid의 법칙을 활용하면, 일축 인장 (혹은 압축) 응력값($\sigma$)와 전위 슬립계
  (dislocation slip system)의 방위 관계 ($\phi,\lambda$)를 활용해 분해전단응력($\tau$)값을 구할 수 있다.

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

## 4.5. 위치 인자 (\*args)를 활용한 다항함수(polynomial function) 구하기

- 다항식의 규칙성을 이해해보자.
- 2차

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

## 4.6. 키워드 인자 (keyword arguments; \*\*kwargs) 활용 예시

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

## 4.7. 여러 슬립계로 이루어진 재료에 가해진 응력에 따라, 가장 큰 분해 전단 응력을 가진 슬립계 찾기

- 재료는 다양한 슬립계로 이루어져 있다. 주어진 슬립계를 class로 만들어 보자.
- 클래스로 객체를 만들때(instantiated) 주어진 응력에 대해 가장
  높은 분해 전단 응력 (Resolved shear stress)를 갖는 슬립계를
  찾도록 프로그램을 만들어 보자.

# 쉬운 연습 문제

## 문제 1

길이 변화량과 초기 길이를 받아 공칭변형률을 반환하는 식을 쓰시오.

<!--
풀이와 해답:
공칭변형률은 길이 변화량을 초기 길이로 나눈 값이다.
-->

## 문제 2

클래스로 만든 객체가 가지는 데이터 값을 일반적으로 무엇이라고 하는가?

<!--
풀이와 해답:
속성(attribute)이라고 한다.
-->

## 문제 3

Young 계수 200 GPa와 탄성변형률 0.001을 곱해 응력을 구하라.

<!--
풀이와 해답:
0.2 GPa, 즉 200 MPa이다.
-->
