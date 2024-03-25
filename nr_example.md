---
layout: page
title: Newton Raphson method for inhomogeneous specimen in tension
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

해당 페이지에서는 인장중인 시편의 불균질성을 고려한 방정식을
수치해석적으로 풀기 위한 방법을 다룹니다.

## 교재의 4-6 Fig.
자세한 설명은 [여기](https://github.com/youngung/lectures/blob/master/ipynb/fig4-6_metalforming_hosford%26caddell.ipynb)에서 얻을 수 있습니다.
위의 링크에서 찾을 수 있는 Jupyter notebook을 직접 활용하기 위해서는 사용중인 컴퓨터에 Anaconda Python이 설치되어야 합니다.
자세한 것은 [여기서]({% link anaconda.md%}) 찾으세요.

** Microsoft Excel을 활용한 방법은 [여기](https://youtu.be/lxwJ8XfAl80)에서 찾을 수 있습니다. **


## 교재의 5-10 Fig.
해당 논의와 관련된 Jupyter notebook은 [여기](https://github.com/youngung/lectures/blob/master/ipynb/fig5-10_metalforming_hosford%26caddell.ipynb)에서 살펴볼 수 있습니다.


## 교재의 Eq. 5-14

Eq. 5-14는 다음과 같은 미분 방정식입니다.

$$
\exp(-\varepsilon_a)\varepsilon_a^n\dot{\varepsilon}_a^m=f_0\exp(-\varepsilon_b)\varepsilon_b^n\dot{\varepsilon}_b^m
$$

위의 미분 방정식을 NR method를 사용하여 풀이하는 과정을 [여기](https://github.com/youngung/lectures/blob/master/ipynb/Eq5-14-Hosford-Caddell.ipynb)에서 찾아볼 수 있습니다.
