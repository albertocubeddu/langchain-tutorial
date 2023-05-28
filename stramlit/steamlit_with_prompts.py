"""
Movie title to emoji
Using template to convert movie title to emoji and trying to stop prompt injection.
"""
import os

import streamlit as st
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI

def main():
    """ main function """
    st.title('Movie Title to Emoji')
    st.subheader('Convert any movie title in a nice set of emojis')

    generated_text = st.empty()
    generated_text.content = ""

    # Create an output box
    with st.form("my_form"):
        # Create a text area input box
        user_input = st.text_input(label="Insert a movie title:", max_chars=128)

        submitted = st.form_submit_button("Submit")
        if submitted:

            chat = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

            # Create the template for the SystemMessagePrompt
            template = "You are a helpful assistant that translates movie title to emoji."
            system_message_prompt = SystemMessagePromptTemplate.from_template(template)

            # Create the template for the HumanMessagePrompt
            template = "Convert this movie title: {movie_title} to emoji."
            human_message_prompt = HumanMessagePromptTemplate.from_template(template)

            # Create the template for the ChatPrompt (join system and human message)
            chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

            # Chat: Run the model using all the variables
            generated_text = chat(chat_prompt.format_prompt(movie_title=user_input).to_messages())



    # Display the generated text
    st.write("Generated text:", generated_text.content)


if __name__ == '__main__':
    main()
