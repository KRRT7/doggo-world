from requests import get
from random import randint

if __name__ == "__main__":
    if "__compiled__" in globals():
        print("Running as compiled")
        for i in range(randint(1,10)):
            print(get("https://www.google.com").status_code)
    else:
        print("Running as script")