import pickle


class book:
    def __init__(self, title):
        self.title = title


a = book("Python3 Program")
b = book("Design Patterns")
c = book("Gang of four")
d = book("Non-software examples of DP")

# file=open("test.pkl",'wb')
# pickle.dump(a,file)
# pickle.dump(b,file)
# #file.close()

with open("test.pkl", 'wb') as file:
    pickle.dump(a, file)
    pickle.dump(b, file)

# file=open("test.pkl",'ab')
# pickle.dump(c,file)
# pickle.dump(d,file)
# #file.close()

with open("test.pkl", 'ab') as file:
    pickle.dump(c, file)
    pickle.dump(d, file)

print("Reading from file")

file2 = open("test.pkl", 'rb')
try:
    while True:
        s = pickle.load(file2)
        print(s.title)
except:
    print("Reached EoF")

print("Reading completed")
# file2.close()
