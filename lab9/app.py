import os
import sys

name = os.getenv("USER_NAME", "Student")

if len(sys.argv) > 1 and sys.argv[1] != "--serve":
    name = sys.argv[1]

if "--serve" in sys.argv:
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return f"Hello from my Docker container! Hello, {name}!"

    app.run(host="0.0.0.0", port=5000)
else:
    print("Hello from my Docker container!")
    print(f"Hello, {name}!")
