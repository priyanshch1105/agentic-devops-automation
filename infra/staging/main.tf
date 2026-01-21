terraform {
  required_version = ">= 1.6.0"
}

provider "aws" {
  region = local.region
}

module "network" {
  source     = "../modules/network"
  cidr_block = local.vpc_cidr
  env        = local.env
}

