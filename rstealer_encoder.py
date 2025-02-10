import base64

def base64_encode(data: bytes) -> str:
    return base64.b64encode(data).decode('utf-8')

def base64_decode(data: str) -> bytes:
    return base64.b64decode(data)

def create_encoded_python_file(original_code: str) -> str:
    base64_encoded_code = base64_encode(original_code.encode('utf-8'))

    final_code = f"""
import base64
encoded_code = "{base64_encoded_code}"
exec(base64.b64decode(encoded_code))
"""

    output_filename = "final_output.py"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(final_code)
    
    return output_filename

def main():
    with open('rstealer_output.py', 'r', encoding='utf-8') as file:
        original_code = file.read()

    final_filename = create_encoded_python_file(original_code)
    print(f"Encoded Python file created: {final_filename}")
