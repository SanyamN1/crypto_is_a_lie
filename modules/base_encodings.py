import base64
import urllib.parse
import binascii

def analyze_and_decode(text):
    output = ["🔍 Base Encodings & URL Decoding Results:"]
    try:
        decoded = base64.b64decode(text).decode("utf-8")
        output.append(f"Base64: {decoded}")
    except Exception:
        pass

    try:
        decoded = base64.b32decode(text).decode("utf-8")
        output.append(f"Base32: {decoded}")
    except Exception:
        pass

    try:
        decoded = base64.b16decode(text).decode("utf-8")
        output.append(f"Base16: {decoded}")
    except Exception:
        pass

    try:
        decoded = binascii.unhexlify(text).decode("utf-8")
        output.append(f"Hex: {decoded}")
    except Exception:
        pass

    try:
        decoded = "".join(chr(int(b, 2)) for b in text.split())
        output.append(f"Binary: {decoded}")
    except Exception:
        pass

    try:
        decoded = urllib.parse.unquote(text)
        output.append(f"URL Encoded: {decoded}")
    except Exception:
        pass

    try:
        ascii_text = ''.join([chr(int(num)) for num in text.split()])
        output.append(f"ASCII Codes: {ascii_text}")
    except Exception:
        pass

    return "\n".join(output)
