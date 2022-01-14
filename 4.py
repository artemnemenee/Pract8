def most_word(m):
    t=[]
    with open(m, 'r') as f:
        nums = f.read().splitlines()
        for i in nums:
            t.extend(i.split())
            t = list(reversed(sorted(t, key=len)))
            len_max = len(t[0])
            for i in t:
                if len(i) == len_max:
                    print(i)
                else:
                    break
most_word('text4.txt')
