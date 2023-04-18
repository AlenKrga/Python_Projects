# collect email from user
# split the email using the @, the first part as the username, the second part is gonna be  saved as domain
# split the domain using "." .

def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("Input your email address: ")

# Split the email address into two parts: the username and the domain
    (username, domain) = email_input.split("@")
# Split the domain part of the email address into two parts: the domain name and the extension 
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain : ", domain)
    print("Extension: ", extension)

while True:
    main()