import os
updatename = input("what is this update's name? ") 
os.system("git add .")
os.system("git commit -m \"" + updatename+"\"")
os.system("git push")