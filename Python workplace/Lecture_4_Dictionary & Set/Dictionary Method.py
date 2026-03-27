info = {
    "name" : "Rashel Mahmud Rabbi",
    "age" : 25,
    45 : 78
}

info["name"] =  "Rashel Mahmud"

info["surename"]="Pk"

print(type(info))

print(info)

print(info.keys())

print(info.values())

print(info.items())

print(info.get("name"))

new_info = {
    "Degree" : "Honers",
    "Subj_name" : "CSE"
}

info.update(new_info)

# print(info)

print(list(info.keys()))