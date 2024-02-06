# buddy-chat

buddy-chat is a real-time messaging API built with Django. It enables peer-to-peer messaging between users through API and WebSocket connections. It includes read receipts in the response.

## Features

- Real-time peer-to-peer messaging: Users can send and receive messages in real time.
- API Key/Token Authentication: The API is secured and can only be accessed using a JWT token.
- Read Status Update: The read status of a message can be updated through an API call. The frontend makes this API call once the message is read.

## Technology

The API is built with Django and is dockerized for easy deployment and scalability. It utilizes Django Channels for websocket connections and the Django Rest Framework for the API endpoints.

## Usage

Make sure you have Docker and Docker Compose installed on your machine.

1. Create a `.env` file using the provided `.env.sample` file as a template:

    ```
    cp .env.sample .env
    ```

2. To run the app, use the following command:

    ```
    docker-compose up --build -d
    ```

3. To stop the app, use the following command:

    ```
    docker-compose down
    ```

## API Documentation

- Postman: [https://www.postman.com/thor-nuga/workspace/demos/collection/65c1f1f1a6e12996118e047b?action=share&creator=24636682](https://www.postman.com/thor-nuga/workspace/demos/collection/65c1f1f1a6e12996118e047b?action=share&creator=24636682)
- ReDoc: [localhost:8000/api-schema/redoc/](localhost:8000/api-schema/redoc/)
- Swagger-ui: [localhost:8000/api-schema/swagger-ui/](localhost:8000/api-schema/swagger-ui/)

## License

buddy-chat is open-source software licensed under the BSD-3-Clause license.
