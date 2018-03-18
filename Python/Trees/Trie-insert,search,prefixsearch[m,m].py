#create Trie data struction with insearch, search, startswith operations
'''
Why Trie: Using Trie, search complexities can be brought to optimal limit (key length). If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. Using Trie, we can search the key in O(M) time.

INSERT:
Time complexity : O(m), where m is the key length.
In each iteration of the algorithm, we either examine or create a node in the trie till we reach the end of the key. This takes only m operations.

Space complexity : O(m).
In the worst case newly inserted key doesn't share a prefix with the the keys already inserted in the trie. We have to add m new nodes, which takes us O(m) space.

SEARCH:
Time complexity : O(m) In each step of the algorithm we search for the next key character. In the worst case the algorithm performs m operations.

Space complexity : O(1)

SEARCH For a key prefix in a trie:(Startswith)
Time complexity : O(m)
Space complexity : O(1)

''''
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.is_endof_word=False #isEndOfWord is True if node represent the end of the word
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            current = current.children[char]
        current.is_endof_word = True

    def search(self, word):
        current = self.root
        for char in word:
            current = current.children.get(char) #method get() returns a value for the given char
            if current is None:
                return False
        return current.is_endof_word

    def startswith(self, prefix):
        current = self.root
        for char in prefix:
            current = current.children.get(char)
            if current is None:
                return False
        return True

keys = ["I","love","to","work","at","Facebook"]

t = Trie()
for key in keys:
        t.insert(key)
        
print (t.search('Facebook'))
print (t.startswith('lov'))
        
