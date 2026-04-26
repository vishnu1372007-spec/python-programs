try:
  a='ab'
  print(int(a))
except ValueError:
    print("value not found")
finally:
    print("Code runs successfully")
