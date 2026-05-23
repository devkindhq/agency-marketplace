# WhatWeb MCP Server
# Web technology fingerprinting

FROM ruby:3.2-alpine

LABEL org.opencontainers.image.source="https://github.com/FuzzingLabs/offensive-security-mcps"
LABEL org.opencontainers.image.description="WhatWeb MCP Server - Web technology fingerprinting"
LABEL org.opencontainers.image.licenses="MIT"

RUN addgroup -g 1000 mcpuser && \
    adduser -D -u 1000 -G mcpuser mcpuser

RUN apk add --no-cache \
    ca-certificates \
    tini \
    git \
    python3 \
    py3-pip \
    build-base \
    ruby-dev \
    && rm -rf /var/cache/apk/*

# Install WhatWeb
RUN git clone --depth 1 https://github.com/urbanadventurer/WhatWeb.git /opt/whatweb && \
    cd /opt/whatweb && bundle install --without development test && \
    ln -s /opt/whatweb/whatweb /usr/local/bin/whatweb && \
    apk del build-base ruby-dev

RUN whatweb --version

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt
COPY --chown=mcpuser:mcpuser . .
RUN mkdir -p /app/output && chown -R mcpuser:mcpuser /app

USER mcpuser

ENV WHATWEB_OUTPUT_DIR=/app/output
ENV WHATWEB_TIMEOUT=300
ENV PYTHONUNBUFFERED=1

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD pgrep -f "python.*server.py" > /dev/null || exit 1

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["python3", "server.py"]
