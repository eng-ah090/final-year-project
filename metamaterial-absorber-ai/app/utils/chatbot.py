def simple_research_reply(query: str) -> str:
    query = query.strip()
    if not query:
        return "Please enter a question."
    return (
        "Research assistant note: focus on absorber bandwidth, polarization stability, and manufacturability. "
        f"You asked: '{query}'."
    )
