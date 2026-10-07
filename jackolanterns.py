"""
Kattis Jack-O-Lanterns
Elizabeth Posusta - Oct 26
"""

def main() -> None:
  # input
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    
  # processing
    M: int = a * b * c
    
  # output
    print(M)

if __name__ == "__main__":
  main()
    
