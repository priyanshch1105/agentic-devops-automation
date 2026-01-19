# Agentic DevOps / Cloud Automation Assistant

An **agentic, safe-by-default DevOps assistant** that converts natural language into Terraform plans, runs them in a Docker sandbox, enforces OPA policies, audits AWS (read-only), estimates costs, and generates CI/CD pipelines — **without ever applying infrastructure automatically**.

---

## ✨ Features

* Natural Language → Terraform (AWS)
* Docker-based Terraform sandbox (`plan` only)
* AWS AssumeRole (read-only, no static keys)
* OPA policy enforcement on Terraform plans
* Cloud cost audit (AWS Cost Explorer)
* CI/CD pipeline generator (GitHub Actions)
* CLI + FastAPI API
* LangGraph-based agent orchestration
* Human-in-the-loop approval model

---

## 🔐 Safety Guarantees (Non-Negotiable)

* ❌ No `terraform apply`
* ❌ No host execution of Terraform
* ❌ No static AWS credentials
* ✅ Docker isolation
* ✅ Read-only IAM role
* ✅ Policy-as-code (OPA)
* ✅ Manual approval before prod

---

## 🏗️ Architecture

```
User (CLI / API)
      ↓
FastAPI
      ↓
LangGraph Orchestrator
      ↓
Planner → IaC → Terraform Plan (Docker)
      ↓
OPA Policy Check
      ↓
AWS Audit + Cost Agent
      ↓
CI/CD Generator
      ↓
Human Approval
```

---

## 📁 Project Structure

```
agentic-devops/
├── api/                # FastAPI routes
├── agents/             # Planner, IaC, Audit, CI/CD agents
├── executor/           # Docker + Terraform + AWS AssumeRole
├── infra/runtime/      # Generated Terraform files
├── policies/           # OPA Rego policies
├── cli/                # Developer CLI
├── docker/             # Terraform sandbox image
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

System dependencies (must be installed):

* Docker
* Terraform
* OPA CLI
* Ollama (local LLM)
* AWS CLI (for bootstrap auth)

Python:

* Python 3.11+

---

## 🤖 Ollama Setup (LLM)

```bash
ollama serve
ollama pull qwen2.5
```

Used via `langchain-community` → `ChatOllama`.

---

## 🐳 Terraform Docker Sandbox

Build once from project root:

```bash
docker build -t tf-sandbox -f docker/terraform.Dockerfile .
```

Verify:

```bash
docker run --rm tf-sandbox version
```

---

## 🔑 AWS Read-Only Access

Create an IAM role with **ReadOnlyAccess**
Use **STS AssumeRole** only (no static keys).

Required permissions include:

* `ec2:Describe*`
* `eks:Describe*`
* `iam:Get*`
* `cloudwatch:Get*`
* `ce:GetCostAndUsage`

---

## ▶️ Run the API

```bash
uvicorn api.main:app --reload
```

Test:

```http
POST /generate
{
  "prompt": "Create a scalable AWS backend in ap-south-1"
}
```

---

## 🧑‍💻 CLI Usage

```bash
python cli/main.py generate "Create AWS EKS cluster"
```

Returns:

* Terraform plan output
* Policy violations (if any)
* Cost estimate
* CI/CD pipeline YAML

---

## 🧪 What the System Does NOT Do

* ❌ Apply Terraform
* ❌ Modify AWS resources
* ❌ Bypass policies
* ❌ Run with admin IAM

This is intentional.

---
## 🔧 About `infra/runtime` (Important)

`infra/runtime` is **not an environment**.

It is a **temporary execution sandbox** managed entirely by the platform.

### What this means

* Users **never edit** `infra/runtime`
* Users **never commit** `infra/runtime`
* All Terraform plans and applies run **inside `runtime`**
* Environment safety is enforced by **policies, approvals, and GitHub protections**, not folder names

### Where users work

Users define intent in:

```
infra/dev
infra/staging
infra/prod
```

The platform automatically:

```
infra/{environment} → infra/runtime → plan / policy / approval / apply
```

### Why this design

* Prevents accidental production changes
* Guarantees consistent execution
* Enables policy enforcement and audit trails
* Separates **intent** from **execution**

> **Think of `runtime` as a secure execution engine — not a workspace.**

⚠️ Do not edit or commit files inside `infra/runtime`.


---
## 🛣️ Roadmap

* Kubernetes runtime agent
* GitHub PR auto-generation
* Multi-cloud (GCP / Azure)
* Incident response agent
* SaaS dashboard

---

## 🧠 Philosophy

> “Infra automation should be **agentic**, but never **autonomous without consent**.”

This project prioritizes **trust, safety, and production realism**.

---

## 📜 License

MIT License
