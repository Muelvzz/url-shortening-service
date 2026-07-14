import secrets, string

def generate_short_code(length=6):
  characters = string.ascii_letters + string.digits
  short_code = ''.join(secrets.choice(characters) for _ in range(length))
  
  return short_code

if __name__ == "__main__":
  code = generate_short_code()
  print(f"Generated Code: {code}")