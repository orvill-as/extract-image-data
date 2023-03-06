import exifread

image_path = input('Enter the path to the image file: ')

f = open(image_path, 'rb')

tags = exifread.process_file(f)

date_time = tags.get('EXIF DateTimeOriginal')

gps_latitude = tags.get('GPS GPSLatitude')
gps_latitude_ref = tags.get('GPS GPSLatitudeRef')
gps_longitude = tags.get('GPS GPSLongitude')
gps_longitude_ref = tags.get('GPS GPSLongitudeRef')

device_make = tags.get('Image Make')
device_model = tags.get('Image Model')

print('Date and time the image was taken:', date_time)

print('GPS coordinates:', gps_latitude, gps_latitude_ref, gps_longitude, gps_longitude_ref)

print('Device make and model:', device_make, device_model)

f.close()
