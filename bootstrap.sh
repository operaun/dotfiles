#!/bin/bash
set -euo pipefail

echo "🚀 Dotfiles Bootstrap 시작..."

# =============================================================================
# 1. Xcode Command Line Tools
# =============================================================================
if ! xcode-select -p &>/dev/null; then
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
if ! command -v brew &>/dev/null; then
  echo "🍺 Homebrew 설치 중..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Homebrew 환경 설정 (Apple Silicon / Intel Mac 호환)
if [[ -x /opt/homebrew/bin/brew ]]; then
  eval "$(/opt/homebrew/bin/brew shellenv)"
elif [[ -x /usr/local/bin/brew ]]; then
  eval "$(/usr/local/bin/brew shellenv)"
fi

# =============================================================================
# 3. chezmoi 설치
# =============================================================================
if ! command -v chezmoi &>/dev/null; then
  echo "📦 chezmoi 설치 중..."
  brew install chezmoi
fi

# =============================================================================
# 4. chezmoi로 dotfiles 적용
# =============================================================================
echo ""
echo "🔧 dotfiles 설정을 시작합니다..."
echo "   - Profile 선택: personal (개인용) / work (업무용)"
echo "   - Git 이름/이메일 입력"
echo ""
chezmoi init --apply operaun

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
