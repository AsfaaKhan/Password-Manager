import streamlit as st
import random  # Importing the random library for generating random characters
import string # Importing the string library for using string characters
import re


st.set_page_config(page_title="Password Manager", page_icon="🔐")


st.sidebar.markdown("### Password Manager 🔐\n\n")

user_select_option = st.sidebar.selectbox("\n **Select options:** ", ["Password Strength Checker", "Password Generator Meter"], )


if user_select_option == "Password Generator Meter":
    st.sidebar.markdown("\n **You selected**  ***Password Manager Tool*** **to use the** ***Password Generator Meter*** " )

    st.title(" Password Generator🔐")
    st.markdown("""
                ### Welcome to Ultimate  ***Password Generator Meter*** !👋
                Use this simple tool to generate the Password. This tool **Generate Password** by using alphabets,  digits, special characters .  
                """)

    length = st.slider(" **Select Password Length** ", min_value=9 , max_value=50, value=11)

    use_digits = st.checkbox("**Include Digits**")
    use_special_char = st.checkbox("**Include Special Characters**")

    def generator_password(length,use_digits,use_special_char):
        characters = string.ascii_letters # Includes all letters (a-z)(A-Z)

        if use_digits:
            characters += string.digits # Add numbers (0 - 9) 

        if use_special_char:
            characters += string.punctuation   # Add special characters ( @, $, %, !, *, ^ )

        return ''.join(random.choice(characters) for _ in range(length))  
    
    if st.button("**Generate Password**"):  
        st.slider()
        password = generator_password(length, use_digits,use_special_char)
        st.write(f"**Generated Password:** `{password}`") 
        if not use_special_char and not use_digits:
            st.warning("⚠️  Your Password is weak! Consider adding digits and  special characters for the best security.")
        elif not use_digits:
            st.warning("⚠️  Your Password is weak! Consider adding digits  for the best security.")
        elif not use_special_char:
            st.warning("⚠️  Your Password is weak! Consider adding  special characters for the best security.")
        else :
            st.success("✅ Strong Password!") 
           


### Password Strength Checker
if user_select_option == "Password Strength Checker":
    st.sidebar.markdown("\n **You selected**  ***Password Manager Tool*** **to use the** ***Password Strength Checker*** " )
 
    st.title("🔐Password Strength Checker")
    st.markdown("""
            ### Welcome To ultimate  Password Strength Checker! 👋
            Use this simple tool to check the **Password Strength** of your password and get suggestions on how to make it stronger. We will give you helpful tips to create a **Strong Password**🔒 """)

    # Get User input 
    password2 =st.text_input("Enter Your Password")

    st.button("**Check Password**")
        # st.write("#### Password Suggestion ")
    score = 0

    if password2 :
        st.write("#### ***Password Suggestions:*** ")
        # length Check 
        if len(password2) >= 8:
            score += 1
        else:
            st.write("###### ❌Password should be at least 8 characters long.")    

        # Upper & Lower Case:
        if re.search(r"[A-Z]", password2) and re.search(r"[a-z]", password2):
            score += 1 
        else:
            st.write("###### ❌ Include at Uppercase and Lowercase letters !")
        
        # Digits Check
        if re.search(r"\d",password2):
            score += 1
        else:
            st.write("###### ❌ Add at least one number (0-9)")

        # Special Character Check 
        if re.search(r"[!@#$%^&*]",password2):
            score += 1
        else:
            st.write("###### ❌ Include at least one special character (!@#$%^&*)")

        # Strength Rating 
        if score == 4:
            st.write("###### ✅ Strong Password!")
            st.balloons()
        elif score == 3:
            st.write("###### ⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.markdown(" ###### ❌  Weak Password - Improve it by using the above suggestions!")






# def generator_password(length,use_digits,use_special_char):
#     characters = string.printable # Includes all letters (a-z)(A-Z)

#     if use_digits:
#         characters += string.digits # Add numbers (0 - 9) 

#     if use_special_char:
#         characters += string.punctuation   # Add special characters ( @, $, %, !, *, ^ )

#     return ''.join(random.choice(characters) for _ in range(length))  
 
# st.title("Password Generator 🔐")

# length = st.slider ("Select Password Length ", min_value=9 , max_value=50, value=11)

# use_digits = st.checkbox("Include Digits")
# use_special_char = st.checkbox("Include Special Characters")

# if st.button("Generte Password"):
#     password = generator_password(length, use_digits,use_special_char)
#     st.write(f"Generated Password: `{password}`")


# Password Strength Meter
 

# st.title("🔐Password Strength Checker")
# st.markdown("""
#             ### Welcome To ultimate  Password Strength Checker! 👋
#             Use this simple tool to check the **Password Strength** of your password and get suggestions on how to make it stronger. We will give you helpful tips to create a **Strong Password**🔒 """)

# # Get User input 
# password2 =st.text_input("Enter Your Password")

# if st.button("Check Password"):
#     st.write("Password Suggestion  : `{check_password_Strength}`")

# score = 0

# if password2 :
#     # length Check 
#     if len(password2) >= 8:
#         score += 1
#     else:
#        st.write("❌Password should be at least 8 characters long.")    

#     # Upper & Lower Case:
#     if re.search(r"[A-Z]", password2) and re.search(r"[a-z]", password2):
#         score += 1 
#     else:
#         st.write("❌ Include at Uppercase and Lowercase letters !")
    
#     # Digits Check
#     if re.search(r"\d",password2):
#         score += 1
#     else:
#         st.write("❌ Add at least one number (0-9)")

#     # Special Character Check 
#     if re.search(r"[!@#$%^&*]",password2):
#         score += 1
#     else:
#         st.write("❌ Include at least one special character (!@#$%^&*)")

  


#     # Strength Rating 
#     if score == 4:
#         st.write("✅ Strong Password!")
#     elif score == 3:
#         st.write("⚠️ Moderate Password - Consider adding more security features.")
#     else:
#         st.write("❌ Weak Password - Improve it using the suggestions above.")



st.write ("-"*50)   
st.write("Made With 💛 by [Asfaa Khan](https://github.com/AsfaaKhan)")