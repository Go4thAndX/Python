# Exercise 3: Print the value of key ‘history’ from the dictionary [sampleDict]

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


# Expected output:
# 80
# My solution:

print(sampleDict["class"]["student"]["marks"]["history"])

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}
# sampleDict['class']['student']['marks']['history'] = 80

# Output:
# 80

# Given solution:

print(sampleDict['class']['student']['marks']['history'])