#!/bin/bash
#
# Build script for Ledall Roll Enhanced Study Guide PDF
#
# Usage: ./scripts/build-pdf.sh
#

set -e  # Exit on error

echo "=========================================="
echo "Building Ledall Roll Enhanced Study Guide"
echo "=========================================="
echo ""

# Check if required tools are installed
if ! command -v pandoc &> /dev/null; then
    echo "✗ Error: Pandoc is not installed."
    echo "Run ./scripts/install-build-tools.sh first."
    exit 1
fi

if ! command -v xelatex &> /dev/null; then
    echo "✗ Error: XeLaTeX is not installed."
    echo "Run ./scripts/install-build-tools.sh first."
    exit 1
fi

# Check if source file exists
if [[ ! -f "Ledall_Longsword_manuscript_for_pdf.md" ]]; then
    echo "✗ Error: Source file not found: Ledall_Longsword_manuscript_for_pdf.md"
    echo "Make sure you're running this from the project root directory."
    exit 1
fi

# Check if image exists
if [[ ! -f "src/img/battle_of_pavia.jpg" ]]; then
    echo "⚠ Warning: Title page image not found: src/img/battle_of_pavia.jpg"
    echo "The PDF will be generated without the title page image."
fi

echo "Source: Ledall_Longsword_manuscript_for_pdf.md"
echo "Output: Ledall_Roll_Enhanced_Study_Guide_FINAL.pdf"
echo ""
echo "Building PDF... This may take 1-2 minutes."
echo ""

# Build the PDF
pandoc Ledall_Longsword_manuscript_for_pdf.md \
  -o Ledall_Roll_Enhanced_Study_Guide_FINAL.pdf \
  --pdf-engine=xelatex \
  --resource-path=.:src/img \
  2>&1 | grep -v "Missing character.*ſ" || true

# Check if build succeeded
if [[ -f "Ledall_Roll_Enhanced_Study_Guide_FINAL.pdf" ]]; then
    FILE_SIZE=$(du -h "Ledall_Roll_Enhanced_Study_Guide_FINAL.pdf" | cut -f1)
    echo ""
    echo "=========================================="
    echo "✓ PDF Generated Successfully!"
    echo "=========================================="
    echo ""
    echo "File: Ledall_Roll_Enhanced_Study_Guide_FINAL.pdf"
    echo "Size: $FILE_SIZE"
    echo ""
    echo "The PDF is ready for printing and binding."
else
    echo ""
    echo "✗ Build failed. Check the errors above."
    exit 1
fi
