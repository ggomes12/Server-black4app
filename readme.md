<h1 style="text-align: center;">
  TCP Client-Server System
</h1>

This is a TCP client-server system that allows message exchange between a client and a server.


## Prerequisites

Make sure you have the following tools installed on your machine:

- IDE (Vscode, Pycharm etc.) or text editor of your choice
- Docker

## Git and GitHub Setup

1. Clone this repository:
    ```bash
   $ git clone https://github.com/ggomes12/Backend-project.git
    ```

2. Navigate to the project directory:
    ```bash
    $ cd tcp-client-server
    ```

## Building Docker Images

1. Make sure you have Docker installed on your machine.

2. Build the server and client images:
    ```bash
    $ docker build -t tcp-server -f Dockerfile.server .
    $ docker build -t tcp-client -f Dockerfile.client .
    ```

## Running the Server

1. Run the server container:
    ```bash
    $ docker run --network="host" -e SERVER_PORT=9000 tcp-server
    ```

## Running the Client

1. Run the client container, replacing `SERVER_IP` with the server's IP and `SERVER_PORT` with the server's port:
    ```bash
    $ docker run --network="host" -e SERVER_IP=127.0.0.1 -e SERVER_PORT=9000 -it tcp-client
    ```

## Interacting with the Operations

Upon starting the client, you will be presented with a menu of options. Select the desired operation by typing the corresponding number and pressing Enter. You will receive additional instructions as needed to interact with each operation.
