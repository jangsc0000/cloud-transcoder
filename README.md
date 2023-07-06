# **Cloud-Transcoder**

![version](https://img.shields.io/badge/version-0.0.0-blue)
![license](https://img.shields.io/badge/license-MIT-green)

Cloud-Transcoder is a highly efficient video transcoding solution, optimized for cloud environments. It allows for rapid transcoding of high-quality videos, given sufficient computational resources. Unlike conventional systems, which send decoded videos for transcoding, Cloud-Transcoder enables transcoding nodes to directly fetch bitstreams from an S3 bucket. This significantly reduces network bandwidth usage.

Please note that this repository is an implementation of a cloud transcoder for test or experimental purposes. Given the nature of a transcoder, this project assumes that external access is impossible, and it is not intended for production use.

The current goal of this repository is to implement the Naver distributed transcoder (https://d2.naver.com/helloworld/3661677). Afterward, the project aims to implement Intel's transcoder (https://networkbuilders.intel.com/blog/svt-av1-enables-highly-efficient-large-scale-video-on-demand-vod-services).

The project comprises three main repositories:

1. Cloud-Transcoder (this repository): provides a comprehensive description of the project and scripts for AWS system setup.
2. **[Transcoding Node Repo](https://github.com/over-engineers/cloud-transcoder-transcoding-node)**: responsible for the transcoding process of each video segment.
3. **[Broker Node Repo](https://github.com/over-engineers/cloud-transcoder-broker-node)**: manages the distribution of video segments to the transcoding nodes.

## **Directory Structure**

The project follows the given directory structure:

```bash
.
├── client
│   └── uploader.py
├── terraform
│   └── main.tf
├── HOW_TO_USE.md
├── README.md
└── LICENSE

```

## **How To Use**

To get started with Cloud-Transcoder, please refer to the [How to Use Guide](./HOW_TO_USE.md) for a step-by-step guide.


## **License**

Distributed under the MIT License. See **`LICENSE`** for more information.

## **Contact**

Seungchul Jang - **[jangsc0000@gmail.com](mailto:jangsc0000@gmail.com)**

Project Link: **https://github.com/over-engineers/Cloud-Transcoder**