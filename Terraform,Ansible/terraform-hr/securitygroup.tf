data "aws_ip_ranges" "european_ec2" {
  regions  = ["us-west-2", "us-west-1"]
  services = ["ec2"]
}

resource "aws_security_group" "security" {
  name        = "security"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port        = 80
    to_port          = 80
    protocol         = "tcp" 
    cidr_blocks      = slice(data.aws_ip_ranges.european_ec2.cidr_blocks, 0, 50)
  }

  egress {
    from_port        = 80
    to_port          = 80
    protocol         = "tcp" 
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    CreateDate = data.aws_ip_ranges.european_ec2.create_date
    SyncToken  = data.aws_ip_ranges.european_ec2.sync_token
  }
}
