ColorsDict={
    "FavColor":"Blue",
    "Piece" :  "White"

}
ColorsDict['FavColor']='Pink'
print(type(ColorsDict))
print(ColorsDict)

student={
    'studentname': 'Shefali',
    'Email': 'abc@gmail.com',
    'marks': (25, 90, 45, 50),
    'sports': {
                "indoor":"Carrom",
                "outdoor":"Cricket"
    }
}

#Tuple inside the Dictionary
print(student["marks"][0])
#Dictionary inside Dictionary
print(student["sports"]["outdoor"])