class HashTable:
    def __init__(self,size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
    
    def set_value(self,key,value):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for index , record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                bucket[index] = (key,value)
                return
        bucket.append((key,value))

    def get_value(self,key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        for index,record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                return record
        return "Key Not Found!"

    def __str__(self):
        return str(self.hash_table)

hast_table = HashTable(5)
hast_table.set_value("kno0109@mail.ru","Knyaz Harutyunyan 2003 , Armenia")
hast_table.set_value("kno0103@mail.ru","David Vardanyan 1999 , Armenia")
hast_table.set_value("kno0101@mail.ru","Armen Hakobyan 2003 , Armenia")
print(hast_table.get_value("kno0109@mail.ru"))
print(hast_table)