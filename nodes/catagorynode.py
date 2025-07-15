def general_node(state:dict)->dict:
  state["answer"]= f"{state['symptom']} : seems general: directing to general ward for consulting doctor"
  return state

def emergency_node(state:dict)->dict:
  state["answer"]= f"{state['symptom']} : seems emergency: directing to emergency ward for consulting doctor"
  return state

def mental_health_node(state:dict)->dict:
  state["answer"]= f"{state['symptom']} : seems mental: directing to mental health department for consulting doctor"
