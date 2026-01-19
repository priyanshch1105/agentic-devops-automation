import argparse
from devops_agents.orchestrator import run_orchestrator
from executor.approval_store import update_status
from devops_agents.apply_agent import apply_agent


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd")

    g = sub.add_parser("generate")
    g.add_argument("prompt")

    a = sub.add_parser("approve")
    a.add_argument("plan_id")

    r = sub.add_parser("reject")
    r.add_argument("plan_id")

    r = sub.add_parser("apply")
    r.add_argument("plan_id")
    r.add_argument("tf_dir", nargs="?", default="infra/runtime")

    args = p.parse_args()

    if args.cmd == "generate":
        res = run_orchestrator(args.prompt)
        print(res)

    elif args.cmd == "approve":
        update_status(args.plan_id, "APPROVED")
        print("Approved:", args.plan_id)

    elif args.cmd == "reject":
        update_status(args.plan_id, "REJECTED")
        print("Rejected:", args.plan_id)

    # add subcommand
    elif args.cmd == "apply":
        result = apply_agent(args.plan_id, args.tf_dir)
        print(result)


if __name__ == "__main__":
    main()
