#creating dog dictionary
dog=dict()
dog["Name"]="Puppy"
dog["Color"]="White"
dog["Breed"]="Shih Tzu"
dog["legs"]=4
dog["Age"]=3
print(" Dog dictionary is : ",dog)
print()

#creating student dictionary
student=dict()
student["first_name"]="Manisha Reddy"
student["last_name"]="Lenkala"
student["Gender"]="Female"
student["Age"]=27
student["Marital status"]="Married"
student["Skills"]=["python","Java"]
student["Country"]="India"
student["City"]="Nalgonda"
student["Address"]="H.no:13-79/1"
print("Student dictionary is : ",student)


#length of student dictionary
print("length of student dictionary is : ",str(len(student)));

#value of student skills and datatype
print("student skills are : ",end='')
print(student["Skills"])
print("type of student skills is : ",type(student["Skills"]))

#modifying student skills
student["Skills"].append("Mandala Artist")
student["Skills"].append("AWS")
print("modified student skills : ",student["Skills"])

#getting dictionary keys as list
dog_keys=list(dog.keys())
print("dog dictionary keys : ",dog_keys)
student_keys=list(student.keys())
print("student dictionary keys : ",student_keys)

#getting dictionary values as list
dog_values=list(dog.values())
print("dog dictionary values : ",dog_values)
student_values=list(student.values())
print("student dictionary values : ",student_values)
