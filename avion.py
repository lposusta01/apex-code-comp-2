"""
Kattis Avion
Elizabeth Posusta - Oct 26
"""

def main() -> None:
  # input
    ships: list[str] = []
    n: list[int] = []
    
    for i in range(0,5):
        ships.append(input())
        if "FBI" in ships[i]:
            n.append(i + 1)
    
  # processing

  # output
    if len(n) > 0:
        for i in n:
            print(f"{i} ", end='')
        print("")
    else:
        print("HE GOT AWAY!")

if __name__ == "__main__":
  main()
    