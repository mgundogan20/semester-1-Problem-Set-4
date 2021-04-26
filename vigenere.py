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

  For Example: is_word(word_list, 'bat') returns True
  and is_word(word_list, 'asdf') returns False
  '''
  word = word.lower()
  word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
  return word in word_list

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
  def __init__(self, text):
    '''
    Initializes a Message object

    text (string): the message's text

    a Message object has two attributes:
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
    words_list = load_words(WORDLIST_FILENAME)
    return words_list

  def shift_letter(self, letter, key):
    '''
    letter (string of length 1)
    key (an integer)
    shifts the letter by key and returns the shifted letter
    '''
    asc = ord(letter)
    if asc in range(65,91):
        asc -= 65
        asc = (asc+key) % 26
        asc += 65
    elif asc in range(97,123):
        asc -= 97
        asc = (asc+key) % 26
        asc += 97
    output = chr(asc)
    return output

  def apply_vigenere(self, key):
    '''
    Applies the Vigenere Cipher to self.message_text with the input key.
    Creates a new string that is self.message_text such that each letter
    has been shifted by some number of characters determined by key.
    Uses the shift_letter method above.

    key (list of integers): the key to encrypt the message.

    Returns: the message text (string) encrypted by key
    '''
    key_extended = []
    encrypted = ""
    for i, char in enumerate(self.get_message_text()):
        key_extended.append(key[i%len(key)])
        encrypted += self.shift_letter(char, key_extended[i])
    
    return encrypted

class PlaintextMessage(Message):
  def __init__(self, text, key):
    '''
    Initializes a PlaintextMessage object

    text (string): the message's text
    key (list of integers): the key associated with this message

    A PlaintextMessage object inherits from Message and has four attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
        self.key (list of integers, determined by input key)
        self.message_text_encrypted (string, created using self.message_text and self.key)

    '''
    Message.__init__(self, text)
    self.key = key
    self.message_text_encrypted = self.apply_vigenere(self.key)

    pass #delete this line and replace with your code here

  def get_key(self):
    '''
    Used to safely access self.key outside of the class

    Returns: a COPY of self.key
    '''
    output = self.key[:]
    return output

  def get_message_text_encrypted(self):
    '''
    Used to safely access self.message_text_encrypted outside of the class
    Returns: self.message_text_encrypted
    '''
    return self.message_text_encrypted

  def change_key(self, key):
    '''
    Changes self.key of the PlaintextMessage and updates other
    attributes determined by key.

    key (list of integers): the new key that should be associated with this message.

    Returns: nothing
    '''
    self.__init__(self.get_message_text(), key)
    pass


class CiphertextMessage(Message):
  def __init__(self, text):
    '''
    Initializes a CiphertextMessage object

    text (string): the message's text

    a CiphertextMessage object has two attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
    '''
    Message.__init__(self, text)
    pass #delete this line and replace with your code here

  def decrypt_message(self):
    '''
    Decrypt self.message_text by trying every possible key value
    and find the "best" one. We will define "best" as the key that
    creates the maximum number of real words when we use apply_vigenere(key)
    on the message text. If [k0, k1, k2, ...] is the original key used to
    encrypt the message, then we would expect [26-k0, 26-k1, 26-k2,...] to
    be the best key for decrypting it.

    IMPORTANT NOTE1: FOR THIS PART, ONLY CONSIDER THE KEYS WITH LENGTH UP TO 3. ALSO ASSUME THAT EACH VALUE IN THE KEY IS NOT GREATER THAN 12.
    OTHERWISE IT WILL TAKE VERY VERY LONG TIME TO FINISH.

    IMPORTANT NOTE2: RETURN THE SHORTEST FORM OF A KEY. FOR EXAMPLE THE KEYS
    [2,2,2] AND [2] ARE EQUAL. AND IN SUCH CASES YOU SHOULD RETURN THE SHORTER
    ONE.

    Note: if multiple keys are equally good such that they all create
    the maximum number of valid words, you may choose any of those key
    (and their corresponding decrypted messages) to return

    Returns: a tuple of the best key used to decrypt the message
    and the decrypted message text using that key
    '''
    maxDict =  {"keys":[],
                "score":0,
                "message":""}
    words_list = self.get_valid_words()
    list_of_keys = self.possible_keys()
    
    for element in list_of_keys:
        inverse = [26-k for k in element]
        message = self.apply_vigenere(inverse)
        score = 0
        for word in message.split():
            score += 1 * is_word(words_list,word)
        anyDict =  {"keys":element,
                    "score":score,
                    "message":message}
        if anyDict["score"] > maxDict["score"]:
            maxDict = anyDict
    
    message = maxDict["message"]
    key_found = (self.key_print(maxDict["keys"]))
    return(key_found,message)
  
  def key_print(self, key):
    '''
    Returns the shortest version of a given key of size 3 as a list of integers of size up to 3.
    '''
    for i in range(1,4):
        key_extended = []
        key_slice = key[:i]
        for i in range(3):
            key_extended.append(key_slice[i%len(key_slice)])
        if key_extended == key:
            return key_slice
    

  def possible_keys(self):
    '''
    Returns all the possible keys between [0,0,0] and [12,12,12] as a list of lists
    '''
    list_of_keys = []
    for i in range(13):
        for j in range(13):
            for k in range(13):
                list_of_keys.append([i,j,k])
    return list_of_keys

if __name__ == '__main__':    
  '''
  Can you find out what this hidden message says?
  Uncomment the next lines to find out!
  '''
#   myMes = Message("Hello Every One")
#   print(myMes.shift_letter("'",2))
#   print(myMes.apply_vigenere([2,3,5]))
#   print("Jhqnr Gyjtb Qqj")

#   myPlain = PlaintextMessage("Hello Every One", [2,3,5])
#   print(myPlain.get_key())
#   print(myPlain.get_message_text_encrypted())
#   myPlain.change_key([1,2,3])
#   print(myPlain.get_key())
#   print(myPlain.get_message_text_encrypted())

#   myCiphered = CiphertextMessage("Jhqnr Gyjtb Qqj")
#   print("end",myCiphered.key_print([2,3,4]))
#   print(myCiphered.decrypt_message())


  ciphertext = CiphertextMessage('"Drmu spna vwvu bz ay nbmhd zmqlxbpcbz boo dkg dpli ky ay nbmhd teapmqhxa kvk ijdwyc, mqcstpjiaswu epvt tctz ay arm xmed sodlv" [Jysiu Oyomuo]')
  decrypted = ciphertext.decrypt_message()
  print(decrypted[1])
  pass
