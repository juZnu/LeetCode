import hashlib


def encode( longUrl):
    pass
    
def decode( shortUrl):
    pass
print(decode(encode(longUrl= "https://leetcode.com/problems/design-tinyurl")))

url = "https://leetcode.com/problems/design-tinyurl"
print(hashlib.md5(url.encode()).hexdigest())