import getpass
import repl
import sys

def main():
    print("Hello %s! This is the Monkey programming language!" % (getpass.getuser()))
    print("Feel free to type in commands")

    repl.Start(sys.stdin, sys.stdout)

if __name__ == "__main__":
    main()