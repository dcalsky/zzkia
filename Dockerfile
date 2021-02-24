FROM node:current-alpine3.13
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .