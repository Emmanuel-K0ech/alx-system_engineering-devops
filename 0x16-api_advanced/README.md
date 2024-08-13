# 0x16. API advanced

## Background Context

Questions involving APIs are common in interviews. Sometimes they’re as simple as asking you to "write a Python script that queries a given endpoint," while other times, they may require you to use recursive functions and format or sort the results.

A great API to practice with is the [Reddit API](https://www.reddit.com/dev/api/). It offers a wide range of endpoints, many of which don’t require any form of authentication, and it provides tons of information that can be parsed and presented. Getting comfortable with API calls now can save you a lot of stress during technical interviews. Additionally, outside of the job market, you might find personal use cases that make your life easier.

## Resources

Read or watch:

- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts to anyone, without the help of Google:

### General

- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Copyright - Plagiarism

You are expected to come up with solutions for the tasks below yourself to meet the above learning objectives. 

- **Do not copy and paste** someone else’s work; this will not help you meet the objectives of this or any following project.
- **You are not allowed to publish** any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Libraries imported in your Python files must be organized in alphabetical order
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use the `Requests` module for sending HTTP requests to the Reddit API
