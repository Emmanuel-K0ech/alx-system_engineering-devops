# 0x0D. Web Stack Debugging #0

## DevOps | SysAdmin | Scripting | Debugging  
**Weight:** 1

---

## Concepts
For this project, we expect you to look at these concepts:
- **Network basics**
- **Docker**
- **Web stack debugging**

---

## Background Context
The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that’s the “fun” part of the job!).

Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to master this skill.

In this debugging series, broken/bugged webstacks will be provided to you. The final goal is to come up with a Bash script that, once executed, will bring the webstack to a working state. However, before writing the Bash script, you should figure out what is going wrong and fix it manually.

### Example Problem
Your server must:
- Have a copy of the `/etc/passwd` file in `/tmp`
- Have a file named `/tmp/isworking` containing the string `OK`

Without these two elements, the web application cannot function.

### Example Fix
```bash
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
vagrant@vagrant:~$ docker ps
vagrant@vagrant:~$ docker exec -ti <container_id> /bin/bash
root@<container_id>:/# cp /etc/passwd /tmp/
root@<container_id>:/# echo OK > /tmp/isworking
root@<container_id>:/# ls /tmp/
isworking  passwd
```

### Answer File Example:
```bash
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
```

**Note:** Since you cannot use interactive software such as `vi` or `emacs` in your Bash script, all modifications should be done via the command line.

---

## Installing Docker
For this project, you will be given a container to solve the task. However, if you would like to install Docker locally to experiment with the task, you can do so on various systems.

### Supported Operating Systems:
- **Mac OS**
- **Windows**
- **Ubuntu 14.04** (Note that Docker for Ubuntu 14 is deprecated and may require adjustments)
- **Ubuntu 16.04**

### Example Commands:
```bash
# Pull the Ubuntu 14.04 image
docker run -d -ti ubuntu:14.04

# Check running containers
docker ps

# Access a running container
docker exec -ti <container_id> /bin/bash
```

---

## Resources
- **man** or **help**: `curl`

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on **Ubuntu 14.04 LTS**
- All files should end with a new line
- A `README.md` file is mandatory at the root of the project folder
- All Bash script files must be executable
- All Bash scripts must pass **Shellcheck** without any errors
- All Bash scripts must run without errors
- The first line of all Bash scripts must be `#!/usr/bin/env bash`
- The second line of all Bash scripts must be a comment explaining what the script does
