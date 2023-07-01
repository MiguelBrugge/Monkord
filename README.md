# Monkord

Welcome to the Monkord! This project is a chat application built using Django and Django Channels, incorporating websockets for real-time communication. With this application, users can log in, choose who they want to chat with, and have interactive conversations. Additionally, users have the ability to customize their online status, search for specific chats, and format their messages using bold, italic, and h1 styles.

![image](https://github.com/MiguelBrugge/Monkord/assets/103996305/5e087003-fc70-4a35-b0be-ba6d37a2d93f)
![image](https://github.com/MiguelBrugge/Monkord/assets/103996305/44cdb8a5-b711-4913-b21f-412619065391)
![image](https://github.com/MiguelBrugge/Monkord/assets/103996305/f27930fb-75b4-45ff-8a22-1e1ad283e791)

# Features
- **User Registration and Authentication:**
Users can create an account and log in to the application.
User authentication is implemented to ensure secure access.

- **Chat Functionality:**
Users can select a recipient to start a chat conversation.
The application leverages Django Channels to enable real-time messaging through websockets.
Messages are updated instantly, providing a seamless chat experience.

- **Online Status:**
Users can update their online status to indicate their availability for chat.
The online status is displayed in real-time to other users.

- **Chat Search:**
The application provides a search bar to quickly find specific chats.
Users can search for chats based on the recipient's name or other relevant information.

- **Message Formatting:**
Users can format their messages using bold, italic, and h1 styles.
The formatting is rendered in real-time, making the chat more visually appealing.

- **User Profile:**
Each user has a profile that includes information such as their username, name, about section, and profile picture (pfp).
Users can update their profile information and upload a custom profile picture.

# Technologies Used
**Monkord utilizes the following technologies:**

Python: A powerful programming language used for the development of the backend logic.
Django: A high-level Python web framework that provides a robust foundation for building web applications.
Django Channels: A Django library that adds support for WebSocket communication, enabling real-time, bidirectional communication between the client and the server.
HTML: The standard markup language used for creating web pages.
CSS: A stylesheet language used for describing the visual presentation of the application.
JavaScript: A programming language that enables dynamic and interactive elements on web pages.
