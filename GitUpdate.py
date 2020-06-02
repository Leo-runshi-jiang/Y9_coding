import os
fileadded = input("What file did you update?")
updatename = input("what is this update's name? ") 
os.system("git add "+fileadded)
os.system("git commit -m \"" + updatename+"\"")
os.system("git push")
