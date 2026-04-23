def carregar_config():
    configuracoes = {}
    try:
        with open("configuracoes.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if "=" in linha:
                    chave, valor = linha.strip().split("=")
                    configuracoes[chave] = valor
    except FileNotFoundError:
        configuracoes = {"tema": "dark", "usuario": "Usuario"}
    
    return configuracoes