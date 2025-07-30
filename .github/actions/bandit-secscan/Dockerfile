# .github/actions/bandit-secscan/Dockerfile

FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y build-essential && \
    pip install --no-cache-dir bandit

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
