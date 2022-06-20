resource "aws_eks_cluster" "tean" {
  name     = var.cluster-name
  role_arn = aws_iam_role.tean-cluster.arn

  vpc_config {
    subnet_ids = [aws_subnet.tean-public-1.id, aws_subnet.tean-public-2.id]

    security_group_ids = [aws_security_group.tean-cluster.id]
  }

  depends_on = [
    aws_iam_role_policy_attachment.tean-cluster-AmazonEKSClusterPolicy,
    aws_iam_role_policy_attachment.tean-cluster-AmazonEKSServicePolicy,
  ]

}
