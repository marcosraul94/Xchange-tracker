FROM ubuntu:24.04

WORKDIR /app
COPY package.json .
COPY package-lock.json .

# Install node 22
RUN apt update
RUN apt install -y curl
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
RUN apt-get update && apt-get install -y nodejs

# App dependencies
RUN npm i 

# Install browsers
RUN apt-get install -y packagekit-gtk3-module
RUN apt-get install -y libasound2t64
RUN npx puppeteer browsers install firefox
RUN npx puppeteer browsers install chrome

COPY . .
