class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      board = board
      word = word
      def ExistCharacter(i,j,index,word):
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[i])) :
            return False   

        # when index character does not match  
        if(board[i][j] != word[index])  :
            return False   

        # when completely matched  
        if(index == len(word) - 1)  :
            return True  
        # mark the current character  
        board[i][j] = '#'  

        # check every direction  
        found = ExistCharacter(i, j - 1, index + 1, word) or ExistCharacter(i, j + 1, index + 1, word) or ExistCharacter(i - 1, j, index + 1, word) or  ExistCharacter(i + 1, j, index + 1, word)  

        # unmark the current character  
        board[i][j] = word[index]  
        return found
      if (word == ""): 
          return False   

      # iterate over the board  
      for i in range(len(board)):
          for j in range(len(board[0])):
              if (ExistCharacter(i, j, 0, word)): 
                  return True   

      return False   
