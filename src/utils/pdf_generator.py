import re
from fpdf import FPDF


def generate_swot_pdf(idea: str, report_text: str) -> bytearray:
    """
    Takes the business idea and the Markdown report, cleans it up, and returns a generated PDF as a bytearray for Streamlit to download.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Header
    pdf.set_font("helvetica", style="B", size=18)
    pdf.cell(
        0, 10, "VentureVal: Executive Report", new_x="LMARGIN", new_y="NEXT", align="C"
    )
    pdf.ln(5)

    # The Idea
    pdf.set_font("helvetica", style="I", size=12)
    pdf.set_text_color(100, 100, 100)  # Dark gray
    pdf.multi_cell(0, 8, f"Analyzed Idea: {idea}")
    pdf.ln(5)

    # Clean up the Markdown for the PDF
    # FPDF2 supports some basic markdown, but it's safer to strip asterisks and hashes for a clean look
    clean_text = re.sub(r"\*\*(.*?)\*\*", r"\1", report_text)  # Remove bold **
    clean_text = re.sub(r"#+\s*(.*?)\n", r"\1\n", clean_text)  # Remove heading #

    # Body Text
    pdf.set_font("helvetica", size=11)
    pdf.set_text_color(0, 0, 0)  # Back to black

    # Replace emojis or unsupported characters (FPDF's default fonts don't like emojis)
    safe_text = clean_text.encode("latin-1", "replace").decode("latin-1")

    pdf.multi_cell(0, 6, safe_text)

    # Return the raw PDF bytes
    return bytes(pdf.output())
