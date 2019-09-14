import weblio_fetch
import tatoeba_fetch
import csv

if __name__ == "__main__":
    # Read word list and parse
    vocabfile = open("words.txt", "r")

    # Open CSV file
    with open('test_output.csv', mode='w') as test_file:
        test_writer = csv.writer(test_file, dialect='excel', escapechar=' ', quoting=csv.QUOTE_NONE)
        for vocab in vocabfile:
            # Returns string/list of definitions for each word in the list (+debug print)
            weblio_result = weblio_fetch.getDefinition(vocab)
            if weblio_result == (-1) or weblio_result == (-2):
                weblio_result = list()
                weblio_result.append("Error finding definition")
                
            # TODO: Retry definition search due to randomization
            #elif weblio_result == (-2):

            tatoeba_result = tatoeba_fetch.getSentence(vocab)

            result = list()
            result.append(tatoeba_result)
            result.extend(weblio_result)
            #debug
            print(weblio_result)

            # CSV Export
            test_writer.writerow(result)

