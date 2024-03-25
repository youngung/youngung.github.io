---
layout: page
title: Thin-walled tube
---

아래 python script는 W. F. Hosford & R. M. Caddell 의 Metal Forming의 chapter 4에 실린 삽화 4-4를 재현합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

def norm_pressure(P,K,t0_r0):
	return P/2/K/t0_r0

def hollomon(k,eps,n):
	return k*eps**n

fig=plt.figure(figsize=(9,4))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
eps=np.linspace(0,1,1000)

K=300 ## [MPa]
n=0.25
t0_r0=0.3



ax1.plot(eps,hollomon(K,eps,n))

p=[]
for i in xrange(len(eps)):
	dum=2.*K*eps[i]**n*t0_r0*np.exp(-3/2.*eps[i])
	p.append(dum)
ax2.plot(eps,p)
ylim0=ax2.get_ylim()
ax2.plot([n*2/3,n*2/3],[0,10000])


## labels
ax2.set_ylim(0,ylim0[1])
ax1.set_xlabel(r'$\bar{\varepsilon}$',fontsize=20)
ax2.set_xlabel(r'$\bar{\varepsilon}$',fontsize=20)
ax1.set_ylabel(r'$\bar{\sigma}$ [MPa]',fontsize=20)
ax2.set_ylabel('P (pressure) \n [MPa]',fontsize=15)
tight_layout()
```

<img src="/images/examples/output_2_0.png" width="600">


직접 Python을 활용하여 위를 실행할 계획이라면 [여기](https://github.com/youngung/lectures/blob/master/ipynb/fig4-4_metalforming_hosford%26caddell.ipynb)를 참고하세요.
