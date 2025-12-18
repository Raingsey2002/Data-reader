FROM node:20-alpine

WORKDIR /app

# Copy dependency files first (better caching)
COPY package.json package-lock.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Next.js dev port
EXPOSE 3000

# Start dev server
CMD ["npm", "run", "dev"]
