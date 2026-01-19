resource "aws_vpc" "this" {
  cidr_block = var.cidr_block

  tags = {
    Name        = "${var.env}-vpc"
    Environment = var.env
  }
}
