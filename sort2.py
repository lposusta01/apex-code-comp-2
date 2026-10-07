"""
Kattis Sort Two Numbers
Elizabeth Posusta - Oct 26
"""

def main() -> None:
  # input
    a, b = input().split()
    a = int(a)
    b = int(b)
    
  # processing
    
  # output
    if a > b:
        print(f"{b} {a}")
    else:
        print(f"{a} {b}")

if __name__ == "__main__":
  main()
    
