# Overview

This project was created to explore the fundamentals of networking and understand how devices communicate over a network. Beyond just sending data, networking allows us to solve real problems like enabling multiple users to connect, exchanging messages in real time, and collaborating remotely. This project is a hands-on way to see networking in action and appreciate how servers and clients interact.

This program is a simple client/server chat application. The server listens for incoming connections and broadcasts messages to all connected clients, while the client provides a browser-based interface for sending and receiving messages. It demonstrates core networking concepts like sockets, message handling, and multi-client communication, packaged in a lightweight and interactive program.

To use NetworkChat, start the server by running python server.py in a terminal. Then, open index.html in a browser to launch the client, and start chatting. Messages sent from any client are immediately broadcast to all others, allowing multiple users to communicate in real time. If clients and server are on the same network the server runs on "localhost:8765". If hosted in the cloud, both index.html and server.py would need "localhost" changed to the cloud server address.

[Network Chat](https://youtu.be/3LATz4S7Yvc)

# Network Communication

This program uses a client/server architecture, where a central server manages connections and message distribution to multiple clients.

The application communicates over TCP to ensure reliable delivery of messages. By default, the server listens on port 8765

Messages between the client and server are sent as plain text strings, with each message representing a single chat line. The server broadcasts each incoming message to all connected clients, allowing real-time communication across multiple users.

# Development Environment

{Describe the tools that you used to develop the software}
Visual Studio Code

{Describe the programming language that you used and any libraries.}
Python
Python Websockets Library
Python asyncio Library
Javascript
Html
Css

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [websockets](https://websockets.readthedocs.io/en/stable/index.html)
* [Python Docs](https://docs.python.org/3/library/socket.html)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Save chat history even when server is turned off
* Create rooms to organize chats
* Create log term users with access to their personal chats and rooms

# AI Disclosure
While developing, I used AI (GPT-5 & Gemini 3 Thinking) as a learning tool and guide. The AI helped answer general questions about Django, web development concepts, best practices, and troubleshooting, acting like a virtual teacher.

This project was developed with the assistance of AI (GPT-5 & Gemini 3 Thinking), which served as a researcher and teacher throughout the process. AI helped provide explanations of networking concepts, client/server architecture, websockets, and Python libraries such as asyncio, as well as offering guidance on how to structure the server and the client.

The focus of this project was developing a network application. All code, project design, and implementation decisions were created and implemented independently. The HTML and CSS **styles** were generated with AI assistance (Gemini 3 Thinking) to provide a cleaner look. All javascript and python was independantly created. 