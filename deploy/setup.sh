#!/usr/bin/env bash
# Run on the existing memi.click server (Caddy + uv + memi user already set up).
# Usage: WEBHOOK_SECRET=xxxx bash setup.sh
set -euo pipefail

: "${WEBHOOK_SECRET:?Set WEBHOOK_SECRET (the GitHub webhook secret) before running}"

REPO=https://github.com/filias/memi-lx.git
APP_DIR=/opt/memi-lx

# Clone (memi user already exists from the main memi setup)
git clone "$REPO" "$APP_DIR"
chown -R memi:memi "$APP_DIR"

# Install dependencies as memi user
cd "$APP_DIR"
sudo -u memi uv sync

# App service
cp deploy/memi-lx.service /etc/systemd/system/memi-lx.service

# Webhook service + secret
echo "WEBHOOK_SECRET=${WEBHOOK_SECRET}" > /etc/memi-lx-webhook.env
chmod 600 /etc/memi-lx-webhook.env
cp deploy/memi-lx-webhook.service /etc/systemd/system/memi-lx-webhook.service

systemctl daemon-reload
systemctl enable --now memi-lx memi-lx-webhook

# Append the lx.memi.click block to Caddy. If the file already has custom edits,
# add this block by hand instead:
cat >> /etc/caddy/Caddyfile <<'EOF'

lx.memi.click {
    handle /deploy {
        reverse_proxy localhost:9004
    }
    handle {
        reverse_proxy localhost:8086
    }
}
EOF
systemctl reload caddy

echo ""
echo "Done."
echo "1. Make sure DNS A record for lx.memi.click points to this server."
echo "2. Add a GitHub webhook at https://github.com/filias/memi-lx/settings/hooks"
echo "   URL: https://lx.memi.click/deploy   content-type: application/json"
echo "   Secret: \$WEBHOOK_SECRET   events: push"
