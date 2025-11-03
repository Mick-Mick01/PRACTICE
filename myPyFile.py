from pathlib import Path

myFile = Path(__file__)

dirName = myFile.parent.resolve()

print(dirName)