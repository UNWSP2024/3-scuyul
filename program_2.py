#Griffin Corniea 9/19/25 age classifier

def categorize_age(age):
    ageCategory = "TBD"

    if age <= 1:
        ageCategory = "infant"
    elif age > 1 and age < 13:
        ageCategory = "child"
    elif age >= 13 and age < 20:
        ageCategory = "teenager"
    elif age >= 20:
        ageCategory = "adult"


    return ageCategory


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)