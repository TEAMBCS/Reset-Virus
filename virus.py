import platform
b = platform.architecture()[0]
if b == '64bit':
    import reset_virus
    reset_virus.BCS()
else:
     print("\033[1;32m\033[1m32bit\033[0m\033[1;31m\033[1m Not Supported!")
