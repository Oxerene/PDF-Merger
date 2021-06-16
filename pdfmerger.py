import sys
import PyPDF2

files = sys.argv[1:]

def pdfMerge(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')

pdfMerge(files)