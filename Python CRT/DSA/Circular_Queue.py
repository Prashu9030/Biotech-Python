
class pq:
    def __init__(self):
        self.q=[]
        self.a=0
    def add(self,newdata):
        self.q.append(newdata)
        print(self.q)
        self.a+=1
    def delete(self):
        maxv=max(self.q)
        maxi=self.q.index(maxv)
        del self.q[maxi]
        print("deleted data=",maxv)
        print(self.q)
        self.a-=1




p1=pq()
p1.add(12)
p1.add(1)
p1.add(14)
p1.add(17)
while p1.a:
    p1.delete()