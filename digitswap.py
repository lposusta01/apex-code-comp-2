"""
Kattis Digit Swap
Elizabeth Posusta - Oct 26
"""

def main() -> None:
  # input
    n: int = int(input())
    
  # processing
    a: int = n % 10
    b: int = int(n / 10)
    

  # output
    print(f"{a}{b}")

if __name__ == "__main__":
  main()
    
