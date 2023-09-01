#sha bruteforce
import hashlib
pieces =[
     'b53f0fd11d33ebec50064781135799d72d3d4ea2',
  '5678e0f829a7667e31ad20fa14b092dcb3b8992b',
  '9d4a0905daaa27073dcabe66adc59051a08240f0',
  '7b5feb45a9c246100091c32d660940fbfbbf75e3',
  '8dc0e8a48d516f33a8f8ac0ac20d8ae21212bd67',
  '27a868f2dc4ba35e5451942b0c267c27ef888742',
  '8604c899d98a3dbbd668f801222ba7a939c6ae5b',
  'dfa27014e5cc7c7c68422071de4c36570315c7e6',
  '8eee64e9ecdc7c8928b2e3a8c0d17e246136268d',
  '3836ced657531d5294f15f0f5b78bbb4e5f8d6ba',
  'cbc2f8710b4b394c594f7c5df8cba2317f086600',
  '1d1f764a6eee2b072e5ee5f4f2d7973950afe073',
  '08caae9561ae6679e7b0d84f197c1d03805cd258',
  'fd3ecd1ced67ca3b1f1c444a21ce5f2f25e37337',
  '9d2b06f0bbb0f46f0bdd20e635c2e0d187b1b472'
]
  
  
def cracker(hashed):
    for i in range(65281, 65375):
        for j in range(65281, 65375):
            for k in range(65281, 65375):
                for l in range(65281, 65375):
                    trial = chr(i)+chr(j)+chr(k)+chr(l)
                    res = hashlib.sha1(trial.encode("utf-8")).hexdigest()
                    if res == hashed:
                        return trial
    
    return ""


def main():
    decoded = ''
    for i in pieces:
        decoded += cracker(i)

    print(decoded)

if __name__ == "__main__":
    main()