""" example_008: How to use the various output parsers """
import os

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser, DatetimeOutputParser


def comma_separated_list_output_parser():
    """Parse out using the CommaSeparatedListOutputParser."""
    # Use a default function that will output in Comma Separated List Output
    output_parser = CommaSeparatedListOutputParser()
    # Get the format instructions from the output parser, this is a simple prompt command that will give the LLM
    # instructions on how to format the output. 'Your response should be a list of comma separated values, eg: `foo,
    # bar, baz`'
    format_instructions = output_parser.get_format_instructions()

    # Using the PromptTemplate to feed the information.
    prompt = PromptTemplate(
        template="List five {subject}.\n{format_instructions}",
        input_variables=["subject"],
        partial_variables={"format_instructions": format_instructions}
    )

    _input = prompt.format(subject="programming languages?")
    output = chat(_input)

    final = output_parser.parse(output)
    print(final)


def datetime_output_parser():
    """Parse out using the CommaSeparatedListOutputParser. Warning: The parser produce
    hallucination when you give a question that is replied by a date. (2023-06-04)"""
    output_parser = DatetimeOutputParser()

    template = """Answer the users question:
    {question}
    {format_instructions}"""
    prompt = PromptTemplate.from_template(template,
                                          partial_variables={
                                              "format_instructions": output_parser.get_format_instructions()})

    # Ask a question that will be replied by a date
    _input = prompt.format(question="When was Elvis Presley born?")
    output = chat(_input)

    # Print the output directly from the LLM
    print(output)

    # Apply the parser and show an example!
    final = output_parser.parse(output)
    print(final)


if __name__ == '__main__':
    chat = OpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

    # Select the parser type to run the below examples
    PARSER_TYPE = "comma_separated_list_output_parser"

    if PARSER_TYPE == "comma_separated_list_output_parser":
        comma_separated_list_output_parser()
    elif PARSER_TYPE == "datetime_output_parser":
        datetime_output_parser()
    else:
        print("Type not found")
