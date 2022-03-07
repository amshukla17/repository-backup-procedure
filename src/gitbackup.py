#!/usr/bin/python3

import csv
import sys
import os
from datetime import datetime

now = datetime.now()


REPO_LIST_FILE = sys.argv[1]
PATH_TO_CLONE = sys.argv[2]

def guessFolderName(repoUrl):
    """This funcation return expected folder name after clone
    repository."""
    return repoUrl.split('/')[-1]

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

def main():
    """Main method of the procedure."""
    print('\n\n' + '-'*80)
    print('Backup START:', datetime.now())
    with open(REPO_LIST_FILE, mode='r') as csv_file:
        csvReader = csv.DictReader(csv_file)
        cloneCount = fetchCount = failCount = 0

        for row in csvReader:
            #try:
            if 1:
                operation = cloneOrFetchNow(PATH_TO_CLONE, row['URL'])
                if operation == 'error':
                    failCount += 1
                elif operation == 'clone':
                    cloneCount += 1
                elif operation == 'fetch':
                    fetchCount += 1
                else:
                    print(
                        "Check repository " + row['URL'] +
                        "for operation " + operation + ".")
            #except Exception as e:
            #    print(e)
            #    failCount += 1

        print(f'Processed clone for #{cloneCount} repositories.')
        print(f'Processed fetch for #{fetchCount} repositories.')
        print(f'Failed #{failCount} repositories.')
    print('Backup END:', datetime.now())
    if failCount == 0:
        print('\nBACKUP SUCCESSFULLY COMPLETED!')
    print('-'*80)

if __name__ == '__main__':
    main()