for i in range (0, 24):
    for j in range (0, 60):
        if (i == 0 and j == 0):
            print(i,":",j,"AM - Midnight")
        elif (i < 12):
            print(i,":",j,"AM")
        elif (i == 12 and j == 0):
            print(i,":",j,"AM - Noon")
        elif (i >= 12):
            print(i,":",j,"PM")