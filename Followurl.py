import requests

def follow_redirects(url, depth=0):
  """
  Recursively follows redirects from a URL and logs them to a text file, 
  with a maximum recursion depth.

  Args:
      url: The starting URL to follow.
      depth (int, optional): The current recursion depth. Defaults to 0.

  Returns:
      A list of all the URLs encountered during redirection.
  """
  if depth >= 10:
    print("Maximum recursion depth reached, stopping...")
    return []
  urls = [url]
  while True:
    response = requests.get(url, allow_redirects=False)
    if response.status_code in (301, 302, 303):
      new_url = response.headers.get("Location")
      urls.append(new_url)
      url = new_url
      urls.extend(follow_redirects(new_url, depth + 1))  # Recursive call with depth increment
    else:
      break
  return urls

def save_to_file(urls, filename):
  """
  Saves a list of URLs to a text file.

  Args:
      urls: A list of URLs to save.
      filename: The name of the file to save to.
  """
  with open(filename, "w") as f:
    f.write("\n".join(urls))

def main():
  """
  Prompts the user for a URL, follows all redirects (up to 10), and saves them to a file.
  """
  url = input("Enter a URL: ")
  urls = follow_redirects(url)
  filename = "redirection_log.txt"
  save_to_file(urls, filename)
  print(f"Redirections logged to {filename}")

if __name__ == "__main__":
  main()
