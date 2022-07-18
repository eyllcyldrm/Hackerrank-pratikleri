# x,y,z ve n i integer olarak kullanıcıdan al.
# x, y, z için mümkün tüm arrayleri oluştur.
# x + y + z toplamı n e eşit olamayan tüm arrayleri elde et

if __name__ == '__main__':

    x, y, z, n = (int(input()) + 1 for _ in range(4))
    liste = []
    for a in range(x):
        for b in range(y):
            for c in range(z) :
                if a+b+c != n-1:

                    liste.append([a,b,c])

    print(liste)











