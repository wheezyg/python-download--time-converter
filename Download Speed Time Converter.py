print ("Download time Calculator")

speed = float(input("enter your download speed (mbps)"))

file_type = str(input("File Megabyte (MB) or Gigabyte (GB)"))

size = float(input("enter file size"))

formula = size * 1000 * 8 / speed

formula2 = formula / 60

formula3 = formula2 / 60

mbformula = size * 8 / speed

mbformula2 = mbformula / 60

mbformula3 = mbformula2 / 60





while speed:
    if file_type == "GB" or file_type == "gb":
        print (formula, "seconds")
        print (formula2, "minutes")
        print (formula3, "hours")
        speed = float(input("enter your download speed (mbps)"))
        file_type = str(input("File Megabyte (MB) or Gigabyte (GB)"))
        size = float(input("enter file size"))
    if file_type == "MB" or file_type == "mb":
        print (mbformula, "seconds")
        print (mbformula2, "minutes")
        print (mbformula3, "hours")
        speed = float(input("enter your download speed (mbps)"))
        file_type = str(input("File Megabyte (MB) or Gigabyte (GB)"))
        size = float(input("enter file size"))
        
        


    










