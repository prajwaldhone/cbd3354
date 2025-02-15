#!/bin/bash

mkdir -p /builds
chown gitlab-runner:gitlab-runner /builds
chmod 777 /var/run/docker.sock

# Register the GitLab Runner (replace these values as needed)
gitlab-runner register --non-interactive \
  --url "https://gitlab.com" \
  --registration-token "<TOKEN>" \
  --executor "shell" \
  --docker-image "alpine:latest"\
  --docker-privileged

# Start the GitLab Runner
gitlab-runner run --user=gitlab-runner
