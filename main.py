import PyPDF2
import sys
import os

# Creates a merger object
merger = PyPDF2.PdfMerger()

# Iterates over the pdfs in the current directory
for file in os.listdir(os.curdir):
   
    # Checks if file has a .pdf extenstion
    if file.endswith(".pdf"):
        
        merger.append(file)
    
    # Combined file name
    merger.write("combinedDocs.pdf")