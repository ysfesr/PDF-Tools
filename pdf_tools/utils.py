from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def handle_uploaded_file(f):  
    with open('static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 

def extract_information(pdf_file):
    pdf = PdfFileReader(pdf_file)
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    dict = {}
    dict['author'] = information.author
    dict['creator'] = information.creator
    dict['producer'] = information.producer
    dict['subject'] = information.subject
    dict['title'] = information.title
    dict['nbr_page'] = number_of_pages
    return dict


def merge_pdfs(list_files):
    pdf_writer = PdfFileWriter()

    for file in list_files:
        if file:
            pdf_reader = PdfFileReader(file)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(os.path.join('media', 'merged_file.pdf'), 'wb') as out:
        pdf_writer.write(out)