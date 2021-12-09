import pickle, os

class db :
    
    def __init__(self, path=""):
        self.path = path #use only ".pickle", ".json", ".db" extension
        if not os.path.exists(self.path):
            f = open(self.path, "wb")
            pickle.dump({"file":"True"}, f)
            f.close()
        
    def get(self, key):
        with open(self.path,  "rb") as f:
            x = pickle.load(f)
            f.close()
            if not key in x.keys():
                return False
            else:
                return x[key]
        
    def set(self, key, data):
        with open(self.path,  "rb") as f:
            x = pickle.load(f)
            f.close()
            x[key] = data
            with open(self.path,"wb") as f:
                pickle.dump(x, f)
                f.close()
                
    def get_all(self):
        with open(self.path, "rb") as f:
            x = pickle.load(f)
            f.close()
            return x
        
    def put(self, d):
        with open(self.path, "rb") as f:
            x = pickle.load(f)
            f.close()
            res = {**x, **d}
            with open(self.path, "wb") as f:
                pickle.dump(res, f)
                f.close()

    def remove(self, key):
        f = open(self.path, "rb")
        x = pickle.load(f)
        f.close()
        if key in x.keys():
            del x[key]
        f = open(self.path, "wb")
        pickle.dump(x, f)
        f.close()

    def clear_all(self):
        x = {}
        f = open(self.path, "wb")
        pickle.dump(x, f)
        f.close()

