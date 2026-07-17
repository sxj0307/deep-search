from pathlib import Path
import markdown
from weasyprint import HTML

from utils.logger_utils import logger


def convert_md_to_pdf_via_word(md_abs_path: Path, pdf_abs_path: Path) -> str:
    """
    macOS/Linux通用方案
    Markdown -> HTML -> PDF
    """

    try:
        with open(md_abs_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        html_body = markdown.markdown(
            md_content,
            extensions=["tables", "fenced_code"]
        )

        html_content = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                }}

                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}

                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                }}

                pre {{
                    background: #f5f5f5;
                    padding: 10px;
                }}
            </style>
        </head>
        <body>
            {html_body}
        </body>
        </html>
        """

        HTML(string=html_content).write_pdf(
            str(pdf_abs_path)
        )

        return f"成功转换: {pdf_abs_path}"

    except Exception as e:
        logger.error(f"PDF转换失败: {e}", exc_info=True)
        return f"转换失败: {e}"