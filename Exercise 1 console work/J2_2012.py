dep1 = input("depth 1")
dep2 = input("depth 2")
dep3 = input("depth 3")
dep4 = input("depth 4")
pattern = False

if dep1 > dep2 > dep3 > dep4:
	pattern = True
	print("Fish Diving")

if dep1 < dep2 < dep3 < dep4:
	pattern = True
	print("Fish Rising")

if dep1 > dep2 > dep3 > dep4:
	pattern = True
	print("Constant Depth")

if pattern == False:
	print("No Fish")