#!/usr/bin/env python3
"""
Convert Markdown study guide to PDF for printing/publishing.

This script converts your Ledall Roll study guide from Markdown to a
professionally formatted PDF suitable for printing.

Usage:
    python convert_to_pdf.py [input.md] [output.pdf]

If no arguments provided, converts ../Ledall_Longsword_manuscript.md to
Ledall_Study_Guide.pdf in the publish/ directory.
"""

import sys
import os
from pathlib import Path
import markdown

# Try to import xhtml2pdf (pure Python, works on Windows)
try:
    from xhtml2pdf import pisa

    HAS_XHTML2PDF = True
except ImportError:
    HAS_XHTML2PDF = False

# Try to import weasyprint (requires GTK+ on Windows)
HAS_WEASYPRINT = False
WEASYPRINT_HTML = None
WEASYPRINT_FontConfiguration = None
try:
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration

    WEASYPRINT_HTML = HTML
    WEASYPRINT_FontConfiguration = FontConfiguration
    HAS_WEASYPRINT = True
except (ImportError, OSError):
    # OSError can occur if GTK+ libraries aren't available
    HAS_WEASYPRINT = False

# Try to import pypandoc as fallback (requires system Pandoc)
try:
    import pypandoc

    HAS_PYPANDOC = True
except ImportError:
    HAS_PYPANDOC = False

# Get the project root (parent of publish/)
PROJECT_ROOT = Path(__file__).parent.parent


def markdown_to_html(md_content, input_file=None, use_simple_css=False):
    """Convert Markdown to HTML with enhanced features."""
    # Configure markdown extensions for better formatting
    extensions = [
        "markdown.extensions.tables",  # Table support
        "markdown.extensions.fenced_code",  # Code blocks
        "markdown.extensions.toc",  # Table of contents
        "markdown.extensions.extra",  # Extra features
        "pymdownx.superfences",  # Enhanced code fences
    ]

    md = markdown.Markdown(extensions=extensions)
    html_body = md.convert(md_content)

    # Generate CSS - simplified for xhtml2pdf, full for WeasyPrint/Pandoc
    if use_simple_css:
        # Simplified CSS for xhtml2pdf (doesn't support @page)
        css_style = """
        body {
            font-family: "Georgia", "Times New Roman", serif;
            line-height: 1.6;
            color: #333;
            margin: 1in;
        }
        """
    else:
        # Full CSS with @page support for WeasyPrint/Pandoc
        css_style = """
        @page {
            size: letter;
            margin: 1in;
            @top-center {
                content: "The Ledall Roll - Enhanced Study Guide";
                font-size: 10pt;
                color: #666;
            }
            @bottom-center {
                content: "Page " counter(page);
                font-size: 10pt;
                color: #666;
            }
        }
        
        body {
            font-family: "Georgia", "Times New Roman", serif;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
        }
        """

    # Generate full HTML document with styling
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ledall Roll Study Guide</title>
    <style>
        {css_style}
        
        
        h1 {{
            font-size: 24pt;
            margin-top: 2em;
            margin-bottom: 1em;
            page-break-after: avoid;
            border-bottom: 2px solid #333;
            padding-bottom: 0.5em;
        }}
        
        h2 {{
            font-size: 20pt;
            margin-top: 1.5em;
            margin-bottom: 0.75em;
            page-break-after: avoid;
        }}
        
        h3 {{
            font-size: 16pt;
            margin-top: 1.25em;
            margin-bottom: 0.5em;
            page-break-after: avoid;
        }}
        
        h4 {{
            font-size: 14pt;
            margin-top: 1em;
            margin-bottom: 0.5em;
            page-break-after: avoid;
        }}
        
        /* Table styling for step breakdowns */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1em 0;
            page-break-inside: avoid;
        }}
        
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        /* Code and original text styling */
        code {{
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: "Courier New", monospace;
            font-size: 0.9em;
        }}
        
        pre {{
            background-color: #f4f4f4;
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
            page-break-inside: avoid;
        }}
        
        /* Blockquotes for original text */
        blockquote {{
            border-left: 4px solid #666;
            margin: 1em 0;
            padding-left: 1em;
            font-style: italic;
            color: #555;
        }}
        
        /* Lists */
        ul, ol {{
            margin: 0.5em 0;
            padding-left: 2em;
        }}
        
        li {{
            margin: 0.25em 0;
        }}
        
        /* Horizontal rules */
        hr {{
            border: none;
            border-top: 1px solid #ddd;
            margin: 2em 0;
        }}
        
        /* Page breaks */
        .page-break {{
            page-break-before: always;
        }}
        
        /* Avoid breaking inside important sections */
        .section {{
            page-break-inside: avoid;
        }}
        
        /* Citations and footnotes */
        sup {{
            font-size: 0.8em;
            vertical-align: super;
        }}
        
        /* Print-specific adjustments */
        @media print {{
            a {{
                color: #000;
                text-decoration: none;
            }}
            a[href^="http"]:after {{
                content: " (" attr(href) ")";
                font-size: 0.8em;
                color: #666;
            }}
        }}
    </style>
</head>
<body>
{html_body}
</body>
</html>"""

    return html


def convert_with_xhtml2pdf(md_file, pdf_file):
    """Convert Markdown to PDF using xhtml2pdf (pure Python, Windows-friendly)."""
    print(f"Reading Markdown file: {md_file}")
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    print("Converting Markdown to HTML...")
    html_content = markdown_to_html(md_content, md_file, use_simple_css=True)

    print(f"Generating PDF: {pdf_file}")
    with open(pdf_file, "wb") as result_file:
        pisa_status = pisa.CreatePDF(html_content, dest=result_file, encoding="utf-8")

    if pisa_status.err:
        raise Exception(f"Error creating PDF: {pisa_status.err}")
    print(f"Successfully created: {pdf_file}")


def convert_with_weasyprint(md_file, pdf_file):
    """Convert Markdown to PDF using WeasyPrint (requires GTK+ on Windows)."""
    if not HAS_WEASYPRINT:
        raise ImportError("WeasyPrint not available (requires GTK+ on Windows)")

    print(f"Reading Markdown file: {md_file}")
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    print("Converting Markdown to HTML...")
    html_content = markdown_to_html(md_content, md_file)

    print(f"Generating PDF: {pdf_file}")
    font_config = WEASYPRINT_FontConfiguration()
    WEASYPRINT_HTML(string=html_content).write_pdf(pdf_file, font_config=font_config)
    print(f"Successfully created: {pdf_file}")


def convert_with_pandoc(md_file, pdf_file):
    """Convert Markdown to PDF using Pandoc (requires system installation)."""
    if not HAS_PYPANDOC:
        raise ImportError("pypandoc not available. Install Pandoc system-wide first.")

    print(f"Converting {md_file} to PDF using Pandoc...")
    try:
        pypandoc.convert_file(
            md_file,
            "pdf",
            outputfile=pdf_file,
            extra_args=[
                "--pdf-engine=xelatex",
                "--toc",
                "--number-sections",
                "--variable=geometry:margin=1in",
                "--variable=fontsize:11pt",
            ],
        )
        print(f"Successfully created: {pdf_file}")
    except Exception as e:
        print(f"✗ Pandoc conversion failed: {e}")
        print("Falling back to xhtml2pdf...")
        if HAS_XHTML2PDF:
            convert_with_xhtml2pdf(md_file, pdf_file)
        elif HAS_WEASYPRINT:
            convert_with_weasyprint(md_file, pdf_file)
        else:
            raise Exception("No PDF conversion library available!")


def main():
    """Main conversion function."""
    # Determine input and output files
    if len(sys.argv) >= 2:
        # If path is absolute or relative to current dir, use as-is
        input_file = Path(sys.argv[1])
        if not input_file.is_absolute():
            # Try relative to project root first
            if (PROJECT_ROOT / input_file).exists():
                input_file = PROJECT_ROOT / input_file
            elif not input_file.exists():
                # Try relative to current directory (publish/)
                input_file = Path.cwd() / input_file
    else:
        # Default: look in project root
        input_file = PROJECT_ROOT / "Ledall_Longsword_manuscript.md"

    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])
        if not output_file.is_absolute():
            output_file = Path.cwd() / output_file
    else:
        # Default: output in publish/ directory
        output_file = Path.cwd() / input_file.stem.replace("_", "_").replace("-", "_") / ".pdf"
        output_file = Path.cwd() / f"{input_file.stem}.pdf"

    # Check if input file exists
    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        print(f"\nLooking for Markdown files in project root ({PROJECT_ROOT}):")
        for md in PROJECT_ROOT.glob("*.md"):
            print(f"  - {md.relative_to(PROJECT_ROOT)}")
        print(f"\nLooking in current directory ({Path.cwd()}):")
        for md in Path.cwd().glob("*.md"):
            print(f"  - {md}")
        sys.exit(1)

    # Try Pandoc first (if available), then xhtml2pdf, then WeasyPrint
    if HAS_PYPANDOC:
        print("Pandoc detected. Using Pandoc for conversion...")
        try:
            convert_with_pandoc(input_file, output_file)
        except Exception as e:
            print(f"Pandoc failed: {e}")
            if HAS_XHTML2PDF:
                print("Using xhtml2pdf instead...")
                convert_with_xhtml2pdf(input_file, output_file)
            elif HAS_WEASYPRINT:
                print("Using WeasyPrint instead...")
                convert_with_weasyprint(input_file, output_file)
            else:
                raise Exception("No PDF conversion library available!")
    elif HAS_XHTML2PDF:
        print("Using xhtml2pdf (pure Python, Windows-friendly)...")
        convert_with_xhtml2pdf(input_file, output_file)
    elif HAS_WEASYPRINT:
        print("Using WeasyPrint (requires GTK+ on Windows)...")
        convert_with_weasyprint(input_file, output_file)
    else:
        raise Exception("No PDF conversion library available! Install xhtml2pdf or pypandoc.")

    print(f"\nConversion complete!")
    print(f"  Input:  {input_file}")
    print(f"  Output: {output_file}")


if __name__ == "__main__":
    main()
