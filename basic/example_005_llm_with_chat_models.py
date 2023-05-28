""" example_005: How to use Chat with HumanMessage, HumanMessage & SystemMessage and lastly a batch of messages """

import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

def chat_with_human_message():
    """ Function that interacts with the ChatOpenAI using a HumanMessage"""

    # Chat: Start the chat
    output = chat([HumanMessage(content="Translate this sentence from English to French. \
        I love programming.")])

    print(output)

def chat_with_human_system_message():
    """ Function that interacts with the ChatOpenAI using a Human Message + a System Message """

    messages = [
        SystemMessage(content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="I love programming.")
    ]

    output = chat(messages)

    print(output)

def chat_with_human_system_batch_messages():
    """ Function that interacts with the ChatOpenAI using a batch of messages"""
    batch_messages = [
        [
            SystemMessage(content="You are a helpful assistant that translates English to French."),
            HumanMessage(content="I love programming.")
        ],
        [
            SystemMessage(content="You are a helpful assistant that translates English to French."),
            HumanMessage(content="I love artificial intelligence.")
        ],
    ]
    output = chat.generate(batch_messages)

    print (output)


if __name__ == '__main__':
    # Print the product name
    TYPE_CHAT = "human_system_batch"

    # This variable because is defined in the outer scope will be accessible to all
    # function within the scope, e.g. chat_with_human_message
    chat = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))


    # match the type_chat with the different type, e.g. HumanMessage, ai, SystemMessage
    if TYPE_CHAT == "human":
        chat_with_human_message()
    elif TYPE_CHAT == "human_system":
        chat_with_human_system_message()
    elif TYPE_CHAT == "human_system_batch":
        chat_with_human_system_batch_messages()
    else:
        print("not supported")
