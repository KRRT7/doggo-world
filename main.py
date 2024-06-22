if __name__ == "__main__":
    if "__compiled__" in globals():
        print("Running as compiled")
    else:
        print("Running as script")