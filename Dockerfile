FROM mottosso/maya:2026 AS install_stage

# RUN dnf update -y

# install go
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


# Setup project
FROM install_stage AS project_stage

# Setup folder structure
RUN mkdir /maya-stubs
WORKDIR /maya-stubs
RUN mkdir src

# Copy all the relevant files from the host
COPY packages packages
COPY go.work go.work
COPY build_stubs.sh build_stubs.sh

# Download go dependencies
RUN go1.25.4 work sync

# Build and install the stubgen binary
RUN go1.25.4 install -C packages/maya-stubgen


# Get the synopsis from mayapy
FROM project_stage AS mayapy_stage
RUN mayapy packages/maya-stubgen/scripts/get_synopsis.py


# Copy synopsis files over
FROM scratch AS mayapy_output_stage
COPY --from=mayapy_stage /maya-stubs/.cache/synopsis ./.cache/synopsis


# Run go stubgen program
FROM project_stage AS build_stubs_stage
CMD ["sh", "build_stubs.sh"]
