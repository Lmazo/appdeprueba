import sqlite3
import hashlib

class UserManagementSystem:
    def __init__(self, db_name="users.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                contact_info TEXT NOT NULL
            )
            """)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def create_account(self, username, password, contact_info):
        hashed_password = self.hash_password(password)
        try:
            with self.conn:
                self.conn.execute("INSERT INTO users (username, password, contact_info) VALUES (?, ?, ?)",
                                  (username, hashed_password, contact_info))
            print(f"Cuenta creada exitosamente para {username}.")
        except sqlite3.IntegrityError:
            print("Error: El nombre de usuario ya existe.")

    def update_password(self, username, old_password, new_password):
        hashed_old_password = self.hash_password(old_password)
        hashed_new_password = self.hash_password(new_password)
        cursor = self.conn.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result is None:
            print("Error: Nombre de usuario no encontrado.")
        elif result[0] == hashed_old_password:
            with self.conn:
                self.conn.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_new_password, username))
            print("Contraseña actualizada exitosamente.")
        else:
            print("Error: La contraseña actual no es correcta.")

    def display_user_info(self, username):
        cursor = self.conn.execute("SELECT contact_info FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result is None:
            print("Error: Nombre de usuario no encontrado.")
        else:
            print(f"Información del usuario {username}:")
            print(f" - Contacto: {result[0]}")

    def close(self):
        self.conn.close()

def main():
    system = UserManagementSystem()

    while True:
        print("\n1. Crear cuenta")
        print("\n2. Actualizar contraseña")
        print("\n3. Mostrar información de contacto")
        print("\n4. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            contact_info = input("Información de contacto: ")
            system.create_account(username, password, contact_info)
        elif choice == '2':
            username = input("Nombre de usuario: ")
            old_password = input("Contraseña actual: ")
            new_password = input("Nueva contraseña: ")
            system.update_password(username, old_password, new_password)
        elif choice == '3':
            username = input("Nombre de usuario: ")
            system.display_user_info(username)
        elif choice == '4':
            system.close()
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
