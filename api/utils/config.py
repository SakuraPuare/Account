# coding=utf-8
import os


def load_env() -> None:
    # Load environment variables from .env file
    with open('.env') as f:
        for line in f:
            line = line.strip()
            key, value = line[:line.find('=')], line[line.find('=') + 1:]
            os.environ[key] = value
