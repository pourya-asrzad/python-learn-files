class Text(str):
    def duplicate(self):
        return self +' '+ self
    

class TrackableList(list):
    def append(self,object):
        print("Appended !!")
        super().append(object)
        

golam =TrackableList()
golam.append('1')