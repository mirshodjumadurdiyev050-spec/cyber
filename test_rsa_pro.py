import sys
import os
# Add the current directory to sys.path to import logic
sys.path.append(os.getcwd())

from logic.rsa import RSAManager
import time

def test_rsa():
    print("--- Professional RSA Testi boshlandi ---")
    
    # 1. Kalit generatsiyasi
    print("[1] 1024-bitli kalitlar generatsiya qilinmoqda...")
    start = time.time()
    rsa = RSAManager(bits=1024)
    rsa.generate_keys()
    print(f"Tayyor! Vaqt: {time.time() - start:.2f} sek")
    
    # 2. Oddiy shifrlash (OAEP)
    message = "Salom, bu professional RSA moduli!"
    print(f"\n[2] Shifrlanmoqda: '{message}'")
    ciphertext = rsa.encrypt(message)
    print(f"Ciphertext (int): {str(ciphertext)[:50]}...")
    
    decrypted = rsa.decrypt(ciphertext)
    print(f"Dekriptizatsiya: '{decrypted}'")
    
    assert message == decrypted, "Xatolik: Dekriptizatsiya noto'g'ri!"
    print("Muvaffaqiyatli!")

    # 3. Parallel qayta ishlash
    print("\n[3] Parallel qayta ishlash testi (katta matn)...")
    large_text = "Bu juda uzun matn bo'lib, u bir nechta bloklarga bo'linadi. " * 5
    print(f"Matn uzunligi: {len(large_text)} belgi")
    
    start = time.time()
    encrypted_blocks = rsa.parallel_process(large_text, mode='encrypt', processes=4)
    print(f"Parallel shifrlash tugadi. Bloklar soni: {len(encrypted_blocks)}")
    
    decrypted_large = rsa.parallel_process(encrypted_blocks, mode='decrypt', processes=4)
    print(f"Parallel dekriptizatsiya tugadi. Vaqt: {time.time() - start:.2f} sek")
    
    assert large_text == decrypted_large, "Xatolik: Parallel dekriptizatsiya noto'g'ri!"
    print("Muvaffaqiyatli!")

if __name__ == "__main__":
    test_rsa()
