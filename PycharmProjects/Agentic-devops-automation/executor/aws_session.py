import boto3

def assume_readonly_role(role_arn: str, region: str = "ap-south-1"):
    sts = boto3.client("sts", region_name=region)
    creds = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName="agentic-devops-ro"
    )["Credentials"]

    return boto3.Session(
        aws_access_key_id=creds["AccessKeyId"],
        aws_secret_access_key=creds["SecretAccessKey"],
        aws_session_token=creds["SessionToken"],
        region_name=region
    )
