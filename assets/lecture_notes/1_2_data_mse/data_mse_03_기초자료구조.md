---
layout: distill
title: 데이터 재료과학 (제 3강)
description:
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

- [1. 목표](#1-목표)
- [2. List](#2-list)
- [3. Tuple](#3-tuple)
- [4. Set](#4-set)
- [5. Dictionary](#5-dictionary)
- [6. Misc.](#6-misc)
- [7. Take-home 실습](#7-take-home-실습)


# 1. 목표
- List, Tuple, Dictionary, set 의 자료 구조 이해하기


# 2. List

- 특징:
  - 수정 가능(mutable): 추가, 삭제, 변경 가능
  - 중복 허용
  - 순서 있음 (ordered)
  - 여러 자료형 혼합해서 저장 가능

- 리스트 생성 - 대괄호 사용 `[]`
  아래 실습해보기
  ```python
  elements = ["H", "He", "Li", "Be"]
  ```
  vs code에서 살펴보기

- 요소 접근 (인덱싱; indexing); 0에서 부터 시작

  ```python
  print(elements[0])   # H
  ```

- 요소 변경

  ```python
  elements[1] = "Helium"
  print(elements)     #elements = ["H", "Helium", "Li", "Be"]
  ```

- 요소 추가 / 삭제

  ```python
  elements.append("B")   #elements = ["H", "Helium", "Li", "Be", "B"]
  elements.remove("Li")  #elements = ["H", "Helium", "Be", "B"]
  ```

- 중복 허용

  ```python
  elements = ['H','He','H']
  print(elements)
  ```

- 여러 자료형 혼합

  ```python
  myList=['H',203,2.3,['H','He']]
  myMatrix=[[1,2,3],[4,5,6],[7,8,9]] ##중첩된 리스트
  ```

- 언패킹 (unpacking)

  ```python
  a,b,c,d=[1,3,4,5]
  ```

# 3. Tuple

- 특징

  - 수정 불가능 (immutable); 한번 만들어지면 이후 변경 불가능
  - 중복 허용
  - 순서 있음
  - 여러 자료형 혼합해서 저장 가능

- 튜플 생성 - 소괄호 `()` 사용

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

# 4. Set

- 특징

  - 중복제거: 같은 값이 입력되어도 하나만 남게 됨
  - 순서없음
  - 인덱싱 불가: list나 tuple과 다름
  - 수정 가능 (mutable)
  - 원소의 타입에 제한 **있음**:

- 실습

  - 실습1: 생성

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

  - 실습2: 변경

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

# 5. Dictionary

- 특징

  - 키(key)와 값(value)을 짝지어(패어) 저장하는 자료구조.
  - 순서 있음
  - 값 중복 가능
  - 키는 변경 불가능(immutable)

- 실습

  - 실습1: 생성

  ```python
  # - 딕셔너리 생성
  Fe = {
  	"name": "iron",
  	"structure": 'fcc',
  	"density": "7.874",
  	"density_unit": 'g/cm^3'
  }
  ```

  - 실습2: 값 접근(access)

  ```python
  print(Fe) # 전체 키/값 짝 출력
  print(Fe.keys()) # 키들만 출력
  print(Fe['name']) # 'name'키의 값
  print(Fe.get('name')) # 'name'키에 해당하는 값
  ```

  - 실습3: 값 변경

  ```python
  Fe.update(CTE=12e-6)
  ```

<!-- * 정리

	| 특징          | List (리스트)                         | Tuple (튜플)              | Dictionary (딕셔너리)              |
	|--------------|--------------------------------------|-------------------------|-----------------------------------|
	| 선언 방식      | `my_list = [1, 2, 3]`                | `my_tuple = (1, 2, 3)`  | `my_dict = {"a": 1, "b": 2}`      |
	| 변경 가능성     | ✅ 변경 가능 (mutable)                 | ❌ 변경 불가 (immutable)  | ✅ 값(value) 변경 가능 (muable)       |
	| 인덱싱/슬라이싱  | ✅ 지원                               | ✅ 지원                  | ❌ key를 통한 접근만 가능               |
	| 데이터 순서     | ✅ 순서 유지 (Python 3.7+ 보장)         | ✅ 순서 유지              | ✅ 순서 유지 (Python 3.7+ 보장)        |
	| 중복 허용      | ✅ 허용                               | ✅ 허용                  | ❌ key는 중복 불가 (value는 가능)       |
	| 사용 목적      | 여러 데이터를 순차적으로 저장/관리            | 고정된 데이터를 안전하게 저장 | key-value 구조로 빠른 탐색 및 매핑       |
	| 대표 메서드     | `append`, `extend`, `remove`, `sort` | 없음 (불변이므로)          | `keys`, `values`, `items`, `update`|
 -->

# 6. Misc.

- `len` built-in function중 하나 (함수에 대한 수업은 차후에 다시 진행할 예정)

  ```python
  a=[3,4,5,'a','b']
  len(a) # 정수 5
  ```

- List slicing
  ```python
  a=[0,1,2,3,4,5]
  # format
  # a[begin:end:step]; end-begin = len(a)
  a[::] # == a[0:6:1] ## default
  a[1::2] # == a[1:6:2]
  ```

# 7. Take-home 실습

- 1족 원소 기호를 순서대로 포함한 리스트 만들기 (수소, 리튬, 나트륨, 칼륨, 루비듐, 세슘, 프랑슘)
- Calister 예제 2.1

```python
#세륨의 동위원소는 4가지 존재한다:
# 각 동위원소의 분율은 아래와 같다.
Ce_f= [0.185, 0.251, 88.450, 11.114]  #[%]
# 각 동위원소의 원자량은 아래와 같다.
Ce_w = [135.907, 137.906, 139.905, 141.909]
# 세륨의 평균 원자량은 얼마인가?
avg=(Ce_f[0]*Ce_w[0]+ Ce_f[1]*Ce_w[1]+ Ce_f[2]*Ce_w[2]+ Ce_f[3]*Ce_w[3])/(Ce_f[0]+Ce_f[1]+Ce_f[2]+Ce_f[3])
## average
print(avg)
```

---