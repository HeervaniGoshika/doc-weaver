from fastapi import FastAPI, HTTPException

from schemas import AgentRequest, AgentResponse

from agent.planner import generate_plan
from agent.executor import execute_plan

app = FastAPI(
    title="Autonomous AI Agent",
    description="Simple AI Agent with Planning, Execution, Reflection and DOCX Generation",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Autonomous AI Agent is running"
    }

@app.post("/agent", response_model=AgentResponse)
def run_agent(request: AgentRequest):

    try:
        
        #step 1 generate execution plan
        plan = generate_plan(request.request)

        #step 2 execute plan
        result = execute_plan(
            user_request=request.request,
            plan=plan["tasks"]
        )

        return AgentResponse(
            status="success",
            goal=plan["goal"],
            assumptions=plan["assumptions"],
            plan=plan["tasks"],
            document=result["document"],
            message=result["message"]
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )