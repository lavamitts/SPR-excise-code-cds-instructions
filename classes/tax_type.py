import os
import sys
import shutil


class TaxType(object):
    def __init__(self, row):
        self.excise_code = row[0].value
        self.description = row[1].value
        self.rate = row[2].value
        self.formula = row[3].value
        self.tax_type = row[4].value
        self.additional_code = row[5].value
        self.measurement_unit = row[6].value
        self.measurement_unit_value = row[7].value
        self.measurement_unit_code = row[8].value
        self.asv = row[9].value
        self.spr = row[10].value
        self.eas_code = row[11].value
        self.eas_asv = row[12].value
        self.supp_unit = row[13].value

    def apply_template(self, template, output_folder):
        self.output_folder = output_folder
        f = open(template, 'r')
        content = f.read()

        self.content = content.replace("{{excise_code}}", str(self.excise_code))
        self.content = self.content.replace("{{description}}", str(self.description))
        self.content = self.content.replace("{{rate}}", str(self.rate))
        self.content = self.content.replace("{{formula}}", str(self.formula))
        self.content = self.content.replace("{{tax_type}}", str(self.tax_type))
        self.content = self.content.replace("{{additional_code}}", str(self.additional_code))
        self.content = self.content.replace("{{measurement_unit}}", str(self.measurement_unit))
        self.content = self.content.replace("{{measurement_unit_value}}", str(self.measurement_unit_value))
        self.content = self.content.replace("{{measurement_unit_code}}", str(self.measurement_unit_code))
        self.content = self.content.replace("{{asv}}", str(self.asv))
        self.content = self.content.replace("{{spr}}", str(self.spr))
        self.content = self.content.replace("{{eas_code}}", str(self.eas_code))
        self.content = self.content.replace("{{eas_asv}}", str(self.eas_asv))
        self.content = self.content.replace("{{supp_unit}}", str(self.supp_unit))

        f.close()
        self.get_yaml()
        self.write()
        self.copy()

    def write(self):
        self.filename = "_small_producer_relief_{additional_code}.html".format(additional_code=self.additional_code)
        self.filepath = os.path.join(self.output_folder, self.filename)
        f = open(self.filepath, 'w')
        f.write(self.content)
        f.close()

    def copy(self):
        dest = "/Users/MLavis.Admin/sites and projects/1. Online Tariff/01. prototypes/ott-prototype/app/views/spr_conditions"
        dest = os.path.join(dest, self.filename)
        shutil.copy(self.filepath, dest)

    def get_yaml(self):
        self.yaml = """- additional_code: 'X{tax_type}'
  measure_type_id: '306'
  content_file: 'small_producer_relief_X{tax_type}'
  overwrite: false
""".format(tax_type=self.tax_type)
