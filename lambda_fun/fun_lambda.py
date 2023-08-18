# lambda function

def downloadfile(url):
  print("establish connection" + url)
  print("open connection" + url)
  print("download data")
  print("close connection" + url)

downloadfile("ftb://www.abc.org.com ")
#     downloadfile("ftb://www.xyz.com")
#     downloadfile("ftb://www.url.com")