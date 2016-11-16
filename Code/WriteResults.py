import csv

"""
This module is always available. It provides access to the
write csv functions.
"""

def write_csv(file_name, predicted_results):
    """
    Write csv
    :return: void, write predicted results in csv file
    """
    with open('../SubmisionResults/' + file_name + '.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile,
                                quotechar=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['ImageId'] + ['Label'])

        for i in range(len(predicted_results)):
            spamwriter.writerow([i+1] + [predicted_results[i]])

