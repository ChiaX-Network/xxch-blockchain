#!/usr/bin/env bash
# Post install script for the UI .deb to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /opt/xxch/resources/app.asar.unpacked/daemon/xxch /usr/bin/xxch || true
ln -s /opt/chiax-network/xxch-blockchain /usr/bin/xxch-blockchain || true
