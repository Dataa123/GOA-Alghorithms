### Easy version

largest = a
if b > largest then
    largest = b
end if
if c > largest then
    largest = c
end if
if d > largest then
    largest = d
end if
if e > largest then
    largest = e
end if
return largest

### Hard version

if a > b then
    if a > c then
        if a > d then
            if a > e then
                return a
            else
                return e
            end if
        else
            if d > e then
                return d
            else
                return e
            end if
        end if
    else
        if c > d then
            if c > e then
                return c
            else
                return e
            end if
        else
            if d > e then
                return d
            else
                return e
            end if
        end if
else
    if b > c then
        if b > d then
            if b > e then
                return b
            else
                return e
            end if
        else
            if d > e then
                return d
            else
                return e
            end if
        end if
    else
        if c > d then
            if c > e then
                return c
            else
                return e
            end if
        else
            if d > e then
                return d
            else
                return e
            end if
        end if
    end if
end if
