"""At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?

Example
n=3
There are 3 attendees, p1,p2and p3 .  p1shakes hands with p2 and p3,p2 and p3 shakes hands with . Now they have all shaken hands after  handshakes.

Function Description

Complete the handshakes function in the editor below.

handshakes has the following parameter:

int n: the number of attendees
Returns

int: the number of handshakes
Input Format
The first line contains the number of test cases t.
Each of the following t lines contains an integer,n 
Constraints
1<=t<=1000
0<=n<=10 power 6



Sample Input

2
1
2
Sample Output

0
1
Explanation

Case 1 : The lonely board member shakes no hands, hence 0.
Case 2 : There are 2 board members, so 1 handshake takes place."""

code:
def handshakes(n):
    return n * (n - 1) // 2


test_cases = int(input())
for _ in range(test_cases):
    attendees = int(input())
    result = handshakes(attendees)
    print(result)
