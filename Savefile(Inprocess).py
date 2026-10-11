import re
from pathlib import Path

USER_DIR = Path(__file__).with_name("users")


def _path(username):
    """คืน path ไฟล์ของ user ถ้า username ไม่ปลอดภัยคืน None"""
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,32}", username):
        return None  # กันชื่อแปลก เช่น ../x ที่เขียนออกนอกโฟลเดอร์
    return USER_DIR / f"{username}.txt"


def create_user(username, password):
    """สมัครใหม่ ถ้ามีไฟล์ของ user นี้อยู่แล้วจะไม่ทับ คืน True=สำเร็จ"""
    path = _path(username)
    if path is None:
        return False
    USER_DIR.mkdir(exist_ok=True)
    try:
        with open(path, "x", encoding="utf-8") as f:  # "x" = สร้างใหม่เท่านั้น
            f.write(f"{username}\n{password}\n")
    except FileExistsError:
        return False
    return True


def update_user(username, password):
    """อัพเดทรหัสผ่านของ user ที่มีอยู่แล้ว คืน True=สำเร็จ"""
    path = _path(username)
    if path is None or not path.exists():
        return False
    path.write_text(f"{username}\n{password}\n", encoding="utf-8")
    return True


def load_user(username):
    """อ่านกลับ คืน (username, password) ไม่มีหรือข้อมูลไม่ครบคืน None"""
    path = _path(username)
    if path is None:
        return None
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return None
    if len(lines) < 2:
        return None
    return lines[0], lines[1]

#if __name__ == "__main__":
#    name = input("Username: ")
#    pw = input("Password: ")
#    if create_user(name, pw):
#        print("User created.")
#    else:
#        print("User already exists or invalid username.")
#    user_data = load_user(name)
#    if user_data:
#        print("Loaded user:", user_data)
#    else:
#        print("Failed to load user.")
