import pandas as pd
import matplotlib.pyplot as plt

def generate_csv():
    # Sample data for CSV
    data = {
        "Name": ["John", "Anna", "Peter", "Linda"],
        "Age": [28, 34, 29, 32],
        "City": ["New York", "Paris", "Berlin", "London"]
    }
    
    df = pd.DataFrame(data)
    
    # Generate CSV
    csv_filename = "sample_data.csv"
    df.to_csv(csv_filename, index=False)
    print(f"{csv_filename} has been generated.")

def generate_png():
    # Sample data for PNG
    x = [1, 2, 3, 4]
    y = [10, 20, 25, 30]
    
    plt.figure()
    plt.plot(x, y, label='Sample Data')
    plt.title('Sample Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    
    # Generate PNG
    png_filename = "sample_plot.png"
    plt.savefig(png_filename)
    print(f"{png_filename} has been generated.")
    
if __name__ == "__main__":
    generate_csv()
    generate_png()
