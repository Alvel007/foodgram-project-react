FROM node:13.12.0-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install --force
COPY . ./
RUN npm run build
CMD ["npx", "-y", "http-server", "-p", "9080", "/app/build"]