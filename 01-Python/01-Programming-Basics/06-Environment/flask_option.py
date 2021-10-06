# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    FLASK_ENV= ["development", "production"]
    if os.environ['FLASK_ENV'] == "development" or os.environ['FLASK_ENV'] == "production":
        return "Starting in development mode..."

    return "Starting in production mode..."

if __name__ == "__main__":
    print(start())
