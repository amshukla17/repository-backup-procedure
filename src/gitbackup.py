#!/usr/bin/python3

import csv
from datetime import datetime
import os
import sys
import urllib.request

# ToDo: Add help message for command line areguments.

REPO_LIST_OPTION = sys.argv[1]  # csv,g-sheet
REPO_LIST_ADDRESS = sys.argv[2]
PATH_TO_CLONE = sys.argv[3]

def logSeparator():
    """Print seperator line."""
    print('\n' + '-'*80 + '\n')

def guessFolderName(repoUrl):
    """This funcation return expected folder name after clone
    repository."""
    return repoUrl.split('/')[-1]

def getFullUrlForGoogleSheet(sheetId, sheetName='repositories'):
    """Returns spreadsheet csv export compatible export url."""
    return f'https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}'

def cloneBareRepository(path, repoUrl):
    """cloneBareRepository: is used when we want to clone a bare
    repository on the given path.

    path: takes path of the filesystem to clone repository inside it.

    repoUrl: Provide your repo url to clone from the given url
    i.e. user@www.example.com:user/test.git
    """
    cloneCmd = 'git clone --bare ' + repoUrl
    # Change directory
    os.chdir(path)
    # Clone the repository
    os.system(cloneCmd)

def fetchBareRepository(pathToRepo):
    """Executes fetch all for the already --bare cloned repositories."""
    fetchCmd = 'git fetch --all'
    # change the pwd path
    os.chdir(pathToRepo)
    # fetch all with lfs
    os.system(fetchCmd)

def cloneOrFetchNow(path, repoUrl):
    """This method confirms backup is processed properly for given repository.

    path: takes path of the filesystem to clone repository inside it.

    repoUrl: Provide your repo url to clone from the given url
    i.e. user@www.example.com:user/test.git

    returns if clone performed OR fetch performed for given repository.
    """
    folderName = guessFolderName(repoUrl)
    pathToRepo = '/'.join([path, folderName])
    operation = 'error'

    if os.path.exists(pathToRepo):
        # Fetch new changes
        fetchBareRepository(pathToRepo)
        operation = 'fetch'
    else:
        # New clone repository
        cloneBareRepository(path, repoUrl)
        operation = 'clone'

    return operation

def backupFromCSV(filePath):
    """Reads csv file from given path and make sures backup is stored for
    listed reposities in the given filePath.
    """
    cloneCount = fetchCount = failCount = 0
    with open(filePath, mode='r') as csv_file:
        for repository in csv.DictReader(csv_file):
            try:
                operation = cloneOrFetchNow(PATH_TO_CLONE, repository['URL'])
                if operation == 'error':
                    failCount += 1
                elif operation == 'clone':
                    cloneCount += 1
                elif operation == 'fetch':
                    fetchCount += 1
                else:
                    print("Check repository " + repository['URL'] +
                          "for operation " + operation + ".")
            except Exception as error:
                print(error)
                failCount += 1
    return cloneCount, fetchCount, failCount

def backupFromGoogleSheet(fileUri):
    """Reads google spreadsheet file from given path and make sures backup
    is stored for listed reposities in the given fileUri.
    """
    cloneCount = fetchCount = failCount = 0
    sheetResponse = urllib.request.urlopen(fileUri)
    sheetLines = [l.decode('utf-8') for l in sheetResponse.readlines()]
    for repository in csv.DictReader(sheetLines):
        try:
            operation = cloneOrFetchNow(PATH_TO_CLONE, repository['URL'])
            if operation == 'error':
                failCount += 1
            elif operation == 'clone':
                cloneCount += 1
            elif operation == 'fetch':
                fetchCount += 1
            else:
                print("Check repository " + repository['URL'] +
                      "for operation " + operation + ".")
        except Exception as error:
            print(error)
            failCount += 1
    return cloneCount, fetchCount, failCount

def startBackupProcess(
        listOption=REPO_LIST_OPTION, listAddress=REPO_LIST_ADDRESS):
    """Handels backup procedure for all repository."""
    if listOption == 'csv':
        return backupFromCSV(listAddress)
    elif listOption == 'g-sheet':
        return backupFromGoogleSheet(
            getFullUrlForGoogleSheet(listAddress)
        )
    else:
        raise "Not supported option:" + listOption

def main():
    """Main method of the procedure."""
    logSeparator()
    print(f'Backup START: {datetime.now()}\n')
    cloneCount, fetchCount, failCount = startBackupProcess()
    print(f'Processed clone for #{cloneCount} repositories.')
    print(f'Processed fetch for #{fetchCount} repositories.')
    print(f'Failed #{failCount} repositories.')
    print(f'\nBackup END: {datetime.now()}')
    print(
        f'\nBACKUP COMPLETED {"WITH ISSUE" if failCount else "SUCCESSFULLY"}!')
    logSeparator()

if __name__ == '__main__':
    main()
