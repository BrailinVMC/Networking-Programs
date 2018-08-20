#########################################################################
# VERIFY FUNCTIONS
#########################################################################
# Check if the string provided is a valid IPv4 Address.
def verify_IPv4(ipv4):
    # Convert ipv4 to a string if possible.
    try:
        ipv4 = str(ipv4)
    except:
        # Return false if not possible.
        return False
        
    # Split the ipv4 string using '.' as the delimiter.
    ip_octet_list = ipv4.split('.')

    # Check the size of the ip_octet_list.
    if len(ip_octet_list) != 4:
        # Return false if there are not 4 octets.
        return False
        
    # Check that each octet is valid.
    else:
        for octet in ip_octet_list:
            # Check that each octet is an integer between 0 and 255.
            try:
                # Check if the octet is an integer.
                check = int(octet)

                # Check if octet is between 0 and 255.
                if (check < 0 or check > 255):
                    # Return false for octets out of range.
                    return False
            except:
                # Return false if an octet is not an integer.
                return False
    # Return true if the string defines a valid IPv4 Address.
    return True
