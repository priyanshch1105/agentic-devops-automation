def cicd_agent(state: dict) -> dict:
    pipeline = """
name: Terraform Plan

on: [pull_request]

jobs:
  plan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
      - run: terraform init
      - run: terraform plan
"""
    return {
        **state,
        "cicd_pipeline": pipeline
    }
