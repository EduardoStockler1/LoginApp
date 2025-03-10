import tkinter as tk
from tkinter import messagebox
from auth import register_user, login_user
from database import setup_database

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")
        self.root.geometry("300x400")

        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Bem-vindo!", font=("Arial", 14)).pack(pady=10)
        
        tk.Button(self.root, text="Login", command=self.login_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Cadastrar", command=self.register_screen, width=20).pack(pady=5)

    def register_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Cadastro", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.root, text="Username:").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="Nome:").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()

        tk.Label(self.root, text="Email:").pack()
        email_entry = tk.Entry(self.root)
        email_entry.pack()

        tk.Label(self.root, text="Senha:").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        tk.Button(self.root, text="Cadastrar", command=lambda: self.handle_register(
            username_entry.get(), name_entry.get(), email_entry.get(), password_entry.get())).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.main_menu).pack()

    def handle_register(self, username, name, email, password):
        result = register_user(username, name, email, password)
        messagebox.showinfo("Resultado", result)

    def login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Login", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Email:").pack()
        email_entry = tk.Entry(self.root)
        email_entry.pack()

        tk.Label(self.root, text="Senha:").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        tk.Button(self.root, text="Entrar", command=lambda: self.handle_login(
            email_entry.get(), password_entry.get())).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.main_menu).pack()

    def handle_login(self, email, password):
        result = login_user(email, password)

        if result == "Login bem-sucedido!":
            messagebox.showinfo("Login", result)
        else:
            messagebox.showerror("Erro", result)

if __name__ == "__main__":
    setup_database() 
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
