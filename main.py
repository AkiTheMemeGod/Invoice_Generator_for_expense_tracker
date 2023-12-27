import pandas as pd
import os
from fpdf import FPDF
import time as t

os.system("pip freeze > requirements.txt")
df = pd.read_csv("report.csv", sep=",",index_col=None)
print(df)
df.to_excel("report.xlsx",index=False,sheet_name="Sheet 1")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font(family="Times", size=40, style="B")
pdf.image(name="Untitled design.png", type="png",w=50,h=50,link="https://spend-it-akash.streamlit.app")
pdf.cell(w=0, h=20, txt="$pend-It.",ln=1)

pdf.set_font(family="Times", size=20, style="B")
pdf.cell(w=50, h=8, txt="Expense Report",ln=1)

pdf.cell(w=50, h=8, txt=t.strftime("Date : %d/%m/%y"))

pdf.output("report.pdf")