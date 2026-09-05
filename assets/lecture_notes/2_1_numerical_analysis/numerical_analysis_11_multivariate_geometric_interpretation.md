
## 11.2. 수업 08-2 (Geometric interpretation of multivariate NR)

- 앞선 예제를 기하학적으로 해석하자.
- 우선 정형화된 아래 2D 그래프 생선 함수를 사용하자.

  ```python
  def init_fig(f1,f2):
  	fig=plt.figure(figsize=(8,8))
  	ax1=fig.add_subplot(221)#,projection='3d')
  	ax2=fig.add_subplot(222,projection='3d')
  	ax3=fig.add_subplot(223)#,projection='3d')
  	ax4=fig.add_subplot(224,projection='3d')

  	# Grid
  	x=np.linspace(-10,10,100)
  	y=np.linspace(-10,10,100)
  	X,Y=np.meshgrid(x,y)

  	## 2D contour plot
  	mappable=ax1.contourf(X,Y,f1(X,Y),cmap='jet')
  	plt.colorbar(mappable,ax=ax1,label=r'$f_1$')
  	ax1.set_title(r'$f_1(x_1,x_2)$')
  	ax1.set_xlabel(r'$x_1$')
  	ax1.set_ylabel(r'$x_2$')
  	## 3D plane
  	ax2.plot_surface(X,Y,f1(X,Y),cmap='jet')
  	ax2.set_zlabel(r'$f_1$')
  	ax2.set_xlabel(r'$x_1$')
  	ax2.set_ylabel(r'$x_2$')

  	## 2D contour plot
  	mappable=ax3.contourf(X,Y,f2(X,Y),cmap='jet')
  	plt.colorbar(mappable,ax=ax3,label=r'$f_2$')
  	ax3.set_title(r'$f_2(x_1,x_2)$')
  	ax3.set_xlabel(r'$x_1$')
  	ax3.set_ylabel(r'$x_2$')
  	## 3D plane
  	ax4.plot_surface(X,Y,f2(X,Y),cmap='jet')
  	ax4.set_zlabel(r'$f_2$')
  	ax4.set_xlabel(r'$x_1$')
  	ax4.set_ylabel(r'$x_2$')
  	return fig,ax1,ax2,ax3,ax4
  ```

- 아래 예제를 활용해보자

  ```python
  def f1(x,y):  return x*y-10
  def f2(x,y):  return x**2-y-3
  def func(x,y): return np.array([f1(x,y),f2(x,y)])
  def jacob(x,y):
  	j=np.zeros((2,2))
  	j[0,0]=y
  	j[0,1]=x
  	j[1,0]=2*x
  	j[1,1]=-1
  	return j

  ## NEWTON-RAPHSON begins here.
  ## Initial guess
  x=np.zeros(2) ## initial guess
  x[::]=4.0 ## initial guess
  x,hist,fhist,jhist,niters=mvNR(func,jacob,xinit=np.ones(2))
  print(f'niters: {niters}')

  ## Below is to create figures
  %matplotlib widget
  #%matplotlib inline

  fig,ax1,ax2,ax3,ax4=init_fig(f1,f2)

  kws=dict(mfc='None',zorder=100,ls='None')
  for n,x in enumerate(hist):
  	f1,f2=fhist[n]
  	x1,x2=x

  	kws.update(label=r'$n$=%i'%n)
  	ax1.plot(x1,x2,**kws)
  	ax2.plot(x1,x2,f1,**kws)
  	ax3.plot(x1,x2,**kws)
  	ax4.plot(x1,x2,f2,**kws)

  ax1.legend(loc='upper left')
  ```

- 아래 그림을 보고 어떠한 일이 일어나고 있는지 이해해보자.
  ![imag](/assets/dat_files/lectures/2_1_numerical_analysis/mvNR.gif)
