# Create a VPC
resource "aws_vpc" "custom-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "${var.TAG_NAME}"
  }
}

resource "aws_subnet" "custom-subnet" {
  vpc_id     = aws_vpc.custom-vpc.id
  cidr_block = "10.0.8.0/24"
  tags = {
    Name = "${var.TAG_NAME}"
  }
}

resource "aws_instance" "web" {
  ami           = var.EC2_AMI
  instance_type = var.EC2_INSTANCE_TYPE
  subnet_id     = aws_subnet.custom-subnet.id
  tags = {
    Name = "${var.TAG_NAME}"
  }
} 