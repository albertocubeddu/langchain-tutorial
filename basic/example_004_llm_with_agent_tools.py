""" example_004: How to input a basic prompt to the LLM using Tools and an agent """
import os

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

def llm_with_requests_tool(human_input):
    """ Function that takes a product name and generates a company name"""

    # LLM: Initialise the OpenAI agent
    llm = OpenAI(temperature=0.9, openai_api_key=os.getenv("OPENAI_API_KEY"))

    # Tools: Initialise the tools
    tools = load_tools(["requests_all"])

    # Agent: Initialise the agent with tools, llm & AgentType
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)

    # Run the agent with the human_input provided.
    output = agent.run(human_input)

    print(output)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    HUMAN_INPUT = "check how to get the date in a unix system?"
    # Call the main functionality that will use an LLM, tools
    # and an agent to combine everything and run.
    llm_with_requests_tool(HUMAN_INPUT)
