""" Streamlit read from a CSV and talk with it """
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import pandas as pd
import streamlit as st

def main():
    """ Main function """
    st.set_page_config(page_title="Chat with your CSV")
    st.header("Upload and interact with your CSV")

    st.info("Upload the file streamlit_read_csv.csv and ask question like:  \n"
            "How many time Alberto is showing on the dataset?  \n"
            "What's Alberto's maximum score? \n")


    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:
        data_frame = pd.read_csv(csv_file.name)
        st.dataframe(data_frame, use_container_width=True)

        agent = create_csv_agent(
            OpenAI(temperature=0), csv_file, verbose=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()
