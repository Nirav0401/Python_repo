import qrcode
import re

def generate_upi_qr(upi_id_or_phone, name="Recipient Name", amount="1000", currency="INR"):

    # Check if the input is a phone number (10 digits)
    if re.match(r'^\d{10}$', upi_id_or_phone):
        # Format phone number as a UPI ID with the suffix (use a standard UPI suffix for phone numbers)
        upi_id = f"{upi_id_or_phone}@ybl"  # Adjust "@upi" if needed by provider
    else:
        # input is a UPI ID
        upi_id = upi_id_or_phone
    
    # recipient name for URL (replacing spaces with %20)
    recipient_name = name.replace(" ", "%20")

    # Define the UPI URL for payment
    upi_url = f"upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu={currency}"

    # Generate the QR code
    upi_qr = qrcode.make(upi_url)

    # Save and show the QR code
    upi_qr.save("upi_qr.png")
    upi_qr.show()
    print("QR code saved as 'upi_qr.png'")

# user input for UPI ID or phone number
user_input = input("Enter UPI ID or Phone Number: ")
generate_upi_qr(user_input, "Nirav Prajapati")