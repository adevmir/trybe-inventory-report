from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def generate(list):
        simple_report = SimpleReport.generate(list)
        list_simple_report = simple_report.split(":")
        length = len(list_simple_report)
        company = str(list_simple_report[length-1]).strip()
        products_in_stock = [product["nome_do_produto"] for product in list
                             if product["nome_da_empresa"] == company]
        products_dict = {}
        for product in products_in_stock:
            quant = products_in_stock.count(product)
            products_dict[product] = quant
        products_string = ""
        for product, quant in products_dict.items():
            products_string += f"- {product}: {quant}\n"
        return (f"{simple_report}\n"
                f"Produtos estocados por empresa:\n"
                f"- {company}: {len(products_in_stock)}\n"
                f"{products_string}")
