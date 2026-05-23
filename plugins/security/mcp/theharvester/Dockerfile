FROM python:3.12-slim

LABEL org.opencontainers.image.description="theHarvester MCP Server - OSINT email, subdomain and contact harvesting"
LABEL org.opencontainers.image.licenses="MIT"

RUN addgroup --gid 1000 mcpuser && \
    adduser --disabled-password --uid 1000 --ingroup mcpuser mcpuser

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ca-certificates \
    tini \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Install theHarvester
RUN git clone --depth 1 https://github.com/laramies/theHarvester.git /opt/theharvester && \
    cd /opt/theharvester && \
    uv sync --no-dev

# MCP layer runs on system Python; theHarvester runs via its own venv
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=mcpuser:mcpuser . .
RUN mkdir -p /app/output && chown -R mcpuser:mcpuser /app

USER mcpuser

ENV THEHARVESTER_OUTPUT_DIR=/app/output
ENV THEHARVESTER_TIMEOUT=120
ENV PYTHONUNBUFFERED=1

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD pgrep -f "python.*server.py" > /dev/null || exit 1

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/usr/local/bin/python3", "server.py"]
