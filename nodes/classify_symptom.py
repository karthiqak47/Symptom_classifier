def classify_symptom(state:dict) -> dict:
  prompt =( f"""
      You are a medical triage assistant. Classify the given symptom into one of the following categories:

      - "General" — common, non-urgent physical issues like fever, cold, cough, headache.
      - "Emergency" — life-threatening symptoms like chest pain, severe bleeding, trouble breathing, loss of consciousness.
      - "Mental" — psychological symptoms like anxiety, panic attacks, depression, hallucinations.

      Respond with only the category: "General", "Emergency", or "Mental".

      Symptom: {state["symptom"]}

      """)
  response=llm.invoke([HumanMessage(content=prompt)])
  catagory=response.content.strip()
  state["catagory"]=catagory
  return state
