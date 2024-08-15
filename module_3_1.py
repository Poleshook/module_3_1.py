calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    tuple_ = len(string), string.upper(), string.lower()
    print(tuple_)


def is_contains(string, list_to_search):
    count_calls()
    if string.upper() in [string2.upper() for string2 in list_to_search]:
        print(True)
    else:
        print(False)


string_info("Школа")
string_info("Невообразимый")
is_contains("Поиск", ['ПиСк', 'ПОисК', 'КиоСк'])
is_contains("TwO", ["OnE", "tWo", "THrEE"])
is_contains("Elephant", ["Tiger", "monKey", "GiraffE"])
print(calls)