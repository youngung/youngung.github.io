---
layout: page
title: Tape Archive installation on Windows
---

[GNU Tar](http://savannah.gnu.org/projects/tar) provides the ability to create tar archives.

You can download the tar binary [here](http://gnuwin32.sourceforge.net/packages/gtar.htm).


--------------------
### 1. 바이너리 파일을 다운로드 합니다.

<img src="/images/installTar/1.png" width="600">

--------------------
### 2. 더블 클릭하여 설치를 합니다. 이때 설치되는 장소를 메모합니다.
저의 경우 E:\program\GnuWin32 에 설치하였습니다.

--------------------
### 3. tar 실행 파일은 설치한 장소 아래의 **bin** folder 아래에 위치됩니다.

<img src="/images/installTar/2.png" width="600">

--------------------
### 4. 해당 파일이 위치한 폴더 위치를 환경변수 **Path** 에 추가하여야 합니다.

이를 위해
내컴퓨터(PC) 에서 우클릭->속성->고급시스템설정->환경변수

<img src="/images/installTar/3.png" width="600">

아래와 같이 **Path** 라는 변수를 한번 클릭하여 highlight한 뒤 아래의 **편집**을 클릭.

<img src="/images/installTar/4.png" width="600">

다음으로, 아래와 같이 **새로만들기**를 눌러서 **E:\program\GnuWin32\bin** 을 추가하면 됩니다.

<img src="/images/installTar/5.png" width="600">

주의) 실제로 tar binary file이 저장이 되어있는 폴더의 위치를 추가해야 합니다.


### 5. Test

Tar가 잘 설치되었는지 테스트를 실행합니다.
명령 프롬프트를 실행하여 다음을 실행해보세요.

```bash
c:\Users> tar --help
```
아래와 같이 tar 명령에 대한 설명이 출력됩니다.
<img src="/images/installTar/6.png" width="700">



아래의 program 을 테스트 해봅시다.

```fortran
		Program Eigenvalue
c finding the eigenvalues of a complex matrix using LAPACK
		Implicit none
c declarations, notice double precision
		complex*16 A(3,3), b(3), DUMMY(1,1), WORK(6)
		integer i, ok
c define matrix A
		A(1,1)=(3.1, -1.8)
		A(1,2)=(1.3, 0.2)
		A(1,3)=(-5.7, -4.3)
		A(2,1)=(1.0, 0)
		A(2,2)=(-6.9, 3.2)
		A(2,3)=(5.8, 2.2)
		A(3,1)=(3.4, -4.0)
		A(3,2)=(7.2, 2.9)
		A(3,3)=(-8.8, 3.2)
c
c find the solution using the LAPACK routine ZGEEV
		call ZGEEV('N', 'N', 3, A, 3, b, DUMMY, 1, DUMMY, 1, WORK, 6,
	 $       WORK, ok)
c
c parameters in the order as they appear in the function call
c    no left eigenvectors, no right eigenvectors, order of input matrix A,
c    input matrix A, leading dimension of A, array for eigenvalues,
c    array for left eigenvalue, leading dimension of DUMMY,
c    array for right eigenvalues, leading dimension of DUMMY,
c    workspace array dim>=2*order of A, dimension of WORK
c    workspace array dim=2*order of A, return value
c
c output of eigenvalues
		if (ok .eq. 0) then
		   do i=1, 3
			  write(*,*) b(i)
		   enddo
		else
		   write (*,*) "An error occured"
		endif
		end
```
