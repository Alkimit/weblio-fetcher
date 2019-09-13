import fetch
import csv

if __name__ == "__main__":
    # Read word list and parse
    vocabfile = open("words.txt", "r")

    # Open CSV file
    with open('test_output.csv', mode='w') as test_file:
        test_writer = csv.writer(test_file, dialect='excel', escapechar=' ', quoting=csv.QUOTE_NONE)
        for vocab in vocabfile:
            # Returns string/list of definitions for each word in the list (+debug print)
            result = fetch.getDefinition(vocab)
            print(result)

            # CSV Export
            test_writer.writerow(result)

