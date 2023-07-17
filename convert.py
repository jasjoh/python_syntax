def convert_temp(unit_in, unit_out, temp):
    """Convert fahrenheit <-> celsius and return results.

    - unit_in: either "f" or "c"
    - unit-out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    # c=>f c*9/5 +32
    # f=>c (f-32) *5/9
    def _f_to_c(f):
        """converts farenheit to centigrade"""
        return (f-32)*5/9

    def _c_to_f(c):
        """converts centigrade to farenheit"""
        return c*(9/5) + 32

    def _is_c_or_f(unit):
        """Returns true if the unit is 'c' or 'f' """
        if unit=="c" or unit == "f":
            return True
        else:
            return False

    if not _is_c_or_f(unit_in):
        return f"Invalid unit {unit_in}"

    if not _is_c_or_f(unit_out):
        return f"Invalid unit {unit_out}"


    if unit_in == "c":
        if unit_out == "c":
            return temp
        elif unit_out =="f":
            return _c_to_f(temp)
    else:
        if unit_out =="f":
            return temp
        else:
            return _f_to_c(temp)


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")
