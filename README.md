# C-Crack
This tool is a password list generator tool using argparse in python. It was named after me (CYPHER) hense its called 'C-Crack' stands for Cypher-Crack

# How To Use
-n or --num = Number of passwords to generate\n
-l or --length = The length of the passwords\n
-o or --output = What name should the output file be called\n
-k or --keywords = Specify the keywords to use in the list\n
--no-upper = Exclude uppercase letters\n
--no-digits = Exclude digits\n
--no-symbols = Exclude symbols\n

# Example Command
python3 c-crack.py -n 500 -o passwords.txt --no-symbols -k "password, root, flipper, dog"
