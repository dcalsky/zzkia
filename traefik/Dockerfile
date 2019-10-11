FROM traefik:alpine
RUN mkdir -p /etc/traefik/acme
RUN touch /etc/traefik/acme/acme.json
RUN chmod 600 /etc/traefik/acme/acme.json
COPY ./traefik.toml /etc/traefik
