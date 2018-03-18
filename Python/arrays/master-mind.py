#Master-mind
def evaluate(guess, secret):
        b, w = 0, 0
        gs, ss = set([]), set([])
        for i in range(4):
            if guess[i] == secret[i]:
                b = b + 1 
            else:
                gs.add(guess[i])
                ss.add(secret[i])
        return (('b'*b)+('w'*(len(gs.intersection(ss)))) )
        #return b, len(gs.intersection(ss))

print (evaluate('YGBR','YGWG'))
