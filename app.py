import streamlit as st
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title="chat with pdfs",page_icon=":books:")
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about attached pdfs:")
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your pdfs here and click on 'process'",accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
            #get pdf text


            #get the text chunks


            #create vector storage

if __name__=='__main__':
    main()