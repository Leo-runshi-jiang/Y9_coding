nums=[4,13,13,49,20,6,13,13,12,1,3,13,9,13]
'''
if len(nums)>4:
  for i in range(0,len(nums)-3,1):
    if nums[i] == 13:
      nums.pop(i)
      if nums[i] == 13:
        nums.pop(i)
        nums.pop(i)
      else:
        nums.pop(i)
  for i in range(0,len(nums),1):
    if nums[i] == 13:
      nums.pop(i)
print(nums) 
print("second try")
'''

badnums=[]
ctr=0
for i in range(0,len(nums),1):
  if nums[i] == 13:
    badnums.append(i-ctr)
    ctr=ctr+1
    print(ctr)
    if i < len(nums)-1 and nums[i+1] != 13:
      badnums.append(i-ctr+1)
      ctr=ctr+1
print(badnums)

for i in range(0,len(badnums),1):
  nums.pop(badnums[i])

print(nums)
