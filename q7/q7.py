from decimal import Decimal
import sys
def get_inputs(path):
    result=[]
    with open(path,'r') as file:
        result=file.readlines()
    return result

if __name__ == "__main__":
    file_name=sys.argv[1]
    result=get_inputs(file_name)
    #print(result)
    T=int(result[0])
    for i in range(T):
        H,M,S,a,b,c=map(int,result[i+1].split(sep=' '))
        hour_angle=(360/H)*a+(360/(H*M))*b+(360/(H*M*S))*c
        minute_angle=(360/M)*b+(360/(M*S))*c
        diff_angle=abs(float(hour_angle)-float(minute_angle))
        print(round(Decimal(str(diff_angle)),2))
