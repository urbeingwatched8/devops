resource "aws_instance" "example" {
  ami           = " ami-00399ec92321828f5"
  instance_type = "t2.micro"

  tags = {
    Name = "new-vm"
  }
}

provider "aws" {
  region = "us-east-2"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.56.0"
    }
  }
}



