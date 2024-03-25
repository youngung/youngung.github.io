      implicit none

      dimension r(3,3), velocity_old(3), stress(3,3), velocity_new(3)
      real*8 r, velocity_old, stress, th, velocity_new
      integer i,j,k

      !! the transformation matrix:

      write(*,*)'Type: Rotation angle [in degree]:'
      read(*,*) th
      th = th* 3.141592 / 180. !! convert the degree to radian

      r(:,:)=0d0
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
         velocity_new(i)=0d0
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
