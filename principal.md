---
layout: page
title: Principal stress space
---

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

## Principal stress space

Principal stress space에서는 응력 텐서의 전단 성분들이 zero 가 된다.

현재 응력텐서가 참조되는 (being referred to) 좌표계를 여러 [Euler angle]({%link euler.md%})들을
시도해보며 shear component가 없어지는 각도를 찾아 볼 수도 있다.

하지만 위의 방법은, 몇번 시도해보면 알게 되겠지만, 쉽지 않다.

물론 해석적으로 응력텐서의 주값들을 구할 수도 있겠지만, 주로 '수치적'인 접근으로도 풀 수 있다.

## Algorithm

응력 텐서를 3x3 matrix 형태로 생각한다면, 해당 행렬의 eigen values가 응력텐서의 principal value가 된다.
그리고 eigen vectors들이 principal space에서의 basis vectors가 된다.

[LAPACK](http://www.netlib.org/lapack/)의 dsysev 함수를 활용하여 eigen vector와 eigen values들을 구한다.

dsyev 에서 찾아지는 eigenvector들로 이뤄지는 3x3matrix가 principal space의 basis vector들을 old axes에 참조한 값들이다.

따라서, 해당 3x3 matrix는 old axes를 principal space로 mapping 한다. 다만,  해당 3x3 matrix는 right-handedness 혹은 left-handedness 일 수 있다.

우리는 right-handedness를 지켜야 한다. 이는 간단히 determinant를 구해보면 알 수 있다. determinant가 +1 일때, righthanded-ness, -1일 때 left handed coordinate system을 이루게 된다.

이를 바탕으로 right-handed coordinate를 구성할 수 있게 끔 **조정** 하여 해당 matrix를 'transformation matrix'로 사용할 수 있다.

그리고, transformation matrix를 안다면, 손쉽게 Euler angle들로 변환가능하다.

위의 작업들을 Fortran을 사용한 프로그램으로 옮겨 보았다.

```fortran
	  program ev
	  implicit none
	  integer lwmax
	  parameter(lwmax=1000)
	  dimension A(3,3),W(3),work(lwmax),stress(3,3),s_new(3,3),rot(3,3),
	 $     rotinv(3,3),aux33(3,3),rotaux(3,3),icols(6,2)
	  real*8 A, W, WORK, STRESS,s_new,rot,phi1,phi,phi2,rotinv,aux33,
	 $     dum,err,tol,rotaux,det
	  parameter(tol=1e-5)
	  integer i,j,k,l,lwork,info, ior,kerr,iopt,ipiv,iter,
	 $     ix,jx,icols
	  logical ibr
	  data icols /
	 $     1,2,1,2,1,2,
	 $     1,3,3,3,3,3/

c---------------------------------------------------------------------
c     upper triangle matrix
	  open(1,file='stress.inp',status='unknown')
	  open(2,file='result.txt',status='unknown')
	  do i=1,3
		 read(1,*) stress(i,:)
	  enddo
	  close(1)
c---------------------------------------------------------------------

	  A(:,:)=0d0
	  A(:,:)=stress(:,:)*1d0

	  do 10 i=1,3
	  do 10 j=1,3
		 stress(j,i)=stress(i,j)
 10   continue

c     --------
	  lwork=-1
	  call dsyev('V','U',3,A,3,W,work,lwork,info)
	  lwork=min(lwmax,int(work(1)))
	  call dsyev('V','U',3,A,3,W,work,lwork,info)
c     --------

	  IF( INFO.GT.0 ) THEN
		 WRITE(*,*)'The algorithm failed to compute eigenvalues.'
		 STOP -1
	  END IF

	  write(2,'(a)')'** Principal stress values'
	  write(2,'(3e11.3)')(w(i),i=1,3)

	  do 15 i=1,3
	  do 15 j=1,3
		 rot(i,j) = a(j,i)
 15   continue
	  call keep_right_handedness(rot)
	  rotaux(:,:)=rot(:,:)
	  iter = 1
	  err=1.

c     ----------------------------
!     check if transformation matrix rotate the stress tensor correctly.

	  do 20 i=1,3
	  do 20 j=1,3
		 s_new(i,j)=0d0
	  do 20 k=1,3
	  do 20 l=1,3
		 s_new(i,j)=s_new(i,j)+       rot(i,k)*stress(k,l)*rot(j,l)
 20   continue

	  write(2,'(a)')'** Stress tensor referred to principal space'
	  do i=1,3
		 write(2,'(3e11.3)')(s_new(i,j),j=1,3)
	  enddo

	  iopt=1
	  call euler(iopt, phi1,phi,phi2,rot)

	  write(2,'(a)')'** Euler angles that transform the old axes
	 $to principal space'
	  write(2,'(3a9)')'phi1','phi','phi2'
	  write(2,'(3(f7.2,2x))')phi1,phi,phi2
	  close(2)

	  write(*,'(a)')'** Completed - check result.txt'
	  end program ev
c----------------------------------------------------------------------
	  subroutine keep_right_handedness(a)
c     If the determinant>0, the vectors form right-handedness.
	  dimension a(3,3)
	  real*8 a,det

	  if (dabs(det(a)-1d0).lt.1e-8) return
	  a(1,:)=-a(1,:)
	  if (dabs(det(a)-1d0).lt.1e-8) return
	  a(2,:)=-a(2,:)
	  if (dabs(det(a)-1d0).lt.1e-8) return
	  a(3,:)=-a(3,:)
	  if (dabs(det(a)-1d0).lt.1e-8) return

	  write(*,*)'could not achieve right-handedness'
	  stop -1

	  return
	  end subroutine keep_right_handedness
c----------------------------------------------------------------------
	  subroutine euler (iopt,ph,th,tm,a)
c
c     CALCULATE THE EULER ANGLES ASSOCIATED WITH THE TRANSFORMATION
c     MATRIX A(I,J) IF IOPT=1 AND VICEVERSA IF IOPT=2
c     A(i,j) TRANSFORMS FROM SYSTEM sa TO SYSTEM ca.
c     ph,th,om ARE THE EULER ANGLES (in degrees) OF ca REFERRED TO sa.
c *****************************************************************************

c     tm:3 (phi2)
c     th:2 (phi)
c     ph:1 (phi1)

	  dimension a(3,3)
	  real*8 a,ph,th,tm
	  integer iopt

	  pi=4.*atan(1.d0)

	  if(iopt.eq.1) then
		 th=acos(a(3,3))
		 if(abs(a(3,3)).ge.0.9999) then
			tm=0.
			ph=atan2(a(1,2),a(1,1))
		 else
			sth=sin(th)
			tm=atan2(a(1,3)/sth,a(2,3)/sth)
			ph=atan2(a(3,1)/sth,-a(3,2)/sth)
		 endif
		 th=th*180./pi
		 ph=ph*180./pi
		 tm=tm*180./pi
	  else if(iopt.eq.2) then
		 sph=sin(ph*pi/180.)
		 cph=cos(ph*pi/180.)
		 sth=sin(th*pi/180.)
		 cth=cos(th*pi/180.)
		 stm=sin(tm*pi/180.)
		 ctm=cos(tm*pi/180.)
		 a(1,1)=ctm*cph-sph*stm*cth !!  c3*c1 - s1*s3*c2
		 a(2,1)=-stm*cph-sph*ctm*cth !! -s3*c1 - s1*c3*c2
		 a(3,1)=sph*sth         !!  s1*s2
		 a(1,2)=ctm*sph+cph*stm*cth !!  c3*s1 + c1*s3*c2
		 a(2,2)=-sph*stm+cph*ctm*cth !! -s1*s3 + c1*c3*c2
		 a(3,2)=-sth*cph        !! -s2*c1
		 a(1,3)=sth*stm         !!  s2*s3
		 a(2,3)=ctm*sth         !!  c3*s2
		 a(3,3)=cth             !!  c2
	  endif

	  return
	  end subroutine euler

c----------------------------------------------------------------------
	  real*8 function det(a)
	  dimension a(3,3)
	  real*8 a

det=a(1,1)*a(2,2)*a(3,3)
	 $     +a(1,2)*a(2,3)*a(3,1)
	 $     +a(1,3)*a(2,1)*a(3,2)
	 $     -a(1,3)*a(2,2)*a(3,1)
	 $     -a(2,3)*a(3,2)*a(1,1)
	 $     -a(1,2)*a(2,1)*a(3,3)
	  return
	  end function det

```

위 프로그램을 실행하기 위해서는
- 첫째, LAPACK이 설치되어 있어야 한다 - [설치방법]({% link lapack.md %})
- 둘째, 위의 프로그램을 fortran compiler를 사용해 적절히 executable을 생성시켜야 한다.
  예를 들어 위의 코드를 *ex.f* 로 저장했다면 아래와 같이 gfortran과 LAPACK을 활용해 compile할 수 있다.
```bash
$> gfortran ex.f -llapack -o ex
```

**ex** 파일을 실행하기 위해서는 특정 공간에서의 응력텐서를 주어야 한다.
해당 코드는 **stress.inp** 에서 응력 텐서를 읽어들인다.

**stress.inp** 파일은 아래와 같이 작성한다.

```text
-30.  25.   11.
25.  1.    -9.
11.   -9.    17.
```

이 파일을 **ex** executable 파일과 같은 위치에 놓고

```bash
$> ./ex
```
로 실행을 하면

**result.txt** 라는 파일이 생성되며 다음과 같은 결과를 얻을 수 있다.

해당 파일은 아래와 같이 생성될 것이다.

```
** Principal stress values
 -0.470E+02  0.139E+02  0.210E+02
** Stress tensor referred to principal space
 -0.470E+02 -0.129E-13 -0.222E-14
 -0.102E-13  0.139E+02 -0.266E-14
 -0.444E-15 -0.266E-14  0.210E+02
** Euler angles that transform the old axes to principal space
	 phi1      phi     phi2
  -1.40    24.86   -30.59
```

여기서 -0.470E+02 는 $$-0.470\times10^2$$를 의미한다. 즉 E+02 부분은 $$10^{2}$$ 형태의 지수 값이 곱해져 있음을 의미한다.

$$\phi_1, \Phi, \phi_2$$ Euler angle들의 형태로 Old coordinate system을 변환하면
얻어진 주 응력값을 주는 principal stress space를 얻을 수 있다.

위의 example를 [Excel spreadsheet]({% link Euler2ndTensor.md %})로 직접 실습해보자.

위의 전과정을 성공적으로 마무리 했다면 ... 축하드립니다!

<img src="https://imgs.xkcd.com/comics/error_code.png">
