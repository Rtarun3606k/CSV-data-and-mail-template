import csv

def extract_data(source_file, destination_file):
    # Define the field names to extract from the source CSV file
    field_names = ['Name','Body','Subject', 'Status', 'To','Attach']  # Adjust this list as per your CSV file structure
    
    # Open the source CSV file in 'read' mode
    with open(source_file, 'r', newline='') as source:
        reader = csv.DictReader(source)
        
        # Open the destination CSV file in 'write' mode
        with open(destination_file, 'w', newline='') as destination:
            writer = csv.DictWriter(destination, fieldnames=field_names)
            writer.writeheader()  # Write the header row
            
            # Iterate through each row in the source file
            for row in reader:
                event="event name" #event name
                name=row['Name']
                ambassador="ambassador name" #ambassador name
                sub=f"Congratulations {row['Name']}"
                files=f"{row['Name']}.pdf"
                coustomestr=f"""

Thank you for your participation in the {event}!

Dear {name},
Thank you so much for your interest in being a part of the {event} program.
We appreciate your time and effort in completing the program.
This email contains your certificate of participation.
Please feel free to reply back to this email should you have any questions.
Looking forward to seeing you further programs,
{ambassador}, Microsoft Learn Student Ambassadors."""
                # Extract the required fields and write them to the destination file
                if row['Name']!=" ":
                    writer.writerow({'Name': row['Name'], 'To': row['Email'],'Body': coustomestr,'Status':"Send",'Subject':sub,'Attach':files})  # Adjust field names as needed

# Example usage:
source_file = 'data.csv' #sourse file which contains participants data
destination_file = 'destination.csv' #file where the data should be written
extract_data(source_file, destination_file)
