
import sys

class Encryptor:

    # func that encrypts shellcode with XOR key and appends it to byte array
    # (encrypted), that is then returned

    @staticmethod

    def xor_encrypt (shellcode, key):

        """
        Encrypts every byte in shellcode using XOR and appends to bytearray
        """
        
        try:
            
            encrypted = bytearray()

            ## determines the length of the key in bytes, to ensure encryption length##

            key_len = len(key)

            ### encryption process. cycles through every byte with XOR with key ###
            ### uses enumerate to assign every shellcode byte a pairing of index + byte (i + byte)###
            ### uses modulo operator to cycle through all code regardless of key length ### 

            for i, byte in enumerate(shellcode):
                encrypted.append(byte ^ key[i % key_len])

            return encrypted
        
        except Exception as e:
            print ("[-] Unexpected ERROR at encryption stage")
            print (f"Error type: {e}")
            sys.exit(1) 