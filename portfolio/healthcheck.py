"""Portfolio healthcheck template; does not print secret values."""
import os
REQUIRED = []
def check(required=REQUIRED):
    return {name: bool(os.getenv(name)) for name in required}
if __name__ == "__main__":
    print(check())
