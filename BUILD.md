# Building the PDF from Source

This document explains how to build the final PDF version of the Ledall Roll Enhanced Study Guide from the Markdown source.

## Prerequisites

You need to install:
1. **Pandoc** - Document converter
2. **TinyTeX** - Lightweight LaTeX distribution
3. **Required LaTeX packages** - For professional formatting

## Quick Start (Windows)

Run the installation script:

```bash
./scripts/install-build-tools.sh
```

This will install Pandoc, TinyTeX, and all required LaTeX packages.

## Manual Installation

### 1. Install Pandoc

**Windows:**
- Download the installer from [pandoc.org/installing.html](https://pandoc.org/installing.html)
- Run the installer
- Verify installation: `pandoc --version`

**macOS:**
```bash
brew install pandoc
```

**Linux:**
```bash
sudo apt-get install pandoc  # Debian/Ubuntu
# or
sudo dnf install pandoc      # Fedora
```

### 2. Install TinyTeX

TinyTeX is a lightweight, portable LaTeX distribution perfect for Pandoc.

**Windows (via PowerShell):**
```powershell
wget -qO- "https://yihui.org/tinytex/install-bin-windows.bat" | cmd
```

**macOS/Linux:**
```bash
curl -sL "https://yihui.org/tinytex/install-unx.sh" | sh
```

**Verify installation:**
```bash
xelatex --version
```

You should see output indicating XeTeX version 3.141592653 or similar.

### 3. Install Required LaTeX Packages

TinyTeX requires you to manually install packages. Run these commands:

**Windows:**
```bash
tlmgr install setspace koma-script colortbl adjustbox background csquotes \
  footmisc footnotebackref framed fvextra mdframed pagecolor sourcecodepro \
  sourcesanspro titling zref environ trimspaces collectbox
```

**Note:** On Windows with TinyTeX, you may need to use the full path:
```bash
"C:\Users\YOUR_USERNAME\AppData\Roaming\TinyTeX\bin\windows\tlmgr.bat" install [packages]
```

**macOS/Linux:**
```bash
tlmgr install setspace koma-script colortbl adjustbox background csquotes \
  footmisc footnotebackref framed fvextra mdframed pagecolor sourcecodepro \
  sourcesanspro titling zref environ trimspaces collectbox
```

## Building the PDF

Once everything is installed:

```bash
# From the project root directory
pandoc Ledall_Longsword_manuscript_for_pdf.md \
  -o Ledall_Roll_Enhanced_Study_Guide_FINAL.pdf \
  --pdf-engine=xelatex \
  --resource-path=.:src/img
```

Or use the build script:

```bash
./scripts/build-pdf.sh
```

The final PDF will be generated as `Ledall_Roll_Enhanced_Study_Guide_FINAL.pdf` (approximately 2.7MB, 172 pages).

## PDF Features

The generated PDF includes:
- **Custom title page** with Battle of Pavia historical image
- **Modern typography** using Merriweather font (designed 2016)
- **Professional formatting** - 1" margins, 1.2 line spacing
- **Comprehensive table of contents** (3 levels deep)
- **Book-style layout** - Single-sided, perfect for hole-punching and binding
- **Headers and footers** with page numbers
- **172 pages** covering all 41 plays

## Troubleshooting

### Missing LaTeX Packages

If you see errors like `! LaTeX Error: File 'package.sty' not found`, install the missing package:

```bash
tlmgr install package-name
```

### Images Not Showing

Make sure you're using the `--resource-path` option:

```bash
--resource-path=.:src/img
```

### Permission Denied on PDF

Close the PDF file in your viewer before regenerating.

### Missing Fonts

The build uses Merriweather font. On most systems this is available by default. If you get font errors:

- **Windows**: Merriweather should be included with Windows 10/11
- **macOS**: Install from Font Book or `brew install font-merriweather`
- **Linux**: `sudo apt-get install fonts-merriweather`

Alternatively, you can change the font in `Ledall_Longsword_manuscript_for_pdf.md` by editing the `mainfont` setting.

## Build Options

You can customize the PDF by editing the YAML metadata block at the top of `Ledall_Longsword_manuscript_for_pdf.md`:

- `mainfont`: Change the font (try "Georgia", "Palatino Linotype", "Noto Serif")
- `fontsize`: Change font size (10pt, 11pt, 12pt)
- `linestretch`: Adjust line spacing (1.0 = single, 1.5, 2.0 = double)
- `geometry`: Change margins (e.g., `margin=1.5in`)

## File Structure

```
.
├── Ledall_Longsword_manuscript.md           # Original source manuscript
├── Ledall_Longsword_manuscript_for_pdf.md   # PDF-optimized version with YAML metadata
├── Ledall_Roll_Enhanced_Study_Guide_FINAL.pdf  # Final generated PDF
├── src/
│   └── img/
│       └── battle_of_pavia.jpg              # Title page image
├── scripts/
│   ├── install-build-tools.sh               # Installation script
│   └── build-pdf.sh                          # Build script
└── BUILD.md                                  # This file
```

## Resources

- [Pandoc User Guide](https://pandoc.org/MANUAL.html)
- [TinyTeX Documentation](https://yihui.org/tinytex/)
- [Pandoc Markdown Syntax](https://pandoc.org/MANUAL.html#pandocs-markdown)
- [Font Selection Guide](https://fonts.google.com/)

## License

See LICENSE.md for details on manuscript licensing and usage.
