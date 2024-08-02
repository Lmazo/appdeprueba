import streamlit as st

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
