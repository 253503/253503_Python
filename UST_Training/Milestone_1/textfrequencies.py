import pandas as pd

# Read the CSV file
file_path = 'novel.csv'  
df = pd.read_csv(file_path)

# Initialize a dictionary 
word_counts = {}

# Loop through each text entry in the CSV file
for text in df['story']:  
   
   # Split the text into words
    words = text.split()

    # Count the frequency of each word using if-else
    for word in words:
        if word in word_counts:
            word_counts[word] += 1 
        else:
            word_counts[word] = 1

# Create a DataFrame from the word counts
frequency_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])

#  Display the DataFrame with word frequencies
print(frequency_df)