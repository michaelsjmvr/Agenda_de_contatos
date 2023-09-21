# Projeto: Agenda de Contatos em Python com SQLite3 e PySide6

## Autor: Michael Douglas P Lima
## Contato: michaelsjmvr@hotmail.com
## LinkedIn: [michael-douglas-640a11180](https://www.linkedin.com/in/michael-douglas-640a11180/)

## Descrição do Projeto
Neste projeto, foi desenvolvida uma Agenda de Contatos em Python utilizando as bibliotecas SQLite3 e PySide6. A aplicação permite aos usuários adicionar, pesquisar e excluir contatos, armazenando as informações em um banco de dados SQLite3.

## Interface Gráfica
A interface gráfica foi construída com o PySide6, uma biblioteca para criação de aplicativos desktop em Python. Abaixo, estão os principais elementos da interface:

- **Janela Principal:** Exibe a lista de contatos, campos para adicionar novos contatos e uma área de pesquisa.

- **Campos de Entrada:** Dois campos de entrada de texto para nome e telefone dos contatos, com placeholders para orientar o usuário.

- **Botão "Adicionar":** Permite adicionar um novo contato à lista ao preencher os campos de nome e telefone e pressionar o botão.

- **Área de Pesquisa:** Permite filtrar os contatos à medida que o usuário digita o nome na pesquisa, atualizando em tempo real.

- **Lista de Contatos:** Utiliza um QListWidget para mostrar a lista de contatos, carregada do banco de dados SQLite3.

- **Botão "Deletar":** Permite ao usuário excluir o contato selecionado na lista.

## Banco de Dados SQLite3
Os contatos são armazenados em um banco de dados SQLite3 chamado "agenda.db". Eis os principais aspectos relacionados ao banco de dados:

- **Conexão com o Banco de Dados:** A aplicação estabelece uma conexão com o banco de dados SQLite3 usando a biblioteca sqlite3.

- **Tabela de Contatos:** A tabela "contatos" é criada no banco de dados, se não existir. Ela possui três colunas: "id" (chave primária), "nome" e "telefone".

- **Adicionar Contato:** Quando um novo contato é adicionado, os dados são inseridos na tabela de contatos usando uma instrução SQL preparada.

- **Filtrar Contatos:** A pesquisa de contatos é baseada no nome e é executada no banco de dados. A consulta SQL usa a cláusula LIKE para encontrar correspondências parciais, possibilitando a filtragem dos contatos conforme o usuário digita na pesquisa.

- **Deletar Contato:** A exclusão de um contato remove o registro correspondente da tabela de contatos usando uma instrução SQL preparada.

## Funcionalidades
A aplicação oferece as seguintes funcionalidades:

- **Adicionar Contato:** Os usuários podem adicionar um novo contato preenchendo os campos de nome e telefone e clicando no botão "Adicionar".

- **Pesquisar Contato:** A área de pesquisa permite que os usuários filtrem os contatos existentes à medida que digitam o nome desejado na pesquisa.

- **Deletar Contato:** Os usuários podem selecionar um contato na lista e clicar no botão "Deletar" para excluí-lo da lista de contatos e do banco de dados.

## Resumo
Este projeto exemplifica como criar uma aplicação desktop em Python para gerenciar uma lista de contatos, utilizando PySide6 para a interface gráfica e SQLite3 para o armazenamento de dados. A aplicação oferece uma solução simples para adicionar, pesquisar e excluir contatos, tornando-se uma ferramenta útil como uma agenda de contatos básica. Certifique-se de criar um arquivo de banco de dados chamado "agenda.db" no mesmo diretório em que o código é executado antes de utilizar a aplicação.

