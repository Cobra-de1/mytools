FROM ubuntu:20.04

ENV LC_CTYPE C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

RUN useradd -d /home/cobra/ -m -p cobra -s /bin/bash cobra
RUN echo "cobra:cobra" | chpasswd

WORKDIR /home/cobra/

RUN dpkg --add-architecture i386 && \
apt-get update && apt-get -y install sudo && apt-get install -y socat && \
apt-get install -y build-essential jq strace ltrace curl wget rubygems gcc dnsutils netcat gcc-multilib net-tools gdb gdb-multiarch python python3 python3-pip python3-dev libssl-dev libffi-dev wget git make procps libpcre3-dev libdb-dev libxt-dev libxaw7-dev libc6:i386 libncurses5:i386 libstdc++6:i386 patchelf elfutils && \
pip3 install pwntools keystone-engine unicorn capstone ropper && \
apt-get install -y python-is-python3 && \
mkdir Install && cd Install && \
git clone https://github.com/pwndbg/pwndbg && cd pwndbg && ./setup.sh && \
cd .. && git clone https://github.com/Cobra-de1/mytools.git && \
cd .. && mkdir chall

WORKDIR /home/cobra/chall

COPY ./chall/ .

EXPOSE 13337

CMD socat \
      TCP-LISTEN:13337,reuseaddr,fork \
      EXEC:"/home/cobra/chall/chall"
