import sys
import argparse

class CookieInstance:
    """
    A new CookieInstance object with which to call the methods to process the
    list of cookies on.
    """
    def __init__(self):
        """
        Initializes the CookieInstance, creates a csvFile to contain the csv file,
        a map of cookies containing which dates correspond to which cookies,
        a list of highest occuring cookies, sorted using bucket sort
        """
        self.csvFile = []
        self.mapOfCookies = {}
        self.listOfOccurences = []

    def readInCSV(self, fileName):
        """
        Input: The fileName of the CSV file
        Output: An array containing the contents of the CSV file
        """
        try:
            with open(fileName, 'r') as csv:
                csvFile = []
                for row in csv:
                        entries = row.split(',')
                        csvFile.append((entries[0], entries[1]))
            self.csvFile = csvFile
            return(0)
        except IOError:
            print('Oops, ',fileName,' is not a valid filename, try again!')
            return(1)

    def updateMapOfCookies(self):
        """
        Input: The cookie instance
        Output: Updates the cookie instacne to contain the CSV information. 
                The keys contain the dates, and the values contain the cookies.
        """
        dictionary = {}
        for i in range(len(self.csvFile)):
            if(i != 0):
                currentKey = self.csvFile[i][1]
                currentKey = currentKey[0: currentKey.index('T')]
                currentValue = self.csvFile[i][0]
                if currentKey not in dictionary:
                    dictionary[currentKey] = [currentValue]
                else:
                    dictionary[currentKey] = dictionary[currentKey] + [currentValue]
        self.mapOfCookies = dictionary
        return(0)


    def findOccurences(self, date):
        """
        Input: A date to find the cookies on that given day.
        Output: Update the cookie instance's listOfOccurences to contain
                an array of cookies on that given date, sorted using bucket sort
        """
        # Make a dictionary, containing the number of times each cookie occurs
        occurences = {}
        try:
            for cookie in self.mapOfCookies[date]:
                if cookie not in occurences:
                        occurences[cookie] = 1
                else:
                    occurences[cookie] += 1
        except Exception as e:
            print('Oops, ',date,' is not a valid date, try again!')
            return(1)

        # Put the values in the dictionary in a new array using bucket sort
        bucket = [[]] * (len(occurences) + 1)
        for cookie in occurences:
            value = occurences[cookie]
            if bucket[value] == []:
                bucket[value] = [cookie]
            else:
                bucket[value] = bucket[value] + [cookie]
        self.listOfOccurences = bucket
        return(0)


    def returnMax(self):
        """
        Input: A cookie instance with a listOfOccurences
        Output: Prints the most frequent cookie/cookies if there is a tie.
        """
        for i in range(len(self.listOfOccurences) - 1, -1, -1):
            if(self.listOfOccurences[i] != []):
                for item in self.listOfOccurences[i]:
                    print(item)
                return(0)
        print("There were no cookies present.")
        return(1)

    def runScript(self, fileName, date):
        """
        Input: A cookie instance, the required fileName, and the date
        Output: Updates the cookie to hold the CSV file, the dictionary, the bucket
                sorted dictionary, and then prints from the bucket sorted array the highest
                occurences.
        """
        if(self.readInCSV(fileName) == 0):
            if(self.updateMapOfCookies() == 0):
                if(self.findOccurences(date) == 0):
                    self.returnMax()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--date', type=str, required=True)
    parser.add_argument('fileName')
    args = parser.parse_args()
    cookies = CookieInstance()
    cookies.runScript(args.fileName, args.date)
