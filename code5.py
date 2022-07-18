# TASK
# The included code stub will read an integer,n, from STDIN.
#
# Without using any string methods, try to print the following:
# 123...n
#
# Note that "..." represents the consecutive values in between.
#
# Example
# n=5
# Print the string 12345.

"""if __name__ == '__main__':
    n = int(input())

    if n >=1 and n <=150:
        a = range(1,n+1)

        for i in a:
            print(f"{i}", end ="")
"""

# burada end = ' ' argüman olarak bir sonraki yinelemeyi alacak ve aynı satırda yazdıracaktır.


if __name__ == '__main__':
    n = int(input())

    if n >=1 and n <=150:
        a = range(1,n+1)

        print(*a, sep="")

# Genel olarak, bunun gibi argümanlar iletirsiniz:
#
# function(arg1,arg2,arg3)
#
# Ancak, bunları aşağıdaki gibi bir listeye koyarsanız:
#
# function([arg1,arg2,arg3])
#
# o zaman sadece 1 argüman (liste) iletiyorsunuz ve fonksiyonun 3 argüman beklediğini ve sadece 1 argüman aldığını söyleyen bir hata alacaksınız.
#
# Öte yandan, * eklerseniz, listeyi "açar" (listenin bir bavul olduğunu ve öğelerin ayrı ayrı bakmak için yatağa koymak istediğiniz giysi parçaları olduğunu hayal edin.
#
# function(*[arg1,arg2,arg3])
# becomes
# function(arg1,arg2,arg3)
#
#
#
#
#



