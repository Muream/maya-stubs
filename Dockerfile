FROM mottosso/maya:2026 AS installs_stage

# Install go
RUN dnf install -y golang
ENV GOPATH="/root/go"
ENV GOBIN="/root/go/bin"
ENV PATH="$PATH:$GOPATH/bin"
RUN go install golang.org/dl/go1.25.4@latest
RUN go1.25.4 download

# Install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH=:"$PATH:/root/.local/bin/"
RUN uv tool install ruff@latest


# Setup project
FROM installs_stage AS project_setup_stage

# Setup folder structure
RUN mkdir /maya-stubs
WORKDIR /maya-stubs
RUN mkdir src

# Copy go project the relevant files from the host
COPY packages packages
COPY go.work go.work

# Download go dependencies
RUN go1.25.4 work sync

# Build and install the stubgen binary
RUN go1.25.4 install -C packages/maya-stubgen


# Setup project
FROM project_setup_stage AS build_stubs_stage

# Copy build script and run it
COPY build_stubs.sh build_stubs.sh
CMD ["sh", "build_stubs.sh"]
