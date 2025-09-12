# Use an official Node.js runtime as a parent image
FROM node:20-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package.json ./

# Install app dependencies
# Using --frozen-lockfile is a good practice for CI/CD
RUN npm install

# Copy the rest of the application's code
COPY . .

# The Next.js app will be started by the command in docker-compose
EXPOSE 3000
# CMD ["npm", "run", "dev"]
