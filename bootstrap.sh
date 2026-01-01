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

# Homebrew 환경 설정
eval "$(/opt/homebrew/bin/brew shellenv)"

# =============================================================================
# 3. chezmoi & Infisical CLI
# =============================================================================
echo "📦 필수 도구 설치 중..."
brew install chezmoi infisical/get-cli/infisical

# =============================================================================
# 4. chezmoi로 dotfiles 적용
# =============================================================================
echo "🔧 dotfiles 적용 중..."
chezmoi init --apply operaun

echo ""
echo "=============================================="
echo "✅ Bootstrap 완료!"
echo "=============================================="
echo ""
echo "다음 단계:"
echo "  1. 새 터미널을 열어 설정 적용 확인"
echo "  2. 'auth-start' 실행하여 시크릿 로드"
echo "  3. 'nvim' 실행하여 LazyVim 플러그인 설치"
echo ""
