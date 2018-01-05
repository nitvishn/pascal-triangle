from math import *
import time
from itertools import permutations

def sieve(numbers,n):
    for m in range(n*n,len(numbers)+1,2*n):
        numbers[m-1]=False

def primesFromFile(filename):
    file=open(filename, "r")
    primes=[]
    for line in file:
        line.replace('\n',"")
        line=int(line)
        primes.append(line)
    return primes

class Fraction(object):
    def __init__(self, numer, denom=1):
        self.numer=numer
        self.denom=denom
        self.simplify()
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def setNumer(self, numer):
        self.numer=numer
    def setDenom(self, denom):
        self.denom=denom
    
    def value(self):
        return float(self.numer)/self.denom

    def reciprocal(self):
        return Fraction(self.getDenom(),self.getNumer())
    
    def recurring_cycles(self):
        denom=self.getDenom()
        cursor=(self.getNumer()*10)%denom
        cycles=[]
        count=0
        while((cursor not in cycles) and count<denom):
            cycles.append(cursor)
            cursor=(cursor*10)%denom
            count+=1
            if(cursor==0):
                return cursor
        return count
    
    def simplify(self):
        num1=self.getNumer()
        num2=self.getDenom()
        while(not(int(num1)==num1 and int(num2)==num2)):
            num1*=10
            num2*=10
        primes = intersection(prime_factors(abs(num1)), prime_factors(abs(num2)))
        if(len(primes)<1):
            return 
        i=0
        prime=primes[i]
        while(num1%prime==0 and num2%prime==0 and len(primes)>0):
            while(num1%prime==0 and num2%prime==0):
                num1/=prime
                num2/=prime
            del primes[i]
            if(len(primes)==0):
                break
            prime=primes[i]
        self.setNumer(num1)
        self.setDenom(num2)
    
    def __str__(self):
        return '('+str(int(self.getNumer()))+'/'+str(int(self.getDenom()))+')'
        
    def __eq__(self, other):
        self.simplify()
        other.simplify()
        if(self.getNumer()==other.getNumer()):
            if(self.getDenom()==other.getDenom()):
                return True
        return False
        
def get_digits(number):
    digits=set()
    number=str(number)
    for char in number:
        digits.add(int(char))
    return digits

def convertNumbers(numbers):
    primes=[]
    for index in range(len(numbers)):
        if(numbers[index]==True):
            primes.append(index)
    return primes

def primes_under(limit):
    upper=int(sqrt(limit))
    if(upper<10):
        upper=int(limit)
    sieve=[False]*limit
    sieve[2]=True
    sieve[3]=True
    test1=set([1, 13, 17, 29, 37, 41, 49, 53])
    for x in range(1, upper+1):
        for y in range(1, upper+1):
            n=(4* x**2)+y**2
            if(n<=limit and (n%12==1 or n%12==5)):
                sieve[n]=True
                
            n=(3* x**2)+y**2
            if(n<=limit and n%12==7):
                sieve[n]=True
            
            n=(3* x**2)-y**2
            if(x>y and n%12==11 and n<=limit):
                sieve[n]=True
    for r in range(1, upper):
        if(sieve[r]):
            for i in range(r**2, limit, r**2):
                sieve[i]=False
    return convertNumbers(sieve)

def isPrime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def number_from_digits(digits):
    number=''
    for digit in digits:
        number+=str(digit)
    return number

def number_rotations(number):
    rotations=[]
    number=str(number)
    current=number[1:]+number[0]
    rotations.append(current)
    while(current!=number):
        current=current[1:]+current[0]
        rotations.append(current)
    return rotations
        
    
def factorize(number):
    primes=primes_under(int(sqrt(number)))
    powernums=[]
    for prime in primes:
        if(number==1):
            break
        power=0
        while(number%prime==0):
            number=int(number/prime)
            power+=1
        powernums.append(power+1)
    product=1
    for number in powernums:
        product*=number
    return product

def pascalTriangle(length):
    assert length>=5 and type(length)==int
    triangle=[[1],[1,]]
    n=2
    k=2
    for i in range(length):
        k+=1
        if(n==k-1):
            triangle[n-1].append(1)
            n+=1
            k=2
            triangle.append([1,])
        triangle[n-1].append(triangle[n-2][k-2]+triangle[n-2][k-1])
    return triangle

def factors_raw(n):
    """
    Returns the factors of the number.
    factors may be repeated, to ensure that the
    product of the factors is equal to the number.
    """
    divisors=[]
    for i in range(2,int(sqrt(n))+int(n)):
        if(n%i==0):
            if(n/i==i or i==1):
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(int(n/i))
    return divisors

def intersection(list1, list2):
    return list(set(list1).intersection(list2))

def simplify_fraction(fraction):
    num1=fraction.getNumer()
    num2=fraction.getDenom()
    while(not(int(num1)==num1 and int(num2)==num2)):
        num1*=10
        num2*=10
    primes = intersection(prime_factors(num1), prime_factors(num2))
    if(len(primes)<1):
        return Fraction(num1, num2)
    i=0
    prime=primes[i]
    while(num1%prime==0 and num2%prime==0 and len(primes)>0):
        if(num1%prime==0 and num2%prime==0 and len(primes)>0):
            num1/=prime
            num2/=prime
            del primes[i]
            if(len(primes)==0):
                break
            prime=primes[i]
    return Fraction(num1, num2)


def num_factors(n):
    facts=0
    for prime in primes:
        if(prime>n):
            break
        if(n%prime==0):
            facts+=1
    return facts


def fib():
    cursor1=1
    cursor2=1
    temp=0
    yield cursor1
    yield cursor2
    while(True):
        temp=cursor1+cursor2
        cursor1=cursor2
        cursor2=temp
        yield temp


def squares_under(n):
    squares=set()
    for i in range(1, ceil(sqrt(n))):
        squares.add(i**2)
    return squares


def odds():
    cursor=9
    while(True):
        yield cursor
        cursor+=2


def divisible(num, list1):
    for element in list1:
        if(num%element==0):
            return True
    return False


def odd_composites():
    primes=set(primes_under(1000000))
    for number in odds():
        if number not in primes:
            yield number
            continue
        else:
            if(divisible(number, primes)):
                yield number
            else:
                primes.add(number)
                continue


def factorial(x):
    product=1
    for i in range(2, x+1):
        product*=i
    return product


def combinations(n, r):
    return int(fact(n)/(fact(r)*fact(n-r)))


def digitsum(n):
    n=str(n)
    tot=0
    for c in n:
        tot+=int(c)
    return tot


def prime_factorise(n):
    """

    Recursive algorithm to prime factorise a number.

    First, find a prime factor for n. Add it to a list, L.

    :param n:
    :return list of primes whose product is n.:

    """
    L=[] #List of factors, factors need not be prime.

    for prime in primes:
        if n%prime==0:
            L.append(prime)
            if(n/prime != 1):
                L.extend(prime_factorise(n/prime))
                return L
            return L

def randomFunction(x):
    return 7 - 2**x

def binarySearch(upperBound, lowerBound, epsilon, f):
    value=(upperBound+lowerBound)/2
    x=f(value)

    if(abs(x)<epsilon):
        return value
    elif(x<0):
        return binarySearch(value, lowerBound, epsilon, f)
    else:
        return binarySearch(upperBound, value, epsilon, f)

def log(number, base, significantFigures=4):

    if (number<=0):
        raise ValueError

    def logFunction(x):
        return number-base**x

    return round(binarySearch(number, -number, 10**(-significantFigures), logFunction), significantFigures)

if __name__ == "__main__":

    for i in range(1, 100):
        print(log(i, 10))