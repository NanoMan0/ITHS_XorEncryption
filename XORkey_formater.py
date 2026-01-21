
import argparse
import sys

class xorkey_formater:

    @staticmethod

    # key converter and validation with error for incorrect input format #

    def key_check(value):

        """
        Function to valitade and sanitize user input before sending for encryption
        """

        try:

            if isinstance (value, str) and value.startswith ("0x") or value.startswith ("0X"):

                #slices away hex marker#
                    
                value_sliced = value[2:]

                #checks for valid hex characters if value, string starts with hex marker# 

                if all(c in "0123456789ABCDEFabcdef " for c in value_sliced):
                    
                    return bytearray.fromhex(value_sliced)
                
                else:
                    raise argparse.ArgumentTypeError(f"Invalid HEX value: {value}.")  
            
            elif value.isdigit():

                # Convert the string (argparse is always string) to an integer
                num = int(value)

                # Make sure the number is not negative (reduntant since will get seen as string)#

                if num < 0:
                    raise argparse.ArgumentTypeError(f"[-] ERROR Numeric key must be positive: {value}")

                # Calculates how many bytes we need to store this number#
                # bit_length() tells us how many bits are needed, divide by 8 for bytes#
                # "or 1" ensures at least 1 byte#

                num_bytes = (num.bit_length() + 7) // 8 or 1

                # Convert the number to bytes (big-endian) for XOR#

                return num.to_bytes(num_bytes, "big")

            
            elif isinstance (value, str):

                #if key is a string it gets encoded#
        
                return value.encode("utf-8")
        
            
        except argparse.ArgumentTypeError:
            raise

        except Exception as e:
            print ("[-] Unexpected ERROR at key validation stage")
            print (f"Error type: {e}")
            sys.exit(1) 