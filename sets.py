from hashtable import HashTable

class Set(HashTable):
    def __init__(self, init_size=8):
          super(Set, self).__init__()

    def bucket_index(self, key):
        return super.bucket_index(super.self, key)

    def length(self):
        length = 0
        for bucket in self.buckets:
            length += bucket.length()
        return length
