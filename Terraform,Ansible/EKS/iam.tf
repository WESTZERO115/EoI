resource "aws_iam_role" "tean-cluster" {
  name = "terraform-eks-tean-cluster"

  assume_role_policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "ec2.amazonaws.com",
          "Service" : "eks.amazonaws.com"
        },
        "Action" : "sts:AssumeRole"
      }
    ]
}
POLICY

}


resource "aws_iam_role_policy_attachment" "tean-cluster-AmazonEKSClusterPolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role = aws_iam_role.tean-cluster.name
}

resource "aws_iam_role_policy_attachment" "tean-cluster-AmazonEKSServicePolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSServicePolicy"
  role = aws_iam_role.tean-cluster.name
}



# If no loadbalancer was ever created in this region, then this following role is necessary
resource "aws_iam_role_policy" "tean-cluster-service-linked-role" {
  name = "service-linked-role"
  role = aws_iam_role.tean-cluster.name

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",

            "Resource": "arn:aws:iam::*:role/aws-service-role/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeAccountAttributes"
            ],
            "Resource": "*"
        }
    ]
}
EOF

}
