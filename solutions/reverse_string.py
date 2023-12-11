def reverse_string(string):
    # base case
    if len(string) < 2:
        return string
    
    # recursive case
    else:
        return reverse_string(string[1:]) + string[0]
    
if __name__ == "__main__":
    print("Expecting: 'ih'")
    print(reverse_string('hi'))

    print("")

    print("Expecting: 'ybabtac'")
    print(reverse_string('catbaby'))

    print("")

    print("Expecting: 'a'")
    print(reverse_string('a'))

    print("")

    print("Expecting: '' (empty string)")
    print(reverse_string(''))

############################################################################
# return string if length == 1 or is empty
# 
# return reverse_string(string - 0th char) + 0th char
############################################################################

############################################################################
#  First I thought about the base case: if the string is empty or just one character,
#  we can return it as is. Next, I thought about if the string were 2 characters. In
#  that case, I need to return str[1] + str[0] for it to be reversed. Since recursion
#  is depth-first, i.e. it goes as deep as possible before it starts returning up the
#  stack, that means the algorithm won't start returning until it hits the last character
#  in the string. Let's pretend the string is 'hi'. On the first frame we recurse with 'i'
#  as the argument. This hits the base case, so 'i' returns. In the previous frame, the
#  0th character is 'h', so I just need to put the 'h' after the 'i' that's returned from
#  the recursive call: reverse_string('i') + 'h'. This holds true for strings of any length
#  because as each frame returns up the stack, the 0th character in each previous frame is 
#  the character that comes right before the one that was returned.
############################################################################