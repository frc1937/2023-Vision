import os

os.chdir('C:\\Users\\itayo\\Charged_Up_2023_Vision\\straight_cones')
print(os.getcwd())

for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "cone" + str(count+1)

    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)