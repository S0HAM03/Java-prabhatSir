# # # What is File Handling?
# # # File handling in Python allows you to read, write, append, and modify files stored on your system.
# # #
# # # Python provides built-in functions and a powerful with statement to manage file operations safely and efficiently.
# #
# # # | Mode  | Description                       |
# # # | ----- | --------------------------------- |
# # # | `'r'` | Read (default)                    |
# # # | `'w'` | Write (overwrites file)           |
# # # | `'a'` | Append (adds to end)              |
# # # | `'x'` | Create new file (error if exists) |
# # # | `'b'` | Binary mode                       |
# # # | `'t'` | Text mode (default)               |
# #
# #
# #
# # ###############
# # # . 1)Writing to a File (Overwrites existing)
# # #
# # with open("PCU1234.txt", "w") as f:
# #     f.write("PUNE ,SOLAPUR,INDIA,USA,UK .")
# #
# # #2
with open("PCU.txt", "r") as f:
    content = f.read()
    print(content)
# # #
# #
# #
# # #3Appending to a File
# # with open("file123.txt", "a") as f:
# #     f.write("\ntrinffhbn,vhdjjfdhjhhhdmbvhtyfhdyuthdggfhdyk.")
# #
# #
# # #4Reading Line-by-Line
with open("file123.txt", "r") as f:
    for line in f:
        print(line)
        print(line.strip())  # .strip() removes newline
# #
# # #File Existence & Deletion (using os)
import os

if os.path.exists("file12.txt"):
    os.remove("file12.txt")
    print("File delete d.")
else:
    print("File does not exist.")
# #
# #
# # ## Example: Count Words in a File
with open("file123.txt", "r") as f:
    content = f.read()
    words = content.split()
    print( "Total words:", len(words))
# #
# #
# #
# #
file=open("file123.txt",'r')
cont=file.read()
print(cont)
file.close()
# # #
# #
# #
# # #
file=open("data.txt","a")
file.write("\nthis is new line code")
file.close()
# #
# #
# # # with opne("student.txt","w") as file:
# # #     file.write("zjbfjhbfjhjb")
# # #     file.write("djhfsdjhfbsh")
# #
