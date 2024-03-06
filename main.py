import random

male = 'male' # This one croaks
female = 'female' # This one will save us

def getRandomFrog():
    return random.choice([male,female])
def twoRandomFrogs():
    return getRandomFrog(), getRandomFrog()

print('Hello! We are going to simulate the frog riddle from ted ed. https://www.youtube.com/watch?v=cpwSGsb-rTs')
print('The riddle claims we have a 67% survival chance if we lick two frogs. Lets see if thats true.')

numTests = 10000
numValidTests = 0
timesSurvived = 0
# perform this test a lot of times and run an average
for _ in range(numTests):
    frogs = twoRandomFrogs()
    # I hear a croak, so invalidate test if they are both female
    if not (frogs[0] == female and frogs[1] == female):
        numValidTests += 1
        # For valid senarios, lick both frogs, if either is female, you live!
        if frogs[0] == female or frogs[1] == female:
            timesSurvived += 1
percentSurvived = timesSurvived/numValidTests
print(f'Well looks like we survived {round(percentSurvived*100,0)}% of the time. Wow looks like ted ed was right.')