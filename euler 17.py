a=['one','two','three','four','five','six','seven','eight','nine','ten','eleven'
   ,'twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty',
   'thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred']
dic={30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7,0:0}
for i in range(1,21):
   dic[i]=len(a[i-1])
s=11
# for i in range(1,10):
#    s+=72*dic[i]
# for i in range(10,20):
#    s+=(9*dic[i])
# s+=99*9*3
#
# for i in range(20,99,10):
#    s+=(90*dic[i])
# s+=dic[100]*900
# for i in range(1,10):
#    s+=(100*dic[i])
# s+=11
# print(s)
def getsums(a,s=0,p=1):
   x=a//p
   if(x==0):
      print(s)
      return s
   elif(p>=10):
      s+=(dic[a//100]+10)
      if(a//100==0):
         s-=3
      return getsums(a,s,p*10)
   elif(p<10):
      if(10<a%100<20):
         s+=dic[a%100]
      else:
         s+=dic[a%10]
         if(a>10):
            s+=dic[((a//10)%10)*10]
      return getsums(a,s,p*100)
for i in range(1,1000):
  s+=getsums(i)
print(s)