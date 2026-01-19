from collections import Counter

def summarize_plan(plan: dict) -> dict:
    counts = Counter()
    details = []

    for r in plan.get("resource_changes", []):
        actions = r["change"]["actions"]
        for a in actions:
            counts[a] += 1
        details.append({
            "type": r["type"],
            "name": r["name"],
            "actions": actions
        })

    return {
        "counts": dict(counts),
        "resources": details
    }
