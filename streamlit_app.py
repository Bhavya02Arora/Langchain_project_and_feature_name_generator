# pip install streamlit

import streamlit as st
import langchain_helper
st.title("Project Names and Features List Generator")
project_field = st.sidebar.selectbox("Select CS department", ["ML", "AI", "NLP", "CV", "SWE", "DS", "DA", "DE", "DBA", "QA", "PM", "BA"])

if project_field:
	st.write(f"Selected CS department: {project_field}")

	# Input for project name
	response = langchain_helper.generated_project_name_and_features(project_field)
	# print the project name
	st.write("Generated Project Name:")
	st.write(response['project_name'].strip())
	st.write("Generated Features:")

	# Handle the features string safely
	features_raw = response['features_list']

	# If it's a string with bullet points or newlines, split it properly
	if isinstance(features_raw, str):
		features = [f.strip("-• \n") for f in features_raw.split("\n") if f.strip()]
	else:
		features = features_raw  # If already a list

	# Display each feature
	for feature in features:
		st.write(f"• {feature}")
