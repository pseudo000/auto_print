import win32print
import PyPDF2
import win32api

pdf_path = "C:/Users/swwoo/Desktop/VS TEST/kensa.pdf"
number = "363189141066"
formatted_number = "KIT2" + number

def find_pages_with_number(pdf_path, number):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    pages_with_number = []

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        page_text = page.extractText()
        if number in page_text:
            pages_with_number.append(page_num)

    pdf_file.close()

    return pages_with_number

def print_pages_with_number(pdf_path, number):
    pages_with_number = find_pages_with_number(pdf_path, number)
    printer_name = win32print.GetDefaultPrinter()

    h_printer = win32print.OpenPrinter(printer_name)
    doc_info = ("Pages with Number", None, "RAW")

    for page_num in pages_with_number:
        job_id = win32print.StartDocPrinter(h_printer, 1, doc_info)
        win32print.StartPagePrinter(h_printer)

        pdf_file = open(pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        page = pdf_reader.getPage(page_num)
        page_text = page.extractText()
        data = page_text.encode('utf-8')
        win32print.WritePrinter(h_printer, data)

        pdf_file.close()

        win32print.EndPagePrinter(h_printer)
        win32print.EndDocPrinter(h_printer)

    win32print.ClosePrinter(h_printer)

print_pages_with_number(pdf_path, formatted_number)
