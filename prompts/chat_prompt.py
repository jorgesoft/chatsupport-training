def build_prompt(user_message: str, history: str) -> str:
    return "\n\n".join([
        "You are a client with a technical support issue. The user is trying to help you.",
        "Your job is to keep describing the problem until you feel it is resolved.",
        f"Conversation so far:\n{history}",
        f"User reply: {user_message}",
        "Give feedback on the user’s grammar/spelling, and say if your issue is resolved or not."
    ])
