## Requirements

- Python 3.x

## Getting Started

### Installation

1. Clone the repository:


2. Ensure you have Python 3.x installed on your machine.

## Usage

To start the server, run the `main.py` file with Python:
```sh
python main.py
```

By default, the server listens on 127.0.0.1:6379. You can change this by modifying the host and port variables in the start_server function.

Interacting with the Server
Once the server is running, you can interact with it using nc (netcat). In a new terminal window, run:

```sh
nc 127.0.0.1 6379
```

You can then start sending commands to the server, such as:
    ```sh

    SET key1 value1

    GET key1

    DEL key1

    EXPIRE key1 10

    TTL key1
    ```

It should create ```data.json``` file automatically for the data to persist