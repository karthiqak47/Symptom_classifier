def symptom_router(state:dict)->dict:
   cat=state["catagory"].lower()
   if "general" in cat:
     return "general"
   elif "emergency" in cat:
      return "emergency"
   elif "mental" in cat:
      return "mental_health"
   else:
      return "general"
