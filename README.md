# Cloud-Encoder

![version](https://img.shields.io/badge/version-0.0.0-blue)
![license](https://img.shields.io/badge/license-MIT-green)

Cloud-Encoder is an innovative video encoding solution, optimized for cloud environments. It allows for high-speed encoding of high-quality videos, provided sufficient computing resources. Unlike traditional systems that send decoded videos for encoding, Cloud-Encoder allows encoding nodes to directly fetch bitstreams from an S3 bucket. This approach significantly reduces network bandwidth usage. 

The project consists of three main repositories:

1. Cloud-Encoder (this repository): provides a comprehensive description of the project and scripts for AWS system setup.
2. [Encoding Node Repo](https://github.com/over-engineers/cloud-encoder-encoding-node): responsible for the encoding process of each video segment.
3. [Broker Node Repo](https://github.com/over-engineers/cloud-encoder-broker-node): manages the distribution of video segments to the encoding nodes.


## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Seungchul Jang - jangsc0000@gmail.com

Project Link: [https://github.com/over-engineers/Cloud-Encoder](https://github.com/over-engineers/Cloud-Encoder)