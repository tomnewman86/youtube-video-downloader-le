from pytube import YouTube
import csv
import os

print(
        '''
	############################################################
	#                                                          #
	# YouTube Video Downloader                                 #
	#                                                          #
	# This python script can be used by law enforcement to     #
	# capture YT videos and exhibit them                       #
	#                                                          #
	# The exhibit reference and video metadata will be         #
	# captured in a csv file                                   #   
    #                                                          #
	#                                                           #
	# Author: Tom Newman                                       #
	#                                                          #
	# Support: tom.newman@ofcom.org.uk                         #
	#                                                          #
	#                                                          #
	############################################################
	
	''')

# Enter case reference
case_ref = input("Please enter a case reference: ")

# Create a new directory for files
path = os.getcwd()
os.mkdir(path + "/" + case_ref + "-" + "YouTube Data")

# Change into directory
os.chdir(path + "/" + case_ref + "-" + "YouTube Data")
path = os.getcwd()

# Create CSV log file
outfile = open(
    path + '/video_log.csv', 'w', newline='')
writer = csv.writer(outfile)
writer.writerow(["Exh Ref", "Title", "No. Of Views",
                 "Length of Video", "Description", "Ratings", "Date Published", "Source"])

# Download YT videos and log data to csv
trigger_end = 0

while trigger_end == 0:
    exh_ref = input("Please enter an Exhibit Reference: " + "\n")

    link = input("Please enter the full Youtube link: " + "\n")

    yt = YouTube(link)

    writer.writerow([exh_ref, yt.title, yt.views, yt.length,
                     yt.description, yt.rating, yt.publish_date, link])

    ys = yt.streams.get_highest_resolution()

    print("Downloading " + yt.title + "\n")
    ys.download(path)
    print("+++ Downloading complete +++" + "\n")
    os.rename(path + "/" +
              ys.default_filename, path + "/" + exh_ref + '.mp4')
    dl_more = input(
        "Do you want to download another video? (please enter Y or N) ")
    if dl_more == 'Y':
        trigger_end = 0
    else:
        trigger_end = 1
