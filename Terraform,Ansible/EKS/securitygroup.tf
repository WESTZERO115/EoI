resource "aws_security_group" "tean-cluster" {
  vpc_id      = aws_vpc.tean.id
  name        = "tean-cluster"

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

}

resource "aws_security_group_rule" "tean-cluster-ingress-node-https" {
  description              = "Allow pods to communicate with the cluster API Server"
  from_port                = 443
  protocol                 = "tcp"
  security_group_id        = aws_security_group.tean-cluster.id
  source_security_group_id = aws_security_group.tean-node.id
  to_port                  = 443
  type                     = "ingress"
}

resource "aws_security_group_rule" "tean-cluster-ingress-workstation-https" {
  cidr_blocks       = ["0.0.0.0/0"]
  description       = "Allow workstation to communicate with the cluster API Server"
  from_port         = 443
  protocol          = "tcp"
  security_group_id = aws_security_group.tean-cluster.id
  to_port           = 443
  type              = "ingress"
}
