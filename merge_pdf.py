import os
from pypdf import PdfMerger
files = [file for file in os.listdir() if file.endswith('.pdf')]

print(files)
merger = PdfMerger()

for file in files:
    merger.append(file)

merger.write('merged_pdf.pdf')
merger.close()
