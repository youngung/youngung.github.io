---
layout: distill
title: 파일 입출력
description: 키보드 입력과 텍스트 파일 읽기·쓰기의 기초
target: 1학년 2학기
permalink:
featured: true
prerequisite: Python 기초 자료구조, 조건문과 반복문
toc:
  sidebar: left
hidden: true
tabs: true
tikzjax: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

- [1. 학습 목표](#1-학습-목표)
- [2. 화면 출력과 키보드 입력](#2-화면-출력과-키보드-입력)
- [3. 문자열 포매팅](#3-문자열-포매팅)
- [4. 파일 입출력의 기본](#4-파일-입출력의-기본)
  - [4.1. 파일 열기 모드](#41-파일-열기-모드)
  - [4.2. with 문을 사용하는 이유](#42-with-문을-사용하는-이유)
- [5. 텍스트 파일 쓰기](#5-텍스트-파일-쓰기)
  - [5.1. 한 줄 쓰기](#51-한-줄-쓰기)
  - [5.2. 여러 줄 쓰기](#52-여러-줄-쓰기)
  - [5.3. 기존 내용 끝에 추가하기](#53-기존-내용-끝에-추가하기)
- [6. 텍스트 파일 읽기](#6-텍스트-파일-읽기)
  - [6.1. 파일 전체 읽기](#61-파일-전체-읽기)
  - [6.2. 한 줄씩 읽기](#62-한-줄씩-읽기)
  - [6.3. 모든 줄을 리스트로 읽기](#63-모든-줄을-리스트로-읽기)
- [7. 숫자 데이터 저장하고 읽기](#7-숫자-데이터-저장하고-읽기)
- [8. 예제: 성적 데이터 처리](#8-예제-성적-데이터-처리)
- [9. 여러 파일 다루기](#9-여러-파일-다루기)
- [10. 파일 이름 안전하게 바꾸기](#10-파일-이름-안전하게-바꾸기)
- [11. 오류가 발생했을 때](#11-오류가-발생했을-때)
  - [11.1. FileNotFoundError](#111-filenotfounderror)
  - [11.2. ValueError](#112-valueerror)
  - [11.3. PermissionError](#113-permissionerror)
- [12. 정리](#12-정리)
- [13. 쉬운 연습 문제](#13-쉬운-연습-문제)
  - [문제 1](#문제-1)
  - [문제 2](#문제-2)
  - [문제 3](#문제-3)
  - [문제 4](#문제-4)
  - [문제 5](#문제-5)
  - [문제 6](#문제-6)

# 1. 학습 목표

이번 강의가 끝나면 다음을 할 수 있어야 한다.

- 문자열과 숫자 입력을 구분할 수 있다.
- f-string을 사용하여 결과를 읽기 좋게 출력할 수 있다.
- <code>with open()</code>을 사용하여 텍스트 파일을 쓰고 읽을 수 있다.
- <code>r</code>, <code>w</code>, <code>a</code> 모드의 차이를 설명할 수 있다.
- 한 줄씩 저장된 숫자를 읽어 합계와 평균을 계산할 수 있다.
- 파일 이름을 바꾸기 전에 변경 결과를 미리 확인할 수 있다.

# 2. 화면 출력과 키보드 입력

<code>print()</code>는 값을 화면에 출력하고, <code>input()</code>은 키보드 입력을
**문자열**로 받는다.

~~~python
name = input("이름을 입력하세요: ")
print("안녕하세요,", name)
~~~

- **중요:** <code>input()</code>의 결과는 항상 **문자열**이다.

따라서 다음 코드는 숫자 덧셈을 하지 않는다.

~~~python
value1 = input("첫 번째 값: ")
value2 = input("두 번째 값: ")

print(value1 + value2)
~~~

2와 3을 입력하면 문자열을 연결한 <code>23</code>이 출력된다. 숫자로 계산하려면
<code>int()</code> 또는 <code>float()</code>로 변환해야 한다.

~~~python
value1 = float(input("첫 번째 값: "))
value2 = float(input("두 번째 값: "))

print(value1 + value2)
~~~

빈 줄을 입력할 때까지 여러 값을 더하는 프로그램은 다음과 같다.

~~~python
total = 0.0
while True:
    text = input("값을 입력하세요. 종료하려면 Enter: ")
    if text == "":
        break
    total += float(text)

print("합계:", total)
~~~

평균을 구하려면 합계뿐 아니라 입력한 값의 개수도 저장해야 한다.

~~~python
total = 0.0 ## 합계 (float)
count = 0   ## 값의 개수 (integer)

while True:
    text = input("값을 입력하세요. 종료하려면 Enter: ")
    if text == "":
        break
    total += float(text)
    count += 1

if count > 0:
    average = total / count
    print("평균:", average)
else:
    print("입력된 값이 없습니다.")
~~~

# 3. 문자열 포매팅

계산 결과를 문자열 안에 넣을 때는 f-string을 사용하면 편리하다.

~~~python
name = "Iron"
density = 7.87

print(f"The density of {name} is {density:.2f} g/cm^3")
~~~

<code>{density:.2f}</code>는 실수를 소수점 아래 둘째 자리까지 표시한다.

~~~python
value = 9 / 6

print(f"{value:.1f}")
print(f"{value:.5f}")
~~~

Python 코드에서는 다음과 같은 <code>%</code> 포매팅을 볼 수도 있다.

~~~python
print("The density of %s is %.2f g/cm^3" % (name, density))
~~~

변수와 출력 위치를 한눈에 확인하기 쉬운 f-string이 더욱 선호되는 방식이다.
실수에 <code>%d</code>를 사용하면 소수 부분이 표시되지 않으므로 주의한다.

# 4. 파일 입출력의 기본

Python에서는 <code>open()</code>으로 파일 객체를 만든 뒤 내용을 읽거나 쓴다.

~~~text
open(파일이름, 모드, encoding="utf-8")
~~~

텍스트 파일에서는 한글을 안정적으로 다루기 위해 <code>encoding="utf-8"</code>을
명시하는 것이 좋다. 영문으로만 작성한다면 <code>encoding</code>을 생략해도 된다. <code>open()</code>으로 연 파일은 반드시 <code>close()</code>로 닫아야 한다. <code>with</code> 문을 사용하면 블록을 벗어날 때 자동으로 닫힌다.


## 4.1. 파일 열기 모드

| 모드 | 의미 | 파일이 없을 때 | 파일이 있을 때 |
|---|---|---|---|
| <code>"r"</code> | 읽기(read) | 오류 발생 | 기존 내용 읽기 |
| <code>"w"</code> | 쓰기(write) | 새 파일 생성 | 기존 내용 삭제 후 쓰기 |
| <code>"a"</code> | 추가(append) | 새 파일 생성 | 기존 내용 끝에 추가 |
| <code>"rb"</code> | 이진 파일 읽기 | 오류 발생 | bytes로 읽기 |
| <code>"wb"</code> | 이진 파일 쓰기 | 새 파일 생성 | 기존 내용 삭제 후 쓰기 |

> **주의:** <code>"w"</code> 모드는 기존 내용을 지운다. 중요한 파일에는 바로 사용하지
> 말고 새 파일 이름으로 먼저 시험한다. <code>"binary"</code>라는 모드는 없으며 이진
> 파일에는 <code>"rb"</code> 또는 <code>"wb"</code>를 사용한다.

## 4.2. with 문을 사용하는 이유

파일 사용이 끝나면 파일을 닫아야 한다. <code>with</code> 문을 사용하면 블록을
벗어날 때 파일이 자동으로 닫힌다.

~~~python
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello, file!\n")
~~~

- 즉 아래 둘 중 하나의 방법을 사용해야 한다.
~~~python
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello, file!\n"

# 또는

file = open("example.txt", "w", encoding="utf-8")
file.write("Hello, file!\n")
file.close()
~~~

이 강의에서는 파일을 열 때 항상 <code>with open(...)</code> 형식을 사용한다.

# 5. 텍스트 파일 쓰기

## 5.1. 한 줄 쓰기

~~~python
with open("material.txt", "w", encoding="utf-8") as file:
    file.write("Aluminum\n")
~~~

<code>write()</code>는 줄바꿈을 자동으로 넣지 않는다. 다음 줄로 이동하려면
<code>\n</code>을 직접 써야 한다.

## 5.2. 여러 줄 쓰기

~~~python
lines = [
    "Aluminum\n",
    "Iron\n",
    "Copper\n",
]

with open("materials.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
~~~

## 5.3. 기존 내용 끝에 추가하기

~~~python
with open("materials.txt", "a", encoding="utf-8") as file:
    file.write("Titanium\n")
~~~

# 6. 텍스트 파일 읽기

아래의 재료 정보가 text 파일 ```materials.txt```에 저장되어 있다.

| Name | density | strength |
|------|---------|----------|
| Fe   |    7.87 |    200
| Al    |   2.7  |    90
| Ti    |   4.51 |    240

```txt
name density strength
Fe   7.87     200
Al   2.7       90
Ti   4.51     240
```

## 6.1. 파일 전체 읽기

~~~python
with open("materials.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
~~~

## 6.2. 한 줄씩 읽기

큰 파일은 한 줄씩 처리할 수 있다.

~~~python
with open("materials.txt", "r", encoding="utf-8") as file:
    for line in file:
        material = line.strip()
        print(material)
~~~

<code>strip()</code>은 문자열 양 끝의 줄바꿈(```\n```)과 공백을 제거한다.

## 6.3. 모든 줄을 리스트로 읽기

~~~python
with open("materials.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
~~~

# 7. 숫자 데이터 저장하고 읽기

1부터 10까지의 정수(integer)를 한 줄에 하나씩 저장해 보자.

~~~python
with open("numbers.txt", "w", encoding="utf-8") as file:
    for number in range(1, 11):
        file.write(f"{number}\n")
~~~

파일에서 읽은 값도 문자열이므로 계산 전에 숫자로 변환한다.

~~~python
numbers = []

with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        number = int(line.strip())
        numbers.append(number)

total = sum(numbers)
average = total / len(numbers)

print(f"합계: {total}")
print(f"평균: {average:.1f}")
~~~

# 8. 예제: 성적 데이터 처리

다음 [성적 데이터 파일](/assets/dat_files/lectures/1_2_data_mse/score_records/score_record_2017_MF_final_analysis.txt)은
학생 번호와 점수를 공백으로 구분하여 저장한다. 처음 두 줄은 머리글이므로 건너뛴다.

~~~text
ID Score
--------------
xxxx5093  14.0
xxxx5298  53.0
~~~

먼저 학생 번호와 점수를 읽어 보자.

~~~python
filename = "score_record_2017_MF_final_analysis.txt"

student_ids = []
scores = []

with open(filename, "r", encoding="utf-8") as file:
    next(file)
    next(file)

    for line in file:
        columns = line.split()

        if len(columns) != 2:
            continue

        student_id = columns[0]
        score = float(columns[1])

        student_ids.append(student_id)
        scores.append(score)
~~~

링크에서 파일을 내려받아 실행 중인 Notebook과 같은 폴더에 저장한다. 다른 폴더에
저장했다면 실제 위치를 <code>filename</code>에 지정한다. 웹 주소와 컴퓨터에서 Python이
읽는 로컬 파일 경로는 서로 다를 수 있음에 주의한다.

평균, 표준편차, 최고점과 최저점을 계산한다.

~~~python
average = sum(scores) / len(scores)

squared_sum = 0.0
for score in scores:
    squared_sum += (score - average)**2

standard_deviation = (
    squared_sum / len(scores)
)**0.5

highest_score = max(scores)
lowest_score = min(scores)

highest_index = scores.index(highest_score)
lowest_index = scores.index(lowest_score)

print(f"평균: {average:.2f}")
print(f"표준편차: {standard_deviation:.2f}")
print(
    "최고점:",
    student_ids[highest_index],
    highest_score,
)
print(
    "최저점:",
    student_ids[lowest_index],
    lowest_score,
)
~~~

최고점이 같은 학생이 여러 명이면 <code>index()</code>는 첫 번째 학생만 반환한다.
동점자를 모두 찾는 것은 이후 반복문 연습으로 확장할 수 있다.

# 9. 여러 파일 다루기

<code>pathlib</code>의 <code>glob()</code>을 사용하면 특정 형식의 파일을 찾을 수 있다.

~~~python
from pathlib import Path


data_folder = Path("score_records")

for path in data_folder.glob("*.txt"):
    print(path.name)
~~~

다음 압축 파일을 내려받아 여러 성적 파일을 대상으로 실습할 수 있다.

- [여러 성적 파일](/assets/dat_files/lectures/1_2_data_mse/score_records/all_scores/scores.zip)

처음에는 파일 이름만 출력하여 선택된 파일이 맞는지 확인한다. 그다음 각 파일을 읽는
함수를 만들어 반복 적용할 수 있다.

# 10. 파일 이름 안전하게 바꾸기

다음 [인장시험 파일](/assets/dat_files/lectures/1_2_data_mse/tensile_test_results.zip)의
파일 이름에서 <code>WZ</code>를 <code>EX</code>로 바꾼다고 하자.

파일 이름 변경은 원래 경로를 바꾸는 작업이므로 먼저 변경 계획만 출력한다.

~~~python
from pathlib import Path


data_folder = Path("tensile_test_results")

for old_path in data_folder.glob("*WZ*.csv"):
    new_name = old_path.name.replace("WZ", "EX")
    new_path = old_path.with_name(new_name)

    print(f"{old_path.name} -> {new_path.name}")
~~~

출력된 대상과 새 이름이 모두 올바른지 확인한 뒤에만 다음 줄을 반복문 안에 추가한다.

~~~python
old_path.rename(new_path)
~~~

> **안전 확인:** 원본 파일이 중요하면 먼저 폴더 전체를 복사해 두고 연습한다. 새 이름의
> 파일이 이미 존재하는지도 확인해야 한다.

복사하려면 <code>shutil.copy()</code>를 사용한다.

~~~python
from shutil import copy


copy(old_path, new_path)
~~~

# 11. 오류가 발생했을 때

## 11.1. FileNotFoundError

지정한 위치에 파일이 없을 때 발생한다.

~~~python
from pathlib import Path


path = Path("materials.txt")
print(path.exists())
print(path.resolve())
~~~

<code>exists()</code>로 파일 존재 여부를 확인하고, <code>resolve()</code>로 Python이
확인하는 전체 경로를 살펴본다.

## 11.2. ValueError

<code>float()</code>나 <code>int()</code>로 바꿀 수 없는 문자를 숫자로 변환할 때
발생할 수 있다. 빈 줄이나 머리글인지 먼저 확인한다.

## 11.3. PermissionError

파일을 쓸 권한이 없거나 다른 프로그램이 파일을 사용 중일 때 발생할 수 있다.
쓰기 가능한 실습 폴더인지 확인한다.

# 12. 정리

- <code>input()</code>은 항상 문자열을 반환한다.
- 파일은 <code>with open(...)</code>으로 열면 자동으로 닫힌다.
- <code>"r"</code>은 읽기, <code>"w"</code>는 새로 쓰기, <code>"a"</code>는 이어 쓰기 모드이다.
- 한글이 포함된 텍스트 파일에는 <code>encoding="utf-8"</code>을 명시하는 것이 좋다.
- 파일에서 읽은 숫자는 <code>int()</code> 또는 <code>float()</code>로 변환해야 한다.
- 파일 이름을 바꾸기 전에는 대상과 새 이름을 먼저 출력하여 확인한다.

# 13. 쉬운 연습 문제

## 문제 1

<code>input()</code>이 반환하는 자료형은 무엇인가?

<!--
풀이와 해답:
문자열 str이다.
-->

## 문제 2

텍스트 파일을 읽기 모드로 여는 표현을 쓰시오.

<!--
풀이와 해답:
with open("data.txt", "r", encoding="utf-8") as file:
처럼 작성할 수 있다.
-->

## 문제 3

기존 파일 내용을 지우지 않고 끝에 내용을 추가하려면 어떤 모드를 사용하는가?

<!--
풀이와 해답:
"a" 모드를 사용한다.
-->

## 문제 4

다음 코드가 파일에 기록하는 내용을 쓰시오.

~~~python
with open("value.txt", "w", encoding="utf-8") as file:
    file.write("10\n")
    file.write("20\n")
~~~

<!--
풀이와 해답:
첫 줄에는 10, 둘째 줄에는 20이 기록된다.
-->

## 문제 5

파일에서 읽은 문자열 <code>"3.5"</code>를 실수로 변환하는 표현을 쓰시오.

<!--
풀이와 해답:
float("3.5")
-->

## 문제 6

<code>"w"</code> 모드를 기존의 중요한 파일에 사용할 때 주의해야 하는 이유를 쓰시오.

<!--
풀이와 해답:
기존 파일의 내용을 지우고 처음부터 새로 쓰기 때문이다.
-->
