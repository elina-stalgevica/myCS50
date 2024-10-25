def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))

# If you are not sure wether dictionaire has a specific key, you can type - Model" {spacecraft.get("model", "Unknown")}
# Get will help you to find it, but if it does not exist return Unknown

def create_report(spacecraft):
    return f"""
   ======== REPORT ========

   Name: {spacecraft["name"]}
   Distance: {spacecraft["distance"]} AU
   Model: {spacecraft.get("model", "Unknown")}

   ========================
   """

main()
