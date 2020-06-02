na = 9.0
c = 1.0
fractionvol=1/(c+na)*0.52
'''
#convert to moles
molna = na*2.2/84.0
molc = c*1.66/192.1
masstot = na*2.2+c*1.66

if molna/3.0 < molc:
	moleco=molna
	volco = moleco*44.0/0.00196
else:
	molco = 3*molc
	volco = molco*3*44.0/0.00196
print("volume of CO2 is")
print(volco*por*0.5)
print("moles of CO2")
print(molco)
print("moles of soda")
print(molna*por*0.5)
print("moles of acid")
print(molc*por*0.5)
print(masstot*por*0.5)
'''
volna = na*fractionvol
volc = c*fractionvol

print(volna)
print(" ml of base ")
print(volc)
print(" ml of acid")

molna= volna*2.2/84.0
molc = volc*1.66/192.1

print(molna)
print(" mols of base ")
print(molc)
print(" mols of acid")

masstot = volna*2.2 + volc*1.66

print(masstot)
print(" total mass")

if molna/3.0 < molc:
	molco=molna
	volco = molco*22448.97
else:
	molco = 3*molc
	volco = molco*22448.97
print(molco)
print("moles of co2")
print(volco)
print("ml of co2")






      
