""" example_006: How to use Chat prompt templates """
import os

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)


def convert_input_language_to_output_language(input_lanuage, output_language, text_to_convert):
    """ Function that interacts with the ChatOpenAI using a prompt
    combining (Human Message + System Message) """

    # Create the template for the SystemMessagePrompt
    template = "You are a helpful assistant that translates {input_language} to {output_language}."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    # Create the template for the HumanMessagePrompt
    template = "{text_to_convert}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(template)

    # Create the template for the ChatPrompt (join system and human message)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    # Chat: Run the model using all the variables
    output = chat(chat_prompt.format_prompt(input_language=input_lanuage,
                                            output_language=output_language,
                                            text_to_convert=text_to_convert).to_messages())

    print(output)


def convert_input_language_to_output_language_with_llm(input_lanuage, output_language, text_to_convert):
    """ Function that interacts with the ChatOpenAI using a prompt combining (Human Message + System Message) """

    # Create the template for the SystemMessagePrompt
    template = "You are a helpful assistant that translates {input_language} to {output_language}."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    # Create the template for the HumanMessagePrompt
    template = "{text_to_convert}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(template)

    # Create the template for the ChatPrompt (join system and human message)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    # initialise the LLMChain using llm=chat and prompt=chat_prompt
    chain = LLMChain(llm=chat, prompt=chat_prompt)
    output = chain.run(input_language=input_lanuage, output_language=output_language, text_to_convert=text_to_convert)

    print(output)


if __name__ == '__main__':
    # Print the product name
    CHAT_TYPE = "direct-prompt-llm"

    chat = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

    if CHAT_TYPE == "direct-prompt-template":
        convert_input_language_to_output_language(input_lanuage="English", output_language="French", text_to_convert="No pineapple on pizza!")
    elif CHAT_TYPE == "direct-prompt-llm":
        convert_input_language_to_output_language_with_llm(input_lanuage="English", output_language="Italian", text_to_convert="No pineapple on pizza!")
    else:
        print("Type not found")
