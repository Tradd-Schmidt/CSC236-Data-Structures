def anagrams(s):
    if s == "":
        return[s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                ans.append(s[0]+w[pos:])
        return ans

print(anagrams("Big"))
