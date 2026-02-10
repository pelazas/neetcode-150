
class LetterNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class WordDictionary:
    def __init__(self):
        self.root_node = LetterNode()
        

    def addWord(self, word: str) -> None:
        node = self.root_node
        for c in word:
            if c not in node.children:
                node.children[c] = LetterNode()
            node = node.children[c]
        node.is_end = True

    # Time complexity: O(L) -> L = len(word)
    def search(self, word: str) -> bool:
        def dfs(node, index):
            current = node
            
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    # check all possible children
                    for child in current.children.values():
                        if dfs(child,i+1) == True:
                            return True
                    return False
                else:
                    if char not in current.children:
                        return False
                    current = current.children[char]
            return current.is_end
        return dfs(self.root_node,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)