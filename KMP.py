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
    # By checking the largest word suffix which matches the word prefix, we can
    # generate a 'prefix table' that can then be used as a state machine, where 0 is the 
    # initial state and the last character in the table being the accpeting state.
    # 
    # We generate the prefix table by maintaining a running count of character matches
    # starting from the 2nd character as we are walking the word character by character.
    #
    # The reason this works is because of the prefix count reveals how many prefix
    # matches at any point in the string. The prefix matches will let us know where in
    # the word to jump to (state change) if we see a mismatch as we are actually
    # matching the word.
    #

    def init_prefix_table(word):
        prefix_count = 0
        prefix_table = [0]*len(word)
        # start from the 2nd character
        for i in range(1, len(word)):
            if word[i] == word[prefix_count]:
                prefix_count+=1
            else:
                prefix_count = 0
            prefix_table[i] = prefix_count
        return prefix_table

    prefix_table = init_prefix_table(target)
    #print prefix_table

    # now that we have the state_table (aka prefix table) created, we can do the string matching
    # using it as a guide for state transitions
    start = state = i = 0
    for i in range(len(text)):
        # Check for failure, if failure, then transition to the correct 
        # intermediate state. If no intermediate state is found, then we will go 
        # to the initial state and thus exit the while loop
        while state > 0 and text[i] != target[state]:
            state = prefix_table[state-1]

        # we've updated state so, we need to update new start location
        start = i-state 
        if text[i] == target[state]:
            if state == len(target)-1:
                return start 
            # update the automaton state
            state+=1

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
