__author__ = 'caglar'
import random


class Cache(object):
    def __init__(self, size=32768, block_size=64, sets=2):
        self.size = size
        self.block_size = block_size
        self.sets = sets
        self.cache = list()
        self.line = size/sets*block_size

        self.__build()

    def __build(self):
        for i in range(line):
            self.cache.append(CacheLine(i, self.block_size, self.sets))

    def __repr__(self):
        return str(self.cache.__len__())

    def toquery(self,address):
        mask = (1<<32) - 1
        i=0
        while(i<<1)
        add_index = ((address << 20) & mask) >> 24
        add_data = address << 28 >> 28
        add_word = address << 30
        add_tag = address >> 20
        

    def read(self, address):
        for i in range(self.sets):
            if self.line[i].["tag"] is query["tag"] and self.line[i].['valid'] is True:
                self.__read_hit(i, query)
                return
        self.__read_miss(query)

    def __read_miss(self, set, query):
        self.request_line(self)

    def __read_hit(self, set, query):
        return self.line[set]["data"]

    def request_line(self, query):
        pass
#        rline = query["tag"],self.index
#       self.fill_line(rline)



#CacheLine is a Class for defining each cache blocks in cache hierarchy
#During initialization it build a static block of given sets sized array with given block size as byte
#It has only one method to fill remote block in.
class CacheLine(object):
    def __init__(self, index, size, sets):
        self.size = size
        self.sets = sets
        self.index = index
        self.line = list()
        self.__build()

    def __repr__(self):
        return repr(self.line)


#Initialize the first view of the cache.
#It will invoke build_line() for each line of the cache.
    def __build(self):
        for i in range(self.sets):
            self.line.append(self.__build_line())


#Build a line with default variables.
    def __build_line(self):
        data = bytearray(self.size)
        return {"tag": 0, "valid": False, "dirty": False, "used": False, "data": data}


# It fills into the line the corresponding block from the upper layer.
# Input "rline" is abbreviation of remote line formed as {tag, data}
# As default, it uses Not recently used, random replacement Policy


    def fill_line(self, rline):
        while True:
            i = random.randint(0, self.sets-1)
            if self.line[i]["used"] is False:
                self.line[i]["tag"] = rline["tag"]
                self.line[i]["valid"] = True
                self.line[i]["dirty"] = False
                self.line[i]["used"] = True
                self.line[i]["data"] = rline["data"]
                return i






a = CacheLine(63,2)
a.fill_line({"tag": 1, "data": b"Xxxxcxxvzcf"})
