def decrypt_cisco_type7(encrypted_password):
    key = (
        0x64, 0x73, 0x66, 0x64, 0x3B, 0x6B, 0x66, 0x6F, 0x41, 0x2C,
        0x2E, 0x69, 0x79, 0x65, 0x77, 0x72, 0x6B, 0x6C, 0x64, 0x4A,
        0x4B, 0x44, 0x48, 0x53, 0x55, 0x42, 0x73, 0x67, 0x76, 0x63,
        0x61, 0x36, 0x39, 0x38, 0x33, 0x34, 0x6E, 0x63, 0x78, 0x76,
        0x39, 0x38, 0x37, 0x33, 0x32, 0x35, 0x34, 0x6B, 0x3B, 0x66,
        0x67, 0x38, 0x37
    )

    if len(encrypted_password) < 4 or len(encrypted_password) % 2 != 0:
        return "Error: Invalid encrypted password format."
        
    try:
        salt = int(encrypted_password[:2])
        encrypted = encrypted_password[2:]
        decrypted = ''

        for i in range(0, len(encrypted), 2):
            byte = int(encrypted[i:i+2], 16)
            decrypted += chr(byte ^ key[(i // 2 + salt) % len(key)])

        return decrypted
    except Exception:
        return "Error: Decryption failed."

if __name__ == "__main__":
    encrypted = "072220484B2B002B140A240A0223282D293F" # Cisco Type 7 Password
    print("Decrypted password:", decrypt_cisco_type7(encrypted))
