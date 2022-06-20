resource "aws_instance" "tean" {
  ami = var.AMIS[var.AWS_REGION]
  instance_type = "t2.micro"

  key_name = aws_key_pair.mykeypair.key_name

  subnet_id = aws_subnet.tean-public-1.id

  vpc_security_group_ids = [aws_security_group.tean-cluster.id]

}
