"""
    Implemetn a group by owner
    accept a dictionary containing the file owner name for each file name
    returns a dictionary contaning a list of file names for each ownername
    https://www.testdome.com
    https://www.python-course.eu/python3_history_and_philosophy.php
    https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
    https://docs.python.org/3/library/functions.html#type
"""

class FileOwners:

    @staticmethod
    def group_by_owners(files):
        result = {}
        for file, owner in files.items():
            result[owner] = result.get(owner, []) + [file]

        return result


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))