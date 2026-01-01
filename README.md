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
| **Git** | 전역 설정, alias |
| **macOS** | 시스템 설정 (Finder, Dock, 키보드 등) |

## 🔐 시크릿 관리 (Personal 전용)

SSH/GPG 키를 Infisical에서 동적 로드:

```bash
auth-start   # Infisical에서 SSH/GPG 키 로드 (8시간 캐싱)
auth-stop    # 모든 인증 정보 삭제
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
├── private_dot_ssh/            # SSH 공개키
├── private_dot_gnupg/          # GPG 공개키, agent 설정
└── bootstrap.sh                # 원라이너 부트스트랩
```

## 🔄 업데이트

```bash
chezmoi update   # GitHub에서 최신 dotfiles 가져와서 적용
```

## 📝 License

MIT
