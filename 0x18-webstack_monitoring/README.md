# 0x18. Webstack monitoring

## Background Context

“You cannot fix or improve what you cannot measure” is a well-known saying in the tech industry. In the era of data-ism, monitoring the performance and behavior of our software systems is crucial. In this project, we will implement one of the many tools available to measure what is happening on our servers.

Web stack monitoring can be broken down into two main categories:

1. **Application Monitoring**: Collecting data about your running software to ensure it behaves as expected.
2. **Server Monitoring**: Gathering data about your virtual or physical servers to ensure they are not overloaded (this could include CPU, memory, disk, or network overload).

## Resources

To help you with this project, here are some recommended resources:

- [What is server monitoring](https://www.sumologic.com/glossary/server-monitoring/)
- [What is application monitoring](https://en.wikipedia.org/wiki/Application_performance_management)
- [System monitoring by Google](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without external help:

### General

- **Why is monitoring needed?**
- **What are the two main areas of monitoring?**
- **What are access logs for a web server (such as Nginx)?**
- **What are error logs for a web server (such as Nginx)?**

## Copyright and Plagiarism

You are expected to develop your solutions for the tasks below independently to meet the above learning objectives. Copying and pasting someone else’s work will not help you achieve the objectives of this or any future project. Additionally:

- You are **not allowed to publish any content** from this project.
- Any form of plagiarism is **strictly forbidden** and will result in removal from the program.

## Requirements

### General

- **Allowed editors**: `vi`, `vim`, `emacs`
- All your files will be interpreted on **Ubuntu 16.04 LTS**.
- All your files should end with a **new line**.
- A `README.md` file, located at the root of the project folder, is **mandatory**.
- All your Bash script files must be **executable**.
- Your Bash scripts must pass **Shellcheck (version 0.3.7)** without any error.
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of all your Bash scripts should be a **comment** explaining what the script does.
