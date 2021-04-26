import string

### HELPER CODE ###
def load_words(file_name):
  '''
  file_name (string): the name of the file containing 
  the list of words to load    
  
  Returns: a list of valid words. Words are strings of lowercase letters.
  
  Depending on the size of the word list, this function may
  take a while to finish.
  '''
  
  # inFile: file
  inFile = open(file_name, 'r')
  # wordlist: list of strings
  wordlist = []
  for line in inFile:
    wordlist.extend([word.lower() for word in line.split(' ')])
  return wordlist

def is_word(word_list, word):
  '''
  Determines if word is a valid word, ignoring
  capitalization and punctuation

  word_list (list): list of words in the dictionary.
  word (string): a possible word.
  
  Returns: True if word is in word_list, False otherwise

  Example:
  >>> is_word(word_list, 'bat') returns
  True
  >>> is_word(word_list, 'asdf') returns
  False
  '''
  word = word.lower()
  word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
  return word in word_list

### END HELPER CODE ###


WORDLIST_FILENAME = 'words.txt'

def get_permutations(sequence):
  '''
  sequence (string): a string
  returns all permutations of sequence in a list
  
  You CAN use your code from the PS3.5
  '''
  mylist = []
  if len(sequence) == 1:
      mylist = [sequence]
  else:
      for element in get_permutations(sequence[1:]):
          for position in range(len(element)+1):
              newPerm = element[:position] + sequence[0] + element[position:]
              mylist.append(newPerm)

  return mylist

class SubMessage(object):
  def __init__(self, text):
    '''
    Initializes a SubMessage object
            
    text (string): the message's text

    A SubMessage object has two attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
    '''
    self.message_text = text
    self.valid_words = []
    pass #delete this line and replace with your code here
  
  def get_message_text(self):
    '''
    Used to safely access self.message_text outside of the class
    
    Returns: self.message_text
    '''
    return self.message_text

  def get_valid_words(self):
    '''
    Used to safely access a copy of self.valid_words outside of the class.
    This helps you avoid accidentally mutating class attributes.
    
    Returns: a COPY of self.valid_words
    '''
    words_list = load_words("words.txt")
    return words_list

  def build_transpose_dict(self, letters_permutation):
    '''
    letters_permutation (string): a string containing a permutation of letters (e, t, a, o, i, n)
    
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to an
    uppercase and lowercase letter, respectively. (e, t, a, o, i, n) are shuffled 
    according to letters_permutation. The first letter in letters_permutation 
    corresponds to e, the second to t, and so on in the order e, t, a, o, i, n.
    The other letters remain the same. The dictionary should have 52 
    keys of all the uppercase letters and all the lowercase letters.

    Example: When input "anotei":
    Mapping is e->a, t->n, a->o, o->t, i->e, n->i
    and "Nice To Meet You!" maps to "Ieca Nt Maan Ytu!"

    Returns: a dictionary mapping a letter (string) to 
              another letter (string). 
    '''
    d = {}
    letters_permutation = letters_permutation.lower()
    common_letters = ("e","t","a","o","i","n")

    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter in common_letters:
            index = common_letters.index(letter)
            d[letter] = letters_permutation[index]
            d[letter.upper()] = letters_permutation[index].upper()
        else:
            d[letter] = letter
            d[letter.upper()] = letter.upper()
    return d
  
  def apply_transpose(self, transpose_dict):
    '''
    transpose_dict (dict): a transpose dictionary
    
    Returns: an encrypted version of the message text, based 
    on the dictionary
    '''
    plain = self.get_message_text()
    out = ""

    for letter in plain:
        try:
            char = transpose_dict[letter]
        except KeyError:
            char = letter
        except:
            print("something went wrong")
        
        out += char

    return out

  def __eq__(self, other):
    output = False
    try:
        if (self.get_message_text() == other.get_message_text()) and (self.get_valid_words() == other.get_valid_words()) and (type(self) == type(other)):
            output = True
    except:
        pass
    return output

class EncryptedSubMessage(SubMessage):
  def __init__(self, text):
    '''
    Initializes an EncryptedSubMessage object

    text (string): the encrypted message text

    An EncryptedSubMessage object inherits from SubMessage and has two attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
    '''
    SubMessage.__init__(self,text)
    pass #delete this line and replace with your code here
  
  def decrypt_message(self):
    '''
    Attempt to decrypt the encrypted message 
    
    Idea is to go through each permutation of the 'etaoin' and test it
    on the encrypted message. For each permutation, check how many
    words in the decrypted text are valid English words, and return
    the decrypted message with the most English words.
    
    If no good permutations are found (i.e. no permutations result in 
    at least 1 valid word), return the original string. If there are
    multiple permutations that yield the maximum number of words, return any
    one of them.

    Returns: the best decrypted message    
    '''
    maxDict =  {"perm":"",
                "score":0,
                "message":""}
    words_list = self.get_valid_words()
    list_of_keys = get_permutations("etaoin")
    
    for element in list_of_keys:
        d = self.build_transpose_dict(element)
        message = self.apply_transpose(d)
        score = 0
        for word in message.split():
            score += 1 * is_word(words_list,word)
        anyDict =  {"perm":element,
                    "score":score,
                    "message":message}
        if anyDict["score"] > maxDict["score"]:
            maxDict = anyDict
    
    message = maxDict["message"]
    return(message)
  
  def __eq__(self, other):
    output = False
    try:
        if (self.get_message_text() == other.get_message_text()) and (self.get_valid_words() == other.get_valid_words()) and (type(self) == type(other)):
            output = True
    except:
        pass
    return output
    

if __name__ == '__main__':
  '''
  Can you find out what this hidden message says?
  Uncomment the next lines to find out!
  '''
  # encrypted = EncryptedSubMessage('We re iryotg in prnve nurselves wrntg as quockly as pnssoble, because ntly ot ihai way cat we fotd prngress.  [Rochard Feytmat]')
  # print(encrypted.decrypt_message())

#   myMes = SubMessage("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
  myMes = EncryptedSubMessage("Ieca Nt Maan Ytu!")
  
  print(myMes.decrypt_message())





#   print(len(get_permutations("etaoin")))
  pass