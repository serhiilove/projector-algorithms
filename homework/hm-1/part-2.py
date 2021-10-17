# python3
# def noTwoSlash(url: str) -> str:
#     arr = list(url)
#     i = 1
#     while i < len(arr):
#         if (arr[i-1] == '/') and (arr[i] == '/'):
#             for y in range(i+1, len(arr)):
#                 arr[y-1] = arr[y]
#             arr = arr[:-1]  # same array, but without last element
#         else:
#             i += 1
#     return ''.join(arr)

def noTwoSlash2(url: str) -> str:
    arr = list(url)
    result_arr = []
    is_slash = False
    i=0
    while i < len(arr):
        if (arr[i] != '/'):
            is_slash = False
            result_arr.append(arr[i])
            i += 1
        elif (arr[i] == '/') and is_slash:
            i += 1
        else:
            is_slash = True
            result_arr.append(arr[i])
            i += 1
    return ''.join(result_arr)

print('test 1: ', noTwoSlash2('') == '')
print('test 2: ', noTwoSlash2('//my/l///ink//') == '/my/l/ink/')
print('test 3: ', noTwoSlash2('///') == '/')
print('test 4: ', noTwoSlash2('a/s/a/a') == 'a/s/a/a')
print('test 5: ', noTwoSlash2('/a/s/a/a/') == '/a/s/a/a/')
print('test 6: ', noTwoSlash2('//a///s//a////a//') == '/a/s/a/a/')
print('test 7: ', noTwoSlash2('//a///s//a////a/') == '/a/s/a/a/')
print('test 8: ', noTwoSlash2('/a///s//a////a//') == '/a/s/a/a/')
print('test 9: ', noTwoSlash2('as//a////a//') == 'as/a/a/')
print('test 10: ', noTwoSlash2('/aasdb/a////a//') == '/aasdb/a/a/')
