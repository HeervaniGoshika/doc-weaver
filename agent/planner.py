import json
from services.llm import ask_llm


def generate_plan(user_request: str):
    """
    Uses the LLM to generate a step-by-step execution plan.
    Falls back to a default plan if parsing fails.
    """

    
    prompt = f"""
You are an Autonomous AI Planning Agent.

Analyze the following request and generate a structured execution plan.

User Request:
{user_request}

Return ONLY valid JSON.

Format:

{{
    "goal":"Short goal",

    "assumptions":[
        "...",
        "..."
    ],

    "tasks":[
        "Analyze Request",
        "Identify Assumptions",
        "Create Proposal Outline",
        "Generate Proposal",
        "Review Proposal",
        "Generate DOCX"
    ]
}}

Rules

1. Return only JSON.

2. If assumptions are not needed return an empty list.

3. Tasks must describe execution steps, NOT document headings.
"""

    try:
        response = ask_llm(prompt)

        # Parse JSON
        plan = json.loads(response)

        return plan

    except Exception:
        pass

    # Fallback plan
    return {
    "goal": user_request,
    "assumptions": [],
    "tasks": [
        "Analyze Request",
        "Identify Assumptions",
        "Create Proposal Outline",
        "Generate Proposal",
        "Review Proposal",
        "Generate DOCX"
    ]
}