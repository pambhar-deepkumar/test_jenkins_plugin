import random

def main():
    raise Exception("Raised")
    # List of possible outputs
    outputs = ["SUCCESS", "WARNING", "ERROR"]
    
    # Randomly choose one output
    selected_output = random.choice(outputs)
    raise 
    # Print the selected output
    print(selected_output)

if __name__ == "__main__":
    main()
