#Identify from given inputs if the triangle is isosceles,equilateral,scalene.

def triangle(self,nums:list[int])->str:
    a,b,c = nums[0],nums[1],nums[2]
    if a+b <=c or b+c <=a or c+a<=b:
        return 'none'
    elif a==b==c:
        return 'equilateral'
    elif a==b or b==c or c==a:
        return 'isosceles'
    else:
        return 'scalene'