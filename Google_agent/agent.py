from google.adk.agents.llm_agent import Agent
import google_search

root_agent = Agent(
    model='gemini-3.5-flash',
    name='Google_Agent',
    description='A helpful assistant that can search the web',
    instruction='Answer user questions accurately "use google search when you need current information ""or  need to verify the facts"',
    tools=[google_search]
)
