#!/bin/sh
docker build -t ctf:20.04 .
docker run --rm -v  $PWD/chall:/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -p 15000:13337 -d --name ctf -i ctf:20.04
docker exec -it ctf /bin/bash
