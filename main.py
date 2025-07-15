import os 
import getpass
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage


from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",
    google_api_key="    "
)

builder=StateGraph(dict)

builder.set_entry_point("get_symptom")
builder.add_node("get_symptom",get_symptom)
builder.add_node("classify",classify_symptom)
builder.add_node("router",symptom_router)
builder.add_node("general",general_node)
builder.add_node("emergency",emergency_node)
builder.add_node("mental_health",mental_health_node)

builder.add_edge("get_symptom","classify")
builder.add_conditional_edges("classify",symptom_router,{"general":"general","emergency":"emergency","mental_health":"mental_health"})
builder.add_edge("general",END)
builder.add_edge("emergency",END)
builder.add_edge("mental_health",END)

graph=builder.compile()
final_state=graph.invoke({})
print("Final State:")
print(final_state["answer"])
