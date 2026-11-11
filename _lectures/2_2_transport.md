---
layout: page
title: 이동현상
description: 재료공학도를 위한 운동량, 열 및 물질 전달
target: 2학년 2학기
permalink:
prerequisite: 재료공학개론1, 데이터 재료과학, 수치해석, 대학수학
toc: false
---

**목차**

* TOC
{:toc}

- [제1강 이동현상 개요](/assets/lecture_notes/2_2_transport_phenomena/transport_01_orientation.md)
- [제2강 유체정역학](/assets/lecture_notes/2_2_transport_phenomena/transport_02_fluid_statics.md)
- [제3강 뉴턴 유체와 운동량 전달](/assets/lecture_notes/2_2_transport_phenomena/transport_03_newtonian_viscosity.md)
- [제4강 열전달 기초](/assets/lecture_notes/2_2_transport_phenomena/transport_04_heat_transfer.md)
- [제5강 열전도 방정식](/assets/lecture_notes/2_2_transport_phenomena/transport_05_heat_equation.md)
- [제6강 열전도의 유한차분해석](/assets/lecture_notes/2_2_transport_phenomena/transport_06_heat_fdm.md)
- [제7강 비정상 열전도](/assets/lecture_notes/2_2_transport_phenomena/transport_07_transient_heat.md)
- [제8강 확산 기초](/assets/lecture_notes/2_2_transport_phenomena/transport_08_diffusion_basics.md)
- [제9강 정상상태 확산](/assets/lecture_notes/2_2_transport_phenomena/transport_09_steady_diffusion.md)
- [제10강 비정상 확산](/assets/lecture_notes/2_2_transport_phenomena/transport_10_transient_diffusion.md)

# 교과목 목표

- 운동량, 열에너지 및 질량에 대한 보존식을 세울 수 있다.
- 뉴턴의 점성법칙, 푸리에의 열전도법칙 및 픽의 확산법칙을 비교할 수 있다.
- 간단한 일차원 전달 문제의 지배방정식과 경계조건을 정할 수 있다.
- 해석해와 수치해를 이용하여 전달속도와 장변수의 분포를 계산할 수 있다.


# 학습 흐름과 활용 방법

| 단계 | 강의 | 연결해서 이해할 내용 |
|---|---|---|
| 공통 언어 | 제1강 | 장변수 → 구배 → 플럭스 → 검사체적 보존식 |
| 운동량 전달 | 제2–3강 | 정지 유체의 힘의 평형 → 점성 유동의 운동량 수지 |
| 열전달 | 제4–7강 | 열저항 → 에너지 방정식 → 차분해석 → 시간에 따른 온도 변화 |
| 물질전달 | 제8–10강 | 농도와 확산계수 → 정상 확산 → 시간에 따른 농도 변화 |

각 강의는 식을 외우기보다 **좌표와 부호, 적용 가정, 초기·경계조건**을 먼저
적고 읽는다. 계산 뒤에는 단위와 극한값을 확인하고, 정상 문제에서는 입력과
출력의 수지, 비정상 문제에서는 축적량까지 확인한다.

제6강과 제10강의 Python 예제는 수치해석에서 배운 연립방정식과 이분법을
전달 문제에 적용하는 연결 실습이다. 예제에 주어진 물성은 계산 연습을 위한
값이며, 실제 공정 해석에서는 해당 재료·상·조성·온도에 맞는 물성을 사용한다.
각 강의 말미의 관련자료는 기초 복습과 심화 학습 용도를 구분하여 안내하였다.

# 공개 참고자료

- [MIT OCW 3.185: Transport Phenomena in Materials Engineering](https://ocw.mit.edu/courses/3-185-transport-phenomena-in-materials-engineering-fall-2003/pages/lecture-notes/): 재료공학의 확산, 열전도, 유체 유동을 다루는 강의노트.
- [OpenStax University Physics, Chapter 14](https://openstax.org/books/university-physics-volume-1/pages/14-1-fluids-density-and-pressure): 유체정역학과 점성 유동의 기초 복습.
- [MIT OCW 3.205: Thermodynamics and Kinetics of Materials](https://ocw.mit.edu/courses/3-205-thermodynamics-and-kinetics-of-materials-fall-2006/pages/lecture-notes/): 확산계수, 원자적 기구, 확산방정식 해법을 더 공부할 때 참고할 심화 강의노트.
