import streamlit as st
import requests

st.set_page_config(page_title="Infra Control Plane", layout="centered")

st.title("🚀 Infrastructure Control Plane")

env = st.selectbox(
    "Select Environment",
    ["dev", "staging", "prod"]
)

if st.button("Run Terraform Plan"):
    r = requests.post(
        "http://localhost:8000/run",
        json={"environment": env}
    )

    data = r.json()

    if "message" in data:
        st.success(data["message"])
    else:
        st.error(data.get("error", "Failed to trigger workflow"))

st.markdown("---")
st.caption("All executions are policy-checked and approval-gated.")