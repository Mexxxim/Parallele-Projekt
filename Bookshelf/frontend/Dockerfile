# Use an official Node runtime as a parent image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the local source files to the container
COPY . .

# Build the React app
RUN npm run build

# Expose the port on which your app will run
EXPOSE 3000

# Define the command to run your app
CMD ["npm", "start"]
