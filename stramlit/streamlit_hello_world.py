"""
# My first app
Here's our first attempt at using data to create a table:
"""
import os

import streamlit as st
from langchain.llms import OpenAI


def main():
    st.title('Write an email')
    st.subheader('Personalised for photography studios')

    generated_text = ""
    # Create an output box
    with st.form("my_form"):
        # Create a text area input box
        user_input = st.text_area("Enter your input here:")

        submitted = st.form_submit_button("Submit")
        if submitted:
            llm = OpenAI(temperature=0.9, openai_api_key=os.getenv("OPENAI_API_KEY"))
            generated_text = llm(user_input)

    # Display the generated text
    st.write("Generated text:", generated_text)


if __name__ == '__main__':
    main()
