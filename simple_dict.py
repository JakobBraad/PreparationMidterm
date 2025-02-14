d = {}
eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
print(eng_to_spa["three"])
# {} []
eng_to_spa["pineapple"] = "pina"

eng_to_spa.update({"yes": "si", "no": "no", "i": "yo", "am": "soy", "cuban": "cubano"})
print(f"i know {len(eng_to_spa)}spanish words")
sentence = " i am cuban "
words = sentence.split()
translation = ""
for word in words:
    translation += eng_to_spa[word]+" "
print(f"{sentence} translates to {translation}")
print(list(eng_to_spa.values()))
print(list(eng_to_spa.keys()))
x = eng_to_spa.pop("pineapple")
print(x)
print(eng_to_spa)

if "car" in eng_to_spa:
    print(eng_to_spa["car"])
else:
    print("I dont know this word")
