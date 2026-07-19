from services.llm import ask_llm


def generate_outline(user_request: str):

    prompt = f"""
Create a professional document outline.

Request:
{user_request}

Return headings only.
"""

    return ask_llm(prompt)


def generate_content(user_request: str, outline: str):

    prompt = f"""
Create a professional business document.

User Request:
{user_request}

Outline:
{outline}

Write detailed content for every heading.
"""

    return ask_llm(prompt)