def checkValidString(s: str) -> bool:
        l_cnt = 0
        s_cnt = 0
        l_loc = []
        s_loc = []

        for i, c in enumerate(s):
            if c=='(':
                l_cnt += 1
                l_loc.append(i)
            elif c==')':
                if s_cnt+l_cnt <= 0:
                    return False
                if len(l_loc)>0:
                    l_cnt -= 1
                    l_loc.pop()
                elif s_cnt>0 and l_cnt<0:
                    s_cnt -= 1
                    s_loc.pop()
            elif c=='*':
                s_cnt += 1
                s_loc.append(i)
        
        if l_cnt==0:
            return True
        elif s_cnt>0:
            for l1 in l_loc:
                for i, l2 in enumerate(s_loc):
                    if l2>l1:
                        l_cnt -= 1
                        s_loc[i] = 0
                        break
            if l_cnt <= 0:
                return True
        return False

if __name__ == "__main__":
    s_in = "("
    s_in2 = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
    s_in3 = "(((((()*)(*)*))())())(()())())))((**)))))(()())()"
    print(checkValidString(s_in3))