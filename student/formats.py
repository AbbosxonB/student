from import_export.formats.base_formats import XLS, XLSX

class CustomXLS(XLS):
    def get_title(self):
        return "xls"

class CustomXLSX(XLSX):
    def get_title(self):
        return "xlsx"
