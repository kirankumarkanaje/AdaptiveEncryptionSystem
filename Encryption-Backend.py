from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins


# Helper Function: Padding for Block Encryption
def pad_input(data, block_size=16):
    pad_len = block_size - (len(data) % block_size)
    return data + chr(pad_len) * pad_len


# LEA Encryption Logic
def lea_encrypt(block, key):
    rounds = 24
    delta = [0x9E3779B9, 0x3C6EF372, 0x78DDE6E4, 0xF1BBCDCC]

    keys = []
    for i in range(rounds):
        keys.append((key[0] + i * delta[0]) & 0xFFFFFFFF)
        key = key[1:] + key[:1]

    x0, x1, x2, x3 = block
    for i in range(rounds):
        x0 = ((x0 ^ keys[i]) + (x1 & ~x2 ^ x3)) & 0xFFFFFFFF
        x1 = ((x1 ^ keys[i]) + (x2 & ~x3 ^ x0)) & 0xFFFFFFFF
        x2 = ((x2 ^ keys[i]) + (x3 & ~x0 ^ x1)) & 0xFFFFFFFF
        x3 = ((x3 ^ keys[i]) + (x0 & ~x1 ^ x2)) & 0xFFFFFFFF
    return x0, x1, x2, x3


# PRESENT Cipher Implementation
def present_encrypt(block, key):
    sbox = [0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD, 0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2]
    rounds = 31

    keys = [key >> 16]
    for _ in range(rounds):
        key = ((key & 0xFFFFFFFFFFFFFF) << 61) | (key >> 19)
        msb = (key >> 76) & 0xF
        key = (sbox[msb] << 76) | (key & 0x0FFFFFFFFFFFFFF)
        key ^= _ << 15
        keys.append(key >> 16)

    state = block
    for i in range(rounds):
        state ^= keys[i]
        state = sum((sbox[(state >> (4 * j)) & 0xF] << (4 * j)) for j in range(16))
        new_state = 0
        for bit in range(64):
            if state & (1 << bit):
                new_state |= (1 << ((16 * bit) % 63))
        state = new_state

    state ^= keys[-1]
    return state


# Speck Cipher Implementation
def speck_encrypt(block, key):
    def rotate_left(value, shift, size=32):
        return ((value << shift) | (value >> (size - shift))) & 0xFFFFFFFF

    def rotate_right(value, shift, size=32):
        return ((value >> shift) | (value << (size - shift))) & 0xFFFFFFFF

    rounds = 32
    x, y = block
    for i in range(rounds):
        x = (rotate_right(x, 8) + y) ^ key[i % len(key)]
        y = rotate_left(y, 3) ^ x
    return x, y


# Adaptive Encryption Logic
@app.route('/encrypt', methods=['POST'])
def adaptive_encryption():
    data = request.json.get("data", "")
    sensitivity = request.json.get("sensitivity", 5)
    battery_level = request.json.get("battery_level", 50)

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Handle larger input by padding and splitting into blocks
    padded_data = pad_input(data)
    blocks = [padded_data[i:i + 16] for i in range(0, len(padded_data), 16)]

    key_speck = [0x1918, 0x1110, 0x0908, 0x0100]
    key_lea = [0x12345678, 0x9ABCDEF0, 0x11223344, 0x55667788]
    key_present = 0x0123456789ABCDEF0123

    encrypted_blocks = []
    method = ""

    if battery_level < 20:
        method = "Speck"
        for block in blocks:
            block_data = (int.from_bytes(block[:8].encode(), 'big'), int.from_bytes(block[8:].encode(), 'big'))
            encrypted_blocks.append(speck_encrypt(block_data, key_speck))
    elif sensitivity > 7:
        method = "LEA"
        for block in blocks:
            block_data = (int.from_bytes(block[:4].encode(), 'big'), int.from_bytes(block[4:8].encode(), 'big'),
                          int.from_bytes(block[8:12].encode(), 'big'), int.from_bytes(block[12:].encode(), 'big'))
            encrypted_blocks.append(lea_encrypt(block_data, key_lea))
    else:
        method = "PRESENT"
        for block in blocks:
            block_data = int.from_bytes(block.encode(), 'big')
            encrypted_blocks.append(present_encrypt(block_data, key_present))

    return jsonify({
        "method": method,
        "encrypted_blocks": encrypted_blocks
    })


if __name__ == '__main__':
    app.run(debug=True)
