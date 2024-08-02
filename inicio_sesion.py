import hashlib

class UserManagementSystem:
    def __init__(self):
        self.users = {}

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def create_account(self, username, password, contact_info):
        if username in self.users:
            print("Error: El nombre de usuario ya existe.")
        else:
            hashed_password = self.hash_password(password)
            self.users[username] = {'password': hashed_password, 'contact_info': contact_info}
            print(f"Cuenta creada exitosamente para {username}.")

    def update_password(self, username, old_password, new_password):
        if username not in self.users:
            print("Error: Nombre de usuario no encontrado.")
        else:
            hashed_old_password = self.hash_password(old_password)
            if self.users[username]['password'] == hashed_old_password:
                self.users[username]['password'] = self.hash_password(new_password)
                print("Contraseña actualizada exitosamente.")
            else:
                print("Error: La contraseña actual no es correcta.")

    def display_user_info(self, username):
        if username not in self.users:
            print("Error: Nombre de usuario no encontrado.")
        else:
            print(f"Información del usuario {username}:")
            print(f" - Contacto: {self.users[username]['contact_info']}")

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
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
