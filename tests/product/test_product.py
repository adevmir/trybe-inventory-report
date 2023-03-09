from inventory_report.inventory.product import Product


def test_cria_produto():
    pass  # Seu teste deve ser escrito aqui

    id = 1
    nome_do_produto = "eclado Mecanico"
    nome_da_empresa = "Devmir_LTDA"
    data_de_fabricacao = "11/04/2022"
    data_de_validade = "11/04/2026"
    numero_de_serie = "758493"
    inst_de_armazenamento = "em local sem humidade"

    product_obj = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        inst_de_armazenamento,
    )

    assert product_obj.id == id
    assert product_obj.nome_do_produto == nome_do_produto
    assert product_obj.nome_da_empresa == nome_da_empresa
    assert product_obj.data_de_fabricacao == data_de_fabricacao
    assert product_obj.data_de_validade == data_de_validade
    assert product_obj.numero_de_serie == numero_de_serie
    assert product_obj.instrucoes_de_armazenamento == inst_de_armazenamento
