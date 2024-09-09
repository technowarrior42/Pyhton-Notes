# Global datas
num_array = []

def find_avarage() -> tuple:
    # Call the global data or datas
    global num_array

    sum = 0
    for i in num_array:
        # Sum all numbers
        sum += i
    
    # The length of array and count of users
    user_count = array_length = len(num_array)

    # Find avarage (if array_length is equal to 0, just return zero)
    result = (sum / array_length) if array_length != 0 else 0

    return (user_count, result)

while True:
    # User input
    user_input = input("> ")

    if user_input == "tamam" or not user_input:
        # Get data from function
        data = find_avarage()

        print(f"Girilen kişi sayısı: {data[0]}, Sonuç: {data[1]}")
        break

    else:
        try:
            # Add number into the array
            num_array.append(int(user_input))

        except:
            print("Lütfen sayı giriniz.")