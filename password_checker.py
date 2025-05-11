import re

def check_password_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        remarks.append("Add at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Add at least one special character.")

    return score, remarks

def is_common_password(password, filename="common-passwords-win.txt"):
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as file:
            common = file.read().splitlines()
            return password in common
    except FileNotFoundError:
        print(f"⚠️ Error: {filename} not found.")
        return False

def main():
    password = input("Enter a password to evaluate: ").strip()

    if is_common_password(password):
        print("⚠️ This password is too common. Choose another one.")
        return

    score, feedback = check_password_strength(password)

    print(f"\nPassword Score: {score}/5")

    if score == 5:
        print("✅ Strong password!")
    elif score >= 3:
        print("🟡 Moderate password. Suggestions:")
        for f in feedback:
            print("  -", f)
    else:
        print("🔴 Weak password. Suggestions:")
        for f in feedback:
            print("  -", f)

if __name__ == "__main__":
    main()
