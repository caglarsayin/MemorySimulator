import caches

l1 = caches.Cache()
memory = caches.Memory()
memory[34] = 4
l1.setsuper(memory)
print l1[2515]
