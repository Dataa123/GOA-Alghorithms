# list length will always be 4 
def test1(list1):
    a, b, c, d = list1
#   3  2  4  1
    if a > b:
        if a > c:
            if a > d:
                return "a"
            else:
                return "d"
        else:
            if c > d:
                return "c"
            else:
                return "d"
    else:
        if b > c:
            if b > d:
                return "b"
            else:
                return "d"
        else:
            if c > d:
                return "c"
            else:
                return "d"

print(test1([1, 2, 3, 4]))
print(test1([1, 4, 2, 3]))
# ✔

# do the same for list of length 5

def test2(list1):
    a, b, c, d, e = list1

    if a > b:
        if a > c:
            if a > d:
                if a > e:
                    return "a"
                else:
                    return "e"
            else:
                if d > e:
                    return "d"
                else:
                    return "e"
        else:
            if c > d:
                if c > e:
                    return "c"
                else:
                    return "e"
            else:
                if d > e:
                    return "d"
                else:
                    return "e"
    else:
        if b > c:
            if b > d:
                if b > e:
                    return "b"
                else:
                    return "e"
            else:
                if d > e:
                    return "d"
                else:
                    return "e"
        else:
            if c > d:
                if c > e:
                    return "c"
                else:
                    return "e"
            else:
                if d > e:
                    return "d"
                else:
                    return "e"
                
print(test2([1, 2, 3, 4, 5]))
print(test2([1, 2, 5, 4, 3]))
#            a, b, c, d, e
# ✔
