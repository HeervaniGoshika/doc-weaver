from agent.tools import generate_outline
from agent.tools import generate_content

from agent.reflector import review_document

from services.document_generator import create_docx


def execute_plan(user_request, plan):

    outline = ""
    content = ""

    print("\nExecution Started\n")

    for task in plan:

        print(f"Running: {task}")

        lower = task.lower()

        if "outline" in lower:

            outline = generate_outline(user_request)

        elif (
            "content" in lower
            or "proposal" in lower
            or "document" in lower
            or "report" in lower
        ):

            if not outline:
                outline = generate_outline(user_request)

            content = generate_content(
                user_request,
                outline
            )

        elif (
            "review" in lower
            or "check" in lower
        ):

            if content:
                content = review_document(content)

    if not content:

        outline = generate_outline(user_request)

        content = generate_content(
            user_request,
            outline
        )

        content = review_document(content)

    file_path = create_docx(content)

    return {
        "message": "Document generated successfully.",
        "document": file_path
    }