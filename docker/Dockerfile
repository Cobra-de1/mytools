FROM ubuntu:20.04

ENV LC_CTYPE C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

RUN useradd -d /home/cobra/ -m -p cobra -s /bin/bash cobra
RUN echo "cobra:cobra" | chpasswd

RUN dpkg --add-architecture i386 && \
apt-get update && apt-get install -y socat && \
apt-get install -y build-essential jq strace ltrace curl wget rubygems gcc dnsutils netcat gcc-multilib net-tools gdb gdb-multiarch python python3 python3-pip python3-dev libssl-dev libffi-dev wget git make procps libpcre3-dev libdb-dev libxt-dev libxaw7-dev libc6:i386 libncurses5:i386 libstdc++6:i386 patchelf && \
pip3 install pwntools keystone-engine unicorn capstone ropper && \
apt-get install python-is-python3 && \
mkdir Install && cd Install && \
cd .. && git clone https://github.com/pwndbg/pwndbg && cd pwndbg && git checkout stable && ./setup.sh && \
cd .. && git clone https://github.com/niklasb/libc-database && cd libc-database && ./get && \
cd .. && git clone https://github.com/Cobra-de1/mytools.git

WORKDIR /home/cobra/

RUN mkdir chall

WORKDIR /home/cobra/chall

COPY ./chall/ .

USER cobra

EXPOSE 13337

CMD socat \
      TCP-LISTEN:13337,reuseaddr,fork \
      EXEC:"/home/cobra/"
