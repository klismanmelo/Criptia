import streamlit as st


# Função de Criptografar
def pagina_cript():
    st.header('🤖 Criptografar', divider=True)



# Função de Descriptografar
def pagina_decript():
    st.header('🤖 Descriptografar', divider=True)



# Sidebar para navegação
def sidebar():
    # Usando st.radio para navegar entre as páginas
    pagina = st.selectbox('Escolha uma opção', ('Criptografar', 'Descriptografar'))
    if pagina == 'Criptografar':
        password = st.text_input('Password: ')
        if st.button('Criptografar'):
            print(f'Criptografar: {password}')

    if pagina == 'Descriptografar':
        file = st.file_uploader('Upload File')
        if st.button('Descriptografar'):
            print(f'Descriptografando o arquivo...')
            print("Feito")
    return pagina


def main():
    with st.sidebar:
        pagina = sidebar()

    if pagina == 'Criptografar':
        pagina_cript()  # Exibe a página de criptografia
    elif pagina == 'Descriptografar':
        pagina_decript()  # Exibe a página de descriptografia


if __name__ == '__main__':
    main()
