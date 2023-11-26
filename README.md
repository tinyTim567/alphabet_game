# Number "Game"

## Inspiration
The alphabet, a seemingly ordinary collection of 26 letters, possesses a profound ability to inspire and unlock boundless creativity within me. Each letter represents not just a sound but a gateway to expression, communication, and imagination. As I navigate through the intricate dance of vowels and consonants, I am reminded of the endless possibilities they offer in forming words, sentences, and stories. The simplicity of the alphabet belies its transformative power—it is a foundation upon which ideas are built, a palette with which I paint the canvas of language. In the elegant dance of letters, I find inspiration to construct narratives, share ideas, and connect with others. The alphabet is not merely a tool for communication; it is a source of endless fascination, a catalyst for the creative spark that propels me to explore the vast landscape of language with awe and wonder.

## What it does
This code consists of a simple alphabet validation game with a graphical user interface (GUI) using the Tkinter library in Python. The GUI prompts the user to input alphabets, validating and responding to the correctness of the input by communicating with a server implemented in a separate script. The server, established using the socket module, tracks the user's progress in traversing the alphabet forwards and backward, providing feedback on correctness and updating the user's score. The game loop continues until an incorrect input is received, at which point the server sends a concluding message. The client script, integrated into the GUI code, uses a "client" module to validate user inputs and handle game logic. The GUI includes buttons, labels, and entry fields for user interaction. Overall, this code creates an interactive alphabet game interface with a client-server architecture.

## How we built it
Python

## Challenges we ran into
Tkinter and Sockets

## Accomplishments that we're proud of
Nothing

## What we learned
Never again

## What's next for Alphabet Game
Numbers