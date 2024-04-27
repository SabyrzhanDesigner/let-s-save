from random import randint

def generateOldFile(numberOfRows):
    try:
        old_file = open('old_file.txt', 'w')
        [old_file.write(str(chr(randint(97,122)))*randint(0,20)+'\n') for _ in range(numberOfRows+1)]
        old_file.close()
    except Exception as e:
        print(e)

def rewriteNewFile():
    try:
        new_file = open('new_file.txt', 'w')
        new_file.close()

        new_file = open('new_file.txt', 'a')
        with open('old_file.txt', 'r') as old_file:
            for line in old_file:
                if len(line) > 7:
                    new_file.write(line)

        new_file.close()
    except Exception as e:
        print(e)

generateOldFile(10)
rewriteNewFile()