# Flask Chat App

This is a simple chat application built using Flask and Socket.IO. The application allows users to authenticate with a username and password, and then engage in real-time chat.

## Features

- **User Authentication:** Users need to provide a username and password to authenticate.
- **Real-time Chat:** Once authenticated, users can send and receive real-time messages in the chat.

## Setup

1. Install the required dependencies:

   ```bash
   pip install Flask flask-socketio
   ```

2. Run the Flask application:

   ```bash
   python app.py
   ```

3. Open your browser and navigate to [http://localhost:5000](http://localhost:5000).

## Usage

1. When the application starts, users are prompted to enter their name and password.
2. Upon successful authentication, users can send and receive messages in the chat.

## Technologies Used

- **Flask:** A micro web framework for Python.
- **Socket.IO:** Enables real-time, bidirectional, and event-based communication.

## Directory Structure

- **app.py:** The main Flask application file.
- **templates/index.html:** HTML template for the chat interface.

## Dependencies

- Flask
- Flask-SocketIO
- Bootstrap (CSS and JS)
- Socket.IO client library

## Notes

- The application uses Bootstrap for styling and Socket.IO for real-time communication.
- Authentication is basic and for demonstration purposes only; it's not suitable for a production environment.
- Messages are broadcasted to all connected clients.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
