from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".csv" not in path:
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as file:
                products_reader = csv.DictReader(file)
                list_products = []
                for product in products_reader:
                    list_products.append(product)
                return list_products
