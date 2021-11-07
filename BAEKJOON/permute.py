
# def permute(num):
#     result=[]
#     prev_elements=[]

#     def dfs(elems):
#         if len(elems)==0:
#             result.append(prev_elements[:])
        
#         for e in elems:
#             next_elements=elems[:]
#             next_elements.remove(e)

#             prev_elements.append(e)
#             dfs(next_elements)
#             prev_elements.pop()
        
#     dfs(num)
#     return result

# temp=[1,2,3]
# print(permute(temp))    


def permute(n,Arr):
    ret=[]
    result=[]
    def recur(nextarr):
        if len(result)==n:
            ret.append(result[:])
            return
        if not nextarr:
            return

        
        
        for i in nextarr:
            temp=nextarr[:]
            result.append(i)
            temp.remove(i)
            recur(temp)
            result.pop()
    
    recur(Arr)
    return ret

print(permute(3,[1,2,3]))