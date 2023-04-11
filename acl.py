aclnum = int(input("cual es el número ipv4 acl? "))

if aclnum >= 1 and aclnum <= 99:
    print("este es un acl ipv4 estándar.")
elif aclnum >= 100 and aclnum <= 199:
    print("este es una acl ipv4 extendida.")
else:
    print("el número no corresponde a una lista de acceso.")