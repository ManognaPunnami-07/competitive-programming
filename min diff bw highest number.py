if k==1:
            return 0
        l=[t for t in combinations(nums,k)]
        print(l)
        d=[]
        for i in l:
            i=list(i)
            i.sort()
            diff=i[-1]-i[0]
            d.append(diff)
        d.sort()
        return d[0]

        






