if __name__ == "__main__":
    d1={}
    d2={}
    n=int(input())
    for _ in range(n):
        match,players=input().split(sep=':')
        players=list(players.split(sep=','))
        for player in players:
            name,score=player.split(sep='-')
            if match in d1:
                d1[match][name]=int(score)
            else:
                d1[match]={}
                d1[match][name]=int(score)
            if name in d2:
                t=int(d2[name])
                t+=int(score)
                d2[name]=t
            else:
                d2[name]=int(score)
    
    print(d1)
    l=list(d2.items())
    print(sorted(l,key=lambda x: (x[1],x[0]),reverse=True))