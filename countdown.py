# countdown.py

def main():
    # Ask the user for a starting number
    start = int(input("Enter a number to start the countdown: "))
    
    # Repeat work with a while loop until start reaches 0
    while start > 0:
        print(start)
        start -= 1  # Decrement the counter
        
    print("Blastoff! 🚀")

if __name__ == "__main__":
    main()