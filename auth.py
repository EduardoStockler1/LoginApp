import sqlite3
import bcrypt
import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9._]+@[a-zA-Z]+[.]+[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))

def validate_password(password):
    return len(password) >= 6 and any(char.isdigit() for char in password)

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def check_password(password, hashed_password):
    if isinstance(hashed_password, str):  
        hashed_password = hashed_password.encode('utf-8')

    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# This line is outside any function scope, so it will raise an error.
# print(f"hashed_password type: {type(hashed_password)}") # Remove or move inside a function

def register_user(username, name, email, password):
    if not validate_email(email):
        return "Erro: Email inválido!"
    
    if not validate_password(password):
        return "Erro: Senha fraca! Mínimo de 6 caracteres e um número."

    hashed_password = hash_password(password)  
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO User (username, name, email, password) VALUES (?, ?, ?, ?)", 
                       (username, name, email, hashed_password))
        conn.commit()
        return "Usuário cadastrado com sucesso!"
    except sqlite3.IntegrityError:
        return "Erro: Email ou username já cadastrados!"
    finally:
        conn.close()

def login_user(email, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM User WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password(password, user[0]):
        return "Login bem-sucedido!"
    return "Erro: Email ou senha incorretos!"
