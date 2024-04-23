import random

def main():
    # SAmple List of possible outputs
    outputs = ["OK", "WARNING - Pipeline 1 exceeded the time limit", "ERROR - Pipeline 1,2,3,4 exceeded the time limit"]
    
    # Randomly choose one output
    selected_output = random.choice(outputs)
    raise 
    # Print the selected output
    print(selected_output)

if __name__ == "__main__":
    main()
