def route(source,destination):
    b=[]
    for i in range(len(source)):
        if source[i] in Zone_A and dest[i] in Zone_A:
            b.append("A")
        elif source[i] in Zone_B and dest[i] in Zone_B:
            b.append("B")
        elif source[i] in Zone_C and dest[i] in Zone_C:
            b.append("C")
        elif source[i] in Zone_A and dest[i] in Zone_B or source[i] in Zone_B and dest[i] in Zone_A  :
            b.append("AB")
        elif source[i] in Zone_B and dest[i] in Zone_C or source[i] in Zone_C and dest[i] in Zone_B:
            b.append("BC")
        else:
            b.append("ABC")
    return b



Zone_A=["EFG","GHI"]        
Zone_B=["CDE","IJK"]
Zone_C=["ABC","KLO"]
source=["CDE","EFG"]
dest=["GHI","KLO"]
print(route(source,dest))