import sys

class Formatter:

    # func for converting encrypted to different output formats

    @staticmethod
    
    def format_output (encrypted, outputFormat):

        """
        Fromats the encypted variable (bytearray) to desired output. 
        """

        try:

            if outputFormat == "raw":
                return bytes(encrypted)
            
            ## formatting for py or c array. names the array and encloses it. ##
            ## then converts every byte to a hex value @ byte:02X ##
            ##  

            elif outputFormat == "py":

                bytes_per_line = 16 

                return (
                "xored_shellcode = [\n" + 
                ",\n".join(
                        "    " + ", ".join(f"0x{byte:02X}" for byte in encrypted[i:i + bytes_per_line])
                        for i in range(0, len(encrypted), bytes_per_line)
                    ) + "\n]"
                )
            

            elif outputFormat == "c":
                
                bytes_per_line = 24

                return (
                    "unsigned char xored_shellcode[] = {\n"
                    + ",\n".join(
                        "    " + ", ".join(f"0x{byte:02X}" for byte in encrypted[i:i + bytes_per_line])
                        for i in range(0, len(encrypted), bytes_per_line)
                    )
                + "\n};"
                )
            else:
                #redundant since arg parse catches but stays for modularity#
                print (f"[-] ERROR selected output {outputFormat} is not valid.")
                sys.exit(1)

        except Exception as e:
            print ("[-] Unexpected ERROR at formating stage")
            print (f"Error type: {e}")
            sys.exit(1) 