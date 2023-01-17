Follow me @SudoJvck

SNMP_Jvck -

This python script can poll network devices using SNMP and extract useful information such as interface status, cpu usage, and memory usage.


How it works:

This script uses the pysnmp library to create a SNMP session, send SNMP GET requests to retrieve the interface status, CPU usage, and memory usage using the specified OIDs, and extract the values from the response. Then it prints the results.


Requirements:

-Must have pysnmp library installed.

- pip install pysnmp




Common Issues:

- SNMP MUST BE CONFIGURED/ENABLED ON THE TARGET DEVICE.

- The SNMP community string used in the script may not match the community string configured on the device. Double-check the community string and ensure that it matches the correct value on the device. (USER ID/PW)

- This script uses the SNMP OIDs for CISCO devices, you might have to change the OIDs according to the device you are trying to poll. Double-check the OIDs and ensure that they match the correct values for the device.

- Verify that the version of SNMP running on the device is compatible with the version of the pysnmp library you're using.

- Ensure that your firewall and security rules are configured to allow SNMP traffic.




Follow me @SudoJvck
