---
layout: page
title: Tensors
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

텐서와 벡터에 대한 아주 좋은 설명을 아래 YouTube동영상에서 찾을 수 있다.

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/f5liqUk0ZTw/0.jpg)](http://www.youtube.com/watch?v=f5liqUk0ZTw)


텐서의 정의를 가장 잘 표현한 문구이다:
Tensors transform like tensors.

아래 기존의 references axes 를 새로운 axes로 변환시키는 변환 매트릭스 (transformation matrix)
를 사용하여 벡터 a, second rank tensor $${\bf \sigma}$$ 그리고 4th rank tensor $$\mathbb{M}$$을 변환하는 법칙이 나와 있다.

$$
a^\prime_i = R_{ij} a_j \\
\sigma^\prime_{ij} = R_{ik} \sigma_{kl} R_{jl} \\
\mathbb{M}^\prime_{ijkl} = R_{im} R_{jn} \mathbb{M}_{mnop} R_{ko} R_{lp}
$$


** [Einstein convention](https://en.wikipedia.org/wiki/Einstein_notation) was used for the summation ([아인슈타인 컨벤션](https://ko.wikipedia.org/wiki/아인슈타인_표기법)이 사용되어있다.)


Below fortran code is an example where the coordinate transformation
is applied to a velocity vector ($$[30, 0, 0]$$) by rotating the old coordinate axes
by an angle about the 3rd basis axis in the right-handed manner.


In short, it does

$$
v^\prime_i = \sum_j^3 R_{ij}v_j
$$

More explicitly it does **three** separate summation operations:

$$
v^\prime_1 = \sum_j^3 R_{1j}v_j\\
v^\prime_2 = \sum_j^3 R_{2j}v_j\\
v^\prime_3 = \sum_j^3 R_{3j}v_j\\
$$

Find the code below:

```fortran
	implicit none

	dimension r(3,3), velocity_old(3), stress(3,3), velocity_new(3)
	real*8 r, velocity_old, stress, th, velocity_new
	integer i,j,k

	!! the transformation matrix:
	write(*,*)'Type: Rotation angle [in degree]:'
	read(*,*) th
	th = th* 3.141592 / 180. !! convert the degree to radian

	r(:,:)=0.
	r(1,1)=cos(th)
	r(1,2)=sin(th)
	r(2,1)=-sin(th)
	r(2,2)=cos(th)
	r(3,3)=1.

	!! velocity
	velocity_old(1)=30.
	velocity_old(2)=0.
	velocity_old(3)=0.

	!! let's transform the velocity v`_i = r_ij v_j
	do i=1,3
		velocity_new(i)=0.
	do j=1,3
		velocity_new(i)=velocity_new(i)+r(i,j)*velocity_old(j)
	enddo
	enddo

	!! print out the new velocity
	write(*,*) 'old velocity'
	write(*,'(3f5.1)') (velocity_old(i),i=1,3)
	write(*,*) 'new velocity'
	write(*,'(3f5.1)') (velocity_new(i),i=1,3)

	end program
```

In order to use the code, copy and paste the above to a file (say, **transform.f**)
and compile it using [gfortran](https://gcc.gnu.org/fortran/) as in below

```bash
$ gfortran transform.f -o transform
```

You will find an executable file named **transform** appeared in that same folder.
Execute the program using
```bash
$ ./transform
```
And, type the rotation angle you want to examine.


For 2nd rank tensor transformation, you can use below lines:
```fortran
do i=1,3
do j=1,3
	s_new(i,j)=0.
do k=1,3
do l=1,3
	s_new(i,j)=s_new(i,j) + r(i,k)*s_old(k,l)*r(j,l)
enddo
enddo
enddo
enddo
```

-----------------------------

Similarly, a Python script is as below does the same.

You will need NumPy package installed in your system to run the below correctly.
```python
import numpy as np
velocity_old=np.zeros(3)
velocity_new=np.zeros(3)
r=np.zeros((3,3))
velocity_old[0]=30.

th=raw_input('Type angle [in degree]: ')
th=np.pi*float(th)/180.

r[0,0]=np.cos(th)
r[0,1]=np.sin(th)
r[1,0]=-np.sin(th)
r[1,1]=np.cos(th)
r[2,2]=1.


## Apply v`_i = r_ij v_j
for i in xrange(3):
	for j in xrange(3):
		velocity_new[i]=velocity_new[i]+ \
	r[i,j]*velocity_old[j]

print 'old velocity'
print velocity_old
print 'new velocity'
print velocity_new
```

Copy and paste the above to a file (say **transform.py**).
You can run the above such as
```bash
$ python transform.py
```



Excercise 1:
Modified the above code to transform a stress tensor to a new coordinate axes.


Excercise 2:
Create a transformation matrix using three [Euler angles]({% link euler.md%}) and repeat the above task.

Use below subroutine (downloaded from the [website](http://rollett.org/anthony/) of prof. Anthony Rollett@CMU) to obtain the transformation matrix as a function of the three Euler angles
$$\phi_1, \Phi, \phi_2$$.


```fortran
c     This subroutine has been downloaded from the link below:
c     http://pajarito.materials.cmu.edu/rollett/texture_subroutines/euler.f
c
c  -------------------
c
	  subroutine euler(a,iopt,nomen,d1,d2,d3,ior,kerr)
	  implicit none
c                          Last revision 20nov90 UFK
c                          Revision by YJ for his lectures at CWNU
c      common a(3,3),grvol(1152),epsga(5),ist1,ist2,sqr3,sqrh,ident(3,3)
c  SPECIAL VERSION WITHOUT COMMON BLOCK
	  integer iopt,ior,kerr,kor
	  real*8 dps,rad
	  real*8 a(3,3),d1,d2,d3,th,sth,cth,sph,cph,sps,cps,ps,ph,dth,dph,dps
	  character nomen
	  save kor
	  rad=57.29578
c
c *** this subroutine calculates the euler angles associated with the
c     transformation matrix a(i,j) if iopt=1 and viceversa if iopt=2
c ***  Note that a is sample (rows) in terms of crystal (columns);
c      -- opposite of standard g (e.g.Bunge) - this is Canova s
c ***  Note that in this version, the Euler angles are defined symmetrically:
c      so that interchanging phi and psi means transposing a.
c      ("Kocks" nomen: defined going from +X to +Y in both COD and SOD)
c ***  However, other angle conventions are translated, according to
c  nomen="K" - Kocks (as internally) -- also sometimes "N"...
c        "R" - Roe          (Psi=psi, Phi=180-phi)
c        "B" - Bunge        (phi1=90+psi, Phi=Theta, phi2=90-phi)
c        any other - Canova (Theta first, phiC=90+phi, omega=90-psi)
c ***   Note: only in symm. notation does a point with all Euler angles
c             between 0 and 90 deg appear in the +x,+y quadrant!
c       If you want to see an individual point in this quadrant and are:
c       using Roe,    the third angle must be between 90 and 180;
c             Bunge,      first                                 ;
c             Canova,     second                                .
c ***  Input and output Euler angles d1,d2,d3 in degrees
c
	  goto(5,20),iopt
	5 if(abs(a(3,3)) .ge. 0.999) goto 10
	  th=acos(a(3,3))
	  sth=sin(th)
	  ps=atan2(a(2,3)/sth,a(1,3)/sth)
	  ph=atan2(a(3,2)/sth,a(3,1)/sth)
ccccc   if it bombs out here, both a-components in one arg. are zero
c       (this should not be possible, but has happened, probably fixed)
	  go to 15
c
   10 ps=0.5*atan2(a(1,2),-a(1,1))
	  ph=-ps
c       The above still have the problem that they give too many
c       equivalents of the same grain in DIOROUT and density file. Therefore:
	  if(kerr.eq.1.and.kor.ne.ior) then
	  print*,'NOTE: grain',ior,' has Theta < 1 deg.: sometimes problems'
		print*
		kor=ior
	  endif
c
   15 dth=th*rad
	  dph=ph*rad
	  dps=ps*rad
	  d1=dps
	  d2=dth
	  if(nomen.eq.'K'.or.nomen.eq.'N') then
		d3=dph
	  elseif(nomen.eq.'R') then
		d3=180.-dph
	  elseif(nomen.eq.'B') then
		d1=dps+90.
		d3=90.-dph
	  else
		d1=dth
		d2=dph+90.
		d3=90.-dps
	  endif
	  if(d1.ge.360.) d1=d1-360.
	  if(d3.ge.360.) d3=d3-360.
	  if(d1.lt.0.) d1=d1+360.
	  if(d3.lt.0.) d3=d3+360.
	  return
c  *************************************
   20 dth=d2
	  dps=d1
	  if(nomen.eq.'K') then
		dph=d3
	  elseif(nomen.eq.'R') then
		dph=180.-d3
	  elseif(nomen.eq.'B') then
		dps=d1-90.
		dph=90.-d3
	  else
		dth=d1
		dph=d2-90.
		dps=90.-d3
	  endif
	  ph=dph/rad
	  th=dth/rad
	  ps=dps/rad
	  sph=sin(ph)
	  cph=cos(ph)
	  sth=sin(th)
	  cth=cos(th)
	  sps=sin(ps)
	  cps=cos(ps)
	  a(1,1)=-sps*sph-cph*cps*cth
	  a(2,1)=cps*sph-cph*sps*cth
	  a(3,1)=cph*sth
	  a(1,2)=sps*cph-sph*cps*cth
	  a(2,2)=-cph*cps-sph*sps*cth
	  a(3,2)=sth*sph
	  a(1,3)=sth*cps
	  a(2,3)=sps*sth
	  a(3,3)=cth
	  return
	  end
c
c  &&&&&&&&&&&&&&
c
```
