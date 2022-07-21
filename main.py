# && => and in logical statement
# || => or in logical satatement
# ! => not in logical statement
# qpr => vars in logical statement ( for now)
# () => () in logical statement


# e.g => !(q&p)
# our return =>
#  q   p   !(q&p)
#  T   T      F
#  T   F      T
#  F   T      T
#  F   F      T


from traceback import print_tb


logical = input("enter your logical statement: ")

# now we can use eval to check resual is true or false (python use or instead of || somehow)
logical = logical.replace("||", " or ").replace(
    "&&", " and ").replace("!", " not ")

q, p, r = False, False, False  # init vars that we use in our statement


print("q     p     r     result")
for i in [True, False]:
    for j in [True, False]:
        for k in [True, False]:
            q, p, r = i, j, k
            # bcz True is 1 space smaller than False we have to make another space on true and best way to do that is
            for l in [q, p, r, eval(logical)]:
                if l == True:                  # by looping in print things ;)
                    print(l, end="  ")
                else:
                    print(l, end=" ")
            print("\n")
