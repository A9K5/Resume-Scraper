
import PyPDF2
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
from io import StringIO
from collections import defaultdict
import re
import pandas as pd

def Solve(text):
    z = []
    s = ""
    out = {}
    for i in text:
        if i == '\n':
            s.replace("\n","")
            z.append((s.encode('ascii', 'ignore')).decode("utf-8"))
            s = ""
        else:
            s += i
    for i in z:
        if re.search("Name ",i):
            out["Name"] = i[4:]
        if re.search("Mob",i):
            out["Mob"] = i[7:]
    put = text[text.index("Skill")+6:text.index("Experience")-1]
    out["Skill"]= (put.encode('ascii', 'ignore')).decode("utf-8").replace("\n","")
    return out


path = sys.argv[1]
# path = "./Resume2.pdf"
pdf = PyPDF2.PdfFileReader(open(path, "rb"))
fp = open(path, 'rb')
num_of_pages = pdf.getNumPages()
# print("num_of_pages ",num_of_pages)
extract = ""
output = pd.DataFrame()

for i in range(0,num_of_pages):
    inside = [i]
    pagenos=set(inside)
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    text = ""
    # print(pagenos)
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
        text = retstr.getvalue()
        retstr.truncate(0)

        out = Solve(text)
        output = output.append(out, ignore_index=True)

    output.to_csv('./List2.csv', index = False)

        