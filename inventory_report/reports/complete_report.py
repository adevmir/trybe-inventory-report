from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def generate(list) -> str:
        simple_report = SimpleReport.generate(list)
        products_dict = {}
        for product in list:
            company = product['nome_da_empresa']
            products_dict[company] = products_dict.get(company, 0) + 1
        products_string = ""
        for company, quant in products_dict.items():
            products_string += f"- {company}: {quant}\n"
        return (f"{simple_report}\n"
                f"Produtos estocados por empresa:\n"
                f"{products_string}")
