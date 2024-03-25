---
layout: page
title: Pole figure
---

- 아래의 링크를 따라서 pole figure software를 download 받으세요.
  Find [texture](https://github.com/youngung/texture) at my GitHub repository.
- You will also need [Python](https://python.org) as well as various packages.
- And install the texture package on your system:
```
python setup.py build
python setup.py install --user
```

- I would recommend you to install [Anaconda Python](https://anaconda.org). You can find a short instruction [here]({% link anaconda.md %}), as well.
- Follow the instruction in [this webpage](https://github.com/youngung/texture) to plot the pole figure.


- Plot [1,1,1] pole figure of IF steel. Use the discrete orientation file available [here]({% link B_ST_06000.cmb %}).
  This file contains 6000 discrete orientations and their weights. Follow below procedure in Python.

Run below in terminal to launch ipython.
```bash
$ ipython --pylab
```

In the Python promprt, you can type below snippet of lines to create pole figures.

``` python
from TX import upf
myPF=upf.polefigure(filename='B_ST_06000.cmb',csym='cubic')
myPF.pf_new(poles=[[1,1,1],[1,1,0]])
```


You will find a pop-up window with the pole figures as below:

<img src='/images/pf.pdf' width='700'>


Also find a demonstration as below:
![image of az31 magnesium alloy](/images/tx_tutorial2.gif)
