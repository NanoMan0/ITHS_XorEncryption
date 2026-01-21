
import sys

class shellcode_reader:
    
    # func that reads binary input file using rb (read binary) and sets contents to varibale
    # returns the variable

    @staticmethod

    def read_binary(input_file):
        
        """
        Function reads shellcode from binary file and sets to variable 
        
        """
        
        try:
            with open(input_file, 'rb') as f:
                shellcode = f.read()

                if not shellcode:
                    print(f"[-] ERROR {input_file} is empty, or in wrong fromat.")
                    sys.exit(1)

            return shellcode
        
        except FileNotFoundError:

            print (f"[-] ERROR file {input_file} not found.")
            sys.exit(1)

        except Exception as e:
            
            print ("[-] Unexpected ERROR at file reading stage.")
            print (f"Error type: {e}")
            raise