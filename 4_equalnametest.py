# pdf에서 번호 찾음-> 해당 페이지를 별도 pdf로 변경->프린트

import PyPDF2
import win32print

pdf_path = "C:/Users/swwoo/Desktop/VS TEST/kensa.pdf"
number = "363189141066"
# formatted_number = "KIT2" + number

def find_pages_with_number(pdf_path, number):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    pages_with_number = []

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        page_text = page.extractText()
        # if number in page_text:
        if page_text.strip() == number:   
            pages_with_number.append(page_num)

    pdf_file.close()

    return pages_with_number

def create_printable_pdf(pdf_path, pages_to_print):
    output_pdf_path = "C:/Users/swwoo/Desktop/VS TEST/printable.pdf"
    output_pdf = PyPDF2.PdfFileWriter()

    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    for page_num in pages_to_print:
        page = pdf_reader.getPage(page_num)
        output_pdf.addPage(page)

    output_pdf_stream = open(output_pdf_path, 'wb')
    output_pdf.write(output_pdf_stream)
    output_pdf_stream.close()

    pdf_file.close()

    return output_pdf_path


def print_pages_with_number(pdf_path, number):
    pages_with_number = find_pages_with_number(pdf_path, number)
    printer_name = win32print.GetDefaultPrinter()

    h_printer = win32print.OpenPrinter(printer_name)
    doc_info = ("Pages with Number", None, "RAW")

    output_pdf_path = create_printable_pdf(pdf_path, pages_with_number)

    with open(output_pdf_path, "rb") as pdf_file:
        pdf_data = pdf_file.read()

        job_id = win32print.StartDocPrinter(h_printer, 1, doc_info)
        win32print.StartPagePrinter(h_printer)
        win32print.WritePrinter(h_printer, pdf_data)
        win32print.EndPagePrinter(h_printer)
        win32print.EndDocPrinter(h_printer)

    win32print.ClosePrinter(h_printer)

print_pages_with_number(pdf_path, number)