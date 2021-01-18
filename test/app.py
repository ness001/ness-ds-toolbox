# class Solution:
#     def isNumber(self, s: str) -> bool:
#         states = [
#             { ' ': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start with 'blank'
#             { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
#             { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, # 2. 'digit' before 'dot'
#             { 'd': 3, 'e': 5, ' ': 8 },         # 3. 'digit' after 'dot'
#             { 'd': 3 },                         # 4. 'digit' after 'dot' (‘blank’ before 'dot')
#             { 's': 6, 'd': 7 },                 # 5. 'e'
#             { 'd': 7 },                         # 6. 'sign' after 'e'
#             { 'd': 7, ' ': 8 },                 # 7. 'digit' after 'e'
#             { ' ': 8 }                          # 8. end with 'blank'
#         ]
#         p = 0                           # start with state 0
#         for c in s:
#             if '0' <= c <= '9': t = 'd' # digit
#             elif c in "+-": t = 's'     # sign
#             elif c in "eE": t = 'e'     # e or E
#             elif c in ". ": t = c       # dot, blank
#             else: t = '?'               # unknown
#             if t not in states[p]: return False
#             p = states[p][t]
#         return p in (2, 3, 7, 8)


class Solution:
    def isNumber(self, s: str) -> bool:
        
        # value:
        
        # 0. start - blank
        # 1. digit before dot
        # 2. digit after dot
        # 3. dot with digit
        # 4. e
        # 5. sign before dot
        # 6. sign after e
        # 7. digit after e
        # 8. end - blank 
# key: 
# digit = 'd'
# e E = 'e'
# dot = '.'
# blank = ' '
# + - = 's'

        states = [
            {' ': 0 , 'd': 1, '.':3, 's': 5},
            {'d': 1, '.': 3,'e': 4, ' ':8 },
            {'d': 2 , 'e': 4, ' ': 8},
            {'d': 2},
            {'s': 6, 'd': 7},
            {'d': 1,'.': 8 },
            {'d': 7},
            {'d': 7, ' ': 8},
            {' ': 8}
        ]

        #get key
        current_t = 0
        for c in s:
            if '0' <= c <='9':
                next_key = 'd'
            elif c in '. ':
                next_key = c
            elif c in 'eE':
                next_key= 'e'
            elif c in '+-':
                next_key= 's'
            if next_key not in states[current_t]:
                return False
            current_t = states[current_t][next_key]
        return current_t in [1,2,7,8]

s=Solution()
s.isNumber('0..')