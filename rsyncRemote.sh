#!/bin/bash
# rsync -PaHAv --numeric-ids -e 'ssh -T -i /Users/yj/.ssh/id_rsa' younguj@pal:~/repo/vpsc-fld/archive/FLD_A/20160831/ ./
# rsync -PaHAv --numeric-ids -e 'ssh -T -i /Users/youngung/.ssh/id_rsa  -o Compression=no' younguj@pal:~/repo/vpsc-fld/archive/FLD_A/ ./
## rsync -PaHAv --numeric-ids -e 'ssh -T -i /Users/youngung/.ssh/id_rsa  -o Compression=no' yj@10.0.1.6:~/repo/vpsc/vpsc-dev-fld/archive/FLD_A/ ./


# rsync -PaHAv --numeric-ids -e 'ssh -T -i /Users/youngung/.ssh/id_rsa  -o Compression=no' youngung@mml:~/repo/vpsc-fld-yld/archive/FLD_A/ ./
# rsync -PaHAv --numeric-ids ~/OneDrive\ -\ changwon.ac.kr/Lectures/2017Fall/금속유동해석특론/*.pdf lecturenotes/MetalPlasticity/
# rsync -PaHAv --numeric-ids ~/OneDrive\ -\ changwon.ac.kr/Lectures/2017Fall/기계재료개론/*.pdf lecturenotes/MechMSE/
# rsync -PaHAv --numeric-ids ~/OneDrive\ -\ changwon.ac.kr/Lectures/2017Fall/소성가공/*.pdf lecturenotes/MetalForming/

## 2018-Spring
#rsync -PaHAv --numeric-ids ~/OneDrive\ -\ changwon.ac.kr/Lectures/2018Spring/TransportPhenomena/*.pdf lecturenotes/TransportPhenomena/
#rsync -PaHAv --numeric-ids ~/OneDrive\ -\ changwon.ac.kr/Lectures/2018Spring/MSE/*.pdf lecturenotes/MSE/

## 2019-Fall
# rsync -v ~/OneDrive\ -\ changwon.ac.kr/Lectures/2019-2/mechmse/*.pdf lecturenotes/MechMSE/              ## 기계재료개론rrs
# rsync -v ~/OneDrive\ -\ changwon.ac.kr/Lectures/2019-2/metalforming/*.pdf lecturenotes/MetalForming/
# rsync -v ~/OneDrive\ -\ changwon.ac.kr/Lectures/2019-2/VPSC-theory/*.pdf lecturenotes/vpsc
# rsync -v ~/OneDrive\ -\ changwon.ac.kr/Lectures/2020-1/전산소성가공이론1/*/*.pdf lecturenotes/computationalmechanics1
# rsync -v ~/OneDrive\ -\ changwon.ac.kr/Lectures/2020-1/전산소성가공이론2/*/*.pdf lecturenotes/computationalmechanics2


## 2021-Fall
rsync -v ~/OneDrive\ -\ changwon.ac.kr/Lectures/2021-2/소성가공학/slides_without_movies/*.pdf lecturenotes/MetalForming/

# bash update.sh
# git commit -am 'Lecture note updates'&&git push github master
