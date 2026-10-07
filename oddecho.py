"""
Kattis Odd Echo
Elizabeth Posusta - Oct 26
"""

def main() -> None:
  # input
    n: int = int(input())
    
  # processing
    out: list[str] = []
    
    for i in range(0, n):
        out.append(input())
    

  # output
    for i in range(0, len(out)):
        if (i + 1) % 2 != 0:
            print(out[i])

if __name__ == "__main__":
  main()
    
