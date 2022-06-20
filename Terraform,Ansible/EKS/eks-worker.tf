resource "aws_eks_node_group" "tean-node" {
  cluster_name    = aws_eks_cluster.tean.name
  node_group_name = "tean-node"
  node_role_arn   = aws_iam_role.tean-node.arn
  subnet_ids      = [aws_subnet.tean-public-1.id, aws_subnet.tean-public-2.id]

  scaling_config {
    desired_size = 1
    max_size     = 3
    min_size     = 1
  }

  update_config {
    max_unavailable = 2
  }

  # Ensure that IAM Role permissions are created before and deleted after EKS Node Group handling.
  # Otherwise, EKS will not be able to properly delete EC2 Instances and Elastic Network Interfaces.
  depends_on = [
    aws_iam_role_policy_attachment.tean-cluster-AmazonEKSClusterPolicy,
    aws_iam_role_policy_attachment.tean-cluster-AmazonEKSServicePolicy,

  ]
}
