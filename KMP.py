#
# Implementation of Knuth-Morris-Pratt (KMP) Algorithm 
# anontated.
#
# Algorithm creates a text table for use with searches. 
#
# Running Time is O(n+m), where 'n' is length of the searched text (typically large)
# and 'm' is the length of target (or pattern, typically small).
#
# Assumptions: length of target <= length of text, e.g. m <= n, otherwise 
# function will not find the target
#

def KMP_strstr(text, target):
    def init_state_table(word):
        prefix_count = 0
        state_table = [0]*len(word)
        # start from the 2nd character
        for i in range(1, len(word)):
            if word[i] == word[prefix_count]:
                prefix_count+=1
            else:
                prefix_count = 0
            state_table[i] = prefix_count
        return state_table

    state_table = init_state_table(target)
    #print state_table

    # now that we have a prefix table created, we can do the string matching
    start = cmp_state = i = 0
    for i in range(len(text)):
        # Check for failure, if failure, then transition to the correct 
        # intermediate state. If no intermediate state is found, then we will go 
        # to the initial state and thus exit the while loop
        while cmp_state > 0 and text[i] != target[cmp_state]:
            cmp_state = state_table[cmp_state-1]

        # we've updated cmp_state so, we need to update new start location
        start = i-cmp_state 
        if text[i] == target[cmp_state]:
            if cmp_state == len(target)-1:
                return start 
            # update the automaton state
            cmp_state+=1

    return -1


def main():
    print 'Knuth Morris Pratt (KMP) string search algorithm'

    Input = 'y ababaca siifjae', 'ababaca'
    print Input
    res = KMP_strstr(Input[0], Input[1])
    print 'len:', len(Input[1])
    print 'result:', res, "'{}'".format(Input[0][res:res+len(Input[1])])
    assert Input[0][res:res+len(Input[1])] == Input[1]
    print 'correct:', Input[0].find(Input[1])
    assert res == Input[0].find(Input[1])

    Input = 'y ababac siifjae', 'ababac'
    print Input
    res = KMP_strstr(Input[0], Input[1])
    print 'len:', len(Input[1])
    print res, "'{}'".format(Input[0][res:res+len(Input[1])])
    assert Input[0][res:res+len(Input[1])] == Input[1]
    print 'correct:', Input[0].find(Input[1])
    assert res == Input[0].find(Input[1])
    #return

    Input = 'abababacsiifjae', 'ababac'
    print Input
    res = KMP_strstr(Input[0], Input[1])
    print 'len:', len(Input[1])
    print res, "'{}'".format(Input[0][res:res+len(Input[1])])
    print 'correct:', Input[0].find(Input[1])
    assert Input[0][res:res+len(Input[1])] == Input[1]
    assert res == Input[0].find(Input[1])

    Input = 'adfbec dsfoeifj asdfjww abyyabcdefg siifjae', 'aba'
    res = KMP_strstr(Input[0], Input[1])
    print 'len:', len(Input[1])
    print res 
    print 'correct:', Input[0].find(Input[1])
    assert res == Input[0].find(Input[1])
    #return

    Input = 'adfbec dsfoeifj asdfjww sifmyy abcdefg siifjae', 'ab'
    res = KMP_strstr(Input[0], Input[1])
    print 'len:', len(Input[1])
    print res, "'{}'".format(Input[0][res:res+len(Input[1])])
    print 'correct:', Input[0].find(Input[1])
    #assert res == Input[0].find(Input[1])

    Input = 'adfbec dsfoeifj asdfjww sifmyy abcdefg siifjae', 'a'
    res = KMP_strstr(Input[0], Input[1])
    print 'len:', len(Input[1])
    print res, "'{}'".format(Input[0][res:res+len(Input[1])])
    print 'correct:', Input[0].find(Input[1])
    assert res == Input[0].find(Input[1])

    Input = 'adfbec dsfoeifj asdfjww sifmyy abcdefg siifjae', 'aa'
    res = KMP_strstr(Input[0], Input[1])
    print 'len:', len(Input[1])
    print res, "'{}'".format(Input[0][res:res+len(Input[1])])
    print 'correct:', Input[0].find(Input[1])
    assert res == Input[0].find(Input[1])


if __name__ == "__main__":
    main()
