def main():
    user_time = input("What time is it? ")
    updated_user_time = convert(user_time)
    if 7 <= updated_user_time <=8:
        print("breakfast time")
    elif 12 <= updated_user_time <= 13:
        print("lunch time")
    elif 18 <= updated_user_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    time_as_needed = hours + minutes/60
    return time_as_needed

if __name__ == "__main__":
    main()