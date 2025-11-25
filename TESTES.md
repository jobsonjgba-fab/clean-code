# Implementado:  

| 1 | Cadastrar cliente  
:white_check_mark: tests/test_cliente.py::TestCliente::test_atributos_basicos  
:white_check_mark: tests/test_cliente.py::TestCliente::test_igualdade  
:white_check_mark: tests/test_cliente.py::TestCliente::test_igualdade_outro_tipo  
:white_check_mark: tests/test_system.py::TestSystem::test_adicionar_cliente  

| 2 | Remover cliente  
:white_check_mark: tests/test_system.py::TestSystem::test_remove_cliente_por_telefone  

| 3 | Consultar cliente  
:white_check_mark: tests/test_system.py::TestSystem::test_buscar_clientes  
:white_check_mark: tests/test_system.py::TestSystem::test_busca_sem_resultados  

| 4 | Criar novo pedido  

:white_check_mark: tests/test_pedido.py::TestPedido::test_attributes_and_item_management :white_check_mark: tests/test_pedido.py::TestPedido::test_valor_total_sem_itens  
:black_square_button: tests/test_system.py::TestSystem::test_adicionar_pedido  

| 5 | Inserir itens ao pedido  

:white_check_mark: tests/test_item_pedido.py::TestItemPedido::test_atributos_basicos  
:black_square_button: tests/test_pedido.py::TestPedido::test_preserva_ordem_itens  

| 8 | Adicionar opções ao cardápio  

:white_check_mark: tests/test_cardapio.py::TestCardapio::test_atributos_basicos  
:white_check_mark: tests/test_cardapio.py::TestCardapio::test_igualdade  
:white_check_mark: tests/test_cardapio.py::TestCardapio::test_igualdade_outro_tipo  
:white_check_mark: tests/test_system.py::TestSystem::test_adicionar_item_cardapio  


# A implementar:

## Sugestão de sequência

| 4 |, | 8 | primeiro  
| 5 |, | 6 | e | 9 | em seguida  
| 7 | e | 10 | e | 11 | por último  

## Restantes

| 5 | Inserir itens ao pedido (depende de | 4 | e | 8 |)  

:black_square_button: tests/test_item_pedido.py::TestItemPedido::test_valor_total  
:black_square_button: tests/test_item_pedido.py::TestItemPedido::test_valor_total_zero  
:black_square_button: tests/test_pedido.py::TestPedido::test_item_quantidade_nao_pode_ser_negativa  
:black_square_button: tests/test_pedido.py::TestPedido::test_item_quantidade_deve_ser_inteira  

| 6 | Atualizar situação do pedido (depdende de | 4 |)  

:black_square_button: tests/test_pedido.py::TestPedido::test_status_inicial_e_fluxo_avanco  
:black_square_button: tests/test_pedido.py::TestPedido::test_fechar_pedido_sem_itens  
:black_square_button: tests/test_pedido.py::TestPedido::test_modify_item_in_pedido  
:black_square_button: tests/test_pedido.py::TestPedido::test_modify_pedido_state  
:black_square_button: tests/test_system.py::TestSystem::test_fluxo_processamento_pedidos  
:black_square_button: tests/test_system.py::TestSystem::test_avancar_status_primeiro_pedido  
:black_square_button: tests/test_system.py::TestSystem::test_processar_proximo_pedido_fila_vazia  

| 7 | Listar pedidos em aberto (depende de | 4 | e | 6 |)  

:black_square_button: tests/test_system.py::TestSystem::test_listar_pedidos_abertos_mostra_status  

| 9 | Apresentar as opções do cardápio (depende de | 8 |)  

:black_square_button: tests/test_system.py::TestSystem::test_mostrar_cardapio_vazio  
:black_square_button: tests/test_system.py::TestSystem::test_mostrar_cardapio_com_itens  

| 10 | Cancelar pedido (depende de | 4 | e | 6 |)  

:black_square_button: tests/test_pedido.py::TestPedido::test_cancelar_pedido_define_motivo_e_fecha  
:black_square_button: tests/test_pedido.py::TestPedido::test_cancelar_pedido_entregue_dispara_erro  
:black_square_button: tests/test_pedido.py::TestPedido::test_cancelar_sem_motivo_dispara_erro  
:black_square_button: tests/test_system.py::TestSystem::test_cancelar_primeiro_pedido  

| 11 | Definir forma de pagamento (talvez dependa de | 4 | e | 6 |)  

:black_square_button: tests/test_pedido.py::TestPedido::test_definir_forma_pagamento_dinheiro  
:black_square_button: tests/test_pedido.py::TestPedido::test_definir_forma_pagamento_pix  
:black_square_button: tests/test_pedido.py::TestPedido::test_definir_forma_pagamento_cartao  
:black_square_button: tests/test_pedido.py::TestPedido::test_definir_forma_pagamento_invalida_gera_erro  
:black_square_button: tests/test_pedido.py::TestPedido::test_definir_pagamento_apos_conclusao_dispara_erro  
:black_square_button: tests/test_system.py::TestSystem::test_definir_forma_pagamento_primeiro_pedido  
