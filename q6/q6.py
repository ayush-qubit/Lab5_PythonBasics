from functools import reduce 
from collections import OrderedDict
class BlackMoneyHolder:
    def __init__(self,name,account_info):
        self.name=name
        self.account_info=account_info
        self.index=0
        self.account_info=OrderedDict(sorted(self.account_info.items()))
    
    def update_amount(self,bank_name,amount):
        if bank_name in self.account_info:
            self.account_info[bank_name]+=amount
        else:
            self.account_info[bank_name]=amount
    
    def total_black_money(self):
        return reduce(lambda x,y: x+y,self.account_info.values())
    
    def __iter__(self):
        self.index=0
        return self
    
    def __next__(self):
        try:
            self.index+=1
            return self[self.index-1]
        except IndexError:
            raise StopIteration

    def __str__(self):
        string=''
        for ele in self.account_info:
            string+=str(ele)+':'+str(self.account_info[ele])+'\n'
        return string
    
    
    def __eq__(self, other):
        a=reduce(lambda x,y: x+y,self.account_info.values())
        b=other.total_black_money()
        return a==b
    
    def __lt__(self, other):
        a=reduce(lambda x,y: x+y,self.account_info.values())
        b=other.total_black_money()
        return a<b
    
    def __gt__(self, other):
        a=reduce(lambda x,y: x+y,self.account_info.values())
        b=other.total_black_money()
        return a>b
    
    def __le__(self, other):
        a=reduce(lambda x,y: x+y,self.account_info.values())
        b=other.total_black_money()
        return a<=b
    
    def __ge__(self, other):
        a=reduce(lambda x,y: x+y,self.account_info.values())
        b=other.total_black_money()
        return a>=b
    
    def __len__(self):
        l=len(self.account_info)
        return l
    
    def __getitem__(self,pos):
        key=list(self.account_info)[pos]
        value=list(self.account_info.values())[pos]
        return (key,value)

name='Sonia Gandhi'
account_info={
    'A':100,
    'C':200,
    'B':300
}
B1=BlackMoneyHolder(name,account_info)
#print(B1)
account_info1={
    'A':100,
    'D':200,
    'C':300
}
B2=BlackMoneyHolder('Rahul',account_info1)
print(B1==B2,B1<B2,B1>B2,B1>=B2,B1<=B2)