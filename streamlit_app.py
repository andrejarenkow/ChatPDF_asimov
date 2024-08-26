import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="ChatPDF clone",
    page_icon="🤖",
    #layout="wide",
    #initial_sidebar_state='collapsed'
) 

st.write('olá mundo')

def sidebar():
  uploaded_pdfs = st.file_uploader('Adicione seus arquivos pdf',
                   type=['.pdf'],
                   accept_multiple_files = True)

  if not uploaded_pdfs is None:
    pass
  
  pass

def main():
  with st.sidebar():
    sidebar()
  pass

if __name__ == 'main':
  main()
