"""A Simple Script for Extracting Data from a Webpage
This script allows the user to extract data from a webapge and then export the data to a csv file with column(s).
"""

def get_ips(html_path):
  html_file = html_path
  with open(html_file, "r") as fp:
    lines = fp.readlines()

  login = "error"
  for line in lines:
    if "window.LOGINUID" in line:
      login = line.split("'")[1]
      break

  if login == "error":
    print("Wrong HTML File")

  target_string = "ssh://" + login + "@"
  address_list = []
  for line in lines:
    if target_string in line:
      address = line.split('@')[1].split(':')[0]
      address_list.append(address)

  return address_list

def main():
  html_file = r"C:\Users\Jagan\Downloads\exp.html"
  address_list = get_ips(html_file)
  print(address_list)

if __name__ == "__main__":
    main()