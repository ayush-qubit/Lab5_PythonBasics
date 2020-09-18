from decimal import Decimal
import sys
def get_inputs(path):
    result=[]
    with open(path,'r') as file:
        result.append(file.readline())
    return result

if __name__ == "__main__":
    file_name=sys.argv[0]
    result=get_inputs(file_name)
    T=int(result[0])
    for i in T:
        H,M,S,a,b,c=result[i+1].split(sep=' ')
        hour_angle=(360/H)*a+(360/(H*M))*b+(360/(H*M*S))*c
        minute_angle=(360/M)*b+(360/(M*S))*c
        diff_angle=abs(float(hour_angle)-float(minute_angle))
        print(round(diff_angle,2))
