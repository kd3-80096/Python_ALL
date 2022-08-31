def russiandoll(doll):
    if doll==1:
        print("All the dools are opened")
    else:
        print("Opening doll number",doll)
        russiandoll(doll-1)

russiandoll(5)