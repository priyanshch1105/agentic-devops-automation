# devops_agents/orchestrator.py
from devops_agents.planner_agent import planner_agent
from devops_agents.iac_agent import iac_agent
from devops_agents.verifier_agent import verifier_agent

def run_orchestrator(prompt: str):
    state = {"prompt": prompt}
    state = planner_agent(state)
    state = iac_agent(state)
    state = verifier_agent(state)
    return state
