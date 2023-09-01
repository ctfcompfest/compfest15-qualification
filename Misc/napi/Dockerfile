FROM ubuntu:18.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3.7 && \
    apt-get install -y socat && \
    apt-get install -y openssh-server

# Add users
RUN useradd -m ctf
RUN useradd -m admin

# Set work directory
WORKDIR /home/ctf

# Copy src
COPY src/ctf /home/ctf
COPY src/admin /home/admin

# Set privileges
RUN chown -R ctf:ctf /home/ctf && \
    chmod 700 /home/ctf && \
    chmod +x /home/ctf/start.sh

# Setup SSH shell welcome message
RUN rm -rf /etc/update-motd.d/ && \
    rm -rf /etc/legal && \
    echo "Welcome to PRISON ADMINISTRATOR SHELL" > /etc/motd

# Setup SSH server
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

# Setup SSH key
RUN ssh-keygen -f /home/ctf/creds.txt && \
    base64 creds.txt > creds.64 && \
    mv creds.64 creds.txt

# Add created key as authorized key
RUN mkdir /home/admin/.ssh && \
    mv creds.txt.pub /home/admin/.ssh/authorized_keys && \
    chown -R admin:admin /home/admin/.ssh && \
    chmod 700 /home/admin/.ssh && \
    chmod 600 /home/admin/.ssh/authorized_keys && \
    service ssh start

EXPOSE 9999
EXPOSE 22

CMD ["./start.sh"]