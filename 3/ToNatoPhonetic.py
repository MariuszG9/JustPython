import pandas as pd
import csv

# Loading a source with phonetic notation
source_phonetic = pd.read_csv('nato_phonetic_alphabet.csv')

# Dictionary comprehension - taking the dictionary entries from the columns (letter and pcode)
# and executing a loop that prints out 2 items at a time through the rows
nphonetic_dict = {myrow.letter: myrow.pcode for (index, myrow) in source_phonetic.iterrows()}
print(nphonetic_dict)

# We can achieve the same thing using normal notation by extending the code. DC is shorter and easier to read quickly
# nphonetic_dict = {}
# for index, myrow in source_phonetic.iterrows():
#    nphonetic_dict[myrow.letter] = myrow.pcode

print(f'\nCould you enter a word? Local letters not allowed ')
user_word = input('Word: ').upper()
recoded_value = [nphonetic_dict[letter] for letter in user_word]
print(recoded_value)

# Same as DC, only here we have LC
# recoded_value = []
# for letter in user_word:
#     recoded_value.append(nphonetic_dict[letter])

# CSV filename
filename = 'NPA-values.csv'

# Save to CSV
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file, delimiter='-')
    writer.writerow(recoded_value)

print('List saved to', filename)

# Same as csv.writer, only here we have pandas version
# Creating a DataFrame from a list
# df = pd.DataFrame({'NPA-values': ['-'.join(recoded_value)]})

# Saving a DataFrame to a CSV file
# filename = 'NPA-values.csv'
# df.to_csv(filename, index=False)
