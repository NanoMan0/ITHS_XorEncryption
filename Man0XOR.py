import argparse
import sys

from shellcode_reader import shellcode_reader

from XORkey_formater import xorkey_formater

from encryptor import Encryptor

from formater import Formatter
    
#################################################################################

# UI

def extraHelp():

    """
    Extra help menu (currently unused)
    """

    UItop()
    print()
    print( "[+] Req. argruments and input order [+]")
    print ( "--i /path/to/raw-file")
    print ( "--o /output/path/file-name")
    print ( "--key XOR encryption key in Hex Format")
    print ( "--f format [raw, py or c]")
    print ()

def UItop():

    """
    Cosmetic elements used in various places
    """

    splitter= "------------------------------------------------------"

    print(splitter)
    print (" █ Welcome to Man0Crypt - Shellcode XOR Tool █")
    print (splitter)
    print ("█ XOR and Obfuscate Shellcode like a Real H4cker █")
    print (f"{splitter}\n")


##########################################################################


def main():


  # Arg parser that takes in arguments and calls functions

    # main parser creation

    parser = argparse.ArgumentParser(
        description=UItop())

    # arguments for encyption for parsing 

    parser.add_argument(
        "--i", 
        required=True, 
        dest="InputFile",
        help="specify raw-shellcode.xyz or /path/raw-shellcode.xyz")
    
    parser.add_argument(
        "--o", 
        dest="OutputFile",
        help="encrypted output file name.xyz or /save/location/name.xyz", 
        required=True)
    
    parser.add_argument(
        "--key", 
        dest="Key",
        help="provide XOR encryption key (hex, string or number)",
        required=True, 
        #type=xorkey_formater.key_check
        )
    
    parser.add_argument(
        "--f", 
        dest="Format",
        help="select output format; raw, python-array (py) or c-array (c)",
        required=True, choices=["raw", "py", "c"])
    
    parser.add_argument(
        "--p",
        action="store_true",
        dest="Print",
        help="(optional) prints output to terminal for easy copy pasta")
    
    ### argument parsing ###
    args = parser.parse_args()


    ## START PROCESS ##

    try:

        ##storing original key to be displayed to user##
        original_key = args.Key

        ##validating and formating key for XOR ###

        args.Key = xorkey_formater.key_check(args.Key)



        ### read shellcode from file via shellcodeReader func ###

        shellcode = shellcode_reader.read_binary(args.InputFile)     

        ### call encrypted shellcode func with data from shellcode reader ###
   
        encrypted = Encryptor.xor_encrypt(shellcode, args.Key)

        ### format encrypted shellcode with returned data from encryptor func ###
    
        formatted = Formatter.format_output(encrypted, args.Format)



        ### save in selected fromat and visual feedback ###
   
        if args.Format == "raw":
            with open (args.OutputFile, "wb") as f:
                f.write(formatted)
        else:
            with open (args.OutputFile, "w") as f:
                f.write(formatted)

        print("[+] Encryption Successful [+]\n")

        print (f"-> Output format: {args.Format}\n")

        print (f"-> XOR key: {original_key}\n")

        print (f"-> Key size (bytes): {len(args.Key)}\n")

        print(f"-> Shellcode has been encrypted and saved as: {args.OutputFile}\n")

        if args.Print and args.Format != "raw":
            print(f"Output for copy pasta:\n\n {formatted}")
        elif args.Format == "raw":
            print ("Raw bytes will not be printed to terminal. Use the saved file :)\n")

    except Exception as e:
        print (f"[-] Exiting with unexpected ERROR: {e}")
        sys.exit(1)


#################################

if __name__=="__main__":
   main()