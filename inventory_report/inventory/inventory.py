from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory():

    def import_data(path: str, report_type: str) -> str:
        product_list = []
        with open(path) as file:
            products_reader = csv.DictReader(file)
            for product in products_reader:
                product_list.append(product)
        if report_type == "simples":
            return SimpleReport.generate(product_list)
        if report_type == "completo":
            return CompleteReport.generate(product_list)
