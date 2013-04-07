#!/usr/bin/python

import unittest

SHOW_PRINT_MSGS = False

# 2.1: Computing Parity
def parity1(someInt):
    if SHOW_PRINT_MSGS:
        print "Calculating parity for: {0}, which is {1}".format(someInt, bin(someInt))
    parity = 0
    while someInt > 0:
        if someInt & 1 == 1:
            parity ^= 1
        someInt >>= 1
    if SHOW_PRINT_MSGS:
        print "parity is {0}\n".format(parity)
    return parity   

def dropLowestSetBit(someInt):
    if SHOW_PRINT_MSGS:
        print "Dropping lowest set bit for {0}, which is {1}".format(someInt, bin(someInt))
    result = someInt & (someInt - 1)
    if SHOW_PRINT_MSGS:
        print "Result is {0}, which is {1}".format(result, bin(result))
    return result

def parity2(someInt):
    if SHOW_PRINT_MSGS:
        print "Calculating parity2 for: {0}, which is {1}".format(someInt, bin(someInt))
    parity = 0
    while someInt > 0:
        parity ^= 1
        someInt = dropLowestSetBit(someInt)
    if SHOW_PRINT_MSGS:
        print "parity is {0}\n".format(parity)
    return parity

'''
PRECOMPUTED_PARITY_TABLE = (2**16) * [0]

def constructPrecomputedParityTable():
    for i in range(0, len(PRECOMPUTED_PARITY_TABLE)):
        PRECOMPUTED_PARITY_TABLE[i] = parity2(i)

def parity3(someInt):
    print "Calculating parity3 for: {0}, which is {1}".format(someInt, bin(someInt))
    reverseBits63to48 = PRECOMPUTED_PARITY_TABLE[(someInt >> 48) & 0xFFFF]
    reverseBits47to32 = PRECOMPUTED_PARITY_TABLE[(someInt >> 32) & 0xFFFF] << 16
    reverseBits31to16 = PRECOMPUTED_PARITY_TABLE[(someInt >> 16) & 0xFFFF] << 32
    reverseBits15to0 = PRECOMPUTED_PARITY_TABLE[someInt & 0xFFFF] << 48
    parity = reverseBits15to0 | reverseBits31to16 | reverseBits47to32 | reverseBits63to48
    print "parity is {0}".format(parity)
'''

# 2.2: Swapping bits
def extractLowestSetBit(someLong):
    if SHOW_PRINT_MSGS:
        print "Extracting the lowest set bit for {0}, which is {1}".format(someLong, bin(someLong))
    result = someLong & ~(someLong -1)
    if SHOW_PRINT_MSGS:
        print "Result is {0}, which is {1}".format(result, bin(result))
    return result

def getBitAtIndex(someLong, i):
    if SHOW_PRINT_MSGS:
        print "Extracting the bit at index {0} for {1}".format(i, someLong)
    result = 1 if ((someLong & (1 << i)) != 0) else 0
    if SHOW_PRINT_MSGS:
        print result
    return result

def swapBits(someLong, i, j):
    bitAtIndexI = getBitAtIndex(someLong, i)
    bitAtIndexJ = getBitAtIndex(someLong, j)
    if bitAtIndexI ^ bitAtIndexJ:
        if SHOW_PRINT_MSGS:
            print "swapping bits {0} and {1} for {2}, which is {3} in binary".format(i, j, someLong, bin(someLong))
        someLong ^= (1 << i)
        someLong ^= (1 << j)
    if SHOW_PRINT_MSGS:
        print "result is {0}, which is {1} in binary\n".format(someLong, bin(someLong))
    return someLong

# 2.3: Bit reversal
def reverseBitsRegular(someLong):
    if SHOW_PRINT_MSGS:
        print "Reversing bits for {0}, which is {1} in binary".format(someLong, bin(someLong))
    for i in range(0, 32):
        someLong = swapBits(someLong, i, 63 - i)
    if SHOW_PRINT_MSGS:
        print "result is {0}, which is {1} in binary\n".format(someLong, bin(someLong))
    return someLong

# 2.4: Closest Integers with the same weight
def closestIntSameWeight(x):
    if SHOW_PRINT_MSGS:
        print "Calculating closestIntSameWeight for {0}, which is {1} in binary".format(x, bin(x))
    for i in range(0, 64):
        ithBit = getBitAtIndex(x, i)
        jthBit = getBitAtIndex(x, i + 1)
        if ithBit != jthBit:
            closestInt = swapBits(x, i, i+1)
            if SHOW_PRINT_MSGS:
                print "Calculated closestIntSameWeight for {0} is {1}, or {2} in binary\n".format(x, closestInt, bin(closestInt))
            return closestInt

# 2.5 Printing power set
def printPowerSet(myList):
    print "Printing powerset for {0}".format(myList)
    myListSet = set(myList)
    myUniqueList = list(myListSet)
    setSize = len(myUniqueList)
    # Get number of subsets = 2^setSize
    numSubsets = 1 << setSize
    for i in range(0, numSubsets):
        subSetList = []
        # Go through each bit, as the number of bits is equal to setSize, and if set, add to subset
        for j in range(0, setSize):
            if getBitAtIndex(i, j):
                subSetList.append(myUniqueList[j])
        print set(subSetList)
    print


# 2.6 String to int and int to string

def charToInt(someChar, someBase=10):
    charOrd = ord(someChar)
    aOrd = ord('A')
    someInt = 0

    if charOrd >= aOrd:
        someInt = charOrd - aOrd + 10
    else:
        zeroOrd = ord('0')
        someInt = charOrd - zeroOrd

    if someInt < someBase:
        return someInt
    else:
        raise Exception("Character {0} is not numeric in base {1}".format(someChar, someBase))

def intToChar(someInt, someBase=10):
    if (someInt >= 0 and someInt < someBase):
        if (someInt < 10):
            return chr(ord('0') + someInt)
        else:
            return chr(ord('A') + someInt - 10)
    else:
        raise Exception("Cannot convert integer {0} to a character".format(someInt))

def stringToInt(someString, someBase=10):
    someInt = 0
    if len(someString) == 0:
        raise Exception("Cannot convert empty string to integer")
    isNegative = (someString[0] == '-')
    startIndex = 1 if isNegative else 0
    multiplier = -1 if isNegative else 1
    if SHOW_PRINT_MSGS:
        print "Converting {0} to integer".format(someString)
    for i in range(startIndex, len(someString)):
        someChar = someString[i]
        try:
            charInt = charToInt(someChar, someBase)
        except Exception, e:
            print str(e)
            return
        someInt = (someBase * someInt + charInt)
    if SHOW_PRINT_MSGS:
        print "Converted integer is {0}\n".format(someInt)
    return multiplier * someInt

def intToString(someInt, someBase=10):
    isNegative = (someInt < 0)
    someString = ''
    someInt = abs(someInt)
    if SHOW_PRINT_MSGS:
        print "Converting {0} to a string".format(someInt)
    while (someInt > 0):
        remainder = someInt % someBase
        try:
            remainderChar = intToChar(remainder, someBase)
        except Exception, e:
            print str(e)
            return
        someString = remainderChar + someString
        someInt = someInt / someBase
    someString = '-' + someString if isNegative else someString
    if SHOW_PRINT_MSGS:
        print "Resulting string is {0}\n".format(someString)
    return someString

# 2.7
# Converting an integer string from one base to another.
def convertToBase(someIntString, base1, base2):
    if SHOW_PRINT_MSGS:
        print "Converting {0} in base {1} to base {2}".format(someIntString, base1, base2)
    integerInBase1 = stringToInt(someIntString, base1)
    stringInBase2 = intToString(integerInBase1, base2)
    if SHOW_PRINT_MSGS:
        print "Converted string in base {0} is {1}\n".format(base2, stringInBase2)
    return stringInBase2

# 2.8
# Spreadsheet column encoding
def ssDecodeColId(columnIdString):
    if SHOW_PRINT_MSGS:
        print "Encoding the following column id {0} to an integer".format(columnIdString)
    colIdInt = 0
    for someChar in columnIdString:
        colIdInt = 26 * colIdInt + ord(someChar) - ord('A') + 1
    if SHOW_PRINT_MSGS:
        print "The encoded column id integer is {0}\n".format(colIdInt)
    return colIdInt

# 2.9
# Elias Gamma Encoding
def encodeElias(someIntList):
    if SHOW_PRINT_MSGS:
        print "Encoding the following list {0}".format(someIntList)
    stringEncoding = ""
    for someInt in someIntList:
        someIntString = intToString(someInt, someBase=2)
        stringEncoding = stringEncoding + '0' *( len(someIntString) - 1) + someIntString
    if SHOW_PRINT_MSGS:
        print "The Encoding resulted in the following string {0}\n".format(stringEncoding)
    return stringEncoding

# Elias Gamma Decoding
def decodeElias(someEncodingString):
    if SHOW_PRINT_MSGS:
        print "Decoding the following string {0}".format(someEncodingString)
    someIntList = []
    numZeroes = 0
    index = 0
    stringLen = len(someEncodingString)
    while index <  stringLen:
        if someEncodingString[index] is '0':
            numZeroes += 1
            index += 1
        else:
            newIndex = index + numZeroes + 1
            subString = someEncodingString[index : newIndex]
            someInt = stringToInt(subString, someBase=2)
            someIntList.append(someInt)
            numZeroes = 0
            index = newIndex
    if SHOW_PRINT_MSGS:
        print "The decoding is the following list {0}\n".format(someIntList)
    return someIntList

# Greatest Common Divisor (Problem 2.10)
def isEven(someInt):
    return someInt & 1 == 0

def gcd(a, b):
    isAEven = isEven(a)
    isBEven = isEven(b)
    someGcd = 0
    if a == 0 or b == 0:
        someGcd = 0
    elif a == b:
        someGcd = a
    elif isAEven and isBEven:
        someGcd = gcd(a>>1, b>>1)<<1
    elif isAEven:
        someGcd = gcd(a>>1, b)
    elif isBEven:
        someGcd = gcd(a, b>>1)
    elif a > b:
        someGcd = gcd (a-b, b)
    else:
        someGcd = gcd(a, b-a)
    if SHOW_PRINT_MSGS:
        print "The gcd of {0} and {1} is {2}".format(a, b, someGcd)
    return someGcd

# Enumerating Primes (Problem 2.11)
def enumerateAllPrimes(n):
    if SHOW_PRINT_MSGS:
        print "Enumerating all primes between 1 and {0}".format(n)
    allPrimes = [] if n < 2 else [2]
    if n > 2:
        # for 3, consider array of size 1,
        # for 5, consider array of size 2,
        # for 7, consider array of size 3, etc... 
        size = ((n - 3) >> 1) + 1
        isPrime = [1] * size
        for i in range(0, size):
            if isPrime[i] == 1:
                p = (i << 1) + 3
                allPrimes.append(p)
                j = ((i * i) << 1) + (6 * i) + 3
                while j < size:
                    isPrime[j] = 0
                    j = j + p
    if SHOW_PRINT_MSGS:
        print "All primes between 1 and {0}: {1}".format(n, allPrimes)
    return allPrimes

class Rect:
    """A Rectangle class"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return "Rect[x={x}, y={y}, width={width}, height={height}]".format(x=self.x, y=self.y, width=self.width, height=self.height)

    def __eq__(self, other):
        return self.x == other.x and \
            self.y == other.y and \
            self.width == other.width and \
            self.height == other.height

# Intersecting Rectangles (Problem 2.12)
def hasIntersection(rectR, rectS):
    # For checking no intersections: check if one rectangle's x0 is beyond another rectangle's x1+w1, same with y0 and y1+height
    intersect = not ((rectR.x > (rectS.x + rectS.width)) or \
        ((rectR.x + rectR.width) < rectS.x) or \
        (rectR.y > (rectS.y + rectS.height)) or \
        ((rectR.y + rectR.height) < rectS.y))
    if SHOW_PRINT_MSGS:
        print "Rect {rectR} and {rectS} {answer} intersections".format(rectR=rectR, rectS=rectS, answer="has" if intersect else "does not have")
    return intersect

def getIntersection(rectR, rectS):
    x = 0
    y = 0
    width = 0
    height = 0
    if hasIntersection(rectR, rectS):
        if rectR.x > rectS.x:
            x = rectR.x
            width = min(rectS.x + rectS.width - rectR.x, rectR.width)
        else:
            x = rectS.x
            width = min(rectR.x + rectR.width - rectS.x, rectS.width)
        if rectR.y > rectS.y:
            y = rectR.y
            height = min(rectS.y + rectS.height - rectR.y, rectR.height)
        else:
            y = rectS.y
            height = min(rectR.y + rectR.height - rectS.y, rectS.height)
    intersect = Rect(x, y, width, height)
    if SHOW_PRINT_MSGS:
        print "Rect {rectR} and {rectS} has intersecting rectangle {intersect}".format(rectR=rectR, rectS=rectS, intersect=intersect)
    return intersect

# Multiplication no arithmetic operators (Problem 2.13)
def add(a, b):
    n = 1
    sum = 0
    carry = 0
    while (n <= a or n <= b or carry != 0):
        an = a & n
        bn = b & n
        if SHOW_PRINT_MSGS:
            print "an is {an} and bn is {bn}".format(an=an,bn=bn)
        sumn = (an ^ bn ^ carry)
        sum = sum | sumn
        if SHOW_PRINT_MSGS:
            print "Sum n is {sumn}".format(sumn=bin(sumn))
        carry = (an & bn) | (an & carry) | (bn & carry)
        carry <<= 1
        n <<=1
        if SHOW_PRINT_MSGS:
            print "n is {n}".format(n=n)
    if SHOW_PRINT_MSGS:
        print "The sum of {a} and {b} is {sum}".format(a=a,b=b,sum=sum)
    return sum

def multiply(a, b):
    result = 0
    n = 1
    an = a
    while (n <= b):
        bn = b & n
        if bn > 0:
            if SHOW_PRINT_MSGS:
                print "n is {n}, bn is {bn}, result is {result}, an is {an}".format(n=n,bn=bn,result=result,an=an)
            result = add(result, an)
        n <<= 1
        an <<= 1
    if SHOW_PRINT_MSGS:
        print "The product of {a} and {b} is {result}".format(a=a,b=b,result=result)
    return result

# Division using only addition, subtraction, and multiplication (Problem 2.14)
def divide(x, y):
    result = 0
    if x > y:
        result = 1
        remainder = x - y
        while remainder >= y:
            if y * result < remainder:
                result <<= 1
                remainder -= (y * (result >> 1))
            else:
                result += 1
                remainder -= y
            if SHOW_PRINT_MSGS:
                print "result is {result}, and remainder is {remainder}".format(result=result, remainder=remainder)
    if SHOW_PRINT_MSGS:
        print "Dividing {x} by {y} results in {result}".format(x=x,y=y,result=result)
    return result


class Ch2SolutionsTestCase(unittest.TestCase):
    # Construct a precomputed table of parities for 16-bit integers
    # constructPrecomputedParityTable()

    def testParity1(self):
        # Tests for computing parity using straightforward approach (problem 2.1)
        self.assertEqual(0, parity1(17))
        self.assertEqual(1, parity1(28))

    def testParity2(self):
        # Tests for computing parity using approach where each lowest set bit is dropped (problem 2.1)
        self.assertEqual(0, parity2(17))
        self.assertEqual(1, parity2(28))

    def testParity1AndParity2ReturnsSameResults(self):
        self.assertEqual(parity1(17), parity2(17))
        self.assertEqual(parity1(28), parity2(28))

    def testSwapBits(self):
        # Tests for swapping bits (problem 2.2)
        self.assertEqual(int(0b10001111001000), swapBits(0b10001110001001, 0, 6))
        self.assertEqual(int(0b00010), swapBits(0b10000, 4, 1))

    def testReverseBitsRegular(self):
        # Tests for bit reversal (problem 2.3)
        self.assertEqual(int(0b0111010010000000000000000000000000000000000000000000000000000000),
            reverseBitsRegular(0b100101110))
        self.assertEqual(int(0b1100100000000000000000000000000000000000000000000000000000000000),
            reverseBitsRegular(0b00010011))

    def testClosestIntSameWeight(self):
        # Tests for closest int same weight (problem 2.4)
        self.assertEqual(101, closestIntSameWeight(99))
        self.assertEqual(234, closestIntSameWeight(236))

    def testPrintPowerSet(self):
        # Tests for printing power set (problem 2.5)
        printPowerSet([1, 2, 3, 4])
        printPowerSet([1, 1, 2, 3])

    def testStringToInt(self):
        # Tests for string to integer conversion (problem 2.6)
        self.assertEqual(12335, stringToInt("12335"))
        stringToInt("asdf")
        self.assertEqual(-8981, stringToInt("-8981"))

    def testIntToString(self):
        # Tests for integer to string conversion (problem 2.6)
        self.assertEqual("-8928", intToString(-8928))
        self.assertEqual("819211", intToString(819211))

    def testConvertToBase(self):
        # Tests for converting an integer string between 2 bases (problem 2.7)
        self.assertEquals("11259375", convertToBase("ABCDEF", 16, 10))
        self.assertEqual("1E44D", convertToBase("123981", 10, 16))
        self.assertEqual("1010", convertToBase("A", 16, 2))
        self.assertEqual("27", convertToBase("123", 4, 10))

    def testSSDecodeColId(self):
        # Tests for spreadsheet column encoding (problem 2.8)
        self.assertEqual(1, ssDecodeColId("A"))
        self.assertEqual(26, ssDecodeColId("Z"))
        self.assertEqual(27, ssDecodeColId("AA"))
        self.assertEqual(703, ssDecodeColId("AAA"))

    def testEncodeElias(self):
        # Tests for Elias Gamma Encoding (problem 2.9)
        self.assertEqual("00011010000001000000000010100", encodeElias([13, 64, 20]))
        self.assertEqual([13, 64, 20], decodeElias("00011010000001000000000010100"))

    def testGCD(self):
        # Tests for GCD (problem 2.10)
        self.assertEqual(1, gcd(17, 10))
        self.assertEqual(38, gcd(38, 190))
        self.assertEqual(1, gcd(5, 19))
        self.assertEqual(0, gcd(0, 10))
        self.assertEqual(10, gcd(10, 20))
        self.assertEqual(6, gcd(12, 30))

    def testEnumerateAllPrimes(self):
        # Tests for enumerating all primes (problem 2.11)
        self.assertEqual([], enumerateAllPrimes(1))
        self.assertEqual([], enumerateAllPrimes(0))
        self.assertEqual([2], enumerateAllPrimes(2))
        self.assertEqual([2, 3, 5, 7, 11], enumerateAllPrimes(12))
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], enumerateAllPrimes(30))

    def testRectangleIntersection(self):
        # Tests for rectangle intersection (problem 2.12)
        NON_INTERSECTING_RECT = Rect(0, 0, 0, 0)
        CENTRAL_RECT = Rect(-4, -2, 8, 4)
        self.assertEqual(Rect(0, 0, 0, 0), Rect(0, 0, 0, 0))
        self.assertEqual(NON_INTERSECTING_RECT, getIntersection(CENTRAL_RECT, Rect(-2, 3, 4, 2)))
        self.assertEqual(NON_INTERSECTING_RECT, getIntersection(CENTRAL_RECT, Rect(5, 6, 7, 8)))
        self.assertEqual(CENTRAL_RECT, getIntersection(CENTRAL_RECT, Rect(-5, -6, 20, 30)))
        self.assertEqual(NON_INTERSECTING_RECT, getIntersection(CENTRAL_RECT, Rect(-9, -10, 1, 2)))
        self.assertEqual(Rect(0, 0, 4, 2), getIntersection(CENTRAL_RECT, Rect(0, 0, 10, 10)))
        self.assertEqual(Rect(-2, -2, 4, 4), getIntersection(CENTRAL_RECT, Rect(-2, -5, 4, 30)))
        self.assertEqual(Rect(-4, 0, 8, 2), getIntersection(CENTRAL_RECT, Rect(-9, 0, 30, 2)))

    def testSum(self):
        # Tests for addition with no arithmetic operators (problem 2.13, part 1)
        self.assertEqual(0, add(0, 0))
        self.assertEqual(1, add(1, 0))
        self.assertEqual(1, add(0, 1))
        self.assertEqual(19, add(10, 9))
        self.assertEqual(37, add(23, 14))

    def testMultiply(self):
        # Tests for multiplication with no arithmetic operators (part 2.13, part 2)
        self.assertEqual(0, multiply(0, 0))
        self.assertEqual(0, multiply(9, 0))
        self.assertEqual(0, multiply(0, 9))
        self.assertEqual(17, multiply(1, 17))
        self.assertEqual(17, multiply(17, 1))
        self.assertEqual(64, multiply(32, 2))
        self.assertEqual(35, multiply(5, 7))
        self.assertEqual(28, multiply(14, 2))
        self.assertEqual(17 * 14, multiply(17, 14))

    def testDivide(self):
        # Tests for division with multpication, addition and subtraction (2.14)
        self.assertEqual(2, divide(15, 6))
        self.assertEqual(0, divide(0, 10))
        self.assertEqual(7, divide(7, 1))
        self.assertEqual(5, divide(15, 3))
        self.assertEqual(34, divide(238, 7))

if __name__ == '__main__':
    unittest.main()
    

