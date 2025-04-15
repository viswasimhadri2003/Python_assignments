D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }

#union of 2 dictionaries

dic_union={}
for key in sorted(D1.keys()|D2.keys()):
    dic_union[key]=D1.get(key) or D2.get(key)
print(dic_union)

#intersection of 2 dictionaries

dic_intersection={}
for key in sorted(D1.keys() & D2.keys()):
    dic_intersection[key]=D1[key]
print(dic_intersection)

#dict1-dict2

dic_difference={}
for key in sorted(D1.keys()-D2.keys()):
    dic_difference[key]=D1[key]
print(dic_difference)

#merging values of same keys

dic_merged={}
for key in sorted(D1.keys()|D2.keys()):
    dic_merged[key]=D1.get(key,0)+D2.get(key,0)
print(dic_merged)