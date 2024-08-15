# 0x17. Web stack debugging #3

## Background Context

When debugging software, logs might not always provide enough information. There are times when an error doesn't get logged as expected, or the logged information is insufficient to diagnose the problem. In such situations, you may need to dig deeper into the stack to uncover the root cause. As a Holberton student, you're equipped to tackle these challenges.

WordPress is a widely-used platform, powering approximately 26% of the web. It is used for running blogs, portfolios, e-commerce sites, and company websites. Given its popularity, there’s a good chance you'll encounter WordPress in your career.

WordPress typically runs on a LAMP stack, which includes Linux, Apache, MySQL, and PHP—a widely-used combination of tools for web development. The web stack you're debugging today involves a WordPress website running on this LAMP stack.

## Requirements

### General
- All your files will be interpreted on **Ubuntu 14.04 LTS**.
- All your files should end with a **new line**.
- A `README.md` file at the root of the project folder is **mandatory**.
- Your Puppet manifests must pass **puppet-lint version 2.1.1** without any errors.
- Your Puppet manifests must run without error.
- Your Puppet manifests' first line must be a **comment** explaining what the Puppet manifest is about.
- Your Puppet manifest files must end with the extension `.pp`.
- Files will be checked with **Puppet v3.4**.

### More Info

To install `puppet-lint`:

```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
