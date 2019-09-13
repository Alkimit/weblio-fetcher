import fetch
import csv

if __name__ == "__main__":
    # Read word list and parse
    vocabfile = open("words.txt", "r")
    definitions = list()
    for vocab in vocabfile:

        result = fetch.fetchSource(vocab)
        try:
            # TODO: Fix inconsistent/empty returns from website
            definitions.extend(result)
        except:
            print("Error parsing " + vocab)
            continue
        definitions.append("\n")
        print(result)

    # CSV Export
    with open('test_output.csv', mode='w') as test_file:
        test_writer = csv.writer(test_file, dialect='excel', delimiter=',', quoting=csv.QUOTE_NONE, escapechar=' ')
        test_writer.writerow(definitions)

