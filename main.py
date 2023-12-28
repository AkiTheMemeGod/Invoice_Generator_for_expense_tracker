import pandas as pd
from fpdf import FPDF
import time as t

df = pd.read_csv("report.csv", sep=",", index_col=None)


def generate_invoice(df):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", size=40, style="B")
    pdf.image(name="Untitled design.png", type="png", w=30, h=30, link="https://spend-it-akash.streamlit.app")
    pdf.cell(w=20, h=10, txt='', align="C",ln=1)
    pdf.cell(w=20, h=10, txt='', align="C",ln=1)
    pdf.cell(w=20, h=10, txt='', align="C",ln=1)
    pdf.cell(w=20, h=10, txt='', align="C",ln=1)


    pdf.set_text_color(243, 18, 18)
    pdf.text(txt="$pend-It.",x=75, y=20)

    pdf.set_text_color(100, 100, 100)
    pdf.set_font(family="Times", size=20, style="B")
    pdf.text(txt="Expense Report",x=77, y=35)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family="Times", size=18, style="B")
    pdf.text(txt="AkiTheMemeGod", x=156, y=25)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font(family="Times", size=18, style="B")
    pdf.text(txt=t.strftime("Date : %d/%m/%y"), x=165, y=35)
    pdf.line(x1=10,x2=200,y1=45,y2=45)

    pdf.set_font(family="times", size=25,style="B")
    pdf.set_text_color(50, 50, 50)
    pdf.cell(w=20, h=10, txt='Date', align="C")
    pdf.cell(w=50, h=10, txt='Month',align="C")
    pdf.cell(w=40, h=10, txt='Category',align="C")
    pdf.cell(w=55, h=10, txt='Type',align="C")
    pdf.cell(w=32, h=10, txt='Amount',ln=1,align="C")
    pdf.cell(w=20, h=3, txt='', align="C")
    pdf.cell(w=50, h=3, txt='',align="C")
    pdf.cell(w=40, h=3, txt='',align="C")
    pdf.cell(w=55, h=3, txt='',align="C")
    pdf.cell(w=32, h=3, txt='',ln=1,align="C")

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=25)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(w=20, h=10, txt=str(row['Date']), border=1, align="C")

        pdf.cell(w=50, h=10, txt=str(row['Month']), border=1, align="C")
        pdf.cell(w=40, h=10, txt=str(row['Category']), border=1, align="C")
        pdf.cell(w=55, h=10, txt=str(row['Type']), border=1, align="C")
        pdf.cell(w=32, h=10, txt=str(row['Amount']), border=1,ln=1, align="C")

    total_income = str(df.groupby(by=['Category']).sum()[['Amount']]['Amount'][1])
    total_expense = str(df.groupby(by=['Category']).sum()[['Amount']]['Amount'][0])


    pdf.set_font(family="Times", size=25,style="B")
    pdf.cell(w=20, h=3, txt='', align="C")
    pdf.cell(w=50, h=3, txt='',align="C")
    pdf.cell(w=40, h=3, txt='',align="C")
    pdf.cell(w=55, h=3, txt='',align="C")
    pdf.cell(w=32, h=3, txt='',ln=1,align="C")
    pdf.set_text_color(33, 179, 42)
    pdf.cell(w=20, h=10, txt='', align="C")
    pdf.cell(w=50, h=10, txt='', align="C")
    pdf.cell(w=40, h=10, txt='Total', align="R")
    pdf.cell(w=55, h=10, txt='Income : ', align="L")
    pdf.cell(w=32, h=10, txt=total_income, ln=1, align="L")
    pdf.set_font(family="Times", size=25,style="B")


    pdf.cell(w=20, h=3, txt='', align="C")
    pdf.cell(w=50, h=3, txt='',align="C")
    pdf.cell(w=40, h=3, txt='',align="C")
    pdf.cell(w=55, h=3, txt='',align="C")
    pdf.cell(w=32, h=3, txt='',ln=1,align="C")
    pdf.set_text_color(255, 0, 0)
    pdf.cell(w=20, h=10, txt='', align="C")
    pdf.cell(w=50, h=10, txt='', align="C")
    pdf.cell(w=40, h=10, txt='Total', align="R")
    pdf.cell(w=55, h=10, txt='Expense : ', align="L")
    pdf.cell(w=32, h=10, txt=total_expense, ln=1, align="L")


    pdf.output("report.pdf")