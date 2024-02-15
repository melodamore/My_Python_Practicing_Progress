# Slicing

name = 'Daniel'

# SLICING THE 1ST CHARACTERS & PRINTING THE LAST ONES

no_0_name = name[1:]
no_0to1_name = name[2:]
no_0to2_name = name[3:]
no_0to3_name = name[4:]
no_0to4_name = name[5:]
last_3_name = name[len(name)-3:]

print(name)  # Output: Daniel
print(no_0_name)  # Output: aniel
print(no_0to1_name)  # Output: niel
print(no_0to2_name)  # Output: iel
print(no_0to3_name)  # Output: el
print(no_0to4_name)  # Output: l
print(last_3_name)  # Output: iel

# SLICING THE LAST CHARACTERS & PRINTING THE 1ST ONES

no_5_name = name[:-1]
no_5to4_name = name[:-2]
no_5to3_name = name[:-3]
no_5to2_name = name[:-4]
no_5to1_name = name[:-5]


print(no_5_name)  # Output: Danie
print(no_5to4_name)  # Output: Dani
print(no_5to3_name)  # Output: Dan
print(no_5to2_name)  # Output: Da
print(no_5to1_name)  # Output: D
