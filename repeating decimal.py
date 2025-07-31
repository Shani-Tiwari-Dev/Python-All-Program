"""Write a program (Preferable Python) to calculate the repeating decimal expansion of the following
five fractions using the Vedic Sutra 'Ekādhikena Pūrvena' logic."""

def get_repeating_part(denominator):
    result = ''
    remainders = {}
    remainder = 1
    pos = 0

    while True:
        remainder *= 10
        digit = remainder // denominator
        remainder %= denominator

        if remainder == 0:
            return result, ''  # Terminates, no repeat

        if remainder in remainders:
            start = remainders[remainder]
            return result[:start], result[start:]  # Non-repeating, repeating

        remainders[remainder] = pos
        result += str(digit)
        pos += 1

def print_decimal_expansion(denominator):
    non_repeat, repeat = get_repeating_part(denominator)
    if repeat:
        print(f"1/{denominator} = 0.{non_repeat}({repeat})")
    else:
        print(f"1/{denominator} = 0.{non_repeat}")

# List of denominators
for d in [19, 29, 39, 49, 59]:
    print_decimal_expansion(d)
