import keys


def generate_and_test_keys():

    key = keys.generate_keys()

    for message in range(11, 99):
        try:
            encrypted_message =  pow(message, key["e"], key["n"])
            decrypted_message = pow(encrypted_message, key["d"], key["n"])
            assert message == decrypted_message
        except:
            print(message, encrypted_message, decrypted_message)
            for k, e in key.items():
                print(key.k, key.e)

def test():
    for i in range(1000):
        generate_and_test_keys()

if __name__ == "__main__":
    test()
