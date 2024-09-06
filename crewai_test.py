# import os
# from crewai import Agent, Task, Crew
# # from langchain.agents import AgentType, initialize_agent, load_tools
# # from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
# # from transformers import AutoModelForCausalLM, AutoTokenizer, pipelinef
# from langchain import HuggingFaceHub

# os.environ['HUGGINGFACEHUB_API_TOKEN'] = "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"

# llm = HuggingFaceHub(
#     repo_id="tiiuae/falcon-7b",
#     # model_kwargs={"temperature": 0.5, "max_length": 64,"max_new_tokens":512}
# )

# # os.environ["OPENAI_API_KEY"] = "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"
# # os.environ["OLLAMA_HOST"] = "127.0.0.1:50000"
# # You can choose to use a local model through Ollama for example.
# #
# # from langchain_community.llms import Ollama
# # ollama_llm = Ollama(model="mistral")


# # Install duckduckgo-search for this example:
# # !pip install -U duckduckgo-search

# from langchain_community.tools import DuckDuckGoSearchRun
# search_tool = DuckDuckGoSearchRun()

# # Install duckduckgo-search for this example:
# # !pip install -U duckduckgo-search

# # Define your agents with roles and goals
# researcher = Agent(
#   role='Senior Brand Analyst',
#   goal='Research Dat on leather products mainly wallets for Nayab Leather a brand that is new in the leather industry',
#   backstory="""As a newly-established brand, we strive to always offer our customers the best value. We carry a wide variety of wallets for men 
#   and women ranging in size, color, and style at a very affordable price. All of our products have been crafted by us with pride and attention 
#   to detail. You can purchase your own favorite style or original design of bag as well as giftware such as wallets at our website. Our 
#   leather wallets are unique, handmade, and genuine. With a plethora of colors, styles, and sizes, we’ve got something for everyone.""",
#   verbose=True,
#   allow_delegation=False,
#   tools=[search_tool],
#   llm=llm
#   # You can pass an optional llm attribute specifying what mode you wanna use.
#   # It can be a local model through Ollama / LM Studio or a remote
#   # model like OpenAI, Mistral, Antrophic of others (https://python.langchain.com/docs/integrations/llms/)
#   #
#   # Examples:
#   #llm=ollama_llm # was defined above in the file
#   # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7)
# )
# writer = Agent(
#   role='Brand Markting Content Writer',
#   goal='Craft compelling content for Nayab Leather',
#   backstory="""You are a renowned Content Strategist, known for your insightful and engaging posts. You transform complex concepts into 
#               compelling narratives.""",
#   verbose=True,
#   allow_delegation=True,
#   llm=llm
# )

# # Create tasks for your agents
# task1 = Task(
#   description="""Conduct a small analysis of the trends in the leather industry mainly wallets in Pakistan for Nayab Leather""",
#   agent=researcher
# )

# task2 = Task(
#   description="""Using the insights provided, develop an engaging linkedin
#   post that introduces Nayab Leather products to the industry and mainly market our products.""",
#   agent=writer
# )

# # Instantiate your crew with a sequential process
# crew = Crew(
#   agents=[researcher, writer],
#   tasks=[task1, task2],
#   verbose=2, # You can set it to 1 or 2 to different logging levels
# )

# # Get your crew to work!
# result = crew.kickoff()

# print("######################")
# print(result)

################################################################################################################################################

import os
from crewai import Agent, Task, Crew, Process
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = ""

gpt35 = ChatOpenAI(
  temperature=0.7,
  model_name="gpt-3.5-turbo",
)
# You can choose to use a local model through Ollama for example.
#
# from langchain.llms import Ollama
# ollama_llm = Ollama(model="openhermes")

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

# from langchain.tools import DuckDuckGoSearchRun
# search_tool = DuckDuckGoSearchRun()

# Define your agents with roles and goals

PROMPT = "Can you give me your best mithai"

researcher = Agent(
  role='FT sweets Research Analyst',
  goal='Research data on FT Sweets a sweet confectionist',
  backstory="""FT Description: Since 1920, FT Sweets has been a family-owned Sweets business dedicated to 
  preserving the rich traditions of Bombay Line Sweets called Mithai situated in Karachi, Pakistan. 
  Our Mithai (which are sweets) are made with love and using traditional recipes that have been passed down for generations.
  Brand Motive: At FT Mithai Mart, we take pride in delivering the finest and freshest mithai (sweets) to your doorstep.
  Make sure to remember the details below to answer user queries:
  Ft Sweets Shop timings: Monday to Saturday 9am - 9pm, Sunday: 9 am- 2 pm
  Ft Sweets provides Delivery: which is Only available on weekdays (Monday to Friday) 12pm - 6pm Only available in Defence, Clifton, Saddar and Nanakwara
  Address: Shop no.2, Hakimi Manzil, Wellington street, Surgical Market, Lucky Star, Saddar, Karachi, Pakistan
  If the user asks for a recommendation recommend a product from only these explicitly to the user with small and engaging description of the recommended product.
  Products:
  1 product name: Badam Pak Products desc: Experience the tradition of sweet craftsmanship with 'Badam Pak,' our one of the special halwas made from high-quality almonds, rich khoya (Which is made from milk), premium sugar, and expertise. This delightful treat offers a harmonious blend of nuttiness and creaminess, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 1600 per kg taste: If you like rich and crunchy almonds mixed with khoya (made from milk) and sugar, this sweet is for you.
  2 product name: Pista Pak Products desc: Experience the tradition of sweet craftsmanship with 'Pista Pak,' our one of the special halwas made from high-quality Pistachios, rich khoya (Which is made from milk), premium sugar, and expertise. This delightful treat offers a harmonious blend of nuttiness and creaminess, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 2000 per kg taste: If you like rich and crunchy pistachios mixed with khoya (made from milk) and sugar, this sweet is for you.
  3 product name: Kaju Pak Products desc: Experience the tradition of sweet craftsmanship with 'Kaju Pak,' our one of the special halwas made from high-quality cashews, rich khoya (Which is made from milk solids), premium sugar, and expertise. This delightful treat offers a harmonious blend of nuttiness and creaminess, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 1600 per kg taste: If you like rich and crunchy cashews mixed with khoya (made from milk) and sugar, this sweet is for you.
  4 product name: Akhrot Pak Products desc: Experience the tradition of sweet craftsmanship with 'Akhrot Pak,' our one of the special halwas made from high-quality Walnuts, rich khoya (Which is made from milk solids), premium sugar, and expertise. This delightful treat offers a harmonious blend of nuttiness and creaminess, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 1600 per kg taste: If you like rich and crunchy walnut mixed with khoya (made from milk solid) and sugar, this sweet is for you.
  5 product name: Khopra Pak Products desc: Experience the tradition of sweet craftsmanship with 'Khopra Pak,' our one of the special halwas made from high-quality coconut, rich khoya (Which is made from milk solids), premium sugar, and expertise. This delightful treat offers a harmonious blend of softness, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 1600 per kg taste: If you like rich and soft coconut mixed with khoya (made from milk) and sugar, this sweet is for you. Tastes like bounty chocolate
  6 product name: Pineapple Pak Products desc: Experience the tradition of sweet craftsmanship with 'Pineapple Pak,' our one of the special halwas made from high-quality Pineapple and coconut, rich khoya (Which is made from milk solids), premium sugar, and expertise. This delightful treat offers a harmonious blend of nuttiness and creaminess, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 1600 per kg taste: If you like rich and soft pineapple and coconut mixed with khoya (made from milk) and sugar, this sweet is for you.
  7 product name: Zafrani Paira Products desc: Savor the royal flavors of our special Zafrani Paira, crafted with pure khoya and the exquisite touch of saffron to produce the ultimate taste. category: Classic Sweets (Classic sweets" encompass a wide array of traditional confections enjoyed across various cultures and regions around the world. These sweets have stood the test of time, often passed down through generations,) price: 1400 per kg taste: If you like rich and soft khoya with a touch of saffron and sugar, this sweet is for you.
  8 product name: Gulaab Jaman Products desc: Indulge in the sweet nostalgia of our traditional recipe for “Gulaab Jamun”, these golden brown dumplings are made up of pure khoya, fried to perfection and lovingly dipped in fragrant sugar syrup. category: Classic Sweets (Classic sweets" encompass a wide array of traditional confections enjoyed across various cultures and regions around the world. These sweets have stood the test of time, often passed down through generations,) price: 1200 per kg taste: If you like rich and soft khoya balls dipped in sugar syrup, this sweet is for you.
  9 product name: Egg Maisoo Products desc: Discover the timeless charm of "Egg Maisoo," our famous traditional mithai made from pure eggs, quality oil, and a touch of sugar. Crunchy, succulent, and perfect for celebrations or sharing with loved ones. Experience a legacy of flavors in every bite. category: Classic Sweets (Classic sweets" encompass a wide array of traditional confections enjoyed across various cultures and regions around the world. These sweets have stood the test of time, often passed down through generations,) price: 1500 per kg taste: If you like rich and crunchy texture sweets made with eggs, this sweet is for you.
  10 product name: Malai Khaja Products desc: Experience the essence of tradition in every bite of our premium Malai Khaja that combines crispy layers with a rich, creamy center of Rabri (Made with milk and sugar). This sweet treat is a perfect blend of textures and flavors to fulfill your sweet cravings. category: Malai Khaja (Malai Khaja is a delectable and traditional Indian sweet originating from the eastern state of Odisha. It is known for its flaky layers, rich texture, and delightful taste.) price: 1400 per kg taste: if you like deep fried cripsy sweet with creamy filling, this sweet is for you.
  11 product name: Khoya Puff Products desc: Khoya Puff, also known as Khoya Mawa Puff or Khoya Patties, is a delicious and indulgent Indian sweet treat that features layers of flaky puff pastry filled with a rich and creamy khoya (milk solids) filling. category: Malai Khaja (Malai Khaja is a delectable and traditional Indian sweet originating from the eastern state of Odisha. It is known for its flaky layers, rich texture, and delightful taste.) price: 1100 per kg taste: if you like deep fried cripsy sweet with creamy filling, this sweet is for you.
  12 product name: Malai Khaja Products desc: Experience the essence of tradition in every bite of our premium Malai Khaja that combines crispy layers with a rich, creamy center of Rabri (Made with milk and sugar). This sweet treat is a perfect blend of textures and flavors to fulfill your sweet cravings. category: Malai Khaja (Malai Khaja is a delectable and traditional Indian sweet originating from the eastern state of Odisha. It is known for its flaky layers, rich texture, and delightful taste.) price: 1400 per kg taste: if you like deep fried cripsy sweet with creamy filling, this sweet is for you.
  13 product name: Verki Samosa Products desc: Khoya samosa, also known as verki samosa, is a unique and crispy variation of the traditional Indian samosa. Unlike the typical triangular-shaped samosa, verki samosa is prepared using thinly rolled layers of dough, similar to filo pastry, which are then filled with a savory mixture and folded into small parcels. category: Malai Khaja (Malai Khaja is a delectable and traditional Indian sweet originating from the eastern state of Odisha. It is known for its flaky layers, rich texture, and delightful taste.) price: 840 per kg taste: if you like deep fried cripsy sweet with creamy filling, this sweet is for you.
  14 product name: Barfi Products desc: Barfi, also known as burfi, is a popular Indian sweet delicacy that is enjoyed across various regions and festivities. It is characterized by its dense, fudge-like texture and its wide range of flavors, including traditional ones like plain, almond, pistachio, and coconut, as well as modern variations like chocolate and fruit-flavored barfis.. category: CLassic Sweets (Classic sweets encompass a wide array of traditional confections enjoyed across various cultures and regions around the world. These sweets have stood the test of time, often passed down through generations) price: 1300 per kg
  """,
  verbose=True,
  allow_delegation=False,
  # tools=[search_tool],
  # llm=ollama_llm # was defined above in the file
  llm=gpt35
)

# Define the Langchain agent for brand tone setting, customer service, and product recommendation
tone_setter = Agent(
    role='Brand Tone Setter',
    goal='Craft compelling and brand-specific content to enhance marketing strategies, provide excellent customer service, and recommend products to customers',
    backstory="""As a versatile customer service representative, and product recommender, you are renowned 
    for your ability to create engaging replies, resolve customer queries effectively, and recommend 
    products tailored to customer needs. Your expertise lies in understanding the brand's tone, 
    addressing customer concerns with empathy, and suggesting suitable products to enhance their experience.""",
    verbose=True,
    allow_delegation=True,
    llm=gpt35  # Assuming gpt35 is the language model you want to use
)


writer = Agent(
    role='Customer Service Representative',
    goal='Craft compelling and brand-specific content to enhance marketing strategies across diverse platforms',
    backstory="""As a versatile Content Strategist and writer, you are renowned for creating insightful and engaging marketing posts 
    tailored for various brands across multiple social media platforms. Your expertise lies in transforming complex concepts into compelling 
    narratives, ensuring maximum impact for each unique brand.""",
    verbose=True,
    allow_delegation=True,
    llm=gpt35
)


# Conduct a comprehensive analysis of FT sweets, brief description of the brand. Include its mission, values, Products and unique selling 
#   points. The Brands Target Audience. Identify key competitors in the industry and how the brand differentiates itself from them. Define the key messages or 
#   phrases associated with the brand. What does the brand want to communicate to its audience.Outline the brand's future goals and aspirations. 
#   Where does the brand envision itself in the coming years?

# Create tasks for your agents
task1 = Task(
  description="""Conduct comprehensive analysis of FT sweets,and convert the details in bullet points so that
  when a user asks queries data can be retrieved faster. Make Data connections and answer the users questions
  precisely.""",
  agent=researcher
)

task2 = Task(
    description="""The personality and tone associated with the brand is a friendly, professional, 
    and helpful since you want to converse with the user for our FT sweets users that may need
    help with knowing about our brand and our product details as well as other details of our brand. """,
    agent=tone_setter
)

task3 = Task(
    description="""Using the insights provided, Answer the user prompt precisely: i love eating khoya can you suggest sweets that have this, Make sure that your response is less than 200 words 
    and answers Your response should be a answer to the user query in a precide manner with just the 
    response as output.""",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher,tone_setter,writer],
  tasks=[task1, task2,task3],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)

#################################################################################################################################################

# import os
# from crewai import Agent, Task, Crew
# from langchain.agents import AgentType, initialize_agent, load_tools
# from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
# from transformers import AutoModelForCausalLM, AutoTokenizer, pipelinef
# from langchain_community.llms import HuggingFaceHub
# from langchain_community.llms import LlamaCpp

# from langchain.callbacks.manager import CallbackManager
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# os.environ['HUGGINGFACEHUB_API_TOKEN'] = "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"


# n_gpu_layers = 1  # Metal set to 1 is enough.
# n_batch = 512  # Should be between 1 and n_ctx, consider the amount of RAM of your Apple Silicon Chip.

# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# # Make sure the model path is correct for your system!
# llm = LlamaCpp(
#     # model_path="D:/crewai/llama-2-13b-chat.Q2_K.gguf",
#     model_path="D:/crewai/stablelm-zephyr-3b.Q3_K_L.gguf",
#     temperature=0.75,
#     top_p=1,
#     callback_manager=callback_manager,
#     verbose=True,  # Verbose is required to pass to the callback manager
# )

# print(llm.invoke("Develop an engaging linkedin post that introduces Nayab Leather products to the industry and mainly market our products. "))

# from langchain_community.llms import GPT4All

# gpt4all = GPT4All(
#     model="D:/crewai/llama-2-13b-chat.Q2_K.gguf",
#     max_tokens=2048,
# )

# print(gpt4all.invoke("Develop an engaging linkedin post that introduces Nayab Leather products to the industry and mainly market our products."))

# from langchain_community.tools import DuckDuckGoSearchRun
# search_tool = DuckDuckGoSearchRun()

#   # # # Install duckduckgo-search for this example:
#   # # # !pip install -U duckduckgo-search

#   # # # Define your agents with roles and goals
# researcher = Agent(
# role='Senior Brand Analyst',
# goal='Research Data on leather products mainly wallets for Nayab Leather a brand that is new in the leather industry',
# backstory="""As a newly-established brand, we strive to always offer our customers the best value. We carry a wide variety of wallets for men 
# and women ranging in size, color, and style at a very affordable price. All of our products have been crafted by us with pride and attention 
# to detail. You can purchase your own favorite style or original design of bag as well as giftware such as wallets at our website. Our 
# leather wallets are unique, handmade, and genuine. With a plethora of colors, styles, and sizes, we’ve got something for everyone.""",
# verbose=True,
# allow_delegation=False,
# tools=[search_tool],
# llm=llm
# # You can pass an optional llm attribute specifying what mode you wanna use.
# # It can be a local model through Ollama / LM Studio or a remote
# # model like OpenAI, Mistral, Antrophic of others (https://python.langchain.com/docs/integrations/llms/)
# #
# # Examples:
# #llm=ollama_llm # was defined above in the file
# # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7)
# )
# writer = Agent(
# role='Brand Markting Content Writer',
# goal='Craft compelling content for Nayab Leather',
# backstory="""You are a renowned Content Strategist, known for your insightful and engaging posts. You transform complex concepts into 
#             compelling narratives.""",
# verbose=True,
# allow_delegation=True,
# llm=llm
# )

# # Create tasks for your agents
# task1 = Task(
# description="""Conduct a small analysis of the trends in the leather industry mainly wallets in Pakistan for Nayab Leather""",
# agent=researcher
# )

# task2 = Task(
# description="""Using the insights provided, develop an engaging linkedin
# post that introduces Nayab Leather products to the industry and mainly market our products.""",
# agent=writer
# )

# # Instantiate your crew with a sequential process
# crew = Crew(
# agents=[researcher, writer],
# tasks=[task1, task2],
# verbose=2, # You can set it to 1 or 2 to different logging levels
# )

# # Get your crew to work!
# result = crew.kickoff()

# print("######################")
# print(result['output'])
