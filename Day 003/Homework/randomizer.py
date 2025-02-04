from itertools import permutations

print([" > ".join(i) for i in permutations(["a", "b", "c", "d"])])

# largest = a;
# if(largest < b)
#     largest = b;
# if(largest < c)
#     largest = c;
# if(largest < d)
#     largest = d;
# if(largest < e)
#     largest = e;
# return largest;

# 1. a > b > c > d მინიჭება: 2
# 2. a > b > d > c მინიჭება: 2
# 3. a > c > b > d მინიჭება: 2
# 4. a > c > d > b მინიჭება: 2
# 5. a > d > b > c მინიჭება: 2
# 6. a > d > c > b მინიჭება: 2
# 7. b > a > c > d მინიჭება: 3
# 8. b > a > d > c მინიჭება: 3
# 9. b > c > a > d მინიჭება: 3
# 10. b > c > d > a მინიჭება: 3
# 11. b > d > a > c მინიჭება: 3
# 12. b > d > c > a მინიჭება: 3
# 13. c > a > b > d მინიჭება: 3
# 14. c > a > d > b მინიჭება: 3
# 15. c > b > a > d მინიჭება: 4
# 16. c > b > d > a მინიჭება: 4
# 17. c > d > a > b მინიჭება: 3
# 18. c > d > b > a მინიჭება: 4
# 19. d > a > b > c მინიჭება: 3
# 20. d > a > c > b მინიჭება: 3
# 21. d > b > a > c მინიჭება: 4
# 22. d > b > c > a მინიჭება: 4
# 23. d > c > a > b მინიჭება: 4
# 24. d > c > b > a მინიჭება: 5