import streamlit as st
import os
import tempfile
import crip
import decript

from keys import save_keys_to_file

# Sidebar para navegação
def pagination():
    # Usando st.radio para navegar entre as páginas
    pagina = st.selectbox('Escolha uma opção', ('Criptografar', 'Descriptografar'))
    if pagina == 'Criptografar':
        st.header('🤖 Criptografar', divider=True)
        message_input = st.text_input('Message: ')
        password = st.text_input('Passowrd: ')
        if message_input and password:
            if st.button('Criptografar'):
                if not os.path.exists('keys.bin'):
                    save_keys_to_file(password)
                message = message_input.encode('utf-8')
                crip.criptography(message)

    if pagina == 'Descriptografar':
        st.header('🤖 Descriptografar', divider=True)
        file = st.file_uploader('Ainda em teste')
        if st.button('Descriptografar'):
            data_descripted = decript.decrypt()

            st.text(data_descripted)
    return pagina


def main():
    pagination()


if __name__ == '__main__':
    main()
