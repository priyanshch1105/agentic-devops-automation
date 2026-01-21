terraform {
  required_version = ">= 1.6.0"
}

provider "aws" {
  region = local.region
}

module "network" {
  source     = "../modules/network"
  cidr_block = var.vpc_cidr
  env        = var.env
}

