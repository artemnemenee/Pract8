def strnum(a, new_name):
        t=""
        k = 1
        with open(a, 'r') as f:
            nums = f.read().splitlines()
        for i in nums:
            t+=str(k)+": "+i+"\n"
            k+=1
        with open(new_name, 'w') as f:
            f.write(t)
strnum("text.txt", "text2.txt")
