import os
import sys
import threading
import boto3
import argparse
from botocore.exceptions import NoCredentialsError

from boto3.s3.transfer import TransferConfig

config = TransferConfig(
    multipart_threshold=1024**3,  # 1GB
    multipart_chunksize=1024**2,  # 1MB
    max_concurrency=10,
    use_threads=True,
)


class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %.2fMB / %.2fMB  (%.2f%%)"
                % (
                    self._filename,
                    self._seen_so_far / (1024 * 1024),
                    self._size / (1024 * 1024),
                    percentage,
                )
            )
            sys.stdout.flush()


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client("s3")

    try:
        s3.upload_file(
            local_file,
            bucket,
            s3_file,
            Config=config,
            Callback=ProgressPercentage(local_file),
        )
        print("\nUpload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload video to AWS S3 bucket.")
    parser.add_argument("-b", "--bucket", required=True, help="S3 bucket name")
    parser.add_argument("-v", "--video", required=True, help="Video file name")

    args = parser.parse_args()

    uploaded = upload_to_aws(args.video, args.bucket, args.video)
