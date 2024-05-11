from time import sleep
from src.db import get_client


if __name__ == "__main__":
    max_retries = 5
    retry = 0

    while retry < max_retries:
        try:
            get_client().tables.all()
            print("Connection successful with dynamo!")
            break

        except Exception as error:
            print(error)
            print(f"Trying again... attempt {retry}")
            sleep(1)
            retry += 1
