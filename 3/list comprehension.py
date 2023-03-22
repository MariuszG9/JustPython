# podstawowa LC oparta na liczbach
numbers = [1, 3, 5, 7, 9]
numbers_list = [num+1 for num in numbers]
print(numbers_list)
print('\n')

# podstawowa LC oparta na stringach
my_name = "Mariusz"
letters = [letter for letter in my_name]
print(letters)
print('\n')

# podstawowa LC oparta na zakresie
this_range = [num/2 for num in range(1, 11)]
print(this_range)
print('\n')

# lista LC z warunkiem długości ciągu tekstowego
animals = ["Kangur", 'Pies', "Ryba", 'Papuga', 'Tygrys']
four_char_animals = [animal for animal in animals if len(animal) == 4]
print(four_char_animals)
print('\n')

# lista LC wypisująca liczby gdzie modulo 6 = 0
numbers_x = list(range(1, 100))
numbers_mod = [num for num in numbers_x if num % 6 == 0]
print(numbers_mod)
print('\n')

# wykorzystanie LC do uzyskania kwadratów tylko dla niepowtarzających się liczb
numbers = [1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15]
sq_numbers = [num * num for num in numbers if numbers.count(num) == 1]
print(sq_numbers)
print('\n')

# wykorzystanie LC do uzyskania unikalnych sześcianów z wykorzystaniem enumarate (do uzyskania indeksów elementów)
numbers = [1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15]
cub_numbers_uniq = [num**3 for i, num in enumerate(numbers) if numbers.index(num) == i]
print(cub_numbers_uniq)
print('\n')

# lista LC z małymi literami
animals = ["Kangur", 'Pies', "Ryba", 'Papuga', 'Tygrys']
four_char_animals = [animal.lower() for animal in animals if len(animal) > 4]
print(four_char_animals)
print('\n')

# rysunek choinki z użyciem LC
[print(' ' * (3-i) + '*' * (2*i+1)) for i in range(4)]
print('\n')


# utworzenie NOT IN z wykorzystaniem LC
dataset_1 = list(range(1, 12, 2))
dataset_2 = [1, 2, 6, 7, 8]
data_in = [num for num in dataset_1 if num not in dataset_2]
print(data_in)
print('\n')

# konwersja listy list na listę płaską
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [item for sublist in nested for item in sublist]
print(flat)
print('\n')

# znalezienie najdłuższego słowa w sentencji
sentence = "Królik pobiegł za bezpańskim kotem aby odnaleźć kolekcję kartek"
longest = max([word.strip(",.") for word in sentence.split()], key=len)
print(longest)
print('\n')

# suma liczb w liście
numbers = [1230, 4561, 7892]
sum_of_numbers = sum(int(num) for num in numbers) # krócej oczywiście można: sum_of_numbers = sum(numbers)
print(f"{sum_of_numbers:,}".replace(",", " "))
print('\n')

# suma cyfr w liście
digits = [1230, 4561, 7892]
sum_of_digits = sum(int(digit) for num in digits for digit in str(num))
print(sum_of_digits)
print('\n')

