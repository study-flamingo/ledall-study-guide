#!/bin/bash
# Setup script for Windows (Git Bash) / Linux / macOS

echo "Setting up Python virtual environment for PDF conversion..."

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

echo ""
echo "✓ Virtual environment setup complete!"
echo ""
echo "To activate the virtual environment:"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "  source venv/Scripts/activate"
else
    echo "  source venv/bin/activate"
fi
echo ""
echo "Then run (from the publish/ directory):"
echo "  python convert_to_pdf.py"
echo ""
echo "Or specify a file:"
echo "  python convert_to_pdf.py ../Ledall_Longsword_manuscript.md"
