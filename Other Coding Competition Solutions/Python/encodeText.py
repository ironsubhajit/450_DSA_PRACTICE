"""
Q. Encode plain text
input: "aaabccgg"
output: "3a1b2c2g"

Time complexity: O(n)
"""


def new_st(string):
    st = []
    count = 0
    prev_st = string[0]
    for i in range(len(string)):
        if prev_st == string[i]:
            prev_st = string[i]
            count += 1
        else:
            st.append(f"{count}{prev_st}")
            prev_st = string[i]
            count = 1
    else:
        st.append(f"{count}{prev_st}")

    return ''.join(st)


plain_text = "aaabccgg"
encoded_text = new_st(plain_text)
print(encoded_text)