FROM debian:12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openssh-server \
        sudo \
        bash && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /run/sshd /opt/shadowvault/evidence

RUN useradd -m -s /bin/bash investigator && \
    echo "investigator:nightwatch2026" | chpasswd

COPY maintenance.sh /usr/local/sbin/shadow-maintenance
RUN chown root:root /usr/local/sbin/shadow-maintenance && \
    chmod 755 /usr/local/sbin/shadow-maintenance

RUN echo "investigator ALL=(root) NOPASSWD: /usr/local/sbin/shadow-maintenance" \
    > /etc/sudoers.d/shadowvault && \
    chmod 440 /etc/sudoers.d/shadowvault

COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh

EXPOSE 22

ENTRYPOINT ["/entrypoint.sh"]