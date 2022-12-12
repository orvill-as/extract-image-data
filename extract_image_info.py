# Import the exifread module
import exifread

# Prompt user for a path to the image file
image_path = input('Enter the path to the image file: ')

# Open the image file in binary mode
f = open(image_path, 'rb')

# Return Exif tags
tags = exifread.process_file(f)

# Get date and time the image was taken
date_time = tags.get('EXIF DateTimeOriginal')

# Get GPS coordinates (if available)
gps_latitude = tags.get('GPS GPSLatitude')
gps_latitude_ref = tags.get('GPS GPSLatitudeRef')
gps_longitude = tags.get('GPS GPSLongitude')
gps_longitude_ref = tags.get('GPS GPSLongitudeRef')

# Get device make and model
device_make = tags.get('Image Make')
device_model = tags.get('Image Model')

# Print the date and time the image was taken
print('Date and time the image was taken:', date_time)

# Print the GPS coordinates
print('GPS coordinates:', gps_latitude, gps_latitude_ref, gps_longitude, gps_longitude_ref)

# Print the device make and model
print('Device make and model:', device_make, device_model)

# Close image file
f.close()
