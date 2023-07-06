provider "aws" {
  region = "ap-northeast-2"
}

resource "aws_s3_bucket" "video_transcoding_bucket" {
  bucket = "video-transcoding-bucket"
  acl    = "private"

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["PUT", "POST"]
    allowed_origins = ["http://<your-ip-address>/24"]
    expose_headers  = ["ETag"]
    max_age_seconds = 3000
  }
}

resource "aws_s3_bucket_policy" "bucket_policy" {
  bucket = aws_s3_bucket.video_transcoding_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = "*"
        Action = ["s3:PutObject", "s3:PutObjectAcl"]
        Resource = "${aws_s3_bucket.video_transcoding_bucket.arn}/*"
        Condition = {
          IpAddress = {
            "aws:SourceIp" = "<your-ip-address>/24"
          }
        }
      },
    ]
  })
}

