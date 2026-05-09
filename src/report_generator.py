from fpdf import FPDF

def generate_pdf_report(ticker, analysis):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(200,10,txt="Stock Market Analysis Report", ln=True)

    pdf.ln(10)

    pdf.cell(200,10,txt=f"Ticker: {ticker}", ln=True)

    pdf.cell(200,10,txt=f"Highest Price: {analysis['highest']:.2f}", ln=True)

    pdf.cell(200,10,txt=f"Lowest Price: {analysis['lowest']:.2f}", ln=True)

    pdf.cell(200,10,txt=f"Volatility: {analysis['volatility']:.4f}", ln=True)

    pdf.output(f"reports/{ticker}_report.pdf")