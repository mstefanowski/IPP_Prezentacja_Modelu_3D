def file_loader():
    wierzcholki = []
    polygon_list = []
    f = open("minecraft-steve.obj", "r")
    for x in f:
        if x.startswith("v "):
            wierzcholek = []
            a = x.split()
            a[-1] = a[-1].strip()
            for i in range(3):
                wierzcholek.append(float(a[i+1]))
            wierzcholki.append(wierzcholek)
        if x.startswith("f"):
            polygon = []
            a = x.split()
            for i in range(1, len(a)):
                a[i] = a[i].split("/")[0]
                index_wierzcholka = int(a[i]) - 1
                polygon.append(wierzcholki[index_wierzcholka])
            polygon_list.append(polygon)
    print(polygon_list)        
    f.close()
file_loader()


