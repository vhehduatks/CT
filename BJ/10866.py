import sys
read=sys.stdin.readline

class Deque:
    def __init__(self):
        self.Q=[]

    def push_f(self,X):
        self.Q.insert(0,X)
    
    def push_b(self,X):
        self.Q.append(X)

    def pop_f(self):
        return self.Q.pop(0) if self.Q else -1

    def pop_b(self):
        return self.Q.pop() if self.Q else -1

    def size(self):
        return len(self.Q)
    
    def is_empty(self):
        return 1 if not self.Q else 0

    def front(self):
        return self.Q[0] if self.Q else -1
    
    def back(self):
        return self.Q[-1] if self.Q else -1
    
if __name__=="__main__":
    temp_Q=Deque()
    N=int(read())
    for _ in range(N):
        line=read().split()
        if line[0]=="push_front":
            temp_Q.push_f(int(line[1]))
        elif line[0]=="push_back":
            temp_Q.push_b(int(line[1]))
        elif line[0]=="pop_front":
            print(temp_Q.pop_f())
        elif line[0]=="pop_back":
            print(temp_Q.pop_b())
        elif line[0]=="empty":
            print(temp_Q.is_empty())
        elif line[0]=="size":
            print(temp_Q.size())
        elif line[0]=="front":
            print(temp_Q.front())
        elif line[0]=="back":
            print(temp_Q.back())