class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique = set()
        for word in words:
            morse_block = []
            for ch in word:
                morse_block.append(alphabet[ord(ch) - 97])
            morse_word = ''.join(morse_block)
            unique.add(morse_word)
        
        return (len(unique))
