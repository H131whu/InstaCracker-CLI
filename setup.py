import os 

print("Choose your Operating System")
print("1. Arch Linux")
print("2. Termux")
print("3. Ubuntu")
print("4. Windows")
print("5. Others")
a = int(input("--> "))
if a == 1:
    print('Installing...')
    os.system("sudo pacman -S --needed base-devel git")
    os.system("git clone https://aur.archlinux.org/yay.git")
    os.system('cd yay')
    os.system('makepkg -si')
    o.system('sudo pacman -S python-requests')
    os.system('sudo pacman -S python-typer')
    os.system("yay -S python-inquirer")
    os.system('sudo pacman -S python-tabulate')
    os.system('sudo pacman -S python-colorama')
    print('done!')
    os.system("python3 app.py")
elif a == 2:
    print('Installing...')
    os.system('pip install typer')
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('pip install inquirer')
    os.system('pip install tabulate')
    print('done!')
    os.system("python3 app.py")
elif a == 3:
    print('Installing...')
    os.system('pip install typer')
    os.system('pip install colorama')
    os.system('pip install requests')
    os.system('pip install inquirer')
    os.system('pip install tabulate')
    print('done!')
    os.system("python3 app.py")
elif a == 4:

    print('Installing...')
    os.system('pip install typer')
    os.system('pip install inquirer')
    os.system('pip install colorama')
    os.system('pip install tabulate')
    print('done!')
    os.system("python3 app.py")
else:
    print('Installing...')
    os.system('pip install typer')
    os.system('pip install requests')
    os.system('pip install inquirer')
    os.system('pip install tabulate')
    os.system('pip install colorama')
    print('done!')
os.system("python3 app.py")
