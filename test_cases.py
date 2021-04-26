from vigenere import Message, PlaintextMessage, CiphertextMessage
from substitution import SubMessage, EncryptedSubMessage

def test_vigenere1():
  plaintext = PlaintextMessage('programming', [2, 9, 3])
  assert plaintext.get_message_text_encrypted() == 'rariadovlpp'


def test_vigenere2():
  plaintext = PlaintextMessage('Hello Every One', [2, 3, 5])
  assert plaintext.get_message_text_encrypted() == 'Jhqnr Gyjtb Qqj'
  print('Actual Output:  ', plaintext.get_message_text_encrypted())

def test_vigenere3():
  plaintext = PlaintextMessage('We UsEd To   sWiM tHe SaMe MoonLight Waters!', [18, 11, 5, 25, 13])
  assert plaintext.get_message_text_encrypted() == 'Op TfWo Sb   rJaX sUw XzZw RnbfWnful Bzgwcx!'

def test_vigenere4():
  p = PlaintextMessage('hello', [1,2])
  a = p.get_valid_words()
  a.append('BBBB')
  a.append('CCCC')
  assert len(p.get_valid_words()) == 55901
  m = Message('Bye')
  b = m.get_valid_words()
  b.append('DDDDD')
  b.append('EEEEE')
  assert len(m.get_valid_words()) == 55901
  assert p.get_message_text() == 'hello'

def test_vigenere5():
  p = PlaintextMessage('Caress ThE OnE, ThE Never-Fading RaIn iN your hEArt--ThE tears of snOw-wHitE soRroW', [17, 11, 12, 5, 16, 8])
  a = p.get_key()
  a.append(4)
  c2 = p.get_message_text_encrypted()
  assert c2 == 'Tldjia EtJ WeP, JpV Zjlmi-Rftqer WqQe uS gffd xMRcf--ByP yuiid tv jyAb-eYtfJ afCdtM'

def test_vigenere6():
  p = PlaintextMessage("All the world's a stage and we are home again, home again", [2, 3, 5, 5, 8, 13, 21])
  c1 = p.get_message_text_encrypted()
  k1 = p.get_key()
  p.change_key([2, 8, 1, 4, 25])
  k2 = p.get_key()
  c2 = p.get_message_text_encrypted()
  
  assert c1 == "Coq buz ztwtq'u f agvih fvq yh fzr jrrj nbcls, ujoh fondp"
  assert k1 == [2, 3, 5, 5, 8, 13, 21]
  assert c2 == "Ctm sjm antte'r i wscof zpl ad isi jwni cobmm, islg bkzkv"
  assert k2 == [2, 8, 1, 4, 25] 

def test_vigenere7():
  c = CiphertextMessage('Jhqnr Gyjtb Qqj')
  d = c.decrypt_message()
  assert d == ([2, 3, 5], 'Hello Every One')

def test_vigenere8():
  c = CiphertextMessage('"Oz Jzf Eclty Qzc Alddtyr Epded zc Oz Jzf Eclty Qzc Ncpletgp Tybftcj?" --Yzlx Nszxdvj')
  d = c.decrypt_message()
  assert d == ([11], '"Do You Train For Passing Tests or Do You Train For Creative Inquiry?" --Noam Chomsky')

def test_vigenere9():
  p = PlaintextMessage("Hello Everybody", [2,3,4])
  c = CiphertextMessage("Ok Everybody")
  assert p.get_message_text() == "Hello Everybody"
  assert c.get_message_text() == "Ok Everybody"


def test_vigenere10():
  c = CiphertextMessage('Ymhpz Qwdrmf Etlb Jwg Idp, Epq Zqdb Zn Epq Eactp Euwt Ywf. Ipid Qf Tuvm Lzyzz Lvp Qf Kmy Zpdqc Np Gdmp Ba Pgcb Jwg.           --Fjzuzv Wizyqeemd')
  d = c.decrypt_message()
  assert d == ([11, 8, 12], 'Never Forget What You Are, The Rest Of The World Will Not. Wear It Like Armor And It Can Never Be Used To Hurt You.           --Tyrion Lannister')


  
def test_sub1():
  message = SubMessage("Nice To Meet You!")
  permutation = "anotei"
  enc_dict = message.build_transpose_dict(permutation)
  assert message.apply_transpose(enc_dict) == "Ieca Nt Maan Ytu!"

def test_sub2():
  message = SubMessage("It's LiKE a MEEEeNTAAal JuuuNgle!!")
  permutation = "TiANoE"
  enc_dict = message.build_transpose_dict(permutation)
  assert message.apply_transpose(enc_dict) == "Oi's LoKT a MTTTtEIAAal JuuuEglt!!"

def test_sub3():
  p = SubMessage('hello')
  a = p.get_valid_words()
  a.append('BBBB')
  a.append('CCCC')
  assert len(p.get_valid_words()) == 55901
  m = EncryptedSubMessage('Bye')
  b = m.get_valid_words()
  b.append('DDDDD')
  b.append('EEEEE')
  assert len(m.get_valid_words()) == 55901
  assert p.get_message_text() == 'hello'
  assert m.get_message_text() == 'Bye'



def test_sub4():
  a1 = SubMessage('Hello')
  a2 = SubMessage('Hello')
  a3 = SubMessage('hello')
  assert a1 == a2
  assert a1 != a3

class Dummy:
  def __init__(self, text):
    self.message_text = text
  def set_valid_words(self, words):
    self.valid_words = words

def test_sub5():
  a1 = SubMessage('Hello')
  a2 = Dummy('Hello')
  a3 = SubMessage('Hello')
  a2.set_valid_words(a1.get_valid_words())
  assert a1 == a3
  assert a1 != a2

def test_sub6():
  enc_message = EncryptedSubMessage('OeGHN GtnHaRS, tod OIW My WtnCH bAgEOs')
  assert enc_message.decrypt_message() == 'NiGHT GatHeRS, and NOW My WatCH bEgINs'

def test_sub7():
  e1 = EncryptedSubMessage('HelLo1!')
  e2 = EncryptedSubMessage('HelLo1!')
  e3 = EncryptedSubMessage('HelLo3!')
  s1 = SubMessage('HelLo1!')
  d1 = Dummy('HelLo1!')
  d1.set_valid_words(e1.get_valid_words())
  assert e1 == e2
  assert e1 != e3
  assert e1 != s1
  assert s1 != e1
  assert e1 != d1
  assert d1 != e1

def test_sub8():
  e1 = EncryptedSubMessage("Fnr Mellenos nf Ytars, Maokeod Levtd Jusi Lekt Iht aoemals. Ihto Snmtiheog Happtotd Whech Uoltashtd iht Pnwtr nf Nur Emageoaieno. Wt Ltarotd in Ialk aod Wt Ltarotd in Lesito. Nur grtaitsi hnpts cnuld btcnmt rtaleiy eo iht fuiurt. All wt ottd in dn es makt surt wt kttp ialkeog.   [Sitphto Hawkeog]")
  assert e1.decrypt_message() == "For Millions of Years, Mankind Lived Just Like The animals. Then Something Happened Which Unleashed the Power of Our Imagination. We Learned to Talk and We Learned to Listen. Our greatest hopes could become reality in the future. All we need to do is make sure we keep talking.   [Stephen Hawking]"

def test_sub9():
  e1 = EncryptedSubMessage("If ytu cae'n oxplaie in simply, ytu dte'n uedorsnaed in woll oetugh. --Alborn Oiesnoie")
  assert e1.decrypt_message() == "If you can't explain it simply, you don't understand it well enough. --Albert Einstein"

def test_sub10():
  e1 = EncryptedSubMessage("Ovorlesnaig Iood Wtuld Ytu ploeso? Eiswor Mo eid Meko Mo Ctmplono")
  assert e1.decrypt_message() == "Everlasting Need Would You please? Answer Me and Make Me Complete"

  e2 = EncryptedSubMessage("Iha seog ihti togals snog Iha spall ihti ctlls, Iha Gtiharnog Iha mtgnc ihti mnghi brnog Aiarotl lnfa, Iha Gtiharnog")
  assert e2.decrypt_message() == "The song that angels sing The spell that calls, The Gathering The magic that might bring Eternal life, The Gathering"

  




  
