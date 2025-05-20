bacon_dict = {
    "AAAAA":"A","AAAAB":"B","AAABA":"C","AAABB":"D","AABAA":"E","AABAB":"F",
    "AABBA":"G","AABBB":"H","ABAAA":"I","ABAAB":"J","ABABA":"K","ABABB":"L",
    "ABBAA":"M","ABBAB":"N","ABBBA":"O","ABBBB":"P","BAAAA":"Q","BAAAB":"R",
    "BAABA":"S","BAABB":"T","BABAA":"U","BABAB":"V","BABBA":"W","BABBB":"X",
    "BBAAA":"Y","BBAAB":"Z"
}

morse_dict = {
    ".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G",
    "....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N",
    "---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U",
    "...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z","-----":"0",
    ".----":"1","..---":"2","...--":"3","....-":"4",".....":"5",
    "-....":"6","--...":"7","---..":"8","----.":"9"
}

def decode_bacon(text):
    if all(c in "AB" for c in text.replace(" ", "")):
        groups = text.replace(" ", "").upper()
        chunks = [groups[i:i+5] for i in range(0, len(groups), 5)]
        return ''.join(bacon_dict.get(chunk, '?') for chunk in chunks)
    return ""

def decode_morse(text):
    try:
        return ''.join(morse_dict.get(code, '?') for code in text.split(" "))
    except:
        return ""

def analyze_and_decode(text):
    output = ["🔍 Bacon & Morse Code Analysis:"]
    bacon = decode_bacon(text)
    morse = decode_morse(text)
    if bacon: output.append(f"Bacon Cipher: {bacon}")
    if morse: output.append(f"Morse Code: {morse}")
    return "\n".join(output)
