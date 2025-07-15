# Symptom_classifier
This project implements a simple medical symptom classifier using LangGraph, a state machine framework for managing conversational flows with LLMs.
The chatbot interacts with users to:

Collect a symptom description.

Classify the symptom as one of:

General (e.g., fever, cold)

Emergency (e.g., chest pain, difficulty breathing)

Mental Health (e.g., anxiety, depression)

Route the conversation based on the classification and respond appropriately.

The core logic is implemented as a state graph:

get_symptom: Collects the symptom from the user.

classify: Uses an LLM to classify the symptom.

symptom_router: Determines which path to follow (general, emergency, or mental health).

Final nodes respond with basic advice or guidance and terminate the flow.
