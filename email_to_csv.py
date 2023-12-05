import os
import csv
import re

word_group_palestine = ['palestine', 'palestinian', 'palestinians', 'arab', 'anti-palestinian', 'anti-palestine', 'anti-arab', 'gaza', 'gazan', 'gazans']
word_group_israel = ['israel', 'israeli', 'israelis', 'anti-israel', 'anti-israeli']
word_group_antisemitism = ['jewish', 'jew', 'jews', 'antisemitism', 'antisemitic', 'anti-jewish', 'anti-zionism']
word_group_islamophobia = ['muslim', 'muslims','anti-muslim', 'islamophobia', 'islamophobic', 'doxxing', 'doxing', 'doxxed', 'doxed', 'dox']
# to make an alternative graph, remove "doxxing" and its variants from last word group 

def count_words(text, word_group):
    """
    Count the occurrences of words in a given group within a text.
    """
    count = 0
    for word in word_group: # considers words as themselves (e.g. "word" wouldn't be counted in "swordfish")
        count += len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) # capitalization ignored
    return count

def process_file(file_path):
    """
    Process a single .txt file to calculate the data points.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    israel_count = count_words(text, word_group_israel)
    palestine_count = count_words(text, word_group_palestine)
    antisemitism_count = count_words(text, word_group_antisemitism)
    islamophobia_count = count_words(text, word_group_islamophobia)

    y_point = israel_count - palestine_count
    x_point = antisemitism_count - islamophobia_count

    return y_point, x_point

def process_all_files(folder_path):
    """
    Process all .txt files in a folder and output the results to a CSV file.
    """
    results = []
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            file_path = os.path.join(folder_path, file)
            y_point, x_point = process_file(file_path)
            admin_name = os.path.splitext(file)[0] # assume .txt name is the last name of the administrator
            results.append([admin_name, y_point, x_point])

    with open('compass_doxxed.csv', 'w', newline='', encoding='utf-8') as csvfile: # used csv module instead of pandas
        writer = csv.writer(csvfile)
        writer.writerow(['Administrator', 'State-related (Y-axis)', 'Religous-related (X-axis)'])
        writer.writerows(results)

folder_path = 'emails'
process_all_files(folder_path)

