#!/usr/bin/env bash
# Run on the existing memi.click server (Caddy + uv already installed).
# Usage: bash setup.sh
set -euo pipefail

REPO=https://github.com/filias/memi-lx.git
APP_DIR=/opt/memi-lx

# Clone (memi user already exists from the main memi setup)
git clone "$REPO" "$APP_DIR"
chown -R memi:memi "$APP_DIR"

# Install dependencies as memi user
cd "$APP_DIR"
sudo -u memi uv sync

# Install systemd service
cp deploy/memi-lx.service /etc/systemd/system/memi-lx.service
systemctl daemon-reload
systemctl enable --now memi-lx

# Add the lx.memi.click block to Caddy. Run this manually if the file
# already has custom edits — append the block by hand instead.
cat >> /etc/caddy/Caddyfile <<'EOF'

lx.memi.click {
    reverse_proxy localhost:8086
}
EOF
systemctl reload caddy

echo ""
echo "Done. Make sure DNS A record for lx.memi.click points to this server."
