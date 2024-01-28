class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self. tinyUrl = 'http://tinyurl.com/'

    def encode(self, longUrl):
        if longUrl not in self.encodeMap:
            shortUrl = self.tinyUrl + str(len(self.encodeMap) + 1)
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
        return self.encodeMap[longUrl]
        

    def decode(self, shortUrl):
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))