#!/usr/bin/env python3

from steganography import hide_message, extract_message


def show_banner():
    print("=" * 45)
    print("        STEGANOGRAPHY TOOL")
    print("=" * 45)


def hide():
    print("\n[+] Hide a message")

    input_image = input("Image path: ").strip()
    output_image = input("Output image: ").strip()
    message = input("Message to hide: ")

    try:
        hide_message(input_image, output_image, message)
        print(f"\n[+] Message successfully hidden!")
        print(f"[+] Output: {output_image}")

    except FileNotFoundError:
        print("\n[-] Image file not found.")

    except ValueError as error:
        print(f"\n[-] Error: {error}")

    except Exception as error:
        print(f"\n[-] Unexpected error: {error}")


def extract():
    print("\n[+] Extract a message")

    input_image = input("Image path: ").strip()

    try:
        message = extract_message(input_image)

        print("\n[+] Hidden message:")
        print("-" * 45)
        print(message)
        print("-" * 45)

    except FileNotFoundError:
        print("\n[-] Image file not found.")

    except ValueError as error:
        print(f"\n[-] Error: {error}")

    except Exception as error:
        print(f"\n[-] Unexpected error: {error}")


def main():
    while True:
        show_banner()

        print("1. Hide message")
        print("2. Extract message")
        print("3. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            hide()

        elif choice == "2":
            extract()

        elif choice == "3":
            print("\n[+] Goodbye!")
            break

        else:
            print("\n[-] Invalid option.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
