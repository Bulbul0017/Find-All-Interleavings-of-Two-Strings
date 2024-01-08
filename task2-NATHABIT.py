def interleavings(s1, s2):
    result = set()
    generate_interleavings(s1, s2, "", result)
    return list(result)

def generate_interleavings(s1, s2, current, result):
        if not s1 and not s2:
            result.add(current)
            return
        if s1:
            generate_interleavings(s1[1:], s2, current + s1[0], result)

        if s2:
            generate_interleavings(s1, s2[1:], current + s2[0], result)


s1 = input("Enter String 1:")
s2 = input("Enter String 2:")
interleaved_strings = interleavings(s1, s2)

print("Possible interleavings:")
print(*interleaved_strings,sep = "\n")