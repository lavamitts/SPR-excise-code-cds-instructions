import os
import openpyxl

from classes.tax_type import TaxType


class Excel(object):
    def __init__(self):
        self.resources_folder = os.path.join(os.getcwd(), "resources")
        self.input_folder = os.path.join(self.resources_folder, "input")
        self.output_folder = os.path.join(self.resources_folder, "output")
        self.yaml_path = os.path.join(self.output_folder, "yaml", "test.yaml")

        self.excel_source = os.path.join(self.input_folder, "Trader Declaration Data 3.xlsx")
        self.template = os.path.join(self.input_folder, "template.html")

    def process_excel(self):
        self.yaml = "---\n"
        self.tax_types = []
        wb = openpyxl.load_workbook(self.excel_source)
        ws = wb.active
        cell_range = ws['A1':'N49']
        for row in cell_range:
            tax_type = TaxType(row)
            tax_type.apply_template(self.template, self.output_folder)
            self.tax_types.append(tax_type)
            self.yaml += tax_type.yaml

        self.write_yaml()

    def write_yaml(self):
        f = open(self.yaml_path, 'w')
        f.write(self.yaml)
        f.close()
