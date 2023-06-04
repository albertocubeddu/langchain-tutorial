""" example_008: How to use Chat prompt templates with examples """
import os

from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, FewShotPromptTemplate


def reply_first_letter(input_string):
    """ Function that interacts with the ChatOpenAI using a FewShotPromptTemplate """

    # Put all your example here to train the model
    examples = [
        {"text": "Hello", "output": "H"},
        {"text": "Goodbye", "output": "G"},
        {"text": "How are you?", "output": "H a y"},
        {"text": "I am fine", "output": "I a f"},
        {"text": "What is your name?", "output": "W i y n"},
        {"text": "My name is John", "output": "M n i J"},
        {"text": "What is your favourite Colour?", "output": "W i y f C"},
        {"text": "My favourite Colour is Blue", "output": "M f C i B"},
        # {"text": "My Name Is Roberto usai", "output": "M N I R u"},
    ]

    example_formatter_template = """{text} -> {output}"""

    example_prompt = PromptTemplate(
        template=example_formatter_template,
        input_variables=["text", "output"],
    )

    # Finally, we create the `FewShotPromptTemplate` object.
    few_shot_prompt = FewShotPromptTemplate(
        # These are the examples we want to insert into the prompt.
        examples=examples,
        # This is how we want to format the examples when we insert them into the prompt.
        example_prompt=example_prompt,
        # The prefix is some text that goes before the examples in the prompt.
        # Usually, this consists of intructions.
        prefix="Give the first letter of every word given in the Input:\n",
        # The suffix is some text that goes after the examples in the prompt.
        # Usually, this is where the user input will go
        suffix="Input: {input}\n Letters: ",
        # The input variables are the variables that the overall prompt expects.
        input_variables=["input"],
        # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
        example_separator="\n",
    )

    print(few_shot_prompt.format(input="test phrase"))

    # At the time of commit, you need to uncomment the example:
    # {"text": "My Name Is Roberto usai", "output": "M N I R u"},
    # to let the agent understand that needs to use lowercase for surname too!
    # Output with the line commented: "M N I A C"
    # Output with the line uncommented: "M N I A c"
    # Or you can improve the prefix,
    output = chat(few_shot_prompt.format_prompt(input=input_string).to_messages())
    print(output)


if __name__ == '__main__':
    chat = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

    # Reply only with the first letter of each word
    reply_first_letter(input_string="My Name Is Alberto cubeddu")
