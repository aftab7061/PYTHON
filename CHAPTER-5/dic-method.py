marks={
    "aftab":98,
    "asif":99,
    "sameer":78
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"aftab":95,"priya":100})
print(marks)

print(marks.get("sam"))
print(marks.get("aftab1")) #print none
# print(marks["aftab1"]) #print error
