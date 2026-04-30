# Gerenciador de Biblioteca - Projeto RAD

Aplicação desktop para cadastro de livros e controle de retiradas. Desenvolvido em Python com foco em organização modular e persistência local.

## Funcionalidades:

* Cadastro de livros (título, autor, gênero).
* Registro de quem retirou o livro.
* Captura automática da data de registro via sistema.
* Interface gráfica com suporte a temas (Claro/Escuro).

## Tecnologias usadas e requisitos:

* **Python 3.x**
* **CustomTkinter** (Interface gráfica)
* **SQLite3** (Banco de dados nativo)
* Bibliotecas necessárias: `pip install customtkinter`

## Estrutura do projeto:

* `main.py`: Execução principal e interface do programa.
* `configuracoes.txt`: Arquivo de texto para definir o tema do programa e o nome do usuário.
* `modulo_dados/`: Funções de conexão e comandos SQL.
* `modulo_utils/`: Funções para leitura do arquivo de configuração.

## Como usar:

1. Configure suas preferências no arquivo `configuracoes.txt`.
2. Execute o comando `python main.py`.
3. O banco de dados `database.db` será criado assim que o programa rodar.

## Requisitos acadêmicos:

* Banco de dados SQLITE.
* Interface gráfica em Python.
* Modularização (pacotes e módulos).
* Manipulação de arquivos externos (.txt).
* Implementação de sub-rotinas para lógica de negócio.