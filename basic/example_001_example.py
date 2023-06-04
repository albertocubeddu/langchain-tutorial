""" example_001_example.py: How to initiate a basic conversation with langchain and the LLM """
import os

from langchain.llms import OpenAI


def hello_world_lang_chain():
    """ Function to ensure your environment is set up correctly
    Remember to set up your OPENAI_API_KEY in your environmnet variables
    or in a .env file in the root of your project"""

    llm = OpenAI(temperature=0.9, openai_api_key=os.getenv("OPENAI_API_KEY"))
    text = "What would be a good company name for a company `" \
           "that want to write tutorial for langchain?"

    output = llm(text)

    print(output)


if __name__ == '__main__':
    hello_world_lang_chain()
