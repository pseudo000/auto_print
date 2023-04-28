import PyPDF2
import win32print

pdf_path = "C:/Users/swwoo/Desktop/VS TEST/kensa.pdf"
number = "363189141066"
formatted_number = "KIT2" + number
# formatted_number = number[:4] + '-' + number[4:8] + '-' + number[8:]

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

pages_with_number = find_pages_with_number(pdf_path, formatted_number)
print(pages_with_number)
