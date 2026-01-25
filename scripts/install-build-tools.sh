#!/bin/bash
#
# Installation script for Ledall Roll Study Guide build tools
# Installs Pandoc, TinyTeX, and all required LaTeX packages
#
# Usage: ./scripts/install-build-tools.sh
#

set -e  # Exit on error

echo "=========================================="
echo "Ledall Roll Study Guide - Build Tools Setup"
echo "=========================================="
echo ""

# Detect OS
OS_TYPE="unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS_TYPE="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="macos"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    OS_TYPE="windows"
fi

echo "Detected OS: $OS_TYPE"
echo ""

# Check if Pandoc is installed
echo "Step 1: Checking for Pandoc..."
if command -v pandoc &> /dev/null; then
    PANDOC_VERSION=$(pandoc --version | head -n1)
    echo "✓ Pandoc already installed: $PANDOC_VERSION"
else
    echo "✗ Pandoc not found. Please install Pandoc manually:"
    echo ""
    if [[ "$OS_TYPE" == "linux" ]]; then
        echo "  sudo apt-get install pandoc   # Debian/Ubuntu"
        echo "  sudo dnf install pandoc        # Fedora"
    elif [[ "$OS_TYPE" == "macos" ]]; then
        echo "  brew install pandoc"
    elif [[ "$OS_TYPE" == "windows" ]]; then
        echo "  Download from: https://pandoc.org/installing.html"
    fi
    echo ""
    echo "After installing Pandoc, run this script again."
    exit 1
fi

echo ""

# Check if LaTeX is installed
echo "Step 2: Checking for LaTeX (TinyTeX/XeLaTeX)..."
if command -v xelatex &> /dev/null; then
    LATEX_VERSION=$(xelatex --version | head -n1)
    echo "✓ XeLaTeX already installed: $LATEX_VERSION"
else
    echo "✗ XeLaTeX not found. Installing TinyTeX..."
    echo ""

    if [[ "$OS_TYPE" == "windows" ]]; then
        echo "Please install TinyTeX manually on Windows:"
        echo "  1. Run PowerShell as Administrator"
        echo "  2. Execute: wget -qO- \"https://yihui.org/tinytex/install-bin-windows.bat\" | cmd"
        echo ""
        echo "After installing TinyTeX, run this script again."
        exit 1
    else
        # Install TinyTeX on macOS/Linux
        echo "Installing TinyTeX (this may take a few minutes)..."
        curl -sL "https://yihui.org/tinytex/install-unx.sh" | sh

        # Add to PATH for this session
        export PATH="$HOME/.TinyTeX/bin/x86_64-linux:$PATH"
        export PATH="$HOME/.TinyTeX/bin/x86_64-darwin:$PATH"

        if command -v xelatex &> /dev/null; then
            echo "✓ TinyTeX installed successfully"
        else
            echo "✗ TinyTeX installation failed. Please install manually."
            exit 1
        fi
    fi
fi

echo ""

# Install required LaTeX packages
echo "Step 3: Installing required LaTeX packages..."
echo "This may take several minutes as packages are downloaded..."
echo ""

# List of required packages
PACKAGES=(
    "setspace"
    "koma-script"
    "colortbl"
    "adjustbox"
    "background"
    "csquotes"
    "footmisc"
    "footnotebackref"
    "framed"
    "fvextra"
    "mdframed"
    "pagecolor"
    "sourcecodepro"
    "sourcesanspro"
    "titling"
    "zref"
    "environ"
    "trimspaces"
    "collectbox"
)

# Find tlmgr
TLMGR_CMD="tlmgr"
if [[ "$OS_TYPE" == "windows" ]]; then
    # Try to find tlmgr.bat in common locations
    if [[ -f "$APPDATA/TinyTeX/bin/windows/tlmgr.bat" ]]; then
        TLMGR_CMD="$APPDATA/TinyTeX/bin/windows/tlmgr.bat"
    elif [[ -f "$HOME/AppData/Roaming/TinyTeX/bin/windows/tlmgr.bat" ]]; then
        TLMGR_CMD="$HOME/AppData/Roaming/TinyTeX/bin/windows/tlmgr.bat"
    fi
fi

if ! command -v "$TLMGR_CMD" &> /dev/null; then
    echo "✗ tlmgr not found. Cannot install LaTeX packages."
    echo "Please ensure TinyTeX is properly installed and in your PATH."
    exit 1
fi

echo "Installing packages using: $TLMGR_CMD"
echo ""

for package in "${PACKAGES[@]}"; do
    echo -n "Installing $package... "
    if "$TLMGR_CMD" install "$package" &> /dev/null; then
        echo "✓"
    else
        # Package might already be installed
        echo "⊘ (already installed or failed)"
    fi
done

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "You can now build the PDF using:"
echo "  ./scripts/build-pdf.sh"
echo ""
echo "Or manually:"
echo "  pandoc Ledall_Longsword_manuscript_for_pdf.md \\"
echo "    -o Ledall_Roll_Enhanced_Study_Guide_FINAL.pdf \\"
echo "    --pdf-engine=xelatex \\"
echo "    --resource-path=.:src/img"
echo ""
echo "See BUILD.md for more information."
