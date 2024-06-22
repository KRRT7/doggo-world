from requests import get
from random import randint
from numpy import ndarray
from rich import print
from pathlib import Path
if __name__ == "__main__":
    if "__compiled__" in globals():
        print("Running as compiled")
        array = ndarray((1000,1000))
        resps = []
        for i in range(randint(1,10)):
            resps.append(get("https://www.google.com").status_code)
        print(resps)
        print(array)
        for path in Path(".").iterdir():
            print(path)
    else:
        print("Running as script")