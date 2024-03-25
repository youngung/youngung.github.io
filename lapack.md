---
layout: page
title: LAPACK installation
---

LAPACK (Linear Algebra Package) is a standard software library for numerical linear algebra.
It provides routines for solving systems of linear equations and linear least squares, eigenvalue problems and singular value decomposition.
Find more about it either in [Wikipedia](https://en.wikipedia.org/wiki/LAPACK) or in [Netlib](http://www.netlib.org/lapack/).

This [page](https://gcc.gnu.org/wiki/LAPACK%20on%20Windows) is to give you instructions to install LAPACK on Windows on a step-by-step basis.

-------------------

## 1. gfortran 을 설치합니다: [링크]({% link howtogfortran.md %})

-------------------


## 2. tar 를 설치합니다: [링크]({% link tar.md %})

-------------------

## 3. 다음으로 LAPACK 3.4.0 version을 다운로드 받으세요

 아래의 링크를 사용해 3.4.0 version을 다운로드하거나, [여기서]({% link libs/lapack-3.4.0.tar %}) 다운로드 받으세요.

 [Link to netlib](http://www.netlib.org/lapack/#_lapack_version_3_4_0)

-------------------

## 4. tar를 사용하여 압축을 해제하세요.

 우선 **lapack-3.4.0.tar** 파일의 위치를 확인하고, 해당 위치를 명령 프롬프트를 사용해 찾아갑니다.
 다음으로 아래와 같이

```bash
c:\Users\Youngung\Downloads>tar -xf lapack-3.4.0.tar
```

명령어를 사용해 압축을 해제하면 papack-3.4.0 이라는 새폴더가 형성됩니다.


## 5. Lapack340_gfwin

다음으로 [여기](https://gcc.gnu.org/wiki/LAPACK%20on%20Windows?action=AttachFile&do=view&target=LAPACK_gfortran_Win_7Nov2010.zip) 에서 LAPACK340_gfwin.zip (혹은 유사한 zip file)을 다운로드 받습니다.
해당 zip file을 해제하면 다음과 같은 파일들을 찾을 수 있습니다.

<img src='/images/installLAPACK/3.png'>

해당 파일들을 모우 앞 단계에서 생성된 **c:\Users\Youngung\Downloads\lapack-3.4.0\** 폴더로 복사합니다.

복사후 lapack-3.4.0 폴더를 확인하면 아래와 같은 폴더와 파일들이 존재하는 것을 확인합니다.

<img src='/images/installLAPACK/4.png'>

## 6. CREATE libraries.

다시 명령프롬프트로 돌아와 **c:\Users\Youngung\Downloads\lapack-3.4.0** 폴더로 이동후
다음과 같이 **makelibs.bat** 라는 batch 파일을 실행합니다.

```bash
c:\Users\Youngung\Downloads\lapack-3.4.0> makelibs.bat   [엔터]
```

<img src='/images/installLAPACK/5.png'>

실행과 동시에 화면이 올라가면서 다음과 같은 명령어들이 연속적으로 실행되는 것을 볼 수 있습니다.

<img src='/images/installLAPACK/6.png'>


## 7. Testing libraries.

위의 단계는 길게는 수분 정도 소요되며 끝난 후 다시 명령프롬프트에서 설치된 라이브러리들을 다음과 같이
**testlibs.bat** batch file을 사용해 테스트 하세요.

```bash
c:\Users\Youngung\Downloads\lapack-3.4.0> testlibs.bat   [엔터]
```

<img src='/images/installLAPACK/7.png'>

위 역시 수분이 걸릴 수 있다. 테스트 완료후 다음과 같은 화면을 볼 수 있을 것이다.

<img src='/images/installLAPACK/8.png'>


## 8. Test
한 예제 program 을 테스트 해봅시다: [링크]({%link libs/ev.f %})
