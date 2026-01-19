def planner_agent(user_input: str) -> dict:
    # LLM can be plugged here later
    return {
        "cloud": "aws",
        "environment": "staging",
        "services": ["vpc", "eks"],
        "region": "ap-south-1",
        "constraints": ["cost_optimized", "secure"]
    }
