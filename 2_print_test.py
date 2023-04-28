import win32print


def print_file(filepath):
    printer_name = win32print.GetDefaultPrinter()

    h_printer = win32print.OpenPrinter(printer_name)
    doc_info = win32print.PRINTER_INFO_2()
    doc_info['pDocName'] = "My Document"
    doc_info['pOutputFile'] = None
    doc_info['pDatatype'] = "RAW"

    job_id = win32print.StartDocPrinter(h_printer, 1, doc_info)
    win32print.StartPagePrinter(h_printer)

    with open(filepath, 'rb') as file:
        data = file.read()
        win32print.WritePrinter(h_printer, data)

    win32print.EndPagePrinter(h_printer)
    win32print.EndDocPrinter(h_printer)
    win32print.ClosePrinter(h_printer)

filepath = 'C:/Users/user/Documents/my_file.pdf'

print_file(filepath)
