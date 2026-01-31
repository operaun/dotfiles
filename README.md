# dotfiles

> macOS 개발 환경 자동화 - [chezmoi](https://chezmoi.io) + [Infisical](https://infisical.com)

## 🚀 Quick Start

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/operaun/dotfiles/main/bootstrap.sh)"
```

설치 중 선택:
- **Profile**: `personal` (개인) / `work` (업무)
- **Git 정보**: 이름, 이메일

## 📦 포함 내용

| 구성요소 | 설명 |
|----------|------|
| **Brewfile** | CLI 도구 + GUI 앱 자동 설치 |
| **Zsh** | 모던 CLI 도구 alias, starship, zoxide |
| **Neovim** | LazyVim 자동 설치 |
| **Tmux** | 터미널 멀티플렉서 설정 |
| **Git** | 전역 설정, alias |
| **macOS** | 시스템 설정 (Finder, Dock, 키보드 등) |

## 🔐 시크릿 관리 (Personal 전용)

SSH/GPG 키를 Infisical에서 동적 로드:

```bash
auth-start          # Infisical에서 SSH/GPG 키 로드 (영구 캐싱)
auth-start --temp   # 12시간만 유효한 임시 모드
auth-stop           # 모든 인증 정보 삭제 + GPG agent 종료
```

### Infisical 시크릿 구성

| 키 | 용도 |
|----|------|
| `SSH_PRIVATE_KEY` | SSH 개인키 전문 |
| `GPG_PRIVATE_KEY` | GPG 개인키 (armor 형식) |
| `GIT_SIGNING_KEY` | GPG 키 ID |
| `GITHUB_TOKEN` | GitHub 인증 (선택) |

## 🖥️ 프로필

| 기능 | Personal | Work |
|------|:--------:|:----:|
| macOS 설정 | ✅ | ✅ |
| Brewfile | ✅ | ✅ |
| Zsh/Starship | ✅ | ✅ |
| LazyVim | ✅ | ✅ |
| Infisical 연동 | ✅ | ❌ |
| SSH/GPG 키 | ✅ | ❌ |

## 🛠️ 모던 CLI 도구

| 기존 | 대체 | 설명 |
|------|------|------|
| `ls` | `eza` | 컬러풀한 파일 목록 |
| `cat` | `bat` | 구문 강조 |
| `find` | `fd` | 빠른 파일 검색 |
| `grep` | `rg` | 빠른 텍스트 검색 |
| `cd` | `z` | 히스토리 기반 점프 |

기존 도구 필요시: `orig-ls`, `orig-cat` 등

## 📁 구조

```
~/.local/share/chezmoi/
├── .chezmoi.yaml.tmpl          # 설정 템플릿
├── .chezmoiscripts/            # 자동화 스크립트
├── dot_Brewfile                # Homebrew 패키지
├── dot_gitconfig.tmpl          # Git 설정
├── dot_zshrc.tmpl              # Zsh 설정
├── dot_tmux.conf               # Tmux 설정
├── private_dot_ssh/            # SSH 공개키
├── private_dot_gnupg/          # GPG 공개키, agent 설정
└── bootstrap.sh                # 원라이너 부트스트랩
```

## 🔄 업데이트

```bash
chezmoi update   # GitHub에서 최신 dotfiles 가져와서 적용
```

## ⚙️ 커스텀 설정 요약

기본값과 다른 주요 설정들입니다.

### Tmux

| 설정 | 기본값 | 변경값 | 설명 |
|------|--------|--------|------|
| Prefix | `Ctrl+b` | `Ctrl+a` | 더 접근하기 쉬운 위치 |
| 마우스 | off | on | 마우스로 pane 선택/리사이즈 |
| base-index | 0 | 1 | 창 번호 1부터 시작 |
| escape-time | 500ms | 0ms | Vim/Neovim 호환성 개선 |
| history-limit | 2000 | 50000 | 스크롤백 버퍼 증가 |
| 창 분할 | `"` / `%` | `-` / `\|` | 직관적인 키 |
| Pane 이동 | 방향키 | `hjkl` | Vim 스타일 |
| 복사 모드 | emacs | vi | Vim 키바인딩 |
| 클립보드 | - | pbcopy | macOS 클립보드 연동 |

### Zsh

| 설정 | 기본값 | 변경값 | 설명 |
|------|--------|--------|------|
| `ls` | /bin/ls | eza | 컬러풀한 파일 목록 |
| `cat` | /bin/cat | bat | 구문 강조 |
| `find` | /usr/bin/find | fd | 빠른 파일 검색 |
| `grep` | /usr/bin/grep | rg | 빠른 텍스트 검색 |
| `cd` | builtin | zoxide (`z`) | 히스토리 기반 점프 |
| 프롬프트 | 기본 | starship | 모던 쉘 프롬프트 |

> 💡 기존 도구 필요시: `orig-ls`, `orig-cat`, `orig-find`, `orig-grep`

### GPG Agent

| 설정 | 기본값 | 변경값 | 설명 |
|------|--------|--------|------|
| default-cache-ttl | 600 | 315360000 | 10년 (사실상 영구) |
| max-cache-ttl | 7200 | 315360000 | 10년 (사실상 영구) |
| default-cache-ttl-ssh | 1800 | 315360000 | SSH용 10년 캐싱 |
| max-cache-ttl-ssh | 7200 | 315360000 | SSH용 10년 캐싱 |
| pinentry-program | - | pinentry-mac | macOS 통합 |

> 💡 `auth-stop` 실행 시 GPG agent가 종료되어 캐시된 패스프레이즈가 삭제됩니다.

## 📝 License

MIT
