#hye_rin이라는 iam 사용자를 만들고 정책 추가

resource "aws_iam_user" "hye_rin" {
  name = "hye.rin"
}


resource "aws_iam_user_policy" "art_devops_black_for_hyerin" {
  name  = "super-admin"
  user  = aws_iam_user.hye_rin.name

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "*"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
EOF
}
