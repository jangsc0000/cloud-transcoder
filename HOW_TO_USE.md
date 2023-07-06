# **How To Use**

Follow the detailed steps below to set up and use Cloud-Transcoder:

## **AWS Credentials Setup**

Before you can use Cloud-Transcoder, you will need to provide your AWS credentials. This allows Terraform to access your AWS account and manage resources. Here are two ways to set up your AWS credentials:

## Using Environment Variables:

You can set your AWS credentials through environment variables. Open your terminal and type the following commands:

```bash
export AWS_ACCESS_KEY_ID="your access key"
export AWS_SECRET_ACCESS_KEY="your secret key"
```

Replace **`"your access key"`** and **`"your secret key"`** with your actual AWS access key and secret key.

## Using AWS Credentials File:

Alternatively, you can create an AWS credentials file on your system. By default, the file location is **`~/.aws/credentials`**. At this location, create a file named **`credentials`** and add the following content:

```toml
[default]
aws_access_key_id = your access key
aws_secret_access_key = your secret key
```

Replace **`"your access key"`** and **`"your secret key"`** with your actual AWS access key and secret key. Remember to save the file once you're done.

## **Terraform Setup and Infrastructure Creation**

With your AWS credentials set, you can now initialize your Terraform workspace. First, navigate to the **`terraform`** directory where the **`main.tf`** file is located:

```bash
cd terraform
```

Then, you need to update the allowed_origins and aws:SourceIp in your main.tf file to your IP address. You can use any text editor to make this change. Replace \<your-ip-address>/24 with your IP address.

```hcl
cors_rule {
  allowed_origins = ["http://<your-ip-address>/24"]
}

resource "aws_s3_bucket_policy" "bucket_policy" {
  Condition = {
    IpAddress = {
      "aws:SourceIp" = "<your-ip-address>/24"
    }
  }
}
```
After making the changes, save and close the main.tf file.

Next, initialize your Terraform workspace, which will set up the necessary Terraform files:

```bash
terraform init
```

Once initialized, you can apply the changes proposed in **`main.tf`**:

```bash
terraform apply
```

This command also prompts for confirmation before making any changes to your infrastructure. Once you're done, you can destroy all the resources that were created by using the **`destroy`** command:

```bash
terraform destroy
```

## **Uploading Video Files**

With the infrastructure set up, you can now upload your video files to the S3 bucket. Navigate to the **`client`** directory and execute the **`uploader.py`** script:

```bash
cd ../client
```

For instance, you can download a sample video and upload it to your S3 bucket with the following commands:

```bash
wget https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_20mb.mp4
python3 uploader.py -b video-transcoding-bucket -v big_buck_bunny_720p_20mb.mp4
```

This will upload the downloaded video file to the **`video-transcoding-bucket`** bucket in your AWS account. You can replace **`video-transcoding-bucket`** with the name of your S3 bucket and **`big_buck_bunny_720p_20mb.mp4`** with the path to your video file.