terraform {
    backend "s3" { # 강의는
      bucket         = "tf101-hr-tfstate" # s3 bucket 이름
      key            = "terraform101/iam/terraform.tfstate" # s3 내에서 저장되는 경로를 의미합니다.
      region         = "us-east-2"
      encrypt        = true
      dynamodb_table = "terraform-lock"
    }
}
