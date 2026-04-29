import customtkinter as ctk
from modulo_utils.config_helper import carregar_config
from modulo_dados.banco import criar_tabela, salvar_livro, buscar_livros

class AppBiblioteca(ctk.CTk):
    def __init__(self):
        super().__init__()

        config = carregar_config()
        ctk.set_appearance_mode(config.get("tema", "dark"))
        
        self.title(f"Biblioteca de {config.get('usuario', 'João')}")
        self.geometry("700x450")

        self.grid_columnconfigure(1, weight=1)
        
        self.frame_cad = ctk.CTkFrame(self, width=250)
        self.frame_cad.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_cad, text="Cadastrar Livro", font=("Arial", 16, "bold")).pack(pady=10)
        
        self.ent_titulo = ctk.CTkEntry(self.frame_cad, placeholder_text="Título")
        self.ent_titulo.pack(pady=5, padx=10, fill="x")
        
        self.ent_autor = ctk.CTkEntry(self.frame_cad, placeholder_text="Autor")
        self.ent_autor.pack(pady=5, padx=10, fill="x")
        
        self.cb_nome = ctk.CTkEntry(self.frame_cad, placeholder_text="Nome")
        self.cb_nome.pack(pady=5, padx=10, fill="x")
        
        self.end_data = ctk.CTkEntry(self.frame_cad, placeholder_text="Data (ex: 27/04/2026")
        self.end_data.pack(pady=5, padx=10, fill="x")
        
        self.cb_genero = ctk.CTkComboBox(self.frame_cad, values=["Tecnologia", "Programação", "I.A", "Ficção Científica", "Fantasia", "Suspense", "Romance", "História", "Biografia", "Gastronomia", "Auto-Ajuda", "Outros"])
        self.cb_genero.pack(pady=5, padx=10, fill="x")

        self.btn_add = ctk.CTkButton(self.frame_cad, text="Salvar", command=self.registrar)
        self.btn_add.pack(pady=20, padx=10)

        self.txt_lista = ctk.CTkTextbox(self)
        self.txt_lista.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.atualizar_view()

    def registrar(self):
        t = self.ent_titulo.get()
        a = self.ent_autor.get()
        g = self.cb_genero.get()
        n = self.cb_nome.get()
        d = self.end_data.get()
        if t and a:
            salvar_livro(t, a, g, n, d)
            self.atualizar_view()
            self.ent_titulo.delete(0, 'end')
            self.ent_autor.delete(0, 'end')
            self.end_data.delete(0, 'end')

    def atualizar_view(self):
        self.txt_lista.delete("0.0", "end")
        for item in buscar_livros():
            self.txt_lista.insert("end", f"Data: {item[5]} | {item[1]} ({item[2]}) - Ref: {item[3]} | Por: {item[4]}\n")
            
if __name__ == "__main__":
    criar_tabela()
    app = AppBiblioteca()
    app.mainloop()