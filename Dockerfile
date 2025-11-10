FROM mottosso/maya:2026

# RUN dnf update -y

# install go
RUN dnf install -y golang
ENV PATH="$PATH:/root/go/bin"
RUN go install golang.org/dl/go1.25.4@latest
RUN go1.25.4 download

# Install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH=:"$PATH:/root/.local/bin/"

# Setup folder structure
RUN mkdir /maya-stubs
WORKDIR /maya-stubs
RUN mkdir src

# Copy all the relevant files from the host
COPY packages packages
COPY go.work go.work
COPY build_stubs.sh build_stubs.sh
RUN chmod +x build_stubs.sh

# Download go dependencies
RUN go1.25.4 work sync

# build the stubgen binary
RUN go1.25.4 build -C packages/maya-stubgen

# Get the synopsis from mayapy
RUN mayapy packages/maya-stubgen/scripts/get_synopsis.py

CMD ["sh", "build_stubs.sh"]
