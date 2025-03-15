#!/usr/bin/env python3
import argparse
import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True, keywords=None):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''
    
    all_chars = lower + upper + digits + symbols
    if not all_chars:
        raise ValueError("[CCrack] No character set selected for password generation.")
    
    password = ''.join(random.choices(all_chars, k=length))
    
    if keywords:
        keyword = random.choice(keywords)
        remaining_length = length - len(keyword)
        if remaining_length > 0:
            filler = ''.join(random.choices(all_chars, k=remaining_length))
            insert_pos = random.randint(0, remaining_length)  
            password = filler[:insert_pos] + keyword + filler[insert_pos:]
        else:
            password = keyword[:length]
    
    return password.replace(" ", "")

def main():
    parser = argparse.ArgumentParser(description="C Crack - A.K.A. Cypher Crack, created by Theo Kershaw")
    parser.add_argument('-n', '--num', type=int, default=10, help='Number of passwords to generate')
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of each password')
    parser.add_argument('-o', '--output', type=str, help='Output file to save passwords')
    parser.add_argument('--no-upper', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    parser.add_argument('--no-symbols', action='store_true', help='Exclude symbols')
    parser.add_argument('-k', '--keywords', type=str, help='Comma-separated keywords to include in passwords')
    
    args = parser.parse_args()
    keywords = args.keywords.split(',') if args.keywords else None
    
    passwords = [generate_password(args.length, not args.no_upper, not args.no_digits, not args.no_symbols, keywords) for _ in range(args.num)]
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write('\n'.join(passwords) + '\n')
        print(f"[CCrack] Passwords saved to {args.output}")
    else:
        print('\n'.join(passwords))

if __name__ == "__main__":
    main()

