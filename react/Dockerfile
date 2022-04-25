FROM node:14-alpine
# Install webserver
RUN npm install -g serve
# Add a work directory
RUN mkdir -p /opt/voicee_pay/react/
WORKDIR /opt/voicee_pay/react/
# Copy app files
COPY . /opt/voicee_pay/react/
RUN npm run build
# Expose port
EXPOSE 3000
# Start the app
CMD ["serve", "-s", "build", "-l", "3000"]