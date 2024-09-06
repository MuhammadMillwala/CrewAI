
import os
from crewai import Agent, Task, Crew
# from langchain.agents import AgentType, initialize_agent, load_tools
# from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
# from transformers import AutoModelForCausalLM, AutoTokenizer, pipelinef
from langchain_community.llms import HuggingFaceHub
from langchain_community.llms import LlamaCpp

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

os.environ['HUGGINGFACEHUB_API_TOKEN'] = ""

class BrandRepresentative:
    def __init__(self, brand_name, brand_personality, llm):
        self.brand_name = brand_name
        self.brand_personality = brand_personality
        self.llm = llm

    def communicate(self, message):
        # Simulate communication in the brand's voice
        communication = f"{self.brand_name}: {message}"
        return communication

# Define a generic brand personality
generic_brand_personality = {
    'tone': 'engaging',
    'style': 'versatile',
    'language': 'informative',
    'values': ['innovation', 'quality', 'customer-centric'],
    # Add any other relevant aspects of a generic brand personality
}

# Instantiate the Brand Representative for any brand
brand_representative = BrandRepresentative(brand_name='AnyBrand', brand_personality=generic_brand_personality, llm=llm)

# Create the agents
researcher = Agent(
    role='Senior Brand Analyst',
    goal='Research Data on leather products mainly wallets for AnyBrand in the leather industry',
    backstory="""As a leading brand in the leather industry, we strive to offer our customers the best value. 
                  Our wide variety of wallets for men and women are crafted with pride and attention to detail. 
                  Explore our unique, handmade, and genuine leather wallets available in various colors, styles, and sizes.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

writer = Agent(
    role='Brand Marketing Content Writer',
    goal='Craft compelling content for AnyBrand',
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging posts. You transform complex concepts into 
                compelling narratives.""",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

# Create tasks for your agents
task1 = Task(
    description="""Conduct a small analysis of the trends in the leather industry mainly wallets for AnyBrand""",
    agent=researcher
)

task2 = Task(
    description="""Using the insights provided, develop an engaging LinkedIn post that introduces AnyBrand products to the industry and mainly market our products.""",
    agent=writer
)

# Intermediate task for the Brand Representative to convey insights
intermediate_task = Task(
    description="Communicate research insights to the Content Writer",
    agent=brand_representative
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[brand_representative, researcher, writer],
    tasks=[intermediate_task, task1, task2],
    verbose=2  # You can set it to 1 or 2 for different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result['output'])
