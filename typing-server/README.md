Typing UI Flask App
=================

Restful API for generating text typing videos of the Typist AI. Given any sentence and keyboard layout the AI model generates a human-like typing behaviour.

Usage
-----

Clone the repo:

    git clone https://github.com/aditya02acharya/TypingUI-lite.git
    cd TypingUI-lite/typing-server

Create virtualenv:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Run the sample server

    python api.py

Try the endpoints:

    curl -XPOST -H "Content-Type: application/json" http://localhost:5000/hello -d '{"sentence": "Hello"}'


License
-------

MIT, see LICENSE file
