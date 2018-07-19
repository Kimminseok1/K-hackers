def makeCodebook():#암호화 복호화 하는데 사용할 딕셔너리를 만드는 함수
    decbook={'5':'a','2':'b','#':'d','8':'e','1':'f','3':'g','4':'h','6':'i','0':'1','9':'m',\'*':'n','%':'o','=':'p','(':'r',')':'s',';':'t','?':'u','@':'v',':':'y','7':'z'}
             
    encbook = {}
    for k in decbook:
        val = decbook[k]
        encbook[val] = k


    return encbook, decbook


def encrypt(msg,encbook): #암호화를 담당하는 함수
   for c in msg:
      if c in encbook:
        msg = msg.replace(c, encbook[c])


   return msg

def decrypt(msg, decbook):# 복호화를 담당하는 함수
   for c in msg:
      in c in decbook:
        msg = msg.replace(c, decbook[c])


    return msg
             
def main():
    a,b =makeCodebook()
    msg = input("fdsfhjsfs")
    c = emcrypt()
    ptint(c)
