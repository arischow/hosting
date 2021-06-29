# Self-hosted services

## System-level
- fail2ban

## Application-level
- AdGuard Home
- Traefik
- VaultWarden
- Ghost
- MySQL

## Should backup before destorying the server
- `.env.prod`
- `.env.prod.ghost`
- `.env.prod.mysql`
- `/opt/bitwarden`
- `/opt/adguardhome`
- `/opt/traefik/secrets`
- `/var/lib/ghost/content`
- `/var/lib/mysql`
