array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

def setting_(data):
    return data[0]

array.sort(key=setting_)
print(array)