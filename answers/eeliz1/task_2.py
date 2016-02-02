def cheer():
    print("%s: Who do we appreciate?" % (list(range(2, 10, 2))))


#by naming the main function, we ensure that the function will run anytime the code is run as a script, but not when imported#
if __name__ == "__main__":
    cheer()
