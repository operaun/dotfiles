#!/bin/bash
set -euo pipefail

SETUP_MODE="full"

usage() {
  cat <<'EOF'
Usage: bootstrap.sh [--minimal|--full] [--help]

Options:
  --minimal   Skip package installation steps and apply only core dotfiles.
  --full      Run full setup (default).
  --help      Show this help message.
EOF
}

for arg in "$@"; do
  case "$arg" in
    --minimal|--no-packages)
      SETUP_MODE="minimal"
      ;;
    --full|--with-packages)
      SETUP_MODE="full"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "❌ Unknown option: $arg"
      usage
      exit 1
      ;;
  esac
done

export PATH="$HOME/.local/bin:$PATH"

echo "🚀 Dotfiles Bootstrap 시작..."
echo "   - Setup mode: $SETUP_MODE"

if ! command -v chezmoi &>/dev/null; then
  echo "📦 chezmoi 설치 중..."
  sh -c "$(curl -fsLS get.chezmoi.io)" -- -b "$HOME/.local/bin"
fi

# =============================================================================
# 1. Xcode Command Line Tools
# =============================================================================
if [[ "$SETUP_MODE" == "full" ]] && ! xcode-select -p &>/dev/null; then
  echo "📦 Xcode Command Line Tools 설치 중..."
  xcode-select --install
  echo "⏳ 설치 팝업에서 '설치'를 클릭하세요..."
  
  # 설치 완료 대기
  until xcode-select -p &>/dev/null; do
    sleep 5
  done
  echo "✅ Xcode Command Line Tools 설치 완료"
fi

# =============================================================================
# 2. Homebrew
# =============================================================================
if [[ "$SETUP_MODE" == "full" ]] && ! command -v brew &>/dev/null; then
  echo "🍺 Homebrew 설치 중..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Homebrew 환경 설정 (Apple Silicon / Intel Mac 호환)
if [[ "$SETUP_MODE" == "full" ]] && [[ -x /opt/homebrew/bin/brew ]]; then
  eval "$(/opt/homebrew/bin/brew shellenv)"
elif [[ "$SETUP_MODE" == "full" ]] && [[ -x /usr/local/bin/brew ]]; then
  eval "$(/usr/local/bin/brew shellenv)"
fi

# =============================================================================
# 4. chezmoi로 dotfiles 적용
# =============================================================================
echo ""
echo "🔧 dotfiles 설정을 시작합니다..."
echo "   - Profile 선택: personal (개인용) / work (업무용)"
echo "   - Git 이름/이메일 입력"
echo ""
if ! chezmoi init --apply --promptChoice "Setup mode=$SETUP_MODE" operaun; then
  echo "❌ chezmoi 설정 적용에 실패했습니다."
  exit 1
fi

echo ""
echo "=============================================="
echo "✅ Bootstrap 완료!"
echo "=============================================="
echo ""
echo "다음 단계:"
echo "  1. 새 터미널을 열어 설정 적용 확인"
echo "  2. 'nvim' 실행하여 LazyVim 플러그인 설치"
echo ""
echo "💡 Personal 프로필을 선택했다면:"
echo "   - 'auth-start' 실행하여 SSH/GPG 키 로드"
echo ""
