"""
Kattis Kiki Boba
Elizabeth Posusta - Oct 26
"""

def main() -> None:
  # input
    word: str = input()

  # processing
    kiki: int = 0
    boba: int = 0
    
    for c in word:
        if c == "k":
            kiki += 1
        elif c == "b":
            boba += 1
    
  # output
    if kiki == 0 and boba == 0:
        print("none")
    elif kiki > boba:
        print("kiki")
    elif boba > kiki:
        print("boba")
    else:
        print("boki")

if __name__ == "__main__":
  main()
    
