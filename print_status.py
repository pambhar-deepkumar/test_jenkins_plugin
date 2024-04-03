import random

def main():
    # List of possible outputs
    outputs = ["SUCCESS", "WARNING", "ERROR"]
    
    # Randomly choose one output
    selected_output = random.choice(outputs)
    
    # Print the selected output
    print(selected_output)

if __name__ == "__main__":
    main()
