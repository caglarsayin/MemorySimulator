__author__ = 'caglar'
import random


class Cache(object):
    def __init__(self, size=32768, block_size=64, sets=2):
        self.size = size
        self.block_size = block_size
        self.sets = sets
        self.addr_size = 32
        self.cache = list()
        self.line = size/sets*block_size
        self.block_addr_len = self.__calculate_addr_len(self.block_size)
        self.line_addr_len = self.__calculate_addr_len(self.line)
        self.tag_addr_len = self.addr_size - self.block_addr_len - self.line_addr_len
        self.__build()

    def __repr__(self):
        return str(self.cache.__len__())

    def __getitem__(self, address):
        return self.read_request(address)

    def __build(self):
        for i in range(self.line):
            self.cache.append(CacheLine(i, self.block_size, self.sets))

    def __calculate_addr_len(self,size):
        i = 0
        result = 1
        while size >= result:
            result <<= 1
            i += 1
        return i

    def toquery(self,address):
        mask = (1<<32) - 1
        query = {"tag" : 0, "index" : 0, "block" : 0}
        query["block"] = ((address << (self.addr_size - self.block_addr_len)) & mask) >> (self.addr_size - self.block_addr_len)
        query["index"] = (address >> (self.block_addr_len)) << ((self.addr_size - self.line_addr_len) & mask) >> (self.addr_size - self.line_addr_len)
        query["tag"] = address >> (self.addr_size - self.tag_addr_len)
        return query
        

    def read_request(self, address):
        query = self.toquery(address)
        for i in range(self.cache[query["index"]].sets):
            if (self.cache[query["index"]].line[i]["tag"] is query["tag"]) and (self.line[i]['valid'] is True):
                return self.__read_hit(i, query)
        return self.__read_miss(query)

    def __read_miss(self, set, query):
        self.request_line(self)

    def __read_hit(self, i, query):
        return self.cache[query["index"]].line[i]["data"]

    def request_line(self, query):
        pass
#        rline = query["tag"],self.index
#       self.fill_line(rline)




class CacheLine(object):
#CacheLine is a Class for defining each cache blocks in cache hierarchy
#During initialization it build a static block of given sets sized array with given block size as byte
#It has only one method to fill remote block in.
    def __init__(self, index, size, sets):
        self.size = size
        self.sets = sets
        self.index = index
        self.line = list()
        self.__build()

    def __repr__(self):
        return repr(self.line)


    def __build(self):
#Initialize the first view of the cache.
#It will invoke build_line() for each line of the cache.
        for i in range(self.sets):
            self.line.append(self.__build_line())


    def __build_line(self):
#Build a line with default variables.
        data = bytearray(self.size)
        return {"tag": 0, "valid": False, "dirty": False, "used": False, "data": data}

    def fill_line(self, rline):
# It fills into the line the corresponding block from the upper layer.
# Input "rline" is abbreviation of remote line formed as {tag, data}
# As default, it uses Not recently used, random replacement Policy
        while True:
            i = random.randint(0, self.sets-1)
            if self.line[i]["used"] is False:
                self.line[i]["tag"] = rline["tag"]
                self.line[i]["valid"] = True
                self.line[i]["dirty"] = False
                self.line[i]["used"] = True
                self.line[i]["data"] = rline["data"]
                return i