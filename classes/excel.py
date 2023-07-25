import os
import openpyxl

from classes.tax_type import TaxType


class Excel(object):
    def __init__(self):
        self.resources_folder = os.path.join(os.getcwd(), "resources")
        self.input_folder = os.path.join(self.resources_folder, "input")
        self.template_folder = os.path.join(self.resources_folder, "templates")
        self.output_folder = os.path.join(self.resources_folder, "output")
        self.yaml_folder = os.path.join(self.output_folder, "yaml")
        self.yaml_path = os.path.join(self.yaml_folder, "spr_and_dr_measure_condition_dialog_config.yaml")

        self.excel_source = os.path.join(self.input_folder, "Trader Declaration Data 3.xlsx")

        self.template_blank = os.path.join(self.template_folder, "template_blank.html")
        self.template_dr = os.path.join(self.template_folder, "template_dr.html")
        self.template_spr = os.path.join(self.template_folder, "template_spr.html")
        self.template_spr_dr = os.path.join(self.template_folder, "template_spr_dr.html")

        os.makedirs(self.output_folder, exist_ok=True)
        os.makedirs(self.yaml_folder, exist_ok=True)

    def process_excel(self):
        self.yaml = "---\n"
        self.tax_types = []
        wb = openpyxl.load_workbook(self.excel_source)
        ws = wb.active
        cell_range = ws['A1':'N49']
        for row in cell_range:
            tax_type = TaxType(row)

            if tax_type.is_dr and tax_type.is_spr:
                tax_type.apply_template(self.template_spr_dr, self.output_folder)
            elif tax_type.is_dr:
                tax_type.apply_template(self.template_dr, self.output_folder)
            elif tax_type.is_spr:
                tax_type.apply_template(self.template_spr, self.output_folder)
            else:
                tax_type.apply_template(self.template_blank, self.output_folder)

            self.tax_types.append(tax_type)
            self.yaml += tax_type.yaml

        self.write_yaml()

    def write_yaml(self):
        f = open(self.yaml_path, 'w')
        f.write(self.yaml)
        f.close()
