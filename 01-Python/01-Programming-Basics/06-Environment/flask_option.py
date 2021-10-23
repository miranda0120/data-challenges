# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    # if os.environ.get('FLASK_ENV') == "development":
        # return "Starting in development mode..."
    # if os.environ.get('FLASK_ENV') == "production":
        # return "Starting in production mode..."
    # return "Starting in production mode..."

    env = os.getenv('FLASK_ENV')
    if env:
        return f"Starting in {env} mode..."
    return "Starting in production mode..."







if __name__ == "__main__":
    print(start())
