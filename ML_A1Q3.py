#creating tuples brothers and sisters
sisters=("Mounika","Swetha","Amitha","Anusha")
brothers=("Akhil","Machi","Shiva","Shriyans" , "Shreyas")
print("brothers are : ",brothers)
print("sisters are : ",sisters)

#joining brothers and sisters tuples to siblings
siblings=brothers+sisters
print("siblings are : ",siblings)

#calculating number of siblings
print("number of siblings are : ",len(siblings))

#modifying siblings tuple by adding father name and mother name
family_members=("Narendar Reddy","Aruna")+siblings
print("family members are : ",family_members)