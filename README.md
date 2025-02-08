# C-Crack
This tool is a password list generator tool using argparse in python. It was named after me (CYPHER) hense its called 'C-Crack' stands for Cypher-Crack

# How To Use
-n or --num = Number of passwords to generate
-l or --length = The length of the passwords
-o or --output = What name should the output file be called
-k or --keywords = Specify the keywords to use in the list
--no-upper = Exclude uppercase letters
--no-digits = Exclude digits
--no-symbols = Exclude symbols

# Example Command
python3 c-crack.py -n 500 -o passwords.txt --no-symbols -k "password, root, flipper, dog"
