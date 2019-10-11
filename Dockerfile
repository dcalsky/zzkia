FROM node:12-alpine

# Setting working directory. All the path will be relative to WORKDIR
WORKDIR /app

# Installing dependencies
COPY ./package.json ./
RUN npm install
