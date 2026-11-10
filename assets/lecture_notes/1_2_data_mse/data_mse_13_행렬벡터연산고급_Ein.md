---
layout: distill
title: 행렬·벡터 연산과 Einstein 표기법
description: 인덱스 표기, 수축 연산과 NumPy einsum의 기초
target: 1학년 2학기
permalink:
featured: true
prerequisite: NumPy 배열 활용, 벡터 연산 기초, 행렬 연산 기초
toc: false

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

**목차**

* TOC
{:toc}

# 1. 학습 목표

이 자료에서 $[\boldsymbol A]$, $[\boldsymbol x]$는 행렬·벡터의 성분을 모은 배열을 뜻한다.
행렬곱은 $[\boldsymbol A][\boldsymbol x]$처럼 붙여 쓴다.
[수축(tensor contraction)](https://en.wikipedia.org/wiki/Tensor_contraction)은 특정 인덱스에 대해 합산하여 결과의 인덱스 수를 줄이는 연산이다.
두 텐서의 곱을 수축할 때는 대응하는 성분을 곱해 합산한다. 이 장에서는 익숙한 벡터·행렬 연산을 예로 설명한다.


11·12장에서 익힌 연산을 새로운 연산으로 외우기보다, **원소별 수식 → 반복문 → NumPy 표현**으로 연결한다.
3–6절은 벡터·행렬 연산을 인덱스로 복습하고, 7절은 여러 축의 수축으로 확장한다.
8절에서는 10장의 브로드캐스팅을 다시 해석한다.

- 자유 인덱스와 합산 인덱스를 구분할 수 있다.
- 벡터·행렬 연산을 명시적인 합과 아인슈타인 합 규약으로 표현할 수 있다.
- <code>np.einsum</code>의 입력·출력 인덱스를 읽고 반복문과 비교할 수 있다.
- 축을 합산하는 수축과 길이 1인 축을 확장하는 브로드캐스팅을 구분할 수 있다.

# 2. [아인슈타인 표기법](https://ko.wikipedia.org/wiki/아인슈타인_표기법)과 [np.einsum](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html) 함수

참고 자료: [einsum 설명](https://rockt.ai/2018/04/30/einsum)

[아인슈타인 합 규약(Einstein summation convention)](https://en.wikipedia.org/wiki/Einstein_notation)은 한 항에서 두 번 나타나는 첨자에 대해
합산한다는 약속이다. 이 약속을 이용하면 벡터·행렬·텐서 연산의 합 기호($\sum$)를 생략하여
수식을 간결하게 쓸 수 있다.

아래 수식에서는 벡터를 $\boldsymbol a$처럼 굵게 쓰고,
스칼라와 개별 성분은 $a$, $a_i$처럼 보통 굵기로 쓴다.
수식 아래에 붙이는 성분 번호를 **첨자**라고 하며, 이 장에서는 코드와 연결하기 위해 **인덱스**라고도 부른다.

## 2.1. 자유 인덱스와 합산 인덱스

이 장의 2–7절 수식에서는 성분 번호를 1부터, Python 코드에서는 0부터 센다.
예를 들어 수식의 $a_1$은 코드의 <code>a[0]</code>이다.
8절에서는 길이 1인 축의 유일한 위치를 코드와 직접 비교하기 위해 수식도 0부터 센다.

12장의 행렬–벡터곱을 다시 쓰면

$$
c_i=\sum_{j=1}^{n}A_{ij}v_j
$$

이다. $i$는 결과의 성분을 선택하는 **자유 인덱스(free index)**, $j$는 합을 구한 뒤 사라지는
**합산 인덱스(summation index, dummy index)**다. 아인슈타인 합 규약에서는 한 항 안에서 두 번 나타나는 합산 인덱스의
합 기호를 생략하여 $c_i=A_{ij}v_j$로 쓴다.
반면 $c_i=a_i+b_i$에서는 오른쪽의 각 항에 $i$가 한 번씩 나타나므로 $i$를 합산하지 않는다.
인덱스의 반복은 등식 전체가 아니라 **각 항 안에서** 판단한다.

## 2.2. `einsum`의 명시적 출력 표기 미리 보기

이 장의 코드를 실행하기 전에 다음을 실행한다.

~~~python
import numpy as np
~~~

<code>np.einsum('ij,j->i', A, v)</code>에서 <code>ij</code>와 <code>j</code>는
각 입력 배열의 축 이름이며, <code>->i</code>는 결과에 <code>i</code> 축을 남긴다는 뜻이다.
입력에 있지만 출력에 없는 <code>j</code>를 합산한다.
따라서 12장의 <code>A @ v</code>와 같은 계산을 한다.
<code>np.einsum('i,i->', a, b)</code>는 모든 성분을 합산하여 내적 스칼라를 만든다.
반면 <code>np.einsum('i,i->i', a, b)</code>는 출력에 <code>i</code>를 남겨 원소별 곱 배열을 만든다.
아래 예제에서 이 차이를 확인하고, 7절에서 더 많은 축으로 확장한다.

<a id="3-벡터-스케일링-스칼라-곱"></a>

# 3. 벡터와 스칼라의 곱

벡터 $\boldsymbol a$에 스칼라 $c$를 곱한 결과를 $\boldsymbol b$라고 하자.
여기서 말하는 곱은 벡터에 수 하나를 곱하는 연산이며, 두 벡터의 내적과 구분한다.

$$
c\boldsymbol a=\boldsymbol b
$$

3성분 벡터라면 $b_1=ca_1$, $b_2=ca_2$, $b_3=ca_3$이다.
이를 인덱스 $i$를 사용하여 한 식으로 나타내면 다음과 같다.

$$
b_i=ca_i,\qquad i=1,2,3
$$

같은 계산을 Python 리스트와 NumPy 배열로 각각 구현해 보자.

{% tabs vector-scaling %}
{% tab vector-scaling 1. 리스트 %}

```python
# 리스트로 구현
c=0.3
a=[1,2,3]
b=[] # 빈 리스트
for i in range(3): # 각 성분에 대해 반복
   b.append(c*a[i])
```

{% endtab %}
{% tab vector-scaling 2. range와 len 활용 %}

```python
# len(a)를 사용하면 리스트의 길이에 맞춰 반복한다.
c=0.3
a=[1,2,3]
b=[] # 빈 리스트
for i in range(len(a)): # 각 성분에 대해 반복
   b.append(c*a[i])
```

{% endtab %}
{% tab vector-scaling 3. NumPy %}

```python
## NumPy로 구현
c=0.3
a=np.array([1,2,3])
b=c*a  # 10장에서 배운 배열과 스칼라의 브로드캐스팅
```

{% endtab %}
{% endtabs %}

# 4. 벡터의 크기

11장에서 배운 벡터의 크기를 인덱스로 다시 표현해 보자.
실수 성분으로 이루어진 벡터 $\boldsymbol a$의 크기는 다음과 같다.

$$|\boldsymbol a|=\sqrt{\sum_{i=1}^{3}a_i^2}$$

각 성분의 제곱을 같은 성분끼리의 곱으로 쓰면 $|\boldsymbol a|=\sqrt{\sum_{i=1}^{3}a_i a_i}$이고,
아인슈타인 합 규약으로는 $|\boldsymbol a|=\sqrt{a_i a_i}$로 쓸 수 있다.
<code>einsum</code>에서는 두 입력을 곱해 합산하거나, 먼저 각 원소를 제곱한 배열을 합산할 수 있다.
예를 들어 다음 벡터의 크기를 계산해 보자.

$$
\boldsymbol a= (2,3,4)
$$

```python
import numpy as np
a=np.array([2,3,4])
```

먼저 각 성분의 합 $2+3+4$를 구하려면 다음과 같이 쓴다.

```python
np.einsum('i->',a)
```

벡터의 크기를 구하려면 성분의 합이 아니라 **성분의 제곱합** $\sum_i a_i^2$이 필요하다.

```python
np.einsum('i->',a**2)
```

마지막으로 제곱합의 제곱근을 구한다.

```python
np.sqrt(np.einsum('i->',a**2))
```

같은 값은 NumPy의 선형대수 모듈에 있는 <code>np.linalg.norm(a)</code>로도 간단히 구할 수 있다.

<a id="5-단위-벡터-unit"></a>

# 5. 단위벡터 (unit vector)

크기가 1인 벡터를 단위벡터(unit vector)라고 한다.
0이 아닌 벡터 $\boldsymbol a$를 그 크기로 나누면 원래 벡터와 방향이 같은 단위벡터
$\widehat{\boldsymbol a}$를 얻는다. 영벡터는 방향이 없으므로 이 방법으로 정규화할 수 없다.

$$
\widehat{\boldsymbol a}=\frac{\boldsymbol a}{|\boldsymbol a|}
$$

각 성분을 인덱스로 나타내면 다음과 같다.

$$
\widehat{a}_i=\frac{a_i}{\sqrt{a_1^2+a_2^2+a_3^2}}
$$

위 식은 $i=1,2,3$인 세 성분에 각각 적용된다. 인덱스의 범위를 함께 쓰면

$$
\widehat{a}_i=\frac{a_i}{\sqrt{a_1^2+a_2^2+a_3^2}}, \text{ with } i=1,2,3
$$

이다. 범위가 문맥상 분명하면 $i=1,2,3$을 생략하기도 한다.
아래 탭은 같은 관계를 벡터 표기, 인덱스 표기, 성분별 전개로 나타낸 것이다.

{% tabs unit-vector-formulas %}
{% tab unit-vector-formulas 1. 굵은 글씨체 사용 %}

$$
\widehat{\boldsymbol a}=\frac{\boldsymbol a}{|\boldsymbol a|}
$$

{% endtab %}
{% tab unit-vector-formulas 2. 인덱스 범위 명시 %}

$$
\widehat{a}_i=\frac{a_i}{\sqrt{a_1^2+a_2^2+a_3^2}}, \text{ with } i=1,2,3
$$

{% endtab %}
{% tab unit-vector-formulas 3. 인덱스 범위 생략 %}

$$
\widehat{a}_i=\frac{a_i}{\sqrt{a_1^2+a_2^2+a_3^2}}
$$

{% endtab %}
{% tab unit-vector-formulas 4. 성분별 전개 %}

$$
\widehat{a}_1=\frac{a_1}{\sqrt{a_1^2+a_2^2+a_3^2}},
\ \ \
\widehat{a}_2=\frac{a_2}{\sqrt{a_1^2+a_2^2+a_3^2}},
\ \ \
\widehat{a}_3=\frac{a_3}{\sqrt{a_1^2+a_2^2+a_3^2}}
$$

{% endtab %}
{% endtabs %}
성분별로 전개한 식과 비교하며, 간결한 인덱스 표기가 어떤 계산을 뜻하는지 확인하자.
벡터 표기는 전체 관계를 보여 주고, 인덱스 표기는 각 성분의 계산을 보여 준다.
이 차이를 이해하면 다음 절의 합산 규칙도 읽기 쉽다.

# 6. 예제

<a id="61-같은-방향의-단위-벡터-구하기"></a>

## 6.1. 같은 방향의 단위벡터 구하기

벡터 $\boldsymbol a$와 방향이 같은 단위벡터를 구하는 Python 예제를 살펴보자.

{% tabs unit-vector-code %}
{% tab unit-vector-code 1. 수식 %}

$$
\widehat{a}_i=\frac{a_i}{\sqrt{a_1^2+a_2^2+a_3^2}}
$$

{% endtab %}
{% tab unit-vector-code 2. 리스트 %}

```python
a=[3,4,5]
magnitude=0. ## 벡터 크기
for i in range(len(a)):
	magnitude+=a[i]**2
magnitude=magnitude**0.5 # 제곱합의 제곱근
bar_a = [value / magnitude for value in a]
print(bar_a)
```

{% endtab %}
{% tab unit-vector-code 3. NumPy 구현 1 %}

```python
import numpy as np
old_a=np.array([3,4,5])
new_a=old_a**2
mag=np.sqrt(new_a.sum())
bar_a=old_a/mag
print(bar_a)
```

{% endtab %}
{% tab unit-vector-code 4. NumPy 구현 2 %}

```python
import numpy as np
old_a=np.array([3,4,5])
bar_a=old_a/np.sqrt((old_a**2).sum())
print(bar_a)
```

{% endtab %}
{% endtabs %}

리스트 구현의 <code>[value / magnitude for value in a]</code>는 리스트 컴프리헨션
(list comprehension)이다.[^list-comprehension]

[^list-comprehension]: 리스트 컴프리헨션은
    <code>[표현식 for 원소 in 반복가능객체]</code> 형태로 새 리스트를 만든다.
    여기서는 <code>a</code>의 각 <code>value</code>를 <code>magnitude</code>로 나눈 결과를
    차례로 모으며, 빈 리스트에 반복문으로 계산값을 <code>append()</code>하는 것과 같다.

## 6.2. 예시: 반대방향 벡터

벡터 $\boldsymbol a$와 크기는 같고 방향은 반대인 벡터 $\boldsymbol b$는 다음 관계를 만족한다.
{% tabs opposite-vector %}
{% tab opposite-vector 1. 벡터 표기 %}

$$
\boldsymbol a = - \boldsymbol b
$$

{% endtab %}
{% tab opposite-vector 2. 성분 표기 %}

$$
a_1 = -b_1,
\ \ \
a_2 = -b_2,
\ \ \
a_3 = -b_3
$$

{% endtab %}
{% tab opposite-vector 3. 인덱스 범위 명시 %}

$$
a_i = -b_i, \text{ with } i=1,2,3
$$

{% endtab %}
{% tab opposite-vector 4. 인덱스 범위 생략 %}

$$
a_i = -b_i
$$

{% endtab %}
{% tab opposite-vector 5. 리스트 %}

```python
a=[3,4,5]
b=[0,0,0]
for i in range(len(a)):
	b[i]=-a[i]
```

{% endtab %}
{% tab opposite-vector 6. NumPy %}

```python
a=np.array([3,4,5])
b=-a
```

{% endtab %}
{% endtabs %}

## 6.3. 예시: 벡터의 합

{% tabs vector-addition %}
{% tab vector-addition 1. 벡터 표기 %}

$$
\boldsymbol c =  \boldsymbol a + \boldsymbol b
$$

{% endtab %}
{% tab vector-addition 2. 성분 표기 %}

$$
c_1 = a_1+b_1,
\ \ \
c_2 = a_2+b_2,
\ \ \
c_3 = a_3+b_3
$$

{% endtab %}
{% tab vector-addition 3. 인덱스 범위 명시 %}

$$
c_i = a_i+b_i, \text{ with } i=1,2,3
$$

{% endtab %}
{% tab vector-addition 4. 인덱스 범위 생략 %}

$$
c_i =a_i + b_i
$$

{% endtab %}
{% tab vector-addition 5. 리스트 %}

```python
a=[3,4,5]
b=[3,-5,-2]
c=[0,0,0]
for i in range(len(a)):
	c[i]=a[i]+b[i]
```

{% endtab %}
{% tab vector-addition 6. NumPy %}

```python
a=np.array([3,4,5])
b=np.array([3,-5,-2])
c=a+b
```

{% endtab %}
{% endtabs %}

## 6.4. 예시: 벡터의 차

{% tabs vector-subtraction %}
{% tab vector-subtraction 1. 벡터 표기 %}

$$
\boldsymbol c =  \boldsymbol a - \boldsymbol b
$$

{% endtab %}
{% tab vector-subtraction 2. 성분 표기 %}

$$
c_1 = a_1-b_1,
\ \ \
c_2 = a_2-b_2,
\ \ \
c_3 = a_3-b_3
$$

{% endtab %}
{% tab vector-subtraction 3. 인덱스 범위 명시 %}

$$
c_i = a_i-b_i, \text{ with } i=1,2,3
$$

{% endtab %}
{% tab vector-subtraction 4. 인덱스 범위 생략 %}

$$
c_i =a_i - b_i
$$

{% endtab %}
{% tab vector-subtraction 5. 리스트 %}

```python
a=[3,4,5]
b=[3,-5,-2]
c=[0,0,0]
for i in range(len(a)):
	c[i]=a[i]-b[i]
```

{% endtab %}
{% tab vector-subtraction 6. NumPy %}

```python
a=np.array([3,4,5])
b=np.array([3,-5,-2])
c=a-b
```

{% endtab %}
{% endtabs %}

<a id="65-내적-inner-dot"></a>

## 6.5. 내적 (inner product)

두 벡터의 내적은 대응하는 성분을 곱한 뒤 모두 더한 값이며, 결과는 스칼라다.

$$
\boldsymbol a \cdot \boldsymbol b = \sum_{i=1}^{3} a_ib_i=c
$$

이를 [아인슈타인 합 규약](https://ko.wikipedia.org/wiki/아인슈타인_표기법)으로 나타내면

$$
\boldsymbol a \cdot \boldsymbol b = a_ib_i=c
$$

곱 $a_i b_i$ 안에서 $i$가 두 번 나타나므로 $i$에 대해 합산한다.
이 인덱스는 결과에 남지 않으므로 결과는 스칼라다.
이는 $c_i=a_i+b_i$처럼 각 항의 자유 인덱스 $i$가 결과에 남는 경우와 다르다.

{% tabs dot-product %}
{% tab dot-product 1. 리스트 1 %}

```python
# NumPy 없이 구현
a=[1,2,3]
b=[4,5,6]
c=0.
for i in range(3):
   c=c+a[i]*b[i]
print(c)
```

{% endtab %}
{% tab dot-product 2. 리스트 2 %}

```python
# NumPy 없이 구현
a=[1,2,3]
b=[4,5,6]
c=0.
for i in range(len(a)):
   c=c+a[i]*b[i]
print(c)
```

{% endtab %}
{% tab dot-product 3. NumPy %}

```python
import numpy as np
## NumPy로 구현
a=np.array([1,2,3])
b=np.array([4,5,6])
c=a*b  # 이 단계에서는 원소별 곱을 계산한다.
		## 즉 c=np.array([a[0]*b[0],a[1]*b[1],a[2]*b[2]])
c=c.sum()
print(c)

# 곱셈과 합산을 한 줄로 쓰면 다음과 같다.
c=(a*b).sum()
print(c)
```

{% endtab %}
{% tab dot-product 4. np.einsum %}

```python
import numpy as np
## NumPy로 구현
a=np.array([1,2,3])
b=np.array([4,5,6])
np.einsum('i,i->',a,b)
```

{% endtab %}
{% tab dot-product 5. 여러 NumPy 표현 %}

```python
import numpy as np
## NumPy로 구현
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.einsum('i,i->',a,b))
print(a@b)
print(np.dot(a,b))
print(np.inner(a,b))
print(np.sum(a*b))
```

{% endtab %}
{% endtabs %}

<a id="66-nxn행렬과-n벡터-곱"></a>

## 6.6. 행렬–벡터곱

다음은 $n\times n$ 행렬과 $n$성분 벡터의 곱이다.

$$
[\boldsymbol c] = [\boldsymbol A][\boldsymbol v]
$$

이를 인덱스로 나타내면 다음과 같다.

$$
c_i = \sum_{j=1}^{n}A_{ij}v_j \ \text{ for } i=1,2,...,n
$$

아인슈타인 합 규약으로 쓴 식과 계산 코드를 비교해 보자.

{% tabs matrix-vector-product %}
{% tab matrix-vector-product 1. 합 기호 생략 %}

$$
c_i=A_{ij}v_j
$$

{% endtab %}

{% tab matrix-vector-product 2. 리스트와 반복문 %}

```python
A=[[2,1],[3,1]]
v=[3,1]
n=2 # 2행 2열 행렬과 2성분 벡터
c=[0.0] * n
for i in range(n): # 결과의 각 성분을 0으로 초기화
   c[i]=0.
   for j in range(n): # 합산 인덱스 j에 대한 반복문
      c[i]=c[i]+A[i][j]*v[j]
print(c)
```

{% endtab %}
{% tab matrix-vector-product 3. NumPy 1 %}

```python
A=np.array([[2,1],[3,1]])
v=np.array([3,1])
n=2 # 2행 2열 행렬과 2성분 벡터
c=np.zeros(n)
for i in range(n): # 결과의 각 성분을 0으로 초기화
   c[i]=0.
   for j in range(n): # 합산 인덱스 j에 대한 반복문
      c[i]=c[i]+A[i,j]*v[j]
print(c)
```

{% endtab %}
{% tab matrix-vector-product 4. NumPy 2 %}

```python
A=np.array([[2,1],[3,1]])
v=np.array([3,1])
c=A@v
print(c)
```

{% endtab %}
{% tab matrix-vector-product 5. np.einsum %}

```python
A=np.array([[2,1],[3,1]])
v=np.array([3,1])
c=np.einsum('ij,j->i',A,v)
print(c)
```

{% endtab %}
{% endtabs %}

<a id="67-행렬-곱1-single-dot"></a>

## 6.7. 행렬곱과 단일수축

행렬곱에서는 한 쌍의 대응 인덱스에 대해 합산한다. 이를 **단일수축(single contraction)**이라고 한다.
두 행렬 $\boldsymbol A$, $\boldsymbol B$의 곱은 다음과 같다.

$$
C_{ij} = \sum_{k=1}^{n} A_{ik}B_{kj}, \qquad i,j=1,\ldots,n
$$

아래 코드는 $n=3$인 예제이며, 반복문과 행렬곱의 결과를 비교한다.

{% tabs matrix-product %}
{% tab matrix-product 1. 리스트 %}

```python
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[3,2,1],[6,5,4],[9,8,7]]
C=[]
for i in range(3): # C행렬의 각 행을 초기화
  C.append([])
  for j in range(3): # C의 i행 j열 원소를 0으로 초기화
    C[i].append(0)
    for k in range(3): # k에 대해 곱을 합산
      C[i][j]+=A[i][k]*B[k][j]
```

{% endtab %}
{% tab matrix-product 2. NumPy 1 %}

```python
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
C=np.zeros((3,3)) # 3행 3열 결과 배열을 0으로 초기화
for i in range(3):
	for j in range(3):
		for k in range(3):
			# 중첩 리스트와 달리 쉼표로
			# 각 축의 인덱스를 구분한다.
			C[i,j]+=A[i,k]*B[k,j]
print(C)
```

{% endtab %}
{% tab matrix-product 3. NumPy 2 %}

```python
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
# np.dot()으로 같은 행렬곱 계산
C=np.dot(A,B)
print(C)
```

{% endtab %}
{% tab matrix-product 4. NumPy 3 %}

```python
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
# @ 연산자로 같은 행렬곱 계산
C=A@B  # 이 예제의 정수 입력에서는 결과도 정수 배열이다.
print(C)
```

{% endtab %}
{% tab matrix-product 5. NumPy 4 %}

```python
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
np.einsum('ik,kj->ij',A,B)
```

{% endtab %}
{% endtabs %}

<a id="68-행렬-곱2-double-dot"></a>

## 6.8. 두 행렬의 이중수축

$$
c=\boldsymbol A : \boldsymbol B
$$

$$
\rightarrow c=\sum_i\sum_jA_{ij}B_{ij}=\sum_j\sum_iA_{ij}B_{ij}=\sum_j\sum_iB_{ij}A_{ij}=\sum_i\sum_jB_{ij}A_{ij}
$$

**이중수축(double contraction)**은 두 쌍의 대응 인덱스에 대해 합산하는 연산이다.
여기서는 두 행렬의 같은 위치에 있는 성분끼리 곱해 모두 더하므로 결과는 스칼라다.
아래 코드는 반복문의 순서와 곱셈 순서를 바꾸어도 같은 결과가 나오는지 확인한다.

```python
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[3,2,1],[6,5,4],[9,8,7]]
## 1
c=0.
for i in range(3): # 바깥쪽 반복문
  for j in range(3): # 안쪽 반복문
	  c+=A[i][j]*B[i][j]
print(c)
# 2. 두 반복문의 순서를 바꿈
c=0.
for j in range(3): # 바깥쪽 반복문
  for i in range(3): # 안쪽 반복문
    c+=A[i][j]*B[i][j]
print(c)
# 3. 반복문 순서와 성분을 곱하는 순서를 바꿈
c=0.
for j in range(3): # 바깥쪽 반복문
  for i in range(3): # 안쪽 반복문
    c+=B[i][j]*A[i][j] # A[i][j] x B[i][j] 혹은 B[i][j] x A[i][j]
print(c)
# 4. 각 항에서 성분을 곱하는 순서를 바꿈
c=0.
for i in range(3): # 바깥쪽 반복문
  for j in range(3): # 안쪽 반복문
    c+=B[i][j]*A[i][j] # A[i][j] x B[i][j] 혹은 B[i][j] x A[i][j]
print(c)
```

같은 계산을 NumPy 배열로 나타내면 다음과 같다.
첫 코드는 반복문으로 각 항을 더하고, 두 번째 코드는 <code>einsum</code>으로 두 인덱스를 모두 합산한다.

```python
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
##
c=0.
for i in range(3): # 바깥쪽 반복문
  for j in range(3): # 안쪽 반복문
    c+=A[i,j]*B[i,j]
```

```python
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[3,2,1],[6,5,4],[9,8,7]])
c=np.einsum('ij,ij->',A,B)
```

<a id="cross-product-indices"></a>

## 6.9. 외적의 인덱스 표현

11장에서 배운 3차원 외적은 다음과 같이 쓸 수 있다.

$$
c_i=\sum_{j=1}^{3}\sum_{k=1}^{3}\epsilon_{ijk}a_j b_k
=\epsilon_{ijk}a_j b_k.
$$

여기서 $i$는 자유 인덱스, $j,k$는 합산 인덱스다.
레비치비타(Levi-Civita) 기호 $\epsilon_{ijk}$는 $(i,j,k)$가 $(1,2,3)$의 순환 순열
$(1,2,3),(2,3,1),(3,1,2)$이면 $+1$, 그 반대 순서이면 $-1$이며,
인덱스가 하나라도 같으면 0이다.
예를 들어 $i=1$이면 0이 아닌 항은 두 개뿐이므로
$c_1=a_2b_3-a_3b_2$가 된다. 이는 11장의 $x$성분 식과 같다.
이 식은 오른손 좌표계를 이루는 직교정규 기저에서 사용하는 성분식이다.

# 7. np.einsum 활용

`np.einsum`은 **어떤 축에 대응하는 성분끼리 곱할지, 어떤 축에 대해 합산할지, 결과에 어떤 축을 남길지**를 인덱스 문자열로 지정한다.
앞의 벡터 내적과 행렬곱뿐 아니라, 세 개 이상의 축을 가진 배열의 수축에도 사용할 수 있다.
이 절에서는 실수 배열을 다룬다.

## 7.1. 입력 인덱스와 출력 인덱스 읽기

아래는 인덱스 문자열의 읽는 법을 보여 주는 표현이다.
실행에 필요한 <code>A</code>, <code>B</code>는 7.2절에서 만든다.

```python
C = np.einsum('ikl,lkj->ij', A, B)
```

위 문자열은 다음 순서로 읽는다.

1. 쉼표 앞의 `ikl`은 첫 번째 배열 `A`의 세 축에 붙인 이름이다.
2. 쉼표 뒤의 `lkj`는 두 번째 배열 `B`의 세 축에 붙인 이름이다.
3. `->ij`는 결과에 `i`, `j`를 이 순서로 남긴다는 뜻이다.
4. 입력에는 있지만 출력에는 없는 `k`, `l`은 합산한다.

인덱스 문자는 Python 변수명이 아니라 **배열 축의 이름표**다. 같은 이름으로 연결한 축은 크기가 맞아야 한다.
이 절의 예제는 같은 인덱스의 크기를 정확히 일치시킨다.

고전적인 아인슈타인 합 규약에서는 반복 인덱스를 합산하지만, `einsum`의 명시적 출력 표기는 이를 더 유연하게 지정한다.
예를 들어 `'i,i->i'`는 `i`를 출력에 남기므로 합산하지 않고 원소별 곱을 계산한다.
반대로 `'i->'`는 한 번만 나타난 `i`도 합산한다.
출력을 생략하면 결과 축의 순서가 인덱스 문자의 알파벳 순서로 정해지므로, 여기서는 **`->`를 명시하는 방식**을 사용한다.
세부 동작은 [NumPy 공식 문서](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html)를 참고한다.

## 7.2. 3차원 배열 두 개의 이중수축

`A.shape = (10, 3, 12)`, `B.shape = (12, 3, 8)`인 두 배열을 생각하자.
축이 세 개인 배열은 일반적인 2차원 행렬과 구분한다. 여기서는 아래에 정의한 수축을 수행한다.

$$
C_{ij}=\sum_{k=1}^{3}\sum_{l=1}^{12}A_{ikl}B_{lkj},
\qquad i=1,\ldots,10,\quad j=1,\ldots,8.
$$

| 인덱스 | `A`의 축과 크기 | `B`의 축과 크기 | 처리 |
| --- | --- | --- | --- |
| `i` | 첫째 축: 10 | 없음 | 결과의 첫째 축으로 유지 |
| `j` | 없음 | 셋째 축: 8 | 결과의 둘째 축으로 유지 |
| `k` | 둘째 축: 3 | 둘째 축: 3 | 합산 |
| `l` | 셋째 축: 12 | 첫째 축: 12 | 합산 |

자유 인덱스는 `i`, `j`이고, 합산 인덱스는 `k`, `l`이다.
따라서 결과는 `C.shape = (10, 8)`인 2차원 배열이다.
각 결과 성분은 $3\times12=36$개의 곱을 더한 값이다.
예를 들어 첫 번째 성분은

$$
C_{11}=\sum_{k=1}^{3}\sum_{l=1}^{12}A_{1kl}B_{lk1}
$$

이다. 수식에서는 인덱스를 1부터 표시했지만, Python에서는 0부터 시작하므로 첫 성분은 `C[0, 0]`이다.

먼저 두 예제가 공통으로 사용할 데이터를 만든다.

```python
import numpy as np

A = np.arange(10 * 3 * 12, dtype=float).reshape(10, 3, 12)
B = np.arange(12 * 3 * 8, dtype=float).reshape(12, 3, 8)
```

{% tabs tensor-contraction %}
{% tab tensor-contraction 1. 반복문 %}

```python
C_loop = np.zeros((A.shape[0], B.shape[2]))
for i in range(A.shape[0]):
    for j in range(B.shape[2]):
        for k in range(A.shape[1]):
            for l in range(A.shape[2]):
                C_loop[i, j] += A[i, k, l] * B[l, k, j]

print(C_loop.shape)  # (10, 8)
```

바깥의 두 반복문은 결과 성분을 선택한다. 안쪽의 두 반복문은 수식의 두 합을 계산한다.

{% endtab %}
{% tab tensor-contraction 2. einsum %}

```python
C_einsum = np.einsum('ikl,lkj->ij', A, B)
print(C_einsum.shape)  # (10, 8)
```

`k`, `l`을 출력에서 제외해 두 축을 수축하고, `i`, `j`만 남긴다.

{% endtab %}
{% endtabs %}

두 방법을 모두 실행한 뒤, 결과를 비교한다.

```python
print(np.allclose(C_loop, C_einsum))  # True
print(C_einsum[0, 0])                # 100800.0
```

`np.allclose`는 작은 부동소수점 오차를 허용하여 두 배열이 같은지 검사한다.
인덱스 순서가 맞는지도 확인하려면, 위처럼 원소마다 값이 다른 배열로 비교하는 것이 좋다.
합산되는 항의 개수는 모든 원소가 1인 별도 예제로 확인할 수 있다.

```python
A_ones = np.ones((10, 3, 12))
B_ones = np.ones((12, 3, 8))
C_ones = np.einsum('ikl,lkj->ij', A_ones, B_ones)
print(np.allclose(C_ones, 36))  # True: 각 성분은 1을 36번 더한 값
```

## 7.3. 앞에서 배운 연산과 비교하기

| 연산 | `einsum` 표현 | 같은 연산의 다른 표현 |
| --- | --- | --- |
| 벡터 내적 | `np.einsum('i,i->', a, b)` | `a @ b` |
| 벡터의 원소별 곱 | `np.einsum('i,i->i', a, b)` | `a * b` |
| 다이아딕 곱의 성분 배열 | `np.einsum('i,j->ij', a, b)` | `np.outer(a, b)` |
| 행렬·벡터 곱 | `np.einsum('ij,j->i', M, v)` | `M @ v` |
| 행렬곱 | `np.einsum('ik,kj->ij', M, N)` | `M @ N` |
| 두 행렬의 이중수축 | `np.einsum('ij,ij->', M, Q)` | `np.sum(M * Q)` |
| 행렬 전치 | `np.einsum('ij->ji', M)` | `M.T` |
| 대각 성분 추출 | `np.einsum('ii->i', M)` | `np.diag(M)` |
| 대각합(trace) | `np.einsum('ii->', M)` | `np.trace(M)` |

<code>-></code> 뒤에 출력 인덱스를 쓰지 않으면 결과는 스칼라다.
또한 같은 배열에 `ii`처럼 인덱스를 반복하면 대각 성분을 선택한다.
이를 출력에 남기면 대각 성분 배열이고, 제거하면 대각합이다.
다이아딕 곱(dyadic product, 여기서는 outer product)은 두 성분 $a_i b_j$를 모든 조합으로 곱해 배열을 만드는 연산이며,
11장의 벡터 외적(cross product) <code>np.cross</code>와 다르다.

## 7.4. 인덱스를 작성할 때 확인할 사항

- 입력 문자열의 인덱스 수와 각 배열의 축 수가 맞는지 확인한다.
- 합산하려는 축의 이름과 크기가 맞는지 확인한다. 위 예제에서 `B`가 `(12, 4, 8)`이면 `k`의 크기가 맞지 않아 오류가 발생한다.
- 결과에 남길 인덱스와 그 순서를 `->` 뒤에 적는다. 같은 입력에 `->ji`를 사용하면 결과는 `(8, 10)`이고 앞의 결과의 전치다.
- 단순 행렬곱에는 `@`도 명확한 표현이다. 여러 축을 수축할 때에는 `einsum`으로 수식을 직접 대응시킬 수 있다.

<a id="broadcasting-indices"></a>

# 8. 브로드캐스팅을 인덱스로 이해하기

[10장 8절]({% link assets/lecture_notes/1_2_data_mse/data_mse_10_NumPy기초2.md %})에서 배운
브로드캐스팅을 인덱스로 다시 해석해 보자. 앞에서 다룬 수축 연산과 달리,
브로드캐스팅 자체는 특정 축을 합산하지 않는다.

## 8.1. 원소별 연산과 인덱스

이 절에서는 NumPy와 같이 **인덱스를 0부터** 센다.
예를 들어 shape이 $(M,N)$인 배열 $A$의 원소를 $A_{ij}$라고 쓰면,
$i=0,\ldots,M-1$, $j=0,\ldots,N-1$이다.
아래 덧셈·뺄셈 수식의 인덱스는 결과의 위치를 지정한다.
각 항에서 한 번만 나타나는 자유 인덱스이므로, 등식의 여러 항에 같은 글자가 있어도 합산하지 않는다.
합산이 필요한 평균 식에서는 $\sum$를 명시한다.

먼저 행렬 $A$에 길이 $N$인 배열 $b$를 더하면

$$
C_{ij}=A_{ij}+b_j
$$

가 된다. $b_j$는 $i$와 무관하므로 모든 행에 같은 값이 적용된다.
반면 길이 $M$인 배열 $d$를 <code>A + d[:, None]</code>으로 더하면

$$
C_{ij}=A_{ij}+d_i
$$

가 된다. 이번에는 $d_i$가 $j$와 무관하므로 각 행의 모든 열에 같은 값이 적용된다.
**보정값에 어떤 인덱스가 남는지**를 보면 어느 축에 따라 값이 달라지는지 알 수 있다.

3차원 예제에서 $A$의 shape이 $(2,3,4)$이고 $B$의 shape이 $(3,1)$이면,
<code>C = A + B</code>는 다음 원소별 계산을 뜻한다.

$$
C_{ijk}=A_{ijk}+B_{j0},
\qquad
0\le i<2,\quad 0\le j<3,\quad 0\le k<4.
$$

$B$에는 첫 번째 축에 대응하는 인덱스가 없고, 마지막 축의 길이는 1이므로
그 축의 인덱스는 항상 0이다. 따라서 같은 $B_{j0}$를 모든 $i$와 $k$에 사용한다.

4차원 배열도 같은 방식으로 읽을 수 있다.
$A$의 shape이 $(2,1,4,1)$이고 $B$의 shape이 $(3,1,5)$이면

$$
C_{ijk\ell}=A_{i0k0}+B_{j0\ell},
\qquad
0\le i<2,\quad 0\le j<3,\quad 0\le k<4,\quad 0\le \ell<5.
$$

이다. 결과의 shape은 $(2,3,4,5)$다.
$j,\ell$이 바뀌어도 같은 $A_{i0k0}$를 사용하고, $i,k$가 바뀌어도 같은 $B_{j0\ell}$를 사용한다.

이를 임의 개수의 축으로 확장할 때도 원리는 같다.
**결과의 인덱스를 입력에 대응시키되, 입력에서 길이가 1인 축의 인덱스는 0으로,
왼쪽에 생략된 축의 인덱스는 입력에서 제외한다.**
브로드캐스팅은 이렇게 선택한 입력 원소끼리 연산하는 규칙이며,
내적이나 행렬곱처럼 특정 인덱스에 대해 합을 구하는 연산은 아니다.

## 8.2. 센서별·시점별 보정의 인덱스 표현

10장의 측정 데이터 예제를 다시 사용한다. 배열의 shape은 <code>(2, 3, 4)</code>이고,
축은 순서대로 시편, 시점, 센서를 뜻한다.

~~~python
import numpy as np

data = np.arange(24.0).reshape(2, 3, 4)
sensor_offset = np.array([10.0, 20.0, 30.0, 40.0])
time_offset = np.array([100.0, 200.0, 300.0])
corrected = data + sensor_offset
corrected_time = data + time_offset[None, :, None]
~~~

측정값을 $D_{ijk}$, 센서별 보정값을 $s_k$라고 쓰면 결과는

$$
C^{\mathrm{sensor}}_{ijk}=D_{ijk}+s_k
$$

이다. 여기서 $i$는 시편, $j$는 시점, $k$는 센서 인덱스다.
즉, <code>corrected[i, j, k] = data[i, j, k] + sensor_offset[k]</code>다.

시점별 보정값을 $t_j$라고 하면, 새 축을 추가한 배열 $T$의 원소는
$T_{0j0}=t_j$이고 결과는

$$
C^{\mathrm{time}}_{ijk}=D_{ijk}+T_{0j0}=D_{ijk}+t_j
$$

이다. 즉, <code>corrected_time[i, j, k] = data[i, j, k] + time_offset[j]</code>가 된다.
길이가 1인 축의 인덱스는 0으로 고정되고, 센서별 값에는 $k$만,
시점별 값에는 $j$만 남는다. 이처럼 수식을 먼저 쓰면
<code>None</code>을 어느 위치에 넣어야 하는지도 판단할 수 있다.

## 8.3. 평균의 합산과 브로드캐스팅 구분하기

~~~python
sensor_mean = data.mean(axis=2, keepdims=True)  # (2, 3, 1)
centered = data - sensor_mean                 # (2, 3, 4)
~~~

인덱스로 쓰면 네 센서의 평균과 평균을 뺀 값은 각각

$$
\mu_{ij}=\frac{1}{4}\sum_{q=0}^{3}D_{ijq},
\qquad
E_{ijk}=D_{ijk}-\mu_{ij}
$$

이다. 여기서 $q$는 평균을 구하기 위해 합산하는 센서 인덱스다.
<code>keepdims=True</code>로 만든 평균 배열을 $U$라고 쓰면
$U_{ij0}=\mu_{ij}$이고, NumPy의 뺄셈은

$$
E_{ijk}=D_{ijk}-U_{ij0}
$$

로 해석된다. 평균을 구할 때는 $q$에 대해 합산하지만,
평균을 뺄 때는 같은 $U_{ij0}$를 각 센서 $k$에 사용한다는 차이를 구분하자.

# 9. 정리

- 11·12장의 벡터·행렬 연산을 인덱스로 쓰면 결과의 축과 합산할 축을 구분할 수 있다.
- 자유 인덱스는 결과에 남고, 합산 인덱스는 합을 구한 뒤 사라진다.
- 아인슈타인 합 규약에서는 한 항 안에서 두 번 나타나는 인덱스의 합 기호를 생략한다.
- <code>einsum</code>의 명시적 출력 표기에서는 <code>-></code> 뒤에 남길 축을 직접 정한다.
- 브로드캐스팅에서는 길이 1인 축의 같은 원소를 여러 결과 위치에 사용한다.
- 인덱스의 범위와 입력·출력 shape을 확인하고, 반복문이나 기존 NumPy 연산으로 결과를 비교한다.

---

# 연습 문제

## 문제 1

아인슈타인 합 규약에서 한 항에 같은 첨자가 두 번 나타나면 무엇을 의미하는가?

<!--
풀이와 해답:
그 첨자에 대해 합을 취한다는 의미이다.
-->

## 문제 2

$A_{ij}b_j$에서 자유첨자를 쓰시오.

<!--
풀이와 해답:
i이다.
-->

## 문제 3

NumPy에서 Einstein 표기법 계산에 사용하는 함수는 무엇인가?

<!--
풀이와 해답:
np.einsum이다.
-->

## 문제 4: 합산과 원소별 곱

길이가 같은 실수 배열 <code>a</code>, <code>b</code>에 대해
<code>np.einsum('i,i->', a, b)</code>와 <code>np.einsum('i,i->i', a, b)</code>의
차이를 설명하고, 각각 같은 계산을 하는 NumPy 표현을 쓰시오.

<!--
풀이와 해답:
첫 번째는 i를 합산하는 내적으로 결과가 스칼라이며 a @ b와 같다.
두 번째는 i를 남기는 원소별 곱으로 결과 shape은 a.shape이며 a * b와 같다.
-->

## 문제 5: 브로드캐스팅의 인덱스 표현

<code>A.shape == (2, 3, 4)</code>, <code>b.shape == (3,)</code>일 때
<code>C = A + b[None, :, None]</code>의 결과 shape과 원소 $C_{ijk}$를 쓰시오.
이 문제에서는 인덱스를 0부터 센다.

<!--
풀이와 해답:
결과 shape은 (2, 3, 4)이고 C_ijk = A_ijk + b_j이다.
b의 새 축을 추가한 배열의 shape은 (1, 3, 1)이다.
i와 k에 대해 같은 b_j를 사용하며, 합산은 하지 않는다.
-->

---

[이전 강의](/assets/lecture_notes/1_2_data_mse/data_mse_12_행렬연산기초.md) · [강의 목록](/_lectures/1_2_data_mse.md) · [다음 강의](/assets/lecture_notes/1_2_data_mse/data_mse_14_기초_matplotlib1.md)
