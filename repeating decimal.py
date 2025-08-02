"""Write a program (Preferable Python) to calculate the repeating decimal expansion of the following 
five fractions using the Vedic Sutra 'Ekādhikena Pūrvena' logic."""

def get_repeating_part(denominator):
    result = ''               # This will store the decimal digits as a string
    remainders = {}           # Dictionary to store previously seen remainders and their positions
    remainder = 1             # Start with numerator = 1 (as we are computing 1/denominator)
    pos = 0                   # Position index for digits in result

    while True:
        remainder *= 10       # Bring down a zero like in manual division
        digit = remainder // denominator  # Get the next digit of the result
        remainder %= denominator          # Update the remainder

        if remainder == 0:
            # If remainder becomes zero, the decimal terminates
            return result, ''  # No repeating part

        if remainder in remainders:
            # If this remainder has been seen before, a repeating cycle is detected
            start = remainders[remainder]   # Get the index where this remainder was first seen
            return result[:start], result[start:]  # Split result into non-repeating and repeating parts

        # Store the position of the current remainder
        remainders[remainder] = pos
        result += str(digit)  # Append the digit to the result string
        pos += 1

# Function to print the decimal expansion of 1/denominator in a readable form
def print_decimal_expansion(denominator):
    non_repeat, repeat = get_repeating_part(denominator)
    if repeat:
        # If there's a repeating part, enclose it in parentheses
        print(f"1/{denominator} = 0.{non_repeat}({repeat})")
    else:
        # If no repeating part, just print the decimal
        print(f"1/{denominator} = 0.{non_repeat}")

# Apply the function to a list of denominators ending in 9
# These are typically good candidates for the Vedic Sutra 'Ekādhikena Pūrvena'
# Which suggests using 'one more than the previous' (e.g., 1/19 → use 2)
for d in [19, 29, 39, 49, 59]:
    print_decimal_expansion(d)

"""O/P
1/19 = 0.(052631578947368421)
1/29 = 0.(0344827586206896551724137931)
1/39 = 0.(025641)
1/49 = 0.(020408163265306122448979591836734693877551)
1/59 = 0.(0169491525423728813559322033898305084745762711864406779661)
""" 
