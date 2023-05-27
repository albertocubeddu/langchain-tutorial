""" example_003: How to input a basic prompt to the LLM using an LLMChain """

import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def company_name_creator(input_product_name):
    """ Function that takes a product name and generates a company name"""

    # LLM: Initialise the OpenAI agent
    llm = OpenAI(temperature=0.9, openai_api_key=os.getenv("OPENAI_API_KEY"))

    # Prompt: Use a template, where the input variable can be changed from a user input
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What would be a good company name for a company that makes {product}?",
    )

    # Chain: Use the LLM combined with the Prompt
    chain = LLMChain(llm=llm, prompt=prompt)
    # Run the chain
    output = chain.run(input_product_name)

    print(output)

if __name__ == '__main__':
    # Change the product name to test other input parameters
    PRODUCT_NAME = "programming languages specifically for cats"

    # Print the product name
    company_name_creator(PRODUCT_NAME)
