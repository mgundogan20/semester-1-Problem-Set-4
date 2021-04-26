# PS4 - Classes and Inheritance

# Deadline: 27/12/2020-23:00

In this problem set, you will learn how to define and use classes and inheritance. This problem set consists of two problems.

In both problems, we are going to learn about cryptography to create secret messages. Have fun!

So, let's start with basic terminology:

* **Encryption**: The process of obscuring or encoding messages to make them unreadable
* **Decryption**: Making encrypted messages readable again by decoding them
* **Cipher**: Algorithm for performing encryption and decryption
* **Plaintext**: the original message
* **Ciphertext**: The encrypted message. A ciphertext still contains all of the original message information, even if it looks like gibberish.
* **Key**: A key that is used in the cipher for encryption and/or decryption  

## Problem 1: Vigenère Cipher

First, let's have a look at a simple example of encryption called *Caesar Cipher*:

Suppose that we have a letter like `'a'` and we want to encrypt it. We can shift this letter by a number and get a new letter. For example, if we shift it by `1` we will get the letter `'b'`: 

a &#8594; b

Or if we shift it by `2` we will get the letter `'c'` :

a &#8594; b &#8594; c 

In other words, when shifting a letter by a number `k`, we replace it by the letter in alphabet that is standing `k` places further down in the alphabet.

Note that if we reach the end of the alphabet, we continue from the beginning, e.g. if we shift the letter `'x'` by `4` we will get letter `'b'`.

x &#8594; y &#8594; z &#8594; a &#8594; b

Decrypting this cipher is as easy as its encryption:
If the letter was shifted by `k`, then if we shift the encrypted letter by `26-k` we will get the original letter!

For example:
Encryption (shift by  5): a &#8594  f
Decryption (shift by 21): f &#8594  a

The value `k` which is an integer used for shifting is called the **Key** of this cipher.


Now we are ready to define the *Vigenère Cipher*:

In this cipher, we have a plaintext that is a string of length `m` that we want to encrpyt and a key that is a list of integers of length `n`. If `n < m`, first we extend the key by repeating it until its length matches the plaintext. Then we shift each letter in the plaintext by the corresponding value in the extended key to get the ciphertext.

For example:
**Plaintext**: `'programming'`
**Key**: `[2, 9, 3]` &#8594 **Extended Key**: `[2, 9, 3, 2, 9, 3, 2, 9, 3, 2, 9]`

|  Letter  |  p  |  r  |  o  |  g  |  r  |  a  |  m  |  m  |  i  |  n  |  g  |
|:---:|:---:|:---:|
|  Shift Value  |  2  |  9  |  3  |  2  |  9  |  3  |  2  |  9  |  3  |  2  |  9  |
|  Shifted Letter  |  r  |  a  |  r  |  i  |  a  |  d  |  o  |  v  |  l  |  p  |  p  |

so **Ciphertext** = `'rariadovlpp'`

Note that, decrypting a ciphertext with a known key is again similar to the encrpytion method. We just need to apply shifting with the value `26 - k` for each `k` in the original key used for encrypting.

|  Letter  |  r  |  a  |  r  |  i  |  a  |  d  |  o  |  v  |  l  |  p  |  p  |
|:---:|:---:|:---:|
|  Shift Value  |  24  |  17  |  23  |  24  |  17  |  23  |  24  |  17  |  23  |  24  |  17  |
|  Shifted Letter  |  p  |  r  |  o  |  g  |  r  |  a  |  m  |  m  |  i  |  n  |  g  |




### Now back to python!

In `vigenere.py` file, we have a `Message` class with two subclasses `PlaintextMessage` and `CiphertextMessage`. `Message`​ contains methods that could be used to apply a cipher to a string, either to encrypt or to decrypt a message (since for Vigenère codes this is the same action). `PlaintextMessage` ​ has methods to encode a string using a key; our class will always create an encoded version of the message, and will have methods for changing the encoding. `CiphertextMessage` contains a method used to decode a string.

When you have completed your implementation, you can either create a `CiphertextMessage` ​ instance using an encrypted string that someone provides you and try to decrypt it; or you can encrypt your own ​ `PlaintextMessage` ​ instance, then create a ​ `CiphertextMessage` ​ instance from the encrypted message within the `PlaintextMessage` ​ instance, and try to decrypt it and see if it matches the original plaintext message.

The task is to fill methods for all three of these classes according to the specifications given here and also in the docstrings of methods in `vigenere.py`. ​ Please remember that you never want to directly access attributes outside a class - that's why you have getter and setter methods. Do not overthink this; a getter method should just return an attribute such that it cannot be altered and a set method should just set an attribute equal to the argument passed in. Although they seem simple, we need these methods in order to ensure that we are not manipulating attributes that we should not be. Directly using class attributes outside of the class itself instead of using getters and setters will result in a point deduction – and more importantly can cause you headaches as you design and implement object class hierarchies.

There are a couple of helper functions that we have implemented for you: `load_words` and `is_word`​. You may use these in your solution and you do not need to understand them completely, but should read the associated comments. You should read and understand the helper code in the rest of the file and use it to guide your solution.


### Part 1: Message  

Fill in the methods of the ​ Message​ class found in `vigenere.py` according to the specifications given here and in the docstrings.

We have provided skeleton code in the ​`Message`​ class for the following functions - your task is to implement them. Please also read the docstring comment with each function for more information about the function specification.

* `__init__(self, text)`
* The getter methods: 
    `get_message_text(self)`: This should return an immutable version of the message text we added to this object in init. Luckily, strings are already immutable objects, so we can simply return that string.
    `get_valid_words(self)`: Note: this should return a COPY of self.valid_words to prevent someone from accidentally mutating the original list.
* `shift_letter(self, letter, key)` This method will take a letter (a string with length 1) and a key (an integer) and will shift the letter by the key as explained at the beginning. 
**Important Note1: This function MUST only shift alphabet letters. If the input is not an alphabet letter, such as a space or a punctuation mark it MUST NOT be shifted.**
**Important Note2: If the letter is lowercase, the output should also be lowercase, and if the letter is uppercase the output should also be uppercase.**

Examples:
`shift_letter(self, '!', 2)` must return `'!'`
`shift_letter(self, 'b', 2)` must return `'d'`
`shift_letter(self, 'B', 2)` must return `'D'`

**Hint**: You may find `string` module's `ascii_lowercase` and `ascii_uppercase` constants helpful.

* `apply_vigenere(self, key)` This  method will apply the vigenere cipher on the message text. Again note that any lowercase letter must be mapped to a lowercase, and any uppercase letter must be mapped to an uppercase letter.
For example, if the `message_text` is `'Hello Every One'` and the key is `[2, 3, 5]` the output should be `'Jhqnr Gyjtb Qqj'`

**Hint**: Use the `shift_letter(self, letter, key)` method. 


### Part 2: PlaintextMessage

Fill in the methods of the ​`PlaintextMessage` class found in `vigenere.py`
according to the specifications given here and in the docstrings. The methods you should fill in are:

* `__init__(self, text, key)`: You must use the parent class's constructor to make your code more concise.
* The getter methods:
   `get_key(self)`: Note that you should return a COPY of the key to prevent someone from mutating the list.
   `get_message_text_encrypted(self)`
* `change_key(self, key)`: changes the key associated with this object and updates the other attributes that are affected.

**Hint**: Think about what other methods you can use to make this easier. It should not take more than a couple lines of code 


### Part 3: CiphertextMessage

Given an encrypted message, if you know the key used to encode the message, decoding it is trivial. If ​`message`​ is the encrypted message, and `[k0, k1, k2, ...]` is the key used to encrypt the message, then ​`apply_vigenere(message, [26-k0, 26-k1, 26-k2, ...])` gives you the original plaintext
message. Do you see why?

The problem, of course, is that you don’t know the key. But if we can write a program that tries every possible key and maximizes the number of English words in the decoded message, we can decrypt their cipher. But the problem is that the number of possible keys is very large (`26 ** len(ciphertext)`) and trying every possible key is practicly impossible. 
**So in this part of the problem, we are going to assume that a key has a length of at most `3` and each value in the key is at most `12` and try to decrypt the ciphertext.**

Fill in the methods of the ​`CiphertextMessage` class found in `vigenere.py`
according to the specifications given here and in the docstrings. The methods you should fill in are:

* `__init__(self, text)`: You must use the parent class's constructor to make your code more concise.

* `decrypt_message(self)`: Try every key of length up to 3 such that each value in the key is not greater than 12 and find the one that maximizes the number of words in the decrpyted message.

**Note**: Running this method might take a while.
**Important Note: Return the shortest form of a key. For example the keys ** `[2,2,2]` **and** `[2]`** are equal (Do you see why?) and in such cases, you should return the shorter key.**

**Hint**: You may find the helper function ​`is_word(wordlist, word)` ​and the string method ​[`split`](https://docs.python.org/3/library/stdtypes.html#str.split​)​ useful, or alternatively type `help(str.split)` ​in your console.

**Note**: ​`is_word` ​will ignore punctuation and other special characters when considering whether a word is valid.
Your method should return a tuple consisting of the best key that you found **that was used to encrypt the original message (not the one that you used for decrypting)** and the decrypted message.

For example if the encrypted message is `'Jhqnr Gyjtb Qqj'`, then it must return `([2, 3, 5], 'Hello Every One')`


## Problem 2: Substitution Cipher

Another way to hide your messages is to use a substitution cipher. In this approach, you create a hidden coding scheme, in which you substitute a randomly selected letter for each original letter. For the letter `'a'`, you could pick any of the other 26 letters (including keeping `'a'`), for the letter `'b'`, you could then pick any of the remaining 25 letters (other than what you selected for `'a'`) and so on. You can probably see that the number of possibilities to test if you wanted to decrypt a substitution ciphered message is very large (`26!`). So for this problem, we are going to just consider substitution ciphers in which only the 6 most frequent English letters are encrypted, with lowercase and uppercase versions of a letter being mapped to corresponding letters. (For example, `'A'` &#8594 `'O'` then `'a'`&#8594`'o'`). These 6 letters are: `'e', 't', 'a', 'o', 'i', 'n'`.

Similar to the Vigenère cipher, we are going to use classes to explore this idea. We will have a ​​`SubMessage` ​class with general functions for handling Substitution Messages of this kind. We will also write a class with a more specific implementation and specification, ​​`EncryptedSubMessage`, ​​that inherits from the `SubMessage`​​ class.

The task is to fill methods for both classes according to the specifications given
here and in the docstrings of ​`substitution.py`. Please remember that you never want to directly access attributes outside a class - that's why you have getter and setter methods.
Again, do not overthink this; a get method should just return a variable such that it cannot be altered and a set method should just set an attribute equal to the parameter passed in. Although they are simple, we need these methods in order to make sure that we are not manipulating attributes we shouldn’t be. Directly using class attributes outside of the class itself instead of using getters and setters will result in a point deduction – and more importantly can cause you headaches as you design and implement object class hierarchies.

First, you need to implement the `get_permutations(sequence)` function. This function should take a string as input and return all of the permutations of that string as a list. Note that you should have already implemented this function in PS3.5 and you **can** and **should** reuse that implementation here.


### Part 1: SubMessage

Fill in the methods of the ​​SubMessage ​​class found in `substitution.py` according to the specifications given here and in the docstrings. 
We have provided skeleton code for the following methods in the ​`SubMessage` ​​ class- your task is to implement them. Please see the docstring comment with each function for more information about the function specification.

* `__init__(self, text)`
* The getter methods:
    `get_message_text(self)`
    `get_valid_words(self)` Note: this should return a COPY of self.valid_words to prevent someone from mutating the original list.
* `build_transpose_dict(self, letters_permutation)`: returns a dictionary that maps each English letter (lowercase and uppercase) to the transposed (encrypted) version of the letter according to the `letters_permutation`. Please look at the docstring for more information.
* `apply_transpose(self, transpose_dict)`: returns an encrypted version of the message_text based on `transpose_dict` 
* `__eq__(self, other)`: You should override the `__eq__` function for the `SubMessage` class so that when two instances of this class have the same attributes (`message_text` and `valid_words`), then they should be considered equal (using `==` sign in python).


### Part 2: EncryptedSubMessage

Fill in the methods of the ​EncryptedSubMessage class found in `substitution` according to the specifications given here and in the docstrings.

Don't you want to know what your friends are saying? Given an encrypted message, if you know the substitution used to encode the message, decoding it is trivial. You could just replace each letter with the correct, decoded letter. The problem, of course, is that you don't know the substitution. We have a lot of options for trying different substitutions for the the frequent letters (`'e', 't', 'a', 'o', 'i', 'n'`). As with the Vigenère cipher, we can use the trick of testing (giving a proposed substitution) to see if the decoded words are real English words. We then keep the decryption that yields the most valid English words. 

The methods you should fill in are:
* `__init__(self, text)` **Hint**: Use the parent class constructor to make your code more concise.
* `decrypt_message(self)` Try every possible permutation of `'etaoin'` and find the one that maximizes the number of real English words. Please look at the docstring for more information.
**Note**: Running this method might take a while.

* `__eq__(self, other)`: You should override the `__eq__` function for the `EncryptedSubMessage` class so that when two instances of this class have the same attributes (`message_text` and `valid_words`) then they should be considered equal (using `==` sign in python).