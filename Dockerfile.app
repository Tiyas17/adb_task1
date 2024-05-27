# Set base image (host OS) for React app
FROM node:16

# Set working directory
WORKDIR /app

# Copy the package.json and yarn.lock files
COPY src/app/package.json src/app/yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the rest of the React app
COPY src/app .

# Expose the port the app runs on
EXPOSE 3000

# Start the app
CMD ["yarn", "start"]
