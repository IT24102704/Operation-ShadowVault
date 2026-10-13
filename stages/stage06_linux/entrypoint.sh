#!/bin/bash

set -e

echo "${SHADOWVAULT_FINAL_FLAG}" > /opt/shadowvault/evidence/final_flag.txt
chown root:root /opt/shadowvault/evidence/final_flag.txt
chmod 600 /opt/shadowvault/evidence/final_flag.txt

mkdir -p /var/log/shadowvault

cat > /var/log/shadowvault/maintenance.log <<'EOF'
2026-09-13 18:10:22 INFO ShadowVault maintenance service initialized
2026-09-13 18:14:07 INFO Evidence archive verification completed
2026-09-13 18:21:44 WARN Legacy helper path configuration detected
2026-09-13 18:35:12 INFO Scheduled maintenance task completed
EOF

chown -R root:root /var/log/shadowvault
chmod 755 /var/log/shadowvault
chmod 644 /var/log/shadowvault/maintenance.log

cat > /usr/local/bin/backup-helper <<'EOF'
#!/bin/bash
echo "Backing up ShadowVault evidence..."
EOF

chown root:root /usr/local/bin/backup-helper
chmod 755 /usr/local/bin/backup-helper

exec /usr/sbin/sshd -D