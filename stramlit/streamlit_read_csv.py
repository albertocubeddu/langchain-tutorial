from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import os
import streamlit as st


def main():
    st.set_page_config(page_title="Chat with your CSV")
    st.header("Upload and interact with your CSV")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:

        agent = create_csv_agent(
            OpenAI(temperature=0), csv_file, verbose=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()