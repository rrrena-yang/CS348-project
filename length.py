import csv

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = 'top_10000_1960-now.csv'

# Initialize a dictionary to keep track of the maximum length for each column
max_lengths = {
    "Track URI": 0,
    "Track Name": 0,
    "Artist URI(s)": 0,
    "Artist Name(s)": 0,
    "Album URI": 0,
    "Album Name": 0,
    "Album Artist URI(s)": 0,
    "Album Artist Name(s)": 0,
    "Album Release Date": 0,
    "Album Image URL": 0,
    "Disc Number": 0,
    "Track Number": 0,
    "Track Duration (ms)": 0,
    "Track Preview URL": 0,
    "Explicit": 0,
    "Popularity": 0,
    "ISRC": 0,
    "Added By": 0,
    "Added At": 0,
    "Artist Genres": 0,
    "Danceability": 0,
    "Energy": 0,
    "Key": 0,
    "Loudness": 0,
    "Mode": 0,
    "Speechiness": 0,
    "Acousticness": 0,
    "Instrumentalness": 0,
    "Liveness": 0,
    "Valence": 0,
    "Tempo": 0,
    "Time Signature": 0,
    "Album Genres": 0,
    "Label": 0,
    "Copyrights": 0
}

# Open the CSV file and read it
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV
    for row in reader:
        for column in max_lengths.keys():
            # Update the max length for each column if the current value is longer
            if len(row[column]) > max_lengths[column]:
                max_lengths[column] = len(row[column])

# Print the maximum lengths of each column
for column, length in max_lengths.items():
    print(f"Maximum length of '{column}': {length}")
