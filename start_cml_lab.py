import argparse
import xmltodict
from virl2_client import ClientLibrary

parser = argparse.ArgumentParser(description="Provide file location of session.xml")
parser.add_argument(
    "file_path",
    type=str,
    help="Provides the location of the session.xml file",
)
args = parser.parse_args()

# Get Session Details to start appropriate CML Lab
with open(args.file_path) as f:
    session_info = xmltodict.parse(f.read())

cml_lab = session_info["session"]["scenario"]["name"]

# Connect to CML using Environment Variables for Authentication
# VIRL2_URL, VIRL2_USER and VIRL2_PASS
client = ClientLibrary(ssl_verify=False)

lab = client.find_labs_by_title(cml_lab)[0]

# If lab is not started start the lab once lab is in started state notify user of Started state.
if lab.state() != "STARTED":
    print(
        f"CML Lab: {lab._title} is Starting please standby, this can take several minutes to complete."
    )
    lab.start()
    # After Lab starts

print(f"CML Lab: {lab._title} is {lab.state()}")
