# FOR DÖNGÜSÜ ÇALIŞMA PRENSİBİ:

list = [1,2,3,4]

list_iterator = list.__iter__()

while True:
    try:
        num = list_iterator.__next__()
        print(num)
    except StopIteration:
        break



testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))