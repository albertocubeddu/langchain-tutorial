import os

from langchain.llms import OpenAI

def print_hi():
    """ Function to ensure your environment is setup correctly
    Remember to setup your OPENAI_API_KEY in your environmnet variables
    or in a .env file in the root of your project"""

    llm = OpenAI(temperature=0.9, openai_api_key=os.getenv("OPENAI_API_KEY"))
    text = "What would be a good company name for a company that makes colorful socks?"
    print(llm(text))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
