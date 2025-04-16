import argparse
from HueCode import Encrypt, Decrypt  # Assumes they're exposed in __init__.py

def cli_entry():
    parser = argparse.ArgumentParser(
        description="Encode data to an image using RGB values and decode it back"
    )

    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("data", type=str, help="Data to encrypt or decrypt")
    parser.add_argument("--path", type=str, default=None, help="Optional path to save the output image")
    parser.add_argument("--filename", type=str, default=None, help="Optional filename for the output image")
    parser.add_argument("--title", type=str, default="Untitled", help="Optional title metadata for the image")
    parser.add_argument("--desc", type=str, default="No description", help="Optional description metadata")

    args = parser.parse_args()

    if args.action == "encrypt":
        if not args.data:
            print("Error: No data provided to encrypt.")
            return

        encryptor = Encrypt(
            data=args.data,
            path=args.path,
            filename=args.filename,
            title=args.title,
            desc=args.desc
        )
        encryptor.createImg()
        print("Encryption complete.")

    elif args.action == "decrypt":
        if not args.data:
            print("Error: No data provided to decrypt.")
            return

        decrypted = Decrypt(args.data).decrypt()
        print("Decryption result:")
        print(decrypted)

if __name__ == "__main__":
    cli_entry()