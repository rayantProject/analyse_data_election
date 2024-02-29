import os


def checkMergeFile():
    file = "dist/merged.csv"
    if os.path.exists(file):
        print("File exists")
        return True
    else:
        print("File does not exist")
        return False


def checkMergGeoFile():
    file = "dist/merged_geo.csv"
    if os.path.exists(file):
        print("File exists")
        return True
    else:
        print("File does not exist")
        return False
