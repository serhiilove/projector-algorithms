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

def noTwoSlash(url: str) -> str:
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

print('test 0: ', noTwoSlash('/page1///page2////page3/test.html') == '/page1/page2/page3/test.html')
print('test 1: ', noTwoSlash('') == '')
print('test 2: ', noTwoSlash('//my/l///ink//') == '/my/l/ink/')
print('test 3: ', noTwoSlash('///') == '/')
print('test 4: ', noTwoSlash('a/s/a/a') == 'a/s/a/a')
print('test 5: ', noTwoSlash('/a/s/a/a/') == '/a/s/a/a/')
print('test 6: ', noTwoSlash('//a///s//a////a//') == '/a/s/a/a/')
print('test 7: ', noTwoSlash('//a///s//a////a/') == '/a/s/a/a/')
print('test 8: ', noTwoSlash('/a///s//a////a//') == '/a/s/a/a/')
print('test 9: ', noTwoSlash('as//a////a//') == 'as/a/a/')
print('test 10: ', noTwoSlash('/aasdb/a////a//') == '/aasdb/a/a/')
