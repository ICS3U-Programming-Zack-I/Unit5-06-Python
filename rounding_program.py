# Created by: Zack Isingoma
# Created on: 27th Jan 2022.
# Rounds numbers to a given decimal place

def round_decimal(user_decimal, decimal_position):
    user_decimal[0] = user_decimal[0] * (10 ** decimal_position)
    user_decimal[0] += 0.5
    user_decimal[0] = int(user_decimal[0])
    user_decimal[0] = user_decimal[0] / (10 ** decimal_position)


def main():
    print("Welcome")

    user_dec = []
    dec_position = []
    num_float = input("Enter your decimal number: ")
    user_dec.append(num_float)
    places_decimal = input("Enter your decimal places: ")

    try:
        num_as_float = float(num_float)
        places_decimal_int = int(places_decimal)
        if num_as_float >= 0:
            print("{} rounded off to {} places is"
                  .format(num_as_float, places_decimal_int))
            final = round(num_as_float, places_decimal_int)
            print(final)
        else:
            print("Invalid input")
    except Exception:
        print("Invalid input")


if __name__ == "__main__":
    main()
