"""

祥 -- a
瑞 -- b
生 -- c
辉 -- d
三 -- e
羊 -- f
献 -- g
气 -- h

"""
e = 1
for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for f in range(0,10):
                    for g in range(0,10):
                        for h in range(0,10):
                                if (a*1000+b*100+c*10+d)+(1000+f*100+g*10+b)==(10000+f*1000+c*100+b*10+h):
                                    if a!=b and a!=c and a!=d and a!=e and a!=f and a!=g and a!=h:
                                        if b!=c and b!=d and b!=e and b!=f and b!=g and b!=h:
                                            if c!=d and c!=e and c!=f and c!=g and c!=h:
                                                if d!=e and d!=f and d!=g and d!=h:
                                                    if e!=f and e!=g and e!=h:
                                                        if f!=g and f!=h:
                                                            if g!=h:
                                                                print (e,f,g,b)
