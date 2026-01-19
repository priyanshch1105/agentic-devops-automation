from executor.aws_session import assume_readonly_role
from datetime import date, timedelta

ROLE_ARN = "arn:aws:iam::<ACCOUNT_ID>:role/AgenticDevOpsReadOnly"

def cost_audit_agent(state: dict) -> dict:
    session = assume_readonly_role(ROLE_ARN)
    ce = session.client("ce")

    end = date.today()
    start = end - timedelta(days=30)

    cost = ce.get_cost_and_usage(
        TimePeriod={"Start": start.isoformat(), "End": end.isoformat()},
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )

    amount = cost["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]

    return {
        **state,
        "cost_audit": {
            "last_30_days_usd": float(amount)
        }
    }
