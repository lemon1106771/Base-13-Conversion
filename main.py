# A small excerside to convert decimal numbers to base 13 
def convertToBase13(decimal):
  base13Digits = "0123456789ABC"
  decimal = int(decimal)
  base13 = ""
  if decimal == 0:
    return "0"
  is_negative = decimal < 0 # Check for negative numbers
  if is_negative:
    decimal = -decimal
  while decimal > 0:  # Convert to base 13
    remainder = decimal % 13    # Get the remainder
    base13 = base13Digits[remainder] + base13 # lookup the base 13 digit and sum it to the result
    decimal //= 13  # Divide the decimal value by 13 
  if is_negative:
    base13 = "-" + base13
  return base13
# Test the function
print(convertToBase13(169))  # Expected output: "100"
print(convertToBase13(0))    # Expected output: "0"