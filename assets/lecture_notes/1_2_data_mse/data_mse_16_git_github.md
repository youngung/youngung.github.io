---
layout: distill
title: Git과 GitHub
description: Git 설치와 GitHub 계정 만들기부터 Matplotlib 코드의 버전 관리와 협업까지
target: 1학년 2학기
permalink:
featured: true
prerequisite: 터미널 기초 조작, Matplotlib 기초
toc: false
hidden: true
authors:
  - name: Youngung Jeong
    url: "https://youngung.github.io/"
    affiliations:
      name: Changwon National University
---

**목차**

* TOC
{:toc}

# 1. 왜 분석 코드의 변경을 기록할까?

앞 강의에서 작성한 그래프의 축 이름과 격자 표시를 바꿨다고 하자. 한 달 뒤 같은 그림을 다시 그리려면 어느 파일을 고쳤고 어떤 설정을 사용했는지 알아야 한다. Git은 파일의 변경을 기록하는 **버전 관리 도구**다. 의미 있는 변경마다 기록을 남기면 이전 코드와 현재 코드의 차이를 줄 단위로 살펴볼 수 있다.

**저장소(repository)**는 프로젝트 파일과 그 변경 이력을 관리하는 단위다. 내 컴퓨터의 저장소를 **로컬 저장소(local repository)**라고 한다. GitHub는 Git 저장소를 온라인에 두고 공유하거나 변경을 검토할 수 있는 서비스다. GitHub에 연결한 저장소는 이 실습에서 **원격 저장소(remote repository)**가 된다. Git의 로컬 작업은 GitHub 계정 없이도 할 수 있다.

이번 실습에서는 작은 Matplotlib 프로젝트의 첫 버전을 기록하고 GitHub로 보낸다. 이어서 별도의 작업 줄기에서 그래프를 수정하고 GitHub에서 변경 내용을 검토한다.

# 2. Git 설치와 GitHub 계정 만들기

## Git 설치 확인

VS Code의 터미널을 열어 다음 명령을 실행한다. Windows에서는 Git for Windows에 포함된 Git Bash를 사용해도 된다. 코드 블록에서 `bash`는 명령을 입력할 셸의 종류를 뜻한다.

```bash
git --version
```

`git version`으로 시작하는 줄이 나오면 설치되어 있다. 명령을 찾을 수 없으면 운영체제에 맞는 Git을 설치하고 터미널을 다시 연다. Windows는 Git for Windows, macOS는 `xcode-select --install`을 통한 Command Line Tools, Linux는 배포판의 패키지 관리자를 사용할 수 있다. [Git 설치 안내](https://git-scm.com/install)

## GitHub 가입과 이메일 설정

1. GitHub 가입 화면에서 개인 계정을 만든다. 사용자 이름(username)은 프로필과 저장소 주소에 쓰인다. [가입 화면](https://github.com/signup)
2. 가입에 사용한 이메일을 확인하고 받은 편지함에서 인증을 완료한다. 계정 설정에서 2단계 인증(2FA)을 구성하고 복구 코드는 개인 기기에 보관한다. [GitHub 계정 시작 안내](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account)
3. 커밋에는 작성자 이름과 이메일이 기록된다. 개인 이메일 공개를 피하려면 GitHub의 **Settings → Emails**에서 계정에 부여된 `noreply` 주소를 확인해 아래 이메일 자리에 넣는다. [커밋 이메일 설정](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)

```bash
git config --global user.name "내 이름"
git config --global user.email "내 커밋 이메일"
git config --get user.name
git config --get user.email
```

따옴표 안의 값은 자신의 이름과 이메일로 바꾼다. `--global`은 이 컴퓨터의 현재 사용자 계정에 기본값을 저장한다. 수업용 컴퓨터에서 프로젝트별로 설정하려면 아래의 `git init`을 먼저 실행한 뒤 해당 폴더에서 `--global` 대신 `--local`을 사용한다. 이 이름과 이메일은 작성자 정보다. GitHub 로그인은 원격 저장소 연결 단계에서 별도로 진행한다.

# 3. 실습 1 — 그래프의 첫 버전 기록하기

터미널에서 수업 파일을 저장하는 폴더로 이동한다. 그곳에 실습 폴더를 만들고 새 저장소를 시작한다. `-b main`은 기본 작업 줄기의 이름을 `main`으로 정하는 옵션이다.

```bash
mkdir data-mse-plot
cd data-mse-plot
git init -b main
```

편집기에서 이 폴더를 열고 `plot_data.py`를 만든다. 가상의 측정 데이터를 사용한 예시다.

```python
import matplotlib.pyplot as plt

time_s = [0, 1, 2, 3, 4]
signal_mv = [0.2, 1.0, 2.1, 2.9, 4.2]

fig, ax = plt.subplots()
ax.scatter(time_s, signal_mv)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Signal (mV)")
fig.savefig("plot.png", dpi=150)
```

같은 폴더에 `README.md`를 만들고 아래 내용을 넣는다. README는 프로젝트의 목적과 실행 방법을 설명하는 문서이며, GitHub 저장소 첫 화면에서도 읽을 수 있다.

```markdown
# Data MSE Plot

가상의 시간–신호 측정값을 산점도로 표시한다.

Matplotlib이 설치된 Python 환경에서 `python plot_data.py`를 실행하면 plot.png가 생성된다.
```

이 실습에서는 그림을 코드로 다시 만들 수 있으므로 생성한 `plot.png`는 버전 관리에서 제외한다. 저장소의 최상위 폴더에 `.gitignore` 파일을 만들고 다음 두 줄을 넣는다. `.gitignore`는 아직 추적하지 않는 파일 가운데 Git이 보통 무시할 경로를 지정한다.

```gitignore
/plot.png
__pycache__/
```

```bash
python plot_data.py
git status --short
git add README.md plot_data.py .gitignore
git diff --staged
git commit -m "Add measurement scatter plot"
git status --short
git log --oneline
```

환경에 따라 `python` 명령은 `python3` 또는 `py`로 바꿔 실행한다. 처음 `git status --short`에서 새 파일 세 개 앞에 `??`가 보이고 `plot.png`는 목록에서 빠진다. 커밋 직후에는 `git status --short`의 출력이 비고, `git log --oneline`에는 커밋을 식별하는 짧은 ID와 메시지가 한 줄로 나타난다.

| 위치 | 이 실습에서 하는 일 |
| --- | --- |
| 작업 폴더(working tree) | 편집기에서 실제 파일을 만들고 수정한다. |
| 스테이징 영역(staging area) | `git add`로 다음 커밋에 포함할 파일의 현재 내용을 골라 담는다. |
| 로컬 저장소(local repository) | `git commit`으로 스테이징 영역의 내용을 설명과 함께 기록한다. |
| 원격 저장소(remote repository) | `git push`로 로컬 브랜치의 커밋을 GitHub에 보낸다. |

커밋(commit)은 그 시점에 선택한 프로젝트 상태를 남긴 기록이다. 파일을 스테이징한 뒤 편집하면 새 편집 내용은 작업 폴더에 남는다. `git diff`는 스테이징 이후 작업 폴더에 생긴 변경을, `git diff --staged`는 마지막 커밋과 비교해 다음 커밋에 들어갈 변경을 보여 준다.

# 4. 실습 2 — GitHub에 첫 버전 올리기

1. GitHub에 로그인해 **New repository**를 선택한다. 이름은 `data-mse-plot`, 공개 범위는 실습용으로 **Private**을 선택한다. 공개 저장소(Public)는 누구나 볼 수 있고 비공개 저장소는 권한을 가진 사용자가 볼 수 있다.
2. 로컬에서 첫 커밋을 이미 만들었으므로 GitHub에서는 README, .gitignore, 라이선스 추가 옵션을 선택하지 않고 빈 저장소를 만든다.
3. GitHub CLI를 별도로 설치한다. 터미널에서 `gh auth login`을 실행해 GitHub.com, HTTPS, 브라우저 로그인을 선택한다. 브라우저에서 로그인을 마친 뒤 아래 명령으로 로그인 상태를 확인하고 Git의 인증을 설정한다. [GitHub CLI 인증 안내](https://docs.github.com/en/github-cli/github-cli/authenticating-with-github-cli)
4. 아래 URL의 `USERNAME`을 자신의 GitHub 사용자 이름으로 바꿔 실행한다. GitHub 저장소 화면에서 HTTPS 주소를 복사해 넣어도 된다.

```bash
gh auth status
gh auth setup-git
git remote add origin https://github.com/USERNAME/data-mse-plot.git
git remote -v
git push -u origin main
```

`origin`은 이 원격 저장소에 붙인 이름이다. `-u`는 로컬의 `main`을 원격의 `main`과 연결해 이후에 이 브랜치에서 `git push`와 `git pull`의 대상 지정을 생략할 수 있게 한다. GitHub 저장소 페이지를 새로고침하고 파일 목록과 커밋 메시지를 확인한다.

실제 분석 자료를 올리기 전에는 `git diff --staged`로 포함될 내용을 확인한다. 비밀번호, 토큰, 개인정보, 공개 권한이 없는 실험 데이터는 커밋 대상에서 제외한다. 이미 커밋한 파일을 이후 버전에서 삭제해도 앞선 커밋에는 내용이 남을 수 있다.

# 5. 실습 3 — 브랜치에서 수정하고 Pull Request로 검토하기

**브랜치(branch)**는 커밋이 이어지는 작업 줄기다. 현재의 `main`에서 `add-grid` 브랜치를 만들면 첫 그래프 버전을 바탕으로 격자 추가를 시험할 수 있다.

```bash
git switch -c add-grid
```

`plot_data.py`에서 `fig.savefig(...)` 바로 위에 `ax.grid(True, alpha=0.3)`을 추가한다. `alpha`는 투명도를 조절하는 값이다. 다시 실행해 `plot.png`에 격자가 나타나는지 확인하고, 코드 변경을 기록한다.

```bash
python plot_data.py
git diff
git add plot_data.py
git diff --staged
git commit -m "Add grid to measurement plot"
git push -u origin add-grid
```

1. GitHub에서 **Pull Request**를 열어 비교 대상을 `main`(base), 변경을 가져올 브랜치를 `add-grid`(compare)로 지정한다. Pull Request는 변경을 합치기 전에 차이를 검토하고 의견을 남기는 요청이다.
2. **Files changed**에서 추가된 한 줄을 확인한다. 설명에 무엇을 바꿨고 그림에서 어떻게 확인했는지 적는다.
3. 검토를 마치면 GitHub에서 **Merge pull request**로 변경을 `main`에 합친다. 팀 실습에서는 합치기 전에 팀원에게 검토를 요청할 수 있다.
4. 터미널에서 로컬의 `main`으로 돌아와 원격의 변경을 받아온다. `--ff-only`는 로컬 브랜치가 원격 이력을 그대로 따라갈 수 있을 때만 업데이트하게 한다.

```bash
git switch main
git pull --ff-only
git log --oneline -5
```

[GitHub Flow 안내](https://docs.github.com/en/get-started/using-github/github-flow)

다른 컴퓨터에서 처음 이어서 작업할 때는 실습 폴더 밖에서 `git clone https://github.com/USERNAME/data-mse-plot.git`을 실행한다. `clone`은 파일과 커밋 이력을 담은 새 로컬 저장소를 만들고, `pull`은 이미 가지고 있는 저장소의 현재 브랜치를 업데이트한다. 복제한 폴더에서 README대로 스크립트를 실행해 같은 그림을 재현한다.

# 6. 확인 문제와 다음 강의

1. `git add plot_data.py` 직후 축 이름을 한 번 더 수정했다. 두 변경 중 어느 것이 다음 커밋에 들어가는지, 두 상태를 각각 어떤 명령으로 확인할 수 있는지 설명하시오.
2. `main`에서 새 브랜치를 만들어 점 색을 바꾸시오. 그래프를 실행해 결과를 확인하고, 변경을 커밋한 뒤 GitHub에서 Pull Request를 열어 수정한 줄을 확인하시오.
3. 저장소를 별도 폴더에 복제한 직후에는 `plot.png`가 없다. 그 이유와 그림을 재생성하는 방법을 설명하시오.

<!--
풀이:
1. git add를 실행할 때의 파일 내용이 커밋 후보에 담긴다. git diff --staged로 커밋 후보를, git diff로 그 뒤에 한 수정을 확인한다.
2. git switch -c change-marker-color를 실행한다. ax.scatter(time_s, signal_mv, color="tab:orange")로 바꾸고 그래프를 다시 그린다. git add plot_data.py, git commit -m "Change scatter marker color", git push -u origin change-marker-color를 실행한 뒤 main으로 향하는 Pull Request를 연다.
3. plot.png는 .gitignore에 포함되어 커밋하지 않은 생성물이다. Matplotlib이 설치된 환경에서 python plot_data.py를 실행한다.
-->

다음 강의에서는 측정점에 가장 잘 맞는 직선을 구한다. 적합 코드와 그림을 바꿀 때 측정점만 그린 상태와 적합선을 추가한 상태를 서로 다른 커밋으로 남겨 보자.

---

[이전 강의](/assets/lecture_notes/1_2_data_mse/data_mse_15_기초_matplotlib3.md) · [강의 목록](/_lectures/1_2_data_mse.md) · [다음 강의](/assets/lecture_notes/1_2_data_mse/data_mse_17_최소자승법.md)
