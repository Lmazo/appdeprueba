import streamlit as st

def main():
    st.title("Gestión de Usuarios")
    
    menu = ["Crear cuenta", "Actualizar contraseña", "Mostrar información de contacto"]
    choice = st.sidebar.selectbox("Selecciona una opción", menu)
    
    if choice == "Crear cuenta":
        st.subheader("Crear cuenta")
        username = st.text_input("Nombre de usuario")
        password = st.text_input("Contraseña", type="password")
        contact_info = st.text_input("Información de contacto")
        if st.button("Crear cuenta"):
            create_account(username, password, contact_info)
    
    elif choice == "Actualizar contraseña":
        st.subheader("Actualizar contraseña")
        username = st.text_input("Nombre de usuario")
        old_password = st.text_input("Contraseña actual", type="password")
        new_password = st.text_input("Nueva contraseña", type="password")
        if st.button("Actualizar contraseña"):
            update_password(username, old_password, new_password)
    
    elif choice == "Mostrar información de contacto":
        st.subheader("Mostrar información de contacto")
        username = st.text_input("Nombre de usuario")
        if st.button("Mostrar información"):
            display_user_info(username)

if __name__ == "__main__":
    main()
