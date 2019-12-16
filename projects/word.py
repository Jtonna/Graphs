'''
Given two wods (begin_word and end_word), and a dictionary's word list,
return the shortest transformation sequence from being_word to end_word such that:
Only one letter can be changed at a time
Each Transformed word must exist in the word list
Note that begin_word is not a transformed word

Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume that no duplicated are in the word's list
You may assime begin_word and end_word are non-empty and are not the same

sameple:

begin_word: = "hit"
end_word: = "cog"
return ['hit', 'hot', 'cat', 'cog']

begin_word = "sail"
end_word = "boat"
return ['sail', 'bail', 'boil', 'ball', 'bolt', 'boat']

'''