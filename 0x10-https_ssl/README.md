# 0x10. HTTPS SSL

This directory contains solutions for HTTPS SSL configuration tasks.

## Learning Objectives

- Understanding HTTPS SSL and its 2 main roles
- The purpose of encrypting traffic
- What SSL termination means
- Configuring domain zones and subdomains
- Setting up HAProxy SSL termination
- Redirecting HTTP traffic to HTTPS

## Files

- **0-world_wide_web**: Bash script that displays information about subdomains using dig and awk
- **1-haproxy_ssl_termination**: HAProxy configuration file for SSL termination on port 443
- **100-redirect_http_to_https**: HAProxy configuration that redirects HTTP traffic to HTTPS with 301 status

## Requirements

- All files interpreted on Ubuntu 16.04 LTS
- All Bash scripts must be executable
- Scripts must pass Shellcheck (version 0.3.7) without errors
- First line: `#!/usr/bin/env bash`
- Second line: Comment explaining the script

## Usage

### Task 0: World Wide Web
```bash
./0-world_wide_web holberton.online
./0-world_wide_web holberton.online web-02
```

### Task 1: HAProxy SSL Termination
Configure HAProxy to listen on port 443 and handle SSL traffic.

### Task 2: HTTP to HTTPS Redirect
Configure HAProxy to automatically redirect HTTP traffic to HTTPS with 301 status.
