Follow me @SudoJvck

SNMP_Jvck -

This python script can poll network devices using SNMP and extract useful information such as interface status, cpu usage, and memory usage.


Requirements:

-Must have pysnmp library installed.

- pip install pysnmp


Common Issues:

- SNMP MUST BE CONFIGURED/ENABLED ON THE TARGET DEVICE.

- OIDs can vary depending on the device's manufacturer and model, so it's important to consult the device's documentation or contact the manufacturer for a list of available OIDs. 

- Verify that the version of SNMP running on the device is compatible with the version of the pysnmp library you're using.

- Ensure that your firewall and security rules are configured to allow SNMP traffic.


How it works (If you care.):

This script uses the bulkCmd() function provided by the pysnmp library to perform an SNMP GETBULK request for all the OIDs in the list, it retrieves the value of all OIDs in the list and prints them in a human-readable format.

The bulkCmd() function is similar to the getCmd() function, the only difference is that it retrieves multiple values at once. The bulkCmd() function takes as input the SNMP engine, the community string, the IP address and port of the target device, the context, the non-repeaters, the max-repetitions, the OID, and a flag to set the lexicographicMode.

The script then checks for any error in the response. If an error is found, it will print the error message. If there is no error, it will extract the value of all the OIDs from the response and print it in a human-readable format.

You can also add other OIDs as per your requirement, and also you can add the exception handling and other functionalities as per your requirements.


Follow me @SudoJvck
