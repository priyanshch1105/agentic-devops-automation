from executor.aws_session import assume_readonly_role

ROLE_ARN = "arn:aws:iam::<ACCOUNT_ID>:role/AgenticDevOpsReadOnly"

def audit_agent(state: dict) -> dict:
    session = assume_readonly_role(ROLE_ARN, state.get("region", "ap-south-1"))
    ec2 = session.client("ec2")

    instances = ec2.describe_instances()
    count = sum(len(r["Instances"]) for r in instances["Reservations"])

    return {
        **state,
        "audit": {
            "ec2_instance_count": count
        }
    }
