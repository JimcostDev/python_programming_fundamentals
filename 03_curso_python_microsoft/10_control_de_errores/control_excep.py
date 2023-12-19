
def main():
     try:
        open('config.txt')
     except FileNotFoundError as err:
        print("Couldn't find the config.txt file!", err)
     except PermissionError:
        print("Found config.txt but it is a directory, couldn't read it")
     except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")
   
if __name__ == '__main__':
    main()

