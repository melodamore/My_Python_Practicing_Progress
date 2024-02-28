# Raw Strings

# This is an ordinary string printing
print('C:\Program Files\fnord\foo\bar\baz\frozz\bozz')
# Output:
"""
C:\Program Files
                nord
                    oaaz
                        rozozz
"""

# This is a raw string printing
print(r'C:\Program Files\fnord\foo\bar\baz\frozz\bozz')
# Output: C:\Program Files\fnord\foo\bar\baz\frozz\bozz

print(r'C:\Program Files\fnord\foo\bar\baz\frozz\bozz' '\\')
# Output: C:\Program Files\fnord\foo\bar\baz\frozz\bozz\
