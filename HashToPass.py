password_table = {
    "e10adc3949ba59abbe56e057f20f883e": "123456",
    "7c4a8d09ca3762af61e595209413dc26494f8941b": "123456",
    
    "b59c67bf196a4758191e42f76670ceba": "1111",
    "011c945f30ce2cbafc452f39840f025693339c42": "1111",
    
    "e807f1fcf82d132f9bb018ca6738a19f": "1234567890",
    "01b307acba4f54f55aafc33bb06bbbf6ca803e9a": "1234567890",
    
    "25d55ad283aa400af464c76d713c07ad": "12345678",
    "7c222fb2927d828af22f592134e8932480637c0d": "12345678",
    
    "25f9e794323b453885f5181f1b624d0b": "123456789",
    "f7c3bc1d808e04732adf679965ccc34ca7ae3441": "123456789",
    
}

# ask user for hash
hash_input = input("Enter hash: ")

# search for hash in the table
if hash_input in password_table:
    print("password found:", password_table[hash_input])
else:
    print("password not found.")
