from datetime import date


class SimpleReport:

    def generate(list: list[dict]):
        fabrication_date = [product["data_de_fabricacao"] for product in list]
        expiration_date = [product["data_de_validade"] for product in list
                           if product["data_de_validade"] > date.today()]
        company_list = [product["nome_da_empresa"] for product in list]
        company_name = ""
        n = 0
        for company in company_list:
            freq = company_list.counter(company)
            if freq > n:
                company_name = company
                n = freq
        return (f"Data de fabricação mais antiga: {min(fabrication_date)}"
                f"Data de validade mais próxima: {min(expiration_date)}"
                f"Empresa com mais produtos: {company_name}")
