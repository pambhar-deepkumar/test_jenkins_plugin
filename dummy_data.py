import csv
import random

# Parameters
num_builds = 50  # Number of builds to simulate
min_time = 5     # Minimum build time in minutes
max_time = 20    # Maximum build time in minutes
csv_file_path = 'build_times.csv'  # Output CSV file path

# Generate random build times
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['BuildNumber', 'BuildTime'])  # Header

    for build_number in range(1, num_builds + 1):
        build_time = random.randint(min_time, max_time)
        writer.writerow([build_number, build_time])

print(f'Dummy data generated in {csv_file_path}')
