# TikZ source files

이 폴더에는 강의자료에서 사용하는 TikZ 원본을 교과목별로 보관한다.

## 폴더 구성

- `metal_plasticity/`: 소성가공 및 다결정소성 강의용 그림

## PDF로 컴파일하기

저장소 루트에서 다음과 같이 실행한다.

```bash
mkdir -p output/pdf
pdflatex -interaction=nonstopmode \
  -output-directory=output/pdf \
  assets/tikz/metal_plasticity/rolling_geometry.tex
```

각 `.tex` 파일은 `standalone` 문서이므로 개별적으로 컴파일할 수 있다.
생성된 PDF나 PNG는 TikZ 원본과 구분하여 해당 출력·이미지 폴더에 저장한다.

