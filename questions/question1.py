
NUMS = ['1', '2', '3', '4', '5', '7', '8', '9', '0']
BRACKETS = ['[', ']']


def execute(s: str):
    mem = []
    aux = ''
    i = 0
    _open = 0
    st = -1
    ed = -1
    while i < len(s):
        num = ''
        while s[i] in NUMS:
            if len(aux) > 0:
                mem.append(aux)
                aux = ''
            num += s[i]
            i += 1
        if len(num) > 0:
            while ed == -1:
                if s[i] == '[':   
                    if _open == 0:
                        st = i
                    _open += 1
                elif s[i] == ']':
                    _open -= 1
                    if _open == 0:
                        ed = i
                        lmao = s[st+1:ed] * int(num)
                        
                        x = execute(lmao)
                        mem.append(x)
                        
                i+=1
            st = -1
            ed = -1

        else:
            aux += s[i]
            i += 1
    if len(aux) > 0:
        mem.append(aux)
    return ''.join(mem)


def decompress(s: str):
    s = f"1[{s}]"
    ans = execute(s)
    print(ans)


def main():
    # decompress("3[]4[ab]c")
    # decompress("3[abc]10[ab]c")
    decompress("3[a3[d]b4[a]c]10[ab]c")
    # decompress("3[a]0[ab]c")
    # decompress("3[a]0[ab]c")
    # decompress("aaabre10[a]0[ab]c")


if __name__ == "__main__":
    main()
