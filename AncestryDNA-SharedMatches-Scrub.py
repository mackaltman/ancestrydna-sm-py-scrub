# import packages
import requests, csv
from bs4 import BeautifulSoup

# output location
outputLoc = 'shared-connections.csv'

# import file
fileName = open('shared-connections.html')
soup = BeautifulSoup(fileName)

# instantiate list
matches = []

#for match in soup.select('match-entry'):
for match in soup.select('match-entry'):
    # instantiate compRow
    matchRow = []

    # identify user name and url
    matchUser = match.select('a.userCardTitle')[0]
    matchName = matchUser.getText()
    matchId = matchUser.get('href').split('/with/')[1]

    # identify shared dna
    matchDNA = match.select('span.dnaGrayDark')[0].getText().split(": ")[1]

    matchRow = [matchName, matchId, matchDNA]

    matches.append(matchRow)

# create results file
outputFile = open(outputLoc, 'w')
outputWriter = csv.writer(outputFile)

# iterate through list and write to file
for match in matches:
    outputWriter.writerow(match)

# close output file
outputFile.close()
