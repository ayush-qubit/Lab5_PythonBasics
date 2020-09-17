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
                d1[match][name]=score
            else:
                d1[match]={}
                d1[match][name]=score
            if name in d2:
                t=int(d2[name])
                t+=int(score)
                d2[name]=t
            else:
                d2[name]=score
    
    print(d1)
    l=list(d2.items())
    print(l)
