
def solution(s: str, wrds: list[str]):
    solutions = []
    for word in wrds:
        i = 0
        aux = s
        while i < len(aux) and i < len(word):
            if(word in aux):
                solutions.append(word)
                break
            elif aux[i] == word[i]:                
                i += 1
            else:
                aux = f"{aux[0:i]}{aux[i+1:len(aux)+1]}"
        
    print(max(solutions, key=len))


def main():
    solution("wiowurowetoukwoieruowowieurbwoeiuroiwuerkowieruoiwqeurbwoieruoiweur", ["kbkb", "aaa", "hjhj" ])


if __name__ == "__main__":
    main()
