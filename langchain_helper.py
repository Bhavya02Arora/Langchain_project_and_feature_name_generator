import os
from langchain_openai import OpenAI
from secret_file import openapi_key
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain

os.environ['OPENAI_API_KEY'] = openapi_key

def generated_project_name_and_features(project_field):
	llm = OpenAI(temperature=0.6)

	# prompt template
	prompt_template_name = PromptTemplate(
		input_variables=["project_field"],
		template="I want you to suggest name of my application for {project_field} project"
	)


	name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="project_name")


	prompt_template_features = PromptTemplate(
		input_variables=["project_name"],
		template="I want you to suggest features for my application {project_name}"
	)

	projectFeatures_chain = LLMChain(llm=llm, prompt=prompt_template_features, output_key="features_list")

	chain = SequentialChain(
		chains=[name_chain, projectFeatures_chain],
		input_variables=['project_field'],
		output_variables=['project_name', 'features_list'])

	response = chain.invoke({'project_field': project_field})
	print(response)
	return response