import streamlit as st


def main():
    st.set_page_config(page_title="chat with pdfs",page_icon=":books:")
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about attached pdfs:")
    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your pdfs here and click on 'process'")
        st.button("Process")

if __name__=='__main__':
    main()