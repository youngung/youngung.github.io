---
layout: page
title: Euler angle 과 결정립의 방위
---

# Euler angle


<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML">
</script>



재료공학에서, 특히 집합조직과 관련하여, 시편에 대한 결정립의 방위는 Euler angles로 표현이 되곤 한다.
여기서 우리는 z-x-z convention을 따르는 Euler angles로 세축에 대한 sequential한 회전으로 transformation matrix를 만들 수 있다.
여기서 z, x, 그리고 다시 z축에 대한 회전을 각각 $$\phi_1, \Phi, $$ 그리고 $$\phi_2$$ 값으로 표현이 된다.
각 회전에 의한 rotation matrix (혹은 각 회전에 해당하는 transformation matrix)는 다음과 같이 정의 된다.

$$R^{\phi_1} = \begin{bmatrix} \cos \phi_1 & \sin \phi_1  & 0 \\ -\sin\phi_1 & \cos\phi_1 & 0 \\ 0 & 0& 1 \end{bmatrix}$$


$$R^\Phi = \begin{bmatrix} 1 & 0 & 0 \\ 0 &\cos\Phi &\sin\Phi \\ 0 & -\sin\Phi & \cos\Phi \end{bmatrix}$$


$$R^{\phi_2} = \begin{bmatrix} \cos \phi_2 & \sin \phi_2  & 0 \\ -\sin\phi_2 & \cos\phi_2 & 0 \\ 0 & 0& 1 \end{bmatrix}$$


위 세 rotation (transformation) matrices를 조합하여 세 Euler angle에 의한 coordinate transformation matrix를 구할 수 있다:

$$R_{ij}=R^{\phi_2}_{ik}R^{\Phi}_{kl}R^{\phi_1}_{lj}$$


## Visualization of the three sequential rotations (transformation) by the three Euler angles.
- 아래의 스크립트를 사용하여 서로 misoriented된 두 좌표계를 그릴 수 있습니다.

- Use below script to generate two coordinate systems that are misoriented from each other.

```latex
\documentclass{standalone}
\usepackage{tikz}
\usepackage{tikz-3dplot}
\usepackage{pgfplots}

\begin{document}

%% Below is to rotates it based on z-x`-z`` sequence
\tdplotsetmaincoords{50}{230}
\pgfmathsetmacro{\ph}{40}
\pgfmathsetmacro{\ps}{40}
\pgfmathsetmacro{\omega}{25}
\pgfmathsetmacro{\rad}{3}
\pgfmathsetmacro{\rect}{0.5}

\begin{tikzpicture}[tdplot_main_coords]
  %% initial coord
  \draw[ultra thick,->,>=stealth] (0,0,0) -- (0,\rad,0) node[anchor=north east]{$x^s$};
  \draw[ultra thick,->,>=stealth] (0,0,0) -- (-\rad,0,0) node[anchor=north]{$y^s$};
  \draw[ultra thick,->,>=stealth] (0,0,0) -- (0,0,\rad) node[anchor=south]{$z^s$};%{$z^s//$} node[anchor=south,black,xshift=12,yshift=2]{$z^1$};
  \tdplotdrawarc[black,thin, dashed] {(0,0,0)} {\rad}{90}{180+\ph}{}

  %% rotated coord 1
  \tdplotsetrotatedcoords{\ph}{0}{0}
  \draw[thin,densely dotted, black,->,tdplot_rotated_coords] (0,0,0) -- (0,\rad,0) node[anchor=north,black]{};%{$x^1//x^2$};
  \draw[thin,dotted,black,->,tdplot_rotated_coords] (0,0,0) -- (-\rad,0,0) node(y1)[anchor=west,black]{};%{$y^1$};
  \tdplotdrawarc[black,->          ]{(0,0,0)}{\rad/6.}{90} { 90+\ph}{anchor=north,xshift=-5,yshift=3}{$\phi_1$};
  \tdplotdrawarc[black,->          ]{(0,0,0)}{\rad/6.}{180}{180+\ph}{anchor=west,yshift=-2}{$\phi_1$};

  %% rotated coord 2
  \tdplotsetrotatedcoords{\ph}{\ps}{0}
  \draw[dotted,thin,gray,->,tdplot_rotated_coords] (0,0,0) -- (-\rad,0,0) node[anchor=west]{};%{$y^2$};
  \draw[ultra thick,gray,->,>=stealth,tdplot_rotated_coords] (0,0,0) -- (0,0,\rad) node[anchor=east]{$z^c$};
  \tdplotdrawarc[black,dashed,tdplot_rotated_coords]{(0,0,0)}{\rad}{90}{180+\omega}{anchor=south}{};
  %\tdplotdrawarc[gray,thin,tdplot_rotated_coords]{(0,0,0)}{\rad/1.5}{90}{180+\omega}{anchor=south}{};
  \tdplotdrawarc[black,->,tdplot_rotated_coords]{(0,0,0)}{\rad/1.5}{90}{90+\omega}{anchor=south}{$\phi_2$};
  \tdplotdrawarc[black,->,tdplot_rotated_coords]{(0,0,0)}{\rad/1.5}{180}{180+\omega}{anchor=west,yshift=4}{$\phi_2$};

  \tdplotsetthetaplanecoords{\ph}
  \tdplotdrawarc[black,->,tdplot_rotated_coords]{(0,0,0)}{\rad/3}{0}{\ps}{anchor=south}{$\Phi$};
  \draw[black,->,tdplot_rotated_coords] (0,-\rad/3) arc (-90:-90+\ps:\rad/3) node[anchor=west,xshift=4,yshift=-2]{$\Phi$};
  \draw[black, dashed, tdplot_rotated_coords] (0,-\rad) arc (-90:\ps:\rad);

  % %% rotated coord 3
  \tdplotsetrotatedcoords{\ph}{\ps}{\omega};
  \draw[ultra thick,gray,->,>=stealth,tdplot_rotated_coords] (0,0,0) -- (0,\rad,0) node[anchor=north]{$x^c$};
  \draw[ultra thick,gray,->,>=stealth,tdplot_rotated_coords] (0,0,0) -- (-\rad,0,0) node[anchor=west]{$y^c$};
  % \draw[ultra thick,gray,->,tdplot_rotated_coords] (0,0,0) -- (0,0,\rad) node[anchor=north]{$z^c$};
\end{tikzpicture}

\end{document}
```


- 위의 스크립트를 파일에 복사/붙여넣기 한다음에 pdflatex를 이용하여 그래프를 완성하세요.
우선 [LaTeX](https://www.latex-project.org)를 설치하여야 합니다.
그리고 [tikz package](https://www.ctan.org/pkg/pgf?lang=en)가 필요합니다.
For Windows users, please refer to this internal [link]({% link installtexlive.md %})

- Copy and paste the above snipets to a file and pdflatex it.
Before doing it, you should make sure [LaTeX](https://www.latex-project.org/get/) is available.
 You will also need [tikz package](https://www.ctan.org/pkg/pgf?lang=en).


- 완성된 좌표계입니다.
- Below is an example:

<img src='/images/coord_c.pdf' width='400'>

- 위 스크립트의 ph, ps, omega (각각 $$\phi_1,\Phi,\phi_2$$ 의미) 값들을 변경하여 원하는 좌표계 변환 과정을 그릴 수 있습니다.
- Another example by changing ph, ps, and omega values in the script:

<img src='/images/coord_c_1.pdf' width='400'>


One can calculate the transformation matrix from Euler angles and vice versa.

A Fortran subroutine is available from professor Anthony Rollett at Carnegie Mellon University.

A Python script that does the work is available in below:


```python
def euler(ph=None, th=None, tm=None, a=None, echo=True):
	"""
	note:
		  This is a pythonized fortran subroutine embedded in the VPSC7.sub
		  done by youngung 2010-12-23

		  Matrix A(i,j) is returned as a numpy array
		  all Euler angles are in degree not in radian

		  # A[i,j] transforms from SA to CA

		  Thanks to python's non-hardwirable-arugment feature,
		  if a matrix is not given, it automatically calculates
		  the matrix with given angles.
		  Vice versa, if matrix is given, given angle aurgments
		  are ignored and new euler angles are returned.

	Nomenclature of Euler angle follows Bunge's.
		  ph = phi1,
		  th = phi
		  tm = phi2
	"""
	if type(a).__name__=='NoneType':  a=np.resize(np.array(()),(3,3));iopt=2
	else:
		if type(a).__name__=='ndarray':
			iopt = 1
			pass
		else:
			print 'Error: Unexpected Matrix a type'
			print 'It should be numpy.ndarry!'
			raise IOError

	if iopt==1 :
		th = math.acos(a[2,2])  #Radian
		if abs(a[2,2] > 0.99999):
			tm = 0.
			ph = math.atan2(a[0,1],a[0,0]) #Radian
		else:
			sth = math.sin(th)
			tm = math.atan2(a[0,2]/sth,a[1,2]/sth)
			ph = math.atan2(a[2,0]/sth,-a[2,1]/sth)
		th = th * 180./math.pi
		ph = ph * 180./math.pi
		tm = tm * 180./math.pi
		return [ph,th,tm] #phi1, phi, phi2

	elif (iopt == 2):
		angles = [ph,th,tm]
		if any(angles[i] == None for i in range(len(angles))):
			print 'Angles must be give if iopt==2'
			raise IOError

		""" Convert the angle into Radian"""
		ph = ph * math.pi / 180.
		th = th * math.pi / 180.
		tm = tm * math.pi / 180.

		sph = math.sin(ph)
		cph = math.cos(ph)
		sth = math.sin(th)
		cth = math.cos(th)
		stm = math.sin(tm)
		ctm = math.cos(tm)

		a[0,0] =  ctm * cph - sph * stm * cth
		a[1,0] = -stm * cph - sph * ctm * cth
		a[2,0] =  sph * sth
		a[0,1] =  ctm * sph + cph * stm * cth
		a[1,1] = -sph * stm + cph * ctm * cth
		a[2,1] = -sth * cph
		a[0,2] =  sth * stm
		a[1,2] =  ctm * sth
		a[2,2] =  cth

		if echo==True:
			print 'Matrix a is '
			print a
		return a

	else: print 'Error: Improper iopt input'; raise IOError
```
