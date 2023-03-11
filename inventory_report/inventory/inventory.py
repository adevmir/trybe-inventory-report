from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory():
    @staticmethod
    def read(path):
        list_products = []
        with open(path, encoding="utf-8") as file:
            if "csv" in path:
                products_reader = csv.DictReader(file)
            if "json" in path:
                products_reader = json.load(file)
            for product in products_reader:
                list_products.append(product)
        return list_products

    @classmethod
    def import_data(cls, path, report_type):
        list_products = cls.read(path)
        if report_type == "simples":
            return SimpleReport.generate(list_products)
        else:
            return CompleteReport.generate(list_products)
