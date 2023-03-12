from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".json" not in path:
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as file:
                products_reader = json.load(file)
                return products_reader
