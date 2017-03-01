# Knuth-Morris Pratt Algorithm

An implementation of the Knuth-Morris-Pratt Algorithm on string matching with detailed explanations.
I found this algorithm difficult to understand at first, especially how exactly to utilize the 'prefix table'. 
However, reading the 'string matching finite automota' section in Cormen, Leiserson, Rivest, and Stein (CLRS)'s book really helped to clarify things. 

## Prefix Table Generation
This prefix table defines the state transitions as we traverse character matches
between a space of search characters and a target search pattern. The interesting bit here
is how this prefix table is generated. We need to make the connection that when we have
a partial string match, we can avoid backtracking all the way back to where we started 
if we were able to figure out if there was a substring ending at the point where 
the string matching stopped (suffix), that matches a substring starting at the beginning of the 
pattern string (prefix). This prefix, suffix information informs the string matching
portion of the algorithm how to transition to a new string matching state without having
to backtrack all the way back to the beginning.


## String Matching using the prefix table as a state machine
If we view the prefix table as a state machine where the first entry in the table is the 
initial state, the final entry in the table as the accepting state, and all the values
of the entries in between indicators of how to state transition, we can understand how
the matching algorithm works in conjunction with the prefix table. The included python
code is annotated to show where the algorithm transitions state.

*Hopefully this can help someone!*
