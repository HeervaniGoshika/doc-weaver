from services.llm import ask_llm


def review_document(content: str):
    """
    Reflection step.
    Reviews the generated content and improves it if needed.
    """

    prompt = f"""
You are an AI reviewer.

Review the following document.

Check for:

- Missing sections
- Grammar
- Professional tone
- Clarity
- Completeness

If improvements are needed,
rewrite the document.

Otherwise return the original document.

Document:

{content}
"""

    reviewed = ask_llm(prompt)

    return reviewed