package terraform.policy

# Block IAM policy creation
deny contains msg if {
  rc := input.resource_changes[_]
  rc.type == "aws_iam_policy"
  msg := "IAM policy creation is not allowed"
}

# Block open security groups (0.0.0.0/0)
deny contains msg if {
  rc := input.resource_changes[_]
  rc.type == "aws_security_group"
  rc.change.after.ingress != null
  ingress := rc.change.after.ingress[_]
  ingress.cidr_blocks[_] == "0.0.0.0/0"
  msg := "Security group allows 0.0.0.0/0 ingress"
}

# Block deletions
deny contains msg if {
  rc := input.resource_changes[_]
  "delete" in rc.change.actions
  msg := sprintf("Resource deletion blocked: %s", [rc.type])
}
