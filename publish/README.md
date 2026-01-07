# PDF Publishing Tools

This directory contains tools for converting the Ledall Roll study guide from Markdown to PDF for printing and publishing.

## Quick Start

### 1. Set up the virtual environment

**Windows:**
```cmd
setup_venv.bat
```

**Linux/macOS/Git Bash:**
```bash
bash setup_venv.sh
```

### 2. Activate the virtual environment

**Windows:**
```cmd
venv\Scripts\activate.bat
```

**Linux/macOS/Git Bash:**
```bash
source venv/bin/activate
```

### 3. Convert to PDF

**Default (converts main manuscript):**
```bash
python convert_to_pdf.py
```

**Specify input file:**
```bash
python convert_to_pdf.py ../Ledall_Longsword_manuscript.md
```

**Specify input and output:**
```bash
python convert_to_pdf.py ../Ledall_Longsword_manuscript.md output.pdf
```

## How It Works

The conversion script uses **xhtml2pdf** (pure Python) by default, which works on Windows without requiring GTK+ or other external dependencies. It:

1. Reads your Markdown file
2. Converts it to HTML with professional styling
3. Generates a print-ready PDF with:
   - Proper page headers and footers
   - Table of contents support
   - Formatted tables (for your step breakdowns)
   - Professional typography
   - Page break controls

### Optional: Pandoc or WeasyPrint Support

The script supports multiple PDF engines with automatic fallback:

1. **Pandoc** (best quality, requires system installation):
   ```bash
   pip install pypandoc
   ```
   Requires Pandoc installed system-wide: <https://pandoc.org/installing.html>

2. **WeasyPrint** (better CSS support, requires GTK+ on Windows):
   ```bash
   pip install weasyprint
   ```
   On Windows, you'll need to install GTK+ runtime separately.

3. **xhtml2pdf** (default, pure Python, works everywhere):
   Already included - no additional setup needed!

The script automatically detects and uses the best available option.

## Output

PDFs are generated in the `publish/` directory by default. The script looks for Markdown files in the project root (`../`) if you don't specify a full path.

## Customization

Edit `convert_to_pdf.py` to customize:
- Page size and margins
- Fonts and typography
- Table styling
- Header/footer content
- Color schemes

## Requirements

See `requirements.txt` for the full list of Python packages needed. The main dependencies are:
- `markdown` - Markdown parsing
- `xhtml2pdf` - PDF generation (pure Python, Windows-friendly)
- `pymdown-extensions` - Enhanced Markdown features

All packages are installed automatically when you run the setup script.

## Notes

- **Images**: xhtml2pdf has limited image support. Complex images may not render perfectly.
- **CSS**: Some advanced CSS features (like `@page` rules) are not supported by xhtml2pdf but work with WeasyPrint/Pandoc.
- **Quality**: For best results, consider using Pandoc if you have it installed system-wide.
